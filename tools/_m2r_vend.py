r"""
Vendored https://github.com/miyakogi/m2r.

The project was archived on 2022-11-17.

The most popular fork is https://github.com/CrossNox/m2r2
This fork was last updated on 2023-01-30.

The project depends on https://github.com/lepture/mistune/releases/tag/v0.8.4 which raises:

```py
Lib/site-packages/mistune.py:435: SyntaxWarning: invalid escape sequence '\|'
  cells[i][c] = re.sub('\\\\\|', '|', cell)

```
"""

from __future__ import annotations

import os
import os.path
import re
from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse

import mistune
from docutils.utils import column_width

if TYPE_CHECKING:
    from re import Match, Pattern, RegexFlag

__version__ = "0.3.1"
_flags: RegexFlag = re.DOTALL | re.MULTILINE


class RestBlockGrammar(mistune.BlockGrammar):
    directive: Pattern[str] = re.compile(r"^( *\.\..*?)\n(?=\S)", _flags)
    oneline_directive: Pattern[str] = re.compile(r"^( *\.\..*?)$", _flags)
    rest_code_block: Pattern[str] = re.compile(r"^::\s*$", _flags)


class RestBlockLexer(mistune.BlockLexer):
    grammar_class: type[RestBlockGrammar] = RestBlockGrammar
    default_rules: list[str] = [
        "directive",
        "oneline_directive",
        "rest_code_block",
        *mistune.BlockLexer.default_rules,
    ]

    def parse_directive(self, m: Match[str]) -> None:
        self.tokens.append({"type": "directive", "text": m.group(1)})

    def parse_oneline_directive(self, m: Match[str]) -> None:
        # reuse directive output
        self.tokens.append({"type": "directive", "text": m.group(1)})

    def parse_rest_code_block(self, m: Match[str]) -> None:
        self.tokens.append({"type": "rest_code_block"})


class RestInlineGrammar(mistune.InlineGrammar):
    image_link: Pattern[str] = re.compile(
        r"\[!\[(?P<alt>.*?)\]\((?P<url>.*?)\).*?\]\((?P<target>.*?)\)"
    )
    rest_role: Pattern[str] = re.compile(r":.*?:`.*?`|`[^`]+`:.*?:")
    rest_link: Pattern[str] = re.compile(r"`[^`]*?`_")
    inline_math: Pattern[str] = re.compile(r"`\$(.*)?\$`")
    eol_literal_marker: Pattern[str] = re.compile(r"(\s+)?::\s*$")
    # add colon and space as special text
    text: Pattern[str] = re.compile(r"^[\s\S]+?(?=[\\<!\[:_*`~ ]|https?://| {2,}\n|$)")
    # __word__ or **word**
    double_emphasis: Pattern[str] = re.compile(
        r"^([_*]){2}(?P<text>[\s\S]+?)\1{2}(?!\1)"
    )
    # _word_ or *word*
    emphasis: Pattern[str] = re.compile(
        r"^\b_((?:__|[^_])+?)_\b" r"|" r"^\*(?P<text>(?:\*\*|[^\*])+?)\*(?!\*)"
    )

    def no_underscore_emphasis(self) -> None:
        # **word**
        self.double_emphasis: Pattern[str] = re.compile(
            r"^\*{2}(?P<text>[\s\S]+?)\*{2}(?!\*)"
        )
        # *word*
        self.emphasis: Pattern[str] = re.compile(
            r"^\*(?P<text>(?:\*\*|[^\*])+?)\*(?!\*)"
        )


