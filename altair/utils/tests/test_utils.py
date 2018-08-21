import pytest
import warnings
import json

import numpy as np
import pandas as pd
import six

from .. import infer_vegalite_type, sanitize_dataframe


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
                       'b': np.array([True, False, True, True, False]),
                       'd': pd.date_range('2012-01-01', periods=5, freq='H'),
                       'c': pd.Series(list('ababc'), dtype='category'),
                       'c2': pd.Series([1, 'A', 2.5, 'B', None],
                                       dtype='category'),
                       'o': pd.Series([np.array(i) for i in range(5)]),
                       'p': pd.date_range('2012-01-01', periods=5, freq='H').tz_localize('UTC')})

    # add some nulls
    df.iloc[0, df.columns.get_loc('s')] = None
    df.iloc[0, df.columns.get_loc('f')] = np.nan
    df.iloc[0, df.columns.get_loc('d')] = pd.NaT
    df.iloc[0, df.columns.get_loc('o')] = np.array(np.nan)

    # JSON serialize. This will fail on non-sanitized dataframes
    print(df[['s', 'c2']])
    df_clean = sanitize_dataframe(df)
    print(df_clean[['s', 'c2']])
    print(df_clean[['s', 'c2']].to_dict())
    s = json.dumps(df_clean.to_dict(orient='records'))
    print(s)

    # Re-construct pandas dataframe
    df2 = pd.read_json(s)

    # Re-order the columns to match df
    df2 = df2[df.columns]

    # Re-apply original types
    for col in df:
        if str(df[col].dtype).startswith('datetime'):
            # astype(datetime) introduces time-zone issues:
            # to_datetime() does not.
            utc = isinstance(df[col].dtype, pd.core.dtypes.dtypes.DatetimeTZDtype)
            df2[col] = pd.to_datetime(df2[col], utc = utc)
        else:
            df2[col] = df2[col].astype(df[col].dtype)

    # pandas doesn't properly recognize np.array(np.nan), so change it here
    df.iloc[0, df.columns.get_loc('o')] = np.nan
    assert df.equals(df2)


def test_sanitize_dataframe_colnames():
    df = pd.DataFrame(np.arange(12).reshape(4, 3))

    # Test that RangeIndex is converted to strings
    df = sanitize_dataframe(df)
    assert [isinstance(col, six.string_types) for col in df.columns]

    # Test that non-string columns result in an error
    df.columns = [4, 'foo', 'bar']
    with pytest.raises(ValueError) as err:
        sanitize_dataframe(df)
    assert str(err.value).startswith('Dataframe contains invalid column name: 4.')


def test_sanitize_dataframe_timedelta():
    df = pd.DataFrame({'r': pd.timedelta_range(start='1 day', periods=4)})
    with pytest.raises(ValueError) as err:
        sanitize_dataframe(df)
    assert str(err.value).startswith('Field "r" has type "timedelta')


def test_sanitize_dataframe_infs():
    df = pd.DataFrame({'x': [0, 1, 2, np.inf, -np.inf, np.nan]})
    df_clean = sanitize_dataframe(df)
    assert list(df_clean.dtypes) == [object]
    assert list(df_clean['x']) == [0, 1, 2, None, None, None]
