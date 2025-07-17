"""
Stub file generator for altair.datasets module.

This script automatically generates the type stub file (__init__.pyi) from
the dataset metadata to ensure it stays in sync with available datasets.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from tools import fs

if TYPE_CHECKING:
    from tools.datasets.datapackage import DataPackage

STUB_HEADER = '''"""
Type stubs for altair.datasets module.

This file provides type information for the dynamic dataset accessors
to help static type checkers like Pylance and mypy understand the
available dataset attributes.

The contents of this file are automatically generated from the dataset
metadata. Do not modify directly.
"""

from typing import Any, Union
from ._data import DataObject, DatasetAccessor
from ._loader import Loader

# Type for the data object with all available dataset attributes
class DataObjectWithDatasets(DataObject):
    # All available datasets from _typing.py Dataset type
'''

STUB_FOOTER = """# Export the data object with proper typing
data: DataObjectWithDatasets

# Export functions defined in __init__.py
def load(name: str, backend: str | None = None, **kwargs: Any) -> Any: ...
def url(name: str, suffix: str | None = None, /) -> str: ...

# Export other functions and classes
__all__ = ["Loader", "data", "load", "url"]
"""


def generate_stub_content(dataset_names: list[str]) -> str:
    """
    Generate the stub file content from dataset names.

    Parameters
    ----------
    dataset_names : list[str]
        List of dataset names

    Returns
    -------
    str
        Complete stub file content
    """
    # Generate the dataset accessor attributes
    accessor_lines = []
    for name in sorted(dataset_names):
        accessor_lines.append(f"    {name}: DatasetAccessor")

    accessor_content = "\n".join(accessor_lines)

    return f"{STUB_HEADER}{accessor_content}\n\n{STUB_FOOTER}"


def generate_stub_file(dpkg: DataPackage) -> None:
    """
    Generate the stub file for altair.datasets module.

    Parameters
    ----------
    dpkg : DataPackage
        DataPackage instance.
    """
    out_dir = fs.REPO_ROOT / "altair" / "datasets"
    stub_file = out_dir / "__init__.pyi"

    # Use dataset names from DataPackage
    dataset_names = list(dpkg.dataset_names())

    if not dataset_names:
        msg = "No dataset names found"
        raise ValueError(msg)

    # Generate stub content
    stub_content = generate_stub_content(dataset_names)

    # Write stub file
    stub_file.write_text(stub_content, encoding="utf-8")

    print(f"Generated stub file: {stub_file}")
    print(f"Included {len(dataset_names)} datasets")


if __name__ == "__main__":
    from tools.datasets.datapackage import DataPackage

    dpkg = DataPackage()
    generate_stub_file(dpkg)
