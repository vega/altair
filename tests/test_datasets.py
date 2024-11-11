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


@backends
def test_dataset_not_found(backend: _Backend) -> None:
    """
    Various queries that should **always raise** due to non-existent dataset.

    ``Loader.url`` is used since it doesn't require a remote connection.
    """
    import polars as pl

    data = Loader.with_backend(backend)
    real_name: Literal["disasters"] = "disasters"
    real_suffix: Literal[".csv"] = ".csv"
    real_tag: Literal["v1.14.0"] = "v1.14.0"

    invalid_name: Literal["fake name"] = "fake name"
    invalid_suffix: Literal["fake suffix"] = "fake suffix"
    invalid_tag: Literal["fake tag"] = "fake tag"

    incorrect_suffix: Literal[".json"] = ".json"
    incorrect_tag: Literal["v1.5.0"] = "v1.5.0"

    ERR_NO_RESULT = ValueError
    # NOTE: ``polars`` enforces enums stricter than other packages.
    # Rather than returning an empty dataframe, filtering on a value
    # *outside* of the enum range raises an internal error.
    ERR_NO_RESULT_OR_ENUM = (ERR_NO_RESULT, pl.exceptions.InvalidOperationError)

    MSG_NO_RESULT = "Found no results for"
    NAME = "dataset_name"
    SUFFIX = "suffix"
    TAG = "tag"

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(rf"{MSG_NO_RESULT}.+{NAME}.+{invalid_name}", re.DOTALL),
    ):
        data.url(invalid_name)

    with pytest.raises(
        TypeError,
        match=re.compile(
            rf"Expected '{SUFFIX}' to be one of.+\(.+\).+but got.+{invalid_suffix}",
            re.DOTALL,
        ),
    ):
        data.url(real_name, invalid_suffix)  # type: ignore[arg-type]

    with pytest.raises(
        ERR_NO_RESULT_OR_ENUM,
        match=re.compile(rf"{invalid_tag}", re.DOTALL),
    ):
        data.url(real_name, tag=invalid_tag)  # type: ignore[arg-type]

    with pytest.raises(
        ERR_NO_RESULT_OR_ENUM,
        match=re.compile(rf"{invalid_tag}", re.DOTALL),
    ):
        data.url(real_name, real_suffix, tag=invalid_tag)  # type: ignore[arg-type]

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(
            rf"{MSG_NO_RESULT}.+{TAG}.+{incorrect_tag}.+{SUFFIX}.+{real_suffix}.+{NAME}.+{real_name}",
            re.DOTALL,
        ),
    ):
        data.url(real_name, real_suffix, tag=incorrect_tag)

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(
            rf"{MSG_NO_RESULT}.+{SUFFIX}.+{incorrect_suffix}.+{NAME}.+{real_name}",
            re.DOTALL,
        ),
    ):
        data.url(real_name, incorrect_suffix)

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(
            rf"{MSG_NO_RESULT}.+{TAG}.+{real_tag}.+{SUFFIX}.+{incorrect_suffix}.+{NAME}.+{real_name}",
            re.DOTALL,
        ),
    ):
        data.url(real_name, incorrect_suffix, tag=real_tag)

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(
            rf"{MSG_NO_RESULT}.+{TAG}.+{incorrect_tag}.+{NAME}.+{real_name}", re.DOTALL
        ),
    ):
        data.url(real_name, tag=incorrect_tag)
