from __future__ import annotations

import contextlib
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
from narwhals.dependencies import (
    is_into_dataframe,
    is_pandas_dataframe,
    is_polars_dataframe,
    is_pyarrow_table,
)
from narwhals.stable import v1 as nw

from altair.datasets import Loader, url
from altair.datasets._readers import _METADATA, AltairDatasetsError
from altair.datasets._typing import Dataset, Extension, Metadata, Version, is_ext_read
from tests import skip_requires_pyarrow, slow

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping
    from pathlib import Path
    from typing import Literal

    import polars as pl
    from _pytest.mark.structures import ParameterSet

    from altair.datasets._readers import _Backend, _Polars
    from tests import MarksType

CACHE_ENV_VAR: Literal["ALTAIR_DATASETS_DIR"] = "ALTAIR_DATASETS_DIR"


class DatasetSpec(TypedDict, total=False):
    """Exceptional cases which cannot rely on defaults."""

    name: Dataset
    suffix: Extension
    tag: Version
    marks: MarksType


requires_pyarrow: pytest.MarkDecorator = skip_requires_pyarrow()

backends: pytest.MarkDecorator = pytest.mark.parametrize(
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
        pytest.param("pandas[pyarrow]", marks=requires_pyarrow),
        pytest.param("pyarrow", marks=requires_pyarrow),
    ],
)

datasets_debug: pytest.MarkDecorator = pytest.mark.datasets_debug()
"""
Custom ``pytest.mark`` decorator.

Use for more exhaustive tests that require many requests.

**Disabled** by default in ``pyproject.toml``:

    [tool.pytest.ini_options]
    addopts = ...
"""


@pytest.fixture
def is_flaky_datasets(request: pytest.FixtureRequest) -> bool:
    mark_filter = request.config.getoption("-m", None)  # pyright: ignore[reportArgumentType]
    if mark_filter is None:
        return False
    elif mark_filter == "":
        return True
    elif isinstance(mark_filter, str):
        return False
    else:
        raise TypeError(mark_filter)


@pytest.fixture(scope="session")
def polars_loader(
    tmp_path_factory: pytest.TempPathFactory,
) -> Loader[pl.DataFrame, pl.LazyFrame]:
    data = Loader.from_backend("polars")
    data.cache.path = tmp_path_factory.mktemp("loader-cache-polars")
    return data


@pytest.fixture
def metadata_columns() -> frozenset[str]:
    """
    Returns all defined keys ``Metadata`` (``TypedDict``).

    Note
    ----
    - ``# type: ignore``(s) are to fix a false positive.
    - Should be recognised by this stub `typing_extensions.pyi`_

    .. _typing_extensions.pyi:
        https://github.com/python/typeshed/blob/51d0f0194c27347ab7d0083bd7b11210a09fef75/stdlib/typing_extensions.pyi#L222-L229
    """
    return Metadata.__required_keys__.union(
        Metadata.__optional_keys__,
        Metadata.__readonly_keys__,  # type: ignore[attr-defined]
        Metadata.__mutable_keys__,  # type: ignore[attr-defined]
    )


def match_url(name: Dataset, url: str) -> bool:
    return (
        re.match(rf".+jsdelivr\.net/npm/vega-datasets@.+/data/{name}\..+", url)
        is not None
    )


@backends
def test_loader_from_backend(backend: _Backend) -> None:
    data = Loader.from_backend(backend)
    assert data._reader._name == backend


@backends
def test_loader_url(backend: _Backend) -> None:
    data = Loader.from_backend(backend)
    dataset_name: Dataset = "volcano"
    assert match_url(dataset_name, data.url(dataset_name))


