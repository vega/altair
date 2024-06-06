import os
from typing import Any, Callable
import pytest
import pandas as pd
from altair.utils.data import (
    limit_rows,
    MaxRowsError,
    sample,
    to_values,
    to_json,
    to_csv,
    curry,
    pipe,
)
from altair.utils._importers import import_toolz_function
from altair.utils.deprecation import AltairDeprecationWarning


def _pipe(data: Any, *funcs: Callable[..., Any]) -> Any:
    # Redefined to maintain existing tests
    # Originally part of `toolz` dependency
    for func in funcs:
        data = func(data)
    return data


def _create_dataframe(N):
    data = pd.DataFrame({"x": range(N), "y": range(N)})
    return data


def _create_data_with_values(N):
    data = {"values": [{"x": i, "y": i + 1} for i in range(N)]}
    return data


def test_limit_rows():
    """Test the limit_rows data transformer."""
    data = _create_dataframe(10)
    result = limit_rows(data, max_rows=20)
    assert data is result
    with pytest.raises(MaxRowsError):
        _pipe(data, limit_rows(max_rows=5))
    data = _create_data_with_values(10)
    result = _pipe(data, limit_rows(max_rows=20))
    assert data is result
    with pytest.raises(MaxRowsError):
        limit_rows(data, max_rows=5)


def test_sample():
    """Test the sample data transformer."""
    data = _create_dataframe(20)
    result = _pipe(data, sample(n=10))
    assert len(result) == 10
    assert isinstance(result, pd.DataFrame)
    data = _create_data_with_values(20)
    result = sample(data, n=10)
    assert isinstance(result, dict)
    assert "values" in result
    assert len(result["values"]) == 10
    data = _create_dataframe(20)
    result = _pipe(data, sample(frac=0.5))
    assert len(result) == 10
    assert isinstance(result, pd.DataFrame)
    data = _create_data_with_values(20)
    result = sample(data, frac=0.5)
    assert isinstance(result, dict)
    assert "values" in result
    assert len(result["values"]) == 10


def test_to_values():
    """Test the to_values data transformer."""
    data = _create_dataframe(10)
    result = _pipe(data, to_values)
    assert result == {"values": data.to_dict(orient="records")}


def test_type_error():
    """Ensure that TypeError is raised for types other than dict/DataFrame."""
    for f in (sample, limit_rows, to_values):
        with pytest.raises(TypeError):
            _pipe(0, f)


def test_dataframe_to_json():
    """Test to_json
    - make certain the filename is deterministic
    - make certain the file contents match the data
    """
    data = _create_dataframe(10)
    try:
        result1 = _pipe(data, to_json)
        result2 = _pipe(data, to_json)
        filename = result1["url"]
        output = pd.read_json(filename)
    finally:
        os.remove(filename)

    assert result1 == result2
    assert output.equals(data)


def test_dict_to_json():
    """Test to_json
    - make certain the filename is deterministic
    - make certain the file contents match the data
    """
    data = _create_data_with_values(10)
    try:
        result1 = _pipe(data, to_json)
        result2 = _pipe(data, to_json)
        filename = result1["url"]
        output = pd.read_json(filename).to_dict(orient="records")
    finally:
        os.remove(filename)

    assert result1 == result2
    assert data == {"values": output}


def test_dataframe_to_csv():
    """Test to_csv with dataframe input
    - make certain the filename is deterministic
    - make certain the file contents match the data
    """
    data = _create_dataframe(10)
    try:
        result1 = _pipe(data, to_csv)
        result2 = _pipe(data, to_csv)
        filename = result1["url"]
        output = pd.read_csv(filename)
    finally:
        os.remove(filename)

    assert result1 == result2
    assert output.equals(data)


def test_dict_to_csv():
    """Test to_csv with dict input
    - make certain the filename is deterministic
    - make certain the file contents match the data
    """
    data = _create_data_with_values(10)
    try:
        result1 = _pipe(data, to_csv)
        result2 = _pipe(data, to_csv)
        filename = result1["url"]
        output = pd.read_csv(filename).to_dict(orient="records")
    finally:
        os.remove(filename)

    assert result1 == result2
    assert data == {"values": output}


def test_toolz():
    expected_msg = r"Usage.+ requires"
    data = _create_data_with_values(10)
    try:
        with pytest.warns(AltairDeprecationWarning, match="toolz.curried.pipe"):
            result1 = pipe(data, to_values)
        assert isinstance(result1, dict)
        kwds = {"prefix": "dummy"}
        with pytest.warns(AltairDeprecationWarning, match="toolz.curried.curry"):
            result2 = curry(to_csv, **kwds)
        assert "curry" in type(result2).__name__
        assert result2.func_name == to_csv.__name__
        assert result2.keywords == kwds
    except ImportError as err:
        assert expected_msg in err.msg
    with pytest.raises(ImportError, match=expected_msg):
        dummy = "fake_function_name"
        with pytest.warns(AltairDeprecationWarning, match=f"toolz.curried.{dummy}"):
            func = import_toolz_function(dummy)  # noqa: F841
