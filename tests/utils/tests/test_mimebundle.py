import pytest

import altair as alt
from altair.utils.mimebundle import spec_to_mimebundle

try:
    import altair_saver  # noqa: F401
except ImportError:
    altair_saver = None

try:
    import vl_convert as vlc  # noqa: F401
except ImportError:
    vlc = None


@pytest.fixture
def vegalite_spec():
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
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
        "mark": "bar",
        "encoding": {
            "x": {"field": "a", "type": "ordinal"},
            "y": {"field": "b", "type": "quantitative"},
        },
    }


@pytest.mark.save_engine
@pytest.mark.parametrize("engine", ["vl-convert", "altair_saver", None])
def test_vegalite_to_vega_mimebundle(engine, vegalite_spec, vega_spec):
    if engine == "vl-convert" and vlc is None:
        pytest.skip("vl_convert not importable; cannot run mimebundle tests")
    elif engine == "altair_saver" and altair_saver is None:
        pytest.skip("altair_saver not importable; cannot run mimebundle tests")
    elif vlc is None and altair_saver is None:
        pytest.skip(
            "Neither altair_saver nor vl_convert are importable;"
            + " cannot run mimebundle tests"
        )

    # temporary fix for https://github.com/vega/vega-lite/issues/7776
    def delete_none(axes):
        for axis in axes:
            for key, value in list(axis.items()):
                if value is None:
                    del axis[key]
        return axes

    bundle = spec_to_mimebundle(
        spec=vegalite_spec,
        format="vega",
        mode="vega-lite",
        vega_version=alt.VEGA_VERSION,
        vegalite_version=alt.VEGALITE_VERSION,
        vegaembed_version=alt.VEGAEMBED_VERSION,
        engine=engine,
    )

    bundle["application/vnd.vega.v5+json"]["axes"] = delete_none(
        bundle["application/vnd.vega.v5+json"]["axes"]
    )
    assert bundle == {"application/vnd.vega.v5+json": vega_spec}


def test_spec_to_vegalite_mimebundle(vegalite_spec):
    bundle = spec_to_mimebundle(
        spec=vegalite_spec,
        mode="vega-lite",
        format="vega-lite",
        vegalite_version=alt.VEGALITE_VERSION,
    )
    assert bundle == {"application/vnd.vegalite.v5+json": vegalite_spec}


def test_spec_to_json_mimebundle():
    bundle = spec_to_mimebundle(
        spec=vegalite_spec,
        mode="vega-lite",
        format="json",
    )
    assert bundle == {"application/json": vegalite_spec}
