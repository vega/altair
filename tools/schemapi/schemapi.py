from __future__ import annotations

import contextlib
import inspect
import json
import operator
import sys
import textwrap
from collections import defaultdict, deque
from functools import lru_cache, partial
from importlib.metadata import version as importlib_version
from itertools import chain, groupby, islice, zip_longest
from math import ceil
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Final,
    Generic,
    Iterable,
    List,
    Literal,
    Mapping,
    Sequence,
    TypeVar,
    Union,
    cast,
    overload,
)

import jsonschema
import jsonschema.validators
import narwhals.stable.v1 as nw
from jsonschema import ValidationError
from packaging.version import Version

if sys.version_info >= (3, 12):
    from typing import Protocol, TypeAliasType, runtime_checkable
else:
    from typing_extensions import Protocol, TypeAliasType, runtime_checkable

if TYPE_CHECKING:
    from types import ModuleType
    from typing import Callable, ClassVar, Final, Iterator, KeysView

    from jsonschema.protocols import Validator, _JsonParameter

    from altair.typing import ChartType
    from altair.vegalite.v5.schema._typing import Map

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs

    if sys.version_info >= (3, 11):
        from typing import LiteralString, Never, Self
    else:
        from typing_extensions import LiteralString, Never, Self
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    _OptionalModule: TypeAlias = "ModuleType | None"
    _Errs: TypeAlias = Iterable[ValidationError]
    _ErrsLazy: TypeAlias = Iterator[ValidationError]
    _ErrsLazyGroup: TypeAlias = Iterator[_ErrsLazy]
    _IntoLazyGroup: TypeAlias = Iterator["tuple[str, ValidationError]"]
    _ValidatorKeyword: TypeAlias = Literal[
        "additionalProperties",
        "enum",
        "type",
        "required",
        "properties",
        "anyOf",
        "allOf",
        "oneOf",
        "ref",
        "const",
    ]
    """Non-exhaustive listing of possible literals in ``ValidationError.validator``"""

__all__ = [
    "Optional",  # altair.utils
    "SchemaBase",  # altair.vegalite.v5.schema.core
    "Undefined",  # altair.utils
    "UndefinedType",  # altair.vegalite.v5.schema.core -> (side-effect relied on to propagate to alt.__init__)
    "_is_valid",  # altair.vegalite.v5.api
    "_resolve_references",  # tools.schemapi.utils -> tools.generate_schema_wrapper
    "_subclasses",  # altair.vegalite.v5.schema.core
    "is_undefined",  # altair.typing
    "validate_jsonschema",  # altair.utils.display
    "with_property_setters",  # altair.vegalite.v5.schema.channels
]

_VEGA_LITE_ROOT_URI: Final = "urn:vega-lite-schema"
"""
Prefix added to each ``"$ref"``.

This URI is arbitrary and could be anything else.

It just cannot be an empty string as we need to reference the schema registered in
the ``referencing.Registry``.
"""

_DEFAULT_DIALECT_URI: LiteralString = "http://json-schema.org/draft-07/schema#"
"""
Ideally, this would be parsed from the current Vega-Lite schema, and not hardcoded here.

However, due to circular imports between this module and ``alt.vegalite``,
this information is not yet available as the latter is only *partially* loaded.

The `draft version`_ which is used is unlikely to change often so it's ok to keep this.

.. _draft version:
   https://json-schema.org/understanding-json-schema/reference/schema#declaring-a-dialect
"""
# RELATED: tests/utils/test/schemapi.py/test_actual_json_schema_draft_is_same_as_hardcoded_default

DEBUG_MODE: bool = True
"""
If ``DEBUG_MODE``, then ``SchemaBase`` are converted to ``dict`` and validated at creation time.

This slows things down, particularly for larger specs, but leads to much more
useful tracebacks for the user.

Individual schema classes can override with:

    class Derived(SchemaBase):
        _class_is_valid_at_instantiation: ClassVar[bool] = False
"""


def enable_debug_mode() -> None:
    global DEBUG_MODE
    DEBUG_MODE = True


def disable_debug_mode() -> None:
    global DEBUG_MODE
    DEBUG_MODE = False


@contextlib.contextmanager
def debug_mode(arg: bool) -> Iterator[None]:
    global DEBUG_MODE
    original = DEBUG_MODE
    DEBUG_MODE = arg
    try:
        yield
    finally:
        DEBUG_MODE = original


def validate_jsonschema(
    spec: _JsonParameter, schema: Map, rootschema: Map | None = None
) -> None:
    """
    Validates ``spec`` against ``schema`` in the context of ``rootschema``.

    Any ``ValidationError``(s) are deduplicated and prioritized, with
    the remaining errors deemed relevant to the user.

    Notes
    -----
    - The first error is monkeypatched with a grouped iterator of all remaining errors
    - ``SchemaValidationError`` utilizes the patched attribute, to craft a more helpful error message.
        - However this breaks typing

    ``schema`` and ``rootschema`` are not validated but instead considered as valid.

    We don't use ``jsonschema.validate`` as this would validate the ``schema`` itself.
    Instead, we pass the ``schema`` directly to the validator class.

    This is done for two reasons:

    1. The schema comes from Vega-Lite and is not based on the user
    input, therefore there is no need to validate it in the first place.
    2. The "uri-reference" format checker fails for some of the
    references as URIs in "$ref" are not encoded, e.g.:

        '#/definitions/ValueDefWithCondition<MarkPropFieldOrDatumDef, (Gradient|string|null)>'

    would be a valid $ref in a Vega-Lite schema but it is not a valid
    URI reference due to the characters such as '<'.
    """
    it_errors = _validator(schema, rootschema).iter_errors(spec)
    if first_error := next(it_errors, None):
        groups = _group_tree_leaves(_rechain(first_error, it_errors))
        most_specific = _prune_subset_paths(groups)
        deduplicated = _deduplicate_errors(most_specific)
        dummy_error: Any
        if dummy_error := next(deduplicated, None):
            dummy_error._errors = _regroup(_rechain(dummy_error, deduplicated))  # type: ignore[attr-defined]
            raise dummy_error
        else:
            msg = (
                f"Expected to find at least one error, but first error was `None`.\n\n"
                f"spec: {spec!r}"
            )
            raise NotImplementedError(msg)


def _get_schema_dialect_uri(schema: Map, /) -> str:
    """
    Return value of `$schema`_.

    Defines which JSON Schema draft ``schema`` was written for.

    .. _$schema:
       https://json-schema.org/understanding-json-schema/reference/schema#schema

    """
    return schema.get("$schema", _DEFAULT_DIALECT_URI)


def _prepare_references(schema: Map, /) -> dict[str, Any]:
    """
    Return a deep copy of ``schema`` w/ replaced uri(s).

    All encountered ``dict | list``(s) will be reconstructed
    w/ ``_VEGA_LITE_ROOT_URI`` in front of all nested``$ref`` values.

    Notes
    -----
    ``copy.deepcopy`` is not needed as the iterator yields new objects.
    """
    # FIXME: The hottest function + it is recursive
    # Should be done once per schema
    return dict(_recurse_refs(schema))


