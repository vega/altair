"""View-name allocation and selection references in composed charts."""

import warnings

import pandas as pd
import pytest

import altair as alt


@pytest.fixture
def base():
    with alt.theme.enable("default"):
        yield (
            alt.Chart(
                pd.DataFrame(
                    {"x": [1, 2, 3], "y": [1, 4, 9], "category": ["a", "b", "c"]}
                )
            )
            .mark_point()
            .encode(x="x:Q", y="y:Q")
        )


def _panel(base, kind, name, selection=None):
    named = base.properties(name=name)
    chart = alt.layer(named.mark_line(), base) if kind == "layer" else named
    if selection is not None:
        chart = chart.add_params(selection)
    if kind == "facet":
        chart = chart.facet(column="category:N")
    return chart


def _units(spec):
    if "mark" in spec:
        yield spec
    else:
        for key in ("layer", "concat", "hconcat", "vconcat", "spec"):
            if key in spec:
                children = spec[key]
                for child in children if isinstance(children, list) else [children]:
                    yield from _units(child)


def _names(spec):
    return [unit["name"] for unit in _units(spec) if "name" in unit]


@pytest.mark.parametrize("concat", [alt.concat, alt.hconcat, alt.vconcat])
@pytest.mark.parametrize("kind", ["unit", "layer", "facet"])
@pytest.mark.parametrize("placement", ["none", "before", "after"])
def test_unique_explicit_names_are_preserved(base, concat, kind, placement):
    brush = alt.selection_point(fields=["x"])
    names = ["report_0", "view_0123456789abcdef_1"]
    panels = [
        _panel(base, kind, name, brush if placement == "before" else None)
        for name in names
    ]
    originals = [panel.to_dict() for panel in panels]

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        chart = concat(*panels)
        if placement == "after":
            chart = chart.add_params(brush)
        spec = chart.to_dict()
        assert alt.Chart.from_dict(spec).to_dict() == spec

    assert _names(spec) == names
    if placement != "none":
        assert spec["params"][0]["views"] == names
    assert [panel.to_dict() for panel in panels] == originals


@pytest.mark.parametrize("concat", [alt.concat, alt.hconcat, alt.vconcat])
@pytest.mark.parametrize("kind", ["unit", "layer", "facet"])
@pytest.mark.parametrize("base_name", ["report", "report_0"])
def test_replacements_avoid_reserved_names(base, concat, kind, base_name):
    brush = alt.selection_point(fields=["x"])
    panels = [
        _panel(base, kind, name, brush)
        for name in [base_name, base_name, f"{base_name}_0"]
    ]
    originals = [panel.to_dict() for panel in panels]

    with pytest.warns(UserWarning, match="Chart name") as caught:
        chart = concat(*panels)
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        spec = chart.to_dict()

    names = [f"{base_name}_1", f"{base_name}_2", f"{base_name}_0"]
    assert _names(spec) == names
    assert spec["params"][0]["views"] == names
    assert len(caught) == 1
    assert [panel.to_dict() for panel in panels] == originals


@pytest.mark.parametrize("kind", ["unit", "layer", "facet"])
def test_collisions_without_parameters_are_disambiguated(base, kind):
    panel = _panel(base, kind, "report")
    with pytest.warns(UserWarning, match="Chart name"):
        chart = alt.vconcat(panel, panel)
    spec = chart.to_dict()
    assert _names(spec) == ["report_0", "report_1"]
    assert "params" not in spec


@pytest.mark.parametrize("kind", ["unit", "layer", "facet"])
def test_nested_names_keep_independent_selection_scopes(base, kind):
    first = alt.selection_point(name="first", fields=["x"])
    second = alt.selection_point(name="second", fields=["x"])
    top = alt.hconcat(
        _panel(base, kind, "shared", first), base.properties(name="top_other")
    )
    bottom = alt.hconcat(
        _panel(base, kind, "shared", second), base.properties(name="bottom_other")
    )
    originals = [top.to_dict(), bottom.to_dict()]

    with pytest.warns(UserWarning, match="Chart name"):
        chart = alt.vconcat(top, bottom)
    spec = chart.to_dict()
    assert _names(spec) == ["shared_0", "top_other", "shared_1", "bottom_other"]
    assert {param["name"]: param["views"] for param in spec["params"]} == {
        "first": ["shared_0"],
        "second": ["shared_1"],
    }
    assert [top.to_dict(), bottom.to_dict()] == originals
    vlc = pytest.importorskip("vl_convert")
    vlc.vegalite_to_svg(spec)


