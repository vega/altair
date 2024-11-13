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
from collections.abc import Mapping, Sequence
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
from narwhals.typing import IntoDataFrameT, IntoExpr, IntoFrameT

if TYPE_CHECKING:
    import json  # noqa: F401
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

    from altair.datasets._typing import Dataset, Extension, Metadata, Version
    from altair.vegalite.v5.schema._typing import OneOrSeq

    _ExtensionScan: TypeAlias = Literal[".parquet"]
    _T = TypeVar("_T")

    _Polars: TypeAlias = Literal["polars"]
    _Pandas: TypeAlias = Literal["pandas"]
    _PyArrow: TypeAlias = Literal["pyarrow"]
    _ConcreteT = TypeVar("_ConcreteT", _Polars, _Pandas, _PyArrow)
    _PolarsAny: TypeAlias = Literal[_Polars, "polars[pyarrow]"]
    _PandasAny: TypeAlias = Literal[_Pandas, "pandas[pyarrow]"]
    _Backend: TypeAlias = Literal[_PolarsAny, _PandasAny, _PyArrow]


__all__ = ["backend"]

_METADATA: Final[Path] = Path(__file__).parent / "_metadata" / "metadata.parquet"


class _Reader(Protocol[IntoDataFrameT, IntoFrameT]):
    """
    Describes basic IO for remote & local tabular resources.

    Subclassing this protocol directly will provide a *mostly* complete implementation.

    Each of the following must be explicitly assigned:

        _Reader._read_fn
        _Reader._scan_fn
        _Reader._name
    """

    _read_fn: dict[Extension, Callable[..., IntoDataFrameT]]
    """
    Eager file read functions.

    Each corresponds to a known file extension within ``vega-datasets``.
    """

    _scan_fn: dict[_ExtensionScan, Callable[..., IntoFrameT]]
    """
    *Optionally*-lazy file read/scan functions.

    Used exclusively for ``metadata.parquet``.

    Currently ``polars`` backends are the only lazy options.
    """

    _name: LiteralString
    """
    Used in error messages, repr and matching ``@overload``(s).

    Otherwise, has no concrete meaning.
    """

    _ENV_VAR: ClassVar[LiteralString] = "ALTAIR_DATASETS_DIR"
    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()

    def read_fn(self, source: StrPath, /) -> Callable[..., IntoDataFrameT]:
        suffix = validate_suffix(source, is_ext_read)
        return self._read_fn[suffix]

    def scan_fn(self, source: StrPath, /) -> Callable[..., IntoFrameT]:
        suffix = validate_suffix(source, is_ext_scan)
        return self._scan_fn[suffix]

    def dataset(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: Version | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        df = self.query(**validate_constraints(name, suffix, tag))
        it = islice(df.iter_rows(named=True), 1)
        result = cast("Metadata", next(it))
        url = result["url_npm"]
        fn = self.read_fn(url)

        if cache := self._cache:
            fp = cache / (result["sha"] + result["suffix"])
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
        frame = self.query(**validate_constraints(name, suffix, tag))
        url = nw.to_py_scalar(frame.item(0, "url_npm"))
        if isinstance(url, str):
            return url
        else:
            msg = f"Expected 'str' but got {type(url).__name__!r}\n" f"from {url!r}."
            raise TypeError(msg)

    def query(
        self, *predicates: OneOrSeq[IntoExpr], **constraints: Unpack[Metadata]
    ) -> nw.DataFrame[IntoDataFrameT]:
        """
        Query multi-version trees metadata.

        Notes
        -----
        Arguments correspond to those seen in `pl.LazyFrame.filter`_.

        .. _pl.LazyFrame.filter:
            https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.filter.html
        """
        frame = (
            nw.from_native(self.scan_fn(_METADATA)(_METADATA))
            .filter(_parse_predicates_constraints(predicates, constraints))
            .lazy()
            .collect()
        )
        if not frame.is_empty():
            return frame
        else:
            terms = "\n".join(f"{t!r}" for t in (predicates, constraints) if t)
            msg = f"Found no results for:\n    {terms}"
            raise ValueError(msg)

    def _read_metadata(self) -> IntoDataFrameT:
        """
        Return the full contents of ``metadata.parquet``.

        Effectively an eager read, no filters.
        """
        return (
            nw.from_native(self.scan_fn(_METADATA)(_METADATA))
            .lazy()
            .collect()
            .to_native()
        )

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


class _PandasReader(_Reader["pd.DataFrame", "pd.DataFrame"]):
    def __init__(self, name: _Pandas, /) -> None:
        self._name = _requirements(name)
        if not TYPE_CHECKING:
            pd = self._import(self._name)
        self._read_fn = {
            ".csv": pd.read_csv,
            ".json": pd.read_json,
            ".tsv": partial["pd.DataFrame"](pd.read_csv, sep="\t"),
            ".arrow": pd.read_feather,
        }
        self._scan_fn = {".parquet": pd.read_parquet}


class _PandasPyArrowReader(_Reader["pd.DataFrame", "pd.DataFrame"]):
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
        }
        self._scan_fn = {".parquet": partial(pd.read_parquet, dtype_backend=_pa)}


