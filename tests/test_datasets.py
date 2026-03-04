from __future__ import annotations

import datetime as dt
import re
import sys
from functools import partial
from importlib import import_module
from importlib.util import find_spec
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast, get_args
from urllib.error import URLError

import pytest
from narwhals.stable import v1 as nw
from narwhals.stable.v1 import dependencies as nw_dep

from altair.datasets import Loader
from altair.datasets._exceptions import AltairDatasetsError
from altair.datasets._typing import Dataset, Metadata
from tests import no_xdist, skip_requires_geopandas, skip_requires_pyarrow

if TYPE_CHECKING:
    from collections.abc import Mapping
    from pathlib import Path
    from typing import Literal

    import pandas as pd
    import polars as pl
    from _pytest.mark import ParameterSet  # pyright: ignore[reportPrivateImportUsage]

    from altair.datasets._reader import _Backend, _PandasAny, _Polars, _PyArrow
    from altair.vegalite.v6.schema._typing import OneOrSeq

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    PolarsLoader: TypeAlias = Loader[pl.DataFrame, pl.LazyFrame]

# =============================================================================
# Test Configuration and Fixtures
# =============================================================================

datasets_debug: pytest.MarkDecorator = pytest.mark.datasets_debug()
"""
Custom ``pytest.mark`` decorator.

Use for more exhaustive tests that require many requests.

**Disabled** by default in ``pyproject.toml``:

    [tool.pytest.ini_options]
    addopts = ...
"""

_backend_params: Mapping[_Backend, ParameterSet] = {
    "polars": pytest.param("polars"),
    "pandas": pytest.param("pandas"),
    "pandas[pyarrow]": pytest.param("pandas[pyarrow]", marks=skip_requires_pyarrow()),
    "pyarrow": pytest.param("pyarrow", marks=skip_requires_pyarrow()),
}

backends: pytest.MarkDecorator = pytest.mark.parametrize(
    "backend", _backend_params.values()
)
backends_no_polars: pytest.MarkDecorator = pytest.mark.parametrize(
    "backend", [v for k, v in _backend_params.items() if k != "polars"]
)
backends_pandas_any: pytest.MarkDecorator = pytest.mark.parametrize(
    "backend", [v for k, v in _backend_params.items() if "pandas" in k]
)
backends_pyarrow: pytest.MarkDecorator = pytest.mark.parametrize(
    "backend", [v for k, v in _backend_params.items() if k == "pyarrow"]
)

datasets_all: pytest.MarkDecorator = pytest.mark.parametrize("name", get_args(Dataset))
datasets_spatial: pytest.MarkDecorator = pytest.mark.parametrize(
    "name",
    ["earthquakes", "london_boroughs", "london_tube_lines", "us_10m", "world_110m"],
)

CACHE_ENV_VAR: Literal["ALTAIR_DATASETS_DIR"] = "ALTAIR_DATASETS_DIR"


@pytest.fixture(scope="session")
def polars_loader() -> PolarsLoader:
    """Fastest and **most reliable** backend."""
    load = Loader.from_backend("polars")
    if load.cache.is_not_active():
        load.cache.path = load.cache._XDG_CACHE
    return load


@pytest.fixture
def metadata_columns() -> frozenset[str]:
    return Metadata.__required_keys__.union(Metadata.__optional_keys__)


# =============================================================================
# Utility Functions
# =============================================================================


def is_frame_backend(frame: Any, backend: _Backend, /) -> bool:
    pandas_any: set[_PandasAny] = {"pandas", "pandas[pyarrow]"}
    if backend in pandas_any:
        return nw_dep.is_pandas_dataframe(frame)
    elif backend == "pyarrow":
        return nw_dep.is_pyarrow_table(frame)
    elif backend == "polars":
        return nw_dep.is_polars_dataframe(frame)
    else:
        raise TypeError(backend)


