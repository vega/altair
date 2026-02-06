"""Unit tests for altair API."""

from __future__ import annotations

import io
import json
import operator
import os
import pathlib
import re
import sys
import tempfile
import warnings
from collections.abc import Mapping
from datetime import date, datetime
from importlib.metadata import version as importlib_version
from importlib.util import find_spec
from typing import TYPE_CHECKING

import jsonschema
import narwhals.stable.v1 as nw
import pandas as pd
import polars as pl
import pytest
from packaging.version import Version

import altair as alt
from altair.utils.core import use_signature_func
from altair.utils.schemapi import Optional, SchemaValidationError, Undefined
from tests import (
    skip_requires_duckdb,
    skip_requires_pyarrow,
    skip_requires_vl_convert,
    slow,
)

if TYPE_CHECKING:
    from typing import Any

    import duckdb

    from altair.vegalite.v6.api import _Conditional, _Conditions
    from altair.vegalite.v6.schema._typing import Map


PANDAS_VERSION = Version(importlib_version("pandas"))


def getargs(*args, **kwargs):
    return args, kwargs


OP_DICT = {
    "layer": operator.add,
    "hconcat": operator.or_,
    "vconcat": operator.and_,
}


def _make_chart_type(chart_type):
    data = pd.DataFrame(
        {
            "x": [28, 55, 43, 91, 81, 53, 19, 87],
            "y": [43, 91, 81, 53, 19, 87, 52, 28],
            "color": list("AAAABBBB"),
        }
    )
    base = (
        alt.Chart(data)
        .mark_point()
        .encode(
            x="x",
            y="y",
            color="color",
        )
    )

    if chart_type in {"layer", "hconcat", "vconcat", "concat"}:
        func = getattr(alt, chart_type)
        return func(base.mark_square(), base.mark_circle())
    elif chart_type == "facet":
        return base.facet("color")
    elif chart_type == "facet_encoding":
        return base.encode(facet="color")
    elif chart_type == "repeat":
        return base.encode(alt.X(alt.repeat(), type="quantitative")).repeat(["x", "y"])
    elif chart_type == "chart":
        return base
    else:
        msg = f"chart_type='{chart_type}' is not recognized"
        raise ValueError(msg)


@pytest.fixture
def basic_chart() -> alt.Chart:
    data = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    return alt.Chart(data).mark_bar().encode(x="a", y="b")


@pytest.fixture
def cars():
    return pd.DataFrame(
        {
            "Name": [
                "chevrolet chevelle malibu",
                "buick skylark 320",
                "plymouth satellite",
                "amc rebel sst",
                "ford torino",
                "ford galaxie 500",
                "chevrolet impala",
                "plymouth fury iii",
                "pontiac catalina",
                "amc ambassador dpl",
            ],
            "Miles_per_Gallon": [
                18.0,
                15.0,
                18.0,
                16.0,
                17.0,
                15.0,
                14.0,
                14.0,
                14.0,
                15.0,
            ],
            "Cylinders": [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            "Displacement": [
                307.0,
                350.0,
                318.0,
                304.0,
                302.0,
                429.0,
                454.0,
                440.0,
                455.0,
                390.0,
            ],
            "Horsepower": [
                130.0,
                165.0,
                150.0,
                150.0,
                140.0,
                198.0,
                220.0,
                215.0,
                225.0,
                190.0,
            ],
            "Weight_in_lbs": [
                3504,
                3693,
                3436,
                3433,
                3449,
                4341,
                4354,
                4312,
                4425,
                3850,
            ],
            "Acceleration": [12.0, 11.5, 11.0, 12.0, 10.5, 10.0, 9.0, 8.5, 10.0, 8.5],
            "Year": [
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
                pd.Timestamp("1970-01-01 00:00:00"),
            ],
            "Origin": [
                "USA",
                "USA",
                "USA",
                "USA",
                "USA",
                "USA",
                "USA",
                "USA",
                "USA",
                "USA",
            ],
        }
    )


def test_chart_data_types():
    def Chart(data):
        return alt.Chart(data).mark_point().encode(x="x:Q", y="y:Q")

    # Url Data
    data = "/path/to/my/data.csv"
    dct = Chart(data).to_dict()
    assert dct["data"] == {"url": data}

    # Dict Data
    data = {"values": [{"x": 1, "y": 2}, {"x": 2, "y": 3}]}
    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = Chart(data).to_dict()
    assert dct["data"] == data

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = Chart(data).to_dict()
    name = dct["data"]["name"]
    assert dct["datasets"][name] == data["values"]

    # DataFrame data
    data = pd.DataFrame({"x": range(5), "y": range(5)})
    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = Chart(data).to_dict()
    assert dct["data"]["values"] == data.to_dict(orient="records")

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = Chart(data).to_dict()
    name = dct["data"]["name"]
    assert dct["datasets"][name] == data.to_dict(orient="records")

    # Named data object
    data = alt.NamedData(name="Foo")
    dct = Chart(data).to_dict()
    assert dct["data"] == {"name": "Foo"}


def test_chart_infer_types():
    try:
        x_dates = pd.date_range("2012", periods=10, freq="YE")
    except (ValueError, TypeError):
        # Older pandas may not recognize "YE"; use "Y" (year-end) instead
        x_dates = pd.date_range("2012", periods=10, freq="Y")
    data = pd.DataFrame(
        {
            "x": x_dates,
            "y": range(10),
            "c": list("abcabcabca"),
            "s": pd.Categorical([1, 2] * 5, categories=[2, 1], ordered=True),
        }
    )

    def _check_encodings(chart):
        dct = chart.to_dict()
        assert dct["encoding"]["x"]["type"] == "temporal"
        assert dct["encoding"]["x"]["field"] == "x"
        assert dct["encoding"]["y"]["type"] == "quantitative"
        assert dct["encoding"]["y"]["field"] == "y"
        assert dct["encoding"]["color"]["type"] == "nominal"
        assert dct["encoding"]["color"]["field"] == "c"
        assert dct["encoding"]["size"]["type"] == "ordinal"
        assert dct["encoding"]["size"]["field"] == "s"
        assert dct["encoding"]["size"]["sort"] == [2, 1]
        assert dct["encoding"]["tooltip"]["type"] == "ordinal"
        assert dct["encoding"]["tooltip"]["field"] == "s"
        # "sort" should be removed for channels that don't support it
        assert "sort" not in dct["encoding"]["tooltip"]

    # Pass field names by keyword
    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(x="x", y="y", color="c", size="s", tooltip="s")
    )
    _check_encodings(chart)

    # pass Channel objects by keyword
    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(
            x=alt.X("x"),
            y=alt.Y("y"),
            color=alt.Color("c"),
            size=alt.Size("s"),
            tooltip=alt.Tooltip("s"),
        )
    )
    _check_encodings(chart)

    # pass Channel objects by value
    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(alt.X("x"), alt.Y("y"), alt.Color("c"), alt.Size("s"), alt.Tooltip("s"))
    )
    _check_encodings(chart)

    # override default types
    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(
            alt.X("x", type="nominal"),
            alt.Y("y", type="ordinal"),
            alt.Size("s", type="nominal"),
            alt.Tooltip("s", type="nominal"),
        )
    )
    dct = chart.to_dict()
    assert dct["encoding"]["x"]["type"] == "nominal"
    assert dct["encoding"]["y"]["type"] == "ordinal"
    assert dct["encoding"]["size"]["type"] == "nominal"
    assert "sort" not in dct["encoding"]["size"]
    assert dct["encoding"]["tooltip"]["type"] == "nominal"
    assert "sort" not in dct["encoding"]["tooltip"]


@pytest.mark.parametrize(
    ("args", "kwargs"),
    [
        getargs(detail=["value:Q", "name:N"], tooltip=["value:Q", "name:N"]),
        getargs(detail=["value", "name"], tooltip=["value", "name"]),
        getargs(alt.Detail(["value:Q", "name:N"]), alt.Tooltip(["value:Q", "name:N"])),
        getargs(alt.Detail(["value", "name"]), alt.Tooltip(["value", "name"])),
        getargs(
            [alt.Detail("value:Q"), alt.Detail("name:N")],
            [alt.Tooltip("value:Q"), alt.Tooltip("name:N")],
        ),
        getargs(
            [alt.Detail("value"), alt.Detail("name")],
            [alt.Tooltip("value"), alt.Tooltip("name")],
        ),
    ],
)
def test_multiple_encodings(args, kwargs):
    df = pd.DataFrame({"value": [1, 2, 3], "name": ["A", "B", "C"]})
    encoding_dct = [
        {"field": "value", "type": "quantitative"},
        {"field": "name", "type": "nominal"},
    ]
    chart = alt.Chart(df).mark_point().encode(*args, **kwargs)
    dct = chart.to_dict()
    assert dct["encoding"]["detail"] == encoding_dct
    assert dct["encoding"]["tooltip"] == encoding_dct


