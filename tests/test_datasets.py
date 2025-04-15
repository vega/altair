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
from tests import no_xdist, skip_requires_pyarrow
from tools import fs

if TYPE_CHECKING:
    from collections.abc import Callable, Mapping
    from pathlib import Path
    from typing import Literal

    import pandas as pd
    import polars as pl
    from _pytest.mark import ParameterSet  # pyright: ignore[reportPrivateImportUsage]

    from altair.datasets._reader import _Backend, _PandasAny, _Polars, _PyArrow
    from altair.vegalite.v5.schema._typing import OneOrSeq

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    PolarsLoader: TypeAlias = Loader[pl.DataFrame, pl.LazyFrame]

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
    "name", ["earthquakes", "londonBoroughs", "londonTubeLines", "us-10m", "world-110m"]
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


def is_url(name: Dataset, fn_url: Callable[..., str], /) -> bool:
    pattern = rf".+/vega-datasets@.+/data/{name}\..+"
    url = fn_url(name)
    return re.match(pattern, url) is not None


def is_polars_backed_pyarrow(loader: Loader[Any, Any], /) -> bool:
    """
    User requested ``pyarrow``, but also has ``polars`` installed.

    Both support nested datatypes, which are required for spatial json.
    """
    return (
        is_loader_backend(loader, "pyarrow")
        and "earthquakes" in loader._reader.profile()["supported"]
    )


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
    assert is_url("volcano", load.url)


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


@pytest.mark.parametrize(
    "name",
    [
        "jobs",
        "la-riots",
        "londonBoroughs",
        "londonCentroids",
        "londonTubeLines",
        "lookup_groups",
        "lookup_people",
        "miserables",
        "monarchs",
        "movies",
        "normal-2d",
        "obesity",
        "ohlc",
        "penguins",
        "platformer-terrain",
        "political-contributions",
        "population",
        "population_engineers_hurricanes",
        "unemployment",
        "seattle-weather",
        "seattle-weather-hourly-normals",
        "gapminder-health-income",
        "sp500",
        "sp500-2000",
        "stocks",
        "udistrict",
    ],
)
def test_url(name: Dataset) -> None:
    from altair.datasets import url

    assert is_url(name, url)


def test_url_no_backend(monkeypatch: pytest.MonkeyPatch) -> None:
    from altair.datasets._cache import csv_cache
    from altair.datasets._reader import infer_backend

    priority: Any = ("fake_mod_1", "fake_mod_2", "fake_mod_3", "fake_mod_4")
    assert csv_cache._mapping == {}
    with pytest.raises(AltairDatasetsError):
        infer_backend(priority=priority)

    url = csv_cache.url
    assert is_url("jobs", url)
    assert csv_cache._mapping != {}
    assert is_url("cars", url)
    assert is_url("stocks", url)
    assert is_url("countries", url)
    assert is_url("crimea", url)
    assert is_url("disasters", url)
    assert is_url("driving", url)
    assert is_url("earthquakes", url)
    assert is_url("flare", url)
    assert is_url("flights-10k", url)
    assert is_url("flights-200k", url)
    if find_spec("vegafusion"):
        assert is_url("flights-3m", url)

    with monkeypatch.context() as mp:
        mp.setitem(sys.modules, "vegafusion", None)
        with pytest.raises(AltairDatasetsError, match=r".parquet.+require.+vegafusion"):
            url("flights-3m")
    with pytest.raises(
        TypeError, match="'fake data' does not refer to a known dataset"
    ):
        url("fake data")


@backends
def test_loader_call(backend: _Backend) -> None:
    load = Loader.from_backend(backend)
    frame = load("stocks", ".csv")
    assert nw_dep.is_into_dataframe(frame)
    nw_frame = nw.from_native(frame)
    assert set(nw_frame.columns) == {"symbol", "date", "price"}


