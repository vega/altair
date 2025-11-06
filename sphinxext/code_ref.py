"""Sphinx extension providing formatted code blocks, referencing some function."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, cast, get_args

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util.parsing import nested_parse_to_nodes

from altair.vegalite.v6.schema._typing import VegaThemes
from tools.codemod import extract_func_def, extract_func_def_embed

if TYPE_CHECKING:
    import sys
    from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
    from typing import Any, ClassVar, TypeVar, Union

    from docutils.parsers.rst.states import RSTState, RSTStateMachine
    from docutils.statemachine import StringList
    from sphinx.application import Sphinx

    if sys.version_info >= (3, 12):
        from typing import TypeAliasType
    else:
        from typing_extensions import TypeAliasType
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    T = TypeVar("T")
    OneOrIter = TypeAliasType("OneOrIter", Union[T, Iterable[T]], type_params=(T,))

_OutputShort: TypeAlias = Literal["code", "plot"]
_OutputLong: TypeAlias = Literal["code-block", "altair-plot"]
_OUTPUT_REMAP: Mapping[_OutputShort, _OutputLong] = {
    "code": "code-block",
    "plot": "altair-plot",
}
_Option: TypeAlias = Literal["output", "fold", "summary"]

_PYSCRIPT_URL_FMT = "https://pyscript.net/releases/{0}/core.js"
_PYSCRIPT_VERSION = "2025.2.2"
_PYSCRIPT_URL = _PYSCRIPT_URL_FMT.format(_PYSCRIPT_VERSION)


def validate_output(output: Any) -> _OutputLong:
    output = output.strip().lower()
    if output not in {"plot", "code"}:
        msg = f":output: option must be one of {get_args(_OutputShort)!r}"
        raise TypeError(msg)
    else:
        short = cast("_OutputShort", output)
        return _OUTPUT_REMAP[short]


def validate_packages(packages: Any) -> str:
    if packages is None:
        return '["altair", "vega-datasets"]'
    else:
        split = [pkg.strip() for pkg in packages.split(",")]
        if len(split) == 1:
            return f'["{split[0]}"]'
        else:
            return f"[{','.join(split)}]"


def raw_html(text: str, /) -> nodes.raw:
    return nodes.raw("", text, format="html")


def maybe_details(
    parsed: Iterable[nodes.Node], options: dict[_Option, Any], *, default_summary: str
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


def theme_names() -> tuple[Sequence[str], Sequence[str]]:
    names: set[str] = set(get_args(VegaThemes))
    carbon = {nm for nm in names if nm.startswith("carbon")}
    return ["default", *sorted(names - carbon)], sorted(carbon)


def option(label: str, value: str | None = None, /) -> nodes.raw:
    s = f"<option value={value!r}>" if value else "<option>"
    return raw_html(f"{s}{label}</option>\n")


def optgroup(label: str, *options: OneOrIter[nodes.raw]) -> Iterator[nodes.raw]:
    yield raw_html(f"<optgroup label={label!r}>\n")
    for opt in options:
        if isinstance(opt, nodes.raw):
            yield opt
        else:
            yield from opt
    yield raw_html("</optgroup>\n")


def dropdown(
    id: str, label: str | None, extra_select: str, *options: OneOrIter[nodes.raw]
) -> Iterator[nodes.raw]:
    if label:
        yield raw_html(f"<label for={id!r}>{label}</label>\n")
    select_text = f"<select id={id!r}"
    if extra_select:
        select_text = f"{select_text} {extra_select}"
    yield raw_html(f"{select_text}>\n")
    for opt in options:
        if isinstance(opt, nodes.raw):
            yield opt
        else:
            yield from opt
    yield raw_html("</select>\n")


def pyscript(
    packages: str, target_div_id: str, loading_label: str, py_code: str
) -> Iterator[nodes.raw]:
    PY = "py"
    LB, RB = "{", "}"
    packages = f""""packages":{packages}"""
    yield raw_html(f"<div id={target_div_id!r}>{loading_label}</div>\n")
    yield raw_html(f"<script type={PY!r} config='{LB}{packages}{RB}'>\n")
    yield raw_html(py_code)
    yield raw_html("</script>\n")


def _before_code(refresh_name: str, select_id: str, target_div_id: str) -> str:
    INDENT = " " * 4
    return (
        f"from js import document\n"
        f"from pyscript import display\n"
        f"import altair as alt\n\n"
        f"def {refresh_name}(*args):\n"
        f"{INDENT}selected = document.getElementById({select_id!r}).value\n"
        f"{INDENT}alt.renderers.set_embed_options(theme=selected)\n"
        f"{INDENT}display(chart, append=False, target={target_div_id!r})\n"
    )


class ThemeDirective(SphinxDirective):
    """
    Theme preview directive.

    Similar to ``CodeRefDirective``, but uses `PyScript`_ to access the browser.

    .. _PyScript:
        https://pyscript.net/
    """

    has_content: ClassVar[bool] = False
    required_arguments: ClassVar[int] = 1
    option_spec = {
        "packages": validate_packages,
        "dropdown-label": directives.unchanged,
        "loading-label": directives.unchanged,
        "fold": directives.flag,
        "summary": directives.unchanged_required,
    }

    def run(self) -> Sequence[nodes.Node]:
        results: list[nodes.Node] = []
        SELECT_ID = "embed_theme"
        REFRESH_NAME = "apply_embed_input"
        TARGET_DIV_ID = "render_altair"
        standard_names, carbon_names = theme_names()

        qual_name = self.arguments[0]
        module_name, func_name = qual_name.rsplit(".", 1)
        dropdown_label = self.options.get("dropdown-label", "Select theme:")
        loading_label = self.options.get("loading-label", "loading...")
        packages: str = self.options.get("packages", validate_packages(None))

        results.append(raw_html("<div><p>\n"))
        results.extend(
            dropdown(
                SELECT_ID,
                dropdown_label,
                f"py-input={REFRESH_NAME!r}",
                (option(nm) for nm in standard_names),
                optgroup("Carbon", (option(nm) for nm in carbon_names)),
            )
        )
        py_code = extract_func_def_embed(
            module_name,
            func_name,
            before=_before_code(REFRESH_NAME, SELECT_ID, TARGET_DIV_ID),
            after=f"{REFRESH_NAME}()",
            assign_to="chart",
            indent=4,
        )
        # For PyScript/Pyodide compatibility, use vega_datasets until new Altair is published
        py_code = py_code.replace(
            "from altair.datasets import data", "from vega_datasets import data"
        )
        # vega_datasets uses underscores in column names, not spaces
        # Order matters: do aggregation functions first (they contain field names)
        py_code = py_code.replace("mean(IMDB Rating)", "mean(IMDB_Rating)")
        py_code = py_code.replace(
            "mean(Rotten Tomatoes Rating)", "mean(Rotten_Tomatoes_Rating)"
        )
        py_code = py_code.replace('datum["IMDB Rating"]', "datum.IMDB_Rating")
        py_code = py_code.replace(
            'datum["Rotten Tomatoes Rating"]', "datum.Rotten_Tomatoes_Rating"
        )
        py_code = py_code.replace('datum["IMDB Votes"]', "datum.IMDB_Votes")
        # Field references in encodings (remaining ones)
        py_code = py_code.replace('"IMDB Rating"', '"IMDB_Rating"')
        py_code = py_code.replace(
            '"Rotten Tomatoes Rating"', '"Rotten_Tomatoes_Rating"'
        )
        py_code = py_code.replace('"IMDB Votes"', '"IMDB_Votes"')
        py_code = py_code.replace('"Release Date"', '"Release_Date"')
        py_code = py_code.replace("'IMDB Rating'", "'IMDB_Rating'")
        py_code = py_code.replace(
            "'Rotten Tomatoes Rating'", "'Rotten_Tomatoes_Rating'"
        )
        py_code = py_code.replace("'IMDB Votes'", "'IMDB_Votes'")
        py_code = py_code.replace("'Release Date'", "'Release_Date'")

        results.extend(
            pyscript(packages, TARGET_DIV_ID, loading_label, py_code=py_code)
        )
        results.append(raw_html("</div></p>\n"))
        return maybe_details(
            results,
            self.options,  # pyright: ignore[reportArgumentType]
            default_summary="Show Vega-Altair Theme Test",
        )


class PyScriptDirective(SphinxDirective):
    """Placeholder for non-theme related directive."""

    has_content: ClassVar[bool] = False
    option_spec = {"packages": directives.unchanged}

    def run(self) -> Sequence[nodes.Node]:
        raise NotImplementedError


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

    has_content: ClassVar[bool] = False
    required_arguments: ClassVar[int] = 1
    option_spec: ClassVar[dict[_Option, Callable[[str], Any]]] = {  # pyright: ignore[reportIncompatibleVariableOverride]
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
        super().__init__(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)  # fmt: skip # pyright: ignore[reportArgumentType]
        self.options: dict[_Option, Any]  # pyright: ignore[reportIncompatibleVariableOverride]

    def run(self) -> Sequence[nodes.Node]:
        qual_name = self.arguments[0]
        module_name, func_name = qual_name.rsplit(".", 1)
        output: _OutputLong = self.options.get("output", "code-block")
        content = extract_func_def(module_name, func_name, output=output)
        parsed = nested_parse_to_nodes(self.state, content)
        return maybe_details(parsed, self.options, default_summary="Show code")


def setup(app: Sphinx) -> None:
    app.add_directive_to_domain("py", "altair-code-ref", CodeRefDirective)
    app.add_js_file(_PYSCRIPT_URL, loading_method="defer", type="module")
    # app.add_directive("altair-pyscript", PyScriptDirective)
    app.add_directive("altair-theme", ThemeDirective)
