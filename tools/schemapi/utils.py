"""Utilities for working with schemas."""

from __future__ import annotations

import json
import re
import sys
import textwrap
import urllib.parse
from collections import deque
from collections.abc import Sequence
from contextlib import AbstractContextManager
from copy import deepcopy
from itertools import chain
from keyword import iskeyword
from operator import itemgetter
from typing import TYPE_CHECKING, Generic, Literal, TypeVar, Union, overload

from tools.codemod import ruff
from tools.markup import RSTParseVegaLite, rst_syntax_for_class
from tools.schemapi.schemapi import _resolve_references as resolve_references

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator, KeysView, Mapping
    from pathlib import Path
    from re import Pattern
    from typing import Any, ClassVar

    from _typeshed import SupportsKeysAndGetItem


if sys.version_info >= (3, 12):
    from typing import TypeAliasType
else:
    from typing_extensions import TypeAliasType
if sys.version_info >= (3, 11):
    from typing import LiteralString, Never
else:
    from typing_extensions import LiteralString, Never
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

T = TypeVar("T")

OneOrSeq = TypeAliasType("OneOrSeq", Union[T, Sequence[T]], type_params=(T,))
TargetType: TypeAlias = Literal["annotation", "doc"]

EXCLUDE_KEYS: frozenset[
    Literal["definitions", "title", "description", "$schema", "id"]
] = frozenset(("definitions", "title", "description", "$schema", "id"))
COMPOUND_KEYS: tuple[Literal["anyOf"], Literal["oneOf"], Literal["allOf"]] = (
    "anyOf",
    "oneOf",
    "allOf",
)
jsonschema_to_python_types: dict[str, str] = {
    "string": "str",
    "number": "float",
    "integer": "int",
    "object": "Map",
    "boolean": "bool",
    "array": "list",
    "null": "None",
}
_STDLIB_TYPE_NAMES = frozenset(
    (
        "int",
        "float",
        "str",
        "None",
        "bool",
        "date",
        "datetime",
        "time",
        "tuple",
        "list",
        "deque",
        "dict",
        "set",
    )
)

_VALID_IDENT: Pattern[str] = re.compile(r"^[^\d\W]\w*\Z", re.ASCII)

_RE_LIST_MISSING_ASTERISK: Pattern[str] = re.compile(r"^-(?=[ `\"a-z])", re.MULTILINE)
_RE_LIST_MISSING_WHITESPACE: Pattern[str] = re.compile(r"^\*(?=[`\"a-z])", re.MULTILINE)

_HASH_ENCODER = json.JSONEncoder(sort_keys=True, separators=(",", ":"))