def test_chart_operations():
    data = pd.DataFrame(
        {
            "x": pd.date_range("2012", periods=10, freq="YS"),
            "y": range(10),
            "c": list("abcabcabca"),
        }
    )
    chart1 = alt.Chart(data).mark_line().encode(x="x", y="y", color="c")
    chart2 = chart1.mark_point()
    chart3 = chart1.mark_circle()
    chart4 = chart1.mark_square()

    chart = chart1 + chart2 + chart3
    assert isinstance(chart, alt.LayerChart)
    assert len(chart.layer) == 3
    chart += chart4
    assert len(chart.layer) == 4

    chart = chart1 | chart2 | chart3
    assert isinstance(chart, alt.HConcatChart)
    assert len(chart.hconcat) == 3
    chart |= chart4
    assert len(chart.hconcat) == 4

    chart = chart1 & chart2 & chart3
    assert isinstance(chart, alt.VConcatChart)
    assert len(chart.vconcat) == 3
    chart &= chart4
    assert len(chart.vconcat) == 4


def test_when() -> None:
    select = alt.selection_point(name="select", on="click")
    condition = alt.condition(select, alt.value(1), "two", empty=False)["condition"]
    condition.pop("value")
    when = alt.when(select, empty=False)
    when_constraint = alt.when(Origin="Europe")
    when_constraints = alt.when(
        Name="Name_1", Color="Green", Age=25, StartDate="2000-10-01"
    )
    expected_constraint = alt.datum.Origin == "Europe"
    expected_constraints = (
        (alt.datum.Name == "Name_1")
        & (alt.datum.Color == "Green")
        & (alt.datum.Age == 25)
        & (alt.datum.StartDate == "2000-10-01")
    )

    assert isinstance(when, alt.When)
    assert condition == when._condition
    assert isinstance(when_constraint, alt.When)
    assert when_constraint._condition["test"] == expected_constraint
    assert when_constraints._condition["test"] == expected_constraints
    with pytest.raises((NotImplementedError, TypeError), match="list"):
        alt.when([1, 2, 3])  # type: ignore
    with pytest.raises(TypeError, match="Undefined"):
        alt.when()
    with pytest.raises(TypeError, match="int"):
        alt.when(select, alt.datum.Name == "Name_1", 99, TestCon=5.901)  # type: ignore


def test_when_then() -> None:
    select = alt.selection_point(name="select", on="click")
    when = alt.when(select)
    when_then = when.then(alt.value(5))

    assert isinstance(when_then, alt.Then)
    condition = when_then.condition
    assert isinstance(condition, list)
    assert condition[-1].get("value") == 5

    with pytest.raises(TypeError, match=r"Path"):
        when.then(pathlib.Path("some"))  # type: ignore

    with pytest.raises(TypeError, match="float"):
        when_then.when(select, alt.datum.Name != "Name_2", 86.123, empty=True)  # type: ignore


def test_when_then_only(basic_chart) -> None:
    """`Then` is an acceptable encode argument."""
    select = alt.selection_point(name="select", on="click")

    basic_chart.encode(fillOpacity=alt.when(select).then(alt.value(5))).to_dict()


def test_when_then_otherwise() -> None:
    select = alt.selection_point(name="select", on="click")
    when_then = alt.when(select).then(alt.value(2, empty=False))
    when_then_otherwise = when_then.otherwise(alt.value(0))

    expected = dict(alt.condition(select, alt.value(2, empty=False), alt.value(0)))
    with pytest.raises(TypeError, match="list"):
        when_then.otherwise([1, 2, 3])  # type: ignore

    # Needed to modify to a list of conditions,
    # which isn't possible in `condition`
    single_condition = expected.pop("condition")
    expected["condition"] = [single_condition]

    assert expected == when_then_otherwise


def test_when_then_when_then_otherwise() -> None:
    """Test for [#3301](https://github.com/vega/altair/issues/3301)."""
    data = {
        "values": [
            {"a": "A", "b": 28},
            {"a": "B", "b": 55},
            {"a": "C", "b": 43},
            {"a": "D", "b": 91},
            {"a": "E", "b": 81},
            {"a": "F", "b": 53},
            {"a": "G", "b": 19},
            {"a": "H", "b": 87},
            {"a": "I", "b": 52},
        ]
    }

    select = alt.selection_point(name="select", on="click")
    highlight = alt.selection_point(name="highlight", on="pointerover")
    when_then_when_then = (
        alt.when(select)
        .then(alt.value(2, empty=False))
        .when(highlight)
        .then(alt.value(1, empty=False))
    )
    with pytest.raises(TypeError, match="set"):
        when_then_when_then.otherwise({"five", "six"})  # type: ignore

    expected_stroke = {
        "condition": [
            {"param": "select", "empty": False, "value": 2},
            {"param": "highlight", "empty": False, "value": 1},
        ],
        "value": 0,
    }
    actual_stroke = when_then_when_then.otherwise(alt.value(0))
    fill_opacity = alt.when(select).then(alt.value(1)).otherwise(alt.value(0.3))

    assert expected_stroke == actual_stroke
    chart = (
        alt.Chart(data)
        .mark_bar(fill="#4C78A8", stroke="black", cursor="pointer")
        .encode(x="a:O", y="b:Q", fillOpacity=fill_opacity, strokeWidth=actual_stroke)
        .configure_scale(bandPaddingInner=0.2)
        .add_params(select, highlight)
    )
    chart.to_dict()


def test_when_multi_channel_param(cars):
    """Adapted from [2236376458](https://github.com/vega/altair/pull/3427#issuecomment-2236376458)."""
    brush = alt.selection_interval()
    hover = alt.selection_point(on="pointerover", nearest=True, empty=False)

    chart_1 = (
        alt.Chart(cars)
        .mark_rect()
        .encode(
            x="Cylinders:N",
            y="Origin:N",
            color=alt.when(brush).then("count()").otherwise(alt.value("grey")),
            opacity=alt.when(brush).then(alt.value(1)).otherwise(alt.value(0.6)),
        )
        .add_params(brush)
    )
    chart_1.to_dict()

    color = alt.when(hover).then(alt.value("coral")).otherwise(alt.value("lightgray"))

    chart_2 = (
        alt.Chart(cars, title="Selection obscured by other points")
        .mark_circle(opacity=1)
        .encode(
            x="Horsepower:Q",
            y="Miles_per_Gallon:Q",
            color=color,
            size=alt.when(hover).then(alt.value(300)).otherwise(alt.value(30)),
        )
        .add_params(hover)
    )

    chart_3 = chart_2 | chart_2.encode(
        order=alt.when(hover).then(alt.value(1)).otherwise(alt.value(0))
    ).properties(title="Selection brought to front")

    chart_3.to_dict()


