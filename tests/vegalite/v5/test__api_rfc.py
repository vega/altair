from __future__ import annotations

from typing import TYPE_CHECKING

# ruff: noqa: F401
import re
import pytest

import altair as alt

from altair.vegalite.v5._api_rfc import agg, field, EncodeType
from altair.utils.core import TYPECODE_MAP, INV_TYPECODE_MAP

if TYPE_CHECKING:
    from altair.vegalite.v5.schema._typing import AggregateOp_T


def test_fail_shorthand() -> None:
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
def test_passing_shorthand(
    method_name: AggregateOp_T, col_name: str | None, enc_type: EncodeType
):
    actual = getattr(agg, method_name)(col_name, enc_type)
    assert isinstance(actual, dict)
    assert actual["aggregate"] == method_name
    if col_name:
        assert actual["field"] == col_name
    if enc_type:
        assert actual["type"] == INV_TYPECODE_MAP.get(enc_type, enc_type)


def test_fail_one_of() -> None:
    with pytest.raises(TypeError, match=re.compile(r"Expected.+same type", re.DOTALL)):
        field.one_of("field 1", 5, 6, 7, "nineteen", 8000.4)  # type: ignore[arg-type]


def test_examples_field() -> None:
    print(field("Origin"))


def test_compose_field():
    comp = field.eq("field 1", 10)
    assert isinstance(comp, alt.SelectionPredicateComposition)


def test_compose_predicates():
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