class _TypeAliasTracer:
    """
    Recording all `enum` -> `Literal` translations.

    Rewrites as `TypeAlias` to be reused anywhere, and not clog up method definitions.

    Parameters
    ----------
    fmt
        A format specifier to produce the `TypeAlias` name.

        Will be provided a `SchemaInfo.title` as a single positional argument.

    Attributes
    ----------
    _literals: dict[str, str]
        `{alias_name: literal_statement}`
    _literals_invert: dict[str, str]
        `{literal_statement: alias_name}`
    aliases: list[tuple[str, str]]
        `_literals` sorted by `alias_name`
    _imports: Sequence[str]
        Prefined import statements to appear at beginning of module.
    """

    def __init__(self, fmt: str = "{}_T") -> None:
        self.fmt: str = fmt
        self._literals: dict[str, str] = {}
        self._literals_invert: dict[str, str] = {}
        self._aliases: dict[str, str] = {}
        self._imports: Sequence[str] = (
            "from __future__ import annotations\n",
            "import sys",
            "from datetime import date, datetime",
            "from typing import Annotated, Any, Generic, Literal, Mapping, TypeVar, Sequence, Union, get_args",
            "import re",
            import_typing_extensions(
                (3, 14), "TypedDict", reason="https://peps.python.org/pep-0728/"
            ),
            import_typing_extensions((3, 13), "TypeIs"),
            import_typing_extensions((3, 12), "TypeAliasType"),
            import_typing_extensions((3, 11), "LiteralString"),
            import_typing_extensions((3, 10), "TypeAlias"),
        )

    def _update_literals(self, name: str, tp: str, /) -> None:
        """Produces an inverted index, to reuse a `Literal` when `SchemaInfo.title` is empty."""
        self._literals[name] = tp
        self._literals_invert[tp] = name

    def add_literal(
        self, info: SchemaInfo, tp: str, /, *, replace: bool = False
    ) -> str:
        """
        `replace=True` returns the eventual alias name.

        - Doing so will mean that the `_typing` module must be written first, before the source of `info`.
        - Otherwise, `ruff` will raise an error during `check`/`format`, as the import will be invalid.
        - Where a `title` is not found, an attempt will be made to find an existing alias definition that had one.
        """
        if info.title:
            alias = self.fmt.format(info.title)
            if alias not in self._literals:
                self._update_literals(alias, tp)
            if replace:
                tp = alias
        elif (alias := self._literals_invert.get(tp, "")) and replace:
            tp = alias
        elif replace and info.is_union_literal():
            # Handles one very specific edge case `WindowFieldDef`
            # - Has an anonymous enum union
            # - One of the members is declared afterwards
            # - SchemaBase needs to be first, as the union wont be internally sorted
            it = (
                self.add_literal(el, spell_literal(el.literal), replace=True)
                for el in info.anyOf
            )
            tp = f"Union[SchemaBase, {', '.join(it)}]"
        return tp

    def add_union(
        self, info: SchemaInfo, tp_iter: Iterator[str], /, *, replace: bool = False
    ) -> str:
        if title := info.title:
            alias = self.fmt.format(title)
            if alias not in self._aliases:
                self.update_aliases(
                    (alias, f"Union[{', '.join(sort_type_reprs(tp_iter))}]")
                )
            return alias if replace else title
        else:
            msg = f"Unsupported operation.\nRequires a title.\n\n{info!r}"
            raise NotImplementedError(msg)

    def update_aliases(self, *name_statement: tuple[str, str]) -> None:
        """
        Adds `(name, statement)` pairs to the definitions.

        These types should support annotations in generated code, but
        are not required to be derived from the schema itself.

        Each tuple will appear in the generated module as::

            name: TypeAlias = statement

        All aliases will be written in runtime-scope, therefore
        externally dependent types should be declared as regular imports.
        """
        self._aliases.update(name_statement)

    def generate_aliases(self) -> Iterator[str]:
        """Represents a line per `TypeAlias` declaration."""
        for name, statement in self._aliases.items():
            yield f"{name}: TypeAlias = {statement}"

    def is_cached(self, tp: str, /, *, include_concrete: bool = False) -> bool:
        """
        Applies to both docstring and type hints.

        Currently used as a sort key, to place literals/aliases last.
        """
        return (
            tp in self._literals_invert or tp in self._literals or tp in self._aliases
        ) or (include_concrete and self.fmt.format(tp) in self._literals)

    def write_module(
        self, fp: Path, *extra_all: str, header: LiteralString, extra: LiteralString
    ) -> None:
        """
        Write all collected `TypeAlias`'s to `fp`.

        Parameters
        ----------
        fp
            Path to new module.
        *extra_all
            Any manually spelled types to be exported.
        header
            `tools.generate_schema_wrapper.HEADER`.
        extra
            `tools.generate_schema_wrapper.TYPING_EXTRA`.
        """
        static = (header, "\n", *self._imports, "\n\n")
        self.update_aliases(*sorted(self._literals.items(), key=itemgetter(0)))
        all_ = [*iter(self._aliases), *extra_all]
        it = chain(
            static,
            [f"__all__ = {all_}", "\n\n", extra],
            self.generate_aliases(),
        )
        ruff.write_lint_format(fp, it)

    @property
    def n_entries(self) -> int:
        """Number of unique `TypeAlias` defintions collected."""
        return len(self._literals)


def get_valid_identifier(
    prop: str,
    replacement_character: str = "",
    allow_unicode: bool = False,
    url_decode: bool = True,
) -> str:
    """
    Given a string property, generate a valid Python identifier.

    Parameters
    ----------
    prop: string
        Name of property to decode.
    replacement_character: string, default ''
        The character to replace invalid characters with.
    allow_unicode: boolean, default False
        If True, then allow Python 3-style unicode identifiers.
    url_decode: boolean, default True
        If True, decode URL characters in identifier names.

    Examples
    --------
    >>> get_valid_identifier("my-var")
    'myvar'

    >>> get_valid_identifier("if")
    'if_'

    >>> get_valid_identifier("$schema", "_")
    '_schema'

    >>> get_valid_identifier("$*#$")
    '_'

    >>> get_valid_identifier("Name%3Cstring%3E")
    'Namestring'
    """
    # Decode URL characters.
    if url_decode:
        prop = urllib.parse.unquote(prop)

    # Deal with []
    prop = prop.replace("[]", "Array")

    # First substitute-out all non-valid characters.
    flags = re.UNICODE if allow_unicode else re.ASCII
    valid = re.sub(r"\W", replacement_character, prop, flags=flags)

    # If nothing is left, use just an underscore
    if not valid:
        valid = "_"

    # first character must be a non-digit. Prefix with an underscore
    # if needed
    if re.match(r"^[\d\W]", valid):
        valid = "_" + valid

    # if the result is a reserved keyword, then add an underscore at the end
    if iskeyword(valid):
        valid += "_"
    return valid


def is_valid_identifier(s: str, /) -> bool:
    """Return ``True`` if ``s`` contains a valid Python identifier."""
    return _VALID_IDENT.match(s) is not None and not iskeyword(s)


