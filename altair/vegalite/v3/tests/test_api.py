"""Unit tests for altair API"""

import io
import json
import os
import tempfile

import jsonschema
import pytest
import pandas as pd

import altair.vegalite.v3 as alt

try:
    import selenium
except ImportError:
    selenium = None


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
    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = Chart(data).to_dict()
    assert dct['data'] == data

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = Chart(data).to_dict()
    name = dct['data']['name']
    assert dct['datasets'][name] == data['values']

    # DataFrame data
    data = pd.DataFrame({"x": range(5), "y": range(5)})
    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = Chart(data).to_dict()
    assert dct['data']['values'] == data.to_dict(orient='records')

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = Chart(data).to_dict()
    name = dct['data']['name']
    assert dct['datasets'][name] == data.to_dict(orient='records')

    # Named data object
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


def test_multiple_encodings():
    encoding_dct = [{'field': 'value', 'type': 'quantitative'},
                    {'field': 'name', 'type': 'nominal'}]
    chart1 = alt.Chart('data.csv').mark_point().encode(
        detail=['value:Q', 'name:N'],
        tooltip=['value:Q', 'name:N']
    )

    chart2 = alt.Chart('data.csv').mark_point().encode(
        alt.Detail(['value:Q', 'name:N']),
        alt.Tooltip(['value:Q', 'name:N'])
    )

    chart3 = alt.Chart('data.csv').mark_point().encode(
        [alt.Detail('value:Q'), alt.Detail('name:N')],
        [alt.Tooltip('value:Q'), alt.Tooltip('name:N')]
    )

    for chart in [chart1, chart2, chart3]:
        dct = chart.to_dict()
        assert dct['encoding']['detail'] == encoding_dct
        assert dct['encoding']['tooltip'] == encoding_dct


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
@pytest.mark.skipif('not selenium')
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
        assert content.startswith('<!DOCTYPE html>')


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
    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = chart.to_dict()
    assert 'values' in dct['data']
    assert 'data' not in dct['spec']
    assert dct['facet'] == {'column': {'field': 'column', 'type': 'ordinal'},
                            'row': {'field': 'row', 'type': 'nominal'}}

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = chart.to_dict()
    assert 'datasets' in dct
    assert 'name' in dct['data']
    assert 'data' not in dct['spec']
    assert dct['facet'] == {'column': {'field': 'column', 'type': 'ordinal'},
                            'row': {'field': 'row', 'type': 'nominal'}}


