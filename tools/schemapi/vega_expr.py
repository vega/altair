from __future__ import annotations

import dataclasses
import functools
import keyword
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterable, Iterator, Literal, Sequence, overload
from urllib import request

import mistune
import mistune.util

from tools.schemapi.utils import RSTParse, RSTRenderer

if TYPE_CHECKING:
    import sys
    from re import Pattern

    from mistune import BaseRenderer, BlockParser, InlineParser

    if sys.version_info >= (3, 11):
        from typing import LiteralString, Self, TypeAlias
    else:
        from typing_extensions import LiteralString, Self, TypeAlias
    Token: TypeAlias = "dict[str, Any]"


EXPRESSIONS_URL = (
    "https://raw.githubusercontent.com/vega/vega/main/docs/docs/expressions.md"
)

FUNCTION_DEF_LINE: Pattern[str] = re.compile(r"<a name=\"(.+)\" href=\"#(.+)\">")
LIQUID_INCLUDE: Pattern[str] = re.compile(r"( \{% include.+%\})")

TYPE: Literal[r"type"] = "type"
RAW: Literal["raw"] = "raw"
SOFTBREAK: Literal["softbreak"] = "softbreak"
TEXT: Literal["text"] = "text"
CHILDREN: Literal["children"] = "children"


def download_expressions_md(url: str, /) -> Path:
    """Download to a temporary file, return that as a ``pathlib.Path``."""
    tmp, _ = request.urlretrieve(url)
    fp = Path(tmp)
    if not fp.exists():
        msg = (
            f"Expressions download failed: {fp!s}.\n\n"
            f"Try manually accessing resource: {url!r}"
        )
        raise FileNotFoundError(msg)
    else:
        return fp


def read_tokens(source: Path, /) -> list[Any]:
    """
    Read from ``source``, drop ``BlockState``.

    Factored out to provide accurate typing.
    """
    return mistune.create_markdown(renderer="ast").read(source)[0]


def strip_include_tag(s: str, /) -> str:
    """
    Removes `liquid`_ templating markup.

    .. _liquid:
        https://shopify.github.io/liquid/
    """
    return LIQUID_INCLUDE.sub(r"", s)
