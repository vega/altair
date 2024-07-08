from __future__ import annotations

import ast
import hashlib
import itertools
import json
from pathlib import Path
import re
from typing import Any


def create_thumbnail(
    image_filename: Path,
    thumb_filename: Path,
    window_size: tuple[float, float] = (280, 160),
) -> None:
    """Create a thumbnail whose shortest dimension matches the window"""
    from PIL import Image

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
    from PIL import Image
    import numpy as np

    assert len(shape) == 2

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
    except SyntaxError:
        node = None
    return node, content


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

    if not isinstance(node, ast.Module):
        msg = f"This function only supports modules. You provided {node.__class__.__name__}"
        raise TypeError(msg)
    try:
        # In python 3.7 module knows its docstring.
        # Everything else will raise an attribute error
        docstring = node.docstring

        import tokenize
        from io import BytesIO

        ts = tokenize.tokenize(BytesIO(content).readline)
        ds_lines = 0
        # find the first string according to the tokenizer and get
        # it's end row
        for tk in ts:
            if tk.exact_type == 3:
                ds_lines, _ = tk.end
                break
        # grab the rest of the file
        rest = "\n".join(content.split("\n")[ds_lines:])
        lineno = ds_lines + 1

    except AttributeError:
        # this block can be removed when python 3.6 support is dropped
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, (ast.Str, ast.Constant))
        ):
            docstring_node = node.body[0]
            docstring = docstring_node.value.s
            # python2.7: Code was read in bytes needs decoding to utf-8
            # unless future unicode_literals is imported in source which
            # make ast output unicode strings
            if hasattr(docstring, "decode") and not isinstance(docstring, str):
                docstring = docstring.decode("utf-8")
            # python3.8: has end_lineno
            lineno = getattr(
                docstring_node, "end_lineno", docstring_node.lineno
            )  # The last line of the string.
            # This get the content of the file after the docstring last line
            # Note: 'maxsplit' argument is not a keyword argument in python2
            rest = content.split("\n", lineno)[-1]
            lineno += 1
        else:
            docstring, rest = "", ""

    if not docstring:
        msg = (
            f'Could not find docstring in file "{filename}". '
            "A docstring is required for the example gallery."
        )
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
