from __future__ import annotations

import dataclasses
import enum
import keyword
import re
from collections import deque
from inspect import getmembers
from itertools import chain
from pathlib import Path
from textwrap import TextWrapper as _TextWrapper
from textwrap import indent
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Iterable,
    Iterator,
    Literal,
    Mapping,
    Sequence,
    overload,
)
from urllib import request

from tools.markup import RSTParse, Token, read_ast_tokens
from tools.markup import RSTRenderer as _RSTRenderer
from tools.schemapi.schemapi import SchemaBase as _SchemaBase
from tools.schemapi.utils import (
    ruff_write_lint_format_str as _ruff_write_lint_format_str,
)

if TYPE_CHECKING:
    import sys
    from re import Match, Pattern

    from mistune import BlockState

    if sys.version_info >= (3, 11):
        from typing import LiteralString, Self
    else:
        from typing_extensions import LiteralString, Self
    from _typeshed import SupportsKeysAndGetItem

__all__ = ["parse_expressions", "write_expr_module"]


# NOTE: Urls/fragments
VEGA_DOCS_URL: LiteralString = "https://vega.github.io/vega/docs/"
EXPRESSIONS_DOCS_URL: LiteralString = f"{VEGA_DOCS_URL}expressions/"


class Source(str, enum.Enum):
    """Enumerations for ``expressions.md`` source files."""

    LIVE = "https://raw.githubusercontent.com/vega/vega/main/docs/docs/expressions.md"
    STATIC = "https://raw.githubusercontent.com/vega/vega/ff98519cce32b776a98d01dd982467d76fc9ee34/docs/docs/expressions.md"


# NOTE: Regex patterns
FUNCTION_DEF_LINE: Pattern[str] = re.compile(r"<a name=\"(.+)\" href=\"#(.+)\">")
SENTENCE_BREAK: Pattern[str] = re.compile(r"(?<!\.)\. ")

# NOTE: `mistune` token keys/values
TYPE: Literal[r"type"] = r"type"
RAW: Literal["raw"] = "raw"
SOFTBREAK: Literal["softbreak"] = "softbreak"
TEXT: Literal["text"] = "text"
CHILDREN: Literal["children"] = "children"

# NOTE: Punctuation/markers
ELLIPSIS: Literal["..."] = "..."
OPEN_PAREN: Literal["("] = "("
CLOSE_PAREN: Literal[")"] = ")"
OPEN_BRACKET: Literal["["] = "["
CLOSE_BRACKET: Literal["]"] = "]"
INLINE_OVERLOAD: Literal[" |"] = " |"

METHOD_INDENT: LiteralString = 8 * " "
SECTION_BREAK: Literal["\n\n"] = "\n\n"

# NOTE: `altair` types (for annotations)
RETURN_WRAPPER: LiteralString = "FunctionExpression"
RETURN_ANNOTATION: LiteralString = "Expression"
"""
The annotation is intentionally *less* specific than the real type.

``Expression`` is shorter, while preserving all the user-facing functionality
"""

CONST_WRAPPER: LiteralString = "ConstExpression"
CLS_META: LiteralString = "_ExprMeta"
INPUT_ANNOTATION: LiteralString = "IntoExpression"

# NOTE: `python`/`mypy` related literals
NONE: Literal[r"None"] = r"None"
STAR_ARGS: Literal["*args"] = "*args"
DECORATOR: LiteralString = r"@classmethod"
IGNORE_OVERRIDE: LiteralString = r"# type: ignore[override]"
IGNORE_MISC: LiteralString = r"# type: ignore[misc]"

