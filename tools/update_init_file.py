"""Updates the attribute __all__ in altair/__init__.py based on the updated Altair schema."""

from __future__ import annotations

import typing as t
import typing_extensions as te
from importlib import import_module as _import_module
from importlib.util import find_spec as _find_spec
from inspect import getattr_static, ismodule
from pathlib import Path
from typing import TYPE_CHECKING, Iterable, Iterator

from tools.codemod import ruff

_TYPING_CONSTRUCTS: set[t.Any] = {
    te.TypeAlias,
    t.TypeVar,
    t.cast,
    t.overload,
    te.runtime_checkable,
    t.List,
    t.Dict,
    t.Tuple,
    t.Any,
    t.Literal,
    t.Union,
    t.Iterable,
    t.Protocol,
    te.Protocol,
    t.Sequence,
    t.IO,
    annotations,
    te.Required,
    te.TypedDict,
    t.TypedDict,
    te.Self,
    te.deprecated,
    te.TypeAliasType,
}

DYNAMIC_ALL: tuple[te.LiteralString, ...] = ("altair.vegalite.v5",)


def update__all__variable() -> None:
    """
    Updates the __all__ variable to all relevant attributes of top-level Altair.

    This is for example useful to hide deprecated attributes from code completion in
    Jupyter.
    """
    # Read existing file content
    import altair as alt

    init_path = normalize_source("altair")
    lines = extract_lines(init_path, strip_chars="\n")

    # Find first and last line of the definition of __all__
    first_definition_line = None
    last_definition_line = None
    for idx, line in enumerate(lines):
        if line.startswith("__all__ ="):
            first_definition_line = idx
        elif first_definition_line is not None and line.startswith("]"):
            last_definition_line = idx
            break
    assert first_definition_line is not None
    assert last_definition_line is not None

    # Put file back together, replacing old definition of __all__ with new one, keeping
    # the rest of the file as is
    new_lines = [
        *lines[:first_definition_line],
        f"__all__ = {relevant_attributes(alt.__dict__)}",
        *lines[last_definition_line + 1 :],
    ]
    # Write new version of altair/__init__.py
    # Format file content with ruff
    ruff.write_lint_format(init_path, new_lines)

    for source in DYNAMIC_ALL:
        print(f"Updating `__all__`\n " f"{source!r}\n  ->{normalize_source(source)!s}")
        update_dynamic__all__(source)


def relevant_attributes(namespace: dict[str, t.Any], /) -> list[str]:
    """
    Figure out which attributes in `__all__` are relevant.

    Returns an alphabetically sorted list, to insert into `__all__`.

    Parameters
    ----------
    namespace
        A module dict, like `altair.__dict__`
    """
    from altair.vegalite.v5.schema import _typing

    # NOTE: Exclude any `TypeAlias` that were reused in a runtime definition.
    # Required for imports from `_typing`, outside of a `TYPE_CHECKING` block.
    _TYPING_CONSTRUCTS.update(
        (
            v
            for k, v in _typing.__dict__.items()
            if (not k.startswith("__")) and _is_hashable(v)
        )
    )
    it = (
        name
        for name, attr in namespace.items()
        if (not name.startswith("_")) and _is_relevant(attr, name)
    )
    return sorted(it)


def _is_hashable(obj: t.Any) -> bool:
    """Guard to prevent an `in` check occuring on mutable objects."""
    try:
        return bool(hash(obj))
    except TypeError:
        return False


def _is_relevant(attr: t.Any, name: str, /) -> bool:
    """Predicate logic for filtering attributes."""
    if (
        getattr_static(attr, "_deprecated", False)
        or attr is TYPE_CHECKING
        or (_is_hashable(attr) and attr in _TYPING_CONSTRUCTS)
        or name in {"pd", "jsonschema"}
        or getattr_static(attr, "__deprecated__", False)
    ):
        return False
    elif ismodule(attr):
        # Only include modules which are part of Altair. This excludes built-in
        # modules (they do not have a __file__ attribute), standard library,
        # and third-party packages.
        return getattr_static(attr, "__file__", "").startswith(str(Path.cwd()))
    else:
        return True


def _retrieve_all(name: str, /) -> list[str]:
    """Import `name` and return a defined ``__all__``."""
    found = _import_module(name).__all__
    if not found:
        msg = (
            f"Expected to find a populated `__all__` for {name!r},\n"
            f"but got: {found!r}"
        )
        raise AttributeError(msg)
    return found


def normalize_source(src: str | Path, /) -> Path:
    """
    Return the ``Path`` representation of a module/package.

    Returned unchanged if already a ``Path``.
    """
    if isinstance(src, str):
        if src == "altair" or src.startswith("altair."):
            if (spec := _find_spec(src)) and (origin := spec.origin):
                src = origin
            else:
                raise ModuleNotFoundError(src, spec)
        return Path(src)
    else:
        return src


def extract_lines(fp: Path, /, strip_chars: str | None = None) -> list[str]:
    """Return all lines in ``fp`` with whitespace stripped."""
    with Path(fp).open(encoding="utf-8") as f:
        lines = f.readlines()
        if not lines:
            msg = f"Found no content when reading lines for:\n{lines!r}"
            raise NotImplementedError(msg)
    return [line.strip(strip_chars) for line in lines]


def _normalize_import_lines(lines: Iterable[str]) -> Iterator[str]:
    """
    Collapses file content to contain one line per import source.

    Preserves only lines **before** an existing ``__all__``.
    """
    it: Iterator[str] = iter(lines)
    for line in it:
        if line.endswith("("):
            line = line.rstrip("( ")
            for s_line in it:
                if s_line.endswith(","):
                    line = f"{line} {s_line}"
                elif s_line.endswith(")"):
                    break
                else:
                    NotImplementedError(f"Unexpected line:\n{s_line!r}")
            yield line.rstrip(",")
        elif line.startswith("__all__"):
            break
        else:
            yield line


def process_lines(lines: Iterable[str], /) -> Iterator[str]:
    """Normalize imports, follow ``*``(s), reconstruct `__all__``."""
    _all: set[str] = set()
    for line in _normalize_import_lines(lines):
        if line.startswith("#") or line == "":
            yield line
        elif "import" in line:
            origin_stmt, members = line.split(" import ", maxsplit=1)
            if members == "*":
                _, origin = origin_stmt.split("from ")
                targets = _retrieve_all(origin)
            else:
                targets = members.split(", ")
            _all.update(targets)
            yield line
        else:
            msg = f"Unexpected line:\n{line!r}"
            raise NotImplementedError(msg)
    yield f"__all__ = {sorted(_all)}"


def update_dynamic__all__(source: str | Path, /) -> None:
    """
    ## Relies on all `*` imports leading to an `__all__`.

    Acceptable `source`:

        "altair.package.subpackage.etc"
        Path(...)

    """
    fp = normalize_source(source)
    content = process_lines(extract_lines(fp))
    ruff.write_lint_format(fp, content)


if __name__ == "__main__":
    update__all__variable()
