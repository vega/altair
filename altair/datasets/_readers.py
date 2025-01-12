"""
Backends for ``alt.datasets.Loader``.

- Interfacing with the cached metadata.
    - But not updating it
- Performing requests from those urls
- Dispatching read function on file extension
"""

from __future__ import annotations

import urllib.request
from collections.abc import Iterable, Mapping, Sequence
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
    Final,
    Literal,
    Protocol,
    TypeVar,
    cast,
    overload,
)

import narwhals.stable.v1 as nw
from narwhals.stable.v1.typing import IntoDataFrameT, IntoExpr, IntoFrameT

from altair.datasets._cache import DatasetCache
from altair.datasets._typing import EXTENSION_SUFFIXES, Metadata, is_ext_read

if TYPE_CHECKING:
    import json  # noqa: F401
    import sys
    from io import IOBase
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

    from altair.datasets._typing import Dataset, Extension, Metadata, Version
    from altair.vegalite.v5.schema._typing import OneOrSeq

    _ExtensionScan: TypeAlias = Literal[".parquet"]
    _T = TypeVar("_T")

    # NOTE: Using a constrained instead of bound `TypeVar`
    #       error: Incompatible return value type (got "DataFrame[Any] | LazyFrame[Any]", expected "FrameT")  [return-value]
    # - https://typing.readthedocs.io/en/latest/spec/generics.html#introduction
    # - https://typing.readthedocs.io/en/latest/spec/generics.html#type-variables-with-an-upper-bound
    # https://github.com/narwhals-dev/narwhals/blob/21b8436567de3631c584ef67632317ad70ae5de0/narwhals/typing.py#L59
    FrameT = TypeVar("FrameT", nw.DataFrame[Any], nw.LazyFrame)

    _Polars: TypeAlias = Literal["polars"]
    _Pandas: TypeAlias = Literal["pandas"]
    _PyArrow: TypeAlias = Literal["pyarrow"]
    _ConcreteT = TypeVar("_ConcreteT", _Polars, _Pandas, _PyArrow)
    _PandasAny: TypeAlias = Literal[_Pandas, "pandas[pyarrow]"]
    _Backend: TypeAlias = Literal[_Polars, _PandasAny, _PyArrow]


__all__ = ["backend"]

_METADATA: Final[Path] = Path(__file__).parent / "_metadata" / "metadata.parquet"


class AltairDatasetsError(Exception): ...


