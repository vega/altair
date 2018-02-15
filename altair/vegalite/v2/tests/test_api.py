"""Unit tests for altair API"""

import pytest
import pandas as pd

from altair.vegalite.v2 import api as alt


def test_chart_data_types():
    Chart = lambda data: alt.Chart(data).mark_point().encode(x='x:Q', y='y:Q')

    # Url Data
    data = '/path/to/my/data.csv'
    dct = Chart(data).to_dict()
    assert dct['data'] == {'url': data}

    # Dict Data
    data = {"values": [{"x": 1, "y": 2}, {"x": 2, "y": 3}]}
    dct = Chart(data).to_dict()
    assert dct['data'] == data

    # DataFrame data
    data = pd.DataFrame({"x": range(5), "y": range(5)})
    dct = Chart(data).to_dict()
    assert dct['data']['values'] == data.to_dict(orient='records')

    # Altair data object
    data = alt.NamedData(name='Foo')
    dct = Chart(data).to_dict()
    assert dct['data'] == {'name': 'Foo'}


def test_chart_infer_types():
    data = pd.DataFrame({'x': pd.date_range('2012', periods=10, freq='Y'),
                         'y': range(10),
                         'c': list('abcabcabca')})

    chart = alt.Chart(data).mark_point().encode(x='x', y='y', color='c')
    dct = chart.to_dict()
    assert dct['encoding']['x']['type'] == 'temporal'
    assert dct['encoding']['x']['field'] == 'x'
    assert dct['encoding']['y']['type'] == 'quantitative'
    assert dct['encoding']['y']['field'] == 'y'
    assert dct['encoding']['color']['type'] == 'nominal'
    assert dct['encoding']['color']['field'] == 'c'

    chart = alt.Chart(data).mark_point().encode(x=alt.X('x'), y=alt.Y('y'),
                                                color=alt.Color('c'))
    dct = chart.to_dict()
    assert dct['encoding']['x']['type'] == 'temporal'
    assert dct['encoding']['x']['field'] == 'x'
    assert dct['encoding']['y']['type'] == 'quantitative'
    assert dct['encoding']['y']['field'] == 'y'
    assert dct['encoding']['color']['type'] == 'nominal'
    assert dct['encoding']['color']['field'] == 'c'

    chart = alt.Chart(data).mark_point().encode(alt.X('x'), alt.Y('y'),
                                                alt.Color('c'))
    dct = chart.to_dict()
    assert dct['encoding']['x']['type'] == 'temporal'
    assert dct['encoding']['x']['field'] == 'x'
    assert dct['encoding']['y']['type'] == 'quantitative'
    assert dct['encoding']['y']['field'] == 'y'
    assert dct['encoding']['color']['type'] == 'nominal'
    assert dct['encoding']['color']['field'] == 'c'
