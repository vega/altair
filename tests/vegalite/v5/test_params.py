"""Tests for variable parameters and selection parameters."""

import re
import warnings

import pandas as pd
import pytest

import altair.vegalite.v5 as alt
from altair.utils.deprecation import AltairDeprecationWarning


def test_variable_param():
    data = pd.DataFrame([{"a": "A", "b": 28}])

    rad_slider = alt.binding_range(min=0, max=20, step=1)
    rad_var = alt.param(bind=rad_slider, value=0, name="paramName")

    c = (
        alt.Chart(data)
        .mark_bar(cornerRadius=rad_var)
        .encode(
            x="a:N",
            y="b:Q",
        )
        .add_params(rad_var)
    )

    dct = c.to_dict()

    mark_dict = {"type": "bar", "cornerRadius": {"expr": "paramName"}}
    param_list = [
        {
            "name": "paramName",
            "bind": {"input": "range", "max": 20, "min": 0, "step": 1},
            "value": 0,
        }
    ]

    assert dct["mark"] == mark_dict
    assert dct["params"] == param_list


def test_param_expr():
    height_var = alt.param(name="height")
    inner_var = height_var / 2
    tick_var = (3 * height_var) / 4

    height_str = height_var._to_expr()
    inner_str = inner_var._to_expr()
    tick_str = tick_var._to_expr()

    assert height_str == "height"
    assert inner_str == "(height / 2)"
    assert tick_str == "((3 * height) / 4)"

    data = pd.DataFrame({"r1": [310, 0], "r2": [270, 0], "r3": [125, 225]})

    c1 = alt.Chart(data).mark_bar(size=height_var).encode(x="r1")

    c2 = alt.Chart(data).mark_bar(size=inner_var).encode(x="r2")

    c3 = alt.Chart(data).mark_tick(size=tick_var).encode(x="r3")

    c = (c1 + c2 + c3).add_params(height_var)

    dct = c.to_dict()
    expr_set = {d["mark"]["size"]["expr"] for d in dct["layer"]}

    assert "height" in expr_set
    assert "(height / 2)" in expr_set
    assert "((3 * height) / 4)" in expr_set


def test_selection_deprecation():
    # We use the `warnings.catch_warnings` context so pytest will also report deprecation warnings
    with warnings.catch_warnings():
        warnings.simplefilter("error")

        # new syntax
        alt.selection_point()
        alt.selection_interval()

        # this v4 syntax is deprecated
        with pytest.warns(AltairDeprecationWarning):
            alt.selection_single()
        with pytest.warns(AltairDeprecationWarning):
            alt.selection_multi()

        # new syntax
        brush = alt.selection_interval()
        c = alt.Chart().mark_point()
        c.add_params(brush)

        # this v4 syntax is deprecated
        brush = alt.selection_interval()
        c = alt.Chart().mark_point()
        with pytest.warns(AltairDeprecationWarning):
            c.add_selection(brush)


def test_parameter_naming():
    # test explicit naming
    prm = alt.param(name="some_name")
    assert prm.param.name == "some_name"

    # test automatic naming which has the form such as param_5
    prm0, prm1, prm2 = (alt.param() for _ in range(3))

    res = re.match(r"param_([0-9]+)", prm0.param.name)

    assert res

    num = int(res[1])
    assert prm1.param.name == f"param_{num + 1}"
    assert prm2.param.name == f"param_{num + 2}"


def test_selection_expression():
    from altair.expr.core import Expression

    data = pd.DataFrame([{"a": "A", "b": 28}])

    sel = alt.selection_point(fields=["b"])
    se = sel.b | 300

    assert isinstance(se, alt.SelectionExpression)
    assert isinstance(se.expr, Expression)

    c = (
        alt.Chart(data)
        .mark_point()
        .encode(
            x="a:N",
            y="b:Q",
            size=alt.value(se),
        )
        .add_params(sel)
    )

    dct = c.to_dict()
    expr_str = str(se.expr)

    assert dct["encoding"]["size"]["value"]["expr"] == expr_str


def test_selection_condition():
    sel = alt.selection_point(empty=False)

    c = (
        alt.Chart()
        .mark_point()
        .encode(size=alt.condition(sel, alt.value(100), alt.value(10)))
        .add_params(sel)
    )

    dct = c.to_dict()

    param_name = sel.param.name

    cond = dct["encoding"]["size"]["condition"]

    assert cond["value"] == 100
    assert cond["param"] == param_name

    # The else condition
    assert dct["encoding"]["size"]["value"] == 10


def test_selection_interval_value_typing() -> None:
    """Ensure each encoding restricts types independently."""
    import datetime as dt

    w_date = dt.date(2005, 1, 1), dt.date(2009, 1, 1)
    w_float = (0, 999)
    w_date_datetime = dt.date(2005, 1, 1), alt.DateTime(year=2009)
    w_str = ["0", "500"]

    a = alt.selection_interval(encodings=["x"], value={"x": w_date}).to_dict()
    b = alt.selection_interval(encodings=["y"], value={"y": w_float}).to_dict()
    c = alt.selection_interval(encodings=["x"], value={"x": w_date_datetime}).to_dict()
    d = alt.selection_interval(encodings=["text"], value={"text": w_str}).to_dict()

    a_b = alt.selection_interval(
        encodings=["x", "y"], value={"x": w_date, "y": w_float}
    ).to_dict()
    a_c = alt.selection_interval(
        encodings=["x", "y"], value={"x": w_date, "y": w_date_datetime}
    ).to_dict()
    b_c_d = alt.selection_interval(
        encodings=["x", "y", "text"],
        value={"x": w_date_datetime, "y": w_float, "text": w_str},
    ).to_dict()

    assert a
    assert b
    assert c
    assert d
    assert a_b
    assert a_c
    assert b_c_d


def test_creation_views_params_layered_repeat_chart():
    import altair as alt
    from vega_datasets import data

    source = alt.UrlData(data.flights_2k.url, format={"parse": {"date": "date"}})

    brush = alt.selection_interval(encodings=["x"])

    # Define the base chart, with the common parts of the
    # background and highlights
    base = (
        alt.Chart(width=160, height=130)
        .mark_bar()
        .encode(x=alt.X(alt.repeat("column")).bin(maxbins=20), y="count()")
    )

    # gray background with selection
    background = base.encode(color=alt.value("#ddd")).add_params(brush)

    # blue highlights on the transformed data
    highlight = base.transform_filter(brush)

    # layer the two charts & repeat
    c = (
        alt.layer(background, highlight, data=source)
        .transform_calculate("time", "hours(datum.date)")
        .repeat(column=["distance", "delay", "time"])
    )

    dct = c.to_dict()
    assert "child__column_distance_view_" in dct["params"][0]["views"][0]
