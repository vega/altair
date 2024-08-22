from __future__ import annotations

import contextlib
import inspect
import json
import operator
import sys
import textwrap
from collections import defaultdict
from functools import partial
from importlib.metadata import version as importlib_version
from itertools import chain, groupby, islice, zip_longest
from math import ceil
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Final,
    Iterable,
    Iterator,
    KeysView,
    List,
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

if TYPE_CHECKING:
    from typing import ClassVar, Literal, Mapping

    from jsonschema.protocols import Validator, _JsonParameter
    from referencing import Registry, Specification

    from altair.typing import ChartType

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


_VEGA_LITE_ROOT_URI: Final = "urn:vega-lite-schema"
"""
Prefix added to each ``"$ref"``.

This URI is arbitrary and could be anything else.

It just cannot be an empty string as we need to reference the schema registered in
the ``referencing.Registry``."""

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
    spec: _JsonParameter,
    schema: dict[str, Any],
    rootschema: dict[str, Any] | None = None,
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
    """
    it_errors = _iter_validator_errors(spec, schema, rootschema=rootschema)
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


def validate_jsonschema_fail_fast(
    spec: _JsonParameter,
    schema: dict[str, Any],
    rootschema: dict[str, Any] | None = None,
) -> None:
    """
    Raise as quickly as possible.

    Use instead of ``validate_jsonschema`` when any information about the error(s) are not needed.
    """
    if (
        err := next(_iter_validator_errors(spec, schema, rootschema=rootschema), None)
    ) is not None:
        raise err


def _get_schema_dialect_uri(schema: dict[str, Any]) -> str:
    """
    Return value of `$schema`_.

    Defines which JSON Schema draft ``schema`` was written for.

    .. _$schema:
       https://json-schema.org/understanding-json-schema/reference/schema#schema

    """
    return schema.get("$schema", _DEFAULT_DIALECT_URI)


def _prepare_references(schema: dict[str, Any], /) -> dict[str, Any]:
    """
    Return a deep copy of ``schema`` w/ replaced uri(s).

    All encountered ``dict | list``(s) will be reconstructed
    w/ ``_VEGA_LITE_ROOT_URI`` in front of all nested``$ref`` values.

    Notes
    -----
    ``copy.deepcopy`` is not needed as the iterator yields new objects.
    """
    return dict(_rec_refs(schema))


def _rec_refs(m: dict[str, Any], /) -> Iterator[tuple[str, Any]]:
    """
    Recurse through a schema, yielding fresh copies of mutable containers.

    Adds ``_VEGA_LITE_ROOT_URI`` in front of all nested``$ref`` values.
    """
    for k, v in m.items():
        if k == "$ref":
            yield k, f"{_VEGA_LITE_ROOT_URI}{v}"
        elif isinstance(v, dict):
            yield k, dict(_rec_refs(v))
        elif isinstance(v, list):
            yield k, [dict(_rec_refs(el)) if _is_dict(el) else el for el in v]
        else:
            yield k, v


def _prepare_validator(uri: str, /) -> Callable[..., Validator]:
    tp: Callable[..., Validator] = jsonschema.validators.validator_for({"$schema": uri})
    if hasattr(tp, "FORMAT_CHECKER"):
        return partial(tp, format_checker=tp.FORMAT_CHECKER)
    else:
        return tp


if Version(importlib_version("jsonschema")) >= Version("4.18"):
    from functools import lru_cache

    from referencing import Registry
    from referencing.jsonschema import specification_with as _specification_with

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

    def _construct_validator(
        schema: dict[str, Any], rootschema: dict[str, Any] | None = None
    ) -> Validator:
        uri = _get_schema_dialect_uri(rootschema or schema)
        tp = _prepare_validator(uri)
        registry = _registry(rootschema or schema, uri)
        return tp(_prepare_references(schema), registry=registry)

    def _registry(rootschema: dict[str, Any], dialect_id: str) -> Registry[Any]:
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
        specification = specification_with(dialect_id)
        resource = specification.create_resource(rootschema)
        return Registry().with_resource(uri=_VEGA_LITE_ROOT_URI, resource=resource)

    def _resolve_references(
        schema: dict[str, Any], rootschema: dict[str, Any]
    ) -> dict[str, Any]:
        """Resolve schema references until there is no $ref anymore in the top-level of the dictionary."""
        uri = _get_schema_dialect_uri(rootschema)
        registry = _registry(rootschema or schema, uri)
        resolver = registry.resolver()
        while "$ref" in schema:
            schema = resolver.lookup(_VEGA_LITE_ROOT_URI + schema["$ref"]).contents
        return schema
else:

    def _construct_validator(
        schema: dict[str, Any], rootschema: dict[str, Any] | None = None
    ) -> Validator:
        tp = _prepare_validator(_get_schema_dialect_uri(rootschema or schema))
        resolver: Any = (
            jsonschema.RefResolver.from_schema(rootschema) if rootschema else rootschema
        )
        return tp(schema, resolver=resolver)

    def _resolve_references(
        schema: dict[str, Any], rootschema: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Resolve schema references until there is no $ref anymore in the top-level of the dictionary.

        ``jsonschema`` deprecated ``RefResolver`` in favor of ``referencing``.

        See https://github.com/python-jsonschema/jsonschema/releases/tag/v4.18.0a1
        """
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


