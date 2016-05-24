import pytest
import warnings
import json

import numpy as np
import pandas as pd

from .. import *
from ..utils import parse_shorthand, infer_vegalite_type
from ..api import MARK_TYPES
from ..datasets import connection_ok


def test_encode_update():
    # Test that encode updates rather than overwrites
    layer1 = Layer().encode(x='blah:Q').encode(y='blah:Q')
    layer2 = Layer().encode(x='blah:Q', y='blah:Q')

    assert layer1.to_dict() == layer2.to_dict()


def test_configure_update():
    # Test that configure updates rather than overwrites
    layer1 = Layer().configure(MarkConfig(color='red'))\
                    .configure(background='red')
    layer2 = Layer().configure(MarkConfig(color='red'), background='red')

    assert layer1.to_dict() == layer2.to_dict()


def test_transform_update():
    # Test that transform updates rather than overwrites
    formula = Formula(field='gender', expr='datum.sex == 2 ? "Female":"Male"')
    layer1 = Layer().transform_data(filter='datum.year==2000')\
                    .transform_data(calculate=[formula])

    layer2 = Layer().transform_data(filter='datum.year==2000',
                                    calculate=[formula])

    assert layer1.to_dict() == layer2.to_dict()


def test_from_dict():
    df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
    obj = Layer(df).mark_point().encode(x='x', y='y')
    obj2 = Layer.from_dict(obj.to_dict())
    assert obj.to_dict() == obj2.to_dict()


def test_to_altair():
    df = pd.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
    obj = Layer(df).mark_point().encode(x='x', y='y')

    code = obj.to_altair(data='df')
    obj2 = eval(code)

    assert obj.to_dict() == obj2.to_dict()


@pytest.mark.skipif(not connection_ok(), reason="No Internet Connection")
def test_to_altair_stocks():
    """Test a more complicated spec for conversion to altair"""
    data = load_dataset('stocks')

    layer = Layer(data).mark_line().encode(
        x='date:T',
        y='price:Q'
    ).transform_data(
        filter="datum.symbol==='GOOG'"
    ).configure(
        mark=MarkConfig(color='red')
    )

    code = layer.to_altair(data='data')
    layer2 = eval(code)

    assert layer.to_dict() == layer2.to_dict()


@pytest.mark.parametrize('mark', MARK_TYPES)
def test_mark_config(mark):
    markmethod = lambda layer: getattr(layer, 'mark_' + mark)
    kwds = dict(color='red', opacity=0.5)

    layer1 = Layer(config=Config(mark=MarkConfig(**kwds)))
    # layer1.mark_circle()
    markmethod(layer1)()
    layer1.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')

    layer2 = Layer()
    # layer2.mark_circle(color='red')
    markmethod(layer2)(**kwds)
    layer2.encode(x='Horsepower:Q', y='Miles_per_gallon:Q')

    assert layer1.to_dict() == layer2.to_dict()
