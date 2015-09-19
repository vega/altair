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
    
