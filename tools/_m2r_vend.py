r"""Vendored https://github.com/miyakogi/m2r

The project was archived on 2022-11-17.

The most popular fork is https://github.com/CrossNox/m2r2
This fork was last updated on 2023-01-30.

The project depends on https://github.com/lepture/mistune/releases/tag/v0.8.4 which raises:

```py
Lib/site-packages/mistune.py:435: SyntaxWarning: invalid escape sequence '\|'
  cells[i][c] = re.sub('\\\\\|', '|', cell)

```
"""

# ruff: noqa
import os
import os.path
import re

from docutils import statemachine, nodes, io, utils
from docutils.parsers import rst
from docutils.utils import column_width
import mistune
from urllib.parse import urlparse

__version__ = "0.3.1"
_is_sphinx = False
prolog = """\
.. role:: raw-html-m2r(raw)
   :format: html

"""


class RestBlockGrammar(mistune.BlockGrammar):
    directive = re.compile(
        r"^( *\.\..*?)\n(?=\S)",
        re.DOTALL | re.MULTILINE,
    )
    oneline_directive = re.compile(
        r"^( *\.\..*?)$",
        re.DOTALL | re.MULTILINE,
    )
    rest_code_block = re.compile(
        r"^::\s*$",
        re.DOTALL | re.MULTILINE,
    )


class RestBlockLexer(mistune.BlockLexer):
    grammar_class = RestBlockGrammar
    default_rules = [
        "directive",
        "oneline_directive",
        "rest_code_block",
    ] + mistune.BlockLexer.default_rules

    def parse_directive(self, m):
        self.tokens.append(
            {
                "type": "directive",
                "text": m.group(1),
            }
        )

    def parse_oneline_directive(self, m):
        # reuse directive output
        self.tokens.append(
            {
                "type": "directive",
                "text": m.group(1),
            }
        )

    def parse_rest_code_block(self, m):
        self.tokens.append(
            {
                "type": "rest_code_block",
            }
        )


class RestInlineGrammar(mistune.InlineGrammar):
    image_link = re.compile(
        r"\[!\[(?P<alt>.*?)\]\((?P<url>.*?)\).*?\]\((?P<target>.*?)\)"
    )
    rest_role = re.compile(r":.*?:`.*?`|`[^`]+`:.*?:")
    rest_link = re.compile(r"`[^`]*?`_")
    inline_math = re.compile(r"`\$(.*)?\$`")
    eol_literal_marker = re.compile(r"(\s+)?::\s*$")
    # add colon and space as special text
    text = re.compile(r"^[\s\S]+?(?=[\\<!\[:_*`~ ]|https?://| {2,}\n|$)")
    # __word__ or **word**
    double_emphasis = re.compile(r"^([_*]){2}(?P<text>[\s\S]+?)\1{2}(?!\1)")
    # _word_ or *word*
    emphasis = re.compile(
        r"^\b_((?:__|[^_])+?)_\b"  # _word_
        r"|"
        r"^\*(?P<text>(?:\*\*|[^\*])+?)\*(?!\*)"  # *word*
    )

    def no_underscore_emphasis(self):
        self.double_emphasis = re.compile(
            r"^\*{2}(?P<text>[\s\S]+?)\*{2}(?!\*)"  # **word**
        )
        self.emphasis = re.compile(
            r"^\*(?P<text>(?:\*\*|[^\*])+?)\*(?!\*)"  # *word*
        )


class RestInlineLexer(mistune.InlineLexer):
    grammar_class = RestInlineGrammar
    default_rules = [
        "image_link",
        "rest_role",
        "rest_link",
        "eol_literal_marker",
    ] + mistune.InlineLexer.default_rules

    def __init__(
        self,
        *args,
        disable_inline_math: bool = False,
        no_underscore_emphasis: bool = False,
        **kwargs,
    ):
        super(RestInlineLexer, self).__init__(*args, **kwargs)
        if no_underscore_emphasis:
            self.rules.no_underscore_emphasis()
        inline_maths = "inline_math" in self.default_rules
        if disable_inline_math:
            if inline_maths:
                self.default_rules.remove("inline_math")
        elif not inline_maths:
            self.default_rules.insert(0, "inline_math")

    def output_double_emphasis(self, m):
        # may include code span
        text = self.output(m.group("text"))
        return self.renderer.double_emphasis(text)

    def output_emphasis(self, m):
        # may include code span
        text = self.output(m.group("text") or m.group(1))
        return self.renderer.emphasis(text)

    def output_image_link(self, m):
        """Pass through rest role."""
        return self.renderer.image_link(
            m.group("url"), m.group("target"), m.group("alt")
        )

    def output_rest_role(self, m):
        """Pass through rest role."""
        return self.renderer.rest_role(m.group(0))

    def output_rest_link(self, m):
        """Pass through rest link."""
        return self.renderer.rest_link(m.group(0))

    def output_inline_math(self, m):
        """Pass through rest link."""
        return self.renderer.inline_math(m.group(1))

    def output_eol_literal_marker(self, m):
        """Pass through rest link."""
        marker = ":" if m.group(1) is None else ""
        return self.renderer.eol_literal_marker(marker)