class SchemaProperties:
    """A wrapper for properties within a schema."""

    def __init__(
        self,
        properties: Mapping[str, Any],
        schema: Mapping[str, Any],
        rootschema: Mapping[str, Any] | None = None,
    ) -> None:
        self._properties: Mapping[str, Any] = properties
        self._schema: Mapping[str, Any] = schema
        self._rootschema: Mapping[str, Any] = rootschema or schema

    def __bool__(self) -> bool:
        return bool(self._properties)

    def __dir__(self) -> list[str]:
        return list(self._properties.keys())

    def __getattr__(self, attr) -> SchemaInfo:
        return self[attr]

    def __getitem__(self, attr) -> SchemaInfo:
        dct = self._properties[attr]
        if "definitions" in self._schema and "definitions" not in dct:
            dct = dict(definitions=self._schema["definitions"], **dct)
        return SchemaInfo(dct, self._rootschema)

    def __iter__(self) -> Iterator[str]:
        return iter(self._properties)

    def __len__(self) -> int:
        return len(self._properties)

    def items(self) -> Iterator[tuple[str, SchemaInfo]]:
        return ((key, self[key]) for key in self)

    def keys(self) -> KeysView[str]:
        return self._properties.keys()

    def values(self) -> Iterator[SchemaInfo]:
        return (self[key] for key in self)