def _recurse_refs(m: Map, /) -> Iterator[tuple[str, Any]]:
    """
    Recurse through a schema, yielding fresh copies of mutable containers.

    Adds ``_VEGA_LITE_ROOT_URI`` in front of all nested``$ref`` values.
    """
    for k, v in m.items():
        if k == "$ref":
            yield k, f"{_VEGA_LITE_ROOT_URI}{v}"
        elif isinstance(v, dict):
            yield k, dict(_recurse_refs(v))
        elif isinstance(v, list):
            yield k, [dict(_recurse_refs(el)) if _is_dict(el) else el for el in v]
        else:
            yield k, v


@lru_cache(maxsize=None)
def _validator_for(uri: str, /) -> Callable[..., Validator]:
    """
    Retrieve the constructor for a `Validator`_ class appropriate for validating the given schema.

    Parameters
    ----------
    uri
        Address pointing to the `$schema`_.

    .. _Validator:
       https://python-jsonschema.readthedocs.io/en/stable/validate/#the-validator-protocol
    .. _$schema:
       https://json-schema.org/understanding-json-schema/reference/schema
    """
    tp: Callable[..., Validator] = jsonschema.validators.validator_for({"$schema": uri})
    if hasattr(tp, "FORMAT_CHECKER"):
        return partial(tp, format_checker=tp.FORMAT_CHECKER)
    else:
        return tp


_HASH_ENCODER = json.JSONEncoder(sort_keys=True, separators=(",", ":"))

if Version(importlib_version("jsonschema")) >= Version("4.18"):
    from referencing import Registry
    from referencing.jsonschema import specification_with as _specification_with

    if TYPE_CHECKING:
        from referencing import Specification
        from referencing._core import Resolver

    @lru_cache(maxsize=None)
    def specification_with(dialect_id: str, /) -> Specification[Any]:
        """
        Retrieve the `Specification`_ with the given dialect identifier.

        Wraps `specification_with`_, which returns one **immutable** object per
        JSON Schema **dialect**.

        Raises
        ------
        ``UnknownDialect``
            if the given ``dialect_id`` isn't known

        .. _Specification:
           https://referencing.readthedocs.io/en/stable/api/#referencing.Specification
        .. _specification_with:
           https://referencing.readthedocs.io/en/stable/api/#referencing.jsonschema.specification_with
        """
        return _specification_with(dialect_id)

    class _Registry:
        """
        A cache of `Registry`_ (s).

        An instance named ``registry`` is used to wrap the `Registry`_ API,
        with a managed cache.

        See Also
        --------
        ``_Registry.__call__``

        .. _Registry:
               https://referencing.readthedocs.io/en/stable/api/#referencing.Registry
        """

        _cached: ClassVar[dict[tuple[str, str], Registry[Any]]] = {}

        @staticmethod
        def compute_key(root: Map, dialect_id: str, /) -> tuple[str, str]:
            """
            Generate a simple-minded hash to identify a registry.

            Notes
            -----
            Why the strange hash?
            - **All** generated schemas hit the ``"$ref"`` branch.
            - ``api.Then`` hits the len(...) 1 branch w/ ``{"type": "object"}``.
            - Final branch is only hit by mock schemas in:
                - `tests/utils/test_core.py::test_infer_encoding_types`
                - `tests/utils/test_schemapi.py`
            """
            if "$ref" in root:
                k1 = root["$ref"]
            elif len(root) == 1:
                k1 = "".join(f"{s!s}" for s in chain(*root.items()))
            else:
                k1 = _HASH_ENCODER.encode(root)
            return k1, dialect_id

        @classmethod
        def update_cached(
            cls, root: Map, dialect_id: str, resolver: Resolver[Any]
        ) -> None:
            cls._cached[cls.compute_key(root, dialect_id)] = resolver._registry

        def __call__(self, root: Map, dialect_id: str, /) -> Registry[Any]:
            """
            Constructs a `Registry`_, adding the `Resource`_ produced by ``rootschema``.

            Requires at least ``jsonschema`` `v4.18.0a1`_.

            .. _Registry:
               https://referencing.readthedocs.io/en/stable/api/#referencing.Registry
            .. _Resource:
               https://referencing.readthedocs.io/en/stable/api/#referencing.Resource
            .. _v4.18.0a1:
               https://github.com/python-jsonschema/jsonschema/releases/tag/v4.18.0a1
            """
            cache_key = self.compute_key(root, dialect_id)
            if (reg := self._cached.get(cache_key, None)) is not None:
                return reg
            resource = specification_with(dialect_id).create_resource(root)
            reg = Registry().with_resource(_VEGA_LITE_ROOT_URI, resource).crawl()
            type(self)._cached[cache_key] = reg
            return reg

    registry: _Registry = _Registry()

    def _validator(schema: Map, rootschema: Map | None = None, /) -> Validator:
        """
        Constructs a `Validator`_ for future validation.

        Parameters
        ----------
        schema
            Schema that a spec will be validated against.
        rootschema
            Context to evaluate within.

        We have **both** a current & a backwards-compatible version of this function.

        .. _Validator:
           https://python-jsonschema.readthedocs.io/en/stable/validate/#the-validator-protocol
        """
        # NOTE: This is the current version
        uri = _get_schema_dialect_uri(rootschema or schema)
        validator = _validator_for(uri)
        return validator(
            _prepare_references(schema), registry=registry(rootschema or schema, uri)
        )

    def _resolve_references(schema: Map, rootschema: Map) -> Map:
        """
        Resolve schema references until there is no ``"$ref"`` anymore in the top-level ``dict``.

        ``jsonschema`` deprecated ``RefResolver`` in favor of `referencing`_.

        We have **both** a current & a backwards-compatible version of this function.

        .. _referencing:
           https://github.com/python-jsonschema/jsonschema/releases/tag/v4.18.0a1
        """
        # NOTE: This is the current version
        root = rootschema or schema
        if ("$ref" not in root) or ("$ref" not in schema):
            return schema
        uri = _get_schema_dialect_uri(rootschema)
        resolver = registry(root, uri).resolver(_VEGA_LITE_ROOT_URI)
        while "$ref" in schema:
            resolved = resolver.lookup(schema["$ref"])
            schema = resolved.contents
        registry.update_cached(root, uri, resolved.resolver)
        return schema


else:

    def _validator(schema: Map, rootschema: Map | None = None, /) -> Validator:
        """
        Constructs a `Validator`_ for future validation.

        We have **both** a current & a backwards-compatible version of this function.

        Parameters
        ----------
        schema
            Schema that a spec will be validated against.
        rootschema
            Context to evaluate within.

        .. _Validator:
           https://python-jsonschema.readthedocs.io/en/stable/validate/#the-validator-protocol
        """
        # NOTE: This is the backwards-compatible version
        validator = _validator_for(_get_schema_dialect_uri(rootschema or schema))
        resolver: Any = (
            jsonschema.RefResolver.from_schema(rootschema) if rootschema else rootschema
        )
        return validator(schema, resolver=resolver)

    def _resolve_references(schema: Map, rootschema: Map) -> Map:
        """
        Resolve schema references until there is no ``"$ref"`` anymore in the top-level ``dict``.

        ``jsonschema`` deprecated ``RefResolver`` in favor of `referencing`_.

        We have **both** a current & a backwards-compatible version of this function.

        .. _referencing:
           https://github.com/python-jsonschema/jsonschema/releases/tag/v4.18.0a1
        """
        # NOTE: This is the backwards-compatible version
        resolver = jsonschema.RefResolver.from_schema(rootschema or schema)
        while "$ref" in schema:
            with resolver.resolving(schema["$ref"]) as resolved:
                schema = resolved
        return schema