class RestRenderer(mistune.Renderer):
    _include_raw_html = False
    list_indent_re = re.compile(r"^(\s*(#\.|\*)\s)")
    indent = " " * 3
    list_marker = "{#__rest_list_mark__#}"
    hmarks = {
        1: "=",
        2: "-",
        3: "^",
        4: "~",
        5: '"',
        6: "#",
    }

    def __init__(
        self,
        *args,
        anonymous_references: bool = False,
        parse_relative_links: bool = False,
        **kwargs,
    ):
        self.anonymous_references = anonymous_references
        self.parse_relative_links = parse_relative_links
        super(RestRenderer, self).__init__(*args, **kwargs)

    def _indent_block(self, block):
        return "\n".join(
            self.indent + line if line else "" for line in block.splitlines()
        )

    def _raw_html(self, html):
        self._include_raw_html = True
        return r"\ :raw-html-m2r:`{}`\ ".format(html)

    def block_code(self, code, lang=None):
        if lang == "math":
            first_line = "\n.. math::\n\n"
        elif lang:
            first_line = "\n.. code-block:: {}\n\n".format(lang)
        elif _is_sphinx:
            first_line = "\n::\n\n"
        else:
            first_line = "\n.. code-block::\n\n"
        return first_line + self._indent_block(code) + "\n"

    def block_quote(self, text):
        # text includes some empty line
        return "\n..\n\n{}\n\n".format(self._indent_block(text.strip("\n")))

    def block_html(self, html):
        """Rendering block level pure html content.

        :param html: text content of the html snippet.
        """
        return "\n\n.. raw:: html\n\n" + self._indent_block(html) + "\n\n"

    def header(self, text, level, raw=None):
        """Rendering header/heading tags like ``<h1>`` ``<h2>``.

        :param text: rendered text content for the header.
        :param level: a number for the header level, for example: 1.
        :param raw: raw text content of the header.
        """
        return "\n{0}\n{1}\n".format(text, self.hmarks[level] * column_width(text))

    def hrule(self):
        """Rendering method for ``<hr>`` tag."""
        return "\n----\n"

    def list(self, body, ordered=True):
        """Rendering list tags like ``<ul>`` and ``<ol>``.

        :param body: body contents of the list.
        :param ordered: whether this list is ordered or not.
        """
        mark = "#. " if ordered else "* "
        lines = body.splitlines()
        for i, line in enumerate(lines):
            if line and not line.startswith(self.list_marker):
                lines[i] = " " * len(mark) + line
        return "\n{}\n".format("\n".join(lines)).replace(self.list_marker, mark)

    def list_item(self, text):
        """Rendering list item snippet. Like ``<li>``."""
        return "\n" + self.list_marker + text

    def paragraph(self, text):
        """Rendering paragraph tags. Like ``<p>``."""
        return "\n" + text + "\n"

    def table(self, header, body):
        """Rendering table element. Wrap header and body in it.

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

    def table_row(self, content):
        """Rendering a table row. Like ``<tr>``.

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

    def table_cell(self, content, **flags):
        """Rendering a table cell. Like ``<th>`` ``<td>``.

        :param content: content of current table cell.
        :param header: whether this is header or not.
        :param align: align of current table cell.
        """
        return "- " + content + "\n"

    def double_emphasis(self, text):
        """Rendering **strong** text.

        :param text: text content for emphasis.
        """
        return r"\ **{}**\ ".format(text)

    def emphasis(self, text):
        """Rendering *emphasis* text.

        :param text: text content for emphasis.
        """
        return r"\ *{}*\ ".format(text)

    def codespan(self, text):
        """Rendering inline `code` text.

        :param text: text content for inline code.
        """
        if "``" not in text:
            return r"\ ``{}``\ ".format(text)
        else:
            # actually, docutils split spaces in literal
            return self._raw_html(
                '<code class="docutils literal">'
                '<span class="pre">{}</span>'
                "</code>".format(text.replace("`", "&#96;"))
            )

    def linebreak(self):
        """Rendering line break like ``<br>``."""
        if self.options.get("use_xhtml"):
            return self._raw_html("<br />") + "\n"
        return self._raw_html("<br>") + "\n"

    def strikethrough(self, text):
        """Rendering ~~strikethrough~~ text.

        :param text: text content for strikethrough.
        """
        return self._raw_html("<del>{}</del>".format(text))

    def text(self, text):
        """Rendering unformatted text.

        :param text: text content.
        """
        return text

    def autolink(self, link, is_email=False):
        """Rendering a given link or email address.

        :param link: link content or email address.
        :param is_email: whether this is an email or not.
        """
        return link

    def link(self, link, title, text):
        """Rendering a given link with content and title.

        :param link: href link for ``<a>`` tag.
        :param title: title content for `title` attribute.
        :param text: text content for description.
        """
        if self.anonymous_references:
            underscore = "__"
        else:
            underscore = "_"
        if title:
            return self._raw_html(
                '<a href="{link}" title="{title}">{text}</a>'.format(
                    link=link, title=title, text=text
                )
            )
        if not self.parse_relative_links:
            return r"\ `{text} <{target}>`{underscore}\ ".format(
                target=link, text=text, underscore=underscore
            )
        else:
            url_info = urlparse(link)
            if url_info.scheme:
                return r"\ `{text} <{target}>`{underscore}\ ".format(
                    target=link, text=text, underscore=underscore
                )
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
                doc_link = "{doc_name}{anchor}".format(
                    # splittext approach works whether or not path is set. It
                    # will return an empty string if unset, which leads to
                    # anchor only ref.
                    doc_name=os.path.splitext(url_info.path)[0],
                    anchor=anchor,
                )
                return r"\ :{link_type}:`{text} <{doc_link}>`\ ".format(
                    link_type=link_type, doc_link=doc_link, text=text
                )

    def image(self, src, title, text):
        """Rendering a image with title and text.

        :param src: source link of the image.
        :param title: title text of the image.
        :param text: alt text of the image.
        """
        # rst does not support title option
        # and I couldn't find title attribute in HTML standard
        return "\n".join(
            [
                "",
                ".. image:: {}".format(src),
                "   :target: {}".format(src),
                "   :alt: {}".format(text),
                "",
            ]
        )

    def inline_html(self, html):
        """Rendering span level pure html content.

        :param html: text content of the html snippet.
        """
        return self._raw_html(html)

    def newline(self):
        """Rendering newline element."""
        return ""

    def footnote_ref(self, key, index):
        """Rendering the ref anchor of a footnote.

        :param key: identity key for the footnote.
        :param index: the index count of current footnote.
        """
        return r"\ [#fn-{}]_\ ".format(key)

    def footnote_item(self, key, text):
        """Rendering a footnote item.

        :param key: identity key for the footnote.
        :param text: text content of the footnote.
        """
        return ".. [#fn-{0}] {1}\n".format(key, text.strip())

    def footnotes(self, text):
        """Wrapper for all footnotes.

        :param text: contents of all footnotes.
        """
        if text:
            return "\n\n" + text
        else:
            return ""

    """Below outputs are for rst."""

    def image_link(self, url, target, alt):
        return "\n".join(
            [
                "",
                ".. image:: {}".format(url),
                "   :target: {}".format(target),
                "   :alt: {}".format(alt),
                "",
            ]
        )

    def rest_role(self, text):
        return text

    def rest_link(self, text):
        return text

    def inline_math(self, math):
        """Extension of recommonmark"""
        return r"\ :math:`{}`\ ".format(math)

    def eol_literal_marker(self, marker):
        """Extension of recommonmark"""
        return marker

    def directive(self, text):
        return "\n" + text

    def rest_code_block(self):
        return "\n\n"


class M2R(mistune.Markdown):
    def __init__(
        self, renderer=None, inline=RestInlineLexer, block=RestBlockLexer, **kwargs
    ):
        if renderer is None:
            renderer = RestRenderer(**kwargs)
        super(M2R, self).__init__(renderer, inline=inline, block=block, **kwargs)

    def parse(self, text):
        output = super(M2R, self).parse(text)
        return self.post_process(output)

    def output_directive(self):
        return self.renderer.directive(self.token["text"])

    def output_rest_code_block(self):
        return self.renderer.rest_code_block()

    def post_process(self, text):
        output = (
            text.replace("\\ \n", "\n")
            .replace("\n\\ ", "\n")
            .replace(" \\ ", " ")
            .replace("\\  ", " ")
            .replace("\\ .", ".")
        )
        if self.renderer._include_raw_html:
            return prolog + output
        else:
            return output


def main():
    msg = "CLI usage is not supported"
    raise NotImplementedError(msg)


if __name__ == "__main__":
    main()
