import pytest
import pandas as pd
from ... import expr


@pytest.fixture
def data():
    return pd.DataFrame({'xxx': [1, 2, 3],
                         'yyy': [4, 5, 6],
                         'zzz': [7, 8, 9]})


def test_dataframe_namespace(data):
    df = expr.DataFrame(data)
    assert set(dir(df)) == set(data.columns)

def test_dataframe_newcols(data):
    df = expr.DataFrame(data)
    df['sum'] = df.xxx + df.yyy + df.zzz
    df['prod'] = df.xxx * df.yyy * df.zzz
    assert set(dir(df)) == set.union({'sum', 'prod'}, set(data.columns))
    assert repr(df.sum.contents) == 'datum.xxx+datum.yyy+datum.zzz'
    assert repr(df.prod.contents) == 'datum.xxx*datum.yyy*datum.zzz'