class SchemaInfo:
    """A wrapper for inspecting a JSON schema."""

    _remap_title: ClassVar[dict[str, Sequence[str]]] = {}

    def __init__(
        self, schema: Mapping[str, Any], rootschema: Mapping[str, Any] | None = None
    ) -> None:
        if not rootschema:
            rootschema = schema
        self.raw_schema: Mapping[str, Any]
        self.rootschema: Mapping[str, Any]
        self.schema: Mapping[str, Any]
        object.__setattr__(self, "raw_schema", schema)
        object.__setattr__(self, "rootschema", rootschema)
        object.__setattr__(self, "schema", resolve_references(schema, rootschema))  # type: ignore

    @classmethod
    def from_refname(cls, refname: str, /, rootschema: Mapping[str, Any]) -> SchemaInfo:
        return cls({"$ref": f"#/definitions/{refname}"}, rootschema)

    def __setattr__(self, name: str, value: Any) -> Never:
        msg = f"{type(self).__name__!r} is immutable.\nCould not assign self.{name} = {value}"
        raise TypeError(msg)

    def __hash__(self) -> int:
        return hash(_HASH_ENCODER.encode(self.schema))

    def __eq__(self, value: object) -> bool:
        if isinstance(value, SchemaInfo):
            if self.ref:
                return self.ref == value.ref
            return self.schema == value.schema
        return False

    def child(self, schema: dict[str, Any]) -> SchemaInfo:
        return self.__class__(schema, rootschema=self.rootschema)

    def iter_descendants(self) -> Iterator[SchemaInfo]:
        """Yields `properties`, `anyOf`, `items`."""
        if "properties" in self.schema:
            yield from self.properties.values()
        if "anyOf" in self.schema:
            yield from self.anyOf
        if self.items:
            yield self.child(self.items)

    def __repr__(self) -> str:
        keys = []
        for key in sorted(self.schema.keys()):
            val = self.schema[key]
            rval = repr(val).replace("\n", "")
            if len(rval) > 30:
                rval = rval[:30] + "..."
            if key == "definitions":
                rval = "{...}"
            elif key == "properties":
                rval = "{\n    " + "\n    ".join(sorted(map(repr, val))) + "\n  }"
            keys.append(f'"{key}": {rval}')
        return "SchemaInfo({\n  " + "\n  ".join(keys) + "\n})"

    @property
    def title(self) -> str:
        if self.is_reference():
            return get_valid_identifier(self.refname)
        else:
            return ""

    @overload
    def to_type_repr(
        self,
        *,
        as_str: Literal[True] = ...,
        target: TargetType = ...,
        use_concrete: bool = ...,
        use_undefined: bool = ...,
    ) -> str: ...
    @overload
    def to_type_repr(
        self,
        *,
        as_str: Literal[False],
        target: TargetType = ...,
        use_concrete: bool = ...,
        use_undefined: bool = ...,
    ) -> list[str]: ...
    def to_type_repr(  # noqa: C901
        self,
        *,
        as_str: bool = True,
        target: TargetType = "doc",
        use_concrete: bool = False,
        use_undefined: bool = False,
    ) -> str | list[str]:
        """
        Return the python type representation of ``SchemaInfo``.

        Includes `altair` classes, standard `python` types, etc.

        Parameters
        ----------
        as_str
            Return as a string.
            Should only be ``False`` during internal recursive calls.
        target: {"annotation", "doc"}
            Where the representation will be used.
        use_concrete
            Avoid base classes/wrappers that don't provide type info.
        use_undefined
            Wrap the result in ``altair.typing.Optional``.
        """
        tps: set[str] = set()
        FOR_TYPE_HINTS: bool = target == "annotation"

        if self.title:
            if target == "annotation":
                tps.update(self.title_to_type_reprs(use_concrete=use_concrete))
            elif target == "doc":
                tps.add(rst_syntax_for_class(self.title))

        if self.is_empty():
            tps.add("Any")
        elif self.is_literal():
            tp_str = spell_literal(self.literal)
            if FOR_TYPE_HINTS:
                tp_str = TypeAliasTracer.add_literal(self, tp_str, replace=True)
            tps.add(tp_str)
        elif FOR_TYPE_HINTS and self.is_union_literal():
            it: Iterator[str] = chain.from_iterable(el.literal for el in self.anyOf)
            tp_str = TypeAliasTracer.add_literal(self, spell_literal(it), replace=True)
            tps.add(tp_str)
        elif self.is_anyOf():
            it_nest = (
                s.to_type_repr(target=target, as_str=False, use_concrete=use_concrete)
                for s in self.anyOf
            )
            tps.update(maybe_rewrap_literal(chain.from_iterable(it_nest)))
        elif FOR_TYPE_HINTS and self.is_type_alias_union():
            it = (
                SchemaInfo(dict(self.schema, type=tp)).to_type_repr(
                    target=target, use_concrete=use_concrete
                )
                for tp in self.type
            )
            tps.add(TypeAliasTracer.add_union(self, it, replace=True))
        elif isinstance(self.type, list):
            # We always use title if possible for nested objects
            tps.update(
                SchemaInfo(dict(self.schema, type=tp)).to_type_repr(
                    target=target, use_concrete=use_concrete
                )
                for tp in self.type
            )
        elif self.is_array():
            tps.add(
                spell_nested_sequence(self, target=target, use_concrete=use_concrete)
            )
        elif self.type in jsonschema_to_python_types:
            if self.is_object() and use_concrete:
                ...  # HACK: Fall-through case to avoid `dict` added to `TypedDict`
            elif self.is_object() and target == "doc":
                tps.add("dict")
            else:
                tps.add(jsonschema_to_python_types[self.type])
        else:
            msg = "No Python type representation available for this schema"
            raise ValueError(msg)

        if use_concrete:
            if tps >= {"ColorHex", TypeAliasTracer.fmt.format("ColorName"), "str"}:
                # HACK: Remove regular `str` if HEX & CSS color codes are present as well
                tps.discard("str")
            elif len(tps) == 0 and as_str:
                # HACK: There is a single case that ends up empty here
                # See: https://github.com/vega/altair/pull/3536#discussion_r1714344162
                tps = {"Map"}
        return (
            finalize_type_reprs(tps, target=target, use_undefined=use_undefined)
            if as_str
            else sort_type_reprs(tps)
        )

    @classmethod
    def to_type_repr_batched(
        cls,
        infos: Iterable[SchemaInfo],
        /,
        *,
        target: TargetType = "doc",
        use_concrete: bool = False,
        use_undefined: bool = False,
    ) -> str:
        """
        Return the python type representation of multiple ``SchemaInfo``.

        Intended to handle a subset of a ``Union``.

        Parameters
        ----------
        infos
            Schemas to collapse into a single representation.
        target: {"annotation", "doc"}
            Where the representation will be used.
        use_concrete
            Avoid base classes/wrappers that don't provide type info.
        use_undefined
            Wrap the result in ``altair.typing.Optional``.

        See Also
        --------
        - ``SchemaInfo.to_type_repr``
        """
        it: Iterator[str] = chain.from_iterable(
            info.to_type_repr(
                as_str=False,
                target=target,
                use_concrete=use_concrete,
                use_undefined=False,
            )
            for info in infos
        )
        return finalize_type_reprs(it, target=target, use_undefined=use_undefined)

    def title_to_type_reprs(self, *, use_concrete: bool) -> set[str]:
        """
        Possibly use ``self.title`` as a type, or provide alternative(s).

        Parameters
        ----------
        use_concrete
            Avoid base classes/wrappers that don't provide type info.
        """
        tp_param: set[str] = {"ExprRef", "ParameterExtent"}
        # In these cases, a `VariableParameter` is also always accepted.
        # It could be difficult to differentiate `(Variable|Selection)Parameter`, with typing.
        # TODO: A solution could be defining `Parameter` as generic over either `param` or `param_type`.
        # - Rewriting the init logic to not use an `Undefined` default.
        # - Any narrowing logic could be factored-out into `is_(selection|variable)_parameter` guards.
        EXCLUDE_TITLE: set[str] = tp_param | {"RelativeBandSize"}
        """
        `RelativeBandSize` excluded as it has a single property `band`,
        but all instances also accept `float`.
        """
        REMAP_TITLE = SchemaInfo._remap_title
        title: str = self.title
        tps: set[str] = set()
        if not use_concrete:
            tps.add("SchemaBase")
            # NOTE: To keep type hints simple, we annotate with `SchemaBase` for all subclasses.
            if title in tp_param:
                tps.add("Parameter")
            if self.is_datetime():
                tps.add("Temporal")
        elif self.is_value():
            value = self.properties["value"]
            t = value.to_type_repr(target="annotation", use_concrete=use_concrete)
            tps.add(f"Value[{t}]")
        elif self.is_rowcol():
            row = self.properties["row"]
            t = row.to_type_repr(target="annotation", use_concrete=use_concrete)
            tps.add(f"RowColKwds[{t}]")
        elif title in REMAP_TITLE:
            tps.update(REMAP_TITLE[title])
        elif (
            (title not in EXCLUDE_TITLE)
            and not TypeAliasTracer.is_cached(title, include_concrete=use_concrete)
            and not self.is_union()
            and not self.is_format()
            and not self.is_array()
            and not self.is_type_alias()
            and not self.additionalProperties
        ):
            tps.add(title)
        return tps

    @property
    def properties(self) -> SchemaProperties:
        return SchemaProperties(
            self.schema.get("properties", {}), self.schema, self.rootschema
        )

    @property
    def definitions(self) -> SchemaProperties:
        return SchemaProperties(
            self.schema.get("definitions", {}), self.schema, self.rootschema
        )

    @property
    def required(self) -> list[str]:
        return self.schema.get("required", [])

    @property
    def patternProperties(self) -> dict[str, Any]:
        return self.schema.get("patternProperties", {})

    @property
    def additionalProperties(self) -> bool:
        return self.schema.get("additionalProperties", True)

    @property
    def type(self) -> str | list[Any]:
        return self.schema.get("type", "")

    @property
    def anyOf(self) -> Iterator[SchemaInfo]:
        for s in self.schema.get("anyOf", []):
            yield self.child(s)

    @property
    def oneOf(self) -> Iterator[SchemaInfo]:
        for s in self.schema.get("oneOf", []):
            yield self.child(s)

    @property
    def allOf(self) -> Iterator[SchemaInfo]:
        for s in self.schema.get("allOf", []):
            yield self.child(s)

    @property
    def not_(self) -> SchemaInfo:
        return self.child(self.schema.get("not", {}))

    @property
    def items(self) -> dict[str, Any]:
        return self.schema.get("items", {})

    @property
    def enum(self) -> list[str]:
        return self.schema.get("enum", [])

    @property
    def const(self) -> str:
        return self.schema.get("const", "")

    @property
    def literal(self) -> list[str]:
        return self.schema.get("enum", [self.const])

    @property
    def refname(self) -> str:
        return self.raw_schema.get("$ref", "#/").split("/")[-1]

    @property
    def ref(self) -> str:
        return self.raw_schema.get("$ref", "")

    @property
    def description(self) -> str:
        return self._get_description(include_sublevels=False)

    @property
    def deep_description(self) -> str:
        return process_description(self._get_description(include_sublevels=True))

    def _get_description(self, include_sublevels: bool = False) -> str:
        desc = self.raw_schema.get("description", self.schema.get("description", ""))
        if not desc and include_sublevels:
            for item in self.anyOf:
                sub_desc = item._get_description(include_sublevels=False)
                if desc and sub_desc:
                    raise ValueError(
                        "There are multiple potential descriptions which could"
                        + " be used for the currently inspected schema. You'll need to"
                        + " clarify which one is the correct one.\n"
                        + str(self.schema)
                    )
                if sub_desc:
                    desc = sub_desc
        return desc

    def is_reference(self) -> bool:
        return "$ref" in self.raw_schema

    def is_enum(self) -> bool:
        return "enum" in self.schema

    def is_const(self) -> bool:
        return "const" in self.schema

    def is_literal(self) -> bool:
        """
        Return True for `const`_ or `enum`_ values.

        JSON Schema distinguishes between singular/multiple values.

        But we annotate them both the same way:

            ConstInfo = Literal["single value"]
            EnumInfo = Literal["value 1", "value 2", "value 3"]

        .. _const:
            https://json-schema.org/understanding-json-schema/reference/const
        .. _enum:
            https://json-schema.org/understanding-json-schema/reference/enum
        """
        return not ({"enum", "const"}.isdisjoint(self.schema))

    def is_empty(self) -> bool:
        return not (self.schema.keys() - EXCLUDE_KEYS)

    def is_compound(self) -> bool:
        return any(key in self.schema for key in COMPOUND_KEYS)

    def is_anyOf(self) -> bool:
        return "anyOf" in self.schema

    def is_allOf(self) -> bool:
        return "allOf" in self.schema

    def is_oneOf(self) -> bool:
        return "oneOf" in self.schema

    def is_not(self) -> bool:
        return "not" in self.schema

    def is_object(self) -> bool:
        if self.type == "object":
            return True
        elif self.type:
            return False
        elif (
            self.properties
            or self.required
            or self.additionalProperties
            or self.patternProperties
        ):
            return True
        else:
            msg = "Unclear whether schema.is_object() is True"
            raise ValueError(msg)

    def is_value(self) -> bool:
        return self.is_object() and self.properties.keys() == {"value"}

    def is_rowcol(self) -> bool:
        props = self.properties
        return (
            self.is_object()
            and props.keys() == {"column", "row"}
            and props["column"] == props["row"]
        )

    def is_array(self) -> bool:
        return self.type == "array"

    def is_union(self) -> bool:
        """
        Candidate for ``Union`` type alias.

        Not a real class.
        """
        return self.is_anyOf() and not self.type

    def is_union_literal(self) -> bool:
        """
        Candidate for reducing to a single ``Literal`` alias.

        E.g. `BinnedTimeUnit`
        """
        return self.is_union() and all(el.is_literal() for el in self.anyOf)

    def is_primitive(self) -> bool:
        """
        A basic JSON Schema `type`_ or an array of **only** basic types.

        .. _type:
        https://json-schema.org/understanding-json-schema/reference/type
        """
        TP = "type"
        return (self.schema.keys() == {TP}) or (
            self.is_array() and self.child(self.items).is_primitive()
        )

    def is_flattenable(self) -> bool:
        """
        Represents a range of cases we want to annotate in ``@overload``(s).

        Examples
        --------
        The following are non-exhaustive examples, using ``python`` types.

        Base cases look like:

            Literal["left", "center", "right"]
            float
            Sequence[str]

        We also include compound cases, but only when **every** member meets these criteria:

            Literal["pad", "none", "fit"] | None
            float | Sequence[float]
            Sequence[str] | str | bool | float | None
        """
        return self.is_literal() or self.is_primitive() or self.is_union_flattenable()

    def is_union_flattenable(self) -> bool:
        """
        Represents a fully flattenable ``Union``.

        Used to prevent ``@overload`` explosion in ``channels.py``

        Requires **every** member of the ``Union`` satisfies *at least* **one** the criteria.

        See Also
        --------
        - ``SchemaInfo.is_literal``
        - ``SchemaInfo.is_array``
        - ``SchemaInfo.is_primitive``
        - ``SchemaInfo.is_flattenable``
        """
        if not self.is_union():
            return False
        else:
            fns = (
                SchemaInfo.is_literal,
                SchemaInfo.is_array,
                SchemaInfo.is_primitive,
                SchemaInfo.is_union_flattenable,
            )
            return all(any(fn(el) for fn in fns) for el in self.anyOf)

    def is_format(self) -> bool:
        """
        Represents a string format specifier.

        These do not currently produce useful classes (e.g. ``HexColor``, ``URI``).

        See Also
        --------
        [python-jsonschema](https://python-jsonschema.readthedocs.io/en/latest/faq/#my-schema-specifies-format-validation-why-do-invalid-instances-seem-valid)
        """
        return (self.schema.keys() == {"format", "type"}) and self.type == "string"

    def is_type_alias(self) -> bool:
        """
        Represents a name assigned to a literal type.

        At the time of writing, most of these are:

            SchemaInfo.schema = {"type": "string"}

        The resulting annotation then becomes, e.g. ``FieldName``:

            arg: str | FieldName

        Where both of the above represent:

            arg = "name 1"
            arg = FieldName("name 1")

        The latter is not useful and adds noise.

        ``Dict`` is very similar case, with a *slightly* different schema:

            SchemaInfo.schema = {"additionalProperties": {}, "type": "object"}
        """
        TP = "type"
        ADDITIONAL = "additionalProperties"
        keys = self.schema.keys()
        return (
            (
                (keys == {TP})
                or (keys == {TP, ADDITIONAL} and self.schema[ADDITIONAL] == {})
            )
            and isinstance(self.type, str)
            and self.type in jsonschema_to_python_types
        )

    def is_type_alias_union(self) -> bool:
        """
        Represents a name assigned to a list of literal types.

        Example:

            {"PrimitiveValue": {"type": ["number", "string", "boolean", "null"]}}

        Translating from JSON -> Python, this is the same as an ``"anyOf"`` -> ``Union``.

        The distinction in the schema is purely due to these types being defined in the draft, rather than definitions.
        """
        TP = "type"
        return (
            self.schema.keys() == {TP}
            and isinstance(self.type, list)
            and bool(self.title)
        )

    def is_theme_config_target(self) -> bool:
        """
        Return `True` for candidates  classes in ``ThemeConfig`` hierarchy of ``TypedDict``(s).

        Satisfying these rules ensures:
        - we generate meaningful annotations
        - they improve autocompletion, without overwhelming the UX
        """
        EXCLUDE = {"ExprRef", "ParameterPredicate", "RelativeBandSize"}
        return bool(
            self.ref
            and self.refname not in EXCLUDE
            and self.properties
            and self.type == "object"
            and not self.is_value()
            and "field" not in self.required
            and not (iskeyword(next(iter(self.required), "")))
        )

    def is_datetime(self) -> bool:
        return self.refname == "DateTime"


