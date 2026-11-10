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
    expected = alt.layer(bars + ticks, rule)
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

    assert combined.to_dict() == alt.layer(bars + ticks, datum_rule).to_dict()


@pytest.mark.parametrize("set_data", ["constructor", "properties"])
def test_explicit_shared_data_stays_in_existing_scope(layers, set_data):
    data, bars, ticks, datum_rule, _ = layers

    if set_data == "constructor":
        combined = alt.layer(bars, ticks, data=data)
    else:
        combined = (bars + ticks).properties(data=data)

    result = (combined + datum_rule).to_dict()
    assert "data" not in result
    assert "data" in result["layer"][0]
    assert result["layer"][-1]["data"] == {"name": "empty"}


def test_unrelated_layer_source_is_not_overwritten(layers):
    _, bars, ticks, datum_rule, _ = layers
    separate = alt.Chart(pd.DataFrame({"z": [1]})).mark_point().encode(x="z:Q")
    result = (bars + ticks + separate + datum_rule).to_dict()

    assert "data" not in result
    assert result["layer"][0]["data"] != result["layer"][1]["data"]
    assert len(result["layer"][0]["layer"]) == 2
    assert result["layer"][2]["data"] == {"name": "empty"}


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
    assert copied.to_dict() == alt.layer(bars + ticks, datum_rule).to_dict()


@pytest.mark.parametrize("assignment", ["attribute", "getitem", "properties"])
def test_explicit_data_assignment_preserves_scope(layers, assignment):
    data, bars, ticks, datum_rule, _ = layers
    combined = bars + ticks

    if assignment == "attribute":
        combined.data = data
    elif assignment == "getitem":
        combined["data"] = data
    else:
        combined = combined.properties(data=data)

    result = (combined + datum_rule).to_dict()
    assert "data" not in result
    assert "data" in result["layer"][0]
    assert result["layer"][-1]["data"] == {"name": "empty"}


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
                    (
                        name.removeprefix("mark-")
                        for name in classes
                        if name.startswith("mark-")
                    ),
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


def test_aggregate_rule_requires_explicit_shared_data():
    """An aggregate rule must opt into data shared by independent layers."""
    import xml.etree.ElementTree as et

    vl_convert = pytest.importorskip("vl_convert")
    source = pd.DataFrame({"category": ["A", "B", "C"], "value": [2, 5, 3]})
    base = alt.Chart(source).encode(x="category:N", y="value:Q")
    bars = base.mark_bar()
    ticks = base.mark_tick()
    mean_rule = alt.Chart().mark_rule(color="red").encode(y="mean(value):Q")

    def count_rules(chart):
        root = et.fromstring(vl_convert.vegalite_to_svg(chart.to_dict()))
        return sum(
            len(group)
            for group in root.iter()
            if "role-mark" in group.get("class", "").split()
            and "mark-rule" in group.get("class", "").split()
        )

    # Previously chained aggregation relied on accidentally inherited data.
    assert count_rules(bars + ticks + mean_rule) == 0
    # Both supported ways of explicitly sharing data draw exactly one rule.
    assert count_rules((bars + ticks + mean_rule).properties(data=source)) == 1
    assert count_rules(alt.layer(bars, ticks, mean_rule, data=source)) == 1


def compose(chart, other, operation):
    if operation == "add":
        return chart + other
    if operation == "iadd":
        chart += other
        return chart
    return chart.add_layers(other)


@pytest.mark.parametrize("operation", ["add", "iadd", "add_layers"])
@pytest.mark.parametrize("encoding", ["y", "y:Q"])
def test_shared_encoding_keeps_its_data_for_type_inference(layers, operation, encoding):
    _, bars, ticks, rule, _ = layers
    shared = (bars + ticks).encode(color=encoding)
    expected = alt.layer(shared, rule).to_dict()
    result = compose(shared, rule, operation).to_dict()
    assert result == expected
    assert result["layer"][0]["encoding"]["color"]["type"] == "quantitative"
    assert result["layer"][1]["data"] == {"name": "empty"}


@pytest.mark.parametrize("operation", ["add", "iadd", "add_layers"])
@pytest.mark.parametrize(
    ("property_name", "value"),
    [("usermeta", {"note": "example"}), ("datasets", {"extra": [{"x": 1}]})],
)
def test_root_only_metadata_moves_out_of_nested_scope(
    layers, operation, property_name, value
):
    _, bars, ticks, rule, _ = layers
    shared = (bars + ticks).transform_filter("datum.y > 10")
    shared = shared.properties(**{property_name: value})
    result = compose(shared, rule, operation).to_dict()
    if property_name == "datasets":
        assert result[property_name]["extra"] == value["extra"]
    else:
        assert result[property_name] == value
    assert property_name not in result["layer"][0]


@pytest.mark.parametrize("field", ["data", "usermeta"])
def test_copy_ignore_preserves_root_references(field):
    source = {"values": [{"x": 1}, {"x": 2}]}
    base = alt.Chart(source)
    chart = (base.mark_point() + base.mark_bar()).properties(usermeta={"note": []})
    copied = chart.copy(ignore=[field])
    assert copied[field] is chart[field]


