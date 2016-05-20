import pytest
import warnings

import numpy as np
import pandas as pd

from .. import Layer, Formula, MarkConfig
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
    layer1 = Layer().data_transform(filter='datum.year==2000')\
                    .data_transform(calculate=[formula])

    layer2 = Layer().data_transform(filter='datum.year==2000',
                                    calculate=[formula])

    assert layer1.to_dict() == layer2.to_dict()
