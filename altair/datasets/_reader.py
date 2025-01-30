"""
Backend for ``alt.datasets.Loader``.

Notes
-----
Extending would be more ergonomic if `read`, `scan`, `_constraints` were available under a single export::

    from altair.datasets import ext, reader
    import polars as pl

    impls = (
        ext.read(pl.read_parquet, ext.is_parquet),
        ext.read(pl.read_csv, ext.is_csv),
        ext.read(pl.read_json, ext.is_json),
    )
    user_reader = reader(impls)
    user_reader.dataset("airports")
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Mapping
from importlib import import_module
from importlib.util import find_spec
from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Generic, Literal, cast, overload
from urllib.request import build_opener as _build_opener

from narwhals.stable import v1 as nw
from narwhals.stable.v1.typing import IntoDataFrameT, IntoExpr
from packaging.requirements import Requirement

from altair.datasets import _readimpl
from altair.datasets._cache import CsvCache, DatasetCache, SchemaCache, _iter_metadata
from altair.datasets._constraints import is_parquet
from altair.datasets._exceptions import (
    AltairDatasetsError,
    implementation_not_found,
    module_not_found,
)
from altair.datasets._readimpl import IntoFrameT, is_available
from altair.datasets._typing import EXTENSION_SUFFIXES

if TYPE_CHECKING:
    import sys
    from collections.abc import Callable, Sequence
    from urllib.request import OpenerDirector

    import pandas as pd
    import polars as pl
    import pyarrow as pa

    from altair.datasets._readimpl import BaseImpl, R, Read, Scan
    from altair.datasets._typing import Dataset, Extension, Metadata
    from altair.vegalite.v5.schema._typing import OneOrSeq

    if sys.version_info >= (3, 13):
        from typing import TypeIs, TypeVar
    else:
        from typing_extensions import TypeIs, TypeVar
    if sys.version_info >= (3, 12):
        from typing import Unpack
    else:
        from typing_extensions import Unpack
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    _Polars: TypeAlias = Literal["polars"]
    _Pandas: TypeAlias = Literal["pandas"]
    _PyArrow: TypeAlias = Literal["pyarrow"]
    _PandasAny: TypeAlias = Literal[_Pandas, "pandas[pyarrow]"]
    _Backend: TypeAlias = Literal[_Polars, _PandasAny, _PyArrow]
    _CuDF: TypeAlias = Literal["cudf"]
    _Dask: TypeAlias = Literal["dask"]
    _DuckDB: TypeAlias = Literal["duckdb"]
    _Ibis: TypeAlias = Literal["ibis"]
    _PySpark: TypeAlias = Literal["pyspark"]
    _NwSupport: TypeAlias = Literal[
        _Polars, _Pandas, _PyArrow, _CuDF, _Dask, _DuckDB, _Ibis, _PySpark
    ]
    _NwSupportT = TypeVar(
        "_NwSupportT",
        _Polars,
        _Pandas,
        _PyArrow,
        _CuDF,
        _Dask,
        _DuckDB,
        _Ibis,
        _PySpark,
    )


class Reader(Generic[IntoDataFrameT, IntoFrameT]):
    """
    Modular file reader, targeting remote & local tabular resources.

    .. warning::
        Use ``reader(...)`` instead of instantiating ``Reader`` directly.
    """

    # TODO: Docs
    _read: Sequence[Read[IntoDataFrameT]]
    """Eager file read functions."""

    # TODO: Docs
    _scan: Sequence[Scan[IntoFrameT]]
    """
    *Optionally*-lazy file read/scan functions.

    Used exclusively for ``metadata.parquet``.

    Currently ``"polars"`` is the only lazy option.
    All others defer to the eager variant.
    """

    _name: str
    """
    Used in error messages, repr and matching ``@overload``(s).

    Otherwise, has no concrete meaning.
    """

    _implementation: nw.Implementation
    """
    Corresponding `narwhals implementation`_.

    .. _narwhals implementation:
        https://github.com/narwhals-dev/narwhals/blob/9b6a355530ea46c590d5a6d1d0567be59c0b5742/narwhals/utils.py#L61-L290
    """

    _opener: ClassVar[OpenerDirector] = _build_opener()
    _metadata_path: ClassVar[Path] = (
        Path(__file__).parent / "_metadata" / "metadata.parquet"
    )

    def __init__(
        self,
        read: Sequence[Read[IntoDataFrameT]],
        scan: Sequence[Scan[IntoFrameT]],
        name: str,
        implementation: nw.Implementation,
    ) -> None:
        self._read = read
        self._scan = scan
        self._name = name
        self._implementation = implementation
        self._schema_cache = SchemaCache(implementation=implementation)

    # TODO: Finish working on presentation
    # - The contents of both are functional
    def profile(self, mode: Literal["any", "each"]):
        """
        Describe which datasets/groups are supported.

        Focusing on actual datasets, rather than describing wrapped functions (repr)

        .. note::
            Having this public to make testing easier (``tests.test_datasets.is_polars_backed_pyarrow``)
        """
        if mode == "any":
            relevant_columns = set(
                chain.from_iterable(impl._relevant_columns for impl in self._read)
            )
            frame = self._scan_metadata().select("dataset_name", *relevant_columns)
            it = (impl._include_expr for impl in self._read)
            inc_expr = nw.any_horizontal(*it)
            return {
                "include": _dataset_names(frame, inc_expr),
                "exclude": _dataset_names(frame, ~inc_expr),
            }
        elif mode == "each":
            # FIXME: Rough draft of how to group results
            # - Don't really want a nested dict
            m = {}
            frame = self._scan_metadata()
            for impl in self._read:
                name = impl._contents
                m[name] = {"include": _dataset_names(frame, impl._include_expr)}
                if impl.exclude:
                    m[name].update(exclude=_dataset_names(frame, impl._exclude_expr))
            return m
        else:
            msg = f"Unexpected {mode=}"
            raise TypeError(msg)

    def __repr__(self) -> str:
        from textwrap import indent

        PREFIX = " " * 4
        NL = "\n"
        body = f"read\n{indent(NL.join(el._contents for el in self._read), PREFIX)}"
        if self._scan:
            body += (
                f"\nscan\n{indent(NL.join(el._contents for el in self._scan), PREFIX)}"
            )
        return f"Reader[{self._name}] {self._implementation!r}\n{body}"

    def read_fn(self, meta: Metadata, /) -> Callable[..., IntoDataFrameT]:
        return self._solve(meta, self._read)

    def scan_fn(self, meta: Metadata | Path | str, /) -> Callable[..., IntoFrameT]:
        meta = meta if isinstance(meta, Mapping) else {"suffix": _into_suffix(meta)}
        return self._solve(meta, self._scan)

    @property
    def cache(self) -> DatasetCache:
        return DatasetCache(self)

    def dataset(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        **kwds: Any,
    ) -> IntoDataFrameT:
        frame = self._query(name, suffix)
        meta = next(_iter_metadata(frame))
        fn = self.read_fn(meta)
        fn_kwds = self._merge_kwds(meta, kwds)
        if self.cache.is_active():
            fp = self.cache._maybe_download(meta)
            return fn(fp, **fn_kwds)
        else:
            with self._opener.open(meta["url"]) as f:
                return fn(f, **fn_kwds)

    def url(
        self, name: Dataset | LiteralString, suffix: Extension | None = None, /
    ) -> str:
        frame = self._query(name, suffix)
        meta = next(_iter_metadata(frame))
        if is_parquet(meta.items()) and not is_available("vegafusion"):
            raise AltairDatasetsError.from_url(meta)
        url = meta["url"]
        if isinstance(url, str):
            return url
        else:
            msg = f"Expected 'str' but got {type(url).__name__!r}\nfrom {url!r}."
            raise TypeError(msg)

    def _query(
        self, name: Dataset | LiteralString, suffix: Extension | None = None, /
    ) -> nw.DataFrame[IntoDataFrameT]:
        """
        Query a tabular version of `vega-datasets/datapackage.json`_.

        Applies a filter, erroring out when no results would be returned.

        .. _vega-datasets/datapackage.json:
            https://github.com/vega/vega-datasets/blob/main/datapackage.json
        """
        constraints = _into_constraints(name, suffix)
        frame = self._scan_metadata(**constraints).collect()
        if not frame.is_empty():
            return frame
        else:
            msg = f"Found no results for:\n    {constraints!r}"
            raise ValueError(msg)

    # TODO: Docs
    def _merge_kwds(self, meta: Metadata, kwds: dict[str, Any], /) -> Mapping[str, Any]:
        """
        Hook to utilize ``meta`` to extend ``kwds`` with known helpful defaults.

        - User provided arguments have a higher precedence.
        - The keywords for schemas vary between libraries
            - pandas is internally inconsistent
        - By default, returns unchanged
        """
        if self._schema_cache.is_active() and (
            schema := self._schema_cache.schema_kwds(meta)
        ):
            kwds = schema | kwds if kwds else schema
        return kwds

    @property
    def _metadata_frame(self) -> nw.LazyFrame:
        fp = self._metadata_path
        return nw.from_native(self.scan_fn(fp)(fp)).lazy()

    def _scan_metadata(
        self, *predicates: OneOrSeq[IntoExpr], **constraints: Unpack[Metadata]
    ) -> nw.LazyFrame:
        if predicates or constraints:
            return self._metadata_frame.filter(*predicates, **constraints)
        return self._metadata_frame

    # TODO: Docs
    def _solve(
        self, meta: Metadata, impls: Sequence[BaseImpl[R]], /
    ) -> Callable[..., R]:
        """
        Return the first function meeting constraints of meta.

        Notes
        -----
        - Iterate over impls
        - Each one can either match or signal an error
        - An error blocks any additional checking
            - Both include & exclude
        - Uses ``ItemsView`` to support set ops
            - `meta` isn't iterated over
            - Leaves the door open for caching the search space
        """
        items = meta.items()
        it = (some for impl in impls if (some := impl.unwrap_or_skip(items)))
        if fn_or_err := next(it, None):
            if _is_err(fn_or_err):
                raise fn_or_err.from_tabular(meta, self._name)
            return fn_or_err
        if meta["is_image"]:
            raise AltairDatasetsError.from_tabular(meta, self._name)
        raise implementation_not_found(meta)


# TODO: Review after finishing `profile`
# NOTE: Temp helper function for `Reader.profile`
def _dataset_names(
    frame: nw.LazyFrame,
    *predicates: OneOrSeq[IntoExpr],
    **constraints: Unpack[Metadata],
):
    return (
        frame.filter(*predicates, **constraints)
        .select("dataset_name")
        .collect()
        .get_column("dataset_name")
        .to_list()
    )


class _NoParquetReader(Reader[IntoDataFrameT, IntoFrameT]):
    def __repr__(self) -> str:
        return f"{super().__repr__()}\ncsv_cache\n    {self.csv_cache!r}"

    @property
    def csv_cache(self) -> CsvCache:
        if not hasattr(self, "_csv_cache"):
            self._csv_cache = CsvCache()
        return self._csv_cache

    @property
    def _metadata_frame(self) -> nw.LazyFrame:
        ns = self._implementation.to_native_namespace()
        data = cast("dict[str, Any]", self.csv_cache.rotated)
        return nw.maybe_convert_dtypes(nw.from_dict(data, native_namespace=ns)).lazy()


@overload
def reader(
    read_fns: Sequence[Read[IntoDataFrameT]],
    scan_fns: tuple[()] = ...,
    *,
    name: str | None = ...,
    implementation: nw.Implementation = ...,
) -> Reader[IntoDataFrameT, nw.LazyFrame]: ...


@overload
def reader(
    read_fns: Sequence[Read[IntoDataFrameT]],
    scan_fns: Sequence[Scan[IntoFrameT]],
    *,
    name: str | None = ...,
    implementation: nw.Implementation = ...,
) -> Reader[IntoDataFrameT, IntoFrameT]: ...


def reader(
    read_fns: Sequence[Read[IntoDataFrameT]],
    scan_fns: Sequence[Scan[IntoFrameT]] = (),
    *,
    name: str | None = None,
    implementation: nw.Implementation = nw.Implementation.UNKNOWN,
) -> Reader[IntoDataFrameT, IntoFrameT] | Reader[IntoDataFrameT, nw.LazyFrame]:
    name = name or Counter(el._inferred_package for el in read_fns).most_common(1)[0][0]
    if implementation is nw.Implementation.UNKNOWN:
        implementation = _into_implementation(Requirement(name))
    if scan_fns:
        return Reader(read_fns, scan_fns, name, implementation)
    if stolen := _steal_eager_parquet(read_fns):
        return Reader(read_fns, stolen, name, implementation)
    else:
        return _NoParquetReader[IntoDataFrameT](read_fns, (), name, implementation)


def infer_backend(
    *, priority: Sequence[_Backend] = ("polars", "pandas[pyarrow]", "pandas", "pyarrow")
) -> Reader[Any, Any]:
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
    it = (_from_backend(name) for name in priority if is_available(_requirements(name)))
    if reader := next(it, None):
        return reader
    raise AltairDatasetsError.from_priority(priority)


@overload
def _from_backend(name: _Polars, /) -> Reader[pl.DataFrame, pl.LazyFrame]: ...
@overload
def _from_backend(name: _PandasAny, /) -> Reader[pd.DataFrame, nw.LazyFrame]: ...
@overload
def _from_backend(name: _PyArrow, /) -> Reader[pa.Table, nw.LazyFrame]: ...


# FIXME: The order this is defined in makes splitting the module complicated
# - Can't use a classmethod, since some result in a subclass used
def _from_backend(name: _Backend, /) -> Reader[Any, Any]:
    """
    Reader initialization dispatcher.

    FIXME: Works, but defining these in mixed shape functions seems off.
    """
    if not _is_backend(name):
        msg = f"Unknown backend {name!r}"
        raise TypeError(msg)
    implementation = _into_implementation(name)
    if name == "polars":
        rd, sc = _readimpl.pl_only()
        return reader(rd, sc, name=name, implementation=implementation)
    elif name == "pandas[pyarrow]":
        return reader(_readimpl.pd_pyarrow(), name=name, implementation=implementation)
    elif name == "pandas":
        return reader(_readimpl.pd_only(), name=name, implementation=implementation)
    elif name == "pyarrow":
        return reader(_readimpl.pa_any(), name=name, implementation=implementation)


def _is_backend(obj: Any) -> TypeIs[_Backend]:
    return obj in {"polars", "pandas", "pandas[pyarrow]", "pyarrow"}


def _is_err(obj: Any) -> TypeIs[type[AltairDatasetsError]]:
    return obj is AltairDatasetsError


def _into_constraints(
    name: Dataset | LiteralString, suffix: Extension | None, /
) -> Metadata:
    """Transform args into a mapping to column names."""
    m: Metadata = {}
    if "." in name:
        m["file_name"] = name
    elif suffix is None:
        m["dataset_name"] = name
    elif suffix.startswith("."):
        m = {"dataset_name": name, "suffix": suffix}
    else:
        msg = (
            f"Expected 'suffix' to be one of {EXTENSION_SUFFIXES!r},\n"
            f"but got: {suffix!r}"
        )
        raise TypeError(msg)
    return m


def _into_implementation(
    backend: _NwSupport | _PandasAny | Requirement, /
) -> nw.Implementation:
    primary = _import_guarded(backend)
    mapping: Mapping[LiteralString, nw.Implementation] = {
        "polars": nw.Implementation.POLARS,
        "pandas": nw.Implementation.PANDAS,
        "pyarrow": nw.Implementation.PYARROW,
        "cudf": nw.Implementation.CUDF,
        "dask": nw.Implementation.DASK,
        "duckdb": nw.Implementation.DUCKDB,
        "ibis": nw.Implementation.IBIS,
        "pyspark": nw.Implementation.PYSPARK,
    }
    if impl := mapping.get(primary):
        return impl
    msg = f"Package {primary!r} is not supported by `narhwals`."
    raise ValueError(msg)


def _into_suffix(obj: Path | str, /) -> Any:
    if isinstance(obj, Path):
        return obj.suffix
    elif isinstance(obj, str):
        return obj
    else:
        msg = f"Unexpected type {type(obj).__name__!r}"
        raise TypeError(msg)


def _steal_eager_parquet(
    read_fns: Sequence[Read[IntoDataFrameT]], /
) -> Sequence[Scan[nw.LazyFrame]] | None:
    if convertable := next((rd for rd in read_fns if rd.include <= is_parquet), None):
        return (_readimpl.into_scan(convertable),)
    return None


@overload
def _import_guarded(req: _PandasAny, /) -> _Pandas: ...


@overload
def _import_guarded(req: _NwSupportT, /) -> _NwSupportT: ...


@overload
def _import_guarded(req: Requirement, /) -> LiteralString: ...


def _import_guarded(req: Any, /) -> LiteralString:
    requires = _requirements(req)
    for name in requires:
        if spec := find_spec(name):
            import_module(spec.name)
        else:
            raise module_not_found(str(req), requires, missing=name)
    return requires[0]


def _requirements(req: Requirement | str, /) -> tuple[Any, ...]:
    req = Requirement(req) if isinstance(req, str) else req
    return (req.name, *req.extras)