def is_loader_backend(loader: Loader[Any, Any], backend: _Backend, /) -> bool:
    return repr(loader) == f"{type(loader).__name__}[{backend}]"


def is_polars_backed_pyarrow(loader: Loader[Any, Any], /) -> bool:
    """
    User requested ``pyarrow``, but also has ``polars`` installed.

    Both support nested datatypes, which are required for spatial json.
    """
    return (
        is_loader_backend(loader, "pyarrow")
        and "earthquakes" in loader._reader.profile()["supported"]
    )


def is_geopandas_backed_pandas(loader: Loader[Any, Any], /) -> bool:
    return (
        is_loader_backend(loader, "pandas")
        or is_loader_backend(loader, "pandas[pyarrow]")
    ) and "earthquakes" in loader._reader.profile()["supported"]


# =============================================================================
# Backend and Loader Tests
# =============================================================================


@backends
def test_metadata_columns(backend: _Backend, metadata_columns: frozenset[str]) -> None:
    """Ensure all backends will query the same column names."""
    load = Loader.from_backend(backend)
    schema_columns = load._reader._scan_metadata().collect().columns
    assert set(schema_columns) == metadata_columns


@backends
def test_loader_from_backend(backend: _Backend) -> None:
    load = Loader.from_backend(backend)
    assert is_loader_backend(load, backend)


@backends
def test_loader_url(backend: _Backend) -> None:
    load = Loader.from_backend(backend)
    url = load.url("volcano")
    assert isinstance(url, str)
    assert "vega-datasets" in url


