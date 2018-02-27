"""Tests of functionality that should work in all vegalite versions"""

import pytest

from .. import v1, v2

v1_defaults = {
    'width': 400,
    'height': 300
}

v2_defaults = {
    'config': {
        'view':{
            'height':300,
            'width':400
        }
    }
}

basic_spec = {
    'data': {'url': 'data.csv'},
    'mark': 'line',
    'encoding': {
        'color': {'type': 'nominal', 'field': 'color'},
        'x': {'type': 'quantitative', 'field': 'xval'},
        'y': {'type': 'ordinal', 'field': 'yval'}
    },
}

spec_v1 = dict(v1_defaults, **basic_spec)
spec_v2 = dict(v2_defaults, **basic_spec)


@pytest.mark.parametrize('alt,basic_spec', [(v1, spec_v1), (v2, spec_v2)])
def test_basic_chart_to_dict(alt, basic_spec):
    chart = alt.Chart('data.csv').mark_line().encode(
        alt.X('xval:Q'),
        y = alt.Y('yval:O'),
        color = 'color:N'
    )
    dct = chart.to_dict()

    # schema should be in the top level
    assert dct.pop('$schema').startswith('http')

    # remainder of spec should match the basic spec
    assert dct == basic_spec


@pytest.mark.parametrize('alt,basic_spec', [(v1, spec_v1), (v2, spec_v2)])
def test_basic_chart_from_dict(alt, basic_spec):
    chart = alt.Chart.from_dict(basic_spec)
    dct = chart.to_dict()

    # schema should be in the top level
    assert dct.pop('$schema').startswith('http')

    # remainder of spec should match the basic spec
    assert dct == basic_spec