MODULE_PRE = '''\
"""Tools for creating transform & filter expressions with a python syntax."""

from __future__ import annotations

import sys
from typing import Any, TYPE_CHECKING

from altair.expr.core import {const}, {func}
from altair.vegalite.v5.schema.core import ExprRef as _ExprRef

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

if TYPE_CHECKING:
    from altair.expr.core import {return_ann}, {input_ann}


class {metaclass}(type):
    """
    Metaclass for :class:`expr`.

    Currently providing read-only class properties, representing JavaScript constants.
    """

    @property
    def NaN(cls) -> {return_ann}:
        """Not a number (same as JavaScript literal NaN)."""
        return {const}("NaN")

    @property
    def LN10(cls) -> {return_ann}:
        """The natural log of 10 (alias to Math.LN10)."""
        return {const}("LN10")

    @property
    def E(cls) -> {return_ann}:
        """The transcendental number e (alias to Math.E)."""
        return {const}("E")

    @property
    def LOG10E(cls) -> {return_ann}:
        """The base 10 logarithm e (alias to Math.LOG10E)."""
        return {const}("LOG10E")

    @property
    def LOG2E(cls) -> {return_ann}:
        """The base 2 logarithm of e (alias to Math.LOG2E)."""
        return {const}("LOG2E")

    @property
    def SQRT1_2(cls) -> {return_ann}:
        """The square root of 0.5 (alias to Math.SQRT1_2)."""
        return {const}("SQRT1_2")

    @property
    def LN2(cls) -> {return_ann}:
        """The natural log of 2 (alias to Math.LN2)."""
        return {const}("LN2")

    @property
    def SQRT2(cls) -> {return_ann}:
        """The square root of 2 (alias to Math.SQRT1_2)."""
        return {const}("SQRT2")

    @property
    def PI(cls) -> {return_ann}:
        """The transcendental number pi (alias to Math.PI)."""
        return {const}("PI")
'''

MODULE_POST = """\
_ExprType = expr
# NOTE: Compatibility alias for previous type of `alt.expr`.
# `_ExprType` was not referenced in any internal imports/tests.
"""

CLS_DOC = """
    Utility providing *constants* and *classmethods* to construct expressions.

    `Expressions`_ can be used to write basic formulas that enable custom interactions.

    Alternatively, an `inline expression`_ may be defined via :class:`expr()`.

    Parameters
    ----------
    expr: str
        A `vega expression`_ string.

    Returns
    -------
    ``ExprRef``

    .. _Expressions:
        https://altair-viz.github.io/user_guide/interactions.html#expressions
    .. _inline expression:
       https://altair-viz.github.io/user_guide/interactions.html#inline-expressions
    .. _vega expression:
       https://vega.github.io/vega/docs/expressions/

    Examples
    --------
    >>> import altair as alt

    >>> bind_range = alt.binding_range(min=100, max=300, name="Slider value:  ")
    >>> param_width = alt.param(bind=bind_range, name="param_width")
    >>> param_color = alt.param(
    ...     expr=alt.expr.if_(param_width < 200, "red", "black"),
    ...     name="param_color",
    ... )
    >>> y = alt.Y("yval").axis(titleColor=param_color)

    >>> y
    Y({
      axis: {'titleColor': Parameter('param_color', VariableParameter({
        expr: if((param_width < 200),'red','black'),
        name: 'param_color'
      }))},
      shorthand: 'yval'
    })
    """

CLS_TEMPLATE = '''\
class expr({base}, metaclass={metaclass}):
    """{doc}"""

    @override
    def __new__(cls: type[{base}], expr: str) -> {base}:  {type_ignore}
        return {base}(expr=expr)
'''

METHOD_SIGNATURE = (
    """def {title}(cls, {param_list}{marker}) -> {return_ann}:{type_ignore}"""
)

METHOD_TEMPLATE = '''\
    {decorator}
    {signature}
        """
        {doc}
        """
        return {return_wrapper}({name}, {body_params})
'''


def _override_predicate(obj: Any, /) -> bool:
    return callable(obj) and not (name := obj.__name__).startswith("_")  # noqa: F841


_SCHEMA_BASE_MEMBERS: frozenset[str] = frozenset(
    nm for nm, _ in getmembers(_SchemaBase, _override_predicate)
)


