# ruff: noqa: D418
from __future__ import annotations

import ast
import subprocess
import sys
import textwrap
import warnings
from ast import unparse
from collections import deque
from collections.abc import Iterable
from importlib.util import find_spec
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeVar, overload

if sys.version_info >= (3, 12):
    from typing import Protocol, TypeAliasType
else:
    from typing_extensions import Protocol, TypeAliasType

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString

    from collections.abc import Iterator
    from typing import ClassVar, Literal


__all__ = ["extract_func_def", "extract_func_def_embed", "ruff", "ruff_inline_docs"]

T = TypeVar("T")
OneOrIterV = TypeAliasType(
    "OneOrIterV",
    "T | Iterable[T] | Iterable[OneOrIterV[T]]",
    type_params=(T,),
)
_Code = OneOrIterV[str]


def parse_module(name: str, /) -> ast.Module:
    """
    Find absolute path and parse module into an ast.

    Use regular dotted import style, no `.py` suffix.

    Acceptable ``name``:

        altair.package.subpackage.etc
        tools.____
        tests.____
        doc.____
        sphinxext.____
    """
    if (spec := find_spec(name)) and (origin := spec.origin):
        return ast.parse(Path(origin).read_bytes())
    else:
        raise FileNotFoundError(name)


def find_func_def(mod: ast.Module, fn_name: str, /) -> ast.FunctionDef:
    """
    Return a function node matching ``fn_name``.

    Notes
    -----
    Provides some extra type safety, over::

        ast.Module.body: list[ast.stmt]
    """
    for stmt in mod.body:
        if isinstance(stmt, ast.FunctionDef) and stmt.name == fn_name:
            return stmt
        else:
            continue
    msg = f"Found no function named {fn_name!r}"
    raise NotImplementedError(msg)


def validate_body(fn: ast.FunctionDef, /) -> tuple[list[ast.stmt], ast.expr]:
    """
    Ensure function has inlined imports and a return statement.

    Returns::

        (ast.FunctionDef.body[:-1], ast.Return.value)
    """
    body = fn.body
    first = body[0]
    if not isinstance(first, (ast.Import, ast.ImportFrom)):
        msg = (
            f"First statement in function must be an import, "
            f"got {type(first).__name__!r}\n\n"
            f"{unparse(first)!r}"
        )
        raise TypeError(msg)
    last = body.pop()
    if not isinstance(last, ast.Return) or last.value is None:
        body.append(last)
        msg = (
            f"Last statement in function must return an expression, "
            f"got {type(last).__name__!r}\n\n"
            f"{unparse(last)!r}"
        )
        raise TypeError(msg)
    else:
        return body, last.value


def iter_flatten(*elements: _Code) -> Iterator[str]:
    for el in elements:
        if not isinstance(el, str) and isinstance(el, Iterable):
            yield from iter_flatten(*el)
        elif isinstance(el, str):
            yield el
        else:
            msg = (
                f"Expected all elements to eventually flatten to ``str``, "
                f"but got: {type(el).__name__!r}\n\n"
                f"{el!r}"
            )
            raise TypeError(msg)


def iter_func_def_unparse(
    module_name: str,
    func_name: str,
    /,
    *,
    return_transform: Literal["assign"] | None = None,
    assign_to: str = "chart",
) -> Iterator[str]:
    # Planning to add pyscript code before/after
    # Then add `ruff check` to clean up duplicate imports (on the whole thing)
    # Optional: assign the return to `assign_to`
    #   - Allows writing modular code that doesn't depend on the variable names in the original function
    mod = parse_module(module_name)
    fn = find_func_def(mod, func_name)
    body, ret = validate_body(fn)
    for node in body:
        yield unparse(node)
    yield ""
    ret_value = unparse(ret)
    if return_transform is None:
        yield ret_value
    elif return_transform == "assign":
        yield f"{assign_to} = {ret_value}"
    else:
        msg = f"{return_transform=}"
        raise NotImplementedError(msg)


