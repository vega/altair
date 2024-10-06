"""Sphinx extension providing formatted code blocks, referencing some function."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, get_args

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util.parsing import nested_parse_to_nodes

from tools.codemod import extract_func_def

if TYPE_CHECKING:
    import sys
    from typing import Any, Callable, ClassVar, Iterable, Iterator, Mapping, Sequence

    from docutils.parsers.rst.states import RSTState, RSTStateMachine
    from docutils.statemachine import StringList
    from sphinx.application import Sphinx

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

_OutputShort: TypeAlias = Literal["code", "plot"]
_OutputLong: TypeAlias = Literal["code-block", "altair-plot"]
_OUTPUT_REMAP: Mapping[_OutputShort, _OutputLong] = {
    "code": "code-block",
    "plot": "altair-plot",
}
_Option: TypeAlias = Literal["output", "fold", "summary"]


def validate_output(output: Any) -> _OutputLong:
    output = output.strip().lower()
    if output not in {"plot", "code"}:
        msg = f":output: option must be one of {get_args(_OutputShort)!r}"
        raise TypeError(msg)
    else:
        short: _OutputShort = output
        return _OUTPUT_REMAP[short]


def raw_html(text: str, /) -> nodes.raw:
    return nodes.raw("", text, format="html")


def maybe_details(
    parsed: Iterable[nodes.Node],
    options: dict[_Option, Any],
    *,
    default_summary: str = "Show code",
) -> Sequence[nodes.Node]:
    """
    Wrap ``parsed`` in a folding `details`_ block if requested.

    Parameters
    ----------
    parsed
        Target nodes that have been processed.
    options
        Optional arguments provided to ``.. altair-code-ref::``.

        .. note::
            If no relevant options are  specified,
            ``parsed`` is returned unchanged.

    default_summary
        Label text used when **only** specifying ``:fold:``.

    .. _details:
        https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details
    """

    def gen() -> Iterator[nodes.Node]:
        if {"fold", "summary"}.isdisjoint(options.keys()):
            yield from parsed
        else:
            summary = options.get("summary", default_summary)
            yield raw_html(f"<p><details><summary><a>{summary}</a></summary>")
            yield from parsed
            yield raw_html("</details></p>")

    return list(gen())


class CodeRefDirective(SphinxDirective):
    """
    Formatted code block, referencing the contents of a function definition.

    Options:

        .. altair-code-ref::
            :output: [code, plot]
            :fold: flag
            :summary: str

    Examples
    --------
    Reference a function, generating a code block:

        .. altair-code-ref:: package.module.function

    Wrap the code block in a collapsible `details`_ tag:

        .. altair-code-ref:: package.module.function
            :fold:

    Override default ``"Show code"`` `details`_ summary:

        .. altair-code-ref:: package.module.function
            :fold:
            :summary: Look here!

    Use `altair-plot`_ instead of a code block:

        .. altair-code-ref:: package.module.function
            :output: plot

    .. note::
        Using `altair-plot`_ currently ignores the other options.

    .. _details:
        https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details
    .. _altair-plot:
        https://github.com/vega/sphinxext-altair
    """

    has_content: ClassVar[Literal[False]] = False
    required_arguments: ClassVar[Literal[1]] = 1
    option_spec: ClassVar[dict[_Option, Callable[[str], Any]]] = {
        "output": validate_output,
        "fold": directives.flag,
        "summary": directives.unchanged_required,
    }

    def __init__(
        self,
        name: str,
        arguments: list[str],
        options: dict[_Option, Any],
        content: StringList,
        lineno: int,
        content_offset: int,
        block_text: str,
        state: RSTState,
        state_machine: RSTStateMachine,
    ) -> None:
        super().__init__(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)  # fmt: skip
        self.options: dict[_Option, Any]

    def run(self) -> Sequence[nodes.Node]:
        qual_name = self.arguments[0]
        module_name, func_name = qual_name.rsplit(".", 1)
        output: _OutputLong = self.options.get("output", "code-block")
        content = extract_func_def(module_name, func_name, output=output)
        parsed = nested_parse_to_nodes(self.state, content)
        return maybe_details(parsed, self.options)


def setup(app: Sphinx) -> None:
    app.add_directive_to_domain("py", "altair-code-ref", CodeRefDirective)
