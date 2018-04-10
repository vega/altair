"""Unit tests for altair API"""

import io
import json
import os
import tempfile

import pytest
import pandas as pd

import altair.vegalite.v2 as alt


@pytest.fixture
def basic_chart():
    data = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })

    return alt.Chart(data).mark_bar().encode(
        x='a',
        y='b'
    )


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

    def _check_encodings(chart):
        dct = chart.to_dict()
        assert dct['encoding']['x']['type'] == 'temporal'
        assert dct['encoding']['x']['field'] == 'x'
        assert dct['encoding']['y']['type'] == 'quantitative'
        assert dct['encoding']['y']['field'] == 'y'
        assert dct['encoding']['color']['type'] == 'nominal'
        assert dct['encoding']['color']['field'] == 'c'

    # Pass field names by keyword
    chart = alt.Chart(data).mark_point().encode(x='x', y='y', color='c')
    _check_encodings(chart)

    # pass Channel objects by keyword
    chart = alt.Chart(data).mark_point().encode(x=alt.X('x'), y=alt.Y('y'),
                                                color=alt.Color('c'))
    _check_encodings(chart)

    # pass Channel objects by value
    chart = alt.Chart(data).mark_point().encode(alt.X('x'), alt.Y('y'),
                                                alt.Color('c'))
    _check_encodings(chart)

    # override default types
    chart = alt.Chart(data).mark_point().encode(alt.X('x', type='nominal'),
                                                alt.Y('y', type='ordinal'))
    dct = chart.to_dict()
    assert dct['encoding']['x']['type'] == 'nominal'
    assert dct['encoding']['y']['type'] == 'ordinal'


def test_chart_operations():
    data = pd.DataFrame({'x': pd.date_range('2012', periods=10, freq='Y'),
                         'y': range(10),
                         'c': list('abcabcabca')})
    chart1 = alt.Chart(data).mark_line().encode(x='x', y='y', color='c')
    chart2 = chart1.mark_point()
    chart3 = chart1.mark_circle()
    chart4 = chart1.mark_square()

    chart = chart1 + chart2 + chart3
    assert isinstance(chart, alt.LayerChart)
    assert len(chart.layer) == 3
    chart += chart4
    assert len(chart.layer) == 4

    chart = chart1 | chart2 | chart3
    assert isinstance(chart, alt.HConcatChart)
    assert len(chart.hconcat) == 3
    chart |= chart4
    assert len(chart.hconcat) == 4

    chart = chart1 & chart2 & chart3
    assert isinstance(chart, alt.VConcatChart)
    assert len(chart.vconcat) == 3
    chart &= chart4
    assert len(chart.vconcat) == 4


def test_selection_to_dict():
    brush = alt.selection(type='interval')

    # test some value selections
    # Note: X and Y cannot have conditions
    alt.Chart('path/to/data.json').mark_point().encode(
        color=alt.condition(brush, alt.ColorValue('red'), alt.ColorValue('blue')),
        opacity=alt.condition(brush, alt.value(0.5), alt.value(1.0)),
        text=alt.condition(brush, alt.TextValue('foo'), alt.value('bar'))
    ).to_dict()

    # test some field selections
    # Note: X and Y cannot have conditions
    # Conditions cannot both be fields
    alt.Chart('path/to/data.json').mark_point().encode(
        color=alt.condition(brush, alt.Color('col1:N'), alt.value('blue')),
        opacity=alt.condition(brush, 'col1:N', alt.value(0.5)),
        text=alt.condition(brush, alt.value('abc'), alt.Text('col2:N')),
        size=alt.condition(brush, alt.value(20), 'col2:N')
    ).to_dict()


@pytest.mark.parametrize('format', ['html', 'json', 'png', 'svg'])
def test_save(format, basic_chart):
    if format in ['html', 'json', 'svg']:
        out = io.StringIO()
        mode = 'r'
    else:
        out = io.BytesIO()
        mode = 'rb'
    fid, filename = tempfile.mkstemp(suffix='.' + format)

    try:
        try:
            basic_chart.save(out, format=format)
            basic_chart.save(filename)
        except ImportError as err:
            if 'selenium' in str(err) or 'chromedriver' in str(err):
                pytest.skip("selenium installation required for png/svg export")
            else:
                raise
        except ValueError as err:
            if str(err).startswith('Internet connection'):
                pytest.skip("web connection required for png/svg export")
            else:
                raise

        out.seek(0)
        with open(filename, mode) as f:
            assert f.read() == out.read()
    finally:
        os.remove(filename)

    out.seek(0)

    if format == 'json':
        spec = json.load(out)
        assert '$schema' in spec

    elif format == 'html':
        content = out.read()
        assert content.startswith('\n<!DOCTYPE html>')


def test_facet_parse():
    chart = alt.Chart('data.csv').mark_point().encode(
        x='x:Q',
        y='y:Q'
    ).facet(
        row='row:N',
        column='column:O'
    )
    dct = chart.to_dict()
    assert dct['data'] == {'url': 'data.csv'}
    assert 'data' not in dct['spec']
    assert dct['facet'] == {'column': {'field': 'column', 'type': 'ordinal'},
                            'row': {'field': 'row', 'type': 'nominal'}}