def extract_func_def(
    module_name: str,
    func_name: str,
    *,
    format: bool = True,
    output: Literal["altair-plot", "code-block", "str"] = "str",
) -> str:
    """
    Extract the contents of a function for use as a code block.

    Parameters
    ----------
    module_name
        Absolute, dotted import style.
    func_name
        Name of function in ``module_name``.
    format
        Run through ``ruff format`` before returning.
    output
        Optionally, return embedded in an `rst` directive.

    Notes
    -----
    - Functions must define all imports inline, to ensure they are propagated
    - Must end with a single return statement

    Warning
    -------
    Requires ``python>=3.9`` for `ast.unparse`_

    Examples
    --------
    Transform the contents of a function into a code block::

        >>> extract_func_def("tests.altair_theme_test", "alt_theme_test", output="code-block") # doctest: +SKIP

    .. _ast.unparse:
        https://docs.python.org/3.9/library/ast.html#ast.unparse
    """
    if output not in {"altair-plot", "code-block", "str"}:
        raise TypeError(output)
    it = iter_func_def_unparse(module_name, func_name)
    s = ruff_inline_docs.format(it) if format else "\n".join(it)
    if output == "str":
        return s
    else:
        return f".. {output}::\n\n{textwrap.indent(s, ' ' * 4)}\n"


def extract_func_def_embed(
    module_name: str,
    func_name: str,
    /,
    before: _Code | None = None,
    after: _Code | None = None,
    assign_to: str = "chart",
    indent: int | None = None,
) -> str:
    """
    Extract the contents of a function, wrapping with ``before`` and ``after``.

    The resulting code block is run through ``ruff`` to deduplicate imports
    and apply consistent formatting.

    Parameters
    ----------
    module_name
        Absolute, dotted import style.
    func_name
        Name of function in ``module_name``.
    before
        Code inserted before ``func_name``.
    after
        Code inserted after ``func_name``.
    assign_to
        Variable name to use as the result of ``func_name``.

        .. note::
            Allows the ``after`` block to use a consistent reference.
    indent
        Optionally, prefix ``indent * " "`` to final block.

        .. note::
            Occurs **after** formatting, will not contribute to line length wrap.
    """
    if before is None and after is None:
        msg = (
            f"At least one additional code fragment should be provided, but:\n"
            f"{before=}, {after=}\n\n"
            f"Use {extract_func_def.__qualname__!r} instead."
        )
        warnings.warn(msg, UserWarning, stacklevel=2)
    unparsed = iter_func_def_unparse(
        module_name, func_name, return_transform="assign", assign_to=assign_to
    )
    parts = [p for p in (before, unparsed, after) if p is not None]
    formatted = ruff_inline_docs(parts)
    return textwrap.indent(formatted, " " * indent) if indent else formatted


class CodeMod(Protocol):
    def __call__(self, *code: _Code) -> str:
        """
        Transform some input into a single block of modified code.

        Parameters
        ----------
        *code
            Arbitrarily nested code fragments.
        """
        ...

    def _join(self, code: _Code, *, sep: str = "\n") -> str:
        """
        Concatenate any number of code fragments.

        All nested groups are unwrapped into a flat iterable.
        """
        return sep.join(iter_flatten(code))


