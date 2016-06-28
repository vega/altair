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
    check('foobar:quantitative', type='Q', field='foobar')
    check('foobar:nominal', type='N', field='foobar')
    check('foobar:ordinal', type='O', field='foobar')
    check('foobar:temporal', type='T', field='foobar')

    check('foobar:Q', type='Q', field='foobar')
    check('foobar:N', type='N', field='foobar')
    check('foobar:O', type='O', field='foobar')
    check('foobar:T', type='T', field='foobar')

    # Fields with aggregate and/or type
    check('average(foobar)', field='foobar', aggregate='average')
    check('min(foobar):temporal', type='T', field='foobar', aggregate='min')
    check('sum(foobar):Q', type='Q', field='foobar', aggregate='sum')

    # check that invalid arguments are not split-out
    check('invalid(blah)', field='invalid(blah)')
    check('blah:invalid', field='blah:invalid')
    check('invalid(blah):invalid', field='invalid(blah):invalid')

    # check parsing in presence of strange characters
    check('average(a b:(c\nd):Q', aggregate='average',
          field='a b:(c\nd', type='Q')


def test_parse_shorthand_valid_fields():
    def check(shorthand, valid_fields, **kwargs):
        assert parse_shorthand(shorthand, valid_fields) == kwargs

    check('foo', ['foo', 'bar'], field='foo')
    check('average(foo)', ['average(foo)'], field='average(foo)')
    check('average(foo)', ['foo', 'average(foo)'], field='average(foo)')
    check('average(foo):Q', ['foo', 'average(foo)'],
          field='average(foo)', type='Q')
    check('average(foo):Q', ['foo', 'average(foo)', 'average(foo):Q'],
          field='average(foo):Q')
    check('average(average(foo):Q):Q', ['average(foo):Q'],
          field='average(foo):Q', aggregate='average', type='Q')


def test_parse_shorthand_invalid_fields():
    def check_raises(shorthand, valid_fields):
        with pytest.raises(ValueError) as err:
            parse_shorthand(shorthand, valid_fields)
        assert str(err.value).startswith('No matching field for shorthand:')

    check_raises('foo', ['bar', 'baz'])
    check_raises('average(foo)', ['bar', 'baz'])
    check_raises('average(foo):Q', ['bar', 'baz'])


def test_shorthand_roundtrip():
    def check(**kwargs):
        assert parse_shorthand(construct_shorthand(**kwargs)) == kwargs

    check(field='foo')
    check(field='foo', aggregate='average')
    check(field='foo', type='Q')
    check(field='foo', aggregate='average', type='Q')


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

    if hasattr(pytest, 'warns'):  # added in pytest 2.8
        with pytest.warns(UserWarning):
            _check([], 'N')
    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            _check([], 'N')


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
