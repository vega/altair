import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from traitlets import TraitError

from altair import api

from .. import api, spec


VALID_MARKTYPES = spec.SPEC['properties']['marktype']['enum']

def build_simple_spec():
    data = dict(x=[1, 2, 3],
                y=[4, 5, 6])
    return api.Viz(data), data


def test_empty_data():
    d = api.Data()
    assert d.formatType=='json'
    assert 'formatType' in d
    assert 'url' not in d
    assert 'values' not in d


def test_dict_data():
    spec, data = build_simple_spec()
    assert np.all(spec.data == pd.DataFrame(data))


def test_dataframe_data():
    spec, data = build_simple_spec()
    data = data = pd.DataFrame(data)
    spec = api.Viz(data)
    assert np.all(spec.data == data)


def test_to_dict():
    data = pd.DataFrame({'x': [1, 2, 3],
                         'y': [4, 5, 6]})
    spec = api.Viz(data).encode(x='x', y='y')

    D = spec.to_dict()

    assert D == {'config': {'gridColor': 'black',
                            'gridOpacity': 0.08,
                            'height': 400,
                            'width': 600},
                 'data': {'formatType': 'json',
                          'values': [{'x': 1, 'y': 4},
                                     {'x': 2, 'y': 5},
                                     {'x': 3, 'y': 6}]},
                 'encoding': {'x': {'bin': False, 'name': 'x', 'type': 'Q'},
                              'y': {'bin': False, 'name': 'y', 'type': 'Q'}},
                 'marktype': 'point'}


def test_vl_spec_for_scale_defaults():
    """Check that defaults are according to spec"""

    # This scale object is the property used for X, Y, Size
    scale = api.Scale()
    assert scale.type == 'linear'
    assert scale.reverse == False
    assert scale.zero == True
    assert scale.nice is None
    assert scale.useRawDomain is None

    # Scale object for property in Color
    scale = api.ColorScale()
    assert scale.type == 'linear'
    assert scale.reverse == False
    assert scale.zero == True
    assert scale.nice is None
    assert scale.useRawDomain is None
    assert scale.range is None
    assert scale.c10palette == 'category10'
    assert scale.c20palette == 'category20'
    assert scale.ordinalPalette == 'BuGn'


def test_vl_spec_for_scale_changes():
    """Check that changes are possible and sticky"""

    # This scale object is the property used for X, Y, Size
    scale = api.Scale(type='log', reverse=True, zero=False, nice='second', useRawDomain=True)
    assert scale.type == 'log'
    assert scale.reverse == True
    assert scale.zero == False
    assert scale.nice == 'second'
    assert scale.useRawDomain == True

    scale.type = 'linear'
    scale.reverse = False
    scale.zero = True
    scale.nice = None
    scale.useRawDomain = None
    assert scale.type == 'linear'
    assert scale.reverse == False
    assert scale.zero == True
    assert scale.nice is None
    assert scale.useRawDomain is None

    # Scale object for property in Color
    scale = api.ColorScale(type='log', reverse=True, zero=False, nice='second', useRawDomain=True,
                           range='category10', c10palette='Set1', c20palette='category20c', ordinalPalette='Spectral')
    assert scale.type == 'log'
    assert scale.reverse == True
    assert scale.zero == False
    assert scale.nice == 'second'
    assert scale.useRawDomain == True
    assert scale.range == 'category10'
    assert scale.c10palette == 'Set1'
    assert scale.c20palette == 'category20c'
    assert scale.ordinalPalette == 'Spectral'

    scale.range = ['category10']
    scale.c10palette = 'Set3'
    scale.c20palette = 'category20b'
    scale.ordinalPalette = 'Dark2'
    assert scale.range == ['category10']
    assert scale.c10palette == 'Set3'
    assert scale.c20palette == 'category20b'
    assert scale.ordinalPalette == 'Dark2'


def test_vl_spec_for_font_defaults():
    """Check that defaults are according to spec"""
    font = api.Font()
    assert font.weight == 'normal'
    assert font.size == 10
    assert font.family == 'Helvetica Neue'
    assert font.style == 'normal'


def test_vl_spec_for_font_changes():
    """Check that changes are possible and sticky"""
    font = api.Font(weight='bold', size=15, family='Serif', style='italic')
    assert font.weight == 'bold'
    assert font.size == 15
    assert font.family == 'Serif'
    assert font.style == 'italic'