class RestInlineLexer(mistune.InlineLexer):
    grammar_class: type[RestInlineGrammar] = RestInlineGrammar
    default_rules: list[str] = [
        "image_link",
        "rest_role",
        "rest_link",
        "eol_literal_marker",
        *mistune.InlineLexer.default_rules,
    ]

    def __init__(
        self,
        *args,
        disable_inline_math: bool = False,
        no_underscore_emphasis: bool = False,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.renderer: RestRenderer
        if no_underscore_emphasis:
            self.rules.no_underscore_emphasis()
        inline_maths = "inline_math" in self.default_rules
        if disable_inline_math:
            if inline_maths:
                self.default_rules.remove("inline_math")
        elif not inline_maths:
            self.default_rules.insert(0, "inline_math")

    def output_double_emphasis(self, m: Match[str]) -> str:
        # may include code span
        text = self.output(m.group("text"))
        return self.renderer.double_emphasis(text)

    def output_emphasis(self, m: Match[str]) -> str:
        # may include code span
        text = self.output(m.group("text") or m.group(1))
        return self.renderer.emphasis(text)

    def output_image_link(self, m: Match[str]) -> str:
        """Pass through rest role."""
        return self.renderer.image_link(
            m.group("url"), m.group("target"), m.group("alt")
        )

    def output_rest_role(self, m: Match[str]) -> str:
        """Pass through rest role."""
        return self.renderer.rest_role(m.group(0))

    def output_rest_link(self, m: Match[str]) -> str:
        """Pass through rest link."""
        return self.renderer.rest_link(m.group(0))

    def output_inline_math(self, m: Match[str]) -> str:
        """Pass through rest link."""
        return self.renderer.inline_math(m.group(1))

    def output_eol_literal_marker(self, m: Match[str]) -> str:
        """Pass through rest link."""
        marker = ":" if m.group(1) is None else ""
        return self.renderer.eol_literal_marker(marker)


class RestRenderer(mistune.Renderer):
    _include_raw_html: bool = False
    list_indent_re: Pattern[str] = re.compile(r"^(\s*(#\.|\*)\s)")
    indent: str = " " * 3
    list_marker: str = "{#__rest_list_mark__#}"
    hmarks: dict[int, str] = {1: "=", 2: "-", 3: "^", 4: "~", 5: '"', 6: "#"}

    def __init__(
        self,
        *args,
        anonymous_references: bool = False,
        parse_relative_links: bool = False,
        **kwargs,
    ) -> None:
        self.anonymous_references: bool = anonymous_references
        self.parse_relative_links: bool = parse_relative_links
        super().__init__(*args, **kwargs)

    def _indent_block(self, block: str) -> str:
        return "\n".join(
            self.indent + line if line else "" for line in block.splitlines()
        )

    def _raw_html(self, html: str) -> str:
        self._include_raw_html = True
        return rf"\ :raw-html-m2r:`{html}`\ "

    def block_code(self, code: str, lang: str | None = None) -> str:
        if lang == "math":
            first_line = "\n.. math::\n\n"
        elif lang:
            first_line = f"\n.. code-block:: {lang}\n\n"
        else:
            first_line = "\n.. code-block::\n\n"
        return first_line + self._indent_block(code) + "\n"

    def block_quote(self, text: str) -> str:
        # text includes some empty line
        return "\n..\n\n{}\n\n".format(self._indent_block(text.strip("\n")))

    def block_html(self, html: str) -> str:
        """
        Rendering block level pure html content.

        :param html: text content of the html snippet.
        """
        return "\n\n.. raw:: html\n\n" + self._indent_block(html) + "\n\n"

    def header(self, text: str, level: int, raw: Any = None) -> str:
        """
        Rendering header/heading tags like ``<h1>`` ``<h2>``.

        :param text: rendered text content for the header.
        :param level: a number for the header level, for example: 1.
        :param raw: raw text content of the header.
        """
        return f"\n{text}\n{self.hmarks[level] * column_width(text)}\n"

    def hrule(self) -> str:
        """Rendering method for ``<hr>`` tag."""
        return "\n----\n"

    def list(self, body: str, ordered: bool = True) -> str:
        """
        Rendering list tags like ``<ul>`` and ``<ol>``.

        :param body: body contents of the list.
        :param ordered: whether this list is ordered or not.
        """
        mark = "#. " if ordered else "* "
        lines = body.splitlines()
        for i, line in enumerate(lines):
            if line and not line.startswith(self.list_marker):
                lines[i] = " " * len(mark) + line
        return "\n{}\n".format("\n".join(lines)).replace(self.list_marker, mark)

    def list_item(self, text: str) -> str:
        """Rendering list item snippet. Like ``<li>``."""
        return "\n" + self.list_marker + text

    def paragraph(self, text: str) -> str:
        """Rendering paragraph tags. Like ``<p>``."""
        return "\n" + text + "\n"

    def table(self, header: str, body: str) -> str:
        """
        Rendering table element. Wrap header and body in it.

        :param header: header part of the table.
        :param body: body part of the table.
        """
        table = "\n.. list-table::\n"
        if header and not header.isspace():
            table = (
                table
                + self.indent
                + ":header-rows: 1\n\n"
                + self._indent_block(header)
                + "\n"
            )
        else:
            table = table + "\n"
        table = table + self._indent_block(body) + "\n\n"
        return table

    def table_row(self, content: str) -> str:
        """
        Rendering a table row. Like ``<tr>``.

        :param content: content of current table row.
        """
        contents = content.splitlines()
        if not contents:
            return ""
        clist = ["* " + contents[0]]
        if len(contents) > 1:
            for c in contents[1:]:
                clist.append("  " + c)
        return "\n".join(clist) + "\n"

    def table_cell(self, content: str, **flags) -> str:
        """
        Rendering a table cell. Like ``<th>`` ``<td>``.

        :param content: content of current table cell.
        :param header: whether this is header or not.
        :param align: align of current table cell.
        """
        return "- " + content + "\n"

    def double_emphasis(self, text: str) -> str:
        """
        Rendering **strong** text.

        :param text: text content for emphasis.
        """
        return rf"\ **{text}**\ "

    def emphasis(self, text: str) -> str:
        """
        Rendering *emphasis* text.

        :param text: text content for emphasis.
        """
        return rf"\ *{text}*\ "

    def codespan(self, text: str) -> str:
        """
        Rendering inline `code` text.

        :param text: text content for inline code.
        """
        if "``" not in text:
            return rf"\ ``{text}``\ "
        else:
            # actually, docutils split spaces in literal
            return self._raw_html(
                '<code class="docutils literal">'
                '<span class="pre">{}</span>'
                "</code>".format(text.replace("`", "&#96;"))
            )

    def linebreak(self) -> str:
        """Rendering line break like ``<br>``."""
        if self.options.get("use_xhtml"):
            return self._raw_html("<br />") + "\n"
        return self._raw_html("<br>") + "\n"

    def strikethrough(self, text: str) -> str:
        """
        Rendering ~~strikethrough~~ text.

        :param text: text content for strikethrough.
        """
        return self._raw_html(f"<del>{text}</del>")

    def text(self, text: str) -> str:
        """
        Rendering unformatted text.

        :param text: text content.
        """
        return text

    def autolink(self, link: str, is_email: bool = False) -> str:
        """
        Rendering a given link or email address.

        :param link: link content or email address.
        :param is_email: whether this is an email or not.
        """
        return link

    def link(self, link: str, title: str, text: str) -> str:
        """
        Rendering a given link with content and title.

        :param link: href link for ``<a>`` tag.
        :param title: title content for `title` attribute.
        :param text: text content for description.
        """
        underscore = "__" if self.anonymous_references else "_"
        if title:
            return self._raw_html(f'<a href="{link}" title="{title}">{text}</a>')
        if not self.parse_relative_links:
            return rf"\ `{text} <{link}>`{underscore}\ "
        else:
            url_info = urlparse(link)
            if url_info.scheme:
                return rf"\ `{text} <{link}>`{underscore}\ "
            else:
                link_type = "doc"
                anchor = url_info.fragment
                if url_info.fragment:
                    if url_info.path:
                        # Can't link to anchors via doc directive.
                        anchor = ""
                    else:
                        # Example: [text](#anchor)
                        link_type = "ref"
                # splittext approach works whether or not path is set. It
                # will return an empty string if unset, which leads to
                # anchor only ref.
                doc_link = f"{os.path.splitext(url_info.path)[0]}{anchor}"  # noqa: PTH122
                return rf"\ :{link_type}:`{text} <{doc_link}>`\ "

    def image(self, src: str, title: str, text: str) -> str:
        """
        Rendering a image with title and text.

        :param src: source link of the image.
        :param title: title text of the image.
        :param text: alt text of the image.
        """
        # rst does not support title option
        # and I couldn't find title attribute in HTML standard
        return "\n".join(
            ["", f".. image:: {src}", f"   :target: {src}", f"   :alt: {text}", ""]
        )

    def inline_html(self, html: str) -> str:
        """
        Rendering span level pure html content.

        :param html: text content of the html snippet.
        """
        return self._raw_html(html)

    def newline(self) -> str:
        """Rendering newline element."""
        return ""

    def footnote_ref(self, key: str, index: Any) -> str:
        """
        Rendering the ref anchor of a footnote.

        :param key: identity key for the footnote.
        :param index: the index count of current footnote.
        """
        return rf"\ [#fn-{key}]_\ "

    def footnote_item(self, key: str, text: str) -> str:
        """
        Rendering a footnote item.

        :param key: identity key for the footnote.
        :param text: text content of the footnote.
        """
        return f".. [#fn-{key}] {text.strip()}\n"

    def footnotes(self, text: str) -> str:
        """
        Wrapper for all footnotes.

        :param text: contents of all footnotes.
        """
        if text:
            return "\n\n" + text
        else:
            return ""

    """Below outputs are for rst."""

    def image_link(self, url: str, target: str, alt: str) -> str:
        return "\n".join(
            ["", f".. image:: {url}", f"   :target: {target}", f"   :alt: {alt}", ""]
        )

    def rest_role(self, text: str) -> str:
        return text

    def rest_link(self, text: str) -> str:
        return text

    def inline_math(self, math: str) -> str:
        """Extension of recommonmark."""
        return rf"\ :math:`{math}`\ "

    def eol_literal_marker(self, marker: str) -> str:
        """Extension of recommonmark."""
        return marker

    def directive(self, text: str) -> str:
        return "\n" + text

    def rest_code_block(self) -> str:
        return "\n\n"


class M2R(mistune.Markdown):
    def __init__(
        self,
        renderer: RestRenderer | None = None,
        inline: type[RestInlineLexer] = RestInlineLexer,
        block: type[RestBlockLexer] = RestBlockLexer,
        **kwargs,
    ) -> None:
        r: RestRenderer = renderer or RestRenderer(**kwargs)
        super().__init__(r, inline=inline, block=block, **kwargs)
        self.renderer: RestRenderer

    def parse(self, text: str) -> str:
        return self.post_process(super().parse(text))

    def output_directive(self) -> str:
        return self.renderer.directive(self.token["text"])

    def output_rest_code_block(self) -> str:
        return self.renderer.rest_code_block()

    def post_process(self, text: str) -> str:
        return (
            text.replace("\\ \n", "\n")
            .replace("\n\\ ", "\n")
            .replace(" \\ ", " ")
            .replace("\\  ", " ")
            .replace("\\ .", ".")
        )