def test_when_labels_position_based_on_condition() -> None:
    """
    Test for [2144026368-1](https://github.com/vega/altair/pull/3427#issuecomment-2144026368).

    Original [labels-position-based-on-condition](https://altair-viz.github.io/user_guide/marks/text.html#labels-position-based-on-condition)
    """
    import numpy as np
    import pandas as pd

    from altair.utils.schemapi import SchemaValidationError

    rand = np.random.RandomState(42)
    df = pd.DataFrame({"xval": range(100), "yval": rand.randn(100).cumsum()})

    bind_range = alt.binding_range(min=100, max=300, name="Slider value:  ")
    param_width = alt.param(bind=bind_range)
    param_width_lt_200 = param_width < 200

    # Examples of how to write both js and python expressions
    param_color_js_expr = alt.param(expr=f"{param_width.name} < 200 ? 'red' : 'black'")
    param_color_py_expr = alt.param(
        expr=alt.expr.if_(param_width_lt_200, "red", "black")
    )
    when = (
        alt.when(param_width_lt_200.expr)
        .then(alt.value("red"))
        .otherwise(alt.value("black"))
    )

    # NOTE: If the `@overload` signatures change,
    # `mypy` will flag structural errors here
    cond = when["condition"][0]
    otherwise = when["value"]

    # TODO: Open an issue on making `OperatorMixin` generic
    # Something like this would be used as the return type for all `__dunder__` methods:
    # R = TypeVar("R", Expression, SelectionPredicateComposition)
    test = cond["test"]
    assert not isinstance(test, alt.PredicateComposition)
    param_color_py_when = alt.param(expr=alt.expr.if_(test, cond["value"], otherwise))
    lhs_param = param_color_py_expr.param
    rhs_param = param_color_py_when.param
    assert isinstance(lhs_param, alt.VariableParameter)
    assert isinstance(rhs_param, alt.VariableParameter)
    assert repr(lhs_param.expr) == repr(rhs_param.expr)

    chart = (
        alt.Chart(df)
        .mark_point()
        .encode(
            alt.X("xval").axis(titleColor=param_color_js_expr),
            alt.Y("yval").axis(titleColor=param_color_py_when),
        )
        .add_params(param_width, param_color_js_expr, param_color_py_when)
    )
    chart.to_dict()
    fail_condition = alt.condition(
        param_width < 200, alt.value("red"), alt.value("black")
    )
    with pytest.raises(SchemaValidationError, match="invalid value for `expr`"):
        alt.param(expr=fail_condition)  # type: ignore


def test_when_expressions_inside_parameters() -> None:
    """Test for [2144026368-2](https://github.com/vega/altair/pull/3427#issuecomment-2144026368)."""
    import polars as pl

    source = pl.DataFrame({"a": ["A", "B", "C"], "b": [28, -5, 10]})

    bar = (
        alt.Chart(source)
        .mark_bar()
        .encode(y="a:N", x=alt.X("b:Q").scale(domain=[-10, 35]))
    )
    when_then_otherwise = (
        alt.when(alt.datum.b >= 0).then(alt.value(10)).otherwise(alt.value(-20))
    )
    cond = when_then_otherwise["condition"][0]
    otherwise = when_then_otherwise["value"]
    expected = alt.expr.if_(alt.datum.b >= 0, 10, -20)
    test = cond["test"]
    assert not isinstance(test, alt.PredicateComposition)
    actual = alt.expr.if_(test, cond["value"], otherwise)
    assert expected == actual

    text_conditioned = bar.mark_text(
        align="left",
        baseline="middle",
        dx=alt.expr(actual),  # type: ignore[arg-type]
    ).encode(text="b")

    chart = bar + text_conditioned
    chart.to_dict()


def test_when_multiple_fields():
    # Triggering structural errors
    # https://vega.github.io/vega-lite/docs/condition.html#field
    brush = alt.selection_interval()
    select_x = alt.selection_interval(encodings=["x"])
    when = alt.when(brush)
    reveal_msg = re.compile(r"Only one field.+Shorthand 'max\(\)'", flags=re.DOTALL)
    with pytest.raises(TypeError, match=reveal_msg):
        when.then("count()").otherwise("max()")

    chain_mixed_msg = re.compile(
        r"Chained.+mixed.+conflict.+\{'field': 'field_1', 'type': 'quantitative'\}.+otherwise",
        flags=re.DOTALL,
    )
    with pytest.raises(TypeError, match=chain_mixed_msg):
        when.then({"field": "field_1", "type": "quantitative"}).when(
            select_x, field_2=99
        )

    with pytest.raises(TypeError, match=chain_mixed_msg):
        when.then("field_1:Q").when(Genre="pop")

    chained_when = when.then(alt.value(5)).when(
        alt.selection_point(fields=["b"]) | brush, empty=False, b=63812
    )

    chain_then_msg = re.compile(
        r"Chained.+mixed.+field.+min\(foo\):Q.+'aggregate': 'min', 'field': 'foo', 'type': 'quantitative'",
        flags=re.DOTALL,
    )

    with pytest.raises(TypeError, match=chain_then_msg):
        chained_when.then("min(foo):Q")

    chain_otherwise_msg = re.compile(
        r"Chained.+mixed.+field.+AggregatedFieldDef.+'this_field_here'",
        flags=re.DOTALL,
    )
    with pytest.raises(TypeError, match=chain_otherwise_msg):
        chained_when.then(alt.value(2)).otherwise(
            alt.AggregatedFieldDef(
                "argmax", field="field_9", **{"as": "this_field_here"}
            )
        )


def test_when_typing(cars) -> None:
    chart = alt.Chart(cars).mark_rect()
    predicate = alt.datum.Weight_in_lbs >= 3500
    statement = alt.value("black")
    default = alt.value("white")

    then: alt.Then[_Conditions] = alt.when(predicate).then(statement)
    otherwise: _Conditional[_Conditions] = then.otherwise(default)
    condition: Map = alt.condition(predicate, statement, default)

    # NOTE: both `condition()` and `when-then-otherwise` are allowed in these three locations
    chart.encode(
        color=condition,
        x=alt.X("Cylinders:N").axis(labelColor=condition),
        y=alt.Y("Origin:N", axis=alt.Axis(tickColor=condition)),
    ).to_dict()

    chart.encode(
        color=otherwise,
        x=alt.X("Cylinders:N").axis(labelColor=otherwise),
        y=alt.Y("Origin:N", axis=alt.Axis(tickColor=otherwise)),
    ).to_dict()

    with pytest.raises(SchemaValidationError):
        # NOTE: `when-then` is allowed as an encoding, but not as a `ConditionalAxisProperty`
        # The latter fails validation since it does not have a default `value`
        chart.encode(
            color=then,
            x=alt.X("Cylinders:N").axis(labelColor=then),  # type: ignore[call-overload]
            y=alt.Y("Origin:N", axis=alt.Axis(labelColor=then)),  # type: ignore[arg-type]
        )

    # NOTE: Passing validation then requires an `.otherwise()` **only** for the property cases
    chart.encode(
        color=then,
        x=alt.X("Cylinders:N").axis(labelColor=otherwise),
        y=alt.Y("Origin:N", axis=alt.Axis(labelColor=otherwise)),
    ).to_dict()


@pytest.mark.parametrize(
    ("channel", "then", "otherwise"),
    [
        ("color", alt.ColorValue("red"), alt.ColorValue("blue")),
        ("opacity", alt.value(0.5), alt.value(1.0)),
        ("text", alt.TextValue("foo"), alt.value("bar")),
        ("color", alt.Color("col1:N"), alt.value("blue")),
        ("opacity", "col1:N", alt.value(0.5)),
        ("text", alt.value("abc"), alt.Text("Name:N")),
        ("size", alt.value(20), "Name:N"),
        ("size", "count()", alt.value(0)),
    ],
)
@pytest.mark.parametrize(
    "when",
    [
        alt.selection_interval(),
        alt.selection_point(),
        alt.datum.Displacement > alt.value(350),
        alt.selection_point(name="select", on="click"),
        alt.selection_point(fields=["Horsepower"]),
    ],
)
@pytest.mark.parametrize("empty", [Undefined, True, False])
def test_when_condition_parity(
    cars, channel: str, when, empty: Optional[bool], then, otherwise
):
    params = [when] if isinstance(when, alt.Parameter) else ()
    kwds = {"x": "Cylinders:N", "y": "Origin:N"}

    input_condition = alt.condition(when, then, otherwise, empty=empty)
    chart_condition = (
        alt.Chart(cars)
        .mark_rect()
        .encode(**kwds, **{channel: input_condition})
        .add_params(*params)
        .to_dict()
    )

    input_when = alt.when(when, empty=empty).then(then).otherwise(otherwise)
    chart_when = (
        alt.Chart(cars)
        .mark_rect()
        .encode(**kwds, **{channel: input_when})
        .add_params(*params)
        .to_dict()
    )

    if isinstance(input_when["condition"], list):
        input_when["condition"] = input_when["condition"][0]
        assert input_condition == input_when
    else:
        assert chart_condition == chart_when


def test_when_then_interactive() -> None:
    """Copy-related regression found in https://github.com/vega/altair/pull/3394#issuecomment-2302995453."""
    source = "https://cdn.jsdelivr.net/npm/vega-datasets@v3.2.1/data/movies.json"
    predicate = (alt.datum["IMDB Rating"] == None) | (  # noqa: E711
        alt.datum["Rotten Tomatoes Rating"] == None  # noqa: E711
    )

    chart = (
        alt.Chart(source)
        .mark_point(invalid=None)
        .encode(
            x="IMDB Rating:Q",
            y="Rotten Tomatoes Rating:Q",
            color=alt.when(predicate).then(alt.value("grey")),
        )
    )
    assert chart.interactive()
    assert chart.copy()
    assert chart.to_dict()


