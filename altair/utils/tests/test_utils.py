import pytest
import warnings
import json

import numpy as np
import pandas as pd

from .. import (parse_shorthand, construct_shorthand,
                infer_vegalite_type, sanitize_dataframe)


def test_parse_shorthand():
    def check(s, **kwargs):
        assert parse_shorthand(s) == kwargs

    check('')

    # Fields alone
    check('foobar', field='foobar')
    check('blah:(fd ', field='blah:(fd ')

    # Fields with type
    check('foobar:quantitative', type='quantitative', field='foobar')
    check('foobar:nominal', type='nominal', field='foobar')
    check('foobar:ordinal', type='ordinal', field='foobar')
    check('foobar:temporal', type='temporal', field='foobar')

    check('foobar:Q', type='quantitative', field='foobar')
    check('foobar:N', type='nominal', field='foobar')
    check('foobar:O', type='ordinal', field='foobar')
    check('foobar:T', type='temporal', field='foobar')

    # Fields with aggregate and/or type
    check('average(foobar)', field='foobar', aggregate='average')
    check('min(foobar):temporal', type='temporal', field='foobar', aggregate='min')
    check('sum(foobar):Q', type='quantitative', field='foobar', aggregate='sum')

    # check that invalid arguments are not split-out
    check('invalid(blah)', field='invalid(blah)')
    check('blah:invalid', field='blah:invalid')
    check('invalid(blah):invalid', field='invalid(blah):invalid')

    # check parsing in presence of strange characters
    check('average(a b:(c\nd):Q', aggregate='average',
          field='a b:(c\nd', type='quantitative')


def test_shorthand_roundtrip():
    def check(**kwargs):
        assert parse_shorthand(construct_shorthand(**kwargs)) == kwargs

    check(field='foo')
    check(field='foo', aggregate='average')
    check(field='foo', type='quantitative')
    check(field='foo', aggregate='average', type='quantitative')


def test_infer_vegalite_type():
    def _check(arr, typ):
        assert infer_vegalite_type(arr) == typ

    _check(np.arange(5, dtype=float), 'quantitative')
    _check(np.arange(5, dtype=int), 'quantitative')
    _check(np.zeros(5, dtype=bool), 'nominal')
    _check(pd.date_range('2012', '2013'), 'temporal')
    _check(pd.timedelta_range(365, periods=12), 'temporal')

    nulled = pd.Series(np.random.randint(10, size=10))
    nulled[0] = None
    _check(nulled, 'quantitative')
    _check(['a', 'b', 'c'], 'nominal')

    if hasattr(pytest, 'warns'):  # added in pytest 2.8
        with pytest.warns(UserWarning):
            _check([], 'nominal')
    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            _check([], 'nominal')


def test_sanitize_dataframe():
    # create a dataframe with various types
    df = pd.DataFrame({'s': list('abcde'),
                       'f': np.arange(5, dtype=float),
                       'i': np.arange(5, dtype=int),
                       'd': pd.date_range('2012-01-01', periods=5, freq='H'),
                       'c': pd.Series(list('ababc'), dtype='category')})

    # add some nulls
    df.ix[0, 's'] = None
    df.ix[0, 'f'] = np.nan
    df.ix[0, 'd'] = pd.NaT

    # JSON serialize. This will fail on non-sanitized dataframes
    df_clean = sanitize_dataframe(df)
    s = json.dumps(df_clean.to_dict(orient='records'))

    # Re-construct pandas dataframe
    df2 = pd.read_json(s)

    # Re-apply original types
    for col in df:
        if str(df[col].dtype).startswith('datetime'):
            # astype(datetime) introduces time-zone issues:
            # to_datetime() does not.
            df2[col] = pd.to_datetime(df2[col])
        else:
            df2[col] = df2[col].astype(df[col].dtype)

    assert df.equals(df2)
