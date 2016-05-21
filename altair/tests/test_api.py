import pytest
import warnings

import numpy as np
import pandas as pd

from .. import Layer, Formula, MarkConfig, Encoding
from ..utils import parse_shorthand, infer_vegalite_type


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

    from altair import Encoding, X, Y
    code = obj.to_altair(data='df')
    obj2 = eval(code)

    assert obj.to_dict() == obj2.to_dict()