def test_selection_to_dict():
    brush = alt.selection_interval()

    # test some value selections
    # Note: X and Y cannot have conditions
    alt.Chart("path/to/data.json").mark_point().encode(
        color=alt.condition(brush, alt.ColorValue("red"), alt.ColorValue("blue")),
        opacity=alt.condition(brush, alt.value(0.5), alt.value(1.0)),
        text=alt.condition(brush, alt.TextValue("foo"), alt.value("bar")),
    ).to_dict()

    # test some field selections
    # Note: X and Y cannot have conditions
    # Conditions cannot both be fields
    alt.Chart("path/to/data.json").mark_point().encode(
        color=alt.condition(brush, alt.Color("col1:N"), alt.value("blue")),
        opacity=alt.condition(brush, "col1:N", alt.value(0.5)),
        text=alt.condition(brush, alt.value("abc"), alt.Text("col2:N")),
        size=alt.condition(brush, alt.value(20), "col2:N"),
    ).to_dict()


def test_selection_expression():
    from altair.expr.core import Expression

    selection = alt.selection_point(fields=["value"])

    assert isinstance(selection.value, alt.SelectionExpression)
    assert selection.value.to_dict() == {"expr": f"{selection.name}.value"}

    assert isinstance(selection["value"], Expression)
    assert selection["value"].to_dict() == f"{selection.name}['value']"

    magic_attr = "__magic__"
    with pytest.raises(AttributeError):
        getattr(selection, magic_attr)


@pytest.mark.parametrize(
    "format", ["html", "json", "png", "svg", "pdf", "vega", "bogus"]
)
@pytest.mark.parametrize("engine", ["vl-convert"])
def test_save(format, engine, basic_chart):
    if format in {"pdf", "png"}:
        out = io.BytesIO()
        mode = "rb"
    else:
        out = io.StringIO()
        mode = "r"

    if format in {"svg", "png", "pdf", "vega", "bogus"} and engine == "vl-convert":
        if format == "bogus":
            with pytest.raises(ValueError) as err:  # noqa: PT011
                basic_chart.save(out, format=format, engine=engine)
            assert f"Unsupported format: '{format}'" in str(err.value)
            return
        elif find_spec("vl_convert") is None:
            with pytest.raises(ValueError) as err:  # noqa: PT011
                basic_chart.save(out, format=format, engine=engine)
            assert "vl-convert-python" in str(err.value)
            return

    basic_chart.save(out, format=format, engine=engine)
    out.seek(0)
    content = out.read()

    if format == "json":
        assert "$schema" in json.loads(content)
    elif format == "vega":
        vega_spec = json.loads(content)
        assert "$schema" in vega_spec
        # Verify it's a Vega schema, not Vega-Lite
        assert "vega/v" in vega_spec["$schema"]
        assert "vega-lite" not in vega_spec["$schema"]
        # Verify it has Vega-specific structures
        assert "marks" in vega_spec
        assert "scales" in vega_spec
    elif format == "html":
        assert isinstance(content, str)
        assert content.startswith("<!DOCTYPE html>")
    elif format == "svg":
        assert isinstance(content, str)
        assert content.startswith("<svg")
    elif format == "png":
        assert not isinstance(content, (str, bytearray, memoryview))
        assert content.startswith(b"\x89PNG")
    elif format == "pdf":
        assert not isinstance(content, (str, bytearray, memoryview))
        assert content.startswith(b"%PDF-")

    fid, filename = tempfile.mkstemp(suffix="." + format)
    os.close(fid)

    # test both string filenames and pathlib.Paths
    for fp in [filename, pathlib.Path(filename)]:
        try:
            basic_chart.save(fp, format=format, engine=engine)
            with pathlib.Path(fp).open(mode) as f:
                assert f.read()[:1000] == content[:1000]
        finally:
            pathlib.Path(fp).unlink()


@pytest.mark.parametrize("inline", [False, pytest.param(True, marks=slow)])
@skip_requires_vl_convert
def test_save_html(basic_chart, inline):
    out = io.StringIO()
    basic_chart.save(out, format="html", inline=inline)
    out.seek(0)
    content = out.read()

    assert content.startswith("<!DOCTYPE html>")

    if inline:
        assert '<script type="text/javascript">' in content
    else:
        assert 'src="https://cdn.jsdelivr.net/npm/vega@6' in content
        assert 'src="https://cdn.jsdelivr.net/npm/vega-lite@6' in content
        assert 'src="https://cdn.jsdelivr.net/npm/vega-embed@7' in content


@skip_requires_vl_convert
def test_to_url(basic_chart):
    share_url = basic_chart.to_url()

    assert share_url.startswith("https://vega.github.io/editor/#/url/vega-lite/")

    # Check fullscreen
    fullscreen_share_url = basic_chart.to_url(fullscreen=True)
    assert fullscreen_share_url.startswith(
        "https://vega.github.io/editor/#/url/vega-lite/"
    )
    assert fullscreen_share_url.endswith("/view")


def test_facet_basic():
    # wrapped facet
    chart1 = (
        alt.Chart("data.csv")
        .mark_point()
        .encode(
            x="x:Q",
            y="y:Q",
        )
        .facet("category:N", columns=2)
    )

    dct1 = chart1.to_dict()

    assert dct1["facet"] == alt.Facet("category:N").to_dict()
    assert dct1["columns"] == 2
    assert dct1["data"] == alt.UrlData("data.csv").to_dict()

    # explicit row/col facet
    chart2 = (
        alt.Chart("data.csv")
        .mark_point()
        .encode(
            x="x:Q",
            y="y:Q",
        )
        .facet(row="category1:Q", column="category2:Q")
    )

    dct2 = chart2.to_dict()

    assert dct2["facet"]["row"] == alt.Facet("category1:Q").to_dict()
    assert dct2["facet"]["column"] == alt.Facet("category2:Q").to_dict()
    assert "columns" not in dct2
    assert dct2["data"] == alt.UrlData("data.csv").to_dict()


def test_facet_parse():
    chart = (
        alt.Chart("data.csv")
        .mark_point()
        .encode(x="x:Q", y="y:Q")
        .facet(row="row:N", column="column:O")
    )
    dct = chart.to_dict()
    assert dct["data"] == {"url": "data.csv"}
    assert "data" not in dct["spec"]
    assert dct["facet"] == {
        "column": {"field": "column", "type": "ordinal"},
        "row": {"field": "row", "type": "nominal"},
    }


def test_facet_parse_data():
    data = pd.DataFrame({"x": range(5), "y": range(5), "row": list("abcab")})
    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(x="x", y="y:O")
        .facet(row="row", column="column:O")
    )
    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = chart.to_dict()
    assert "values" in dct["data"]
    assert "data" not in dct["spec"]
    assert dct["facet"] == {
        "column": {"field": "column", "type": "ordinal"},
        "row": {"field": "row", "type": "nominal"},
    }

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = chart.to_dict()
    assert "datasets" in dct
    assert "name" in dct["data"]
    assert "data" not in dct["spec"]
    assert dct["facet"] == {
        "column": {"field": "column", "type": "ordinal"},
        "row": {"field": "row", "type": "nominal"},
    }


def test_selection():
    # test instantiation of selections
    interval = alt.selection_interval(name="selec_1")
    param = interval.param
    assert isinstance(param, alt.SelectionParameter)
    select = param.select
    assert isinstance(select, alt.IntervalSelectionConfig)
    assert select.type == "interval"
    assert interval.name == "selec_1"

    single = alt.selection_point(name="selec_2")
    assert isinstance(single.param, alt.SelectionParameter)
    assert single.param.select.type == "point"
    assert single.name == "selec_2"

    multi = alt.selection_point(name="selec_3")
    assert isinstance(multi.param, alt.SelectionParameter)
    assert multi.param.select.type == "point"
    assert multi.name == "selec_3"

    # test adding to chart
    chart = alt.Chart().add_params(single)
    chart = chart.add_params(multi, interval)
    assert {x.name for x in chart.params} == {"selec_1", "selec_2", "selec_3"}

    # test logical operations
    assert isinstance(single & multi, alt.SelectionPredicateComposition)
    assert isinstance(single | multi, alt.SelectionPredicateComposition)
    assert isinstance(~single, alt.SelectionPredicateComposition)
    assert "and" in (single & multi).to_dict()
    assert "or" in (single | multi).to_dict()
    assert "not" in (~single).to_dict()

    # test that default names are deterministic and unique for different types
    sel1 = alt.selection_point()
    sel2 = alt.selection_point()
    sel3 = alt.selection_interval()
    names = {s.name for s in (sel1, sel2, sel3)}
    # With hash-based naming, identical specifications get the same name
    # sel1 and sel2 are identical selection_point() calls, so they get the same name
    # sel3 is a selection_interval(), so it gets a different name
    assert len(names) == 2
    assert sel1.name == sel2.name  # Identical specifications get same name
    assert sel1.name != sel3.name  # Different specifications get different names