class Grouped(Generic[T]):
    """
    Simple group-by like utility.

    Intended for consuming an iterator in full, splitting into true/false cases.

    Parameters
    ----------
    iterable
        Elements to divide into two groups.
    predicate
        Function to classify each element.

    Attributes
    ----------
    truthy: deque[T]
        Elements which pass ``predicate``.
    falsy: deque[T]
        Elements which fail ``predicate``.
    """

    def __init__(
        self, iterable: Iterable[T], /, predicate: Callable[[T], bool]
    ) -> None:
        truthy, falsy = deque[T](), deque[T]()
        for el in iterable:
            if predicate(el):
                truthy.append(el)
            else:
                falsy.append(el)
        self.truthy: deque[T] = truthy
        self.falsy: deque[T] = falsy


class RemapContext(AbstractContextManager):
    """
    Context Manager to temporarily apply substitution rules for ``SchemaInfo``.

    Upon exiting, the original rules will be in effect.

    Notes
    -----
    The constructor accepts arguments exactly the same way as ``dict``.
    """

    def __init__(
        self,
        m: SupportsKeysAndGetItem[str, Sequence[str]]
        | Iterable[tuple[str, Sequence[str]]] = (),
        /,
        **kwds: Sequence[str],
    ) -> None:
        self._mapping: Mapping[str, Sequence[str]] = dict(m, **kwds)
        self._orig: Mapping[str, Sequence[str]]

    def __enter__(self) -> Any:
        self._orig = deepcopy(SchemaInfo._remap_title)
        SchemaInfo._remap_title.update(self._mapping)
        return self

    def __exit__(self, *args) -> None:
        SchemaInfo._remap_title = dict(**self._orig)
        del self._orig


