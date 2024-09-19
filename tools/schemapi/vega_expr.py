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

from tools.schemapi.utils import RSTParse as _RSTParse
from tools.schemapi.utils import RSTRenderer

if TYPE_CHECKING:
    import sys
    from re import Pattern

    from mistune import BaseRenderer, BlockParser, InlineParser

    if sys.version_info >= (3, 11):
        from typing import LiteralString, Self, TypeAlias
    else:
        from typing_extensions import LiteralString, Self, TypeAlias

Token: TypeAlias = "dict[str, Any]"
WorkInProgress: TypeAlias = Any
"""Marker for a type that will not be final."""


EXPRESSIONS_URL = (
    "https://raw.githubusercontent.com/vega/vega/main/docs/docs/expressions.md"
)

FUNCTION_DEF_LINE: Pattern[str] = re.compile(r"<a name=\"(.+)\" href=\"#(.+)\">")
LIQUID_INCLUDE: Pattern[str] = re.compile(r"( \{% include.+%\})")

TYPE: Literal[r"type"] = r"type"
RAW: Literal["raw"] = "raw"
SOFTBREAK: Literal["softbreak"] = "softbreak"
TEXT: Literal["text"] = "text"
CHILDREN: Literal["children"] = "children"

RETURN_WRAPPER = "FunctionExpression"
RETURN_ANNOTATION = "Expression"
# NOTE: No benefit to annotating with the actual wrapper
# - `Expression` is shorter, and has all the functionality/attributes

INPUT_ANNOTATION = "IntoExpression"

NONE: Literal[r"None"] = r"None"
STAR_ARGS: Literal["*args"] = "*args"
DECORATOR = r"@classmethod"


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


class RSTParse(_RSTParse):
    """
    Minor extension to support partial `ast`_ conversion.

    Only need to convert the docstring tokens to `.rst`.

    NOTE
    ----
    Once `PR`_ is merged, move this to the parent class and rename

    .. _ast:
        https://mistune.lepture.com/en/latest/guide.html#abstract-syntax-tree
    .. _PR:
        https://github.com/vega/altair/pull/3536
    """

    def __init__(
        self,
        renderer: BaseRenderer,
        block: BlockParser | None = None,
        inline: InlineParser | None = None,
        plugins=None,
    ) -> None:
        super().__init__(renderer, block, inline, plugins)
        if self.renderer is None:
            msg = "Must provide a renderer, got `None`"
            raise TypeError(msg)
        self.renderer: BaseRenderer

    def render_tokens(self, tokens: Iterable[Token], /) -> LiteralString:
        """
        Render ast tokens originating from another parser.

        Parameters
        ----------
        tokens
            All tokens will be rendered into a single `.rst` string
        """
        state = self.block.state_cls()
        return self.renderer(self._iter_render(tokens, state), state)


parser: RSTParse = RSTParse(RSTRenderer())


