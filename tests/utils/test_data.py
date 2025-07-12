from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, SupportsIndex, TypeVar

import narwhals.stable.v1 as nw
import pandas as pd
import polars as pl
import pytest

from altair.utils.data import (
    MaxRowsError,
    limit_rows,
    sample,
    to_csv,
    to_json,
    to_values,
)

if TYPE_CHECKING:
    from collections.abc import Callable

T = TypeVar("T")


def _pipe(data: Any, *funcs: Callable[..., Any]) -> Any:
    # Redefined to maintain existing tests
    # Originally part of `toolz` dependency
    for func in funcs:
        data = func(data)
    return data


def _create_dataframe(
    n: SupportsIndex, /, tp: Callable[..., T] | type[Any] = pd.DataFrame
) -> T | Any:
    data = tp({"x": range(n), "y": range(n)})
    return data


def _create_data_with_values(n: SupportsIndex, /) -> dict[str, Any]:
    data = {"values": [{"x": i, "y": i + 1} for i in range(n)]}
    return data


def test_limit_rows():
    """Test the limit_rows data transformer."""
    data = nw.from_native(_create_dataframe(10), eager_only=True)
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
    result = sample(pl.DataFrame(data), n=10)
    assert isinstance(result, pl.DataFrame)
    assert len(result) == 10


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
    """
    Test to_json.

    - make certain the filename is deterministic
    - make certain the file contents match the data.
    """
    filename = ""
    data = _create_dataframe(10)
    try:
        result1 = _pipe(data, to_json)
        result2 = _pipe(data, to_json)
        filename = result1["url"]
        output = pd.read_json(filename)
    finally:
        if filename:
            Path(filename).unlink()

    assert result1 == result2
    assert output.equals(data)


def test_dict_to_json():
    """
    Test to_json.

    - make certain the filename is deterministic
    - make certain the file contents match the data.
    """
    filename = ""
    data = _create_data_with_values(10)
    try:
        result1 = _pipe(data, to_json)
        result2 = _pipe(data, to_json)
        filename = result1["url"]
        output = pd.read_json(filename).to_dict(orient="records")
    finally:
        if filename:
            Path(filename).unlink()

    assert result1 == result2
    assert data == {"values": output}


@pytest.mark.parametrize("tp", [pd.DataFrame, pl.DataFrame], ids=["pandas", "polars"])
def test_dataframe_to_csv(tp: type[Any]) -> None:
    """
    Test to_csv with dataframe input.

    - make certain the filename is deterministic
    - make certain the file contents match the data.
    """
    filename: str = ""
    data = _create_dataframe(10, tp=tp)
    try:
        result1 = _pipe(data, to_csv)
        result2 = _pipe(data, to_csv)
        filename = result1["url"]
        output = tp(pd.read_csv(filename))
    finally:
        if filename:
            Path(filename).unlink()

    assert result1 == result2
    assert output.equals(data)


def test_dict_to_csv():
    """
    Test to_csv with dict input.

    - make certain the filename is deterministic
    - make certain the file contents match the data.
    """
    filename = ""
    data = _create_data_with_values(10)
    try:
        result1 = _pipe(data, to_csv)
        result2 = _pipe(data, to_csv)
        filename = result1["url"]
        output = pd.read_csv(filename).to_dict(orient="records")
    finally:
        if filename:
            Path(filename).unlink()

    assert result1 == result2
    assert data == {"values": output}