def test_selection_empty_property_preservation():
    """Test that the empty property is preserved in logical operations on selections."""
    # Test basic selection with empty=False
    click = alt.selection_point("click", empty=False)
    ctrl_click = alt.selection_point(
        name="ctrl_click", on="click[event.ctrlKey]", empty=True
    )

    # Test AND operation preserves empty properties
    and_result = (click & ctrl_click).to_dict()
    expected_and = {
        "and": [
            {"param": "click", "empty": False},
            {"param": "ctrl_click", "empty": True},
        ]
    }
    assert and_result == expected_and

    # Test with both selections having empty=False
    ctrl_click_false = alt.selection_point(
        name="ctrl_click_false", on="click[event.ctrlKey]", empty=False
    )
    and_result_false = (ctrl_click_false & ctrl_click).to_dict()
    expected_and_false = {
        "and": [
            {"param": "ctrl_click_false", "empty": False},
            {"param": "ctrl_click", "empty": True},
        ]
    }
    assert and_result_false == expected_and_false

    # Test OR operation preserves empty properties
    or_result = (click | ctrl_click).to_dict()
    expected_or = {
        "or": [
            {"param": "click", "empty": False},
            {"param": "ctrl_click", "empty": True},
        ]
    }
    assert or_result == expected_or

    # Test NOT operation preserves empty property
    not_result = (~click).to_dict()
    expected_not = {"not": {"param": "click", "empty": False}}
    assert not_result == expected_not

    # Test complex nested operations
    complex_result = ((click & ctrl_click) | (~ctrl_click_false)).to_dict()
    expected_complex = {
        "or": [
            {
                "and": [
                    {"param": "click", "empty": False},
                    {"param": "ctrl_click", "empty": True},
                ]
            },
            {"not": {"param": "ctrl_click_false", "empty": False}},
        ]
    }
    assert complex_result == expected_complex

    # Test with interval selections
    interval_false = alt.selection_interval(name="interval_false", empty=False)
    interval_true = alt.selection_interval(name="interval_true", empty=True)

    interval_and = (interval_false & interval_true).to_dict()
    expected_interval_and = {
        "and": [
            {"param": "interval_false", "empty": False},
            {"param": "interval_true", "empty": True},
        ]
    }
    assert interval_and == expected_interval_and

    # Test mixed selection types
    mixed_result = (click & interval_true).to_dict()
    expected_mixed = {
        "and": [
            {"param": "click", "empty": False},
            {"param": "interval_true", "empty": True},
        ]
    }
    assert mixed_result == expected_mixed


def test_transforms():
    # aggregate transform
    agg1 = alt.AggregatedFieldDef(op="mean", field="y", **{"as": "x1"})
    agg2 = alt.AggregatedFieldDef(op="median", field="z", **{"as": "x2"})
    chart = alt.Chart().transform_aggregate([agg1], ["foo"], x2="median(z)")
    kwds = {"aggregate": [agg1, agg2], "groupby": ["foo"]}
    assert chart.transform == [alt.AggregateTransform(**kwds)]

    # bin transform
    chart = alt.Chart().transform_bin("binned", field="field", bin=True)
    kwds = {"as": "binned", "field": "field", "bin": True}
    assert chart.transform == [alt.BinTransform(**kwds)]

    # calculate transform
    chart = alt.Chart().transform_calculate("calc", "datum.a * 4")
    kwds = {"as": "calc", "calculate": "datum.a * 4"}
    assert chart.transform == [alt.CalculateTransform(**kwds)]

    # density transform
    chart = alt.Chart().transform_density("x", as_=["value", "density"])
    kwds = {"as": ["value", "density"], "density": "x"}
    assert chart.transform == [alt.DensityTransform(**kwds)]

    # extent transform
    chart = alt.Chart().transform_extent("x", "x_extent")
    assert chart.transform == [alt.ExtentTransform(extent="x", param="x_extent")]

    # filter transform
    chart = alt.Chart().transform_filter("datum.a < 4")
    assert chart.transform == [alt.FilterTransform(filter="datum.a < 4")]

    # flatten transform
    chart = alt.Chart().transform_flatten(["A", "B"], ["X", "Y"])
    kwds = {"as": ["X", "Y"], "flatten": ["A", "B"]}
    assert chart.transform == [alt.FlattenTransform(**kwds)]

    # fold transform
    chart = alt.Chart().transform_fold(["A", "B", "C"], as_=["key", "val"])
    kwds = {"as": ["key", "val"], "fold": ["A", "B", "C"]}
    assert chart.transform == [alt.FoldTransform(**kwds)]

    # impute transform
    chart = alt.Chart().transform_impute("field", "key", groupby=["x"])
    kwds = {"impute": "field", "key": "key", "groupby": ["x"]}
    assert chart.transform == [alt.ImputeTransform(**kwds)]

    # joinaggregate transform
    chart = alt.Chart().transform_joinaggregate(min="min(x)", groupby=["key"])
    kwds = {
        "joinaggregate": [
            alt.JoinAggregateFieldDef(field="x", op="min", **{"as": "min"})
        ],
        "groupby": ["key"],
    }
    assert chart.transform == [alt.JoinAggregateTransform(**kwds)]

    # loess transform
    chart = alt.Chart().transform_loess("x", "y", as_=["xx", "yy"])
    kwds = {"on": "x", "loess": "y", "as": ["xx", "yy"]}
    assert chart.transform == [alt.LoessTransform(**kwds)]

    # lookup transform (data)
    lookup_data = alt.LookupData(alt.UrlData("foo.csv"), "id", ["rate"])
    chart = alt.Chart().transform_lookup("a", from_=lookup_data, as_="a", default="b")
    kwds = {"from": lookup_data, "as": "a", "lookup": "a", "default": "b"}
    assert chart.transform == [alt.LookupTransform(**kwds)]

    # lookup transform (selection)
    lookup_selection = alt.LookupSelection(key="key", param="sel")
    chart = alt.Chart().transform_lookup(
        "a", from_=lookup_selection, as_="a", default="b"
    )
    kwds = {"from": lookup_selection, "as": "a", "lookup": "a", "default": "b"}
    assert chart.transform == [alt.LookupTransform(**kwds)]

    # pivot transform
    chart = alt.Chart().transform_pivot("x", "y")
    assert chart.transform == [alt.PivotTransform(pivot="x", value="y")]

    # quantile transform
    chart = alt.Chart().transform_quantile("x", as_=["prob", "value"])
    kwds = {"quantile": "x", "as": ["prob", "value"]}
    assert chart.transform == [alt.QuantileTransform(**kwds)]

    # regression transform
    chart = alt.Chart().transform_regression("x", "y", as_=["xx", "yy"])
    kwds = {"on": "x", "regression": "y", "as": ["xx", "yy"]}
    assert chart.transform == [alt.RegressionTransform(**kwds)]

    # sample transform
    chart = alt.Chart().transform_sample()
    assert chart.transform == [alt.SampleTransform(1000)]

    # stack transform
    chart = alt.Chart().transform_stack("stacked", "x", groupby=["y"])
    assert chart.transform == [
        alt.StackTransform(
            groupby=["y"],
            stack="x",
            offset=Undefined,
            sort=Undefined,
            **{"as": "stacked"},
        )
    ]

    # timeUnit transform
    chart = alt.Chart().transform_timeunit("foo", field="x", timeUnit="date")
    assert chart.transform == [
        alt.TimeUnitTransform(field="x", timeUnit="date", **{"as": "foo"})
    ]

    # window transform
    chart = alt.Chart().transform_window(xsum="sum(x)", ymin="min(y)", frame=[None, 0])
    window = [
        alt.WindowFieldDef(field="x", op="sum", param=Undefined, **{"as": "xsum"}),
        alt.WindowFieldDef(field="y", op="min", param=Undefined, **{"as": "ymin"}),
    ]

    # kwargs don't maintain order in Python < 3.6, so window list can
    # be reversed
    assert chart.transform in (
        [alt.WindowTransform(frame=[None, 0], window=window)],
        [alt.WindowTransform(frame=[None, 0], window=window[::-1])],
    )