@no_xdist
def test_load_infer_priority(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Ensure the **most reliable**, available backend is selected.

    See Also
    --------
    ``altair.datasets._reader.infer_backend``
    """
    import altair.datasets._loader
    from altair.datasets import load

    assert is_loader_backend(load, "polars")
    monkeypatch.delattr(altair.datasets._loader, "load", raising=False)
    monkeypatch.setitem(sys.modules, "polars", None)

    from altair.datasets import load

    if find_spec("pyarrow") is None:
        # NOTE: We can end the test early for the CI job that removes `pyarrow`
        assert is_loader_backend(load, "pandas")
        monkeypatch.delattr(altair.datasets._loader, "load")
        monkeypatch.setitem(sys.modules, "pandas", None)
        with pytest.raises(AltairDatasetsError, match=r"no.+backend"):
            from altair.datasets import load
    else:
        assert is_loader_backend(load, "pandas[pyarrow]")
        monkeypatch.delattr(altair.datasets._loader, "load")
        monkeypatch.setitem(sys.modules, "pyarrow", None)

        from altair.datasets import load

        assert is_loader_backend(load, "pandas")
        monkeypatch.delattr(altair.datasets._loader, "load")
        monkeypatch.setitem(sys.modules, "pandas", None)
        monkeypatch.delitem(sys.modules, "pyarrow")
        monkeypatch.setitem(sys.modules, "pyarrow", import_module("pyarrow"))
        from altair.datasets import load

        assert is_loader_backend(load, "pyarrow")
        monkeypatch.delattr(altair.datasets._loader, "load")
        monkeypatch.setitem(sys.modules, "pyarrow", None)

        with pytest.raises(AltairDatasetsError, match=r"no.+backend"):
            from altair.datasets import load


@backends
def test_load_call(backend: _Backend, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that the load function can be called with different backends."""
    import altair.datasets._loader

    monkeypatch.delattr(altair.datasets._loader, "load", raising=False)
    from altair.datasets import load

    assert is_loader_backend(load, "polars")
    default = load("cars")
    df = load("cars", backend=backend)
    default_2 = load("cars")
    assert nw_dep.is_polars_dataframe(default)
    assert is_frame_backend(df, backend)
    assert nw_dep.is_polars_dataframe(default_2)


@backends
def test_loader_call(backend: _Backend) -> None:
    load = Loader.from_backend(backend)

    if backend == "pyarrow":
        # PyArrow has a known limitation with non-ISO date formats in CSV
        # The stocks dataset has dates like "Jan 1 2000" which PyArrow cannot parse
        # This should raise an informative AltairDatasetsError
        with pytest.raises(
            AltairDatasetsError, match="PyArrow cannot parse date format"
        ):
            load("stocks", ".csv")
    else:
        # Other backends should work normally
        frame = load("stocks", ".csv")
        assert nw_dep.is_into_dataframe(frame)
        nw_frame = nw.from_native(frame)
        assert set(nw_frame.columns) == {"symbol", "date", "price"}


# =============================================================================
# URL and Dataset Discovery Tests
# =============================================================================


def test_url_no_backend(monkeypatch: pytest.MonkeyPatch) -> None:
    from altair.datasets._cache import csv_cache
    from altair.datasets._reader import infer_backend

    priority: Any = (
        "nonexistent_mod_1",
        "nonexistent_mod_2",
        "nonexistent_mod_3",
        "nonexistent_mod_4",
    )
    assert csv_cache._mapping == {}
    with pytest.raises(AltairDatasetsError):
        infer_backend(priority=priority)

    url = csv_cache.url
    # Test that URLs are valid strings pointing to vega-datasets
    assert isinstance(url("jobs"), str)
    assert "vega-datasets" in url("jobs")
    assert csv_cache._mapping != {}

    # Test a few representative datasets instead of all 15+
    assert isinstance(url("cars"), str)
    assert "vega-datasets" in url("cars")
    assert isinstance(url("flights_10k"), str)
    assert "vega-datasets" in url("flights_10k")

    if find_spec("vegafusion"):
        assert isinstance(url("flights_3m"), str)
        assert "vega-datasets" in url("flights_3m")

    with monkeypatch.context() as mp:
        mp.setitem(sys.modules, "vegafusion", None)
        with pytest.raises(AltairDatasetsError, match=r".parquet.+require.+vegafusion"):
            url("flights_3m")
    with pytest.raises(
        TypeError, match="'nonexistent data' does not refer to a known dataset"
    ):
        url("nonexistent data")


# =============================================================================
# Error Handling and Edge Cases
# =============================================================================


@backends
def test_dataset_not_found(backend: _Backend) -> None:
    """Various queries that should **always raise** due to non-existent dataset."""
    load = Loader.from_backend(backend)
    real_name: Literal["disasters"] = "disasters"
    nonexistent_name: Literal["nonexistent name"] = "nonexistent name"
    unsupported_suffix: Literal["unsupported suffix"] = "unsupported suffix"
    incorrect_suffix: Literal[".json"] = ".json"
    ERR_NO_RESULT = ValueError
    MSG_NO_RESULT = "Found no results for"
    NAME = "dataset_name"
    SUFFIX = "suffix"

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(rf"{MSG_NO_RESULT}.+{NAME}.+{nonexistent_name}", re.DOTALL),
    ):
        load.url(nonexistent_name)
    with pytest.raises(
        TypeError,
        match=re.compile(
            rf"Expected '{SUFFIX}' to be one of.+\(.+\).+but got.+{unsupported_suffix}",
            re.DOTALL,
        ),
    ):
        load.url(real_name, unsupported_suffix)  # type: ignore[arg-type]
    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(
            rf"{MSG_NO_RESULT}.+{NAME}.+{real_name}.+{SUFFIX}.+{incorrect_suffix}",
            re.DOTALL,
        ),
    ):
        load.url(real_name, incorrect_suffix)


