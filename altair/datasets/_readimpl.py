"""Individual read functions and siuations they support."""

from __future__ import annotations

import sys
from enum import Enum
from functools import partial, wraps
from importlib.util import find_spec
from itertools import chain
from operator import itemgetter
from pathlib import Path
from typing import TYPE_CHECKING, Any, Generic, Literal

from narwhals.stable import v1 as nw
from narwhals.stable.v1.dependencies import get_pandas, get_polars
from narwhals.stable.v1.typing import IntoDataFrameT

from altair.datasets._constraints import (
    is_arrow,
    is_csv,
    is_json,
    is_meta,
    is_not_tabular,
    is_parquet,
    is_spatial,
    is_topo,
    is_tsv,
)
from altair.datasets._exceptions import AltairDatasetsError

if sys.version_info >= (3, 13):
    from typing import TypeVar
else:
    from typing_extensions import TypeVar
if sys.version_info >= (3, 12):
    from typing import TypeAliasType
else:
    from typing_extensions import TypeAliasType

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator, Sequence
    from io import IOBase
    from types import ModuleType

    import pandas as pd
    import polars as pl
    import pyarrow as pa
    from narwhals.stable.v1 import typing as nwt

    from altair.datasets._constraints import Items, MetaIs

__all__ = ["is_available", "pa_any", "pd_only", "pd_pyarrow", "pl_only", "read", "scan"]

R = TypeVar("R", bound="nwt.IntoFrame", covariant=True)
IntoFrameT = TypeVar(
    "IntoFrameT",
    bound="nwt.NativeFrame | nw.DataFrame[Any] | nw.LazyFrame[Any] | nwt.DataFrameLike",
    default=nw.LazyFrame[Any],
)
Read = TypeAliasType("Read", "BaseImpl[IntoDataFrameT]", type_params=(IntoDataFrameT,))
"""An *eager* file read function."""

Scan = TypeAliasType("Scan", "BaseImpl[IntoFrameT]", type_params=(IntoFrameT,))
"""A *lazy* file read function."""


class Skip(Enum):
    """Falsy sentinel."""

    skip = 0

    def __bool__(self) -> Literal[False]:
        return False

    def __repr__(self) -> Literal["<Skip>"]:
        return "<Skip>"


class BaseImpl(Generic[R]):
    """
    A function wrapped with dataset support constraints.

    The ``include``, ``exclude`` properties form a `NIMPLY gate`_ (`Material nonimplication`_).

    Examples
    --------
    For some dataset ``D``, we can use ``fn`` if::

        impl: BaseImpl
        impl.include(D) and not impl.exclude(D)


    .. _NIMPLY gate:
        https://en.m.wikipedia.org/wiki/NIMPLY_gate
    .. _Material nonimplication:
        https://en.m.wikipedia.org/wiki/Material_nonimplication#Truth_table
    """

    fn: Callable[..., R]
    """Wrapped read/scan function."""

    include: MetaIs
    """Constraint indicating ``fn`` **supports** reading a dataset."""

    exclude: MetaIs
    """Constraint *subsetting* ``include`` to mark **non-support**."""

    def __init__(
        self,
        fn: Callable[..., R],
        include: MetaIs,
        exclude: MetaIs | None,
        kwds: dict[str, Any],
        /,
    ) -> None:
        exclude = exclude or self._exclude_none()
        if not include.isdisjoint(exclude):
            intersection = ", ".join(f"{k}={v!r}" for k, v in include & exclude)
            msg = f"Constraints overlap at: `{intersection}`\ninclude={include!r}\nexclude={exclude!r}"
            raise TypeError(msg)
        object.__setattr__(self, "fn", partial(fn, **kwds) if kwds else fn)
        object.__setattr__(self, "include", include)
        object.__setattr__(self, "exclude", exclude)

    def unwrap_or_skip(
        self, meta: Items, /
    ) -> Callable[..., R] | type[AltairDatasetsError] | Skip:
        """
        Indicate an action to take for a dataset.

        **Supports** dataset, use this function::

            Callable[..., R]

        Has explicitly marked as **not supported**::

            type[AltairDatasetsError]

        No relevant constraints overlap, safe to check others::

            Skip
        """
        if self.include.issubset(meta):
            return self.fn if self.exclude.isdisjoint(meta) else AltairDatasetsError
        return Skip.skip

    @classmethod
    def _exclude_none(cls) -> MetaIs:
        """Represents the empty set."""
        return is_meta()

    def __setattr__(self, name: str, value: Any):
        msg = (
            f"{type(self).__name__!r} is immutable.\n"
            f"Could not assign self.{name} = {value}"
        )
        raise TypeError(msg)

    @property
    def _inferred_package(self) -> str:
        return _root_package_name(_unwrap_partial(self.fn), "UNKNOWN")

    def __repr__(self) -> str:
        tp_name = f"{type(self).__name__}[{self._inferred_package}?]"
        return f"{tp_name}({self})"

    def __str__(self) -> str:
        if isinstance(self.fn, partial):
            fn = _unwrap_partial(self.fn)
            kwds = self.fn.keywords.items()
            fn_repr = f"{fn.__name__}(..., {', '.join(f'{k}={v!r}' for k, v in kwds)})"
        else:
            fn_repr = f"{self.fn.__name__}(...)"
        inc, exc = self.include, self.exclude
        return f"{fn_repr}, {f'include={inc!r}, exclude={exc!r}' if exc else repr(inc)}"

    @property
    def _relevant_columns(self) -> Iterator[str]:
        name = itemgetter(0)
        yield from (name(obj) for obj in chain(self.include, self.exclude))

    @property
    def _include_expr(self) -> nw.Expr:
        return (
            self.include.to_expr() & ~self.exclude.to_expr()
            if self.exclude
            else self.include.to_expr()
        )

    @property
    def _exclude_expr(self) -> nw.Expr:
        if self.exclude:
            return self.include.to_expr() & self.exclude.to_expr()
        msg = f"Unable to generate an exclude expression without setting exclude\n\n{self!r}"
        raise TypeError(msg)


