from __future__ import annotations

import re
import sys
from importlib.util import find_spec
from typing import TYPE_CHECKING

import pytest
from narwhals.dependencies import is_into_dataframe
from narwhals.stable import v1 as nw

import altair as alt  # noqa: F401
from altair.datasets import Loader
from tests import skip_requires_pyarrow

if TYPE_CHECKING:
    from typing import Literal

    from altair.datasets._readers import _Backend

CACHE_ENV_VAR: Literal["ALTAIR_DATASETS_DIR"] = "ALTAIR_DATASETS_DIR"


requires_pyarrow = skip_requires_pyarrow()

backends = pytest.mark.parametrize(
    "backend",
    [
        "polars",
        pytest.param(
            "pandas",
            marks=pytest.mark.xfail(
                find_spec("pyarrow") is None,
                reason=(
                    "`pandas` supports backends other than `pyarrow` for `.parquet`.\n"
                    "However, none of these are currently an `altair` dependency."
                ),
            ),
        ),
        pytest.param("polars[pyarrow]", marks=requires_pyarrow),
        pytest.param("pandas[pyarrow]", marks=requires_pyarrow),
        pytest.param("pyarrow", marks=requires_pyarrow),
    ],
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
def test_loader_call(backend: _Backend, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(CACHE_ENV_VAR, raising=False)

    data = Loader.with_backend(backend)
    frame = data("stocks", ".csv")
    assert is_into_dataframe(frame)
    nw_frame = nw.from_native(frame)
    assert set(nw_frame.columns) == {"symbol", "date", "price"}


@backends
def test_missing_dependency_single(
    backend: _Backend, monkeypatch: pytest.MonkeyPatch
) -> None:
    if backend in {"polars[pyarrow]", "pandas[pyarrow]"}:
        pytest.skip("Testing single dependency backends only")

    monkeypatch.setitem(sys.modules, backend, None)

    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{backend}.+requires.+{backend}.+but.+{backend}.+not.+found.+pip install {backend}",
            flags=re.DOTALL,
        ),
    ):
        Loader.with_backend(backend)


@pytest.mark.parametrize("backend", ["polars[pyarrow]", "pandas[pyarrow]"])
@skip_requires_pyarrow
def test_missing_dependency_multi(
    backend: _Backend, monkeypatch: pytest.MonkeyPatch
) -> None:
    secondary = "pyarrow"
    primary = backend.removesuffix(f"[{secondary}]")
    monkeypatch.setitem(sys.modules, secondary, None)

    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{re.escape(backend)}.+requires.+'{primary}', '{secondary}'.+but.+{secondary}.+not.+found.+pip install {secondary}",
            flags=re.DOTALL,
        ),
    ):
        Loader.with_backend(backend)