def test_selection():
    # test instantiation of selections
    interval = alt.selection_interval(name='selec_1')
    assert interval.selection.type == 'interval'
    assert interval.name == 'selec_1'

    single = alt.selection_single(name='selec_2')
    assert single.selection.type == 'single'
    assert single.name == 'selec_2'

    multi = alt.selection_multi(name='selec_3')
    assert multi.selection.type == 'multi'
    assert multi.name == 'selec_3'

    # test adding to chart
    chart = alt.Chart().add_selection(single)
    chart = chart.add_selection(multi, interval)
    assert set(chart.selection.keys()) == {'selec_1', 'selec_2', 'selec_3'}

    # test logical operations
    assert isinstance(single & multi, alt.SelectionAnd)
    assert isinstance(single | multi, alt.SelectionOr)
    assert isinstance(~single, alt.SelectionNot)

    # test that default names increment (regression for #1454)
    sel1 = alt.selection_single()
    sel2 = alt.selection_multi()
    sel3 = alt.selection_interval()
    names = {s.name for s in (sel1, sel2, sel3)}
    assert len(names) == 3


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

    # impute transform
    chart = alt.Chart().transform_impute("field", "key", groupby=["x"])
    kwds = {"impute": "field", "key": "key", "groupby": ["x"]}
    assert chart.transform == [alt.ImputeTransform(**kwds)]

    # joinaggregate transform
    chart = alt.Chart().transform_joinaggregate(min='min(x)', groupby=['key'])
    kwds = {
        'joinaggregate': [
            alt.JoinAggregateFieldDef(field='x', op=alt.AggregateOp('min'), **{'as': 'min'})
        ],
        'groupby': ['key']
    }
    assert chart.transform == [
        alt.JoinAggregateTransform(
            joinaggregate=[
                alt.JoinAggregateFieldDef(field='x', op=alt.AggregateOp('min'), **{'as': 'min'})
            ],
            groupby=['key']
        )
    ]

    # filter transform
    chart = alt.Chart().transform_filter("datum.a < 4")
    assert chart.transform == [alt.FilterTransform(filter="datum.a < 4")]

    # flatten transform
    chart = alt.Chart().transform_flatten(['A', 'B'], ['X', 'Y'])
    kwds = {'as': ['X', 'Y'], 'flatten': ['A', 'B']}
    assert chart.transform == [alt.FlattenTransform(**kwds)]

    # fold transform
    chart = alt.Chart().transform_fold(['A', 'B', 'C'], as_=['key', 'val'])
    kwds = {'as': ['key', 'val'], 'fold': ['A', 'B', 'C']}
    assert chart.transform == [alt.FoldTransform(**kwds)]

    # lookup transform
    lookup_data = alt.LookupData(alt.UrlData('foo.csv'), 'id', ['rate'])
    chart = alt.Chart().transform_lookup(from_=lookup_data, as_='a',
                                         lookup='a', default='b')
    kwds = {'from': lookup_data,
            'as': 'a',
            'lookup': 'a',
            'default': 'b'}
    assert chart.transform == [alt.LookupTransform(**kwds)]

    # sample transform
    chart = alt.Chart().transform_sample()
    assert chart.transform == [alt.SampleTransform(1000)]

    # stack transform
    chart = alt.Chart().transform_stack('stacked', 'x', groupby=['y'])
    assert chart.transform == [alt.StackTransform(stack='x', groupby=['y'], **{'as': 'stacked'})]

    # timeUnit transform
    chart = alt.Chart().transform_timeunit("foo", field="x", timeUnit="date")
    kwds = {'as': 'foo', 'field': 'x', 'timeUnit': 'date'}
    assert chart.transform == [alt.TimeUnitTransform(**kwds)]

    # window transform
    chart = alt.Chart().transform_window(xsum='sum(x)', ymin='min(y)',
                                         frame=[None, 0])
    window = [alt.WindowFieldDef(**{'as': 'xsum', 'field': 'x', 'op': 'sum'}),
              alt.WindowFieldDef(**{'as': 'ymin', 'field': 'y', 'op': 'min'})]

    # kwargs don't maintain order in Python < 3.6, so window list can
    # be reversed
    assert (chart.transform == [alt.WindowTransform(frame=[None, 0],
                                                    window=window)]
            or chart.transform == [alt.WindowTransform(frame=[None, 0],
                                                       window=window[::-1])])


def test_filter_transform_selection_predicates():
    selector1 = alt.selection_interval(name='s1')
    selector2 = alt.selection_interval(name='s2')
    base = alt.Chart('data.txt').mark_point()

    chart = base.transform_filter(selector1)
    assert chart.to_dict()['transform'] == [{'filter': {'selection': 's1'}}]

    chart = base.transform_filter(~selector1)
    assert chart.to_dict()['transform'] == [{'filter': {'selection': {'not': 's1'}}}]

    chart = base.transform_filter(selector1 & selector2)
    assert chart.to_dict()['transform'] == [{'filter': {'selection': {'and': ['s1', 's2']}}}]

    chart = base.transform_filter(selector1 | selector2)
    assert chart.to_dict()['transform'] == [{'filter': {'selection': {'or': ['s1', 's2']}}}]