if Version(importlib_version("jsonschema")) >= Version("4.0.1"):
    _json_path: Callable[[ValidationError], str] = operator.attrgetter("json_path")
else:

    def _json_path(err: ValidationError, /) -> str:
        """
        Vendored backport for ``jsonschema.ValidationError.json_path`` property.

        See https://github.com/vega/altair/issues/3038.
        """
        path = "$"
        for elem in err.absolute_path:
            if isinstance(elem, int):
                path += "[" + str(elem) + "]"
            else:
                path += "." + elem
        return path


_FN_PATH = cast("Callable[[tuple[str, ValidationError]], str]", operator.itemgetter(0))
"""Key function for ``(json_path, ValidationError)``."""
_FN_VALIDATOR = cast("Callable[[ValidationError], _ValidatorKeyword]", operator.attrgetter("validator"))  # fmt: off
"""Key function for ``ValidationError.validator``."""


def _message_len(err: ValidationError, /) -> int:
    """Return length of a ``ValidationError`` message."""
    return len(err.message)


def _rechain(element: T, others: Iterable[T], /) -> Iterator[T]:
    """
    Continue an iterator at the last popped ``element``.

    Equivalent to::

        elements = 1, 2, 3, 4, 5
        it = iter(elements)
        element = next(it)
        it_continue = chain([element], it)

    """
    yield element
    yield from others


def _regroup(
    errors: _Errs, /, *, key: Callable[[ValidationError], str] = _json_path
) -> _ErrsLazyGroup:
    """
    Regroup error stream by a ``key`` function.

    Assumes ``errors`` are already sorted, which holds **only** at the end of ``validate_jsonschema``.
    """
    for _, grouped_it in groupby(errors, key):
        yield grouped_it


def _group_tree_leaves(errors: _Errs, /) -> _IntoLazyGroup:
    """
    Combines 3 previously distinct steps:

    1. ``_get_leaves_of_error_tree``

    These are errors which have no further errors that caused it and so they are the most specific errors
    with the most specific error messages.

    2. ``_group_errors_by_json_path`` (part of)

    Extracts the ``.json_path`` property for grouping.

    3. Removes::

        ValidationError: "'value' is a required property"

    as these errors are unlikely to be the relevant ones for the user.
    They come from validation against a schema definition where the output of `alt.value`
    would be valid.
    However, if a user uses `alt.value`, the `value` keyword is included automatically
    from that function and so it's unlikely that this was what the user intended
    if the keyword is not present in the first place.
    """  # noqa: D400
    REQUIRED = "required"
    VALUE = ["value"]
    for err in errors:
        if err_context := err.context:
            yield from _group_tree_leaves(err_context)
        elif err.validator == REQUIRED and err.validator_value == VALUE:
            continue
        else:
            yield _json_path(err), err


def _prune_subset_paths(json_path_errors: _IntoLazyGroup, /) -> Iterator[_Errs]:
    """
    Removes key (json path), value (errors) pairs where the json path is fully contained in another json path.

    For example if `errors_by_json_path` has two keys, `$.encoding.X` and `$.encoding.X.tooltip`,
    then the first one will be removed and only the second one is returned.

    This is done under the assumption that more specific json paths give more helpful error messages to the user.

    Currently using a `list`, but typing it more restrictive to see if it can be avoided.

    - Needs to be sorted to work with groupby
    - Reversing allows prioritising more specific groups, since they are seen first
    - Then re-reversed, to keep seen order
    """
    rev_sort = sorted(json_path_errors, key=_FN_PATH, reverse=True)
    keeping: dict[str, _Errs] = {}
    for unique_path, grouped_errors in groupby(rev_sort, key=_FN_PATH):
        if any(seen.startswith(unique_path) for seen in keeping):
            continue
        else:
            keeping[unique_path] = [err for _, err in grouped_errors]
    yield from islice(reversed(keeping.values()), 3)


def _groupby_validator(
    errors: _Errs, /
) -> Iterator[tuple[_ValidatorKeyword, _ErrsLazy]]:
    """
    Groups the errors by the json schema "validator" that casued the error.

    For example if the error is that a value is not one of an enumeration in the json schema
    then the "validator" is `"enum"`, if the error is due to an unknown property that
    was set although no additional properties are allowed then "validator" is
    `"additionalProperties`, etc.
    """
    yield from groupby(sorted(errors, key=_FN_VALIDATOR), key=_FN_VALIDATOR)


def _deduplicate_errors(grouped_errors: Iterator[_Errs], /) -> _ErrsLazy:
    """
    Some errors have very similar error messages or are just in general not helpful for a user.

    This function removes as many of these cases as possible and
    can be extended over time to handle new cases that come up.
    """
    for by_path in grouped_errors:
        for validator, errors in _groupby_validator(by_path):
            if fn := _FN_MAP_DEDUPLICATION.get(validator):
                errors = fn(errors)
            yield from _distinct_messages(errors)


def _distinct_messages(iterable: _Errs, /) -> _ErrsLazy:
    seen = set()
    for el in iterable:
        if el.message not in seen:
            seen.add(el.message)
            yield el


def _shortest_any_of(iterable: _Errs, /) -> _ErrsLazy:
    """
    If there are multiple additional property errors it usually means that the offending element was validated against multiple schemas and its parent is a common anyOf validator.

    The error messages produced from these cases are usually
    very similar and we just take the shortest one.
    For example the following 3 errors are raised for::

        alt.X("variety", unknown=2)
        - "Additional properties are not allowed ('unknown' was unexpected)"
        - "Additional properties are not allowed ('field', 'unknown' were unexpected)"
        - "Additional properties are not allowed ('field', 'type', 'unknown' were unexpected)".
    """
    it = iter(iterable)
    first = next(it)
    if (
        parent := cast("ValidationError", first.parent)
    ) and parent.validator == "anyOf":
        yield min(_rechain(first, it), key=_message_len)
    else:
        yield first


def _prune_subset_enum(iterable: _Errs, /) -> _ErrsLazy:
    """Skip any``"enum"`` errors that are a subset of another error."""
    enums: tuple[set[str], ...]
    errors: tuple[ValidationError, ...]
    enums, errors = zip(*((set(err.validator_value), err) for err in iterable))  # type: ignore[arg-type]
    for cur_enum, err in zip(enums, errors):
        if not any(cur_enum < e for e in enums if e != cur_enum):
            yield err


_FN_MAP_DEDUPLICATION: Mapping[_ValidatorKeyword, Callable[[_Errs], _ErrsLazy]] = {
    "additionalProperties": _shortest_any_of,
    "enum": _prune_subset_enum,
}


def _from_array_like(obj: Iterable[Any], /) -> list[Any]:
    try:
        ser = nw.from_native(obj, strict=True, series_only=True)
        return ser.to_list()
    except TypeError:
        return list(obj)


