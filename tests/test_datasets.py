from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pytest
from narwhals.dependencies import is_into_dataframe
from narwhals.stable import v1 as nw

import altair as alt  # noqa: F401
from altair.datasets import Loader

if TYPE_CHECKING:
    from altair.datasets._readers import _Backend

backends = pytest.mark.parametrize(
    "backend", ["polars", "polars[pyarrow]", "pandas", "pandas[pyarrow]", "pyarrow"]
)


@backends
def test_loader_with_backend(backend: _Backend) -> None:
    data = Loader.with_backend(backend)
    assert data._reader._name == backend


@backends
def test_loader_url(backend: _Backend) -> None:
    data = Loader.with_backend(backend)
    dataset_name = "volcano"
    pattern = re.compile(
        rf".+jsdelivr\.net/npm/vega-datasets@.+/data/{dataset_name}\..+"
    )
    url = data.url(dataset_name)
    assert isinstance(url, str)
    assert pattern.match(url) is not None


@backends
def test_loader_call(backend: _Backend) -> None:
    data = Loader.with_backend(backend)
    frame = data("stocks", ".csv")
    assert is_into_dataframe(frame)
    nw_frame = nw.from_native(frame)
    assert set(nw_frame.columns) == {"symbol", "date", "price"}
