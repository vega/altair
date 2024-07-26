"""
Request for comment on additions to `api.py`.

Ideally these would be introduced *after* cleaning up the top-level namespace.

Actual runtime dependencies:
- altair.utils.core
- altair.utils.schemapi

The rest are to define aliases only.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Literal, Sequence, Union

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
TimeUnitType: TypeAlias = Optional[Union[Dict[str, Any], SchemaBase, AnyTimeUnit]]
RangeType: TypeAlias = Union[
    Dict[str, Any],
    Parameter,
    SchemaBase,
    Sequence[Union[Dict[str, Any], None, float, Parameter, SchemaBase]],
]
ValueType: TypeAlias = Union[str, bool, float, Dict[str, Any], Parameter, SchemaBase]


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
        *values: str | bool | float | dict[str, Any] | SchemaBase,
        timeUnit: TimeUnitType = Undefined,
    ) -> SelectionPredicateComposition:
        tp: type[Any] = type(values[0])
        if all(isinstance(v, tp) for v in values):
            vals: Sequence[Any] = values
            p = FieldOneOfPredicate(field=field, oneOf=vals, timeUnit=timeUnit)
            return _wrap_composition(p)
        else:
            msg = (
                f"Expected all `values` to be of the same type, but got:\n"
                f"{tuple(f"{type(v).__name__}" for v in values)!r}"
            )
            raise TypeError(msg)

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
