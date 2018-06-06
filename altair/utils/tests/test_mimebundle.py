import pytest
import json

try:
    import selenium
except ImportError:
    selenium = None

from ..mimebundle import spec_to_mimebundle


# example from https://vega.github.io/editor/#/examples/vega-lite/bar
VEGALITE_SPEC = json.loads(
    """
        {
    "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
    "description": "A simple bar chart with embedded data.",
    "data": {
        "values": [
        {"a": "A","b": 28}, {"a": "B","b": 55}, {"a": "C","b": 43},
        {"a": "D","b": 91}, {"a": "E","b": 81}, {"a": "F","b": 53},
        {"a": "G","b": 19}, {"a": "H","b": 87}, {"a": "I","b": 52}
        ]
    },
    "mark": "bar",
    "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"}
    }
    }
    """
)

VEGA_SPEC = json.loads(
    """
    {
    "$schema": "https://vega.github.io/schema/vega/v3.0.json",
    "description": "A simple bar chart with embedded data.",
    "autosize": "pad",
    "padding": 5,
    "height": 200,
    "style": "cell",
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
            {"a": "I", "b": 52}
        ]
        },
        {
        "name": "data_0",
        "source": "source_0",
        "transform": [
            {"type": "formula", "expr": "toNumber(datum[\\"b\\"])", "as": "b"},
            {
            "type": "filter",
            "expr": "datum[\\"b\\"] !== null && !isNaN(datum[\\"b\\"])"
            }
        ]
        }
    ],
    "signals": [
        {"name": "x_step", "value": 21},
        {
        "name": "width",
        "update": "bandspace(domain('x').length, 0.1, 0.05) * x_step"
        }
    ],
    "marks": [
        {
        "name": "marks",
        "type": "rect",
        "style": ["bar"],
        "from": {"data": "data_0"},
        "encode": {
            "update": {
            "fill": {"value": "#4c78a8"},
            "x": {"scale": "x", "field": "a"},
            "width": {"scale": "x", "band": true},
            "y": {"scale": "y", "field": "b"},
            "y2": {"scale": "y", "value": 0}
            }
        }
        }
    ],
    "scales": [
        {
        "name": "x",
        "type": "band",
        "domain": {"data": "data_0", "field": "a", "sort": true},
        "range": {"step": {"signal": "x_step"}},
        "paddingInner": 0.1,
        "paddingOuter": 0.05
        },
        {
        "name": "y",
        "type": "linear",
        "domain": {"data": "data_0", "field": "b"},
        "range": [{"signal": "height"}, 0],
        "nice": true,
        "zero": true
        }
    ],
    "axes": [
        {
        "scale": "x",
        "orient": "bottom",
        "title": "a",
        "labelOverlap": true,
        "encode": {
            "labels": {
            "update": {
                "angle": {"value": 270},
                "align": {"value": "right"},
                "baseline": {"value": "middle"}
            }
            }
        },
        "zindex": 1
        },
        {
        "scale": "y",
        "orient": "left",
        "title": "b",
        "labelOverlap": true,
        "tickCount": {"signal": "ceil(height/40)"},
        "zindex": 1
        },
        {
        "scale": "y",
        "orient": "left",
        "grid": true,
        "tickCount": {"signal": "ceil(height/40)"},
        "gridScale": "x",
        "domain": false,
        "labels": false,
        "maxExtent": 0,
        "minExtent": 0,
        "ticks": false,
        "zindex": 0
        }
    ],
    "config": {"axisY": {"minExtent": 30}}
    }
    """
)

VEGAEMBED_VERSION = '3.14.0'
VEGALITE_VERSION = '2.3.1'
VEGA_VERSION = '3.3.1'

@pytest.mark.skipif('not selenium')
def test_spec_to_vega_mimebundle():
    try:
        bundle = spec_to_mimebundle(
            spec=VEGALITE_SPEC,
            format='vega',
            mode='vega-lite',
            vega_version=VEGA_VERSION,
            vegalite_version=VEGALITE_VERSION,
            vegaembed_version=VEGAEMBED_VERSION
        )
    except ValueError as err:
        if str(err).startswith('Internet connection'):
            pytest.skip("web connection required for png/svg export")
        else:
            raise
    assert bundle == {'application/vnd.vega.v3+json': VEGA_SPEC}


def test_spec_to_vegalite_mimebundle():
    bundle = spec_to_mimebundle(
        spec=VEGALITE_SPEC,
        mode='vega-lite',
        format='vega-lite',
        vegalite_version=VEGALITE_VERSION
    )
    assert bundle == {'application/vnd.vegalite.v2+json': VEGALITE_SPEC}


def test_spec_to_json_mimebundle():
    bundle = spec_to_mimebundle(
        spec=VEGALITE_SPEC,
        mode='vega-lite',
        format='json',
    )
    assert bundle == {'application/json': VEGALITE_SPEC}