@backends
def test_dataset_not_found(backend: _Backend) -> None:
    """Various queries that should **always raise** due to non-existent dataset."""
    load = Loader.from_backend(backend)
    real_name: Literal["disasters"] = "disasters"
    invalid_name: Literal["fake name"] = "fake name"
    invalid_suffix: Literal["fake suffix"] = "fake suffix"
    incorrect_suffix: Literal[".json"] = ".json"
    ERR_NO_RESULT = ValueError
    MSG_NO_RESULT = "Found no results for"
    NAME = "dataset_name"
    SUFFIX = "suffix"

    with pytest.raises(
        ERR_NO_RESULT,
        match=re.compile(rf"{MSG_NO_RESULT}.+{NAME}.+{invalid_name}", re.DOTALL),
    ):
        load.url(invalid_name)
    with pytest.raises(
        TypeError,
        match=re.compile(
            rf"Expected '{SUFFIX}' to be one of.+\(.+\).+but got.+{invalid_suffix}",
            re.DOTALL,
        ),
    ):
        load.url(real_name, invalid_suffix)  # type: ignore[arg-type]
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

    fake_name = "not_a_real_package"
    real_name = "altair"
    fake_extra = "AnotherFakePackage"
    backend = f"{real_name}[{fake_extra}]"
    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{fake_name}.+requires.+{fake_name}.+but.+{fake_name}.+not.+found.+pip install {fake_name}",
            flags=re.DOTALL,
        ),
    ):
        _import_guarded(fake_name)  # type: ignore
    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{re.escape(backend)}.+requires.+'{real_name}', '{fake_extra}'.+but.+{fake_extra}.+not.+found.+pip install {fake_extra}",
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
        rd.dataset("flights-3m")
    with pytest.raises(
        AltairDatasetsError,
        match=re.compile(r"Found no.+support.+flights.+json", flags=re.DOTALL),
    ):
        rd.dataset("flights-2k")
    with pytest.raises(
        AltairDatasetsError, match=re.compile(r"Image data is non-tabular")
    ):
        rd.dataset("7zip")


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

    # smallest csvs
    lookup_groups = load("lookup_groups")
    load("lookup_people")
    load("iowa-electricity")
    load("global-temp")
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
    load("iowa-electricity", ".csv")
    load("global-temp", ".csv")
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
        - The logic for detecting the cache contents uses ``narhwals``
        - Here, we're testing that these ``narwhals`` ops are consistent
    - `DatasetCache.download_all` is expensive for CI, so aiming for it to run **at most once**
        - 34-45s per call (4x backends)
    """
    polars_loader.cache.download_all()
    CLONED: Path = tmp_path / "clone"
    fs.mkdir(CLONED)
    fs.copytree(polars_loader.cache.path, CLONED)

    monkeypatch.setenv(CACHE_ENV_VAR, str(tmp_path))
    load = Loader.from_backend(backend)
    assert load.cache.is_active()
    cache_dir = load.cache.path
    assert cache_dir == tmp_path
    assert tuple(load.cache) == (CLONED,)
    load.cache.path = CLONED
    cached_paths = tuple(load.cache)
    assert cached_paths != ()

    # NOTE: Approximating all datasets downloaded
    assert len(cached_paths) >= 70
    assert all(bool(fp.exists() and fp.stat().st_size) for fp in load.cache)
    # NOTE: Confirm this is a no-op
    load.cache.download_all()
    assert len(cached_paths) == len(tuple(load.cache))

    # NOTE: Ensure unrelated files in the directory are not removed
    dummy: Path = tmp_path / "dummy.json"
    dummy.touch(exist_ok=False)
    load.cache.clear()

    remaining = tuple(tmp_path.iterdir())
    assert set(remaining) == {dummy, CLONED}
    fs.rm(dummy, CLONED)


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
    load.cache.path = None  # type: ignore[assignment]
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
def test_spatial(backend: _Backend, name: Dataset) -> None:
    load = Loader.from_backend(backend)
    if is_polars_backed_pyarrow(load):
        assert nw_dep.is_pyarrow_table(load(name))
    else:
        pattern = re.compile(
            rf"{name}.+geospatial.+native.+{re.escape(backend)}.+try.+polars.+url",
            flags=re.DOTALL | re.IGNORECASE,
        )
        with pytest.raises(AltairDatasetsError, match=pattern):
            load(name)


@backends
def test_tsv(backend: _Backend) -> None:
    load = Loader.from_backend(backend)
    is_frame_backend(load("unemployment", ".tsv"), backend)


@datasets_all
@datasets_debug
def test_all_datasets(polars_loader: PolarsLoader, name: Dataset) -> None:
    if name in {"7zip", "ffox", "gimp"}:
        pattern = re.compile(
            rf"Unable to load.+{name}.png.+as tabular data",
            flags=re.DOTALL | re.IGNORECASE,
        )
        with pytest.raises(AltairDatasetsError, match=pattern):
            polars_loader(name)
    else:
        frame = polars_loader(name)
        assert nw_dep.is_polars_dataframe(frame)


def _raise_exception(e: type[Exception], *args: Any, **kwds: Any):
    raise e(*args, **kwds)


def test_no_remote_connection(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from polars.testing import assert_frame_equal

    load = Loader.from_backend("polars")
    load.cache.path = tmp_path
    load("londonCentroids")
    load("stocks")
    load("driving")
    cached_paths = tuple(tmp_path.iterdir())
    assert len(cached_paths) == 3
    raiser = partial(_raise_exception, URLError)
    with monkeypatch.context() as mp:
        mp.setattr(load._reader._opener, "open", raiser)
        # Existing cache entries don't trigger an error
        load("londonCentroids")
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


@pytest.mark.parametrize(
    ("name", "column"),
    [
        ("cars", "Year"),
        ("unemployment-across-industries", "date"),
        ("flights-10k", "date"),
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
        ("co2-concentration", "Date"),
        ("crimea", "date"),
        ("football", "date"),
        ("iowa-electricity", "year"),
        ("la-riots", "death_date"),
        ("ohlc", "date"),
        ("seattle-weather-hourly-normals", "date"),
        ("seattle-weather", "date"),
        ("sp500-2000", "date"),
        ("unemployment-across-industries", "date"),
        ("us-employment", "month"),
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
    kwds_empty: dict[str, Any] = {k: [] for k in kwds}
    df_schema_derived: pd.DataFrame = load(name)
    nw_schema = nw.from_native(df_schema_derived).schema
    df_manually_specified: pd.DataFrame = load(name, **kwds)
    df_dates_empty: pd.DataFrame = load(name, **kwds_empty)

    assert set(date_columns).issubset(nw_schema)
    for column in date_columns:
        assert nw_schema[column] in {nw.Date, nw.Datetime}

    assert nw_schema == nw.from_native(df_manually_specified).schema
    assert nw_schema != nw.from_native(df_dates_empty).schema

    # NOTE: Checking `polars` infers the same[1] as what `pandas` needs a hint for
    # [1] Doesn't need to be exact, just recognise as *some kind* of date/datetime
    pl_schema: pl.Schema = polars_loader(name).schema
    for column in date_columns:
        assert pl_schema[column].is_temporal()