@dataclasses.dataclass
class VegaExprNode:
    """
    ``SchemaInfo``-like, but operates on `expressions.md`_.

    .. _expressions.md:
        https://raw.githubusercontent.com/vega/vega/main/docs/docs/expressions.md
    """

    name: str
    _children: Sequence[Token] = dataclasses.field(repr=False)
    doc: str = ""
    parameters: list[VegaExprParam] = dataclasses.field(default_factory=list)

    def to_signature(self) -> str:
        """NOTE: 101/147 cases are all required args."""
        pre_params = f"def {self.name_safe}(cls, "
        post_params = f", /) -> {RETURN_ANNOTATION}:"
        param_list = ""
        if self.is_overloaded():
            param_list = VegaExprParam.star_args()
        else:
            param_list = ", ".join(p.to_str() for p in self.parameters)
        return f"{pre_params}{param_list}{post_params}"

    def with_parameters(self) -> Self:
        raw_texts = self._split_signature_tokens()
        name = next(raw_texts)
        # NOTE: Overwriting the <a name> with the rendered text
        if self.name != name:
            self.name = name
        self.parameters = list(VegaExprParam.iter_params(raw_texts))
        return self

    def with_doc(self) -> Self:
        self.doc = self._doc_post_process(parser.render_tokens(self._doc_tokens()))
        return self

    @functools.cached_property
    def parameter_names(self) -> tuple[str, ...]:
        if self.parameters:
            return tuple(param.name for param in self.parameters if not param.variadic)
        else:
            msg = (
                f"Cannot provide `parameter_names` until they have been initialized via:\n"
                f"{type(self).__name__}.with_parameters()"
            )
            raise TypeError(msg)

    @property
    def name_safe(self) -> str:
        """Use for the method definition, but not when calling internally."""
        return f"{self.name}_" if self.is_keyword() else self.name

    def _split_signature_tokens(self) -> Iterator[str]:
        """Very rough splitting/cleaning of relevant token raw text."""
        it = iter(self)
        current = next(it)
        # NOTE: softbreak(s) denote the line the sig appears on
        while current[TYPE] != SOFTBREAK:
            current = next(it)
        current = next(it)
        while current[TYPE] != SOFTBREAK:
            # NOTE: This drops html markup tags
            if current[TYPE] == TEXT:
                clean = strip_include_tag(current[RAW]).strip(", -")
                if clean not in {", ", ""}:
                    yield from VegaExprNode.deep_split_punctuation(clean)
            current = next(it, None)
            if current is None:
                break

    def _doc_tokens(self) -> Sequence[Token]:
        """
        Return the slice of `self.children` that contains docstring content.

        Works for 100% of cases.
        """
        for idx, item in enumerate(self):
            if item[TYPE] == SOFTBREAK and self[idx + 1][TYPE] == TEXT:
                return self[idx + 1 :]
            else:
                continue
        msg = f"Expected to find a text node marking the start of docstring content.\nFailed for:\n\n{self!r}"
        raise NotImplementedError(msg)

    def _doc_post_process(self, rendered: str, /) -> str:
        r"""
        Utilizing properties found during parsing to improve docs.

        Temporarily handling this here.

        TODO
        ----
        - [x] Replace \*param_name\* -> \`\`param_name\`\`.
        - [x] References to ``func`` -> ``alt.expr.func``
            - **Doesn't include other vega expressions yet**
        - [x] Artifacts like: ``monthAbbrevFormat(0) -&gt; &quot;Jan&quot;``
        - [ ] Split after first sentence ends
        - [ ] Replace "For example:" -> an example block
        - [ ] Fix relative links to vega docs
            - There's code in ``utils`` for this
        """
        highlight_params = re.sub(
            rf"\*({'|'.join(self.parameter_names)})\*", r"``\g<1>``", rendered
        )
        with_alt_references = re.sub(
            rf"({self.name}\()", f"alt.expr.{self.name_safe}(", highlight_params
        )
        unescaped = mistune.util.unescape(with_alt_references)
        return unescaped

    @staticmethod
    def deep_split_punctuation(s: str, /) -> Iterator[str]:
        """Deep splitting of ending punctuation."""
        if s.isalnum():
            yield s
        else:
            end: list[str] = []
            if s.endswith((")", "]")):
                end.append(s[-1])
                s = s[:-1]
            elif s.endswith("..."):
                end.append(s[-3:])
                s = s[:-3]
            elif s.endswith(" |"):
                end.append(s[-2:])
                s = s[:-2]
            if len(s) == 1:
                yield s
            elif len(s) > 1:
                yield from VegaExprNode.deep_split_punctuation(s)
            yield from end

    def is_callable(self) -> bool:
        """
        Rough filter for excluding `constants`_.

        - Most of the parsing is to handle varying signatures.
        - Constants can just be referenced by name, so can skip those

        .. _constants:
            https://vega.github.io/vega/docs/expressions/#constants
        """
        name = self.name
        if name.startswith("string_"):
            # HACK: There are string/array functions that overlap
            # - the `.md` handles this by prefixing the `<a name=...` for the string version
            # - however this is another kind of overload
            # - but with more documentation, than the inline overload for color functions
            return True
        elif self.is_bound_variable_name():
            return False
        it = iter(self)
        name = name.lower()
        current = next(it).get(RAW, "").lower()
        while current != name:
            el = next(it, None)
            if el is None:
                print(f"Failed match: {name!r}")
                return True
            current = el.get(RAW, "").lower()
        next(it)
        return next(it).get(RAW, "") == "("

    def is_bound_variable_name(self) -> bool:
        """
        ``Vega`` `bound variables`_.

        .. _bound variables:
            https://vega.github.io/vega/docs/expressions/#bound-variables
        """
        RESERVED_NAMES: set[str] = {"datum", "event", "signal"}
        return self.name in RESERVED_NAMES

    def is_overloaded(self) -> bool:
        """
        Covers the `color functions`_.

        These look like:

            lab(l, a, b[, opacity]) | lab(specifier)

        .. _color functions:
            https://vega.github.io/vega/docs/expressions/#color-functions
        """
        for idx, item in enumerate(self):
            if item[TYPE] == TEXT and item.get(RAW, "") == "]) |":
                return self[idx + 1][TYPE] == SOFTBREAK
            else:
                continue
        return False

    def is_keyword(self) -> bool:
        return keyword.iskeyword(self.name)

    def __iter__(self) -> Iterator[Token]:
        yield from self._children

    @overload
    def __getitem__(self, index: int) -> Token: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[Token]: ...
    def __getitem__(self, index: int | slice) -> Token | Sequence[Token]:
        return self._children.__getitem__(index)


