import pytest
import pandas as pd


from altair.vegalite.data import limit_rows, MaxRowsError, sample, pipe, to_values


def _create_dataframe(N):
    data = pd.DataFrame({"x": range(N), "y": range(N)})
    return data


def _create_data_with_values(N):
    data = {'values': [{'x':i,'y':i+1} for i in range(N)]}
    return data


def test_limit_rows():
    """Test the limit_rows data transformer."""
    data = _create_dataframe(10)
    result = limit_rows(data, max_rows=20)
    assert data is result
    with pytest.raises(MaxRowsError):
        pipe(data, limit_rows(max_rows=5))
    data = _create_data_with_values(10)
    result = pipe(data, limit_rows(max_rows=20))
    assert data is result
    with pytest.raises(MaxRowsError):
        limit_rows(data, max_rows=5)


def test_sample():
    """Test the sample data transformer."""
    data = _create_dataframe(20)
    result = pipe(data, sample(n=10))
    assert len(result)==10
    assert isinstance(result, pd.DataFrame)
    data = _create_data_with_values(20)
    result = sample(data, n=10)
    assert isinstance(result, dict)
    assert 'values' in result
    assert len(result['values'])==10
    data = _create_dataframe(20)
    result = pipe(data, sample(frac=0.5))
    assert len(result)==10
    assert isinstance(result, pd.DataFrame)
    data = _create_data_with_values(20)
    result = sample(data, frac=0.5)
    assert isinstance(result, dict)
    assert 'values' in result
    assert len(result['values'])==10


def test_to_values():
    """Test the to_values data transformer."""
    data = _create_dataframe(10)
    result = pipe(data, to_values)
    assert result=={'values': data.to_dict(orient='records')}


def test_type_error():
    """Ensure that TypeError is raised for types other than dict/DataFrame."""
    for f in (sample, limit_rows, to_values):
        with pytest.raises(TypeError):
            pipe(0, f)