class _PolarsReader(_Reader["pl.DataFrame", "pl.LazyFrame"]):
    def __init__(self, name: _Polars, /) -> None:
        self._name = _requirements(name)
        if not TYPE_CHECKING:
            pl = self._import(self._name)
        self._read_fn = {
            ".csv": pl.read_csv,
            ".json": pl.read_json,
            ".tsv": partial(pl.read_csv, separator="\t"),
            ".arrow": pl.read_ipc,
        }
        self._scan_fn = {".parquet": pl.scan_parquet}


class _PolarsPyArrowReader(_Reader["pl.DataFrame", "pl.LazyFrame"]):
    def __init__(self, name: Literal["polars[pyarrow]"], /) -> None:
        _pl, _pa = _requirements(name)
        self._name = name
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
                import polars as pl

                def pa_read_json(source: StrPath, /, **kwds) -> pa.Table:
                    return pl.read_json(source).to_arrow()

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
        }
        self._scan_fn = {".parquet": pa_read_parquet}


def _parse_predicates_constraints(
    predicates: tuple[Any, ...], constraints: Metadata, /
) -> nw.Expr:
    """
    ``narwhals`` only accepts ``filter(*predicates)``.

    So we convert each item in ``**constraints`` here as::

       col("column_name") == literal_value
    """
    return nw.all_horizontal(
        chain(predicates, (nw.col(name) == v for name, v in constraints.items()))
    )


def validate_constraints(
    name: Dataset | LiteralString, suffix: Extension | None, tag: Version | None, /
) -> Metadata:
    constraints: Metadata = {}
    suffixes = ".csv", ".json", ".tsv", ".arrow"
    if tag is not None:
        constraints["tag"] = tag
    if name.endswith(suffixes):
        fp = Path(name)
        constraints["dataset_name"] = fp.stem
        constraints["suffix"] = fp.suffix
        return constraints
    elif suffix is not None:
        if not is_ext_read(suffix):
            msg = f"Expected 'suffix' to be one of {suffixes!r},\nbut got: {suffix!r}"
            raise TypeError(msg)
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


def is_ext_read(suffix: Any) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}


@overload
def backend(name: _PolarsAny, /) -> _Reader[pl.DataFrame, pl.LazyFrame]: ...


@overload
def backend(name: _PandasAny, /) -> _Reader[pd.DataFrame, pd.DataFrame]: ...


@overload
def backend(name: _PyArrow, /) -> _Reader[pa.Table, pa.Table]: ...


def backend(name: _Backend, /) -> _Reader[Any, Any]:
    """Reader initialization dispatcher."""
    if name == "polars":
        return _PolarsReader(name)
    elif name == "polars[pyarrow]":
        return _PolarsPyArrowReader(name)
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


@overload
def _requirements(s: Literal["polars[pyarrow]"], /) -> tuple[_Polars, _PyArrow]: ...


def _requirements(s: _Backend, /):
    concrete: set[Literal[_Polars, _Pandas, _PyArrow]] = {"polars", "pandas", "pyarrow"}
    if s in concrete:
        return s
    else:
        from packaging.requirements import Requirement

        req = Requirement(s)
        supports_extras: set[Literal[_Polars, _Pandas]] = {"polars", "pandas"}
        if req.name in supports_extras:
            name = req.name
            if (extras := req.extras) and extras == {"pyarrow"}:
                extra = "pyarrow"
                return name, extra
            else:
                raise NotImplementedError(s)
        else:
            raise NotImplementedError(s)