def test_vl_spec_for_text_defaults():
    """Check that defaults are according to spec"""

    text = api.Text('foobar')
    assert text.name == 'foobar'
    assert text.type is None
    assert text.timeUnit is None
    assert text.bin is False
    assert text.sort == []
    assert text.aggregate is None
    assert text.scale is None
    assert text.align == 'right'
    assert text.baseline == 'middle'
    assert text.color == '#000000'
    assert text.margin == 4
    assert text.placeholder == 'Abc'
    assert text.font is None
    assert text.format is None

    text = api.Text('foobar:O')
    assert text.name == 'foobar'
    assert text.type == 'O'
    assert text.timeUnit is None
    assert text.bin is False
    assert text.sort == []
    assert text.aggregate is None
    assert text.scale is None
    assert text.align == 'right'
    assert text.baseline == 'middle'
    assert text.color == '#000000'
    assert text.margin == 4
    assert text.placeholder == 'Abc'
    assert text.font is None
    assert text.format is None

    text = api.Text('sum(foobar):O')
    assert text.name == 'foobar'
    assert text.type == 'O'
    assert text.timeUnit is None
    assert text.bin is False
    assert text.sort == []
    assert text.aggregate == 'sum'
    assert text.scale is None
    assert text.align == 'right'
    assert text.baseline == 'middle'
    assert text.color == '#000000'
    assert text.margin == 4
    assert text.placeholder == 'Abc'
    assert text.font is None
    assert text.format is None


def test_vl_spec_for_text_changes():
    """Check that changes are possible and sticky"""
    text = api.Text('foobar', type='O', timeUnit='minutes', bin=api.Bin(), sort=[api.SortItems()], aggregate='avg',
                    scale=api.Scale(), align='left', baseline='top', color='#111111', margin=3, placeholder = 'Aaa',
                    font=api.Font(), format='format')
    assert text.name == 'foobar'
    assert text.type == 'O'
    assert text.timeUnit == 'minutes'
    assert text.bin.to_dict() == api.Bin().to_dict()
    assert text.sort[0].to_dict() == api.SortItems().to_dict()
    assert text.aggregate == 'avg'
    assert text.scale.to_dict() == api.Scale().to_dict()
    assert text.align == 'left'
    assert text.baseline == 'top'
    assert text.color == '#111111'
    assert text.margin == 3
    assert text.placeholder == 'Aaa'
    assert text.font.to_dict() == api.Font().to_dict()
    assert text.format == 'format'

    text.shorthand = 'sum(foobar):Q'
    assert text.name == 'foobar'
    assert text.type == 'Q'
    assert text.timeUnit == 'minutes'
    assert text.bin.to_dict() == api.Bin().to_dict()
    assert text.sort[0].to_dict() == api.SortItems().to_dict()
    assert text.aggregate == 'sum'
    assert text.scale.to_dict() == api.Scale().to_dict()
    assert text.align == 'left'
    assert text.baseline == 'top'
    assert text.color == '#111111'
    assert text.margin == 3
    assert text.placeholder == 'Aaa'
    assert text.font.to_dict() == api.Font().to_dict()
    assert text.format == 'format'


def test_vl_spec_for_text_edge_values():
    """Check edge values"""
    text = api.Text('foobar')
    try:
        text.margin = -1
        raise Exception('Should have thrown for illegal margin min value.')
    except TraitError:
        pass


def test_markers():
    spec, data = build_simple_spec()

    # call, e.g. spec.mark('point')
    for marktype in VALID_MARKTYPES:
        spec.mark(marktype)
        assert spec.marktype == marktype

    # call, e.g. spec.point()
    for marktype in VALID_MARKTYPES:
        method = marktype
        getattr(spec, method)()
        assert spec.marktype == marktype

def test_encode():
    data = dict(col1=[1.0, 2.0, 3.0],
                col2=[0.1, 0.2, 0.3],
                col3=['A', 'B', 'C'],
                col4=[True, False, True],
                col5=[0.1, 0.2, 0.3],
                col6=pd.date_range('2012', periods=3, freq='A'),
                col7=np.arange(3))
    kwargs = dict(x='col1', y='col2', row='col3', col='col4',
                  size='col5', color='col6', shape='col7')

    spec = api.Viz(data).encode(**kwargs)
    for key, name in kwargs.items():
        assert getattr(spec.encoding, key).name == name


def test_encode_aggregates():
    data = dict(col1=[1.0, 2.0, 3.0],
                col2=[0.1, 0.2, 0.3],
                col3=['A', 'B', 'C'],
                col4=[True, False, True],
                col5=[0.1, 0.2, 0.3],
                col6=pd.date_range('2012', periods=3, freq='A'),
                col7=np.arange(3))
    kwargs = dict(x=('count', 'col1'), y=('count', 'col2'),
                  row=('count', 'col3'), col=('count', 'col4'),
                  size=('avg', 'col5'), color=('max', 'col6'),
                  shape=('count', 'col7'))

    spec = api.Viz(data).encode(**{key:"{0}({1})".format(*val)
                                   for key, val in kwargs.items()})
    for key, val in kwargs.items():
        agg, name = val
        assert getattr(spec.encoding, key).name == name
        assert getattr(spec.encoding, key).aggregate == agg


