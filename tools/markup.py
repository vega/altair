"""Tools for working with formats like ``.md``, ``.rst``."""

from __future__ import annotations

import re
from html import unescape
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal
from urllib import request

import mistune.util
from mistune import InlineParser as _InlineParser
from mistune import Markdown as _Markdown
from mistune.renderers.rst import RSTRenderer as _RSTRenderer

if TYPE_CHECKING:
    import sys
    from collections.abc import Iterable

    if sys.version_info >= (3, 11):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from re import Pattern

    from mistune import BaseRenderer, BlockParser, BlockState, InlineState

    Url: TypeAlias = str

Token: TypeAlias = "dict[str, Any]"

_RE_LINK: Pattern[str] = re.compile(r"(?<=\[)([^\]]+)(?=\]\([^\)]+\))", re.MULTILINE)
_RE_SPECIAL: Pattern[str] = re.compile(r"[*_]{2,3}|`", re.MULTILINE)
_RE_LIQUID_INCLUDE: Pattern[str] = re.compile(r"( \{% include.+%\})")


class RSTRenderer(_RSTRenderer):
    def __init__(self) -> None:
        super().__init__()

    def inline_html(self, token: Token, state: BlockState) -> str:
        html = token["raw"]
        return rf"\ :raw-html:`{html}`\ "


class RSTParse(_Markdown):
    """
    Minor extension to support partial `ast`_ conversion.

    Only need to convert the docstring tokens to `.rst`.

    .. _ast:
        https://mistune.lepture.com/en/latest/guide.html#abstract-syntax-tree
    """

    def __init__(
        self,
        renderer: BaseRenderer | Literal["ast"] | None,
        block: BlockParser | None = None,
        inline: _InlineParser | None = None,
        plugins=None,
    ) -> None:
        if renderer == "ast":
            renderer = None
        super().__init__(renderer, block, inline, plugins)

    def __call__(self, s: str) -> str:
        s = super().__call__(s)  # pyright: ignore[reportAssignmentType]
        return unescape(s).replace(r"\ ,", ",").replace(r"\ ", " ")

    def render_tokens(self, tokens: Iterable[Token], /) -> str:
        """
        Render ast tokens originating from another parser.

        Parameters
        ----------
        tokens
            All tokens will be rendered into a single `.rst` string
        """
        if self.renderer is None:
            msg = "Unable to render tokens without a renderer."
            raise TypeError(msg)
        state = self.block.state_cls()
        s = self.renderer(self._iter_render(tokens, state), state)
        return mistune.util.unescape(s)


class RSTParseVegaLite(RSTParse):
    def __init__(
        self,
        renderer: RSTRenderer | None = None,
        block: BlockParser | None = None,
        inline: _InlineParser | None = None,
        plugins=None,
    ) -> None:
        super().__init__(renderer or RSTRenderer(), block, inline, plugins)

    def __call__(self, s: str) -> str:
        # remove formatting from links
        description = "".join(
            _RE_SPECIAL.sub("", d) if i % 2 else d
            for i, d in enumerate(_RE_LINK.split(s))
        )

        description = super().__call__(description)
        # Some entries in the Vega-Lite schema miss the second occurence of '__'
        description = description.replace("__Default value: ", "__Default value:__ ")
        # Links to the vega-lite documentation cannot be relative but instead need to
        # contain the full URL.
        description = description.replace(
            "types#datetime", "https://vega.github.io/vega-lite/docs/datetime.html"
        )
        # Fixing ambiguous unicode, RUF001 produces RUF002 in docs
        description = description.replace("’", "'")  # noqa: RUF001 [RIGHT SINGLE QUOTATION MARK]
        description = description.replace("–", "-")  # noqa: RUF001 [EN DASH]
        description = description.replace(" ", " ")  # noqa: RUF001 [NO-BREAK SPACE]
        return description.strip()


class InlineParser(_InlineParser):
    def __init__(self, hard_wrap: bool = False) -> None:
        super().__init__(hard_wrap)

    def process_text(self, text: str, state: InlineState) -> None:
        """
        Removes `liquid`_ templating markup.

        .. _liquid:
        https://shopify.github.io/liquid/
        """
        state.append_token({"type": "text", "raw": _RE_LIQUID_INCLUDE.sub(r"", text)})


def read_ast_tokens(source: Url | Path, /) -> list[Token]:
    """
    Read from ``source``, drop ``BlockState``.

    Factored out to provide accurate typing.
    """
    markdown = _Markdown(renderer=None, inline=InlineParser())
    if isinstance(source, Path):
        tokens = markdown.read(source)
    else:
        with request.urlopen(source) as response:
            s = response.read().decode("utf-8")
        tokens = markdown.parse(s, markdown.block.state_cls())
    return tokens[0]


def rst_syntax_for_class(class_name: str) -> str:
    return f":class:`{class_name}`"
