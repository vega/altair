"""
This script updates the attribute __all__ in altair/__init__.py
based on the updated Altair schema.
"""

import inspect
import sys
from os.path import abspath, dirname, join
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
import locale

if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing_extensions import TypeIs
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from typing import Final, Literal

ROOT_DIR: Final = abspath(join(dirname(__file__), ".."))
sys.path.insert(0, abspath(dirname(__file__)))
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
    init_path = alt.__file__
    with open(init_path, encoding=locale.getpreferredencoding(False)) as f:
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
    relevant_attributes = [x for x in alt.__dict__ if _is_relevant_attribute(x)]
    relevant_attributes.sort()
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
    Path(init_path).write_text(
        new_file_content, encoding=locale.getpreferredencoding(False)
    )


def _is_relevant_attribute(attr_name: str) -> bool:
    attr = getattr(alt, attr_name)
    if (
        getattr(attr, "_deprecated", False) is True
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
        or attr_name == "TypingDict"
        or attr_name == "TypingGenerator"
        or attr_name == "ValueOrDatum"
    ):
        return False
    elif inspect.ismodule(attr):
        # Only include modules which are part of Altair. This excludes built-in
        # modules (they do not have a __file__ attribute), standard library,
        # and third-party packages.
        return getattr(attr, "__file__", "").startswith(str(Path(alt.__file__).parent))
    else:
        return True


if __name__ == "__main__":
    update__all__variable()
