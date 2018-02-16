import pytest
import pandas as pd


from altair.vegalite.data import limit_rows




def test_limit_rows():
    data = pd.DataFrame({"x": range(5), "y": range(5)})
    result = limit_rows(data, max_rows=10)
    assert data is result