class RSTRenderer(_RSTRenderer):
    def __init__(self) -> None:
        super().__init__()

    def link(self, token: Token, state: BlockState) -> str:
        """Store link url, for appending at the end of doc."""
        attrs = token["attrs"]
        url = expand_urls(attrs["url"])
        text = self.render_children(token, state)
        text = text.replace("`", "")
        inline = f"`{text}`_"
        state.env["ref_links"][text] = {"url": url}
        return inline

    def _with_links(self, s: str, links: dict[str, Any] | Any, /) -> str:
        it = chain.from_iterable(
            (f".. _{ref_name}:", f"    {attrs['url']}")
            for ref_name, attrs in links.items()
        )
        return "\n".join(chain([s], it))

    def __call__(self, tokens: Iterable[Token], state: BlockState) -> str:
        result = super().__call__(tokens, state)
        if links := state.env.get("ref_links", {}):
            return self._with_links(result, links)
        else:
            return result


parser: RSTParse = RSTParse(RSTRenderer())
text_wrap = _TextWrapper(
    width=100,
    break_long_words=False,
    break_on_hyphens=False,
    initial_indent=METHOD_INDENT,
    subsequent_indent=METHOD_INDENT,
)


class ReplaceMany:
    """
    Perform many ``1:1`` replacements on a given text.

    Structured wrapper around a `dict`_ and `re.sub`_.

    Parameters
    ----------
    mapping
        Optional initial mapping.
    fmt_match
        **Combined** format string/regex pattern.
        Receives the keys of the final ``self._mapping`` as a positional argument.

        .. note::
            Special characters must be escaped **first**, if present.

    fmt_replace
        Format string applied to a succesful match, after substition.
        Receives ``self._mapping[key]`` as a positional argument.

    .. _dict:
        https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    .. _re.sub:
        https://docs.python.org/3/library/re.html#re.sub

    Examples
    --------
    Providing a mapping during construction:

        string = "The dog chased the cat, chasing the mouse. Poor mouse"
        animal_replacer = ReplaceMany({"dog": "cat"})
        >>> animal_replacer(string)
        'The cat chased the cat, chasing the mouse. Poor mouse'

    Updating with new replacements:

        animal_replacer.update({"cat": "mouse", "mouse": "dog"}, duck="rabbit")
        >>> animal_replacer(string, refresh=True)
        'The cat chased the mouse, chasing the dog. Poor dog'

    Further calls will continue using the most recent update:

        >>> animal_replacer("duck")
        'rabbit'
    """

    def __init__(
        self,
        mapping: Mapping[str, str] | None = None,
        /,
        fmt_match: str = "(?P<key>{0})",
        fmt_replace: str = "{0}",
    ) -> None:
        self._mapping: dict[str, str] = dict(mapping) if mapping else {}
        self._fmt_match: str = fmt_match
        self._fmt_replace: str = fmt_replace
        self.pattern: Pattern[str]
        self.repl: Callable[[Match[str]], str]
        self._is_prepared: bool = False

    def update(
        self,
        m: SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]],
        /,
        **kwds: str,
    ) -> None:
        """Update replacements mapping."""
        self._mapping.update(m, **kwds)

    def clear(self) -> None:
        """Reset replacements mapping."""
        self._mapping.clear()

    def refresh(self) -> None:
        """
        Compile replacement pattern and generate substitution function.

        Notes
        -----
        Should be called **after** all (old, new) pairs have been collected.
        """
        self.pattern = self._compile()
        self.repl = self._replacer()
        self._is_prepared = True

    def __call__(self, s: str, count: int = 0, /, refresh: bool = False) -> str:
        """
        Replace the leftmost non-overlapping occurrences of ``self.pattern`` in ``s`` using ``self.repl``.

        Wraps `re.sub`_

        .. _re.sub:
            https://docs.python.org/3/library/re.html#re.sub
        """
        if not self._is_prepared or refresh:
            self.refresh()
        return self.pattern.sub(self.repl, s, count)

    def _compile(self) -> Pattern[str]:
        if not self._mapping:
            name = self._mapping.__qualname__  # type: ignore[attr-defined]
            msg = (
                f"Requires {name!r} to be populated, but got:\n"
                f"{name}={self._mapping!r}"
            )
            raise TypeError(msg)
        return re.compile(rf"{self._fmt_match.format('|'.join(self._mapping))}")

    def _replacer(self) -> Callable[[Match[str]], str]:
        def repl(m: Match[str], /) -> str:
            return self._fmt_replace.format(self._mapping[m["key"]])

        return repl

    def __getitem__(self, key: str) -> str:
        return self._mapping[key]

    def __setitem__(self, key: str, value: str) -> None:
        self._mapping[key] = value

    def __repr__(self) -> str:
        return f"{type(self).__name__}(\n    {self._mapping!r}\n)"