def read(
    fn: Callable[..., IntoDataFrameT],
    /,
    include: MetaIs,
    exclude: MetaIs | None = None,
    **kwds: Any,
) -> Read[IntoDataFrameT]:
    return BaseImpl(fn, include, exclude, kwds)


def scan(
    fn: Callable[..., IntoFrameT],
    /,
    include: MetaIs,
    exclude: MetaIs | None = None,
    **kwds: Any,
) -> Scan[IntoFrameT]:
    return BaseImpl(fn, include, exclude, kwds)


def into_scan(impl: Read[IntoDataFrameT], /) -> Scan[nw.LazyFrame[IntoDataFrameT]]:
    def scan_fn(
        fn: Callable[..., IntoDataFrameT], /
    ) -> Callable[..., nw.LazyFrame[IntoDataFrameT]]:
        @wraps(_unwrap_partial(fn))
        def wrapper(*args: Any, **kwds: Any) -> nw.LazyFrame[IntoDataFrameT]:
            return nw.from_native(fn(*args, **kwds)).lazy()

        return wrapper

    return scan(scan_fn(impl.fn), impl.include, impl.exclude)


def is_available(
    pkg_names: str | Iterable[str], *more_pkg_names: str, require_all: bool = True
) -> bool:
    """
    Check for importable package(s), without raising on failure.

    Parameters
    ----------
    pkg_names, more_pkg_names
        One or more packages.
    require_all
        * ``True`` every package.
        * ``False`` at least one package.
    """
    if not more_pkg_names and isinstance(pkg_names, str):
        return find_spec(pkg_names) is not None
    pkgs_names = pkg_names if not isinstance(pkg_names, str) else (pkg_names,)
    names = chain(pkgs_names, more_pkg_names)
    fn = all if require_all else any
    return fn(find_spec(name) is not None for name in names)


def _root_package_name(obj: Any, default: str, /) -> str:
    # NOTE: Defers importing `inspect`, if we can get the module name
    if hasattr(obj, "__module__"):
        return obj.__module__.split(".")[0]
    else:
        from inspect import getmodule

        module = getmodule(obj)
    if module and (pkg := module.__package__):
        return pkg.split(".")[0]
    return default


def _unwrap_partial(fn: Any, /) -> Any:
    # NOTE: ``functools._unwrap_partial``
    func = fn
    while isinstance(func, partial):
        func = func.func
    return func