def test_filter_transform_selection_predicates():
    selector1 = alt.selection_interval(name="s1")
    selector2 = alt.selection_interval(name="s2")
    base = alt.Chart("data.txt").mark_point()

    chart = base.transform_filter(selector1)
    assert chart.to_dict()["transform"] == [{"filter": {"param": "s1"}}]

    chart = base.transform_filter(~selector1)
    assert chart.to_dict()["transform"] == [{"filter": {"not": {"param": "s1"}}}]

    chart = base.transform_filter(selector1 & selector2)
    assert chart.to_dict()["transform"] == [
        {"filter": {"and": [{"param": "s1"}, {"param": "s2"}]}}
    ]

    chart = base.transform_filter(selector1 | selector2)
    assert chart.to_dict()["transform"] == [
        {"filter": {"or": [{"param": "s1"}, {"param": "s2"}]}}
    ]

    chart = base.transform_filter(selector1 | ~selector2)
    assert chart.to_dict()["transform"] == [
        {"filter": {"or": [{"param": "s1"}, {"not": {"param": "s2"}}]}}
    ]

    chart = base.transform_filter(~selector1 | ~selector2)
    assert chart.to_dict()["transform"] == [
        {"filter": {"or": [{"not": {"param": "s1"}}, {"not": {"param": "s2"}}]}}
    ]

    chart = base.transform_filter(~(selector1 & selector2))
    assert chart.to_dict()["transform"] == [
        {"filter": {"not": {"and": [{"param": "s1"}, {"param": "s2"}]}}}
    ]


def test_predicate_composition() -> None:
    columns = ["Drought", "Epidemic", "Earthquake", "Flood"]
    field_one_of = alt.FieldOneOfPredicate(field="Entity", oneOf=columns)
    field_range = alt.FieldRangePredicate(field="Year", range=[1900, 2000])
    fields_and = field_one_of & field_range
    expected_and = {
        "and": [
            {"field": "Entity", "oneOf": columns},
            {"field": "Year", "range": [1900, 2000]},
        ]
    }
    assert isinstance(fields_and, alt.PredicateComposition)
    actual_and = fields_and.to_dict()

    # NOTE: Extra guarantee that something hasn't overloaded `__eq__` or `to_dict`
    assert isinstance(actual_and, Mapping)
    assert isinstance(actual_and == expected_and, bool)

    assert actual_and == expected_and

    actual_when = (
        alt.when(field_one_of, field_range).then(alt.value(0)).otherwise(alt.value(1))
    )
    expected_when = {"condition": [{"test": fields_and, "value": 0}], "value": 1}
    assert actual_when == expected_when

    field_range = alt.FieldRangePredicate(field="year", range=[1950, 1960])
    field_range_not = ~field_range
    expected_not = {"not": {"field": "year", "range": [1950, 1960]}}
    assert isinstance(field_range_not, alt.PredicateComposition)
    actual_not = field_range_not.to_dict()
    assert actual_not == expected_not

    expected_or = alt.LogicalOrPredicate(
        **{"or": [field_range, field_one_of]}
    ).to_dict()
    actual_or = (field_range | field_one_of).to_dict()
    assert actual_or == expected_or

    param_pred = alt.ParameterPredicate(param="dummy_1", empty=True)
    field_eq = alt.FieldEqualPredicate(equal=999, field="measure")
    field_gt = alt.FieldGTPredicate(gt=4, field="measure 2")
    expected_multi = alt.LogicalOrPredicate(
        **{
            "or": [
                alt.LogicalNotPredicate(**{"not": param_pred}),
                alt.LogicalAndPredicate(**{"and": [field_eq, field_gt]}),
            ]
        }
    ).to_dict()
    actual_multi = (~param_pred | (field_eq & field_gt)).to_dict()
    assert actual_multi == expected_multi


def test_filter_transform_predicates(basic_chart) -> None:
    lhs, rhs = alt.datum["b"] >= 30, alt.datum["b"] < 60
    expected = [{"filter": lhs & rhs}]
    actual = basic_chart.transform_filter(lhs, rhs).to_dict()["transform"]
    assert actual == expected


def test_filter_transform_constraints(basic_chart) -> None:
    lhs, rhs = alt.datum["a"] == "A", alt.datum["b"] == 30
    expected = [{"filter": lhs & rhs}]
    actual = basic_chart.transform_filter(a="A", b=30).to_dict()["transform"]
    assert actual == expected


def test_filter_transform_predicates_constraints(basic_chart) -> None:
    from functools import reduce
    from operator import and_

    predicates = (
        alt.datum["a"] != "A",
        alt.datum["a"] != "B",
        alt.datum["a"] != "C",
        alt.datum["b"] > 1,
        alt.datum["b"] < 99,
    )
    constraints = {"b": 30, "a": "D"}
    pred_constraints = *predicates, alt.datum["b"] == 30, alt.datum["a"] != "D"
    expected = [{"filter": reduce(and_, pred_constraints)}]
    actual = basic_chart.transform_filter(*predicates, **constraints).to_dict()[
        "transform"
    ]
    assert actual == expected


def test_filter_transform_errors(basic_chart) -> None:
    NO_ARGS = r"At least one.+Undefined"
    FILTER_KWARGS = r"ambiguous"

    depr_filter = {"field": "year", "oneOf": [1955, 2000]}
    expected = [{"filter": depr_filter}]

    with pytest.raises(TypeError, match=NO_ARGS):
        basic_chart.transform_filter()
    with pytest.raises(TypeError, match=NO_ARGS):
        basic_chart.transform_filter(empty=True)
    with pytest.raises(TypeError, match=NO_ARGS):
        basic_chart.transform_filter(empty=False)

    with pytest.warns(alt.AltairDeprecationWarning, match=FILTER_KWARGS):
        basic_chart.transform_filter(filter=depr_filter)

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=alt.AltairDeprecationWarning)
        actual = basic_chart.transform_filter(filter=depr_filter).to_dict()["transform"]

    assert actual == expected


def test_resolve_methods():
    chart = alt.LayerChart().resolve_axis(x="shared", y="independent")
    assert chart.resolve == alt.Resolve(
        axis=alt.AxisResolveMap(x="shared", y="independent")
    )

    chart = alt.LayerChart().resolve_legend(color="shared", fill="independent")
    assert chart.resolve == alt.Resolve(
        legend=alt.LegendResolveMap(color="shared", fill="independent")
    )

    chart = alt.LayerChart().resolve_scale(x="shared", y="independent")
    assert chart.resolve == alt.Resolve(
        scale=alt.ScaleResolveMap(x="shared", y="independent")
    )


def test_layer_encodings():
    chart = alt.LayerChart().encode(x="column:Q")
    assert chart.encoding.x == alt.X(shorthand="column:Q")


def test_add_selection():
    selections = [
        alt.selection_interval(),
        alt.selection_point(),
        alt.selection_point(),
    ]
    chart = (
        alt.Chart()
        .mark_point()
        .add_params(selections[0])
        .add_params(selections[1], selections[2])
    )
    # The second and third selections are identical (same hash-based name),
    # so only the first two unique selections should be added
    expected = [selections[0].param, selections[1].param]
    assert chart.params == expected


def test_repeat_add_selections():
    base = alt.Chart("data.csv").mark_point()
    selection = alt.selection_point()
    alt.Chart._counter = 0
    chart1 = base.add_params(selection).repeat(list("ABC"))
    alt.Chart._counter = 0
    chart2 = base.repeat(list("ABC")).add_params(selection)
    assert chart1.to_dict() == chart2.to_dict()


def test_facet_add_selections():
    base = alt.Chart("data.csv").mark_point()
    selection = alt.selection_point()
    alt.Chart._counter = 0
    chart1 = base.add_params(selection).facet("val:Q")
    alt.Chart._counter = 0
    chart2 = base.facet("val:Q").add_params(selection)
    assert chart1.to_dict() == chart2.to_dict()


