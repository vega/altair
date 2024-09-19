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

    from mistune import BaseRenderer, BlockParser, BlockState, InlineParser

    if sys.version_info >= (3, 11):
        from typing import LiteralString, Self, TypeAlias
    else:
        from typing_extensions import LiteralString, Self, TypeAlias
    Token: TypeAlias = "dict[str, Any]"