def _iter_validator_errors(
    spec: _JsonParameter,
    schema: dict[str, Any],
    rootschema: dict[str, Any] | None = None,
) -> _ErrsLazy:
    """
    Uses the relevant ``jsonschema`` validator to validate ``spec`` against ``schema`` using `` rootschema`` to resolve references.

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
    return _construct_validator(schema, rootschema).iter_errors(spec)


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


def _subclasses(cls: type[Any]) -> Iterator[type[Any]]:
    """Breadth-first sequence of all classes which inherit from cls."""
    seen = set()
    current: set[type[Any]] = {cls}
    while current:
        seen |= current
        current = set(chain.from_iterable(cls.__subclasses__() for cls in current))
        for cls in current - seen:
            yield cls


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
    elif (
        hasattr(obj, "to_dict")
        and (module_name := obj.__module__)
        and module_name.startswith("altair")
    ):
        return obj.to_dict()
    elif pd_opt is not None and isinstance(obj, pd_opt.Timestamp):
        return pd_opt.Timestamp(obj).isoformat()
    elif _is_iterable(obj, exclude=(str, bytes)):
        return _todict(_from_array_like(obj), context, np_opt, pd_opt)
    else:
        return obj


class SchemaValidationError(jsonschema.ValidationError):
    """A wrapper for jsonschema.ValidationError with friendlier traceback."""

    def __init__(self, obj: SchemaBase, err: ValidationError) -> None:
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
        it = self._errors
        group_1 = list(next(it))
        if (group_2 := next(it, None)) is not None:
            error_messages = []
            for group in group_1, list(group_2), next(it, None):
                if group is not None:
                    error_messages.append(self._get_message_for_errors_group(group))
            message = "\n\n".join(
                self.indent_from_second_line(f"Error {error_id}: {m}")
                for error_id, m in enumerate(error_messages, start=1)
            )
            return f"Multiple errors were found.\n\n{message}"
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
                bullet_points.append(f"one of {error.validator_value}")

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
        if attr in self._kwds:
            return self._kwds[attr]
        else:
            try:
                _getattr = super().__getattr__  # pyright: ignore[reportAttributeAccessIssue]
            except AttributeError:
                _getattr = super().__getattribute__
            return _getattr(attr)

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
            If True (default), then validate the output dictionary
            against the schema.
        ignore : list[str], optional
            A list of keys to ignore. It is usually not needed
            to specify this argument as a user.
        context : dict[str, Any], optional
            A context dictionary. It is usually not needed
            to specify this argument as a user.

        Notes
        -----
        Technical: The ignore parameter will *not* be passed to child to_dict
        function calls.

        Returns
        -------
        dict
            The dictionary representation of this object

        Raises
        ------
        SchemaValidationError :
            if validate=True and the dict does not conform to the schema
        """
        if context is None:
            context = {}
        if ignore is None:
            ignore = []
        # The following return the package only if it has already been
        # imported - otherwise they return None. This is useful for
        # isinstance checks - for example, if pandas has not been imported,
        # then an object is definitely not a `pandas.Timestamp`.
        pd_opt = sys.modules.get("pandas")
        np_opt = sys.modules.get("numpy")

        if self._args and not self._kwds:
            result = _todict(
                self._args[0], context=context, np_opt=np_opt, pd_opt=pd_opt
            )
        elif not self._args:
            kwds = self._kwds.copy()
            # parsed_shorthand is added by FieldChannelMixin.
            # It's used below to replace shorthand with its long form equivalent
            # parsed_shorthand is removed from context if it exists so that it is
            # not passed to child to_dict function calls
            parsed_shorthand = context.pop("parsed_shorthand", {})
            # Prevent that pandas categorical data is automatically sorted
            # when a non-ordinal data type is specifed manually
            # or if the encoding channel does not support sorting
            if "sort" in parsed_shorthand and (
                "sort" not in kwds or kwds["type"] not in {"ordinal", Undefined}
            ):
                parsed_shorthand.pop("sort")

            kwds.update(
                {
                    k: v
                    for k, v in parsed_shorthand.items()
                    if kwds.get(k, Undefined) is Undefined
                }
            )
            kwds = {
                k: v for k, v in kwds.items() if k not in {*list(ignore), "shorthand"}
            }
            if "mark" in kwds and isinstance(kwds["mark"], str):
                kwds["mark"] = {"type": kwds["mark"]}
            result = _todict(kwds, context=context, np_opt=np_opt, pd_opt=pd_opt)
        else:
            msg = (
                f"{self.__class__} instance has both a value and properties : "
                "cannot serialize to dict"
            )
            raise ValueError(msg)
        if validate:
            try:
                self.validate(result)
            except ValidationError as err:
                # We do not raise `from err` as else the resulting
                # traceback is very long as it contains part
                # of the Vega-Lite schema. It would also first
                # show the less helpful ValidationError instead of
                # the more user friendly SchemaValidationError
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
            If True (default), then validate the output dictionary
            against the schema.
        indent : int, optional
            The number of spaces of indentation to use. The default is 2.
        sort_keys : bool, optional
            If True (default), sort keys in the output.
        ignore : list[str], optional
            A list of keys to ignore. It is usually not needed
            to specify this argument as a user.
        context : dict[str, Any], optional
            A context dictionary. It is usually not needed
            to specify this argument as a user.
        **kwargs
            Additional keyword arguments are passed to ``json.dumps()``

        Notes
        -----
        Technical: The ignore parameter will *not* be passed to child to_dict
        function calls.

        Returns
        -------
        str
            The JSON specification of the chart object.
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

        Returns
        -------
        obj : Schema object
            The wrapped schema

        Raises
        ------
        jsonschema.ValidationError :
            if validate=True and dct does not conform to the schema
        """
        if validate:
            cls.validate(dct)
        converter = _FromDict(cls._default_wrapper_classes())
        return converter.from_dict(dct, cls)

    @classmethod
    def from_json(
        cls,
        json_string: str,
        validate: bool = True,
        **kwargs: Any,
        # Type hints for this method would get rather complicated
        # if we want to provide a more specific return type
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
        rootschema = cls._rootschema or cls._schema or schema
        if rootschema is None:
            name = type(cls).__name__
            msg = (
                f"{name}.resolve_references() provided only `None` values for:\n"
                f"{schema=}, {cls._schema=}, {cls._rootschema=}.\n\n"
                f"This variant indicates the class definition {name!r} is invalid."
            )
            raise TypeError(msg)
        else:
            return _resolve_references(schema or cls._schema, rootschema=rootschema)

    @classmethod
    def validate_property(
        cls, name: str, value: Any, schema: dict[str, Any] | None = None
    ) -> None:
        """Validate a property against property schema in the context of the rootschema."""
        # The following return the package only if it has already been
        # imported - otherwise they return None. This is useful for
        # isinstance checks - for example, if pandas has not been imported,
        # then an object is definitely not a `pandas.Timestamp`.
        pd_opt = sys.modules.get("pandas")
        np_opt = sys.modules.get("numpy")
        value = _todict(value, context={}, np_opt=np_opt, pd_opt=pd_opt)
        props = cls.resolve_references(schema or cls._schema).get("properties", {})
        validate_jsonschema(
            value, props.get(name, {}), rootschema=cls._rootschema or cls._schema
        )

    def __dir__(self) -> list[str]:
        return sorted(chain(super().__dir__(), self._kwds))


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


def _passthrough(*args: Any, **kwds: Any) -> Any | dict[str, Any]:
    return args[0] if args else kwds


def _freeze(val):
    if isinstance(val, dict):
        return frozenset((k, _freeze(v)) for k, v in val.items())
    elif isinstance(val, set):
        return frozenset(_freeze(v) for v in val)
    elif isinstance(val, (list, tuple)):
        return tuple(_freeze(v) for v in val)
    else:
        return val


class _FromDict:
    """
    Class used to construct SchemaBase class hierarchies from a dict.

    The primary purpose of using this class is to be able to build a hash table
    that maps schemas to their wrapper classes. The candidate classes are
    specified in the ``wrapper_classes`` positional-only argument to the constructor.
    """

    _hash_exclude_keys = ("definitions", "title", "description", "$schema", "id")

    def __init__(self, wrapper_classes: Iterable[type[SchemaBase]], /) -> None:
        # Create a mapping of a schema hash to a list of matching classes
        # This lets us quickly determine the correct class to construct
        self.class_dict: dict[int, list[type[SchemaBase]]] = defaultdict(list)
        for tp in wrapper_classes:
            if tp._schema is not None:
                self.class_dict[self.hash_schema(tp._schema)].append(tp)

    @classmethod
    def hash_schema(cls, schema: dict[str, Any], use_json: bool = True) -> int:
        """
        Compute a python hash for a nested dictionary which properly handles dicts, lists, sets, and tuples.

        At the top level, the function excludes from the hashed schema all keys
        listed in `exclude_keys`.

        This implements two methods: one based on conversion to JSON, and one based
        on recursive conversions of unhashable to hashable types; the former seems
        to be slightly faster in several benchmarks.
        """
        if cls._hash_exclude_keys and isinstance(schema, dict):
            schema = {
                key: val
                for key, val in schema.items()
                if key not in cls._hash_exclude_keys
            }
        s: Any = json.dumps(schema, sort_keys=True) if use_json else _freeze(schema)
        return hash(s)

    @overload
    def from_dict(
        self,
        dct: TSchemaBase,
        tp: None = ...,
        schema: None = ...,
        rootschema: None = ...,
        default_class: Any = ...,
    ) -> TSchemaBase: ...
    @overload
    def from_dict(
        self,
        dct: dict[str, Any] | list[dict[str, Any]],
        tp: Any = ...,
        schema: Any = ...,
        rootschema: Any = ...,
        default_class: type[TSchemaBase] = ...,  # pyright: ignore[reportInvalidTypeVarUse]
    ) -> TSchemaBase: ...
    @overload
    def from_dict(
        self,
        dct: dict[str, Any],
        tp: None = ...,
        schema: dict[str, Any] = ...,
        rootschema: None = ...,
        default_class: Any = ...,
    ) -> SchemaBase: ...
    @overload
    def from_dict(
        self,
        dct: dict[str, Any],
        tp: type[TSchemaBase],
        schema: None = ...,
        rootschema: None = ...,
        default_class: Any = ...,
    ) -> TSchemaBase: ...
    @overload
    def from_dict(
        self,
        dct: dict[str, Any] | list[dict[str, Any]],
        tp: type[TSchemaBase],
        schema: dict[str, Any],
        rootschema: dict[str, Any] | None = ...,
        default_class: Any = ...,
    ) -> Never: ...
    def from_dict(
        self,
        dct: dict[str, Any] | list[dict[str, Any]] | TSchemaBase,
        tp: type[TSchemaBase] | None = None,
        schema: dict[str, Any] | None = None,
        rootschema: dict[str, Any] | None = None,
        default_class: Any = _passthrough,
    ) -> TSchemaBase | SchemaBase:
        """Construct an object from a dict representation."""
        target_tp: Any
        current_schema: dict[str, Any]
        if isinstance(dct, SchemaBase):
            return dct
        elif tp is not None:
            current_schema = tp._schema
            root_schema: dict[str, Any] = rootschema or tp._rootschema or current_schema
            target_tp = tp
        elif schema is not None:
            # If there are multiple matches, we use the first one in the dict.
            # Our class dict is constructed breadth-first from top to bottom,
            # so the first class that matches is the most general match.
            current_schema = schema
            root_schema = rootschema or current_schema
            matches = self.class_dict[self.hash_schema(current_schema)]
            target_tp = matches[0] if matches else default_class
        else:
            msg = "Must provide either `tp` or `schema`, but not both."
            raise ValueError(msg)

        from_dict = partial(self.from_dict, rootschema=root_schema)
        # Can also return a list?
        resolved = _resolve_references(current_schema, root_schema)
        if "anyOf" in resolved or "oneOf" in resolved:
            schemas = resolved.get("anyOf", []) + resolved.get("oneOf", [])
            for possible in schemas:
                try:
                    validate_jsonschema_fail_fast(dct, possible, rootschema=root_schema)
                except ValidationError:
                    continue
                else:
                    return from_dict(dct, schema=possible, default_class=target_tp)

        if _is_dict(dct):
            # TODO: handle schemas for additionalProperties/patternProperties
            props: dict[str, Any] = resolved.get("properties", {})
            kwds = {
                k: (from_dict(v, schema=props[k]) if k in props else v)
                for k, v in dct.items()
            }
            return target_tp(**kwds)
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
