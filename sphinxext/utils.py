from __future__ import annotations

import ast
import hashlib
import itertools
import json
from pathlib import Path
import re
from typing import Any
from PIL import Image
import numpy as np


def create_thumbnail(
    image_filename: Path,
    thumb_filename: Path,
    window_size: tuple[float, float] = (280, 160),
) -> None:
    """Create a thumbnail whose shortest dimension matches the window"""

    im = Image.open(image_filename)
    im_width, im_height = im.size
    width, height = window_size

    width_factor, height_factor = width / im_width, height / im_height

    if width_factor > height_factor:
        final_width = width
        final_height = int(im_height * width_factor)
    else:
        final_height = height
        final_width = int(im_width * height_factor)

    thumb = im.resize((final_width, final_height), Image.ANTIALIAS)
    thumb.save(thumb_filename)


def create_generic_image(
    filename: Path, shape: tuple[float, float] = (200, 300), gradient: bool = True
) -> None:
    """Create a generic image"""

    arr = np.zeros((shape[0], shape[1], 3))
    if gradient:
        # gradient from gray to white
        arr += np.linspace(128, 255, shape[1])[:, None]
    im = Image.fromarray(arr.astype("uint8"))
    im.save(filename)


SYNTAX_ERROR_DOCSTRING = """
SyntaxError
===========
Example script with invalid Python syntax
"""


# NOTE
# - reads entire file as text
# - performs a string replace
# - Try/except is probabloy fine
def _parse_source_file(filename: str) -> tuple[ast.Module | None, str]:
    """Parse source file into AST node

    Parameters
    ----------
    filename : str
        File path

    Returns
    -------
    node : AST node
    content : utf-8 encoded string

    Notes
    -----
    This function adapted from the sphinx-gallery project; license: BSD-3
    https://github.com/sphinx-gallery/sphinx-gallery/
    """
    content = Path(filename).read_text(encoding="utf-8")
    # change from Windows format to UNIX for uniformity
    content = content.replace("\r\n", "\n")

    try:
        node = ast.parse(content)
        if not isinstance(node, ast.Module):
            msg = f"This function only supports modules. You provided {type(node).__name__}"
            raise TypeError(msg)
    except SyntaxError:
        node = None
    return node, content


# NOTE:
# - called 1-2x per example
# - re.search, but should be match? (has ^...$ markers, but also multi-line)
#   - replacement possibly inefficient
# - should unnest the stdlib imports
# fully drop 3.6 compat code?
def get_docstring_and_rest(filename: str) -> tuple[str, str | None, str, int]:
    """Separate ``filename`` content between docstring and the rest

    Strongly inspired from ast.get_docstring.

    Parameters
    ----------
    filename: str
        The path to the file containing the code to be read

    Returns
    -------
    docstring: str
        docstring of ``filename``
    category: list
        list of categories specified by the "# category:" comment
    rest: str
        ``filename`` content without the docstring
    lineno: int
         the line number on which the code starts

    Notes
    -----
    This function adapted from the sphinx-gallery project; license: BSD-3
    https://github.com/sphinx-gallery/sphinx-gallery/
    """
    node, content = _parse_source_file(filename)

    # Find the category comment
    find_category = re.compile(r"^#\s*category:\s*(.*)$", re.MULTILINE)
    match = find_category.search(content)
    if match is not None:
        category = match.groups()[0]
        # remove this comment from the content
        content = find_category.sub("", content)
    else:
        category = None

    lineno = 1

    if node is None:
        return SYNTAX_ERROR_DOCSTRING, category, content, lineno

    # NOTE: Incorrect comment below. Still triggered on 3.11
    # this block can be removed when python 3.6 support is dropped
    # ast.get_docstring
    msg = (
        f'Could not find docstring in file "{filename}". '
        "A docstring is required for the example gallery."
    )

    if (
        node.body
        and isinstance(node.body[0], ast.Expr)
        and isinstance(node.body[0].value, ast.Constant)
    ):
        docstring_node = node.body[0]
        if docstring := docstring_node.value.s:
            dn = docstring_node
            lineno = dn.end_lineno or dn.lineno
            # The last line of the string.
            # This get the content of the file after the docstring last line
            rest = content.split("\n", lineno)[-1]
            lineno += 1
        else:
            raise ValueError(msg)
    else:
        raise ValueError(msg)
    return docstring, category, rest, lineno


def prev_this_next(
    it: list[dict[str, Any]], sentinel: None = None
) -> zip[tuple[dict[str, Any] | None, dict[str, Any], dict[str, Any] | None]]:
    """Utility to return (prev, this, next) tuples from an iterator"""
    i1, i2, i3 = itertools.tee(it, 3)
    next(i3, None)
    return zip(itertools.chain([sentinel], i1), i2, itertools.chain(i3, [sentinel]))


def dict_hash(dct: dict[Any, Any]) -> Any:
    """Return a hash of the contents of a dictionary"""
    serialized = json.dumps(dct, sort_keys=True)

    try:
        m = hashlib.sha256(serialized)[:32]
    except TypeError:
        m = hashlib.sha256(serialized.encode())[:32]

    return m.hexdigest()