def flatten(container: Iterable) -> Iterable:
    """
    Flatten arbitrarily flattened list.

    From https://stackoverflow.com/a/10824420
    """
    for i in container:
        if isinstance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i


def finalize_type_reprs(
    tps: Iterable[str],
    /,
    *,
    target: TargetType,
    use_undefined: bool = False,
) -> str:
    """
    Deduplicates, sorts, and returns ``tps`` as a single string.

    Parameters
    ----------
    tps
        Collected type representations.
    target
        Destination for the type.

        .. note::
            `"doc"` skips ``(Union|Optional)`` wrappers.

    use_undefined
        Wrap the result in `altair.typing.Optional`.
        Avoids exposing `UndefinedType`.
    """
    return _collapse_type_repr(
        sort_type_reprs(tps), target=target, use_undefined=use_undefined
    )


def _collapse_type_repr(
    tps: Iterable[str],
    /,
    *,
    target: TargetType,
    use_undefined: bool = False,
) -> str:
    """
    Flatten unique types into a single string.

    See Also
    --------
    - ``utils.finalize_type_reprs``
    """
    tp_str = ", ".join(tps)
    if target == "doc":
        return tp_str
    elif target == "annotation":
        if "," in tp_str:
            tp_str = f"Union[{tp_str}]"
        return f"Optional[{tp_str}]" if use_undefined else tp_str
    else:
        msg = f"Unexpected {target=}.\nUse one of {['annotation', 'doc']!r}"
        raise TypeError(msg)


