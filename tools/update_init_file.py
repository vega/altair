"""
This script updates the attribute __all__ in altair/__init__.py
based on the updated Altair schema.
"""

from __future__ import annotations
from inspect import ismodule, getattr_static
import sys
from pathlib import Path
from typing import (
    IO,
    Any,
    Iterable,
    List,
    Optional,
    Protocol,
    Sequence,
    Type,
    TypeVar,
    Union,
    cast,
)


if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing_extensions import TypeIs
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from typing import Final, Literal

current_dir = Path(__file__).parent
ROOT_DIR: Final = str((current_dir / "..").resolve())
sys.path.insert(0, str(current_dir))

from schemapi.utils import ruff_format_str  # noqa: E402

# Import Altair from head
sys.path.insert(0, ROOT_DIR)
import altair as alt  # noqa: E402


def update__all__variable() -> None:
    """Updates the __all__ variable to all relevant attributes of top-level Altair.
    This is for example useful to hide deprecated attributes from code completion in
    Jupyter.
    """
    # Read existing file content
    encoding = "utf-8"
    init_path = Path(alt.__file__)
    with init_path.open(encoding=encoding) as f:
        lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

    # Find first and last line of the definition of __all__
    first_definition_line = None
    last_definition_line = None
    for idx, line in enumerate(lines):
        if line.startswith("__all__ ="):
            first_definition_line = idx
        elif first_definition_line is not None and line.startswith("]"):
            last_definition_line = idx
            break
    assert first_definition_line is not None and last_definition_line is not None

    # Figure out which attributes are relevant
    relevant_attributes = sorted(x for x in alt.__dict__ if _is_relevant_attribute(x))
    relevant_attributes_str = f"__all__ = {relevant_attributes}"

    # Put file back together, replacing old definition of __all__ with new one, keeping
    # the rest of the file as is
    new_lines = (
        lines[:first_definition_line]
        + [relevant_attributes_str]
        + lines[last_definition_line + 1 :]
    )
    # Format file content with ruff
    new_file_content = ruff_format_str("\n".join(new_lines))

    # Write new version of altair/__init__.py
    init_path.write_text(new_file_content, encoding=encoding)


def _is_relevant_attribute(attr_name: str) -> bool:
    attr = getattr(alt, attr_name)
    if (
        getattr_static(attr, "_deprecated", False)
        or attr_name.startswith("_")
        or attr is TypeVar
        or attr is Self
        or attr is Type
        or attr is cast
        or attr is List
        or attr is Any
        or attr is Literal
        or attr is Optional
        or attr is Iterable
        or attr is Union
        or attr is Protocol
        or attr is Sequence
        or attr is IO
        or attr is TypeIs
        or attr is annotations
        or attr_name == "TypingDict"
        or attr_name == "TypingGenerator"
        or attr_name == "ValueOrDatum"
    ):
        return False
    elif ismodule(attr):
        # Only include modules which are part of Altair. This excludes built-in
        # modules (they do not have a __file__ attribute), standard library,
        # and third-party packages.
        prefix = str(Path(alt.__file__).parent)
        return getattr_static(attr, "__file__", "").startswith(prefix)
    else:
        return True


if __name__ == "__main__":
    update__all__variable()