class VegaExprDef:
    """
    ``SchemaInfo``-like, but operates on `expressions.md`_.

    .. _expressions.md:
        https://raw.githubusercontent.com/vega/vega/main/docs/docs/expressions.md
    """

    remap_title: ClassVar[ReplaceMany] = ReplaceMany(
        fmt_match=r"(?P<key>{0})\(", fmt_replace="{0}("
    )

    def __init__(self, name: str, children: Sequence[Token], /) -> None:
        self.name: str = name
        self._children: Sequence[Token] = children
        self.parameters: list[VegaExprParam] = []
        self.doc: str = ""
        self.signature: str = ""

    def with_doc(self) -> Self:
        """
        Parses docstring content in full.

        Accessible via ``self.doc``
        """
        s: str = parser.render_tokens(self._doc_tokens())
        s = italics_to_backticks(s, self.parameter_names(variadic=False))
        s = type(self).remap_title(s)
        self.doc = format_doc(s)
        return self

    def with_parameters(self) -> Self:
        """
        Parses signature content into an intermediate representation.

        Accessible via  ``self.parameters``.
        """
        split: Iterator[str] = self._split_signature_tokens(exclude_name=True)
        self.parameters = list(VegaExprParam.from_texts(split))
        return self

    def with_signature(self) -> Self:
        """
        Parses ``self.parameters`` into a full signature definition line.

        Accessible via  ``self.signature``
        """
        param_list = (
            VegaExprParam.star_args()
            if self.is_overloaded()
            else ", ".join(p.render() for p in self.parameters)
        )
        self.signature = METHOD_SIGNATURE.format(
            title=self.title,
            param_list=param_list,
            marker="" if self.is_variadic() else ", /",
            return_ann=RETURN_ANNOTATION,
            type_ignore=(
                f"  {IGNORE_OVERRIDE}" if self.is_incompatible_override() else ""
            ),
        )
        return self

    def parameter_names(self, *, variadic: bool = True) -> Iterator[str]:
        """Pass ``variadic=False`` to omit names like``*args``."""
        if self.parameters:
            it: Iterator[str] = (
                (p.name for p in self.parameters)
                if variadic
                else (p.name for p in self.parameters if not p.variadic)
            )
            yield from it
        else:
            msg = (
                f"Cannot provide `parameter_names` until they have been initialized via:\n"
                f"{type(self).__name__}.with_parameters()"
            )
            raise TypeError(msg)

    def render(self) -> str:
        """Return fully parsed method definition."""
        if self.is_overloaded():
            body_params = STAR_ARGS[1:]
        else:
            body_params = (
                f"({self.parameters[0].name},)"
                if len(self.parameters) == 1
                else f"({','.join(self.parameter_names())})"
            )
        return METHOD_TEMPLATE.format(
            decorator=DECORATOR,
            signature=self.signature,
            doc=self.doc,
            return_wrapper=RETURN_WRAPPER,
            name=f"{self.name!r}",
            body_params=body_params,
        )

    @property
    def title(self) -> str:
        """
        Use for the method definition, but not when calling internally.

        Updates ``remap_title`` class variable for documentation example substitutions.
        """
        title = f"{self.name}_" if self.is_keyword() else self.name
        type(self).remap_title.update({self.name: f"alt.expr.{title}"})
        return title

    def _signature_tokens(self) -> Iterator[Token]:
        """
        Target for signature appears between 2 softbreak tokens.

        - Proceeds to the first token **after** a softbreak
        - Yield **only** text tokens
        - Skips all inline html tags
        - Stops at 2nd softbreak
        """
        it: Iterator[Token] = iter(self)
        current = next(it)
        while current[TYPE] != SOFTBREAK:
            current = next(it)
        next(it)
        for target in it:
            if target[TYPE] == TEXT:
                yield target
            elif target[TYPE] == SOFTBREAK:
                break
            else:
                continue

    def _split_signature_tokens(self, *, exclude_name: bool = False) -> Iterator[str]:
        """
        Normalize the text content of the signature.

        Examples
        --------
        The following definition:

            <a name="sequence" href="#sequence">#</a>
            <b>sequence</b>([<i>start</i>, ]<i>stop</i>[, <i>step</i>])<br/>
            Returns an array containing an arithmetic sequence of numbers.
            ...

        Will yield:

            ['sequence', '(', '[', 'start', ']', 'stop', '[', 'step', ']', ')']

        When called with ``exclude_name=True``:

            ['(', '[', 'start', ']', 'stop', '[', 'step', ']', ')']
        """
        EXCLUDE: set[str] = {", ", "", self.name} if exclude_name else {", ", ""}
        for tok in self._signature_tokens():
            clean = tok[RAW].strip(", -")
            if clean not in EXCLUDE:
                yield from VegaExprDef._split_markers(clean)

    @staticmethod
    def _split_markers(s: str, /) -> Iterator[str]:
        """
        When ``s`` ends with one of these markers:

            ")", "]", "...", " |"

        - Split ``s`` into rest, match
            - using the length of the match to index
        - Append match to ``end``
        - Recurse
        """  # noqa: D400
        if s.isalnum():
            yield s
        else:
            end: list[str] = []
            if s.endswith((CLOSE_PAREN, CLOSE_BRACKET)):
                end.append(s[-1])
                s = s[:-1]
            elif s.endswith(ELLIPSIS):
                end.append(s[-3:])
                s = s[:-3]
            elif s.endswith(INLINE_OVERLOAD):
                end.append(s[-2:])
                s = s[:-2]
            if len(s) == 1:
                yield s
            elif len(s) > 1:
                yield from VegaExprDef._split_markers(s)
            yield from end

    def _doc_tokens(self) -> Sequence[Token]:
        """Return the slice of `self.children` that contains docstring content."""
        for idx, item in enumerate(self):
            if item[TYPE] == SOFTBREAK and self[idx + 1][TYPE] == TEXT:
                return self[idx + 1 :]
            else:
                continue
        msg = (
            f"Expected to find a text node marking the start of docstring content.\n"
            f"Failed for:\n\n{self!r}"
        )
        raise NotImplementedError(msg)

    def is_callable(self) -> bool:
        """
        Rough filter for excluding `constants`_.

        - Most of the parsing is to handle varying signatures.
        - Constants can just be referenced by name, so can skip those

        Notes
        -----
        - Overwriting the <a name> with the rendered text
        - required for `clamprange` -> `clampRange`

        .. _constants:
            https://vega.github.io/vega/docs/expressions/#constants
        """
        if self.is_overloaded_string_array() or self.is_bound_variable_name():
            return False
        it: Iterator[Token] = iter(self)
        current: str = next(it, {}).get(RAW, "")
        name: str = self.name.casefold()
        while current.casefold() != name:
            if (el := next(it, None)) is not None:
                current = el.get(RAW, "")
            else:
                return False
        if current != self.name:
            self.name = current
        next(it)
        return next(it).get(RAW, "") == OPEN_PAREN

    def is_bound_variable_name(self) -> bool:
        """
        ``Vega`` `bound variables`_.

        These do not provide signatures:

            {"datum", "event", "signal"}

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

        Looping of parameters is for signatures like `sequence`_:

            sequence([start, ]stop[, step])

        The optional first parameter, followed by a required one would need an
        ``@overload`` in ``python``.

        .. _color functions:
            https://vega.github.io/vega/docs/expressions/#color-functions
        .. _sequence:
            https://vega.github.io/vega/docs/expressions/#sequence
        """
        for idx, item in enumerate(self):
            if item[TYPE] == TEXT and item.get(RAW, "").endswith(INLINE_OVERLOAD):
                return self[idx + 1][TYPE] == SOFTBREAK
            else:
                continue
        for idx, p in enumerate(self.parameters):
            if not p.required:
                others = self.parameters[idx + 1 :]
                if not others:
                    return False
                else:
                    return any(sp.required for sp in others)

        return False

    def is_overloaded_string_array(self) -> bool:
        """
        HACK: There are string/array functions that overlap.

        - the `.md` handles this by prefixing the `<a name=...` for the string version
        - This is very different to the handled overload kinds
        - Both definitions have full documentation and appear under different sections
            - Unlike color functions, sequence
            - These are inline
        """
        return self.name.startswith("string_")

    def is_keyword(self) -> bool:
        return keyword.iskeyword(self.name)

    def is_incompatible_override(self) -> bool:
        """
        ``self.title`` shadows an unrelated ``SchemaBase`` method.

        Requires an ignore comment for a type checker.
        """
        return self.title in _SCHEMA_BASE_MEMBERS

    def is_variadic(self) -> bool:
        """Position-only parameter separator `"/"` not allowed after `"*"` parameter."""
        return self.is_overloaded() or any(p.variadic for p in self.parameters)

    def __iter__(self) -> Iterator[Token]:
        yield from self._children

    @overload
    def __getitem__(self, index: int) -> Token: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[Token]: ...
    def __getitem__(self, index: int | slice) -> Token | Sequence[Token]:
        return self._children.__getitem__(index)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(\n    "
            f"name={self.name!r},\n    "
            f"parameters={self.parameters!r},\n    "
            f"doc={self.doc!r}\n"
            ")"
        )

    @classmethod
    def from_tokens(cls, tokens: Iterable[Token], /) -> Iterator[Self]:
        """
        Lazy, filtered partial parser.

        Applies a series of filters before rendering everything but the docs.

        Parameters
        ----------
        tokens
            `ast tokens`_ produced by ``mistune``

        .. _ast tokens:
            https://mistune.lepture.com/en/latest/guide.html#abstract-syntax-tree
        """
        for tok in tokens:
            if (
                (children := tok.get(CHILDREN)) is not None
                and (child := next(iter(children)).get(RAW)) is not None
                and (match := FUNCTION_DEF_LINE.match(child))
                and (node := cls(match[1], children)).is_callable()
            ):
                yield node.with_parameters().with_signature()


