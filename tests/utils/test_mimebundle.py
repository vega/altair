from __future__ import annotations

from typing import Any

import pytest

import altair as alt
from altair import VEGA_VERSION
from altair.utils.mimebundle import spec_to_mimebundle
from tests import skip_requires_vegafusion, skip_requires_vl_convert


@pytest.fixture
def vegalite_spec() -> dict[str, Any]:
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
        "description": "A simple bar chart with embedded data.",
        "data": {
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
        },
        "mark": {"type": "bar"},
        "encoding": {
            "x": {"field": "a", "type": "ordinal"},
            "y": {"field": "b", "type": "quantitative"},
        },
    }


@pytest.fixture
def vega_spec():
    return {
        "$schema": "https://vega.github.io/schema/vega/v6.json",
        "axes": [
            {
                "aria": False,
                "domain": False,
                "grid": True,
                "gridScale": "x",
                "labels": False,
                "maxExtent": 0,
                "minExtent": 0,
                "orient": "left",
                "scale": "y",
                "tickCount": {"signal": "ceil(height/40)"},
                "ticks": False,
                "zindex": 0,
            },
            {
                "grid": False,
                "labelAlign": "right",
                "labelAngle": 270,
                "labelBaseline": "middle",
                "orient": "bottom",
                "scale": "x",
                "title": "a",
                "zindex": 0,
            },
            {
                "grid": False,
                "labelOverlap": True,
                "orient": "left",
                "scale": "y",
                "tickCount": {"signal": "ceil(height/40)"},
                "title": "b",
                "zindex": 0,
            },
        ],
        "background": "white",
        "data": [
            {
                "name": "source_0",
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
                ],
            },
            {
                "name": "data_0",
                "source": "source_0",
                "transform": [
                    {
                        "as": ["b_start", "b_end"],
                        "field": "b",
                        "groupby": ["a"],
                        "offset": "zero",
                        "sort": {"field": [], "order": []},
                        "type": "stack",
                    },
                    {
                        "expr": 'isValid(datum["b"]) && isFinite(+datum["b"])',
                        "type": "filter",
                    },
                ],
            },
        ],
        "description": "A simple bar chart with embedded data.",
        "height": 300,
        "marks": [
            {
                "encode": {
                    "update": {
                        "ariaRoleDescription": {"value": "bar"},
                        "description": {
                            "signal": '"a: " + (isValid(datum["a"]) ? datum["a"] : ""+datum["a"]) + "; b: " + (format(datum["b"], ""))'
                        },
                        "fill": {"value": "#4c78a8"},
                        "width": {"signal": "max(0.25, bandwidth('x'))"},
                        "x": {"field": "a", "scale": "x"},
                        "y": {"field": "b_end", "scale": "y"},
                        "y2": {"field": "b_start", "scale": "y"},
                    }
                },
                "from": {"data": "data_0"},
                "name": "marks",
                "style": ["bar"],
                "type": "rect",
            }
        ],
        "padding": 5,
        "scales": [
            {
                "domain": {"data": "data_0", "field": "a", "sort": True},
                "name": "x",
                "paddingInner": 0.1,
                "paddingOuter": 0.05,
                "range": {"step": {"signal": "x_step"}},
                "type": "band",
            },
            {
                "domain": {"data": "data_0", "fields": ["b_start", "b_end"]},
                "name": "y",
                "nice": True,
                "range": [{"signal": "height"}, 0],
                "type": "linear",
                "zero": True,
            },
        ],
        "signals": [
            {"name": "x_step", "value": 20},
            {
                "name": "width",
                "update": "bandspace(domain('x').length, 0.1, 0.05) * x_step",
            },
        ],
        "style": "cell",
    }


@skip_requires_vl_convert
def test_vegalite_to_vega_mimebundle(vegalite_spec, vega_spec):
    bundle = spec_to_mimebundle(
        spec=vegalite_spec,
        format="vega",
        mode="vega-lite",
        vega_version=alt.VEGA_VERSION,
        vegalite_version=alt.VEGALITE_VERSION,
        vegaembed_version=alt.VEGAEMBED_VERSION,
        engine="vl-convert",
    )

    assert bundle == {"application/vnd.vega.v6+json": vega_spec}


def test_spec_to_vegalite_mimebundle(vegalite_spec):
    bundle = spec_to_mimebundle(
        spec=vegalite_spec,
        mode="vega-lite",
        format="vega-lite",
        vegalite_version=alt.VEGALITE_VERSION,
    )
    assert bundle == {"application/vnd.vegalite.v6+json": vegalite_spec}


def test_spec_to_vega_mimebundle(vega_spec):
    # ValueError: mode must be 'vega-lite'
    with pytest.raises(ValueError):  # noqa: PT011
        spec_to_mimebundle(  # pyright: ignore[reportCallIssue]
            spec=vega_spec,
            mode="vega",  # pyright: ignore[reportArgumentType]
            format="vega",
            vega_version=alt.VEGA_VERSION,
        )


def test_spec_to_json_mimebundle(vegalite_spec):
    bundle = spec_to_mimebundle(
        spec=vegalite_spec,
        mode="vega-lite",
        format="json",
    )
    assert bundle == {"application/json": vegalite_spec}


def check_pre_transformed_vega_spec(vega_spec):
    assert (
        vega_spec["$schema"]
        == f"https://vega.github.io/schema/vega/v{VEGA_VERSION}.json"
    )

    # Check data_0 is there
    data_0 = vega_spec["data"][1]
    assert data_0["name"] == "data_0"

    # Check that the bin transform has been applied
    row0 = data_0["values"][0]
    assert row0 == {"a": "A", "b_end": 28.0, "b_start": 0.0}

    # And no transforms remain
    assert len(data_0.get("transform", [])) == 0


@skip_requires_vegafusion
def test_vegafusion_spec_to_vega_mime_bundle(vegalite_spec):
    with alt.data_transformers.enable("vegafusion"):
        bundle = spec_to_mimebundle(
            spec=vegalite_spec,
            mode="vega-lite",
            format="vega",
        )
        # Returned bundle will be vega
        vega_spec = bundle["application/vnd.vega.v6+json"]
        check_pre_transformed_vega_spec(vega_spec)


@skip_requires_vegafusion
def test_vegafusion_chart_to_vega_mime_bundle(vegalite_spec):
    chart = alt.Chart.from_dict(vegalite_spec)
    with alt.data_transformers.enable("vegafusion"), alt.renderers.enable("json"):
        bundle = chart._repr_mimebundle_()
        assert isinstance(bundle, tuple)
        vega_spec = bundle[0]["application/json"]
        check_pre_transformed_vega_spec(vega_spec)