class Ruff(CodeMod):
    """
    Run `ruff`_ commands against code fragments or files.

    By default, uses the same config as `pyproject.toml`_.

    Parameters
    ----------
    *extend_select
        `rule codes`_ to use **on top of** the default config.
    ignore
        `rule codes`_ to `ignore`_.
    skip_magic_trailing_comma
        Enables `skip-magic-trailing-comma`_ during formatting.

        .. note::

            Only use on code that is changing indent-level
            (e.g. unwrapping function contents).

    .. _ruff:
        https://docs.astral.sh/ruff/
    .. _pyproject.toml:
        https://github.com/vega/altair/blob/main/pyproject.toml
    .. _rule codes:
        https://docs.astral.sh/ruff/rules/
    .. _ignore:
        https://docs.astral.sh/ruff/settings/#lint_ignore
    .. _skip-magic-trailing-comma:
        https://docs.astral.sh/ruff/settings/#format_skip-magic-trailing-comma
    """

    _stdin_args: ClassVar[tuple[LiteralString, ...]] = (
        "--stdin-filename",
        "placeholder.py",
    )
    _check_args: ClassVar[tuple[LiteralString, ...]] = ("--fix",)

    def __init__(
        self,
        *extend_select: str,
        ignore: OneOrIterV[str] | None = None,
        skip_magic_trailing_comma: bool = False,
    ) -> None:
        self.check_args: deque[str] = deque(self._check_args)
        self.format_args: deque[str] = deque()
        for c in extend_select:
            self.check_args.extend(("--extend-select", c))
        if ignore is not None:
            self.check_args.extend(
                ("--ignore", ",".join(s for s in iter_flatten(ignore)))
            )
        if skip_magic_trailing_comma:
            self.format_args.extend(
                ("--config", "format.skip-magic-trailing-comma = true")
            )

    def write_lint_format(self, fp: Path, code: _Code, /) -> None:
        """
        Combined steps of writing, `ruff check`, `ruff format`.

        Parameters
        ----------
        fp
            Target file to write to
        code
            Some (potentially) nested code fragments.

        Notes
        -----
        - `fp` is written to first, as the size before formatting will be the smallest
        - Better utilizes `ruff` performance, rather than `python` str and io
        """
        self.check(fp, code)
        self.format(fp)

    @overload
    def check(self, *code: _Code, decode: Literal[True] = ...) -> str:
        """Fixes violations and returns fixed code."""

    @overload
    def check(self, *code: _Code, decode: Literal[False]) -> bytes:
        """
        ``decode=False`` will return as ``bytes``.

        Helpful if piping to another command.
        """

    @overload
    def check(self, _write_to: Path, /, *code: _Code) -> None:
        """
        ``code`` is joined, written to provided path and then checked.

        No input returned.
        """

    def check(self, *code: Any, decode: bool = True) -> str | bytes | None:
        """
        Check and fix ``ruff`` rule violations.

        All cases will join ``code`` to a single ``str``.
        """
        base = "ruff", "check"
        if isinstance(code[0], Path):
            fp = code[0]
            fp.write_text(self._join(code[1:]), encoding="utf-8")
            subprocess.run((*base, fp, *self.check_args), check=True)
            return None
        r = subprocess.run(
            (*base, *self.check_args, *self._stdin_args),
            input=self._join(code).encode(),
            check=True,
            capture_output=True,
        )
        return r.stdout.decode() if decode else r.stdout

    @overload
    def format(self, *code: _Code) -> str:
        """Format arbitrarily nested input as a single block."""

    @overload
    def format(self, _target_file: Path, /, *code: None) -> None:
        """
        Format an existing file.

        Running on `win32` after writing lines will ensure ``LF`` is used, and not ``CRLF``:

            ruff format --diff --check _target_file
        """

    @overload
    def format(self, _encoded_result: bytes, /, *code: None) -> str:
        """Format the raw result of ``ruff.check``."""

    def format(self, *code: Any) -> str | None:
        """
        Format some input code, or an existing file.

        Returns decoded result unless formatting an existing file.
        """
        base = "ruff", "format"
        if len(code) == 1 and isinstance(code[0], Path):
            subprocess.run((*base, code[0], *self.format_args), check=True)
            return None
        encoded = (
            code[0]
            if len(code) == 1 and isinstance(code[0], bytes)
            else self._join(code).encode()
        )
        r = subprocess.run(
            (*base, *self.format_args, *self._stdin_args),
            input=encoded,
            check=True,
            capture_output=True,
        )
        return r.stdout.decode()

    def __call__(self, *code: _Code) -> str:
        return self.format(self.check(code, decode=False))


ruff_inline_docs = Ruff(
    ignore=("E711", "F821", "E402", "B018"), skip_magic_trailing_comma=True
)
ruff = Ruff()