def test_resolve_methods():
    chart = alt.LayerChart().resolve_axis(x='shared', y='independent')
    assert chart.resolve == alt.Resolve(axis=alt.AxisResolveMap(x='shared', y='independent'))

    chart = alt.LayerChart().resolve_legend(color='shared', fill='independent')
    assert chart.resolve == alt.Resolve(legend=alt.LegendResolveMap(color='shared', fill='independent'))

    chart = alt.LayerChart().resolve_scale(x='shared', y='independent')
    assert chart.resolve == alt.Resolve(scale=alt.ScaleResolveMap(x='shared', y='independent'))


def test_add_selection():
    selections = [alt.selection_interval(),
                  alt.selection_single(),
                  alt.selection_multi()]
    chart = alt.Chart().mark_point().add_selection(
        selections[0]
    ).add_selection(
        selections[1],
        selections[2]
    )
    expected = {s.name: s.selection for s in selections}
    assert chart.selection == expected


def test_selection_property():
    sel = alt.selection_interval()
    chart = alt.Chart('data.csv').mark_point().properties(
        selection=sel
    )

    assert list(chart['selection'].keys()) == [sel.name]


def test_LookupData():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    lookup = alt.LookupData(data=df, key='x')

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = lookup.to_dict()
    assert dct['key'] == 'x'
    assert dct['data'] == {'values': [{'x': 1, 'y': 4},
                                      {'x': 2, 'y': 5},
                                      {'x': 3, 'y': 6}]}


def test_themes():
    chart = alt.Chart('foo.txt').mark_point()
    active = alt.themes.active

    try:
        alt.themes.enable('default')
        assert chart.to_dict()['config'] == {"mark": {"tooltip": None},
                                             "view": {"width": 400, "height": 300}}

        alt.themes.enable('opaque')
        assert chart.to_dict()['config'] == {"background": "white",
                                             "mark": {"tooltip": None},
                                             "view": {"width": 400, "height": 300}}

        alt.themes.enable('none')
        assert 'config' not in chart.to_dict()

    finally:
        # re-enable the original active theme
        alt.themes.enable(active)


def test_chart_from_dict():
    base = alt.Chart('data.csv').mark_point().encode(x='x:Q', y='y:Q')

    charts = [base,
              base + base,
              base | base,
              base & base,
              base.facet(row='c:N'),
              base.repeat(row=['c:N', 'd:N'])]

    for chart in charts:
        chart_out = alt.Chart.from_dict(chart.to_dict())
        assert type(chart_out) is type(chart)

    # test that an invalid spec leads to a schema validation error
    with pytest.raises(jsonschema.ValidationError):
        alt.Chart.from_dict({'invalid': 'spec'})


def test_consolidate_datasets(basic_chart):
    chart = basic_chart | basic_chart

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct_consolidated = chart.to_dict()

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct_standard = chart.to_dict()

    assert 'datasets' in dct_consolidated
    assert 'datasets' not in dct_standard

    datasets = dct_consolidated['datasets']

    # two dataset copies should be recognized as duplicates
    assert len(datasets) == 1

    # make sure data matches original & names are correct
    name, data = datasets.popitem()

    for spec in dct_standard['hconcat']:
        assert spec['data']['values'] == data

    for spec in dct_consolidated['hconcat']:
        assert spec['data'] == {'name': name}


def test_consolidate_InlineData():
    data = alt.InlineData(
        values=[{'a': 1, 'b': 1}, {'a': 2, 'b': 2}],
        format={'type': 'csv'}
    )
    chart = alt.Chart(data).mark_point()

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = chart.to_dict()
    assert dct['data']['format'] == data.format
    assert dct['data']['values'] == data.values

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = chart.to_dict()
    assert dct['data']['format'] == data.format
    assert list(dct['datasets'].values())[0] == data.values

    data = alt.InlineData(
        values=[],
        name='runtime_data'
    )
    chart = alt.Chart(data).mark_point()

    with alt.data_transformers.enable(consolidate_datasets=False):
        dct = chart.to_dict()
    assert dct['data'] == data.to_dict()

    with alt.data_transformers.enable(consolidate_datasets=True):
        dct = chart.to_dict()
    assert dct['data'] == data.to_dict()
