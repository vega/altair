"""
Request for comment on additions to `api.py`.

Ideally these would be introduced *after* cleaning up the top-level namespace.

Actual runtime dependencies:
- altair.utils.core
- altair.utils.schemapi

The rest are to define aliases only.
"""

# mypy: ignore-errors
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Literal, Mapping, Sequence, Union

from typing_extensions import TypeAlias

from altair.utils.core import TYPECODE_MAP as _TYPE_CODE
from altair.utils.core import parse_shorthand as _parse
from altair.utils.schemapi import Optional, SchemaBase, Undefined
from altair.vegalite.v5.api import Parameter, SelectionPredicateComposition
from altair.vegalite.v5.schema._typing import (
    BinnedTimeUnit_T,
    MultiTimeUnit_T,
    SingleTimeUnit_T,
    Type_T,
    Map,
)
from altair.vegalite.v5.schema.core import (
    FieldEqualPredicate,
    FieldGTEPredicate,
    FieldGTPredicate,
    FieldLTEPredicate,
    FieldLTPredicate,
    FieldOneOfPredicate,
    FieldRangePredicate,
    FieldValidPredicate,
)
from altair.vegalite.v5.schema import channels

if TYPE_CHECKING:
    from altair.utils.core import DataFrameLike
    from altair.vegalite.v5.schema._typing import AggregateOp_T
    from altair.vegalite.v5.schema.core import Predicate


__all__ = ["agg", "field"]

EncodeType: TypeAlias = Union[Type_T, Literal["O", "N", "Q", "T", "G"], None]
AnyTimeUnit: TypeAlias = Union[MultiTimeUnit_T, BinnedTimeUnit_T, SingleTimeUnit_T]
TimeUnitType: TypeAlias = Optional[Union[Dict[str, Any], SchemaBase, AnyTimeUnit]]
RangeType: TypeAlias = Union[
    Dict[str, Any],
    Parameter,
    SchemaBase,
    Sequence[Union[Dict[str, Any], None, float, Parameter, SchemaBase]],
]
ValueType: TypeAlias = Union[str, bool, float, Dict[str, Any], Parameter, SchemaBase]
OneOfType: TypeAlias = Union[str, bool, float, Dict[str, Any], SchemaBase]


_ENCODINGS = frozenset(
    (
        "ordinal",
        "O",
        "nominal",
        "N",
        "quantitative",
        "Q",
        "temporal",
        "T",
        "geojson",
        "G",
        None,
    )
)


def _parse_aggregate(
    aggregate: AggregateOp_T, name: str | None, encode_type: EncodeType, /
) -> dict[str, Any]:
    if encode_type in _ENCODINGS:
        enc = f":{_TYPE_CODE.get(s, s)}" if (s := encode_type) else ""
        return _parse(f"{aggregate}({name or ''}){enc}")
    else:
        msg = (
            f"Expected a short/long-form encoding type, but got {encode_type!r}.\n\n"
            f"Try passing one of the following to `type`:\n"
            f"{', '.join(sorted(f'{e!r}' for e in _ENCODINGS))}."
        )
        raise TypeError(msg)


def _wrap_composition(predicate: Predicate, /) -> SelectionPredicateComposition:
    return SelectionPredicateComposition(predicate.to_dict())


def _one_of_flatten(
    values: tuple[OneOfType, ...] | tuple[Sequence[OneOfType]] | tuple[Any, ...], /
) -> Sequence[OneOfType]:
    if (
        len(values) == 1
        and not isinstance(values[0], (str, bool, float, int, Mapping, SchemaBase))
        and isinstance(values[0], Sequence)
    ):
        return values[0]
    elif len(values) > 1:
        return values
    else:
        msg = (
            f"Expected `values` to be either a single `Sequence` "
            f"or used variadically, but got: {values!r}."
        )
        raise TypeError(msg)


