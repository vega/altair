from __future__ import annotations

import ast
import subprocess
import sys
import textwrap
from importlib.util import find_spec
from itertools import chain
from pathlib import Path
from typing import Iterable, Literal


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


if sys.version_info >= (3, 9):

    def unparse(obj: ast.AST, /) -> str:
        return ast.unparse(obj)  # type: ignore
else:

    def unparse(obj: ast.AST, /) -> str:
        """
        Added in ``3.9``.

        https://docs.python.org/3/library/ast.html#ast.unparse
        """
        # HACK: Will only be used during build/docs
        # - This branch is just to satisfy linters
        return "<ast.unparse() UNAVAILABLE>"


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
    mod = parse_module(module_name)
    fn = find_func_def(mod, func_name)
    body, ret = validate_body(fn)
    it = chain((unparse(node) for node in body), ["", unparse(ret)])
    s = ruff_format_str(it, trailing_comma=False) if format else "\n".join(it)
    if output == "str":
        return s
    else:
        return f".. {output}::\n\n{textwrap.indent(s, ' ' * 4)}\n"


def ruff_format_str(
    code: str | Iterable[str], /, *, trailing_comma: bool = True
) -> str:
    # NOTE: Brought this back w/ changes after removing in #3536
    if not isinstance(code, str):
        code = "\n".join(code)
    encoded = code.encode()

    cmd = ["ruff", "format", "--stdin-filename", "placeholder.py"]
    if not trailing_comma:
        cmd.extend(("--config", "format.skip-magic-trailing-comma = true"))

    r = subprocess.run(cmd, input=encoded, check=True, capture_output=True)
    return r.stdout.decode()
