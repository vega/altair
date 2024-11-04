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

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, Literal, Union
from typing_extensions import TypeAlias

from altair.utils.core import TYPECODE_MAP as _TYPE_CODE
from altair.utils.core import parse_shorthand as _parse
from altair.utils.schemapi import Optional, SchemaBase, Undefined
from altair.vegalite.v5.api import Parameter
from altair.vegalite.v5.schema import channels
from altair.vegalite.v5.schema._typing import (
    BinnedTimeUnit_T,
    Map,
    MultiTimeUnit_T,
    SingleTimeUnit_T,
    Type_T,
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

if TYPE_CHECKING:
    from altair.utils.core import DataFrameLike
    from altair.vegalite.v5.schema._typing import AggregateOp_T
    from altair.vegalite.v5.schema.core import Predicate


__all__ = ["agg", "field"]

EncodeType: TypeAlias = Union[Type_T, Literal["O", "N", "Q", "T", "G"], None]
AnyTimeUnit: TypeAlias = Union[MultiTimeUnit_T, BinnedTimeUnit_T, SingleTimeUnit_T]
TimeUnitType: TypeAlias = Optional[Union[dict[str, Any], SchemaBase, AnyTimeUnit]]
RangeType: TypeAlias = Union[
    dict[str, Any],
    Parameter,
    SchemaBase,
    Sequence[Union[dict[str, Any], None, float, Parameter, SchemaBase]],
]
ValueType: TypeAlias = Union[str, bool, float, dict[str, Any], Parameter, SchemaBase]
OneOfType: TypeAlias = Union[str, bool, float, dict[str, Any], SchemaBase]


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
    FieldOneOfPredicate({
      field: 'Origin',
      oneOf: ('Japan', 'Europe')
    })
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
    ) -> Predicate:
        seq = _one_of_flatten(values)
        one_of = _one_of_variance(*seq)
        return FieldOneOfPredicate(field=field, oneOf=one_of, timeUnit=timeUnit)

    @classmethod
    def eq(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldEqualPredicate(field=field, equal=value, timeUnit=timeUnit)

    @classmethod
    def lt(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldLTPredicate(field=field, lt=value, timeUnit=timeUnit)

    @classmethod
    def lte(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldLTEPredicate(field=field, lte=value, timeUnit=timeUnit)

    @classmethod
    def gt(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldGTPredicate(field=field, gt=value, timeUnit=timeUnit)

    @classmethod
    def gte(
        cls, field: str, value: ValueType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldGTEPredicate(field=field, gte=value, timeUnit=timeUnit)

    @classmethod
    def valid(
        cls, field: str, value: bool, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldValidPredicate(field=field, valid=value, timeUnit=timeUnit)

    @classmethod
    def range(
        cls, field: str, value: RangeType, /, *, timeUnit: TimeUnitType = Undefined
    ) -> Predicate:
        return FieldRangePredicate(field=field, range=value, timeUnit=timeUnit)


# NOTE: Ignore everything below #
# ----------------------------- #


class field_into:
    """
    Return wrapper for `agg`, `field` shorthand dicts.

    Idea
    ----
    Rather than something like::

        op_1 = alt.X(alt.agg.min("Cost", "Q")).scale(None)

    You could chain entirely from the agg::

        # the internal unpacking will avoid double-checking the shorthand
        op_2 = alt.agg.min("Cost", "Q").x().scale(None)

    Optionally, use the chained constructor::

        op_2_1 = alt.agg.min("Cost", "Q").x(scale=None)


    """

    def __init__(self, arg: Map, /) -> None:
        self._arg: Map = arg

    def angle(self, *args: Any, **kwds: Any) -> channels.Angle: ...
    def color(self, *args: Any, **kwds: Any) -> channels.Color: ...
    def column(self, *args: Any, **kwds: Any) -> channels.Column: ...
    def description(self, *args: Any, **kwds: Any) -> channels.Description: ...
    def detail(self, *args: Any, **kwds: Any) -> channels.Detail: ...
    def facet(self, *args: Any, **kwds: Any) -> channels.Facet: ...
    def fill(self, *args: Any, **kwds: Any) -> channels.Fill: ...
    def fill_opacity(self, *args: Any, **kwds: Any) -> channels.FillOpacity: ...
    def href(self, *args: Any, **kwds: Any) -> channels.Href: ...
    def key(self, *args: Any, **kwds: Any) -> channels.Key: ...
    def latitude(self, *args: Any, **kwds: Any) -> channels.Latitude: ...
    def latitude2(self, *args: Any, **kwds: Any) -> channels.Latitude2: ...
    def longitude(self, *args: Any, **kwds: Any) -> channels.Longitude: ...
    def longitude2(self, *args: Any, **kwds: Any) -> channels.Longitude2: ...
    def opacity(self, *args: Any, **kwds: Any) -> channels.Opacity: ...
    def order(self, *args: Any, **kwds: Any) -> channels.Order: ...
    def radius(self, *args: Any, **kwds: Any) -> channels.Radius: ...
    def radius2(self, *args: Any, **kwds: Any) -> channels.Radius2: ...
    def row(self, *args: Any, **kwds: Any) -> channels.Row: ...
    def shape(self, *args: Any, **kwds: Any) -> channels.Shape: ...
    def size(self, *args: Any, **kwds: Any) -> channels.Size: ...
    def stroke(self, *args: Any, **kwds: Any) -> channels.Stroke: ...
    def stroke_dash(self, *args: Any, **kwds: Any) -> channels.StrokeDash: ...
    def stroke_opacity(self, *args: Any, **kwds: Any) -> channels.StrokeOpacity: ...
    def stroke_width(self, *args: Any, **kwds: Any) -> channels.StrokeWidth: ...
    def text(self, *args: Any, **kwds: Any) -> channels.Text: ...
    def theta(self, *args: Any, **kwds: Any) -> channels.Theta: ...
    def theta2(self, *args: Any, **kwds: Any) -> channels.Theta2: ...
    def tooltip(self, *args: Any, **kwds: Any) -> channels.Tooltip: ...
    def url(self, *args: Any, **kwds: Any) -> channels.Url: ...
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


def example_field():
    field_out = agg.q1()
    wrapped = field_into(field_out).x()  # noqa: F841
    some_field = field_into(agg.min("Cost", "Q"))
    beeeee = some_field.x().scale(None).impute(None).axis(None)  # noqa: F841
