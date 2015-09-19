import numpy as np
import pandas as pd

from altair.utils import parse_shorthand, infer_type


def test_parse_shorthand():
    def check(s, **kwargs):
        assert parse_shorthand(s) == kwargs

    check('', type=None)
    check('foobar', type=None, name='foobar')
    check('foobar:nominal', type='N', name='foobar')
    check('foobar:O', type='O', name='foobar')
    check('avg(foobar)', type=None, name='foobar', aggregate='avg')
    check('sum(foobar):Q', type='Q', name='foobar', aggregate='sum')


def test_infer_type():
    def _check(arr, typ):
        assert infer_type(arr) == typ

    _check(np.arange(5, dtype=float), 'Q')
    _check(np.arange(25, dtype=int), 'Q')
    _check(np.arange(5, dtype=int), 'O')
    _check(np.zeros(5, dtype=bool), 'N')
    _check(pd.date_range('2012', '2013'), 'T')
    _check(pd.timedelta_range(365, periods=12), 'T')

    nulled = pd.Series(np.random.randint(10, size=10))
    nulled[0] = None
    _check(nulled, 'Q')
    _check(['a', 'b', 'c'], 'N')
