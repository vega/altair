from __future__ import annotations

import json
from importlib import import_module
from io import BytesIO
from typing import TYPE_CHECKING, Any

import pytest
from narwhals.stable import v1 as nw
from narwhals.stable.v1 import dependencies as nw_dep

from altair.datasets import Loader, _readimpl
from altair.datasets._cache import SchemaCache
from tests import skip_requires_pyarrow

if TYPE_CHECKING:
    from altair.datasets._reader import _Backend
    from altair.datasets._typing import FlFieldStr, Metadata


@pytest.mark.parametrize("field_type", ["array", "object"])
def test_pyarrow_json_schema(field_type: FlFieldStr) -> None:
    """JSON readers infer nested types without constructing an unused Arrow schema."""
    cache = SchemaCache(implementation=nw.Implementation.PYARROW)
    cache._mapping["nested_json"] = {"value": field_type}

    assert cache.schema_kwds({"dataset_name": "nested_json", "suffix": ".json"}) == {}


@pytest.mark.parametrize(
    ("backend", "fallback"),
    [
        ("pandas", None),
        pytest.param("pandas[pyarrow]", None, marks=skip_requires_pyarrow()),
        ("polars", None),
        pytest.param("pyarrow", "polars", marks=skip_requires_pyarrow()),
        pytest.param("pyarrow", "pandas", marks=skip_requires_pyarrow()),
        pytest.param("pyarrow", None, marks=skip_requires_pyarrow()),
    ],
)
def test_read_nested_json(
    backend: _Backend, fallback: str | None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Preserve JSON arrays and objects, including PyArrow's import-dependent fallbacks."""
    rows: list[dict[str, Any]] = [
        {"categories": None, "datasets": [], "details": None},
        {"categories": [], "datasets": ["cars"], "details": {"source": "vega"}},
        {
            "categories": ["distributions", "interactive"],
            "datasets": ["cars", "barley"],
            "details": {"source": "altair"},
        },
    ]
    payload = json.dumps(rows).encode()
    name = "nested_json"
    meta: Metadata = {
        "dataset_name": name,
        "file_name": "nested.json",
        "suffix": ".json",
        "is_json": True,
        "is_spatial": False,
        "is_tabular": True,
        "has_schema": True,
        "url": "https://example.com/nested.json",
    }

    if backend == "pyarrow":
        # Model which optional backends were imported before creating the loader.
        monkeypatch.setattr(
            _readimpl,
            "get_polars",
            lambda: import_module("polars") if fallback == "polars" else None,
        )
        monkeypatch.setattr(
            _readimpl,
            "get_pandas",
            lambda: import_module("pandas") if fallback == "pandas" else None,
        )

    load = Loader.from_backend(backend)
    reader = load._reader
    metadata = nw.from_dict(
        {key: [value] for key, value in meta.items()}, backend=reader._implementation
    )
    monkeypatch.setattr(reader, "_query", lambda *_: metadata)
    monkeypatch.setattr(reader._opener, "open", lambda _: BytesIO(payload))
    monkeypatch.setenv("ALTAIR_DATASETS_DIR", "")
    reader._schema_cache._mapping[name] = {
        "categories": "array",
        "datasets": "array",
        "details": "object",
    }

    result = load(name)
    assert nw.from_native(result).to_dict(as_series=False) == {  # ty: ignore
        key: [row[key] for row in rows] for key in rows[0]
    }
    if nw_dep.is_pandas_dataframe(result):
        assert len(result.explode("categories")) == 4


@pytest.mark.parametrize(
    "dtype_backend", [None, pytest.param("pyarrow", marks=skip_requires_pyarrow())]
)
def test_pandas_json_scalar_dtypes(dtype_backend: str | None) -> None:
    """Keep scalar normalization when distinguishing nested object columns."""
    import pandas as pd

    source = pd.DataFrame(
        {
            "number": [1, None, 3],
            "text": ["one", None, "three"],
            "mixed": [1, "two", 3],
            "nested": [None, [], ["sample"]],
        }
    )
    result = _readimpl._pd_fix_dtypes_nw(source, dtype_backend=dtype_backend)

    assert result.select("number", "text").schema == {
        "number": nw.Int64,
        "text": nw.String,
    }
    # Older Narwhals versions report pandas' newer `str` dtype as Unknown.
    assert pd.api.types.is_string_dtype(result.to_native()["mixed"].dtype)
    assert result.get_column("number").drop_nulls().to_list() == [1, 3]
    assert result.get_column("mixed").to_list() == ["1", "two", "3"]
    assert result.get_column("nested").to_list() == [None, [], ["sample"]]
