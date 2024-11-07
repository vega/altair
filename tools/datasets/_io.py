"""
Will be part of the public ``alt.datasets`` subpackage.

- Interfacing with the cached metadata.
    - But not updating it
- Performing requests from those urls
- Dispatching read function on file extension

Note
----
- Building with ``polars`` first, then will work backwards with ``narwhals``.
    - Since ``narwhals`` is a subset of ``polars``
"""

from __future__ import annotations

import os
import urllib.request
from functools import partial
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
import pandas as pd
import polars as pl
from narwhals.typing import IntoDataFrameT, IntoExpr, IntoFrameT

if TYPE_CHECKING:
    import sys
    from urllib.request import OpenerDirector

    from _typeshed import StrPath

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

    from tools.datasets._typing import DatasetName, Extension, VersionTag
    from tools.datasets.models import Metadata
    from tools.schemapi.utils import OneOrSeq

    _ExtensionScan: TypeAlias = Literal[".parquet"]
    _T = TypeVar("_T")


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
    _metadata: Path

    @property
    def _datasets_dir(self) -> Path | None:  # type: ignore[return]
        """
        Returns path to datasets cache, if possible.

        Requires opt-in via environment variable::

            Reader._ENV_VAR
        """
        if _dir := os.environ.get(self._ENV_VAR):
            datasets_dir = Path(_dir)
            datasets_dir.mkdir(exist_ok=True)
            return datasets_dir

    def reader_from(self, source: StrPath, /) -> Callable[..., IntoDataFrameT]:
        suffix = validate_suffix(source, is_ext_supported)
        return self._read_fn[suffix]

    def scanner_from(self, source: StrPath, /) -> Callable[..., IntoFrameT]:
        suffix = validate_suffix(source, is_ext_scan)
        return self._scan_fn[suffix]

    def url(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
    ) -> str:
        df = self._query(**validate_constraints(name, ext, tag))
        url = df.item(0, "url_npm")
        if isinstance(url, str):
            return url
        else:
            msg = f"Expected 'str' but got {type(url).__name__!r} from {url!r}."
            raise TypeError(msg)

    def dataset(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        """
        Fetch a remote dataset, attempt caching if possible.

        Parameters
        ----------
        name, ext, tag
            TODO
        **kwds
            Arguments passed to the underlying read function.
        """
        df = self._query(**validate_constraints(name, ext, tag))
        it = islice(df.iter_rows(named=True), 1)
        result = cast("Metadata", next(it))
        url = result["url_npm"]
        fn = self.reader_from(url)

        if cache := self._datasets_dir:
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


class _PandasPyArrowReader(_Reader["pd.DataFrame", "pd.DataFrame"]):
    _read_fn = {
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
    _scan_fn = {".parquet": partial(pd.read_parquet, dtype_backend="pyarrow")}

    def __init__(self, metadata: Path, /) -> None:
        self._metadata = metadata


class _PandasReader(_Reader["pd.DataFrame", "pd.DataFrame"]):
    _read_fn = {
        ".csv": pd.read_csv,
        ".json": pd.read_json,
        ".tsv": cast(partial["pd.DataFrame"], partial(pd.read_csv, sep="\t")),
        ".arrow": pd.read_feather,
    }
    _scan_fn = {".parquet": pd.read_parquet}

    def __init__(self, metadata: Path, /) -> None:
        self._metadata = metadata


class _PolarsReader(_Reader["pl.DataFrame", "pl.LazyFrame"]):
    _read_fn = {
        ".csv": pl.read_csv,
        ".json": pl.read_json,
        ".tsv": partial(pl.read_csv, separator="\t"),
        ".arrow": partial(pl.read_ipc, use_pyarrow=True),
    }
    _scan_fn = {".parquet": pl.scan_parquet}

    def __init__(self, metadata: Path, /) -> None:
        self._metadata = metadata


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
    ext: Extension | None,
    tag: VersionTag | Literal["latest"] | None,
    /,
) -> Metadata:
    constraints: Metadata = {}
    if tag == "latest":
        raise NotImplementedError(tag)
    elif tag is not None:
        constraints["tag"] = tag
    if name.endswith((".csv", ".json", ".tsv", ".arrow")):
        fp = Path(name)
        constraints["dataset_name"] = fp.stem
        constraints["suffix"] = fp.suffix
        return constraints
    elif ext is not None:
        if not is_ext_supported(ext):
            raise TypeError(ext)
        else:
            constraints["suffix"] = ext
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
def get_backend(backend: Literal["polars"], /) -> type[_PolarsReader]: ...
@overload
def get_backend(backend: Literal["pandas"], /) -> type[_PandasReader]: ...
@overload
def get_backend(
    backend: Literal["pandas[pyarrow]"], /
) -> type[_PandasPyArrowReader]: ...
def get_backend(
    backend: Literal["polars", "pandas", "pandas[pyarrow]"], /
) -> type[_PolarsReader] | type[_PandasPyArrowReader] | type[_PandasReader]:
    if backend == "polars":
        return _PolarsReader
    elif backend == "pandas[pyarrow]":
        return _PandasPyArrowReader
    elif backend == "pandas":
        return _PandasReader
    elif backend in {"pyarrow", "duckdb"}:
        msg = "Included in ``dev``, not investigated yet"
        raise NotImplementedError(msg)
    elif backend in {"ibis", "cudf", "dask", "modin"}:
        msg = "Supported by ``narwhals``, not investigated yet"
        raise NotImplementedError(msg)
    else:
        raise TypeError(backend)