@dataclasses.dataclass
class VegaExprParam:
    name: str
    required: bool
    variadic: bool = False

    @staticmethod
    def star_args() -> LiteralString:
        return f"{STAR_ARGS}: Any"

    def render(self) -> str:
        """Return as an annotated parameter, with a default if needed."""
        if self.required:
            return f"{self.name}: {INPUT_ANNOTATION}"
        elif not self.variadic:
            return f"{self.name}: {INPUT_ANNOTATION} = {NONE}"
        else:
            return self.star_args()

    @classmethod
    def from_texts(cls, raw_texts: Iterable[str], /) -> Iterator[Self]:
        """Yields an ordered parameter list."""
        is_required: bool = True
        for s in raw_texts:
            if s not in {OPEN_PAREN, CLOSE_PAREN}:
                if s == OPEN_BRACKET:
                    is_required = False
                    continue
                elif s == CLOSE_BRACKET:
                    is_required = True
                    continue
                elif s.isalnum():
                    yield cls(s, required=is_required)
                elif s == ELLIPSIS:
                    yield cls(STAR_ARGS, required=False, variadic=True)
                else:
                    continue


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


def expand_urls(url: str, /) -> str:
    if url.startswith("#"):
        url = f"{EXPRESSIONS_DOCS_URL}{url}"
    else:
        url = url.replace(r"../", VEGA_DOCS_URL)
    return url