class _Reader(Protocol[IntoDataFrameT, IntoFrameT]):
    """
    Describes basic IO for remote & local tabular resources.

    Subclassing this protocol directly will provide a *mostly* complete implementation.

    Each of the following must be explicitly assigned:

        _Reader._read_fn
        _Reader._scan_fn
        _Reader._name
    """

    _read_fn: Mapping[Extension, Callable[..., IntoDataFrameT]]
    """
    Eager file read functions.

    Each corresponds to a known file extension within ``vega-datasets``.
    """

    _scan_fn: Mapping[_ExtensionScan, Callable[..., IntoFrameT]]
    """
    *Optionally*-lazy file read/scan functions.

    Used exclusively for ``metadata.parquet``.

    Currently ``"polars"`` is the only lazy option.
    """

    _name: LiteralString
    """
    Used in error messages, repr and matching ``@overload``(s).

    Otherwise, has no concrete meaning.
    """

    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()

    def read_fn(self, source: StrPath, /) -> Callable[..., IntoDataFrameT]:
        return self._read_fn[_extract_suffix(source, is_ext_read)]

    def scan_fn(self, source: StrPath, /) -> Callable[..., IntoFrameT]:
        return self._scan_fn[_extract_suffix(source, is_ext_scan)]

    def _schema_kwds(self, result: Metadata, /) -> dict[str, Any]:
        """Hook to provide additional schema metadata on read."""
        return {}

    def dataset(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: Version | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        df = self.query(**_extract_constraints(name, suffix, tag))
        it = islice(df.iter_rows(named=True), 1)
        result = cast("Metadata", next(it))
        url = result["url_npm"]
        fn = self.read_fn(url)
        if default_kwds := self._schema_kwds(result):
            kwds = default_kwds | kwds if kwds else default_kwds

        if self.cache.is_active():
            fp = self.cache.path / (result["sha"] + result["suffix"])
            if fp.exists() and fp.stat().st_size:
                return fn(fp, **kwds)
            else:
                with self._opener.open(url) as f:
                    fp.touch()
                    fp.write_bytes(f.read())
                return fn(fp, **kwds)
        else:
            with self._opener.open(url) as f:
                return fn(f, **kwds)

    def url(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: Version | None = None,
    ) -> str:
        frame = self.query(**_extract_constraints(name, suffix, tag))
        url = nw.to_py_scalar(frame.item(0, "url_npm"))
        if isinstance(url, str):
            return url
        else:
            msg = f"Expected 'str' but got {type(url).__name__!r}\nfrom {url!r}."
            raise TypeError(msg)

    def query(
        self, *predicates: OneOrSeq[IntoExpr], **constraints: Unpack[Metadata]
    ) -> nw.DataFrame[IntoDataFrameT]:
        """
        Query multi-version trees metadata.

        Applies a filter, erroring out when no results would be returned.

        Notes
        -----
        Arguments correspond to those seen in `pl.LazyFrame.filter`_.

        .. _pl.LazyFrame.filter:
            https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.filter.html
        """
        frame = self._scan_metadata(*predicates, **constraints).collect()
        if not frame.is_empty():
            return frame
        else:
            terms = "\n".join(f"{t!r}" for t in (predicates, constraints) if t)
            msg = f"Found no results for:\n    {terms}"
            raise ValueError(msg)

    def _scan_metadata(
        self, *predicates: OneOrSeq[IntoExpr], **constraints: Unpack[Metadata]
    ) -> nw.LazyFrame:
        frame = nw.from_native(self.scan_fn(_METADATA)(_METADATA)).lazy()
        if predicates or constraints:
            return frame.filter(*predicates, **constraints)
        return frame

    @property
    def cache(self) -> DatasetCache[IntoDataFrameT, IntoFrameT]:
        return DatasetCache(self)

    def _import(self, name: str, /) -> Any:
        if spec := find_spec(name):
            return import_module(spec.name)
        else:
            reqs = _requirements(self._name)  # type: ignore[call-overload]
            if isinstance(reqs, tuple):
                depends = ", ".join(f"{req!r}" for req in reqs) + " packages"
            else:
                depends = f"{reqs!r} package"

            msg = (
                f"Backend {self._name!r} requires the {depends}, but {name!r} could not be found.\n"
                f"This can be installed with pip using:\n"
                f"    pip install {name}\n"
                f"Or with conda using:\n"
                f"    conda install -c conda-forge {name}"
            )
            raise ModuleNotFoundError(msg, name=name)

    def __repr__(self) -> str:
        return f"Reader[{self._name}]"

    def __init__(self, name: LiteralString, /) -> None: ...


class _PandasReaderBase(_Reader["pd.DataFrame", "pd.DataFrame"], Protocol):
    """
    Provides temporal column names as keyword arguments on read.

    Related
    -------
    - https://github.com/vega/altair/pull/3631#issuecomment-2480816377
    - https://github.com/vega/vega-datasets/pull/631
    - https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    - https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
    """

    def _schema_kwds(self, result: Metadata, /) -> dict[str, Any]:
        from altair.datasets._cache import schema_cache

        name: Any = result["dataset_name"]
        suffix = result["suffix"]
        if cols := schema_cache.by_dtype(name, nw.Date, nw.Datetime):
            if suffix == ".json":
                return {"convert_dates": cols}
            elif suffix in {".csv", ".tsv"}:
                return {"parse_dates": cols}
        return super()._schema_kwds(result)


class _PandasReader(_PandasReaderBase):
    def __init__(self, name: _Pandas, /) -> None:
        self._name = _requirements(name)
        if not TYPE_CHECKING:
            pd = self._import(self._name)
        self._read_fn = {
            ".csv": pd.read_csv,
            ".json": pd.read_json,
            ".tsv": partial["pd.DataFrame"](pd.read_csv, sep="\t"),
            ".arrow": pd.read_feather,
            ".parquet": pd.read_parquet,
        }
        self._scan_fn = {".parquet": pd.read_parquet}


class _PandasPyArrowReader(_PandasReaderBase):
    def __init__(self, name: Literal["pandas[pyarrow]"], /) -> None:
        _pd, _pa = _requirements(name)
        self._name = name
        if not TYPE_CHECKING:
            pd = self._import(_pd)
            pa = self._import(_pa)  # noqa: F841

        self._read_fn = {
            ".csv": partial["pd.DataFrame"](pd.read_csv, dtype_backend=_pa),
            ".json": partial["pd.DataFrame"](pd.read_json, dtype_backend=_pa),
            ".tsv": partial["pd.DataFrame"](pd.read_csv, sep="\t", dtype_backend=_pa),
            ".arrow": partial(pd.read_feather, dtype_backend=_pa),
            ".parquet": partial(pd.read_parquet, dtype_backend=_pa),
        }
        self._scan_fn = {".parquet": partial(pd.read_parquet, dtype_backend=_pa)}


def _pl_read_json_roundtrip(source: Path | IOBase, /, **kwds: Any) -> pl.DataFrame:
    """
    Try to utilize better date parsing available in `pl.read_csv`_.

    `pl.read_json`_ has few options when compared to `pl.read_csv`_.

    Chaining the two together - *where possible* - is still usually faster than `pandas.read_json`_.

    .. _pl.read_json:
        https://docs.pola.rs/api/python/stable/reference/api/polars.read_json.html
    .. _pl.read_csv:
        https://docs.pola.rs/api/python/stable/reference/api/polars.read_csv.html
    .. _pandas.read_json:
        https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
    """
    from io import BytesIO

    import polars as pl

    df = pl.read_json(source, **kwds)
    if any(tp.is_nested() for tp in df.schema.dtypes()):
        # NOTE: Inferred as `(Geo|Topo)JSON`, which wouldn't be supported by `read_csv`
        return df
    buf = BytesIO()
    df.write_csv(buf)
    if kwds:
        SHARED_KWDS = {"schema", "schema_overrides", "infer_schema_length"}
        kwds = {k: v for k, v in kwds.items() if k in SHARED_KWDS}
    return pl.read_csv(buf, try_parse_dates=True, **kwds)


class _PolarsReader(_Reader["pl.DataFrame", "pl.LazyFrame"]):
    def __init__(self, name: _Polars, /) -> None:
        self._name = _requirements(name)
        if not TYPE_CHECKING:
            pl = self._import(self._name)
        self._read_fn = {
            ".csv": partial(pl.read_csv, try_parse_dates=True),
            ".json": _pl_read_json_roundtrip,
            ".tsv": partial(pl.read_csv, separator="\t", try_parse_dates=True),
            ".arrow": pl.read_ipc,
            ".parquet": pl.read_parquet,
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

    def __init__(self, name: _PyArrow, /) -> None:
        self._name = _requirements(name)
        if not TYPE_CHECKING:
            pa = self._import(self._name)
            pa_csv = self._import(f"{self._name}.csv")
            pa_feather = self._import(f"{self._name}.feather")
            pa_parquet = self._import(f"{self._name}.parquet")
            pa_read_csv = pa_csv.read_csv
            pa_read_feather = pa_feather.read_table
            pa_read_parquet = pa_parquet.read_table

            # HACK: Multiple alternatives to `pyarrow.json.read_json`
            # -------------------------------------------------------
            # NOTE: Prefer `polars` since it is zero-copy and fast (1)
            if find_spec("polars") is not None:

                def pa_read_json(source: StrPath, /, **kwds) -> pa.Table:
                    return _pl_read_json_roundtrip(source).to_arrow()

            else:
                # NOTE: Convert inline from stdlib json (2)
                import json

                pa_json = self._import(f"{self._name}.json")

                def pa_read_json(source: Any, /, **kwds) -> pa.Table:
                    if not isinstance(source, Path):
                        obj = json.load(source)
                    else:
                        with Path(source).open(encoding="utf-8") as f:
                            obj = json.load(f)
                    # NOTE: Common case of {"values": [{...}]}, missing the `"values"` keys
                    if isinstance(obj, Sequence) and isinstance(obj[0], Mapping):
                        return pa.Table.from_pylist(obj)
                    elif isinstance(obj, Mapping) and "type" in obj:
                        msg = (
                            "Inferred file as geojson, unsupported by pyarrow.\n"
                            "Try installing `polars` or using `Loader.url(...)` instead."
                        )
                        raise NotImplementedError(msg)
                    else:
                        # NOTE: Almost certainly will fail on read as of `v2.9.0`
                        return pa_json.read_json(source)

        # Stubs suggest using a dataclass, but no way to construct it
        tab_sep: Any = {"delimiter": "\t"}

        self._read_fn = {
            ".csv": pa_read_csv,
            ".json": pa_read_json,
            ".tsv": partial(pa_read_csv, parse_options=tab_sep),
            ".arrow": pa_read_feather,
            ".parquet": pa_read_parquet,
        }
        self._scan_fn = {".parquet": pa_read_parquet}


def _extract_constraints(
    name: Dataset | LiteralString, suffix: Extension | None, tag: Version | None, /
) -> Metadata:
    """Transform args into a mapping to column names."""
    constraints: Metadata = {}
    if tag is not None:
        constraints["tag"] = tag
    if name.endswith(EXTENSION_SUFFIXES):
        fp = Path(name)
        constraints["dataset_name"] = fp.stem
        constraints["suffix"] = fp.suffix
        return constraints
    elif suffix is not None:
        if not is_ext_read(suffix):
            msg = (
                f"Expected 'suffix' to be one of {EXTENSION_SUFFIXES!r},\n"
                f"but got: {suffix!r}"
            )
            raise TypeError(msg)
        else:
            constraints["suffix"] = suffix
    constraints["dataset_name"] = name
    return constraints


def _extract_suffix(source: StrPath, guard: Callable[..., TypeIs[_T]], /) -> _T:
    suffix: Any = Path(source).suffix
    if guard(suffix):
        return suffix
    else:
        msg = f"Unexpected file extension {suffix!r}, from:\n{source}"
        raise TypeError(msg)


def is_ext_scan(suffix: Any) -> TypeIs[_ExtensionScan]:
    return suffix == ".parquet"


def is_available(pkg_names: str | Iterable[str], *more_pkg_names: str) -> bool:
    pkgs_names = pkg_names if not isinstance(pkg_names, str) else (pkg_names,)
    names = chain(pkgs_names, more_pkg_names)
    return all(find_spec(name) is not None for name in names)


def infer_backend(
    *, priority: Sequence[_Backend] = ("polars", "pandas[pyarrow]", "pandas", "pyarrow")
) -> _Reader[Any, Any]:
    """
    Return the first available reader in order of `priority`.

    Notes
    -----
    - ``"polars"``: can natively load every dataset (including ``(Geo|Topo)JSON``)
    - ``"pandas[pyarrow]"``: can load *most* datasets, guarantees ``.parquet`` support
    - ``"pandas"``: supports ``.parquet``, if `fastparquet`_ is installed
    - ``"pyarrow"``: least reliable

    .. _fastparquet:
        https://github.com/dask/fastparquet
    """
    it = (backend(name) for name in priority if is_available(_requirements(name)))
    if reader := next(it, None):
        return reader
    msg = f"Found no supported backend, searched:\n{priority!r}"
    raise AltairDatasetsError(msg)


@overload
def backend(name: _Polars, /) -> _Reader[pl.DataFrame, pl.LazyFrame]: ...


@overload
def backend(name: _PandasAny, /) -> _Reader[pd.DataFrame, pd.DataFrame]: ...


@overload
def backend(name: _PyArrow, /) -> _Reader[pa.Table, pa.Table]: ...


def backend(name: _Backend, /) -> _Reader[Any, Any]:
    """Reader initialization dispatcher."""
    if name == "polars":
        return _PolarsReader(name)
    elif name == "pandas[pyarrow]":
        return _PandasPyArrowReader(name)
    elif name == "pandas":
        return _PandasReader(name)
    elif name == "pyarrow":
        return _PyArrowReader(name)
    elif name in {"ibis", "cudf", "dask", "modin"}:
        msg = "Supported by ``narwhals``, not investigated yet"
        raise NotImplementedError(msg)
    else:
        msg = f"Unknown backend {name!r}"
        raise TypeError(msg)


@overload
def _requirements(s: _ConcreteT, /) -> _ConcreteT: ...


@overload
def _requirements(s: Literal["pandas[pyarrow]"], /) -> tuple[_Pandas, _PyArrow]: ...


def _requirements(s: _Backend, /):
    concrete: set[Literal[_Polars, _Pandas, _PyArrow]] = {"polars", "pandas", "pyarrow"}
    if s in concrete:
        return s
    else:
        from packaging.requirements import Requirement

        req = Requirement(s)
        supports_extras: set[Literal[_Pandas]] = {"pandas"}
        if req.name in supports_extras:
            name = req.name
            if (extras := req.extras) and extras == {"pyarrow"}:
                extra = "pyarrow"
                return name, extra
            else:
                raise NotImplementedError(s)
        else:
            raise NotImplementedError(s)