def sort_type_reprs(tps: Iterable[str], /) -> list[str]:
    """
    Shorter types are usually the more relevant ones, e.g. `str` instead of `SchemaBase`.

    We use `set`_ for unique elements, but the lack of ordering requires additional sorts:
    - If types have same length names, order would still be non-deterministic
    - Hence, we sort as well by type name as a tie-breaker, see `sort-stability`_.
    - Using ``str.lower`` gives priority to `builtins`_.
    - Lower priority is given to generated aliases from ``TypeAliasTracer``.
        - These are purely to improve autocompletion
    - ``None`` will always appear last.

    Related
    -------
    - https://github.com/vega/altair/pull/3573#discussion_r1747121600

    Examples
    --------
    >>> sort_type_reprs(["float", "None", "bool", "Chart", "float", "bool", "Chart", "str"])
    ['str', 'bool', 'float', 'Chart', 'None']

    >>> sort_type_reprs(("None", "int", "Literal[5]", "int", "float"))
    ['int', 'float', 'Literal[5]', 'None']

    >>> sort_type_reprs({"date", "int", "str", "datetime", "Date"})
    ['int', 'str', 'date', 'datetime', 'Date']

    .. _set:
        https://docs.python.org/3/tutorial/datastructures.html#sets
    .. _sort-stability:
        https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
    .. _builtins:
        https://docs.python.org/3/library/functions.html
    """
    dedup = tps if isinstance(tps, set) else set(tps)
    it = sorted(dedup, key=str.lower)  # Quinary sort
    it = sorted(it, key=len)  # Quaternary sort
    it = sorted(it, key=TypeAliasTracer.is_cached)  # Tertiary sort
    it = sorted(it, key=is_not_stdlib)  # Secondary sort
    it = sorted(it, key=is_none)  # Primary sort
    return it


def is_not_stdlib(s: str, /) -> bool:
    """
    Sort key.

    Places a subset of stdlib types at the **start** of list.
    """
    return s not in _STDLIB_TYPE_NAMES


def is_none(s: str, /) -> bool:
    """
    Sort key.

    Always places ``None`` at the **end** of list.
    """
    return s == "None"


def spell_nested_sequence(
    info: SchemaInfo, *, target: TargetType, use_concrete: bool
) -> str:
    """
    Return a type representation for an array.

    Notes
    -----
    A list is invariant in its type parameter.

    This means that ``list[str]`` is not a subtype of ``list[FieldName | str]``
    and hence we would need to explicitly write out the combinations,
    so in this case:

        Accepted: list[FieldName] | list[str] | list[FieldName | str]

    However, this can easily explode to too many combinations.

    Furthermore, we would also need to add additional entries
    for e.g. ``int`` wherever a ``float`` is accepted which would lead to very
    long code.

    As suggested in the `mypy docs`_ we revert to using ``Sequence``.

    This includes ``list``, ``tuple`` and many others supported by ``SchemaBase.to_dict``.

    The original example becomes:

        Accepted: Sequence[FieldName | str]

    .. _mypy docs:
        https://mypy.readthedocs.io/en/stable/common_issues.html#variance

    """
    child: SchemaInfo = info.child(info.items)
    s = child.to_type_repr(target=target, use_concrete=use_concrete)
    return f"Sequence[{s}]"


def spell_literal(it: Iterable[str], /, *, quote: bool = True) -> str:
    """
    Combine individual ``str`` type reprs into a single ``Literal``.

    Parameters
    ----------
    it
        Type representations.
    quote
        Call ``repr()`` on each element in ``it``.

        .. note::
            Set to ``False`` if performing a second pass.
    """
    it_el: Iterable[str] = (f"{s!r}" for s in it) if quote else it
    return f"Literal[{', '.join(it_el)}]"