def _todict(obj: Any, context: dict[str, Any] | None, np_opt: Any, pd_opt: Any) -> Any:  # noqa: C901
    """Convert an object to a dict representation."""
    if np_opt is not None:
        np = np_opt
        if isinstance(obj, np.ndarray):
            return [_todict(v, context, np_opt, pd_opt) for v in obj]
        elif isinstance(obj, np.number):
            return float(obj)
        elif isinstance(obj, np.datetime64):
            result = str(obj)
            if "T" not in result:
                # See https://github.com/vega/altair/issues/1027 for why this is necessary.
                result += "T00:00:00"
            return result
    if isinstance(obj, SchemaBase):
        return obj.to_dict(validate=False, context=context)
    elif isinstance(obj, (list, tuple)):
        return [_todict(v, context, np_opt, pd_opt) for v in obj]
    elif isinstance(obj, dict):
        return {
            k: _todict(v, context, np_opt, pd_opt)
            for k, v in obj.items()
            if v is not Undefined
        }
    elif isinstance(obj, SchemaLike):
        return obj.to_dict()
    elif pd_opt is not None and isinstance(obj, pd_opt.Timestamp):
        return pd_opt.Timestamp(obj).isoformat()
    elif _is_iterable(obj, exclude=(str, bytes)):
        return _todict(_from_array_like(obj), context, np_opt, pd_opt)
    else:
        return obj


