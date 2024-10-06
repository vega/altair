from __future__ import annotations

# ruff: noqa: F401
import re
from typing import TYPE_CHECKING

import pytest

import altair as alt
from altair.utils.core import INV_TYPECODE_MAP, TYPECODE_MAP
from altair.vegalite.v5._api_rfc import EncodeType, agg, field

if TYPE_CHECKING:
    from altair.vegalite.v5.schema._typing import AggregateOp_T


def test_agg_type_invalid() -> None:
    with pytest.raises(
        TypeError, match=re.compile(r"'bogus'.+Try.+'quantitative'", re.DOTALL)
    ):
        agg.count(type="bogus")  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "enc_type",
    [
        "quantitative",
        "ordinal",
        "temporal",
        "nominal",
        "geojson",
        "O",
        "N",
        "Q",
        "T",
        "G",
        None,
    ],
)
@pytest.mark.parametrize("col_name", ["column_1", None])
@pytest.mark.parametrize(
    "method_name",
    [
        "argmax",
        "argmin",
        "average",
        "count",
        "distinct",
        "max",
        "mean",
        "median",
        "min",
        "missing",
        "product",
        "q1",
        "q3",
        "ci0",
        "ci1",
        "stderr",
        "stdev",
        "stdevp",
        "sum",
        "valid",
        "values",
        "variance",
        "variancep",
        "exponential",
        "exponentialb",
    ],
)
def test_agg_methods(
    method_name: AggregateOp_T, col_name: str | None, enc_type: EncodeType
):
    actual = getattr(agg, method_name)(col_name, enc_type)
    assert isinstance(actual, dict)
    assert actual["aggregate"] == method_name
    if col_name:
        assert actual["field"] == col_name
    if enc_type:
        assert actual["type"] == INV_TYPECODE_MAP.get(enc_type, enc_type)


def test_field_one_of_covariant() -> None:
    with pytest.raises(TypeError, match=re.compile(r"Expected.+same type", re.DOTALL)):
        field.one_of("field 1", 5, 6, 7, "nineteen", 8000.4)


def test_field_one_of_variadic():
    args = "A", "B", "C", "D", "E"
    assert field.one_of("field_1", *args) == field.one_of("field_1", args)


def test_field_wrap():
    comp = field.eq("field 1", 10)
    assert isinstance(comp, alt.SelectionPredicateComposition)


def test_field_compose():
    from vega_datasets import data

    cars_select = field.one_of("Origin", "Japan", "Europe") | field.range(
        "Miles_per_Gallon", (25, 40)
    )
    assert isinstance(cars_select, alt.SelectionPredicateComposition)

    source = data.cars()
    chart = (
        alt.Chart(source)
        .mark_point()
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color=alt.condition(cars_select, alt.value("red"), alt.value("grey")),
        )
    )
    chart.to_dict()