def test_facet_parse_data():
    data = pd.DataFrame({'x': range(5), 'y': range(5), 'row': list('abcab')})
    chart = alt.Chart(data).mark_point().encode(
        x='x',
        y='y:O'
    ).facet(
        row='row',
        column='column:O'
    )
    dct = chart.to_dict()
    assert 'values' in dct['data']
    assert 'data' not in dct['spec']
    assert dct['facet'] == {'column': {'field': 'column', 'type': 'ordinal'},
                            'row': {'field': 'row', 'type': 'nominal'}}


def test_SelectionMapping():
    # test instantiation of selections
    interval = alt.selection_interval(name='selec_1')
    assert interval['selec_1'].type == 'interval'
    assert interval._get_name() == 'selec_1'

    single = alt.selection_single(name='selec_2')
    assert single['selec_2'].type == 'single'
    assert single._get_name() == 'selec_2'

    multi = alt.selection_multi(name='selec_3')
    assert multi['selec_3'].type == 'multi'
    assert multi._get_name() == 'selec_3'

    # test addition
    x = single + multi + interval
    assert x.to_dict().keys() == {'selec_1', 'selec_2', 'selec_3'}

    y = single.copy()
    y += multi
    y += interval
    assert x.to_dict() == y.to_dict()

    # test logical operations
    x = single & multi
    assert isinstance(x, alt.SelectionAnd)

    y = single | multi
    assert isinstance(y, alt.SelectionOr)


def test_transforms():
    # aggregate transform
    agg1 = alt.AggregatedFieldDef(**{'as': 'x1', 'op': 'mean', 'field': 'y'})
    agg2 = alt.AggregatedFieldDef(**{'as': 'x2', 'op': 'median', 'field': 'z'})
    chart = alt.Chart().transform_aggregate([agg1], ['foo'], x2='median(z)')
    kwds = dict(aggregate=[agg1, agg2], groupby=['foo'])
    assert chart.transform == [alt.AggregateTransform(**kwds)]

    # bin transform
    chart = alt.Chart().transform_bin("binned", field="field", bin=True)
    kwds = {'as': 'binned', 'field': 'field', 'bin': True}
    assert chart.transform == [alt.BinTransform(**kwds)]

    # calcualte transform
    chart = alt.Chart().transform_calculate("calc", "datum.a * 4")
    kwds = {'as': 'calc', 'calculate': 'datum.a * 4'}
    assert chart.transform == [alt.CalculateTransform(**kwds)]

    # filter transform
    chart = alt.Chart().transform_filter("datum.a < 4")
    assert chart.transform == [alt.FilterTransform(filter="datum.a < 4")]

    # lookup transform
    lookup_data = alt.LookupData(alt.UrlData('foo.csv'), 'id', ['rate'])
    chart = alt.Chart().transform_lookup(from_=lookup_data, as_='a',
                                         lookup='a', default='b')
    kwds = {'from': lookup_data,
            'as': 'a',
            'lookup': 'a',
            'default': 'b'}
    assert chart.transform == [alt.LookupTransform(**kwds)]

    # timeUnit transform
    chart = alt.Chart().transform_timeunit("foo", field="x", timeUnit="date")
    kwds = {'as': 'foo', 'field': 'x', 'timeUnit': 'date'}
    assert chart.transform == [alt.TimeUnitTransform(**kwds)]


def test_resolve_methods():
    chart = alt.LayerChart().resolve_axis(x='shared', y='independent')
    assert chart.resolve == alt.Resolve(axis=alt.AxisResolveMap(x='shared', y='independent'))

    chart = alt.LayerChart().resolve_legend(color='shared', fill='independent')
    assert chart.resolve == alt.Resolve(legend=alt.LegendResolveMap(color='shared', fill='independent'))

    chart = alt.LayerChart().resolve_scale(x='shared', y='independent')
    assert chart.resolve == alt.Resolve(scale=alt.ScaleResolveMap(x='shared', y='independent'))

    with pytest.raises(ValueError) as err:
        alt.Chart().resolve_axis(x='shared')
    assert str(err.value).endswith("object has no attribute 'resolve'")


def test_LookupData():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    lookup = alt.LookupData(data=df, key='x')
    dct = lookup.to_dict()
    assert dct['key'] == 'x'
    assert dct['data'] == {'values': [{'x': 1, 'y': 4},
                                      {'x': 2, 'y': 5},
                                      {'x': 3, 'y': 6}]}


def test_themes():
    chart = alt.Chart('foo.txt').mark_point()
    active = alt.theme.active

    try:
        alt.theme.enable('default')
        assert chart.to_dict()['config'] == {"view": {"width": 400, "height": 300}}

        alt.theme.enable('opaque')
        assert chart.to_dict()['config'] == {"background": "white",
                                             "view": {"width": 400, "height": 300}}

        alt.theme.enable('none')
        assert 'config' not in chart.to_dict()

    finally:
        # re-enable the original active theme
        alt.theme.enable(active)