def _one_of_variance(val_1: Any, *rest: OneOfType) -> Sequence[Any]:
    # Required that all elements are the same type
    tp = type(val_1)
    if all(isinstance(v, tp) for v in rest):
        return (val_1, *rest)
    else:
        msg = (
            f"Expected all `values` to be of the same type, but got:\n"
            f"{tuple(f'{type(v).__name__}' for v in (val_1, *rest))!r}"
        )
        raise TypeError(msg)


class _FieldMeta(type):
    def __new__(  # type: ignore[misc]
        cls, shorthand: dict[str, Any] | str, /, data: DataFrameLike | None = None
    ) -> dict[str, Any]:
        return _parse(shorthand=shorthand, data=data)

    def argmin(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("argmin", col_name, type)

    def argmax(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("argmax", col_name, type)

    def average(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("average", col_name, type)

    def count(
        self, col_name: str | None = None, /, type: EncodeType = "Q"
    ) -> dict[str, Any]:
        return _parse_aggregate("count", col_name, type)

    def distinct(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("distinct", col_name, type)

    def max(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("max", col_name, type)

    def mean(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("mean", col_name, type)

    def median(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("median", col_name, type)

    def min(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("min", col_name, type)

    def missing(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("missing", col_name, type)

    def product(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("product", col_name, type)

    def q1(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("q1", col_name, type)

    def q3(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("q3", col_name, type)

    def ci0(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("ci0", col_name, type)

    def ci1(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("ci1", col_name, type)

    def stderr(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("stderr", col_name, type)

    def stdev(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("stdev", col_name, type)

    def stdevp(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("stdevp", col_name, type)

    def sum(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("sum", col_name, type)

    def valid(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("valid", col_name, type)

    def values(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("values", col_name, type)

    def variance(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("variance", col_name, type)

    def variancep(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("variancep", col_name, type)

    def exponential(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("exponential", col_name, type)

    def exponentialb(
        self, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("exponentialb", col_name, type)


class agg:
    """
    Utility class providing autocomplete for shorthand.

    Functional alternative to shorthand mini-language.
    """

    def __new__(  # type: ignore[misc]
        cls, shorthand: dict[str, Any] | str, /, data: DataFrameLike | None = None
    ) -> dict[str, Any]:
        return _parse(shorthand=shorthand, data=data)

    @classmethod
    def argmin(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("argmin", col_name, type)

    @classmethod
    def argmax(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("argmax", col_name, type)

    @classmethod
    def average(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("average", col_name, type)

    @classmethod
    def count(
        cls, col_name: str | None = None, /, type: EncodeType = "Q"
    ) -> dict[str, Any]:
        return _parse_aggregate("count", col_name, type)

    @classmethod
    def distinct(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("distinct", col_name, type)

    @classmethod
    def max(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("max", col_name, type)

    @classmethod
    def mean(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("mean", col_name, type)

    @classmethod
    def median(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("median", col_name, type)

    @classmethod
    def min(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("min", col_name, type)

    @classmethod
    def missing(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("missing", col_name, type)

    @classmethod
    def product(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("product", col_name, type)

    @classmethod
    def q1(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("q1", col_name, type)

    @classmethod
    def q3(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("q3", col_name, type)

    @classmethod
    def ci0(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("ci0", col_name, type)

    @classmethod
    def ci1(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("ci1", col_name, type)

    @classmethod
    def stderr(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("stderr", col_name, type)

    @classmethod
    def stdev(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("stdev", col_name, type)

    @classmethod
    def stdevp(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("stdevp", col_name, type)

    @classmethod
    def sum(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("sum", col_name, type)

    @classmethod
    def valid(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("valid", col_name, type)

    @classmethod
    def values(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("values", col_name, type)

    @classmethod
    def variance(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("variance", col_name, type)

    @classmethod
    def variancep(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("variancep", col_name, type)

    @classmethod
    def exponential(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("exponential", col_name, type)

    @classmethod
    def exponentialb(
        cls, col_name: str | None = None, /, type: EncodeType = None
    ) -> dict[str, Any]:
        return _parse_aggregate("exponentialb", col_name, type)


class field:
    """
    Utility class for field predicates and shorthand parsing.

    Examples
    --------
    >>> field("Origin")
    {'field': 'Origin'}

    >>> field("Origin:N")
    {'field': 'Origin', 'type': 'nominal'}

    >>> field.one_of("Origin", "Japan", "Europe")
    SelectionPredicateComposition({'field': 'Origin', 'oneOf': ['Japan', 'Europe']})
    """

    def __new__(  # type: ignore[misc]
        cls, shorthand: dict[str, Any] | str, /, data: DataFrameLike | None = None
    ) -> dict[str, Any]:
        return _parse(shorthand=shorthand, data=data)

    @classmethod
    def one_of(
        cls,
        field: str,
        /,
        *values: OneOfType | Sequence[OneOfType],
        timeUnit: TimeUnitType = Undefined,
    ) -> SelectionPredicateComposition:
        seq = _one_of_flatten(values)
        one_of = _one_of_variance(*seq)
        p = FieldOneOfPredicate(field=field, oneOf=one_of, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def eq(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldEqualPredicate(field=field, equal=value, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def lt(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldLTPredicate(field=field, lt=value, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def lte(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldLTEPredicate(field=field, lte=value, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def gt(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldGTPredicate(field=field, gt=value, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def gte(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldGTEPredicate(field=field, gte=value, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def valid(
        cls, field: str, value: bool, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldValidPredicate(field=field, valid=value, timeUnit=timeUnit)
        return _wrap_composition(p)

    @classmethod
    def range(
        cls, field: str, value: RangeType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> SelectionPredicateComposition:
        p = FieldRangePredicate(field=field, range=value, timeUnit=timeUnit)
        return _wrap_composition(p)


class field_into:
    def __init__(self, arg: Map, /) -> None:
        self._arg: Map = arg

    def angle(self, *args: Any, **kwds: Any) -> channels.Angle: ...
    def color(self, *args: Any, **kwds: Any) -> channels.Color: ...
    def column(self, *args: Any, **kwds: Any) -> Any: ...
    def description(self, *args: Any, **kwds: Any) -> Any: ...
    def detail(self, *args: Any, **kwds: Any) -> Any: ...
    def facet(self, *args: Any, **kwds: Any) -> Any: ...
    def fill(self, *args: Any, **kwds: Any) -> Any: ...
    def fill_opacity(self, *args: Any, **kwds: Any) -> Any: ...
    def href(self, *args: Any, **kwds: Any) -> Any: ...
    def key(self, *args: Any, **kwds: Any) -> Any: ...
    def latitude(self, *args: Any, **kwds: Any) -> Any: ...
    def latitude2(self, *args: Any, **kwds: Any) -> Any: ...
    def longitude(self, *args: Any, **kwds: Any) -> Any: ...
    def longitude2(self, *args: Any, **kwds: Any) -> Any: ...
    def opacity(self, *args: Any, **kwds: Any) -> Any: ...
    def order(self, *args: Any, **kwds: Any) -> Any: ...
    def radius(self, *args: Any, **kwds: Any) -> Any: ...
    def radius2(self, *args: Any, **kwds: Any) -> Any: ...
    def row(self, *args: Any, **kwds: Any) -> Any: ...
    def shape(self, *args: Any, **kwds: Any) -> Any: ...
    def size(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke_dash(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke_opacity(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke_width(self, *args: Any, **kwds: Any) -> Any: ...
    def text(self, *args: Any, **kwds: Any) -> Any: ...
    def theta(self, *args: Any, **kwds: Any) -> Any: ...
    def theta2(self, *args: Any, **kwds: Any) -> Any: ...
    def tooltip(self, *args: Any, **kwds: Any) -> Any: ...
    def url(self, *args: Any, **kwds: Any) -> Any: ...
    def x(self, *args: Any, **kwds: Any) -> channels.X:
        return channels.X(*args, **self._arg, **kwds)

    def x2(self, *args: Any, **kwds: Any) -> channels.X2:
        return channels.X2(*args, **self._arg, **kwds)

    def x_error(self, *args: Any, **kwds: Any) -> channels.XError: ...
    def x_error2(self, *args: Any, **kwds: Any) -> channels.XError2: ...
    def x_offset(self, *args: Any, **kwds: Any) -> channels.XOffset: ...
    def y(self, *args: Any, **kwds: Any) -> channels.Y:
        return channels.Y(*args, **self._arg, **kwds)

    def y2(self, *args: Any, **kwds: Any) -> channels.Y2:
        return channels.Y2(*args, **self._arg, **kwds)

    def y_error(self, *args: Any, **kwds: Any) -> channels.YError: ...
    def y_error2(self, *args: Any, **kwds: Any) -> channels.YError2: ...
    def y_offset(self, *args: Any, **kwds: Any) -> channels.YOffset: ...
    @property
    def value(self) -> _ChannelValueNamespace:
        return _ChannelValueNamespace(self._arg)


class _ChannelValueNamespace:
    def __init__(self, arg: Map, /) -> None:
        self._arg: Map = arg

    def angle(self, *args: Any, **kwds: Any) -> Any: ...
    def color(self, *args: Any, **kwds: Any) -> Any: ...
    def description(self, *args: Any, **kwds: Any) -> Any: ...
    def fill(self, *args: Any, **kwds: Any) -> Any: ...
    def fill_opacity(self, *args: Any, **kwds: Any) -> Any: ...
    def href(self, *args: Any, **kwds: Any) -> Any: ...
    def latitude2(self, *args: Any, **kwds: Any) -> Any: ...
    def longitude2(self, *args: Any, **kwds: Any) -> Any: ...
    def opacity(self, *args: Any, **kwds: Any) -> Any: ...
    def order(self, *args: Any, **kwds: Any) -> Any: ...
    def radius(self, *args: Any, **kwds: Any) -> Any: ...
    def radius2(self, *args: Any, **kwds: Any) -> Any: ...
    def shape(self, *args: Any, **kwds: Any) -> Any: ...
    def size(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke_dash(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke_opacity(self, *args: Any, **kwds: Any) -> Any: ...
    def stroke_width(self, *args: Any, **kwds: Any) -> Any: ...
    def text(self, *args: Any, **kwds: Any) -> Any: ...
    def theta(self, *args: Any, **kwds: Any) -> Any: ...
    def theta2(self, *args: Any, **kwds: Any) -> Any: ...
    def tooltip(self, *args: Any, **kwds: Any) -> Any: ...
    def url(self, *args: Any, **kwds: Any) -> Any: ...
    def x(self, *args: Any, **kwds: Any) -> channels.XValue:
        return channels.XValue(*args, **self._arg, **kwds)

    def x2(self, *args: Any, **kwds: Any) -> channels.X2Value:
        return channels.X2Value(*args, **self._arg, **kwds)

    def x_error(self, *args: Any, **kwds: Any) -> channels.XErrorValue: ...
    def x_error2(self, *args: Any, **kwds: Any) -> channels.XError2Value: ...
    def x_offset(self, *args: Any, **kwds: Any) -> channels.XOffsetValue: ...
    def y(self, *args: Any, **kwds: Any) -> channels.YValue:
        return channels.YValue(*args, **self._arg, **kwds)

    def y2(self, *args: Any, **kwds: Any) -> channels.Y2Value:
        return channels.Y2Value(*args, **self._arg, **kwds)

    def y_error(self, *args: Any, **kwds: Any) -> channels.YErrorValue: ...
    def y_error2(self, *args: Any, **kwds: Any) -> channels.YError2Value: ...
    def y_offset(self, *args: Any, **kwds: Any) -> channels.YOffsetValue: ...


# field_out = agg.q1()
# wrapped = field_into(field_out).value.x()
## efg = field2.angle()
## some_field = field2.min("Cost", "Q")
# some_field = field_into(field("Cost:Q"))
# beeeee = some_field.x()
# cee = some_field.value.x()
#
#
# ffff = field_into(field("Cost:Q")).x2().bandPosition(4.7)
