"""
Test spec for auto-detect alt.expr in encodings feature.

This feature automatically creates calculate transforms when alt.expr objects
are used directly in encodings.

Usage:
    python test_auto_expr_encoding.py

Expected: All tests pass and output valid Vega-Lite specs with auto-created transforms.
"""

import json

import altair as alt
from altair.expr.core import datum


def test_simple_expression():
    """Test: Simple expression in encoding."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x="a:Q",
            y=datum.b + datum.c,
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 1
    assert spec["transform"][0]["calculate"] == "(datum.b + datum.c)"
    assert spec["encoding"]["y"]["field"].startswith("_calc_")
    print("✓ test_simple_expression passed")


def test_multiple_expressions():
    """Test: Multiple expressions in different encodings."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=datum.a * 2,
            y=datum.b + datum.c,
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 2
    print("✓ test_multiple_expressions passed")


def test_expression_with_string_shorthand():
    """Test: Mix of expression and regular string shorthand."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x="a:Q",
            y=datum.b + datum.c,
            color="category:N",
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 1
    assert spec["encoding"]["color"]["type"] == "nominal"
    print("✓ test_expression_with_string_shorthand passed")


def test_expression_with_aggregation():
    """Test: Expression encoding + aggregation on another field."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x="a:Q",
            y=datum.b + datum.c,
            size="mean(d):Q",
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 1
    assert spec["encoding"]["size"]["aggregate"] == "mean"
    print("✓ test_expression_with_aggregation passed")


def test_expr_functions():
    """Test: Using alt.expr functions."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x="a:Q",
            y=alt.expr.sqrt(datum.b * datum.b + datum.c * datum.c),
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert "sqrt" in spec["transform"][0]["calculate"]
    assert spec["encoding"]["y"]["type"] == "quantitative"
    print("✓ test_expr_functions passed")


def test_random_function():
    """Test: random() function returns quantitative type."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.random(),
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["x"]["type"] == "quantitative"
    print("✓ test_random_function passed")


def test_now_function():
    """Test: now() function returns quantitative type (timestamp in ms)."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.now(),
        )
    )
    spec = chart.to_dict()

    # now() returns a timestamp (number), so it's quantitative
    assert spec["encoding"]["x"]["type"] == "quantitative"
    print("✓ test_now_function passed")


def test_datetime_function():
    """Test: datetime() function returns temporal type."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.datetime(2020, 1, 1),
        )
    )
    spec = chart.to_dict()

    # datetime() creates a Date object, so it's temporal
    assert spec["encoding"]["x"]["type"] == "temporal"
    print("✓ test_datetime_function passed")


def test_is_valid_function():
    """Test: isValid() returns nominal (boolean) type."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.isValid(datum.value),
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["x"]["type"] == "nominal"
    print("✓ test_is_valid_function passed")


def test_format_function():
    """Test: format() returns nominal type."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.format(datum.value, ".2f"),
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["x"]["type"] == "nominal"
    print("✓ test_format_function passed")


def test_type_inference_numeric():
    """Test: Type inference for numeric operations."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x="a:Q",
            y=datum.b + datum.c,
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["y"]["type"] == "quantitative"
    print("✓ test_type_inference_numeric passed")


def test_type_inference_string():
    """Test: Type inference for string operations."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.lower(datum.category),
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["x"]["type"] == "nominal"
    print("✓ test_type_inference_string passed")


def test_type_inference_temporal():
    """Test: Type inference for temporal operations."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.year(datum.date),
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["x"]["type"] == "temporal"
    print("✓ test_type_inference_temporal passed")


def test_type_inference_comparison():
    """Test: Type inference for comparison operations."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=datum.a > datum.b,
        )
    )
    spec = chart.to_dict()

    assert spec["encoding"]["x"]["type"] == "nominal"
    print("✓ test_type_inference_comparison passed")


def test_chained_operations():
    """Test: Chained operations - using alt.expr functions."""
    # Note: datum.a.abs() doesn't work, but alt.expr.abs(datum.a) does
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=alt.expr.abs(datum.a),
            y=datum.b + datum.c,
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    calc = spec["transform"][0]["calculate"]
    assert "abs" in calc
    print("✓ test_chained_operations passed")


def test_param_in_datum():
    """Test: Using alt.param with datum[xcol_param]."""
    dropdown = alt.binding_select(
        options=["Horsepower", "Displacement"],
        name="X-axis column ",
    )
    xcol_param = alt.param(value="Horsepower", bind=dropdown)

    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x=datum[xcol_param],
            y="Miles_per_Gallon:Q",
        )
        .add_params(xcol_param)
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 1
    assert "param_" in spec["transform"][0]["calculate"]
    assert spec["encoding"]["x"]["field"].startswith("_calc_")
    assert "params" in spec
    print("✓ test_param_in_datum passed")


def test_mixed_with_transform_calculate():
    """Test: Expression encoding mixed with explicit transform_calculate."""
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .transform_calculate(explicit_field="datum.a * 2")
        .encode(
            x="explicit_field:Q",
            y=datum.b + datum.c,
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 2
    print("✓ test_mixed_with_transform_calculate passed")


def test_dataframe():
    """Test: Using with pandas DataFrame."""
    import pandas as pd

    data = pd.DataFrame(
        {"a": [1, 2, 3, 4, 5], "b": [10, 20, 30, 40, 50], "c": [5, 15, 25, 35, 45]}
    )

    chart = (
        alt.Chart(data)
        .mark_point()
        .encode(
            x="a:Q",
            y=datum.b + datum.c,
        )
    )
    spec = chart.to_dict()

    assert "transform" in spec
    assert len(spec["transform"]) == 1
    print("✓ test_dataframe passed")


if __name__ == "__main__":
    print("=" * 60)
    print("Testing auto-detect alt.expr in encodings")
    print("=" * 60)
    print()

    test_simple_expression()
    test_multiple_expressions()
    test_expression_with_string_shorthand()
    test_expression_with_aggregation()
    test_expr_functions()
    test_random_function()
    test_now_function()
    test_datetime_function()
    test_is_valid_function()
    test_format_function()
    test_type_inference_numeric()
    test_type_inference_string()
    test_type_inference_temporal()
    test_type_inference_comparison()
    test_chained_operations()
    test_mixed_with_transform_calculate()
    test_dataframe()
    test_param_in_datum()

    print()
    print("=" * 60)
    print("All tests passed!")
    print("=" * 60)

    # Print example spec
    print()
    print("Example spec:")
    chart = (
        alt.Chart("data.json")
        .mark_point()
        .encode(
            x="a:Q",
            y=datum.b + datum.c,
        )
    )
    print(json.dumps(chart.to_dict(), indent=2))