def test_layer_add_selection():
    base = alt.Chart("data.csv").mark_point()
    selection = alt.selection_point()
    alt.Chart._counter = 0
    chart1 = alt.layer(base.add_params(selection), base)
    alt.Chart._counter = 0
    chart2 = alt.layer(base, base).add_params(selection)
    assert chart1.to_dict() == chart2.to_dict()


@pytest.mark.parametrize("charttype", [alt.concat, alt.hconcat, alt.vconcat])
def test_compound_add_selections(charttype):
    base = alt.Chart("data.csv").mark_point()
    selection = alt.selection_point()
    alt.Chart._counter = 0
    chart1 = charttype(base.add_params(selection), base.add_params(selection))
    alt.Chart._counter = 0
    chart2 = charttype(base, base).add_params(selection)
    assert chart1.to_dict() == chart2.to_dict()


def test_selection_property():
    sel = alt.selection_interval()
    chart = alt.Chart("data.csv").mark_point().properties(selection=sel)

    assert list(chart["selection"].keys()) == [sel.name]


def test_LookupData():
    df = nw.from_native(pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]}))
    # Data type hints won't match with what TopLevelUnitSpec expects
    # as there is some data processing happening when converting to a VL spec
    lookup = alt.LookupData(data=df, key="x")  # pyright: ignore[reportArgumentType]

    dct = lookup.to_dict()
    assert dct["key"] == "x"
    assert dct["data"] == {
        "values": [{"x": 1, "y": 4}, {"x": 2, "y": 5}, {"x": 3, "y": 6}]
    }


def test_themes():
    from altair import theme

    chart = alt.Chart("foo.txt").mark_point()

    with theme.enable("default"):
        assert chart.to_dict()["config"] == {
            "view": {"continuousWidth": 300, "continuousHeight": 300}
        }

    with theme.enable("opaque"):
        assert chart.to_dict()["config"] == {
            "background": "white",
            "view": {"continuousWidth": 300, "continuousHeight": 300},
        }

    with theme.enable("none"):
        assert "config" not in chart.to_dict()


def test_chart_from_dict():
    base = alt.Chart("data.csv").mark_point().encode(x="x:Q", y="y:Q")

    charts = [
        base,
        base + base,
        base | base,
        base & base,
        base.facet("c:N"),
        (base + base).facet(row="c:N", data="data.csv"),
        base.repeat(["c", "d"]),
        (base + base).repeat(row=["c", "d"]),
    ]

    for chart in charts:
        chart_out = alt.Chart.from_dict(chart.to_dict())
        assert type(chart_out) is type(chart)

    # test that an invalid spec leads to a schema validation error
    with pytest.raises(jsonschema.ValidationError):
        alt.Chart.from_dict({"invalid": "spec"})


def test_consolidate_datasets(basic_chart):
    subchart1 = basic_chart
    subchart2 = basic_chart.copy()
    subchart2.data = basic_chart.data.copy()
    chart = subchart1 | subchart2

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct_consolidated = chart.to_dict()

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct_standard = chart.to_dict()

    assert "datasets" in dct_consolidated
    assert "datasets" not in dct_standard

    datasets = dct_consolidated["datasets"]

    # two dataset copies should be recognized as duplicates
    assert len(datasets) == 1

    # make sure data matches original & names are correct
    name, data = datasets.popitem()

    for spec in dct_standard["hconcat"]:
        assert spec["data"]["values"] == data

    for spec in dct_consolidated["hconcat"]:
        assert spec["data"] == {"name": name}


def test_consolidate_InlineData():
    data = alt.InlineData(
        values=[{"a": 1, "b": 1}, {"a": 2, "b": 2}], format={"type": "csv"}
    )
    chart = alt.Chart(data).mark_point()

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = chart.to_dict()
    assert dct["data"]["format"] == data.format
    assert dct["data"]["values"] == data.values

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = chart.to_dict()
    assert dct["data"]["format"] == data.format
    assert next(iter(dct["datasets"].values())) == data.values

    data = alt.InlineData(values=[], name="runtime_data")
    chart = alt.Chart(data).mark_point()

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = chart.to_dict()
    assert dct["data"] == data.to_dict()

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = chart.to_dict()
    assert dct["data"] == data.to_dict()


def test_repeat():
    # wrapped repeat
    chart1 = (
        alt.Chart("data.csv")
        .mark_point()
        .encode(
            x=alt.X(alt.repeat(), type="quantitative"),
            y="y:Q",
        )
        .repeat(["A", "B", "C", "D"], columns=2)
    )

    dct1 = chart1.to_dict()

    assert dct1["repeat"] == ["A", "B", "C", "D"]
    assert dct1["columns"] == 2
    assert dct1["spec"]["encoding"]["x"]["field"] == {"repeat": "repeat"}

    # explicit row/col repeat
    chart2 = (
        alt.Chart("data.csv")
        .mark_point()
        .encode(
            x=alt.X(alt.repeat("row"), type="quantitative"),
            y=alt.Y(alt.repeat("column"), type="quantitative"),
        )
        .repeat(row=["A", "B", "C"], column=["C", "B", "A"])
    )

    dct2 = chart2.to_dict()

    assert dct2["repeat"] == {"row": ["A", "B", "C"], "column": ["C", "B", "A"]}
    assert "columns" not in dct2
    assert dct2["spec"]["encoding"]["x"]["field"] == {"repeat": "row"}
    assert dct2["spec"]["encoding"]["y"]["field"] == {"repeat": "column"}


def test_data_property():
    data = pd.DataFrame({"x": [1, 2, 3], "y": list("ABC")})
    chart1 = alt.Chart(data).mark_point()
    chart2 = alt.Chart().mark_point().properties(data=data)

    assert chart1.to_dict() == chart2.to_dict()


@pytest.mark.parametrize("method", ["layer", "hconcat", "vconcat", "concat"])
@pytest.mark.parametrize(
    "data", ["data.json", pd.DataFrame({"x": range(3), "y": list("abc")})]
)
def test_subcharts_with_same_data(method, data):
    func = getattr(alt, method)

    point = alt.Chart(data).mark_point().encode(x="x:Q", y="y:Q")
    line = point.mark_line()
    text = point.mark_text()

    chart1 = func(point, line, text)
    assert chart1.data is not Undefined
    assert all(c.data is Undefined for c in getattr(chart1, method))

    if method != "concat":
        op = OP_DICT[method]
        chart2 = op(op(point, line), text)
        assert chart2.data is not Undefined
        assert all(c.data is Undefined for c in getattr(chart2, method))


@pytest.mark.parametrize("method", ["layer", "hconcat", "vconcat", "concat"])
@pytest.mark.parametrize(
    "data", ["data.json", pd.DataFrame({"x": range(3), "y": list("abc")})]
)
def test_subcharts_different_data(method, data):
    func = getattr(alt, method)

    point = alt.Chart(data).mark_point().encode(x="x:Q", y="y:Q")
    otherdata = alt.Chart("data.csv").mark_point().encode(x="x:Q", y="y:Q")
    nodata = alt.Chart().mark_point().encode(x="x:Q", y="y:Q")

    chart1 = func(point, otherdata)
    assert chart1.data is Undefined
    assert getattr(chart1, method)[0].data is data

    chart2 = func(point, nodata)
    assert chart2.data is Undefined
    assert getattr(chart2, method)[0].data is data


def test_layer_facet(basic_chart):
    chart = (basic_chart + basic_chart).facet(row="row:Q")
    assert chart.data is not Undefined
    assert chart.spec.data is Undefined
    for layer in chart.spec.layer:
        assert layer.data is Undefined

    dct = chart.to_dict()
    assert "data" in dct


def test_layer_errors():
    toplevel_chart = alt.Chart("data.txt").mark_point().configure_legend(columns=2)

    facet_chart1 = alt.Chart("data.txt").mark_point().encode(facet="row:Q")

    facet_chart2 = alt.Chart("data.txt").mark_point().facet("row:Q")

    repeat_chart = alt.Chart("data.txt").mark_point().repeat(["A", "B", "C"])

    simple_chart = alt.Chart("data.txt").mark_point()

    with pytest.raises(TypeError, match=r".config. attribute cannot.+LayerChart"):
        toplevel_chart + simple_chart

    with pytest.raises(TypeError, match=r"Concat.+cannot.+layered.+before concat"):
        alt.hconcat(simple_chart) + simple_chart

    with pytest.raises(TypeError, match=r"Repeat.+cannot.+layered.+before repeat"):
        repeat_chart + simple_chart

    with pytest.raises(TypeError, match=r"Facet.+.+cannot.+layered.+before facet"):
        facet_chart1 + simple_chart

    with pytest.raises(TypeError, match=r"Facet.+.+cannot.+layered.+before facet"):
        alt.layer(simple_chart) + facet_chart2


