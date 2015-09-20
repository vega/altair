import pytest
import warnings

import numpy as np
import pandas as pd

from ..utils import parse_shorthand, infer_vegalite_type


def test_parse_shorthand():
    def check(s, **kwargs):
        assert parse_shorthand(s) == kwargs

    check('')
    check('foobar', name='foobar')
    check('foobar:nominal', type='N', name='foobar')
    check('foobar:O', type='O', name='foobar')
    check('avg(foobar)', name='foobar', aggregate='avg')
    check('min(foobar):time', type='T', name='foobar', aggregate='min')
    check('sum(foobar):Q', type='Q', name='foobar', aggregate='sum')


def test_infer_vegalite_type():
    def _check(arr, typ):
        assert infer_vegalite_type(arr) == typ

    _check(np.arange(5, dtype=float), 'Q')
    _check(np.arange(5, dtype=int), 'Q')
    _check(np.zeros(5, dtype=bool), 'N')
    _check(pd.date_range('2012', '2013'), 'T')
    _check(pd.timedelta_range(365, periods=12), 'T')

    nulled = pd.Series(np.random.randint(10, size=10))
    nulled[0] = None
    _check(nulled, 'Q')
    _check(['a', 'b', 'c'], 'N')

    if hasattr(pytest, 'warns'): # added in pytest 2.8
        with pytest.warns(UserWarning):
            _check([], 'N')
    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            _check([], 'N')
