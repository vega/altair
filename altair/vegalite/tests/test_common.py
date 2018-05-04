"""Tests of functionality that should work in all vegalite versions"""

import pytest

import pandas as pd

from .. import v1, v2

v1_defaults = {
    'width': 400,
    'height': 300
}

v2_defaults = {
    'config': {
        'view': {
            'height': 300,
            'width': 400
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


def make_basic_chart(alt):
    data = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })

    return alt.Chart(data).mark_bar().encode(
        x='a',
        y='b'
    )


spec_v1 = dict(v1_defaults, **basic_spec)
spec_v2 = dict(v2_defaults, **basic_spec)


@pytest.mark.parametrize('alt,basic_spec', [(v1, spec_v1), (v2, spec_v2)])
def test_basic_chart_to_dict(alt, basic_spec):
    chart = alt.Chart('data.csv').mark_line().encode(
        alt.X('xval:Q'),
        y=alt.Y('yval:O'),
        color='color:N'
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


@pytest.mark.parametrize('alt', [v1, v2])
def test_theme_enable(alt):
    active_theme = alt.themes.active

    try:
        alt.themes.enable('none')

        chart = alt.Chart.from_dict(basic_spec)
        dct = chart.to_dict()

        # schema should be in the top level
        assert dct.pop('$schema').startswith('http')

        # remainder of spec should match the basic spec
        # without any theme settings
        assert dct == basic_spec
    finally:
        # reset the theme to its initial value
        alt.themes.enable(active_theme)


@pytest.mark.parametrize('alt', [v1, v2])
def test_max_rows(alt):
    basic_chart = make_basic_chart(alt)

    with alt.data_transformers.enable('default'):
        basic_chart.to_dict()  # this should not fail

    with alt.data_transformers.enable('default', max_rows=5):
        print(alt.data_transformers.options)
        with pytest.raises(alt.MaxRowsError):
            basic_chart.to_dict()  # this should not fail
