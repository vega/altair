"""
Backends for ``alt.datasets.Loader``.

- Interfacing with the cached metadata.
    - But not updating it
- Performing requests from those urls
- Dispatching read function on file extension
"""

from __future__ import annotations

import os
import urllib.request
from functools import partial
from importlib import import_module
from importlib.util import find_spec
from itertools import chain, islice
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Generic,
    Literal,
    Protocol,
    TypeVar,
    cast,
    overload,
)

import narwhals.stable.v1 as nw
from narwhals.typing import IntoDataFrameT, IntoExpr, IntoFrameT

if TYPE_CHECKING:
    import sys
    from urllib.request import OpenerDirector

    import pandas as pd
    import polars as pl
    import pyarrow as pa
    from _typeshed import StrPath
    from pyarrow.csv import read_csv as pa_read_csv  # noqa: F401
    from pyarrow.feather import read_table as pa_read_feather  # noqa: F401
    from pyarrow.json import read_json as pa_read_json  # noqa: F401
    from pyarrow.parquet import read_table as pa_read_parquet  # noqa: F401

    if sys.version_info >= (3, 13):
        from typing import TypeIs, Unpack
    else:
        from typing_extensions import TypeIs, Unpack
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    from altair.datasets._typing import DatasetName, Extension, Metadata, VersionTag
    from altair.vegalite.v5.schema._typing import OneOrSeq

    _ExtensionScan: TypeAlias = Literal[".parquet"]
    _T = TypeVar("_T")
    _Backend: TypeAlias = Literal[
        "polars", "pandas", "pandas[pyarrow]", "polars[pyarrow]", "pyarrow"
    ]


__all__ = ["get_backend"]