def pl_only() -> tuple[Sequence[Read[pl.DataFrame]], Sequence[Scan[pl.LazyFrame]]]:
    import polars as pl

    pl_read_json = read(_pl_read_json_roundtrip(get_polars()), is_json)
    if is_available("polars_st"):
        fn_json: Sequence[Read[pl.DataFrame]] = (
            _pl_read_json_polars_st_topo_impl(),  # TopoJSON files first
            _pl_read_json_polars_st_impl(),  # Then other spatial JSON
            pl_read_json,
        )
    else:
        fn_json = (pl_read_json,)

    read_fns = (
        read(pl.read_csv, is_csv, try_parse_dates=True),
        *fn_json,
        read(pl.read_csv, is_tsv, separator="\t", try_parse_dates=True),
        read(pl.read_ipc, is_arrow),
        read(pl.read_parquet, is_parquet),
    )
    scan_fns = (scan(pl.scan_parquet, is_parquet),)
    return read_fns, scan_fns


def pd_only() -> Sequence[Read[pd.DataFrame]]:
    import pandas as pd

    opt: Sequence[Read[pd.DataFrame]]
    if is_available("pyarrow"):
        opt = read(pd.read_feather, is_arrow), read(pd.read_parquet, is_parquet)
    elif is_available("fastparquet"):
        opt = (read(pd.read_parquet, is_parquet),)
    else:
        opt = ()
    pd_read_json = read(_pd_read_json(get_pandas()), is_json, exclude=is_spatial)
    if is_available("geopandas"):
        fn_json: Sequence[Read[pd.DataFrame]] = (
            _pd_read_json_geopandas_impl(),
            pd_read_json,
        )
    else:
        fn_json = (pd_read_json,)
    return (
        read(pd.read_csv, is_csv),
        *fn_json,
        read(pd.read_csv, is_tsv, sep="\t"),
        *opt,
    )


def pd_pyarrow() -> Sequence[Read[pd.DataFrame]]:
    import pandas as pd

    kwds: dict[str, Any] = {"dtype_backend": "pyarrow"}
    pd_read_json = read(
        _pd_read_json(get_pandas()), is_json, exclude=is_spatial, **kwds
    )
    if is_available("geopandas"):
        fn_json: Sequence[Read[pd.DataFrame]] = (
            _pd_read_json_geopandas_impl(),
            pd_read_json,
        )
    else:
        fn_json = (pd_read_json,)
    return (
        read(pd.read_csv, is_csv, **kwds),
        *fn_json,
        read(pd.read_csv, is_tsv, sep="\t", **kwds),
        read(pd.read_feather, is_arrow, **kwds),
        read(pd.read_parquet, is_parquet, **kwds),
    )


def pa_any() -> Sequence[Read[pa.Table]]:
    from pyarrow import csv, feather, parquet

    return (
        read(csv.read_csv, is_csv),
        _pa_read_json_impl(),
        read(csv.read_csv, is_tsv, parse_options=csv.ParseOptions(delimiter="\t")),  # pyright: ignore[reportCallIssue]
        read(feather.read_table, is_arrow),
        read(parquet.read_table, is_parquet),
    )


def _pa_read_json_impl() -> Read[pa.Table]:
    """
    Mitigating ``pyarrow``'s `line-delimited`_ JSON requirement.

    .. _line-delimited:
        https://arrow.apache.org/docs/python/json.html#reading-json-files
    """
    if is_available("polars"):
        polars_ns = get_polars()
        if polars_ns is not None:
            return read(_pl_read_json_roundtrip_to_arrow(polars_ns), is_json)
    if is_available("pandas"):
        pandas_ns = get_pandas()
        if pandas_ns is not None:
            return read(_pd_read_json_to_arrow(pandas_ns), is_json, exclude=is_spatial)
    return read(_stdlib_read_json_to_arrow, is_json, exclude=is_not_tabular)


def _pd_read_json(ns: ModuleType, /) -> Callable[..., pd.DataFrame]:
    @wraps(ns.read_json)
    def fn(source: Path | Any, /, **kwds: Any) -> pd.DataFrame:
        return _pd_fix_dtypes_nw(ns.read_json(source, **kwds), **kwds).to_native()

    return fn