def test_reader_missing_dependencies() -> None:
    from altair.datasets._reader import _import_guarded

    nonexistent_name = "not_a_real_package"
    real_name = "altair"
    nonexistent_extra = "AnotherNonexistentPackage"
    backend = f"{real_name}[{nonexistent_extra}]"
    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{nonexistent_name}.+requires.+{nonexistent_name}.+but.+{nonexistent_name}.+not.+found.+pip install {nonexistent_name}",
            flags=re.DOTALL,
        ),
    ):
        _import_guarded(nonexistent_name)  # type: ignore
    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{re.escape(backend)}.+requires.+'{real_name}', '{nonexistent_extra}'.+but.+{nonexistent_extra}.+not.+found.+pip install {nonexistent_extra}",
            flags=re.DOTALL,
        ),
    ):
        _import_guarded(backend)  # type: ignore


def test_reader_missing_implementation() -> None:
    from altair.datasets._constraints import is_csv
    from altair.datasets._reader import reader
    from altair.datasets._readimpl import read

    def func(*args, **kwds) -> pd.DataFrame:
        if TYPE_CHECKING:
            return pd.DataFrame()

    name = "pandas"
    rd = reader((read(func, is_csv),), name=name)
    with pytest.raises(
        AltairDatasetsError,
        match=re.compile(rf"Unable.+parquet.+native.+{name}", flags=re.DOTALL),
    ):
        rd.dataset("flights_3m")
    with pytest.raises(
        AltairDatasetsError,
        match=re.compile(r"Found no.+support.+flights.+json", flags=re.DOTALL),
    ):
        rd.dataset("flights_2k")
    with pytest.raises(
        AltairDatasetsError, match=re.compile(r"Image data is non-tabular")
    ):
        rd.dataset("icon_7zip")


# =============================================================================
# Caching Tests
# =============================================================================