def format_doc(doc: str, /) -> str:
    """
    Format rendered docstring content.

    Primarily used to prevent wrapping on `summary line`_ and references.

    Notes
    -----
    - Source is very different to `vega-lite`
    - There are no real sections, so these are created here
    - Single line docs are unchanged
    - Multi-line have everything following the first line wrappped.
        - With a double break inserted for a summary line
    - Reference-like links section (if present) are also ommitted from wrapping

    .. _summary line:
        https://numpydoc.readthedocs.io/en/latest/format.html#short-summary
    """
    sentences: deque[str] = deque(SENTENCE_BREAK.split(doc))
    if len(sentences) > 1:
        references: str = ""
        summary = f"{sentences.popleft()}.\n"
        last_line = sentences.pop().strip()
        sentences = deque(f"{s}. " for s in sentences)
        if SECTION_BREAK in last_line:
            last_line, references = last_line.split(SECTION_BREAK, maxsplit=1)
        sentences.append(last_line)
        sentences = deque(text_wrap.wrap("".join(sentences)))
        sentences.appendleft(summary)
        if references:
            sentences.extend(("", indent(references, METHOD_INDENT)))
        return "\n".join(sentences)
    else:
        return sentences.pop().strip()


def italics_to_backticks(s: str, names: Iterable[str], /) -> str:
    """
    Perform a targeted replacement, considering links.

    Parameters
    ----------
    s
        String containing rendered `.rst`.
    names
        Group of names the replacement applies to.

    Notes
    -----
    - Avoids adding backticks to parameter names that are also used in a link.
    - All cases of these are for `unit|units`.

    Examples
    --------
    >>> italics_to_backticks(
    ...     "some text and *name* and more text but also *other* text",
    ...     ("name", "other"),
    ... )
    "some text and ``name`` and more text but also ``other`` text"
    """
    pattern = rf"(?P<not_link_start>[^`_])\*(?P<name>{'|'.join(names)})\*(?P<not_link_end>[^`])"
    return re.sub(pattern, r"\g<not_link_start>``\g<name>``\g<not_link_end>", s)


