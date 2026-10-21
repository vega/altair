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