def test_load(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Inferring the best backend available.

    Based on the following order:

        priority: Sequence[_Backend] = "polars", "pandas[pyarrow]", "pandas", "pyarrow"
    """
    import altair.datasets._loader
    from altair.datasets import load

    assert load._reader._name == "polars"
    monkeypatch.delattr(altair.datasets._loader, "load", raising=False)

    monkeypatch.setitem(sys.modules, "polars", None)

    from altair.datasets import load

    if find_spec("pyarrow") is None:
        # NOTE: We can end the test early for the CI job that removes `pyarrow`
        assert load._reader._name == "pandas"
        monkeypatch.delattr(altair.datasets._loader, "load")
        monkeypatch.setitem(sys.modules, "pandas", None)
        with pytest.raises(AltairDatasetsError, match="no.+backend"):
            from altair.datasets import load
    else:
        assert load._reader._name == "pandas[pyarrow]"
        monkeypatch.delattr(altair.datasets._loader, "load")

        monkeypatch.setitem(sys.modules, "pyarrow", None)

        from altair.datasets import load

        assert load._reader._name == "pandas"
        monkeypatch.delattr(altair.datasets._loader, "load")

        monkeypatch.setitem(sys.modules, "pandas", None)
        monkeypatch.delitem(sys.modules, "pyarrow")
        monkeypatch.setitem(sys.modules, "pyarrow", import_module("pyarrow"))
        from altair.datasets import load

        assert load._reader._name == "pyarrow"
        monkeypatch.delattr(altair.datasets._loader, "load")
        monkeypatch.setitem(sys.modules, "pyarrow", None)

        with pytest.raises(AltairDatasetsError, match="no.+backend"):
            from altair.datasets import load


# HACK: Using a fixture to get a command line option
# https://docs.pytest.org/en/stable/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options
@pytest.mark.xfail(
    is_flaky_datasets,  # type: ignore
    reason=(
        "'pandas[pyarrow]' seems to break locally when running:\n"
        ">>> pytest -p no:randomly -n logical tests -k test_datasets -m ''\n\n"
        "Possibly related:\n"
        "    https://github.com/modin-project/modin/issues/951\n"
        "    https://github.com/pandas-dev/pandas/blob/1c986d6213904fd7d9acc5622dc91d029d3f1218/pandas/io/parquet.py#L164\n"
        "    https://github.com/pandas-dev/pandas/blob/1c986d6213904fd7d9acc5622dc91d029d3f1218/pandas/io/parquet.py#L257\n"
    ),
    raises=AttributeError,
)
@requires_pyarrow
def test_load_call(monkeypatch: pytest.MonkeyPatch) -> None:
    import altair.datasets._loader

    monkeypatch.delattr(altair.datasets._loader, "load", raising=False)
    from altair.datasets import load

    assert load._reader._name == "polars"

    default = load("cars")
    df_pyarrow = load("cars", backend="pyarrow")
    df_pandas = load("cars", backend="pandas[pyarrow]")
    default_2 = load("cars")
    df_polars = load("cars", backend="polars")

    assert is_polars_dataframe(default)
    assert is_pyarrow_table(df_pyarrow)
    assert is_pandas_dataframe(df_pandas)
    assert is_polars_dataframe(default_2)
    assert is_polars_dataframe(df_polars)


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
        "points",
        "political-contributions",
        "population",
        "population_engineers_hurricanes",
        "seattle-temps",
        "seattle-weather",
        "seattle-weather-hourly-normals",
        "sf-temps",
        "sp500",
        "sp500-2000",
        "stocks",
        "udistrict",
    ],
)
def test_url(name: Dataset) -> None:
    from altair.datasets import url

    assert match_url(name, url(name))


def test_url_no_backend(monkeypatch: pytest.MonkeyPatch) -> None:
    import altair.datasets
    from altair.datasets._cache import url_cache

    monkeypatch.setitem(sys.modules, "polars", None)
    monkeypatch.setitem(sys.modules, "pandas", None)
    monkeypatch.setitem(sys.modules, "pyarrow", None)

    assert url_cache._mapping == {}

    with contextlib.suppress(AltairDatasetsError):
        monkeypatch.delattr(altair.datasets._loader, "load", raising=False)
    with pytest.raises(AltairDatasetsError):
        from altair.datasets import load as load

    assert match_url("jobs", url("jobs"))

    assert url_cache._mapping != {}

    assert match_url("cars", url("cars"))
    assert match_url("stocks", url("stocks"))
    assert match_url("countries", url("countries"))
    assert match_url("crimea", url("crimea"))
    assert match_url("disasters", url("disasters"))
    assert match_url("driving", url("driving"))
    assert match_url("earthquakes", url("earthquakes"))
    assert match_url("flare", url("flare"))
    assert match_url("flights-10k", url("flights-10k"))
    assert match_url("flights-200k", url("flights-200k"))

    with pytest.raises(TypeError, match="cannot be loaded via url"):
        url("climate")

    with pytest.raises(TypeError, match="cannot be loaded via url"):
        url("flights-3m")

    with pytest.raises(
        TypeError, match="'fake data' does not refer to a known dataset"
    ):
        url("fake data")


@backends
def test_loader_call(backend: _Backend, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(CACHE_ENV_VAR, raising=False)

    data = Loader.from_backend(backend)
    frame = data("stocks", ".csv")
    assert is_into_dataframe(frame)
    nw_frame = nw.from_native(frame)
    assert set(nw_frame.columns) == {"symbol", "date", "price"}


@backends
def test_missing_dependency_single(
    backend: _Backend, monkeypatch: pytest.MonkeyPatch
) -> None:
    if backend == "pandas[pyarrow]":
        pytest.skip("Testing single dependency backends only")

    monkeypatch.setitem(sys.modules, backend, None)

    with pytest.raises(
        ModuleNotFoundError,
        match=re.compile(
            rf"{backend}.+requires.+{backend}.+but.+{backend}.+not.+found.+pip install {backend}",
            flags=re.DOTALL,
        ),
    ):
        Loader.from_backend(backend)


@pytest.mark.parametrize("backend", ["pandas[pyarrow]"])
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
        Loader.from_backend(backend)


@backends
def test_dataset_not_found(backend: _Backend) -> None:
    """
    Various queries that should **always raise** due to non-existent dataset.

    ``Loader.url`` is used since it doesn't require a remote connection.
    """
    import polars as pl

    data = Loader.from_backend(backend)
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


@backends
def test_reader_cache(
    backend: _Backend, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """
    Using a sample of the smallest datasets, make *"requests"* that are all caught by prior hits.

    Note
    ----
    `tmp_path`_ is a built-in fixture.

    .. _tmp_path:
        https://docs.pytest.org/en/stable/getting-started.html#request-a-unique-temporary-directory-for-functional-tests
    """
    import polars as pl
    from polars.testing import assert_frame_equal

    monkeypatch.setenv(CACHE_ENV_VAR, str(tmp_path))

    data = Loader.from_backend(backend)
    assert data.cache.is_active()
    cache_dir = data.cache.path
    assert cache_dir == tmp_path

    assert tuple(data.cache) == ()

    # smallest csvs
    lookup_groups = data("lookup_groups", tag="v2.5.3")
    data("lookup_people", tag="v2.4.0")
    data("iowa-electricity", tag="v2.3.1")
    data("global-temp", tag="v2.9.0")

    cached_paths = tuple(data.cache)
    assert len(cached_paths) == 4

    if is_polars_dataframe(lookup_groups):
        left, right = (
            lookup_groups,
            cast(pl.DataFrame, data("lookup_groups", tag="v2.5.3")),
        )
    else:
        left, right = (
            pl.DataFrame(lookup_groups),
            pl.DataFrame(data("lookup_groups", tag="v2.5.3")),
        )

    assert_frame_equal(left, right)
    assert len(tuple(data.cache)) == 4
    assert cached_paths == tuple(data.cache)

    data("iowa-electricity", tag="v1.30.2")
    data("global-temp", tag="v2.8.1")
    data("global-temp", tag="v2.8.0")

    assert len(tuple(data.cache)) == 4
    assert cached_paths == tuple(data.cache)

    data("lookup_people", tag="v1.10.0")
    data("lookup_people", tag="v1.11.0")
    data("lookup_people", tag="v1.20.0")
    data("lookup_people", tag="v1.21.0")
    data("lookup_people", tag="v2.1.0")
    data("lookup_people", tag="v2.3.0")
    data("lookup_people", tag="v2.5.0-next.0")

    assert len(tuple(data.cache)) == 4
    assert cached_paths == tuple(data.cache)


@slow
@datasets_debug
@backends
def test_reader_cache_exhaustive(
    backend: _Backend, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """
    Fully populate and then purge the cache for all backends.

    - Does not attempt to read the files
    - Checking we can support pre-downloading and safely deleting
    """
    monkeypatch.setenv(CACHE_ENV_VAR, str(tmp_path))
    data = Loader.from_backend(backend)
    assert data.cache.is_active()
    cache_dir = data.cache.path
    assert cache_dir == tmp_path
    assert tuple(data.cache) == ()

    data.cache.download_all()
    cached_paths = tuple(data.cache)
    assert cached_paths != ()

    # NOTE: Approximating all datasets downloaded
    assert len(cached_paths) >= 40
    assert all(
        bool(fp.exists() and is_ext_read(fp.suffix) and fp.stat().st_size)
        for fp in data.cache
    )
    # NOTE: Confirm this is a no-op
    data.cache.download_all()
    assert len(cached_paths) == len(tuple(data.cache))

    # NOTE: Ensure unrelated files in the directory are not removed
    dummy: Path = tmp_path / "dummy.json"
    dummy.touch(exist_ok=False)
    data.cache.clear()

    remaining = tuple(tmp_path.iterdir())
    assert len(remaining) == 1
    assert remaining[0] == dummy
    dummy.unlink()


movies_fail: ParameterSet = pytest.param(
    "movies",
    marks=pytest.mark.xfail(
        reason="Only working for `polars`.\n"
        "`pyarrow` isn't happy with the mixed `int`/`str` column."
    ),
)
earthquakes_fail: ParameterSet = pytest.param(
    "earthquakes",
    marks=pytest.mark.xfail(
        reason="Only working for `polars`.\n" "GeoJSON fails on native `pyarrow`"
    ),
)


@pytest.mark.parametrize(
    "name",
    [
        "cars",
        movies_fail,
        "wheat",
        "barley",
        "gapminder",
        "income",
        "burtin",
        earthquakes_fail,
    ],
)
@pytest.mark.parametrize("fallback", ["polars", None])
@skip_requires_pyarrow
def test_pyarrow_read_json(
    fallback: _Polars | None, name: Dataset, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv(CACHE_ENV_VAR, raising=False)
    monkeypatch.delitem(sys.modules, "pandas", raising=False)
    if fallback is None:
        monkeypatch.setitem(sys.modules, "polars", None)

    data = Loader.from_backend("pyarrow")

    data(name, ".json")


@pytest.mark.parametrize(
    ("spec", "column"),
    [
        (DatasetSpec(name="cars", tag="v2.11.0"), "Year"),
        (DatasetSpec(name="unemployment-across-industries", tag="v2.11.0"), "date"),
        (DatasetSpec(name="flights-10k", tag="v2.11.0"), "date"),
        (DatasetSpec(name="football", tag="v2.11.0"), "date"),
        (DatasetSpec(name="crimea", tag="v2.11.0"), "date"),
        (DatasetSpec(name="ohlc", tag="v2.11.0"), "date"),
    ],
)
def test_polars_read_json_roundtrip(
    polars_loader: Loader[pl.DataFrame, pl.LazyFrame],
    spec: DatasetSpec,
    column: str,
) -> None:
    frame = polars_loader(spec["name"], ".json", tag=spec["tag"])
    tp = frame.schema.to_python()[column]
    assert tp is dt.date or issubclass(tp, dt.date)


def _dataset_params(overrides: Mapping[Dataset, DatasetSpec]) -> Iterator[ParameterSet]:
    """https://github.com/vega/vega-datasets/issues/627."""
    names: tuple[Dataset, ...] = get_args(Dataset)
    args: tuple[Dataset, Extension | None, Version | None]
    for name in names:
        marks: MarksType = ()
        if name in overrides:
            el = overrides[name]
            args = name, el.get("suffix"), el.get("tag")
            marks = el.get("marks", ())
        else:
            args = name, None, None
        yield pytest.param(*args, marks=marks)


@slow
@datasets_debug
@pytest.mark.parametrize(
    ("name", "suffix", "tag"),
    list(_dataset_params({"flights-3m": DatasetSpec(tag="v2.11.0")})),
)
def test_all_datasets(
    polars_loader: Loader[pl.DataFrame, pl.LazyFrame],
    name: Dataset,
    suffix: Extension,
    tag: Version,
) -> None:
    """Ensure all annotated datasets can be loaded with the most reliable backend."""
    frame = polars_loader(name, suffix, tag=tag)
    assert is_polars_dataframe(frame)


def _raise_exception(e: type[Exception], *args: Any, **kwds: Any):
    raise e(*args, **kwds)


def test_no_remote_connection(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from polars.testing import assert_frame_equal

    data = Loader.from_backend("polars")
    data.cache.path = tmp_path

    data("londonCentroids")
    data("stocks")
    data("driving")

    cached_paths = tuple(tmp_path.iterdir())
    assert len(cached_paths) == 3

    raiser = partial(_raise_exception, URLError)
    with monkeypatch.context() as mp:
        mp.setattr(data._reader._opener, "open", raiser)
        # Existing cache entries don't trigger an error
        data("londonCentroids")
        data("stocks")
        data("driving")
        # Mocking cache-miss without remote conn
        with pytest.raises(URLError):
            data("birdstrikes")
        assert len(tuple(tmp_path.iterdir())) == 3

    # Now we can get a cache-hit
    frame = data("birdstrikes")
    assert is_polars_dataframe(frame)
    assert len(tuple(tmp_path.iterdir())) == 4

    with monkeypatch.context() as mp:
        mp.setattr(data._reader._opener, "open", raiser)
        # Here, the remote conn isn't considered - we already have the file
        frame_from_cache = data("birdstrikes")
        assert len(tuple(tmp_path.iterdir())) == 4

    assert_frame_equal(frame, frame_from_cache)


@backends
def test_metadata_columns(backend: _Backend, metadata_columns: frozenset[str]) -> None:
    """Ensure all backends will query the same column names."""
    data = Loader.from_backend(backend)
    fn = data._reader.scan_fn(_METADATA)
    native = fn(_METADATA)
    schema_columns = nw.from_native(native).lazy().collect().columns
    assert set(schema_columns) == metadata_columns
