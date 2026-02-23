"""Tests for variable parameters and selection parameters."""

import re
import warnings

import pandas as pd
import pytest

import altair.vegalite.v6 as alt
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

    # test automatic naming which now uses hash-based naming
    prm0, prm1, prm2 = (alt.param() for _ in range(3))

    # Check that all parameters have hash-based names (16 character hex)
    res = re.match(r"param_([0-9a-f]{16})", prm0.param.name)
    assert res, f"Expected hash-based name, got: {prm0.param.name}"

    # With hash-based naming, identical specifications get the same name
    assert prm0.param.name == prm1.param.name == prm2.param.name, (
        "Identical parameters should have same hash-based name"
    )


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
    from altair.datasets import data

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


def test_parameter_deduplication():
    """Test that hash-based parameters are deduplicated to avoid duplicate signal names."""
    # Test with hash-based naming - these should be deduplicated
    param1 = alt.param()  # Will get hash-based name
    param2 = alt.param()  # Will get same hash-based name

    chart = alt.Chart().mark_point().add_params(param1, param2)

    # Check that only one parameter was added
    assert len(chart.params) == 1
    assert param1.name == param2.name  # Should have same hash-based name
    assert chart.params[0].name == param1.name

    # Test that the spec doesn't have duplicate parameter names
    spec = chart.to_dict()
    param_names = [p["name"] for p in spec["params"]]
    assert len(param_names) == len(set(param_names)), (
        "Duplicate parameter names found in spec"
    )


def test_explicitly_named_parameters_error():
    """Test that explicitly named parameters with duplicate names raise an error."""
    # Create two parameters with explicit names - this should raise an error
    param1 = alt.param(name="my_param_1")
    param2 = alt.param(name="my_param_1")

    # Create a chart and add both parameters - should raise an error
    with pytest.raises(
        ValueError, match="Duplicate explicit parameter name: my_param_1"
    ):
        alt.Chart().mark_point().add_params(param1, param2)


def test_identical_hash_based_parameters_deduplication():
    """Test that identical parameters with hash-based names are deduplicated."""
    from altair.datasets import data

    cars = data.cars.url
    param_opacity = alt.param(value=1)
    param_size = alt.param(value=1)

    # Create chart with same parameter added twice
    chart = (
        alt.Chart(cars)
        .mark_circle(opacity=param_opacity, size=param_size)
        .encode(x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin:N")
        .add_params(param_opacity, param_size)
    )

    # Check that only one parameter was added
    assert len(chart.params) == 1

    # Get the spec and verify it has only one parameter
    spec = chart.to_dict()
    assert len(spec["params"]) == 1

    # Verify the parameter name is hash-based
    param_name = spec["params"][0]["name"]
    assert param_name.startswith("param_")
    assert len(param_name) == 22  # "param_" + 16 hex chars

    # Verify both opacity and size reference the same parameter
    assert spec["mark"]["opacity"]["expr"] == param_name
    assert spec["mark"]["size"]["expr"] == param_name


def test_interactive_name_respected():
    import altair as alt
    from altair.datasets import data

    cars = data.cars.url

    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(x="Horsepower:Q", y="Miles_per_Gallon:Q")
        .interactive(name="MY_CHART")
    )

    # Suppress warning since this deduplication is intentional (same chart concatenated)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        spec = (chart & chart).to_dict()
    # There should be a single parameter with the name 'MY_CHART'
    param_names = [p["name"] for p in spec["params"]]
    assert param_names == ["MY_CHART"], f"Expected ['MY_CHART'], got {param_names}"

    # Check that the parameter has the correct view IDs
    # The view IDs should be deterministic and consistent across OS/chart types
    param = spec["params"][0]
    assert "views" in param, "Parameter should have 'views' field"
    view_ids = param["views"]
    assert len(view_ids) == 2, f"Expected 2 view IDs, got {len(view_ids)}"

    # The view IDs should follow the pattern: view_<hash>_<position>
    # where <hash> is the same for both charts (they're identical)
    # and <position> is 0 and 1 for the two concatenated charts
    assert view_ids[0].endswith("_0"), (
        f"First view ID should end with '_0', got {view_ids[0]}"
    )
    assert view_ids[1].endswith("_1"), (
        f"Second view ID should end with '_1', got {view_ids[1]}"
    )

    # Both view IDs should have the same base hash name
    base_name_0 = view_ids[0].rsplit("_", 1)[0]
    base_name_1 = view_ids[1].rsplit("_", 1)[0]
    assert base_name_0 == base_name_1, (
        f"View IDs should have same base name: {base_name_0} vs {base_name_1}"
    )

    # The base name should start with 'view_' and contain a hex hash
    assert base_name_0.startswith("view_"), (
        f"Base name should start with 'view_', got {base_name_0}"
    )
    hash_part = base_name_0[5:]  # Remove 'view_' prefix
    assert len(hash_part) == 16, (
        f"Hash part should be 16 characters, got {len(hash_part)}: {hash_part}"
    )
    assert all(c in "0123456789abcdef" for c in hash_part), (
        f"Hash part should be hex, got {hash_part}"
    )

    # For this specific chart configuration, we expect a consistent hash
    # This ensures the hash is deterministic across different runs/OS
    expected_base_name = "view_6e7cfb454e831ee6"
    assert base_name_0 == expected_base_name, (
        f"Expected base name {expected_base_name}, got {base_name_0}"
    )


def test_concat_facet_enumeration():
    df = pd.DataFrame(
        {
            "x": [1, 2, 3, 4],
            "y": [1, 2, 3, 4],
            "z": [0, 0, 1, 1],
        }
    )
    c = alt.Chart(df).mark_line().encode(x="x", y="y").facet("z")
    # Unique names to since this is not related to parameter deduplication
    p1 = alt.selection_point(name="p1")
    p2 = alt.selection_point(name="p2")
    p3 = alt.selection_point(name="p3")
    concat_facet = c.add_params(p1) & c.add_params(p2) & c.add_params(p3)

    # Test that concatenation of faceted charts result in a unique name for each chart.
    # https://github.com/vega/altair/issues/3954
    assert concat_facet.vconcat[0].spec.name != concat_facet.vconcat[1].spec.name
    assert concat_facet.vconcat[0].spec.name != concat_facet.vconcat[2].spec.name
    assert concat_facet.vconcat[1].spec.name != concat_facet.vconcat[2].spec.name