@dataclasses.dataclass
class VegaExprParam:
    name: str
    required: bool
    variadic: bool = False

    @staticmethod
    def star_args() -> LiteralString:
        return f"{STAR_ARGS}: Any"

    def to_str(self) -> str:
        """Return as an annotated parameter, with a default if needed."""
        if self.required:
            return f"{self.name}: {INPUT_ANNOTATION}"
        elif not self.variadic:
            return f"{self.name}: {INPUT_ANNOTATION} = {NONE}"
        else:
            return self.star_args()

    @classmethod
    def iter_params(cls, raw_texts: Iterable[str], /) -> Iterator[Self]:
        """Yields an ordered parameter list."""
        is_required: bool = True
        for s in raw_texts:
            if s not in {"(", ")"}:
                if s == "[":
                    is_required = False
                    continue
                elif s == "]":
                    is_required = True
                    continue
                elif s.isalnum():
                    yield cls(s, required=is_required)
                elif s == "...":
                    yield cls(STAR_ARGS, required=False, variadic=True)
                else:
                    continue


def parse_expressions(url: str, /) -> Iterator[tuple[str, VegaExprNode]]:
    """Download, read markdown and iteratively parse into signature representations."""
    for tok in read_tokens(download_expressions_md(url)):
        if (
            (children := tok.get(CHILDREN)) is not None
            and (child := next(iter(children)).get(RAW)) is not None
            and (match := FUNCTION_DEF_LINE.match(child))
        ):
            node = VegaExprNode(match[1], children)
            if node.is_callable():
                yield node.name, node.with_parameters().with_doc()
    request.urlcleanup()


def render_expr_method(node: VegaExprNode, /) -> WorkInProgress:
    if node.is_overloaded():
        body_params = STAR_ARGS[1:]
    else:
        body_params = f"({', '.join(param.name for param in node.parameters)})"
    body = f"return {RETURN_WRAPPER}({node.name}, {body_params})"
    return DECORATOR, node.to_signature(), node.doc, body


def test_parse() -> dict[str, VegaExprNode]:
    return dict(parse_expressions(EXPRESSIONS_URL))