def test_encode_types():
    data = dict(col1=[1.0, 2.0, 3.0],
                col2=[0.1, 0.2, 0.3],
                col3=['A', 'B', 'C'],
                col4=[True, False, True],
                col5=[0.1, 0.2, 0.3],
                col6=pd.date_range('2012', periods=3, freq='A'),
                col7=np.arange(3))
    kwargs = dict(x=('col1', 'Q'), y=('col2', 'Q'),
                  row=('col3', 'O'), col=('col4', 'N'),
                  size=('col5', 'Q'), color=('col6', 'T'),
                  shape=('col7', 'O'))

    spec = api.Viz(data).encode(**{key:"{0}:{1}".format(*val)
                                   for key, val in kwargs.items()})
    for key, val in kwargs.items():
        name, typ = val
        assert getattr(spec.encoding, key).name == name
        assert getattr(spec.encoding, key).type == typ

def test_infer_types():
    data = dict(col1=[1.0, 2.0, 3.0],
                col2=[0.1, 0.2, 0.3],
                col3=['A', 'B', 'C'],
                col4=[True, False, True],
                col5=[0.1, 0.2, 0.3],
                col6=pd.date_range('2012', periods=3, freq='A'),
                col7=np.arange(3))
    kwargs = dict(x=('col1', 'Q'), y=('col2', 'Q'),
                  row=('col3', 'N'), col=('col4', 'N'),
                  size=('col5', 'Q'), color=('col6', 'T'),
                  shape=('col7', 'Q'))

    spec = api.Viz(data).encode(**{key: val[0]
                                   for key, val in kwargs.items()})
    for key, val in kwargs.items():
        name, typ = val
        assert getattr(spec.encoding, key).name == name
        assert getattr(spec.encoding, key).type == typ


def test_configure():
  spec, data = build_simple_spec()
  spec.configure(height=100, width=200)
  res = spec.to_dict()
  assert res['config']['height'] == 100
  assert res['config']['width'] == 200


def test_single_dim_setting():
    spec, data = build_simple_spec()
    spec.encode(x="x:N", y="y:Q").set_single_dims(100, 100)
    res = spec.to_dict()

    assert res['config']['width'] == 100
    assert res['config']['height'] == 100
    assert res['config']['singleWidth'] == 75
    assert res['config']['singleHeight'] == 75

    assert res['encoding']['x']['band']['size'] == 10
    assert res['encoding']['y'].get('band') is None


def test_hist():
    data = dict(x=[1, 2, 3],
                y=[4, 5, 6])

    viz1 = api.Viz(data).hist(x='x')
    assert viz1.encoding.x.name == "x"
    assert viz1.encoding.x.bin.maxbins == 10
    assert viz1.encoding.y.name == "x"
    assert viz1.encoding.y.type == "Q"
    assert viz1.encoding.y.aggregate == "count"

    viz2 = api.Viz(data).hist(x="x", bins=30)
    assert viz2.encoding.x.bin.maxbins == 30
    expected = {'config': {'gridColor': 'black',
                           'gridOpacity': 0.08,
                           'height': 400,
                           'width': 600},
                'data': {'formatType': 'json',
                         'values': [{'x': 1, 'y': 4},
                                    {'x': 2, 'y': 5},
                                    {'x': 3, 'y': 6}]},
                'encoding': {'x': {'bin': {'maxbins': 30},
                                   'name': 'x',
                                   'type': 'Q'},
                             'y': {'aggregate': 'count',
                                   'bin': False,
                                   'name': 'x',
                                   'type': 'Q'}},
                 'marktype': 'bar'}

    assert viz2.to_dict() == expected

    viz3 = api.Viz(data).hist(x="x:O",
        color=api.Color(shorthand="bar", type="N")
    )
    assert viz3.encoding.x.name == "x"
    assert viz3.encoding.x.type == "O"

    expected = {'config': {'gridColor': 'black',
                           'gridOpacity': 0.08,
                           'height': 400,
                           'width': 600},
                'data': {'formatType': 'json',
                'values': [{'x': 1, 'y': 4}, {'x': 2, 'y': 5},
                           {'x': 3, 'y': 6}]},
                'encoding': {'x': {'bin': {'maxbins': 10},
                                   'name': 'x', 'type': 'O'},
                             'y': {'aggregate': 'count',
                                   'bin': False,
                                   'name': 'x',
                                   'type': 'Q'},
                             'color': {'bin': False,
                                       'name': 'bar',
                                       'opacity': 1.0,
                                       'type': 'N',
                                       'value': '#4682b4',
                                       'legend': True}},
                'marktype': 'bar'}


    assert viz3.to_dict() == expected

    viz4 = api.Viz(data).hist(
        x=api.X(shorthand="x", bin=api.Bin(maxbins=40)))
    assert viz4.encoding.x.name == "x"
    assert viz4.encoding.x.bin.maxbins == 40