@pytest.mark.parametrize(
    "chart_type",
    ["layer", "hconcat", "vconcat", "concat", "facet", "facet_encoding", "repeat"],
)
def test_resolve(chart_type):
    chart = _make_chart_type(chart_type)
    chart = (
        chart.resolve_scale(
            x="independent",
        )
        .resolve_legend(color="independent")
        .resolve_axis(y="independent")
    )
    dct = chart.to_dict()
    assert dct["resolve"] == {
        "scale": {"x": "independent"},
        "legend": {"color": "independent"},
        "axis": {"y": "independent"},
    }


# TODO: test vconcat, hconcat, concat, facet_encoding when schema allows them.
# This is blocked by https://github.com/vega/vega-lite/issues/5261
@pytest.mark.parametrize("chart_type", ["chart", "layer"])
@pytest.mark.parametrize("facet_arg", [None, "facet", "row", "column"])
def test_facet(chart_type, facet_arg):
    chart = _make_chart_type(chart_type)
    if facet_arg is None:
        chart = chart.facet("color:N", columns=2)
    else:
        chart = chart.facet(**{facet_arg: "color:N", "columns": 2})
    dct = chart.to_dict()

    assert "spec" in dct
    assert dct["columns"] == 2
    expected = {"field": "color", "type": "nominal"}
    if facet_arg is None or facet_arg == "facet":
        assert dct["facet"] == expected
    else:
        assert dct["facet"][facet_arg] == expected


def test_sequence():
    data = alt.sequence(100)
    assert data.to_dict() == {"sequence": {"start": 0, "stop": 100}}

    data = alt.sequence(5, 10)
    assert data.to_dict() == {"sequence": {"start": 5, "stop": 10}}

    data = alt.sequence(0, 1, 0.1, as_="x")
    assert data.to_dict() == {
        "sequence": {"start": 0, "stop": 1, "step": 0.1, "as": "x"}
    }


def test_graticule():
    data = alt.graticule()
    assert data.to_dict() == {"graticule": True}

    data = alt.graticule(step=[15, 15])
    assert data.to_dict() == {"graticule": {"step": [15, 15]}}


def test_sphere():
    data = alt.sphere()
    assert data.to_dict() == {"sphere": True}


def test_validate_dataset():
    d = {"data": {"values": [{}]}, "mark": {"type": "point"}}

    chart = alt.Chart.from_dict(d)
    jsn = chart.to_json()

    assert jsn


def test_polars_with_pandas_nor_pyarrow(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delitem(sys.modules, "pandas")
    monkeypatch.delitem(sys.modules, "numpy")
    monkeypatch.delitem(sys.modules, "pyarrow", raising=False)

    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    _ = alt.Chart(df).mark_line().encode(x="a", y="b").to_json()
    # Check pandas and PyArrow weren't imported anywhere along the way,
    # confirming that the plot above would work without pandas no PyArrow
    # installed.
    assert "pandas" not in sys.modules
    assert "pyarrow" not in sys.modules
    assert "numpy" not in sys.modules


def test_polars_date_32():
    df = pl.DataFrame(
        {"a": [1, 2, 3], "b": [date(2020, 1, 1), date(2020, 1, 2), date(2020, 1, 3)]}
    )
    result = alt.Chart(df).mark_line().encode(x="a", y="b").to_dict()
    assert next(iter(result["datasets"].values())) == [
        {"a": 1, "b": "2020-01-01T00:00:00"},
        {"a": 2, "b": "2020-01-02T00:00:00"},
        {"a": 3, "b": "2020-01-03T00:00:00"},
    ]


@skip_requires_pyarrow(requires_tzdata=True)
@skip_requires_duckdb
def test_interchange_with_date_32():
    # Test that objects which Narwhals only supports at the interchange
    # level can be plotted when they contain date32 columns.
    import duckdb

    df = pl.DataFrame(  # noqa: F841
        {"a": [1, 2, 3], "b": [date(2020, 1, 1), date(2020, 1, 2), date(2020, 1, 3)]}
    )
    rel = duckdb.sql("select * from df")
    result = alt.Chart(rel).mark_line().encode(x="a", y="b").to_dict()
    assert next(iter(result["datasets"].values())) == [
        {"a": 1, "b": "2020-01-01T00:00:00"},
        {"a": 2, "b": "2020-01-02T00:00:00"},
        {"a": 3, "b": "2020-01-03T00:00:00"},
    ]


@skip_requires_pyarrow(requires_tzdata=True)
@skip_requires_duckdb
def test_interchange_with_vegafusion(monkeypatch: pytest.MonkeyPatch):
    # Test that objects which Narwhals only supports at the interchange
    # level don't get converted to PyArrow unnecessarily when plotted
    # with the vegafusion transformer.
    # TODO: this test can be drastically simplified when some level of
    # DuckDB support in VegaFusion, as it can then just be `alt.Chart(rel_df)`
    # without DuckDBWithInterchangeSupport.
    import duckdb

    df = pl.DataFrame(  # noqa: F841
        {
            "a": [1, 2, 3],
            "b": [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)],
        }
    )
    rel = duckdb.sql("select * from df")

    class DuckDBWithInterchangeSupport:
        """
        DuckDB doesn't (yet?) support the interchange protocol.

        So, we create duckdb wrapper which defers to PyArrow's
        implementation of the protocol.
        """

        def __init__(self, rel: duckdb.DuckDBPyRelation) -> None:
            self._rel = rel

        def __dataframe__(self, allow_copy: bool = True) -> object:
            return self._rel.to_arrow_table().__dataframe__()

    rel_df = DuckDBWithInterchangeSupport(rel)
    # "poison" `arrow_table_from_dfi_dataframe` to check that it does not get called
    # if we use the vegafusion transformer
    monkeypatch.setattr(
        "altair.utils.data.arrow_table_from_dfi_dataframe", lambda x: 1 / 0
    )

    # Narwhals doesn't fully support our custom DuckDBWithInterchangeSupport,
    # so we need to overwrite `to_native`
    def to_native(df, strict):
        if isinstance(df, nw.DataFrame):
            return rel_df
        return df

    monkeypatch.setattr("narwhals.stable.v1.to_native", to_native)

    with alt.data_transformers.enable("vegafusion"):
        result = (
            alt.Chart(rel_df).mark_line().encode(x="a", y="b").to_dict(format="vega")
        )
    assert next(iter(result["data"]))["values"] == [
        {"a": 1, "b": "2020-01-01T00:00:00.000"},
        {"a": 2, "b": "2020-01-02T00:00:00.000"},
        {"a": 3, "b": "2020-01-03T00:00:00.000"},
    ]


def test_binding() -> None:
    @use_signature_func(alt.Binding)
    def old_binding(input: Any, **kwargs: Any) -> alt.Binding:
        """A generic binding."""
        return alt.Binding(input=input, **kwargs)

    # NOTE: `mypy` doesn't complain, but `pyright` does
    old = old_binding(input="search", placeholder="Country", name="Search")  # pyright: ignore[reportCallIssue]
    old_positional = old_binding("search", placeholder="Country", name="Search")

    new = alt.binding(input="search", placeholder="Country", name="Search")
    new_positional = alt.binding("search", placeholder="Country", name="Search")

    assert (
        old.to_dict()
        == old_positional.to_dict()
        == new.to_dict()
        == new_positional.to_dict()
    )
    assert all(
        isinstance(x, alt.Binding) for x in (old, old_positional, new, new_positional)
    )

    MISSING_INPUT = r"missing 1 required positional argument: 'input"

    # NOTE: `mypy` doesn't complain, but `pyright` does (Again)
    with pytest.raises(TypeError, match=MISSING_INPUT):
        old_binding(placeholder="Country", name="Search")  # pyright: ignore[reportCallIssue]

    # NOTE: Both type checkers can detect the issue on the new signature
    with pytest.raises(TypeError, match=MISSING_INPUT):
        alt.binding(placeholder="Country", name="Search")  # type: ignore[call-arg]