@backends
def test_reader_cache(
    backend: _Backend, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Ensure cache hits avoid network activity."""
    import polars as pl
    from polars.testing import assert_frame_equal

    monkeypatch.setenv(CACHE_ENV_VAR, str(tmp_path))
    load = Loader.from_backend(backend)
    assert load.cache.is_active()
    cache_dir = load.cache.path
    assert cache_dir == tmp_path
    assert tuple(load.cache) == ()

    # Use smaller datasets for faster testing
    lookup_groups = load("lookup_groups")
    load("lookup_people")
    load("iowa_electricity")
    load("global_temp")
    cached_paths = tuple(load.cache)
    assert len(cached_paths) == 4

    if nw_dep.is_polars_dataframe(lookup_groups):
        left, right = (
            lookup_groups,
            cast("pl.DataFrame", load("lookup_groups", ".csv")),
        )
    else:
        left, right = (
            pl.DataFrame(lookup_groups),
            pl.DataFrame(load("lookup_groups", ".csv")),
        )

    assert_frame_equal(left, right)
    assert len(tuple(load.cache)) == 4
    assert cached_paths == tuple(load.cache)
    load("iowa_electricity", ".csv")
    load("global_temp", ".csv")
    load("global-temp.csv")
    assert len(tuple(load.cache)) == 4
    assert cached_paths == tuple(load.cache)
    load("lookup_people")
    load("lookup_people.csv")
    load("lookup_people", ".csv")
    load("lookup_people")
    assert len(tuple(load.cache)) == 4
    assert cached_paths == tuple(load.cache)


@datasets_debug
@backends
def test_reader_cache_exhaustive(
    backend: _Backend,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    polars_loader: PolarsLoader,
) -> None:
    """
    Fully populate and then purge the cache for all backends.

    Notes
    -----
    - Does not attempt to read the files
    - Checking we can support pre-downloading and safely deleting
        - Requests work the same for all backends
        - The logic for detecting the cache contents uses ``narwhals``
        - Here, we're testing that these ``narwhals`` operations are consistent
    - `DatasetCache.download_all` is expensive for CI, so aiming for it to run **at most once**
        - 34-45s per call (4x backends)
    """
    polars_loader.cache.download_all()
    CLONED: Path = tmp_path / "clone"
    CLONED.mkdir(exist_ok=True)

    # Copy the cache contents
    import shutil

    shutil.copytree(polars_loader.cache.path, CLONED, dirs_exist_ok=True)

    monkeypatch.setenv(CACHE_ENV_VAR, str(tmp_path))
    load = Loader.from_backend(backend)
    assert load.cache.is_active()
    cache_dir = load.cache.path
    assert cache_dir == tmp_path
    assert tuple(load.cache) == (CLONED,)
    load.cache.path = CLONED
    cached_paths = tuple(load.cache)
    assert cached_paths != ()

    # NOTE: Approximating all datasets downloaded (minimum expected count)
    assert len(cached_paths) >= 70
    assert all(bool(fp.exists() and fp.stat().st_size) for fp in load.cache)
    # NOTE: Confirm this is a no-op (already downloaded)
    load.cache.download_all()
    assert len(cached_paths) == len(tuple(load.cache))

    # NOTE: Ensure unrelated files in the directory are not removed during cache clearing
    test_file: Path = tmp_path / "test_file.json"
    test_file.touch(exist_ok=False)
    load.cache.clear()

    remaining = tuple(tmp_path.iterdir())
    assert set(remaining) == {test_file, CLONED}
    test_file.unlink()  # Remove the test file
    shutil.rmtree(CLONED)  # Remove the cloned directory


@no_xdist
def test_reader_cache_disable(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from altair.datasets import load

    monkeypatch.setenv(CACHE_ENV_VAR, str(tmp_path))
    assert load.cache.is_active()
    assert load.cache.path == tmp_path
    assert load.cache.is_empty()
    load("cars")
    assert not load.cache.is_empty()
    # ISSUE: https://github.com/python/mypy/issues/3004
    load.cache.path = None
    assert load.cache.is_not_active()
    with pytest.raises(
        ValueError,
        match=re.compile(
            rf"Cache.+unset.+{CACHE_ENV_VAR}.+\.cache\.path =", flags=re.DOTALL
        ),
    ):
        tuple(load.cache)
    load.cache.path = tmp_path
    assert load.cache.is_active()
    assert load.cache.path == tmp_path
    assert not load.cache.is_empty()


# =============================================================================
# Format-Specific Tests
# =============================================================================


@pytest.mark.parametrize(
    "name", ["cars", "movies", "wheat", "barley", "gapminder", "income", "burtin"]
)
@pytest.mark.parametrize("fallback", ["polars", None])
@backends_pyarrow
def test_pyarrow_read_json(
    backend: _PyArrow,
    fallback: _Polars | None,
    name: Dataset,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    if fallback is None:
        monkeypatch.setitem(sys.modules, "polars", None)
    load = Loader.from_backend(backend)
    assert load(name, ".json")


@datasets_spatial
@backends_no_polars
@pytest.mark.geospatial
@skip_requires_geopandas
def test_spatial(backend: _Backend, name: Dataset) -> None:
    load = Loader.from_backend(backend)

    # Specify layer parameter for datasets with multiple layers to avoid warnings
    layer_kwargs = {}
    if name == "us_10m":
        layer_kwargs = {"layer": "counties"}
    elif name == "world_110m":
        layer_kwargs = {"layer": "countries"}

    if is_polars_backed_pyarrow(load):
        assert nw_dep.is_pyarrow_table(load(name, **layer_kwargs))
    elif is_geopandas_backed_pandas(load):
        import geopandas

        assert isinstance(load(name, **layer_kwargs), geopandas.GeoDataFrame)
    else:
        pattern = re.compile(
            rf"{name}.+geospatial.+native.+{re.escape(backend)}.+try.+polars.+url",
            flags=re.DOTALL | re.IGNORECASE,
        )
        with pytest.raises(AltairDatasetsError, match=pattern):
            load(name, **layer_kwargs)


@backends
def test_tsv(backend: _Backend) -> None:
    load = Loader.from_backend(backend)
    is_frame_backend(load("unemployment", ".tsv"), backend)


# =============================================================================
# Comprehensive Dataset Tests
# =============================================================================


@datasets_all
@datasets_debug
def test_all_datasets(polars_loader: PolarsLoader, name: Dataset) -> None:
    """
    Test that all datasets can be loaded with the polars backend.

    - For image files (e.g., icon_7zip, ffox, gimp), we expect an error because these are not tabular data.
      The error message should be clear and helpful, and this is the correct behavior.
    - Dataset names are valid Python identifiers, but the URLs may differ; we do not test URL construction here.
    - This test checks Altair's integration with the datasets API, not the validity of upstream datasets or backends.
    """
    if name in {"icon_7zip", "ffox", "gimp"}:
        # These are image files that should raise an error when loaded as tabular data
        # The error message contains the actual filename (e.g., '7zip.png', 'ffox.png', 'gimp.png')
        pattern = re.compile(
            r"Unable to load '.+\.png' as tabular data",
            flags=re.DOTALL | re.IGNORECASE,
        )
        with pytest.raises(AltairDatasetsError, match=pattern):
            polars_loader(name)
    else:
        frame = polars_loader(name)
        assert nw_dep.is_polars_dataframe(frame)


# =============================================================================
# Network and Connection Tests
# =============================================================================


def _raise_exception(e: type[Exception], *args: Any, **kwds: Any):
    raise e(*args, **kwds)


def test_no_remote_connection(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from polars.testing import assert_frame_equal

    load = Loader.from_backend("polars")
    load.cache.path = tmp_path
    load("london_centroids")
    load("stocks")
    load("driving")
    cached_paths = tuple(tmp_path.iterdir())
    assert len(cached_paths) == 3
    raiser = partial(_raise_exception, URLError)
    with monkeypatch.context() as mp:
        mp.setattr(load._reader._opener, "open", raiser)
        # Existing cache entries don't trigger an error
        load("london_centroids")
        load("stocks")
        load("driving")
        # Mocking cache-miss without remote conn
        with pytest.raises(URLError):
            load("birdstrikes")
        assert len(tuple(tmp_path.iterdir())) == 3

    # Now we can get a cache-hit
    frame = load("birdstrikes")
    assert nw_dep.is_polars_dataframe(frame)
    assert len(tuple(tmp_path.iterdir())) == 4

    with monkeypatch.context() as mp:
        mp.setattr(load._reader._opener, "open", raiser)
        # Here, the remote conn isn't considered - we already have the file
        frame_from_cache = load("birdstrikes")
        assert len(tuple(tmp_path.iterdir())) == 4
    assert_frame_equal(frame, frame_from_cache)


# =============================================================================
# Data Type and Schema Tests
# =============================================================================


@pytest.mark.parametrize(
    ("name", "column"),
    [
        ("cars", "Year"),
        ("unemployment_across_industries", "date"),
        ("flights_10k", "date"),
        ("football", "date"),
        ("crimea", "date"),
        ("ohlc", "date"),
    ],
)
def test_polars_date_read_json_roundtrip(
    polars_loader: PolarsLoader, name: Dataset, column: str
) -> None:
    """Ensure ``date`` columns are inferred using the roundtrip json -> csv method."""
    frame = polars_loader(name, ".json")
    tp = frame.schema.to_python()[column]
    assert tp is dt.date or issubclass(tp, dt.date)


@backends_pandas_any
@pytest.mark.parametrize(
    ("name", "columns"),
    [
        ("birdstrikes", "Flight Date"),
        ("cars", "Year"),
        ("co2_concentration", "Date"),
        ("crimea", "date"),
        ("football", "date"),
        ("iowa_electricity", "year"),
        ("la_riots", "death_date"),
        ("ohlc", "date"),
        ("seattle_weather_hourly_normals", "date"),
        ("seattle_weather", "date"),
        ("sp500_2000", "date"),
        ("unemployment_across_industries", "date"),
        ("us_employment", "month"),
    ],
)
def test_pandas_date_parse(
    backend: _PandasAny,
    name: Dataset,
    columns: OneOrSeq[str],
    polars_loader: PolarsLoader,
) -> None:
    """
    Ensure schema defaults are correctly parsed.

    Notes
    -----
    - Depends on ``frictionless`` being able to detect the date/datetime columns.
    - Not all format strings work
    """
    date_columns: list[str] = [columns] if isinstance(columns, str) else list(columns)
    load = Loader.from_backend(backend)
    url = load.url(name)
    kwds: dict[str, Any] = (
        {"convert_dates": date_columns}
        if url.endswith(".json")
        else {"parse_dates": date_columns}
    )
    df_schema_derived: pd.DataFrame = load(name)
    nw_schema = nw.from_native(df_schema_derived).schema
    df_manually_specified: pd.DataFrame = load(name, **kwds)

    assert set(date_columns).issubset(nw_schema)
    for column in date_columns:
        assert nw_schema[column] in {nw.Date, nw.Datetime}

    assert nw_schema == nw.from_native(df_manually_specified).schema
    # We do not assert that loading with parse_dates=[]/convert_dates=[] yields a
    # different schema: backends may still infer date columns from the file.

    # NOTE: Checking `polars` infers the same[1] as what `pandas` needs a hint for
    # [1] Doesn't need to be exact, just recognize as *some kind* of date/datetime
    pl_schema: pl.Schema = polars_loader(name).schema
    for column in date_columns:
        assert pl_schema[column].is_temporal()


# =============================================================================
# Data API Tests
# =============================================================================


class TestDataObject:
    """Test the main DataObject functionality."""

    def test_list_datasets(self) -> None:
        """Test that list_datasets returns a list of available datasets."""
        from altair.datasets import data

        datasets = data.list_datasets()
        assert isinstance(datasets, list)
        assert len(datasets) > 0
        # Check that common datasets are present
        common_datasets = ["cars", "movies", "stocks", "penguins"]
        for dataset in common_datasets:
            if dataset in datasets:
                break
        else:
            pytest.fail("No common datasets found in list_datasets")

    def test_get_default_engine(self) -> None:
        """Test getting the default engine."""
        from altair.datasets import data

        default_engine = data.get_default_engine()
        assert default_engine in {"pandas", "polars", "pandas[pyarrow]", "pyarrow"}

    def test_set_default_engine(self) -> None:
        """Test setting the default engine."""
        from altair.datasets import data

        original_engine = data.get_default_engine()

        data.set_default_engine("polars")
        assert data.get_default_engine() == "polars"

        data.set_default_engine("pandas")
        assert data.get_default_engine() == "pandas"

        data.set_default_engine(original_engine)

    def test_nonexistent_dataset_attribute(self):
        from altair.datasets import data

        with pytest.raises(
            AttributeError, match="Dataset 'nonexistent_dataset' not found"
        ):
            # NOTE: Needing a type ignore here is a good thing
            _ = data.nonexistent_dataset  # pyright: ignore[reportArgumentType]


class TestDataAPIIntegration:
    """Test integration scenarios with the data API."""

    def test_data_consistency(self) -> None:
        """Test that data loaded through different methods is consistent."""
        from altair.datasets import data

        # Load through data API
        cars_data_api = data.cars()

        # Load through direct loader
        from altair.datasets import Loader

        loader = Loader.from_backend("pandas")
        cars_loader = loader("cars")

        # Both should have the same number of rows
        assert len(cars_data_api) == len(cars_loader)


def test_unsupported_engine():
    """Test that unsupported engine raises appropriate error."""
    from altair.datasets import data

    with pytest.raises(TypeError, match="Unknown backend"):
        # NOTE: Needing a type ignore here is a good thing
        data.cars(engine="unsupported_engine")  # pyright: ignore[reportArgumentType, reportCallIssue]
