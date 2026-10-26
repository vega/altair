"""Regression tests for layer data inheritance when using chart addition."""

import pandas as pd
import pytest

import altair as alt


@pytest.fixture
def layers():
    data = pd.DataFrame({"x": list(range(15)), "y": list(range(15))})
    bars = alt.Chart(data).mark_bar().encode(x="x:O", y="y:Q")
    ticks = bars.mark_tick()
    datum_rule = alt.Chart().mark_rule(color="red").encode(y=alt.datum(5))
    aggregate_rule = alt.Chart().mark_rule(color="red").encode(y="mean(y):Q")
    return data, bars, ticks, datum_rule, aggregate_rule


@pytest.mark.parametrize("rule_index", [2, 3])
def test_add_data_less_layer_matches_layer_constructor(layers, rule_index):
    _, bars, ticks, datum_rule, aggregate_rule = layers
    rule = (datum_rule, aggregate_rule)[rule_index - 2]

    combined = bars + ticks + rule
    expected = alt.layer(bars, ticks, rule)
    assert combined.to_dict() == expected.to_dict()
    assert "data" not in combined.to_dict()
    assert combined.to_dict()["layer"][-1]["data"] == {"name": "empty"}


def test_layer_addition_order_keeps_each_layers_data(layers):
    _, bars, ticks, datum_rule, _ = layers

    combined = datum_rule + bars + ticks
    explicit = alt.layer(datum_rule, bars, ticks)
    assert combined.to_dict() == explicit.to_dict()
    assert combined.to_dict()["layer"][0]["data"] == {"name": "empty"}


@pytest.mark.parametrize("method", ["iadd", "add_layers", "copy"])
def test_add_preserves_data_less_layer_with_layerchart_methods(layers, method):
    _, bars, ticks, datum_rule, _ = layers
    combined = bars + ticks

    if method == "iadd":
        combined += datum_rule
    elif method == "add_layers":
        combined = combined.add_layers(datum_rule)
    else:
        combined = combined.copy(deep=["layer"]) + datum_rule

    assert combined.to_dict() == alt.layer(bars, ticks, datum_rule).to_dict()


@pytest.mark.parametrize("set_data", ["constructor", "properties"])
def test_explicit_shared_data_is_inherited_by_new_layers(layers, set_data):
    data, bars, ticks, datum_rule, _ = layers

    if set_data == "constructor":
        combined = alt.layer(bars, ticks, data=data)
    else:
        combined = (bars + ticks).properties(data=data)

    result = (combined + datum_rule).to_dict()
    assert "data" in result
    assert all("data" not in part for part in result["layer"])


def test_unrelated_layer_source_is_not_overwritten(layers):
    _, bars, ticks, datum_rule, _ = layers
    separate = alt.Chart(pd.DataFrame({"z": [1]})).mark_point().encode(x="z:Q")
    result = (bars + ticks + separate + datum_rule).to_dict()

    assert "data" not in result
    assert result["layer"][0]["data"] == result["layer"][1]["data"]
    assert result["layer"][2]["data"] != result["layer"][0]["data"]
    assert result["layer"][3]["data"] == {"name": "empty"}


@pytest.mark.parametrize("operator", ["add", "iadd", "add_layers"])
def test_filter_scope_survives_data_less_addition(layers, operator):
    _, bars, ticks, datum_rule, _ = layers
    filtered = (bars + ticks).transform_filter("datum.y > 10")
    expected = alt.layer(filtered, datum_rule)

    if operator == "iadd":
        filtered += datum_rule
        combined = filtered
    elif operator == "add_layers":
        combined = filtered.add_layers(datum_rule)
    else:
        combined = filtered + datum_rule

    assert combined.to_dict() == expected.to_dict()
    # The filter applies to the nested original chart, not the annotation.
    assert "transform" not in combined.to_dict()
    assert combined.to_dict()["layer"][0]["transform"] == [{"filter": "datum.y > 10"}]


def test_nested_deep_copy_preserves_data_ownership(layers):
    _, bars, ticks, datum_rule, _ = layers
    separate = (
        alt.Chart(pd.DataFrame({"x": [1], "y": [1]}))
        .mark_point()
        .encode(x="x:O", y="y:Q")
    )
    outer = alt.layer(bars + ticks, separate)
    original = outer.layer[0] + datum_rule
    copied = outer.copy().layer[0] + datum_rule

    assert copied.to_dict() == original.to_dict()
    assert copied.to_dict() == alt.layer(bars, ticks, datum_rule).to_dict()