class SchemaValidationError(jsonschema.ValidationError):
    def __init__(self, obj: SchemaBase, err: ValidationError) -> None:
        """
        A wrapper for ``jsonschema.ValidationError`` with friendlier traceback.

        Parameters
        ----------
        obj
            The instance that failed ``self.validate(...)``.
        err
            The original ``ValidationError``.

        Notes
        -----
        We do not raise `from err` as else the resulting traceback is very long
        as it contains part of the Vega-Lite schema.

        It would also first show the less helpful `ValidationError` instead of
        the more user friendly `SchemaValidationError`.
        """
        super().__init__(**err._contents())
        self.obj = obj
        err = cast("SchemaValidationError", err)
        self._errors: _ErrsLazyGroup = err._errors
        # This is the message from err
        self._original_message = self.message
        self.message = self._get_message()

    def __str__(self) -> str:
        return self.message

    @staticmethod
    def indent_from_second_line(msg: str, /, indent: int = 4) -> str:
        return "\n".join(
            " " * indent + s if idx > 0 and s else s
            for idx, s in enumerate(msg.split("\n"))
        )

    def _get_message(self) -> str:
        it: _ErrsLazyGroup = self._errors
        group_1 = list(next(it))
        if (group_2 := next(it, None)) is not None:
            messages: Iterator[str] = (
                self._get_message_for_errors_group(g)
                for g in (group_1, list(group_2), next(it, None))
                if g is not None
            )
            msg = "\n\n".join(
                self.indent_from_second_line(f"Error {error_id}: {m}")
                for error_id, m in enumerate(messages, start=1)
            )
            return f"Multiple errors were found.\n\n{msg}"
        else:
            return self._get_message_for_errors_group(group_1)

    def _get_message_for_errors_group(self, errors: _Errs) -> str:
        """
        Note.

        During development, we only found cases where an additionalProperties
        error was raised if that was the only error for the offending instance
        as identifiable by the json path.

        Therefore, we just check here the first error.
        However, other constellations might exist in which case this should be adapted
        so that other error messages are shown as well.
        """
        if not isinstance(errors, Sequence):
            errors = list(errors)
        if errors[0].validator == "additionalProperties":
            return self._get_additional_properties_error_message(errors[0])
        else:
            return self._get_default_error_message(errors=errors)

    def _get_additional_properties_error_message(
        self,
        error: ValidationError,
    ) -> str:
        """Output all existing parameters when an unknown parameter is specified."""
        altair_cls = self._get_altair_class_for_error(error)
        param_dict_keys = inspect.signature(altair_cls).parameters.keys()
        param_names_table = self._format_params_as_table(param_dict_keys)

        # Error messages for these errors look like this:
        # "Additional properties are not allowed ('unknown' was unexpected)"
        # Line below extracts "unknown" from this string
        parameter_name = error.message.split("('")[-1].split("'")[0]
        cls_name = altair_cls.__name__
        return (
            f"`{cls_name}` has no parameter named '{parameter_name}'\n\n"
            f"Existing parameter names are:\n{param_names_table}\n"
            f"See the help for `{cls_name}` to read the full description of these parameters"
        )

    def _get_altair_class_for_error(self, error: ValidationError) -> type[SchemaBase]:
        """
        Try to get the lowest class possible in the chart hierarchy so it can be displayed in the error message.

        This should lead to more informative error messages pointing the user closer to the source of the issue.
        """
        from altair import vegalite

        for prop_name in reversed(error.absolute_path):
            # Check if str as e.g. first item can be a 0
            if isinstance(prop_name, str):
                potential_class_name = prop_name[0].upper() + prop_name[1:]
                cls = getattr(vegalite, potential_class_name, None)
                if cls is not None:
                    break
        else:
            # Did not find a suitable class based on traversing the path so we fall
            # back on the class of the top-level object which created
            # the SchemaValidationError
            cls = type(self.obj)
        return cls

    @staticmethod
    def _format_params_as_table(param_view: KeysView[str]) -> str:
        """Format param names into a table so that they are easier to read."""
        param_names: list[str] = [nm for nm in param_view if nm not in {"kwds", "self"}]

        # Worst case scenario with the same longest param name in the same
        # row for all columns
        max_name_length = len(max(param_view, key=len))
        max_column_width = 80
        # Output a square table if not too big (since it is easier to read)
        num_param_names = len(param_names)
        square_columns = int(ceil(num_param_names**0.5))
        columns = min(max_column_width // max_name_length, square_columns)

        # Compute roughly equal column heights to evenly divide the param names
        def split_into_equal_parts(n: int, p: int) -> list[int]:
            return [n // p + 1] * (n % p) + [n // p] * (p - n % p)

        column_heights = split_into_equal_parts(num_param_names, columns)

        # Section the param names into columns and compute their widths
        param_names_columns: list[Sequence[str]] = []
        column_max_widths: list[int] = []
        last_end_idx: int = 0
        for ch in column_heights:
            param_names_columns.append(param_names[last_end_idx : last_end_idx + ch])
            column_max_widths.append(
                max(len(param_name) for param_name in param_names_columns[-1])
            )
            last_end_idx = ch + last_end_idx

        # Transpose the param name columns into rows to facilitate looping
        # Build the table as a string by iterating over and formatting the rows
        param_names_table: str = ""
        column_pad = 3
        for param_names_row in zip_longest(*param_names_columns, fillvalue=""):
            last_element = len(param_names_row) - 1
            for num, param_name in enumerate(param_names_row):
                # Set column width based on the longest param in the column
                width = column_pad + column_max_widths[num]
                param_names_table += "{:<{}}".format(param_name, width)
                # Insert newlines and spacing after the last element in each row
                if num == last_element:
                    param_names_table += "\n"
        return param_names_table

    def _get_default_error_message(
        self,
        errors: Sequence[ValidationError],
    ) -> str:
        bullet_points: list[str] = []
        errors_by_validator: defaultdict[str, list[ValidationError]] = defaultdict(list)
        for err in errors:
            errors_by_validator[err.validator].append(err)  # type: ignore[index]

        if "enum" in errors_by_validator:
            for error in errors_by_validator["enum"]:
                bullet_points.append(f"one of {error.validator_value}")  # noqa: PERF401

        if "type" in errors_by_validator:
            types = [f"'{err.validator_value}'" for err in errors_by_validator["type"]]
            point = "of type "
            if len(types) == 1:
                point += types[0]
            elif len(types) == 2:
                point += f"{types[0]} or {types[1]}"
            else:
                point += ", ".join(types[:-1]) + f", or {types[-1]}"
            bullet_points.append(point)

        # It should not matter which error is specifically used as they are all
        # about the same offending instance (i.e. invalid value), so we can just
        # take the first one
        error = errors[0]
        # Add a summary line when parameters are passed an invalid value
        # For example: "'asdf' is an invalid value for `stack`
        message = f"'{error.instance}' is an invalid value"
        if error.absolute_path:
            message += f" for `{error.absolute_path[-1]}`"

        # Add bullet points
        if len(bullet_points) == 0:
            message += ".\n\n"
        elif len(bullet_points) == 1:
            message += f". Valid values are {bullet_points[0]}.\n\n"
        else:
            # We don't use .capitalize below to make the first letter uppercase
            # as that makes the rest of the message lowercase
            bullet_points = [point[0].upper() + point[1:] for point in bullet_points]
            message += ". Valid values are:\n\n"
            message += "\n".join([f"- {point}" for point in bullet_points])
            message += "\n\n"

        # Add unformatted messages of any remaining errors which were not
        # considered so far. This is not expected to be used but more exists
        # as a fallback for cases which were not known during development.
        it = (
            "\n".join(e.message for e in errors)
            for validator, errors in errors_by_validator.items()
            if validator not in {"enum", "type"}
        )
        message += "".join(it)
        return message.strip()


_JSON_VT_co = TypeVar(
    "_JSON_VT_co",
    Literal["string"],
    Literal["object"],
    Literal["array"],
    covariant=True,
)
"""
One of a subset of JSON Schema `primitive types`_:

    ["string", "object", "array"]

.. _primitive types:
    https://json-schema.org/draft-07/json-schema-validation#rfc.section.6.1.1
"""

_TypeMap = TypeAliasType(
    "_TypeMap", Mapping[Literal["type"], _JSON_VT_co], type_params=(_JSON_VT_co,)
)
"""
A single item JSON Schema using the `type`_ keyword.

This may represent **one of**:

    {"type": "string"}
    {"type": "object"}
    {"type": "array"}

.. _type:
    https://json-schema.org/understanding-json-schema/reference/type
"""

# NOTE: Type checkers want opposing things:
# - `mypy`   : Covariant type variable "_JSON_VT_co" used in protocol where invariant one is expected  [misc]
# - `pyright`: Type variable "_JSON_VT_co" used in generic protocol "SchemaLike" should be covariant [reportInvalidTypeVarUse]
# Siding with `pyright` as this is consistent with https://github.com/python/typeshed/blob/9e506eb5e8fc2823db8c60ad561b1145ff114947/stdlib/typing.pyi#L690


@runtime_checkable
class SchemaLike(Generic[_JSON_VT_co], Protocol):  # type: ignore[misc]
    """
    Represents ``altair`` classes which *may* not derive ``SchemaBase``.

    Attributes
    ----------
    _schema
        A single item JSON Schema using the `type`_ keyword.

    Notes
    -----
    Should be kept tightly defined to the **minimum** requirements for:
        - Converting into a form that can be validated by `jsonschema`_.
        - Avoiding calling ``.to_dict()`` on a class external to ``altair``.
    - ``_schema`` is more accurately described as a ``ClassVar``
        - See `discussion`_ for blocking issue.

    .. _jsonschema:
        https://github.com/python-jsonschema/jsonschema
    .. _type:
        https://json-schema.org/understanding-json-schema/reference/type
    .. _discussion:
        https://github.com/python/typing/discussions/1424
    """

    _schema: _TypeMap[_JSON_VT_co]

    def to_dict(self, *args, **kwds) -> Any: ...


@runtime_checkable
class ConditionLike(SchemaLike[Literal["object"]], Protocol):
    """
    Represents the wrapped state of a conditional encoding or property.

    Attributes
    ----------
    condition
        One or more (predicate, statement) pairs which each form a condition.

    Notes
    -----
    - Can be extended with additional conditions.
    - *Does not* define a default value, but can be finalized with one.
    """

    condition: Any
    _schema: _TypeMap[Literal["object"]] = {"type": "object"}


class UndefinedType:
    """A singleton object for marking undefined parameters."""

    __instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __repr__(self) -> str:
        return "Undefined"


Undefined = UndefinedType()
T = TypeVar("T")
Optional: TypeAlias = Union[T, UndefinedType]
"""One of ``T`` specified type(s), or the ``Undefined`` singleton.

Examples
--------
The parameters ``short``, ``long`` accept the same range of types::

    # ruff: noqa: UP006, UP007
    from altair.typing import Optional

    def func_1(
        short: Optional[str | bool | float | dict[str, Any] | SchemaBase] = Undefined,
        long: Union[
            str, bool, float, Dict[str, Any], SchemaBase, UndefinedType
        ] = Undefined,
    ): ...

This is distinct from `typing.Optional <https://typing.readthedocs.io/en/latest/spec/historical.html#union-and-optional>`__.

``altair.typing.Optional`` treats ``None`` like any other type::

    # ruff: noqa: UP006, UP007
    from altair.typing import Optional

    def func_2(
        short: Optional[str | float | dict[str, Any] | None | SchemaBase] = Undefined,
        long: Union[
            str, float, Dict[str, Any], None, SchemaBase, UndefinedType
        ] = Undefined,
    ): ...
"""


def is_undefined(obj: Any) -> TypeIs[UndefinedType]:
    """
    Type-safe singleton check for `UndefinedType`.

    Notes
    -----
    - Using `obj is Undefined` does not narrow from `UndefinedType` in a union.
        - Due to the assumption that other `UndefinedType`'s could exist.
    - Current [typing spec advises](https://typing.readthedocs.io/en/latest/spec/concepts.html#support-for-singleton-types-in-unions) using an `Enum`.
        - Otherwise, requires an explicit guard to inform the type checker.
    """
    return obj is Undefined


@overload
def _shallow_copy(obj: _CopyImpl) -> _CopyImpl: ...
@overload
def _shallow_copy(obj: Any) -> Any: ...
def _shallow_copy(obj: _CopyImpl | Any) -> _CopyImpl | Any:
    if isinstance(obj, SchemaBase):
        return obj.copy(deep=False)
    elif isinstance(obj, (list, dict)):
        return obj.copy()
    else:
        return obj


@overload
def _deep_copy(obj: _CopyImpl, by_ref: set[str]) -> _CopyImpl: ...
@overload
def _deep_copy(obj: Any, by_ref: set[str]) -> Any: ...
def _deep_copy(obj: _CopyImpl | Any, by_ref: set[str]) -> _CopyImpl | Any:
    copy = partial(_deep_copy, by_ref=by_ref)
    if isinstance(obj, SchemaBase):
        if copier := getattr(obj, "__deepcopy__", None):
            with debug_mode(False):
                return copier(obj)
        args = (copy(arg) for arg in obj._args)
        kwds = {k: (copy(v) if k not in by_ref else v) for k, v in obj._kwds.items()}
        with debug_mode(False):
            return obj.__class__(*args, **kwds)
    elif isinstance(obj, list):
        return [copy(v) for v in obj]
    elif isinstance(obj, dict):
        return {k: (copy(v) if k not in by_ref else v) for k, v in obj.items()}
    else:
        return obj


class SchemaBase:
    """
    Base class for schema wrappers.

    Each derived class should set the _schema class attribute (and optionally
    the _rootschema class attribute) which is used for validation.
    """

    _schema: ClassVar[dict[str, Any] | Any] = None
    _rootschema: ClassVar[dict[str, Any] | Any] = None
    _class_is_valid_at_instantiation: ClassVar[bool] = True

    def __init__(self, *args: Any, **kwds: Any) -> None:
        # Two valid options for initialization, which should be handled by
        # derived classes:
        # - a single arg with no kwds, for, e.g. {'type': 'string'}
        # - zero args with zero or more kwds for {'type': 'object'}
        if self._schema is None:
            msg = (
                f"Cannot instantiate object of type {self.__class__}: "
                "_schema class attribute is not defined."
                ""
            )
            raise ValueError(msg)

        if kwds:
            assert len(args) == 0
        else:
            assert len(args) in {0, 1}

        # use object.__setattr__ because we override setattr below.
        object.__setattr__(self, "_args", args)
        object.__setattr__(self, "_kwds", kwds)

        if DEBUG_MODE and self._class_is_valid_at_instantiation:
            self.to_dict(validate=True)

    def copy(
        self, deep: bool | Iterable[Any] = True, ignore: list[str] | None = None
    ) -> Self:
        """
        Return a copy of the object.

        Parameters
        ----------
        deep : boolean or list, optional
            If True (default) then return a deep copy of all dict, list, and
            SchemaBase objects within the object structure.
            If False, then only copy the top object.
            If a list or iterable, then only copy the listed attributes.
        ignore : list, optional
            A list of keys for which the contents should not be copied, but
            only stored by reference.
        """
        if deep is True:
            return cast("Self", _deep_copy(self, set(ignore) if ignore else set()))
        with debug_mode(False):
            copy = self.__class__(*self._args, **self._kwds)
        if _is_iterable(deep):
            for attr in deep:
                copy[attr] = _shallow_copy(copy._get(attr))
        return copy

    def _get(self, attr, default=Undefined):
        """Get an attribute, returning default if not present."""
        attr = self._kwds.get(attr, Undefined)
        if attr is Undefined:
            attr = default
        return attr

    def __getattr__(self, attr):
        # reminder: getattr is called after the normal lookups
        if attr == "_kwds":
            raise AttributeError()
        elif attr in self._kwds:
            return self._kwds[attr]
        else:
            return getattr(super(), "__getattr__", super().__getattribute__)(attr)

    def __setattr__(self, item, val) -> None:
        self._kwds[item] = val

    def __getitem__(self, item):
        return self._kwds[item]

    def __setitem__(self, item, val) -> None:
        self._kwds[item] = val

    def __repr__(self) -> str:
        name = type(self).__name__
        if kwds := self._kwds:
            it = (f"{k}: {v!r}" for k, v in sorted(kwds.items()) if v is not Undefined)
            args = ",\n".join(it).replace("\n", "\n  ")
            LB, RB = "{", "}"
            return f"{name}({LB}\n  {args}\n{RB})"
        else:
            return f"{name}({self._args[0]!r})"

    def __eq__(self, other: Any) -> bool:
        return (
            type(self) is type(other)
            and self._args == other._args
            and self._kwds == other._kwds
        )

    def to_dict(
        self,
        validate: bool = True,
        *,
        ignore: list[str] | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Return a dictionary representation of the object.

        Parameters
        ----------
        validate : bool, optional
            If True (default), then validate the result against the schema.
        ignore : list[str], optional
            A list of keys to ignore.
        context : dict[str, Any], optional
            A context dictionary.

        Raises
        ------
        SchemaValidationError :
            If ``validate`` and the result does not conform to the schema.

        Notes
        -----
        - ``ignore``, ``context`` are usually not needed to be specified as a user.
        - *Technical*: ``ignore`` will **not** be passed to child :meth:`.to_dict()`.
        """
        context = context or {}
        ignore = ignore or []
        opts = _get_optional_modules(np_opt="numpy", pd_opt="pandas")

        if self._args and not self._kwds:
            kwds = self._args[0]
        elif not self._args:
            kwds = self._kwds.copy()
            exclude = {*ignore, "shorthand"}
            if parsed := context.pop("parsed_shorthand", None):
                kwds = _replace_parsed_shorthand(parsed, kwds)
            kwds = {k: v for k, v in kwds.items() if k not in exclude}
            if (mark := kwds.get("mark")) and isinstance(mark, str):
                kwds["mark"] = {"type": mark}
        else:
            msg = f"{type(self)} instance has both a value and properties : cannot serialize to dict"
            raise ValueError(msg)
        result = _todict(kwds, context=context, **opts)
        if validate:
            # NOTE: Don't raise `from err`, see `SchemaValidationError` doc
            try:
                self.validate(result)
            except ValidationError as err:
                raise SchemaValidationError(self, err) from None
        return result

    def to_json(
        self,
        validate: bool = True,
        indent: int | str | None = 2,
        sort_keys: bool = True,
        *,
        ignore: list[str] | None = None,
        context: dict[str, Any] | None = None,
        **kwargs,
    ) -> str:
        """
        Emit the JSON representation for this object as a string.

        Parameters
        ----------
        validate : bool, optional
            If True (default), then validate the result against the schema.
        indent : int, optional
            The number of spaces of indentation to use. The default is 2.
        sort_keys : bool, optional
            If True (default), sort keys in the output.
        ignore : list[str], optional
            A list of keys to ignore.
        context : dict[str, Any], optional
            A context dictionary.
        **kwargs
            Additional keyword arguments are passed to ``json.dumps()``

        Raises
        ------
        SchemaValidationError :
            If ``validate`` and the result does not conform to the schema.

        Notes
        -----
        - ``ignore``, ``context`` are usually not needed to be specified as a user.
        - *Technical*: ``ignore`` will **not** be passed to child :meth:`.to_dict()`.
        """
        if ignore is None:
            ignore = []
        if context is None:
            context = {}
        dct = self.to_dict(validate=validate, ignore=ignore, context=context)
        return json.dumps(dct, indent=indent, sort_keys=sort_keys, **kwargs)

    @classmethod
    def _default_wrapper_classes(cls) -> Iterator[type[SchemaBase]]:
        """Return the set of classes used within cls.from_dict()."""
        return _subclasses(SchemaBase)

    @classmethod
    def from_dict(
        cls: type[TSchemaBase], dct: dict[str, Any], validate: bool = True
    ) -> TSchemaBase:
        """
        Construct class from a dictionary representation.

        Parameters
        ----------
        dct : dictionary
            The dict from which to construct the class
        validate : boolean
            If True (default), then validate the input against the schema.

        Raises
        ------
        jsonschema.ValidationError :
            If ``validate`` and ``dct`` does not conform to the schema
        """
        if validate:
            cls.validate(dct)
        converter: type[_FromDict] | _FromDict = (
            _FromDict
            if _FromDict.hash_tps
            else _FromDict(cls._default_wrapper_classes())
        )
        return converter.from_dict(dct, cls)

    @classmethod
    def from_json(
        cls, json_string: str, validate: bool = True, **kwargs: Any
    ) -> ChartType:
        """
        Instantiate the object from a valid JSON string.

        Parameters
        ----------
        json_string : string
            The string containing a valid JSON chart specification.
        validate : boolean
            If True (default), then validate the input against the schema.
        **kwargs :
            Additional keyword arguments are passed to json.loads

        Returns
        -------
        chart : Chart object
            The altair Chart object built from the specification.
        """
        dct: dict[str, Any] = json.loads(json_string, **kwargs)
        return cls.from_dict(dct, validate=validate)  # type: ignore[return-value]

    @classmethod
    def validate(
        cls, instance: dict[str, Any], schema: dict[str, Any] | None = None
    ) -> None:
        """Validate the instance against the class schema in the context of the rootschema."""
        validate_jsonschema(
            instance, schema or cls._schema, cls._rootschema or cls._schema
        )

    @classmethod
    def resolve_references(cls, schema: dict[str, Any] | None = None) -> dict[str, Any]:
        """Resolve references in the context of this object's schema or root schema."""
        rootschema = cls._rootschema or cls._schema
        if rootschema is None:
            name = type(cls).__name__
            msg = (
                f"{name}.resolve_references() provided only `None` values for:\n"
                f"{schema=}, {cls._schema=}, {cls._rootschema=}.\n\n"
                f"This variant indicates the class definition {name!r} is invalid."
            )
            raise TypeError(msg)
        else:
            resolved = _resolve_references(schema or cls._schema, rootschema)
            return cast("dict[str, Any]", resolved)

    @classmethod
    def validate_property(
        cls, name: str, value: Any, schema: dict[str, Any] | None = None
    ) -> None:
        """Validate a property against property schema in the context of the rootschema."""
        opts = _get_optional_modules(np_opt="numpy", pd_opt="pandas")
        value = _todict(value, context={}, **opts)
        props = cls.resolve_references(schema or cls._schema).get("properties", {})
        validate_jsonschema(
            value, props.get(name, {}), rootschema=cls._rootschema or cls._schema
        )

    def __dir__(self) -> list[str]:
        return sorted(chain(super().__dir__(), self._kwds))


def _get_optional_modules(**modules: str) -> dict[str, _OptionalModule]:
    """
    Returns packages only if they have already been imported - otherwise they return `None`.

    This is useful for `isinstance` checks.

    For example, if `pandas` has not been imported, then an object is
    definitely not a `pandas.Timestamp`.

    Parameters
    ----------
    **modules
        Keyword-only binding from `{alias: module_name}`.

    Examples
    --------
    >>> import pandas as pd  # doctest: +SKIP
    >>> import polars as pl  # doctest: +SKIP
    >>> from altair.utils.schemapi import _get_optional_modules  # doctest: +SKIP
    >>>
    >>> _get_optional_modules(pd="pandas", pl="polars", ibis="ibis")  # doctest: +SKIP
    {
        "pd": <module 'pandas' from '...'>,
        "pl": <module 'polars' from '...'>,
        "ibis": None,
    }

    If the user later imports ``ibis``, it would appear in subsequent calls.

    >>> import ibis  # doctest: +SKIP
    >>>
    >>> _get_optional_modules(ibis="ibis")  # doctest: +SKIP
    {
        "ibis": <module 'ibis' from '...'>,
    }
    """
    return {k: sys.modules.get(v) for k, v in modules.items()}


def _replace_parsed_shorthand(
    parsed_shorthand: dict[str, Any], kwds: dict[str, Any]
) -> dict[str, Any]:
    """
    `parsed_shorthand` is added by `FieldChannelMixin`.

    It's used below to replace shorthand with its long form equivalent
    `parsed_shorthand` is removed from `context` if it exists so that it is
    not passed to child `to_dict` function calls.
    """
    # Prevent that pandas categorical data is automatically sorted
    # when a non-ordinal data type is specifed manually
    # or if the encoding channel does not support sorting
    if "sort" in parsed_shorthand and (
        "sort" not in kwds or kwds["type"] not in {"ordinal", Undefined}
    ):
        parsed_shorthand.pop("sort")

    kwds.update(
        (k, v)
        for k, v in parsed_shorthand.items()
        if kwds.get(k, Undefined) is Undefined
    )
    return kwds


TSchemaBase = TypeVar("TSchemaBase", bound=SchemaBase)

_CopyImpl = TypeVar("_CopyImpl", SchemaBase, Dict[Any, Any], List[Any])
"""
Types which have an implementation in ``SchemaBase.copy()``.

All other types are returned **by reference**.
"""


def _is_dict(obj: Any | dict[Any, Any]) -> TypeIs[dict[Any, Any]]:
    return isinstance(obj, dict)


def _is_list(obj: Any | list[Any]) -> TypeIs[list[Any]]:
    return isinstance(obj, list)


def _is_iterable(
    obj: Any, *, exclude: type | tuple[type, ...] = (str, bytes)
) -> TypeIs[Iterable[Any]]:
    return not isinstance(obj, exclude) and isinstance(obj, Iterable)


def _is_valid(spec: _JsonParameter, tp: type[SchemaBase], /) -> bool:
    """
    Return True if ``tp`` can be constructed from ``spec``.

    Notes
    -----
    Don't use this if you need to know *details* of the errors in ``spec``..
    """
    return next(_validator(tp._schema, tp._rootschema).iter_errors(spec), None) is None


def _passthrough(*args: Any, **kwds: Any) -> Any | dict[str, Any]:
    return args[0] if args else kwds


def _hash_schema(
    schema: _JsonParameter,
    /,
    *,
    exclude: Iterable[str] = frozenset(
        ("definitions", "title", "description", "$schema", "id")
    ),
) -> int:
    """
    Return the hash value for a ``schema``.

    Parameters
    ----------
    schema
        ``SchemaBase._schema``.
    exclude
        ``schema`` keys which are not considered when identifying equivalence.
    """
    if isinstance(schema, Mapping):
        schema = {k: v for k, v in schema.items() if k not in exclude}
    return hash(_HASH_ENCODER.encode(schema))


def _subclasses(cls: type[TSchemaBase]) -> Iterator[type[TSchemaBase]]:
    """Breadth-first sequence of all classes which inherit from ``cls``."""
    seen = set()
    current: set[type[TSchemaBase]] = {cls}
    while current:
        seen |= current
        current = set(chain.from_iterable(cls.__subclasses__() for cls in current))
        for cls in current - seen:
            yield cls


class _FromDict:
    """
    Class used to construct SchemaBase class hierarchies from a dict.

    The primary purpose of using this class is to be able to build a hash table
    that maps schemas to their wrapper classes. The candidate classes are
    specified in the ``wrapper_classes`` positional-only argument to the constructor.
    """

    hash_tps: ClassVar[defaultdict[int, deque[type[SchemaBase]]]] = defaultdict(deque)
    """
    Maps unique schemas to corresponding types.

    The logic is that after removing a subset of keys, some schemas are identical.

    If there are multiple matches, we use the first one in the ``deque``.

    ``_subclasses`` yields the results of a `breadth-first search`_,
    so the first matching class is the most general match.

    .. _breadth-first search:
       https://en.wikipedia.org/wiki/Breadth-first_search
    """

    hash_resolved: ClassVar[dict[int, Map]] = {}
    """
    Maps unique schemas to their reference-resolved equivalent.

    Ensures that ``_resolve_references`` is evaluated **at most once**, per hash.
    """

    def __init__(self, wrapper_classes: Iterator[type[SchemaBase]], /) -> None:
        cls = type(self)
        for tp in wrapper_classes:
            if tp._schema is not None:
                cls.hash_tps[_hash_schema(tp._schema)].append(tp)

    @overload
    @classmethod
    def from_dict(
        cls,
        dct: TSchemaBase,
        tp: None = ...,
        schema: None = ...,
        rootschema: None = ...,
        default_class: Any = ...,
    ) -> TSchemaBase: ...
    @overload
    @classmethod
    def from_dict(
        cls,
        dct: dict[str, Any] | list[dict[str, Any]],
        tp: Any = ...,
        schema: Any = ...,
        rootschema: Any = ...,
        default_class: type[TSchemaBase] = ...,  # pyright: ignore[reportInvalidTypeVarUse]
    ) -> TSchemaBase: ...
    @overload
    @classmethod
    def from_dict(
        cls,
        dct: dict[str, Any],
        tp: None = ...,
        schema: dict[str, Any] = ...,
        rootschema: None = ...,
        default_class: Any = ...,
    ) -> SchemaBase: ...
    @overload
    @classmethod
    def from_dict(
        cls,
        dct: dict[str, Any],
        tp: type[TSchemaBase],
        schema: None = ...,
        rootschema: None = ...,
        default_class: Any = ...,
    ) -> TSchemaBase: ...
    @overload
    @classmethod
    def from_dict(
        cls,
        dct: dict[str, Any] | list[dict[str, Any]],
        tp: type[TSchemaBase],
        schema: dict[str, Any],
        rootschema: dict[str, Any] | None = ...,
        default_class: Any = ...,
    ) -> Never: ...
    @classmethod
    def from_dict(  # noqa: C901
        cls,
        dct: dict[str, Any] | list[dict[str, Any]] | TSchemaBase,
        tp: type[TSchemaBase] | None = None,
        schema: dict[str, Any] | None = None,
        rootschema: dict[str, Any] | None = None,
        default_class: Any = _passthrough,
    ) -> TSchemaBase | SchemaBase:
        """Construct an object from a dict representation."""
        target_tp: Any
        current_schema: dict[str, Any]
        hash_schema: int
        if isinstance(dct, SchemaBase):
            return dct
        elif tp is not None:
            current_schema = tp._schema
            hash_schema = _hash_schema(current_schema)
            root_schema: dict[str, Any] = rootschema or tp._rootschema or current_schema
            target_tp = tp
        elif schema is not None:
            current_schema = schema
            hash_schema = _hash_schema(current_schema)
            root_schema = rootschema or current_schema
            matches = cls.hash_tps[hash_schema]
            target_tp = next(iter(matches), default_class)
        else:
            msg = "Must provide either `tp` or `schema`, but not both."
            raise ValueError(msg)

        from_dict = partial(cls.from_dict, rootschema=root_schema)
        if (resolved := cls.hash_resolved.get(hash_schema)) is None:
            resolved = _resolve_references(current_schema, root_schema)
            cls.hash_resolved[hash_schema] = resolved
        if "anyOf" in resolved:
            for possible in resolved["anyOf"]:
                # NOTE: Instead of raise/except/continue
                # Pre-"zero-cost" exceptions, this has a huge performance gain.
                # https://docs.python.org/3/whatsnew/3.11.html#misc
                # https://github.com/python/cpython/blob/9b3749849eda4012261a112b22eb07f26fd345a9/InternalDocs/exception_handling.md
                it_errs = _validator(possible, root_schema).iter_errors(dct)
                if next(it_errs, None) is None:
                    return from_dict(dct, schema=possible, default_class=target_tp)

        if _is_dict(dct):
            # TODO: handle schemas for additionalProperties/patternProperties
            if props := resolved.get("properties"):
                kwds = {
                    k: (from_dict(v, schema=sch) if (sch := props.get(k)) else v)
                    for k, v in dct.items()
                }
                return target_tp(**kwds)
            else:
                return target_tp(**dct)
        elif _is_list(dct):
            item_schema: dict[str, Any] = resolved.get("items", {})
            return target_tp([from_dict(k, schema=item_schema) for k in dct])
        else:
            # NOTE: Unsure what is valid here
            return target_tp(dct)


class _PropertySetter:
    def __init__(self, prop: str, schema: dict[str, Any]) -> None:
        self.prop = prop
        self.schema = schema

    def __get__(self, obj, cls):
        from altair import vegalite

        self.obj = obj
        self.cls = cls
        # The docs from the encoding class parameter (e.g. `bin` in X, Color,
        # etc); this provides a general description of the parameter.
        self.__doc__ = self.schema["description"].replace("__", "**")
        property_name = f"{self.prop}"[0].upper() + f"{self.prop}"[1:]
        if hasattr(vegalite, property_name):
            altair_prop = getattr(vegalite, property_name)
            # Add the docstring from the helper class (e.g. `BinParams`) so
            # that all the parameter names of the helper class are included in
            # the final docstring
            parameter_index = altair_prop.__doc__.find("Parameters\n")
            if parameter_index > -1:
                self.__doc__ = (
                    altair_prop.__doc__[:parameter_index].replace("    ", "")
                    + self.__doc__
                    + textwrap.dedent(
                        f"\n\n    {altair_prop.__doc__[parameter_index:]}"
                    )
                )
            # For short docstrings such as Aggregate, Stack, et
            else:
                self.__doc__ = (
                    altair_prop.__doc__.replace("    ", "") + "\n" + self.__doc__
                )
            # Add signatures and tab completion for the method and parameter names
            self.__signature__ = inspect.signature(altair_prop)
            self.__wrapped__ = inspect.getfullargspec(altair_prop)
            self.__name__ = altair_prop.__name__
        else:
            # It seems like bandPosition is the only parameter that doesn't
            # have a helper class.
            pass
        return self

    def __call__(self, *args: Any, **kwargs: Any):
        obj = self.obj.copy()
        # TODO: use schema to validate
        obj[self.prop] = args[0] if args else kwargs
        return obj


def with_property_setters(cls: type[TSchemaBase]) -> type[TSchemaBase]:
    """Decorator to add property setters to a Schema class."""
    schema = cls.resolve_references()
    for prop, propschema in schema.get("properties", {}).items():
        setattr(cls, prop, _PropertySetter(prop, propschema))
    return cls
