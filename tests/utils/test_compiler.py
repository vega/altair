import json

import pytest

from altair import Chart, vegalite_compilers
from tests import skip_requires_vl_convert


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


@skip_requires_vl_convert
def test_vegalite_compiler(chart):
    vegalite_spec = chart.to_dict()
    fn = vegalite_compilers.get()
    assert fn is not None
    vega_spec = fn(vegalite_spec)
    assert_is_vega_spec(vega_spec)


@skip_requires_vl_convert
def test_to_dict_with_format_vega(chart):
    vega_spec = chart.to_dict(format="vega")
    assert_is_vega_spec(vega_spec)


@skip_requires_vl_convert
def test_to_json_with_format_vega(chart):
    json_spec = chart.to_json(format="vega")
    assert isinstance(json_spec, str)
    spec = json.loads(json_spec)
    assert_is_vega_spec(spec)