@pytest.mark.parametrize("operation", ["add", "iadd", "add_layers"])
@pytest.mark.parametrize("round_trip", ["dict", "json"])
def test_round_trip_preserves_independent_annotation(layers, operation, round_trip):
    _, bars, ticks, rule, _ = layers
    chart = bars + ticks
    if round_trip == "dict":
        restored = alt.LayerChart.from_dict(chart.to_dict())
    else:
        restored = alt.LayerChart.from_json(chart.to_json())
    before = restored.to_dict()
    result = compose(restored, rule, operation).to_dict()
    assert result["layer"][0]["layer"] == before["layer"]
    assert result["layer"][0]["data"] == before["data"]
    assert result["config"] == before["config"]
    assert "config" not in result["layer"][0]
    assert result["layer"][-1]["data"] == {"name": "empty"}


@pytest.mark.parametrize("assignment", ["attribute", "getitem", "properties"])
def test_clearing_data_uses_one_consistent_scope(layers, assignment):
    _, bars, ticks, rule, _ = layers
    chart = alt.LayerChart()
    if assignment == "attribute":
        chart.data = alt.Undefined
    elif assignment == "getitem":
        chart["data"] = alt.Undefined
    else:
        chart = chart.properties(data=alt.Undefined)
    chart += bars
    chart += ticks
    assert (chart + rule).to_dict() == alt.layer(bars + ticks, rule).to_dict()


def test_same_length_replacement_never_restores_stale_data(layers):
    _, bars, ticks, rule, _ = layers
    chart = bars + ticks
    chart.layer[1] = rule
    result = (chart + rule).to_dict()
    # The replacement inherits its current parent data; adding another layer
    # must preserve that existing scope, without replaying old ownership flags.
    assert result == alt.layer(chart, rule).to_dict()
    assert result["layer"][-1]["data"] == {"name": "empty"}


def test_identical_source_chain_stays_flat(layers):
    _, bars, ticks, _, _ = layers
    result = (bars + ticks + bars.mark_line()).to_dict()
    assert len(result["layer"]) == 3
    assert all("layer" not in part for part in result["layer"])


@pytest.mark.parametrize("operation", ["add", "iadd", "add_layers"])
def test_resolve_scope_does_not_leak(layers, operation):
    _, bars, ticks, rule, _ = layers
    chart = (bars + ticks).resolve_scale(y="independent")
    expected = alt.layer(chart, rule).to_dict()
    assert compose(chart, rule, operation).to_dict() == expected


def test_rendered_shared_encoding_and_round_trip_draw_one_rule(layers):
    import xml.etree.ElementTree as et

    vl_convert = pytest.importorskip("vl_convert")
    _, bars, ticks, rule, _ = layers
    chart = (bars + ticks).encode(color="y")
    restored = alt.LayerChart.from_dict(chart.to_dict())
    for source in [chart, restored]:
        svg = vl_convert.vegalite_to_svg((source + rule).to_dict())
        root = et.fromstring(svg)
        rules = sum(
            len(group)
            for group in root.iter()
            if "mark-rule" in group.get("class", "").split()
            and "role-mark" in group.get("class", "").split()
        )
        assert rules == 1


def test_repeated_independent_annotations_do_not_accumulate_nesting(layers):
    _, bars, ticks, rule, _ = layers
    chart = bars + ticks
    for _ in range(20):
        chart += rule
    result = chart.to_dict()
    assert len(result["layer"]) == 21
    assert len(result["layer"][0]["layer"]) == 2
    assert all("layer" not in part for part in result["layer"][1:])


@pytest.mark.parametrize("reconstruct", [False, True])
def test_transformed_view_names_keep_nested_unit_views(layers, reconstruct):
    from altair.utils._transformed_data import name_views

    _, bars, ticks, rule, _ = layers
    chart = bars + ticks + rule.properties(name="annotation")
    if reconstruct:
        chart = alt.Chart.from_dict(chart.to_dict())
    names = name_views(chart, exclude=["annotation"])
    assert len(names) == 2
    assert len(set(names)) == 2
    assert names == [part.name for part in chart.layer[0].layer]


@pytest.mark.parametrize("scale", ["shared", "independent"])
@pytest.mark.parametrize("construction", ["constructor", "addition"])
def test_faceted_explicit_shared_data_renders_one_annotation_per_panel(
    scale, construction
):
    import xml.etree.ElementTree as et

    vl_convert = pytest.importorskip("vl_convert")
    data = pd.DataFrame(
        {"group": ["A", "A", "B", "B"], "x": [1, 2, 1, 2], "y": [2, 4, 3, 5]}
    )
    base = alt.Chart().encode(x="x:O", y="y:Q")
    bars, ticks = base.mark_bar(), base.mark_tick()
    rule = alt.Chart(alt.InlineData(values=[{}])).mark_rule().encode(y=alt.datum(3))
    if construction == "constructor":
        chart = alt.layer(bars, ticks, rule, data=data)
    else:
        chart = (bars + ticks + rule).properties(data=data)
    faceted = chart.facet(column="group:N").resolve_scale(y=scale)
    spec = faceted.to_dict()
    assert spec["resolve"]["scale"]["y"] == scale
    root = et.fromstring(vl_convert.vegalite_to_svg(spec))
    rule_counts = []
    bar_counts = []
    for group in root.iter():
        classes = group.get("class", "").split()
        if "role-mark" in classes:
            if "mark-rule" in classes:
                rule_counts.append(len(group))
            elif "mark-rect" in classes:
                bar_counts.append(len(group))
    assert rule_counts == [1, 1]
    assert bar_counts == [2, 2, 2, 2]
