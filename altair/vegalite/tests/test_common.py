"""Tests of functionality that should work in all vegalite versions"""

import pytest

from .. import v1, v2


@pytest.fixture
def basic_spec():
    return {
        'data': {'url': 'data.csv'},
        'mark': 'line',
        'encoding': {
            'color': {'type': 'nominal', 'field': 'color'},
            'x': {'type': 'quantitative', 'field': 'xval'},
            'y': {'type': 'ordinal', 'field': 'yval'}
        },
        'height': 300,
        'width': 400
    }


@pytest.mark.parametrize('alt', [v1, v2])
def test_basic_chart_to_dict(alt, basic_spec):
    chart = alt.Chart('data.csv').mark_line().encode(
        alt.X('xval:Q'),
        y = alt.Y('yval:O'),
        color = 'color:N'
    )
    dct = chart.to_dict()
    assert dct == basic_spec


@pytest.mark.parametrize('alt', [v1, v2])
def test_basic_chart_from_dict(alt, basic_spec):
    chart = alt.Chart.from_dict(basic_spec)
    assert chart.to_dict() == basic_spec
