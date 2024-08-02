import json

import pytest

from altair import Chart, vegalite_compilers

try:
    import vl_convert as vlc
except ImportError:
    vlc = None


@pytest.fixture
def chart():
    return (
        Chart("cars.json")
        .mark_point()
        .encode(
            x="Horsepower:Q",
            y="Miles_per_Gallon:Q",
        )
    )


def assert_is_vega_spec(vega_spec):
    assert vega_spec["$schema"] == "https://vega.github.io/schema/vega/v5.json"
    assert "data" in vega_spec
    assert "marks" in vega_spec
    assert "scales" in vega_spec
    assert "axes" in vega_spec


def test_vegalite_compiler(chart):
    if vlc is None:
        pytest.skip("vl_convert is not installed")

    vegalite_spec = chart.to_dict()
    vega_spec = vegalite_compilers.get()(vegalite_spec)
    assert_is_vega_spec(vega_spec)


def test_to_dict_with_format_vega(chart):
    if vlc is None:
        pytest.skip("vl_convert is not installed")

    vega_spec = chart.to_dict(format="vega")
    assert_is_vega_spec(vega_spec)


def test_to_json_with_format_vega(chart):
    if vlc is None:
        pytest.skip("vl_convert is not installed")

    json_spec = chart.to_json(format="vega")
    assert isinstance(json_spec, str)
    spec = json.loads(json_spec)
    assert_is_vega_spec(spec)