@pytest.mark.parametrize("assignment", ["attribute", "getitem", "properties"])
def test_explicit_data_assignment_is_inherited(layers, assignment):
    data, bars, ticks, datum_rule, _ = layers
    combined = bars + ticks

    if assignment == "attribute":
        combined.data = data
    elif assignment == "getitem":
        combined["data"] = data
    else:
        combined = combined.properties(data=data)

    result = (combined + datum_rule).to_dict()
    assert "data" in result
    assert all("data" not in part for part in result["layer"])


@pytest.mark.parametrize("mutation", ["append", "replace"])
def test_manually_edited_layers_do_not_raise_zip_errors(layers, mutation):
    _, bars, ticks, datum_rule, _ = layers
    combined = bars + ticks
    if mutation == "append":
        combined.layer.append(ticks)
    else:
        combined.layer = [bars, ticks, bars]
    result = combined + datum_rule
    assert len(result.to_dict()["layer"]) == 2
    assert result.to_dict()["layer"][-1]["mark"]["type"] == "rule"


@pytest.mark.parametrize(
    ("property_name", "value"), [("background", "white"), ("padding", 12)]
)
def test_filter_and_top_level_properties_stay_intact(layers, property_name, value):
    _, bars, ticks, datum_rule, _ = layers
    filtered = (
        (bars + ticks)
        .transform_filter("datum.y > 10")
        .properties(**{property_name: value})
    )

    result = (filtered + datum_rule).to_dict()

    assert result[property_name] == value
    assert result["layer"][0]["transform"] == [{"filter": "datum.y > 10"}]
    assert property_name not in result["layer"][0]


@pytest.mark.parametrize("operator", ["add", "iadd", "add_layers"])
def test_filter_scope_does_not_leak_to_a_new_data_backed_layer(layers, operator):
    """A new independent data source must not inherit the prior layer filter."""
    _, bars, ticks, _, _ = layers
    separate = (
        alt.Chart(pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 2]}))
        .mark_point()
        .encode(x="x:O", y="y:Q")
    )
    filtered = (bars + ticks).transform_filter("datum.y > 10")
    expected = alt.layer(filtered, separate).to_dict()

    if operator == "iadd":
        filtered += separate
        actual = filtered.to_dict()
    elif operator == "add_layers":
        actual = filtered.add_layers(separate).to_dict()
    else:
        actual = (filtered + separate).to_dict()

    assert actual == expected
    assert "transform" not in actual
    assert actual["layer"][0]["transform"] == [{"filter": "datum.y > 10"}]
    assert "transform" not in actual["layer"][1]
    assert actual["layer"][1]["data"] != actual["layer"][0]["data"]


@pytest.mark.parametrize("operation", ["add", "iadd", "add_layers"])
@pytest.mark.parametrize("other_kind", ["datum_rule", "separate_data"])
def test_rendered_filter_scope_matches_explicit_layer(layers, operation, other_kind):
    """The actual Vega-Lite SVG must keep original marks filtered (#4182)."""
    import xml.etree.ElementTree as et

    vl_convert = pytest.importorskip("vl_convert")
    _, bars, ticks, datum_rule, _ = layers
    if other_kind == "datum_rule":
        other = datum_rule
    else:
        other = (
            alt.Chart(pd.DataFrame({"x": [0, 1, 2], "y": [1, 2, 3]}))
            .mark_point(color="green")
            .encode(x="x:O", y="y:Q")
        )

    def count_marks(chart):
        root = et.fromstring(vl_convert.vegalite_to_svg(chart.to_dict()))
        counts = []
        for element in root.iter():
            classes = element.get("class", "").split()
            if "role-mark" in classes:
                mark = next(
                    (name.removeprefix("mark-") for name in classes
                     if name.startswith("mark-")),
                    None,
                )
                counts.append((mark, len(element)))
        return counts

    def filtered_base():
        return (bars + ticks).transform_filter("datum.x < 4")

    expected = count_marks(alt.layer(filtered_base(), other))
    chart = filtered_base()
    if operation == "add":
        chart = chart + other
    elif operation == "iadd":
        chart += other
    else:
        chart = chart.add_layers(other)

    actual = count_marks(chart)
    assert actual == expected
    expected_extra = ("rule", 1) if other_kind == "datum_rule" else ("symbol", 3)
    assert actual == [("rect", 4), ("rect", 4), expected_extra]
