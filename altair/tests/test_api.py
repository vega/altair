import pytest
import warnings
import json

import numpy as np
import pandas as pd

from .. import *
from ..utils import parse_shorthand, infer_vegalite_type
from ..api import MARK_TYPES
from ..datasets import connection_ok


def test_chart_url_input():
    url = 'http://vega.github.io/vega-lite/data/'
    chart1 = Chart(Data(url=url))
    chart2 = Chart(url)

    assert chart1.to_dict() == chart2.to_dict()

    assert chart1.to_altair() == chart2.to_altair()


def test_encode_update():
    # Test that encode updates rather than overwrites
    chart1 = Chart().encode(x='blah:Q').encode(y='blah:Q')
    chart2 = Chart().encode(x='blah:Q', y='blah:Q')

    assert chart1.to_dict() == chart2.to_dict()


def test_configure_update():
    # Test that configure updates rather than overwrites
    chart1 = Chart().configure(MarkConfig(color='red'))\
                    .configure(background='red')
    chart2 = Chart().configure(MarkConfig(color='red'), background='red')

    assert chart1.to_dict() == chart2.to_dict()


def test_transform_update():
    # Test that transform updates rather than overwrites
    formula = Formula(field='gender', expr='datum.sex == 2 ? "Female":"Male"')
    chart1 = Chart().transform_data(filter='datum.year==2000')\
                    .transform_data(calculate=[formula])

    chart2 = Chart().transform_data(filter='datum.year==2000',
                                    calculate=[formula])

    assert chart1.to_dict() == chart2.to_dict()


def test_from_dict():
    df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
    obj = Chart(df).mark_point().encode(x='x', y='y')
    obj2 = Chart.from_dict(obj.to_dict())
    assert obj.to_dict() == obj2.to_dict()


def test_to_altair():
    df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
    obj = Chart(df).mark_point().encode(x='x', y='y')

    code = obj.to_altair(data='df')
    obj2 = eval(code)

    assert obj.to_dict() == obj2.to_dict()


def test_to_altair_with_methods():
    from ..utils._py3k_compat import PY2
    if PY2:
        code_in = "Chart('http://vega.github.io').mark_point(color=u'red',)"
    else:
        code_in = "Chart('http://vega.github.io').mark_point(color='red',)"
    code_out = eval(code_in).to_altair()
    assert code_in == code_out.replace(' ', '').replace('\n','')


@pytest.mark.skipif(not connection_ok(), reason="No Internet Connection")
def test_to_altair_stocks():
    """Test a more complicated spec for conversion to altair"""
    data = load_dataset('stocks')

    chart = Chart(data).mark_line().encode(
        x='date:T',
        y='price:Q'
    ).transform_data(
        filter="datum.symbol==='GOOG'"
    ).configure(
        mark=MarkConfig(color='red')
    )

    code = chart.to_altair(data='data')
    chart2 = eval(code)

    assert chart.to_dict() == chart2.to_dict()


@pytest.mark.parametrize('mark', MARK_TYPES)
def test_mark_config(mark):
    markmethod = lambda chart: getattr(chart, 'mark_' + mark)
    kwds = dict(color='red', opacity=0.5)

    chart1 = Chart(config=Config(mark=MarkConfig(**kwds)))
    # chart1.mark_circle()
    markmethod(chart1)()
    chart1.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')

    chart2 = Chart()
    # chart2.mark_circle(color='red')
    markmethod(chart2)(**kwds)
    chart2.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')
    
    chart3 = Chart()
    #chart3.mark_circle().configure_mark(**kwargs)
    markmethod(chart3)().configure_mark(**kwds)
    chart3.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')
    
    assert chart1.to_dict() == chart2.to_dict()
    assert chart2.to_dict() == chart3.to_dict()


_config_method_params = [
    {'name': 'axis',
     'class': AxisConfig,
     'kwds': dict(axisWidth=1.0, grid=False)
    },
    {'name': 'cell',
     'class': CellConfig,
     'kwds': dict(clip=False, fillOpacity=0.5)
    },
    {'name': 'legend',
     'class': LegendConfig,
     'kwds': dict(orient=u'foo', shortTimeLabels=True)
    },
    {'name': 'scale',
     'class': ScaleConfig,
     'kwds': dict(pointSizeRange=[1.0, 2.0], round=False)
    },
]

@pytest.mark.parametrize('params', _config_method_params)
def test_config_methods(params):
    kwds = params['kwds']
    klass = params['class']
    name = params['name']
    configmethod = lambda chart: getattr(chart, 'configure_'+name)

    chart1 = Chart(config=Config( **{name:klass(**kwds)} ))
    chart2 = Chart().configure( **{name:klass(**kwds)} )
    chart3 = configmethod(Chart())(**kwds)

    assert chart1.to_dict() == chart2.to_dict()
    assert chart2.to_dict() == chart3.to_dict()


def test_config_facet_grid():
    
    kwds = dict(opacity=0.5, color='red')
    
    chart1 = Chart(
        config=Config(
            facet=FacetConfig(grid=FacetGridConfig(**kwds))
        )
    )
    chart2 = Chart().configure_facet_grid(**kwds)

    assert chart1.to_dict() == chart2.to_dict()