def _pd_read_json_geopandas_impl() -> Read[pd.DataFrame]:
    import geopandas

    @wraps(geopandas.read_file)
    def fn(source: Path | Any, /, schema: Any = None, **kwds: Any) -> pd.DataFrame:
        return geopandas.read_file(source, **kwds)

    return read(fn, is_meta(is_spatial=True, suffix=".json"))


def _pd_fix_dtypes_nw(
    df: pd.DataFrame, /, *, dtype_backend: Any = None, **kwds: Any
) -> nw.DataFrame[pd.DataFrame]:
    kwds = {"dtype_backend": dtype_backend} if dtype_backend else {}
    return (
        df.convert_dtypes(**kwds)
        .pipe(nw.from_native, eager_only=True)
        .with_columns(nw.selectors.by_dtype(nw.Object).cast(nw.String))
    )


def _pd_read_json_to_arrow(ns: ModuleType, /) -> Callable[..., pa.Table]:
    @wraps(ns.read_json)
    def fn(source: Path | Any, /, *, schema: Any = None, **kwds: Any) -> pa.Table:
        """``schema`` is only here to swallow the ``SchemaCache`` if used."""
        return (
            ns.read_json(source, **kwds)
            .pipe(_pd_fix_dtypes_nw, dtype_backend="pyarrow")
            .to_arrow()
        )

    return fn


def _pl_read_json_polars_st_impl() -> Read[pl.DataFrame]:
    import polars_st as st

    @wraps(st.read_file)
    def fn(source: Path | Any, /, schema: Any = None, **kwds: Any) -> pl.DataFrame:
        return st.read_file(source, **kwds)

    return read(fn, is_meta(is_spatial=True, suffix=".json"))


def _pl_read_json_polars_st_topo_impl() -> Read[pl.DataFrame]:
    import polars_st as st

    @wraps(st.read_file)
    def fn(source: Path | Any, /, schema: Any = None, **kwds: Any) -> pl.DataFrame:
        # Add TopoJSON driver prefix for URLs
        if isinstance(source, str) and source.startswith("http"):
            source = f"TopoJSON:{source}"
        return st.read_file(source, **kwds)

    return read(fn, is_topo)


def _pl_read_json_roundtrip(ns: ModuleType, /) -> Callable[..., pl.DataFrame]:
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

    @wraps(ns.read_json)
    def fn(source: Path | IOBase, /, **kwds: Any) -> pl.DataFrame:
        df = ns.read_json(source, **kwds)
        if any(tp.is_nested() for tp in df.schema.dtypes()):
            return df
        buf = BytesIO()
        df.write_csv(buf)
        if kwds:
            SHARED_KWDS = {"schema", "schema_overrides", "infer_schema_length"}
            kwds = {k: v for k, v in kwds.items() if k in SHARED_KWDS}
        return ns.read_csv(buf, try_parse_dates=True, **kwds)

    return fn


def _pl_read_json_roundtrip_to_arrow(ns: ModuleType, /) -> Callable[..., pa.Table]:
    eager = _pl_read_json_roundtrip(ns)

    @wraps(ns.read_json)
    def fn(source: Path | IOBase, /, **kwds: Any) -> pa.Table:
        return eager(source).to_arrow()

    return fn


def _stdlib_read_json(source: Path | Any, /) -> Any:
    import json

    if not isinstance(source, Path):
        return json.load(source)
    else:
        with Path(source).open(encoding="utf-8") as f:
            return json.load(f)


def _stdlib_read_json_to_arrow(source: Path | Any, /, **kwds: Any) -> pa.Table:
    import pyarrow as pa

    rows: list[dict[str, Any]] = _stdlib_read_json(source)
    try:
        return pa.Table.from_pylist(rows, **kwds)
    except TypeError:
        import csv
        import io

        from pyarrow import csv as pa_csv

        with io.StringIO() as f:
            writer = csv.DictWriter(f, rows[0].keys(), dialect=csv.unix_dialect)
            writer.writeheader()
            writer.writerows(rows)
            with io.BytesIO(f.getvalue().encode()) as f2:
                return pa_csv.read_csv(f2)
