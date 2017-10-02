import pytest
import warnings
import json

import numpy as np
import pandas as pd

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
                       'o': pd.Series([np.array(i) for i in range(5)])})

    # add some nulls
    df.ix[0, 's'] = None
    df.ix[0, 'f'] = np.nan
    df.ix[0, 'd'] = pd.NaT
    df.ix[0, 'o'] = np.array(np.nan)

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

    # pandas doesn't properly recognize np.array(np.nan), so change it here
    df.ix[0, 'o'] = np.nan
    assert df.equals(df2)