@pytest.mark.parametrize("new_selection", [False, True])
def test_appending_a_panel_does_not_broaden_existing_selections(base, new_selection):
    brush = alt.selection_point(name="first", fields=["x"])
    original = alt.hconcat(
        base.properties(name="shared").add_params(brush), base.properties(name="other")
    )
    before = original.to_dict()
    appended = base.properties(name="shared")
    if new_selection:
        appended = appended.add_params(alt.selection_point(name="second", fields=["x"]))

    with pytest.warns(UserWarning, match="Chart name"):
        chart = original | appended
    spec = chart.to_dict()
    names = _names(spec)
    params = {param["name"]: param["views"] for param in spec["params"]}
    assert len(set(names)) == len(names)
    assert params["first"] == [names[0]]
    if new_selection:
        assert params["second"] == [names[2]]
    assert original.to_dict() == before


def test_generated_names_yield_to_explicit_names_without_warning(base):
    brush = alt.selection_point(fields=["x"])
    generated = alt.layer(base.add_params(brush), base.mark_line())
    old_name = generated.layer[0].name
    original = generated.to_dict()
    derived = generated.transform_filter("datum.x > 1").copy()

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        chart = alt.vconcat(derived, base.properties(name=old_name))
        spec = chart.to_dict()
    names = _names(spec)
    assert names[0] != old_name
    assert names[1] == old_name
    assert spec["params"][0]["views"] == [names[0]]
    assert generated.to_dict() == original


def test_explicitly_setting_a_generated_name_changes_its_provenance(base):
    brush = alt.selection_point(fields=["x"])
    generated = alt.hconcat(base.add_params(brush)).hconcat[0]
    explicit = generated.properties(name=generated.name)

    with pytest.warns(UserWarning, match="Chart name"):
        chart = alt.hconcat(explicit, explicit)
    assert _names(chart.to_dict()) == [f"{generated.name}_0", f"{generated.name}_1"]


def test_container_names_are_reserved_before_generating_replacements(base):
    row = alt.hconcat(base).properties(name="report_0")
    with pytest.warns(UserWarning, match="Chart name"):
        chart = alt.vconcat(
            base.properties(name="report"), base.properties(name="report"), row
        )
    spec = chart.to_dict()
    assert _names(spec) == ["report_1", "report_2"]
    assert spec["vconcat"][2]["name"] == "report_0"


@pytest.mark.parametrize("layered", [False, True])
def test_repeated_view_references_follow_renaming(base, layered):
    brush = alt.selection_point(fields=["x"])
    named = base.properties(name="report")
    panel = alt.layer(named, base.mark_line()) if layered else named
    panels = [
        (panel.properties(name=f"layer_{i}") if layered else panel)
        .add_params(brush)
        .repeat(column=["x", "y"])
        for i in range(2)
    ]

    with pytest.warns(UserWarning, match="Chart name"):
        chart = alt.vconcat(*panels)
    spec = chart.to_dict()
    expected = [
        f"child__column_{field}_report_{i}"
        if layered
        else f"report_{i}_child__column_{field}"
        for i in range(2)
        for field in ["x", "y"]
    ]
    assert spec["params"][0]["views"] == expected
    vlc = pytest.importorskip("vl_convert")
    vlc.vegalite_to_svg(spec)


def test_colliding_layer_names_render_with_a_selection(base):
    named = base.properties(name="panel")
    brush = alt.selection_point(fields=["x"])
    with pytest.warns(UserWarning, match="Chart name"):
        chart = alt.layer(named.mark_line(), named).add_params(brush)
    spec = chart.to_dict()
    assert _names(spec) == ["panel_0", "panel_1"]
    assert spec["params"][0]["views"] == ["panel_0"]
    vlc = pytest.importorskip("vl_convert")
    vlc.vegalite_to_svg(spec)