def parse_expressions(url: str, /) -> Iterator[VegaExprDef]:
    """
    Download, read markdown and eagerly parse signatures of relevant definitions.

    Yields with docs to ensure each can use all remapped names, regardless of the order they appear.
    """
    tokens = read_ast_tokens(download_expressions_md(url))
    expr_defs = tuple(VegaExprDef.from_tokens(tokens))
    request.urlcleanup()
    VegaExprDef.remap_title.refresh()
    for expr_def in expr_defs:
        yield expr_def.with_doc()


def write_expr_module(
    source_url: Literal["live", "static"] | str, output: Path
) -> None:
    """
    Parse an ``expressions.md`` into a ``.py`` module.

    Parameters
    ----------
    source_url
        - ``"live"``: current version
        - ``"static"``: most recent version available during testing
        - Or provide an alternative as a ``str``
    output
        Target path to write to.
    """
    if source_url == "live":
        url = Source.LIVE.value
    elif source_url == "static":
        url = Source.STATIC.value
    else:
        url = source_url
    content = (
        MODULE_PRE.format(
            metaclass=CLS_META,
            const=CONST_WRAPPER,
            return_ann=RETURN_ANNOTATION,
            input_ann=INPUT_ANNOTATION,
            func=RETURN_WRAPPER,
        ),
        CLS_TEMPLATE.format(
            base="_ExprRef",
            metaclass=CLS_META,
            doc=CLS_DOC,
            type_ignore=IGNORE_MISC,
        ),
    )
    contents = chain(
        content,
        (expr_def.render() for expr_def in parse_expressions(url)),
        [MODULE_POST],
    )
    print(f"Generating\n {url!s}\n  ->{output!s}")
    _ruff_write_lint_format_str(output, contents)
