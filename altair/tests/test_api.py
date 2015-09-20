import numpy as np
import pandas as pd

from .. import api, spec


VALID_MARKTYPES = spec.SPEC['properties']['marktype']['enum']


def test_empty_data():
    d = api.Data()
    assert d.formatType=='json'
    assert 'formatType' in d
    assert 'url' not in d
    assert 'data' not in d


def test_dict_data():
    data = dict(x=[1, 2, 3],
                y=[4, 5, 6])
    spec = api.Viz(data)
    assert spec.data == data


#def test_dataframe_data():
#    datadict = dict(x=[1, 2, 3],
#                    y=[4, 5, 6])
#    data = pd.DataFrame(datadict)
#    spec = api.Viz(data)
#    assert spec.data == datadict


def test_markers():
    data = dict(x=[1, 2, 3],
                y=[4, 5, 6])

    spec = api.Viz(data)

    # call, e.g. spec.mark('point')
    for marktype in VALID_MARKTYPES:
        spec.mark(marktype)
        assert spec.marktype == marktype
        
    # call, e.g. spec.mark_point()
    for marktype in VALID_MARKTYPES:
        method = 'mark_' + marktype
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
    