def maybe_rewrap_literal(it: Iterable[str], /) -> Iterator[str]:
    """
    Where `it` may contain one or more `"enum"`, `"const"`, flatten to a single `Literal[...]`.

    All other type representations are yielded unchanged.
    """
    seen: set[str] = set()
    for s in it:
        if s.startswith("Literal["):
            seen.add(unwrap_literal(s))
        else:
            yield s
    if seen:
        yield spell_literal(sorted(seen), quote=False)


def unwrap_literal(tp: str, /) -> str:
    """`"Literal['value']"` -> `"value"`."""
    return re.sub(r"Literal\[(.+)\]", r"\g<1>", tp)


def import_type_checking(*imports: str) -> str:
    """Write an `if TYPE_CHECKING` block."""
    imps = "\n".join(f"    {s}" for s in imports)
    return f"\nif TYPE_CHECKING:\n    # ruff: noqa: F405\n{imps}\n"


def import_typing_extensions(
    version_added: tuple[float, float],
    /,
    *symbol_names: str,
    reason: str | None = None,
    include_sys: bool = False,
) -> str:
    major, minor = version_added
    names = ", ".join(symbol_names)
    line_1 = "import sys\n" if include_sys else "\n"
    comment = f" # {reason}" if reason else ""
    return (
        f"{line_1}"
        f"if sys.version_info >= ({major}, {minor}):{comment}\n    "
        f"from typing import {names}\n"
        f"else:\n    "
        f"from typing_extensions import {names}"
    )


TypeAliasTracer: _TypeAliasTracer = _TypeAliasTracer("{}_T")
"""An instance of `_TypeAliasTracer`.

Collects a cache of unique `Literal` types used globally.

These are then converted to `TypeAlias` statements, written to another module.

Allows for a single definition to be reused multiple times,
rather than repeating long literals in every method definition.
"""


def indent_docstring(  # noqa: C901
    lines: Iterable[str], indent_level: int, width: int = 100, lstrip=True
) -> str:
    """Indent a docstring for use in generated code."""
    final_lines = []
    if not isinstance(lines, list):
        lines = list(lines)
    if len(lines) > 1:
        lines += [""]

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped:
            leading_space = len(line) - len(stripped)
            indent = indent_level + leading_space
            wrapper = textwrap.TextWrapper(
                width=width - indent,
                initial_indent=indent * " ",
                subsequent_indent=indent * " ",
                break_long_words=False,
                break_on_hyphens=False,
                drop_whitespace=True,
            )
            list_wrapper = textwrap.TextWrapper(
                width=width - indent,
                initial_indent=indent * " " + "* ",
                subsequent_indent=indent * " " + "  ",
                break_long_words=False,
                break_on_hyphens=False,
                drop_whitespace=True,
            )
            for line in stripped.split("\n"):
                line_stripped = line.lstrip()
                line_stripped = fix_docstring_issues(line_stripped)
                if line_stripped == "":
                    final_lines.append("")
                elif line_stripped.startswith("* "):
                    final_lines.extend(list_wrapper.wrap(line_stripped[2:]))
                # Matches lines where an attribute is mentioned followed by the accepted
                # types (lines starting with a character sequence that
                # does not contain white spaces or '*' followed by ' : ').
                # It therefore matches 'condition : anyOf(...' but not '**Notes** : ...'
                # These lines should not be wrapped at all but appear on one line
                elif re.match(r"[^\s*]+ : ", line_stripped):
                    final_lines.append(indent * " " + line_stripped)
                else:
                    final_lines.extend(wrapper.wrap(line_stripped))

        # If this is the last line, put in an indent
        elif i + 1 == len(lines):
            final_lines.append(indent_level * " ")
        # If it's not the last line, this is a blank line that should not indent.
        else:
            final_lines.append("")
    # Remove any trailing whitespaces on the right side
    stripped_lines = []
    for i, line in enumerate(final_lines):
        if i + 1 == len(final_lines):
            stripped_lines.append(line)
        else:
            stripped_lines.append(line.rstrip())
    # Join it all together
    wrapped = "\n".join(stripped_lines)
    if lstrip:
        wrapped = wrapped.lstrip()
    return wrapped


def fix_docstring_issues(docstring: str) -> str:
    """
    All lists should start with `"* "`.

    1. Fixes the ones which either do not have `" "` and/or start with `"-"` replacing `"-"` ->  `"*"` and then adding `" "` where necessary.
    2. Now add a `" "` where a `"*"` is followed by one of the characters in the square brackets of the regex pattern.

    Parameters
    ----------
    docstring
        A processed docstring line.
    """
    return _RE_LIST_MISSING_WHITESPACE.sub(
        "* ", _RE_LIST_MISSING_ASTERISK.sub("*", docstring)
    )


rst_parse: RSTParseVegaLite = RSTParseVegaLite()


# TODO: Investigate `mistune.Markdown.(before|after)_render_hooks`.
def process_description(description: str) -> str:
    """Parse a JSON encoded markdown description into an `RST` string."""
    return rst_parse(description)
