"""
Stub file generator for altair.datasets module.

This script automatically generates the type stub file (__init__.pyi) from
the dataset metadata to ensure it stays in sync with available datasets.
"""

from __future__ import annotations

import ast
from pathlib import Path
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
from ._reader import load, url

# Type for the data object with all available dataset attributes
class DataObjectWithDatasets(DataObject):
    # All available datasets from _typing.py Dataset type
'''

STUB_FOOTER = '''# Export the data object with proper typing
data: DataObjectWithDatasets

# Export other functions and classes
__all__ = ["data", "Loader", "load", "url"]
'''


def extract_dataset_names_from_typing(typing_file: Path) -> list[str]:
    """
    Extract dataset names from the _typing.py file.
    
    Parameters
    ----------
    typing_file : Path
        Path to the _typing.py file
        
    Returns
    -------
    list[str]
        List of dataset names
    """
    with open(typing_file, 'r') as f:
        content = f.read()
    
    # Parse the file to find the Dataset Literal type
    tree = ast.parse(content)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'Dataset':
                    if isinstance(node.value, ast.Call):
                        # Handle Literal case
                        if hasattr(node.value, 'args') and node.value.args:
                            arg = node.value.args[0]
                            if isinstance(arg, ast.List):
                                return [elt.value for elt in arg.elts if isinstance(elt, ast.Constant)]
    
    # Fallback: try to extract from string content using regex
    import re
    # Look for the Dataset Literal pattern specifically
    pattern = r'Dataset: TypeAlias = Literal\[(.*?)\]'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        literal_content = match.group(1)
        # Extract quoted strings from the literal content
        string_pattern = r'"([^"]+)"'
        matches = re.findall(string_pattern, literal_content)
        return sorted(matches)
    
    # Final fallback: extract all quoted strings and filter
    pattern = r'"([^"]+)"'
    matches = re.findall(pattern, content)
    # Filter out non-dataset names (like file extensions, etc.)
    dataset_names = [name for name in matches if not name.startswith('.') and '_' in name]
    return sorted(list(set(dataset_names)))


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
    
    accessor_content = '\n'.join(accessor_lines)
    
    return f"{STUB_HEADER}{accessor_content}\n\n{STUB_FOOTER}"


def generate_stub_file(dpkg: DataPackage | None = None) -> None:
    """
    Generate the stub file for altair.datasets module.
    
    Parameters
    ----------
    dpkg : DataPackage, optional
        DataPackage instance. If None, will extract from _typing.py
    """
    out_dir = fs.REPO_ROOT / "altair" / "datasets"
    typing_file = out_dir / "_typing.py"
    stub_file = out_dir / "__init__.pyi"
    
    if dpkg is not None:
        # Use dataset names from DataPackage
        dataset_names = list(dpkg.dataset_names())
    else:
        # Extract from existing _typing.py file
        dataset_names = extract_dataset_names_from_typing(typing_file)
    
    if not dataset_names:
        raise ValueError("No dataset names found")
    
    # Generate stub content
    stub_content = generate_stub_content(dataset_names)
    
    # Write stub file
    with open(stub_file, 'w') as f:
        f.write(stub_content)
    
    print(f"Generated stub file: {stub_file}")
    print(f"Included {len(dataset_names)} datasets")


if __name__ == "__main__":
    generate_stub_file() 