class _Reader(Generic[IntoDataFrameT, IntoFrameT], Protocol):
    """
    Common functionality between backends.

    Trying to use ``narwhals`` as much as possible
    """

    _read_fn: dict[Extension, Callable[..., IntoDataFrameT]]
    _scan_fn: dict[_ExtensionScan, Callable[..., IntoFrameT]]
    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()
    _ENV_VAR: ClassVar[LiteralString] = "ALTAIR_DATASETS_DIR"
    _metadata: Path = Path(__file__).parent / "_metadata" / "metadata.parquet"

    @property
    def _cache(self) -> Path | None:  # type: ignore[return]
        """
        Returns path to datasets cache, if possible.

        Requires opt-in via environment variable::

            Reader._ENV_VAR
        """
        if _dir := os.environ.get(self._ENV_VAR):
            cache_dir = Path(_dir)
            cache_dir.mkdir(exist_ok=True)
            return cache_dir

    def reader_from(self, source: StrPath, /) -> Callable[..., IntoDataFrameT]:
        suffix = validate_suffix(source, is_ext_supported)
        return self._read_fn[suffix]

    def scanner_from(self, source: StrPath, /) -> Callable[..., IntoFrameT]:
        suffix = validate_suffix(source, is_ext_scan)
        return self._scan_fn[suffix]

    def url(
        self,
        name: DatasetName | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: VersionTag | None = None,
    ) -> str:
        df = self._query(**validate_constraints(name, suffix, tag))
        url = df.item(0, "url_npm")
        if isinstance(url, str):
            return url
        else:
            msg = f"Expected 'str' but got {type(url).__name__!r} from {url!r}."
            raise TypeError(msg)

    def dataset(
        self,
        name: DatasetName | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: VersionTag | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        """
        Fetch a remote dataset, attempt caching if possible.

        Parameters
        ----------
        name, suffix, tag
            TODO
        **kwds
            Arguments passed to the underlying read function.
        """
        df = self._query(**validate_constraints(name, suffix, tag))
        it = islice(df.iter_rows(named=True), 1)
        result = cast("Metadata", next(it))
        url = result["url_npm"]
        fn = self.reader_from(url)

        if cache := self._cache:
            fp = cache / (result["sha"] + result["suffix"])
            if fp.exists():
                return fn(fp, **kwds)
            else:
                fp.touch()
                with self._opener.open(url) as f:
                    fp.write_bytes(f.read())
                return fn(fp, **kwds)
        else:
            with self._opener.open(url) as f:
                return fn(f.read(), **kwds)

    def _query(
        self, *predicates: OneOrSeq[IntoExpr], **constraints: Unpack[Metadata]
    ) -> nw.DataFrame[IntoDataFrameT]:
        r"""
        Query multi-version trees metadata.

        Parameters
        ----------
        \*predicates, \*\*constraints
            Passed directly to `pl.LazyFrame.filter`_.

        .. _pl.LazyFrame.filter:
            https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.filter.html
        """
        source = self._metadata
        fn = self.scanner_from(source)
        frame = nw.from_native(fn(source), pass_through=False)
        result = frame.filter(_filter_reduce(predicates, constraints))
        df: nw.DataFrame[Any] = (
            result.collect() if isinstance(result, nw.LazyFrame) else result
        )
        if not df.is_empty():
            return df
        else:
            terms = "\n".join(f"{t!r}" for t in (predicates, constraints) if t)
            msg = f"Found no results for:\n{terms}"
            raise NotImplementedError(msg)

    def _import(self, name: str, /) -> Any:
        if spec := find_spec(name):
            return import_module(spec.name)
        else:
            msg = f"{type(self).__name__!r} requires missing dependency {name!r}."
            raise ModuleNotFoundError(msg, name=name)

    def __init__(self, *specs: str) -> None: ...


class _PandasPyArrowReader(_Reader["pd.DataFrame", "pd.DataFrame"]):
    def __init__(self, _pd: str, _pa: str, /) -> None:
        if not TYPE_CHECKING:
            pd = self._import(_pd)
            pa = self._import(_pa)  # noqa: F841

        self._read_fn = {
            ".csv": cast(
                partial["pd.DataFrame"], partial(pd.read_csv, dtype_backend="pyarrow")
            ),
            ".json": cast(
                partial["pd.DataFrame"], partial(pd.read_json, dtype_backend="pyarrow")
            ),
            ".tsv": cast(
                partial["pd.DataFrame"],
                partial(pd.read_csv, sep="\t", dtype_backend="pyarrow"),
            ),
            ".arrow": partial(pd.read_feather, dtype_backend="pyarrow"),
        }
        self._scan_fn = {".parquet": partial(pd.read_parquet, dtype_backend="pyarrow")}


class _PandasReader(_Reader["pd.DataFrame", "pd.DataFrame"]):
    def __init__(self, _pd: str, /) -> None:
        if not TYPE_CHECKING:
            pd = self._import(_pd)
        self._read_fn = {
            ".csv": pd.read_csv,
            ".json": pd.read_json,
            ".tsv": cast(partial["pd.DataFrame"], partial(pd.read_csv, sep="\t")),
            ".arrow": pd.read_feather,
        }
        self._scan_fn = {".parquet": pd.read_parquet}


class _PolarsReader(_Reader["pl.DataFrame", "pl.LazyFrame"]):
    def __init__(self, _pl: str, /) -> None:
        if not TYPE_CHECKING:
            pl = self._import(_pl)
        self._read_fn = {
            ".csv": pl.read_csv,
            ".json": pl.read_json,
            ".tsv": partial(pl.read_csv, separator="\t"),
            ".arrow": pl.read_ipc,
        }
        self._scan_fn = {".parquet": pl.scan_parquet}


class _PolarsPyArrowReader(_Reader["pl.DataFrame", "pl.LazyFrame"]):
    def __init__(self, _pl: str, _pa: str, /) -> None:
        if not TYPE_CHECKING:
            pl = self._import(_pl)
            pa = self._import(_pa)  # noqa: F841
        self._read_fn = {
            ".csv": partial(pl.read_csv, use_pyarrow=True),
            ".json": pl.read_json,
            ".tsv": partial(pl.read_csv, separator="\t", use_pyarrow=True),
            ".arrow": partial(pl.read_ipc, use_pyarrow=True),
        }
        self._scan_fn = {".parquet": pl.scan_parquet}


class _PyArrowReader(_Reader["pa.Table", "pa.Table"]):
    """
    Reader backed by `pyarrow.Table`_.

    Warning
    -------
    **JSON**: Only supports `line-delimited`_ JSON.
    Likely to raise the following error:

        ArrowInvalid: JSON parse error: Column() changed from object to array in row 0

    .. _pyarrow.Table:
        https://arrow.apache.org/docs/python/generated/pyarrow.Table.html
    .. _line-delimited:
        https://arrow.apache.org/docs/python/json.html#reading-json-files
    """

    def __init__(self, _pa: str, /) -> None:
        if not TYPE_CHECKING:
            pa = self._import(_pa)  # noqa: F841
            pa_csv = self._import(f"{_pa}.csv")
            pa_feather = self._import(f"{_pa}.feather")
            pa_json = self._import(f"{_pa}.json")
            pa_parquet = self._import(f"{_pa}.parquet")

            pa_read_csv = pa_csv.read_csv
            pa_read_feather = pa_feather.read_table
            pa_read_json = pa_json.read_json
            pa_read_parquet = pa_parquet.read_table

        # opt1 = ParseOptions(delimiter="\t")  # type: ignore
        # Stubs suggest using a dataclass, but no way to construct it
        opt2: Any = {"delimiter": "\t"}

        self._read_fn = {
            ".csv": pa_read_csv,
            ".json": pa_read_json,
            ".tsv": partial(pa_read_csv, parse_options=opt2),
            ".arrow": pa_read_feather,
        }
        self._scan_fn = {".parquet": pa_read_parquet}


def _filter_reduce(predicates: tuple[Any, ...], constraints: Metadata, /) -> nw.Expr:
    """
    ``narwhals`` only accepts ``filter(*predicates)`.

    Manually converts the constraints into ``==``
    """
    return nw.all_horizontal(
        chain(predicates, (nw.col(name) == v for name, v in constraints.items()))
    )


def validate_constraints(
    name: DatasetName | LiteralString,
    suffix: Extension | None,
    tag: VersionTag | None,
    /,
) -> Metadata:
    constraints: Metadata = {}
    if tag is not None:
        constraints["tag"] = tag
    if name.endswith((".csv", ".json", ".tsv", ".arrow")):
        fp = Path(name)
        constraints["dataset_name"] = fp.stem
        constraints["suffix"] = fp.suffix
        return constraints
    elif suffix is not None:
        if not is_ext_supported(suffix):
            raise TypeError(suffix)
        else:
            constraints["suffix"] = suffix
    constraints["dataset_name"] = name
    return constraints


def validate_suffix(source: StrPath, guard: Callable[..., TypeIs[_T]], /) -> _T:
    suffix: Any = Path(source).suffix
    if guard(suffix):
        return suffix
    else:
        msg = f"Unexpected file extension {suffix!r}, from:\n{source}"
        raise TypeError(msg)


def is_ext_scan(suffix: Any) -> TypeIs[_ExtensionScan]:
    return suffix == ".parquet"


def is_ext_supported(suffix: Any) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}


@overload
def get_backend(
    backend: Literal["polars", "polars[pyarrow]"], /
) -> _Reader[pl.DataFrame, pl.LazyFrame]: ...


@overload
def get_backend(
    backend: Literal["pandas", "pandas[pyarrow]"], /
) -> _Reader[pd.DataFrame, pd.DataFrame]: ...


@overload
def get_backend(backend: Literal["pyarrow"], /) -> _Reader[pa.Table, pa.Table]: ...


def get_backend(backend: _Backend, /) -> _Reader[Any, Any]:
    if backend == "polars":
        return _PolarsReader("polars")
    elif backend == "polars[pyarrow]":
        return _PolarsPyArrowReader("polars", "pyarrow")
    elif backend == "pandas[pyarrow]":
        return _PandasPyArrowReader("pandas", "pyarrow")
    elif backend == "pandas":
        return _PandasReader("pandas")
    elif backend == "pyarrow":
        return _PyArrowReader("pyarrow")
    elif backend in {"ibis", "cudf", "dask", "modin"}:
        msg = "Supported by ``narwhals``, not investigated yet"
        raise NotImplementedError(msg)
    else:
        raise TypeError(backend)
