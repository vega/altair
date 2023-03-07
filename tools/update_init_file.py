"""
This script updates the attribute __all__ in altair/__init__.py
based on the updated Altair schema.
"""
import inspect
import sys
from pathlib import Path
from os.path import abspath, dirname, join
from typing import TypeVar, Type, cast, List, Any

import black

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

# Import Altair from head
ROOT_DIR = abspath(join(dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)
import altair as alt  # noqa: E402


def update__all__variable():
    """Updates the __all__ variable to all relevant attributes of top-level Altair.
    This is for example useful to hide deprecated attributes from code completion in
    Jupyter.
    """
    # Read existing file content
    init_path = alt.__file__
    with open(init_path, "r") as f:
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
    # Format file content with black
    new_file_content = black.format_str("\n".join(new_lines), mode=black.Mode())

    # Write new version of altair/__init__.py
    with open(init_path, "w") as f:
        f.write(new_file_content)


def _is_relevant_attribute(attr_name):
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
    ):
        return False
    else:
        if inspect.ismodule(attr):
            # Only include modules which are part of Altair. This excludes built-in
            # modules (they do not have a __file__ attribute), standard library,
            # and third-party packages.
            return getattr(attr, "__file__", "").startswith(
                str(Path(alt.__file__).parent)
            )
        else:
            return True


if __name__ == "__main__":
    update__all__variable()
