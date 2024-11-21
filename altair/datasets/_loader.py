from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Generic, TypeVar, final, get_args, overload

from narwhals.typing import IntoDataFrameT, IntoFrameT

from altair.datasets._readers import _Reader, backend

if TYPE_CHECKING:
    import sys
    from collections.abc import MutableMapping
    from typing import Any, Final, Literal

    import pandas as pd
    import polars as pl
    import pyarrow as pa
    from _typeshed import StrPath

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from altair.datasets._readers import _Backend
    from altair.datasets._typing import Dataset, Extension, Version


__all__ = ["Loader", "load"]

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

_URL: Final[Path] = Path(__file__).parent / "_metadata" / "url.csv.gz"


class Loader(Generic[IntoDataFrameT, IntoFrameT]):
    """
    Load examples **remotely** from `vega-datasets`_, with *optional* caching.

    A new ``Loader`` must be initialized by specifying a backend:

        from altair.datasets import Loader

        data = Loader.from_backend("polars")
        >>> data  # doctest: +SKIP
        Loader[polars]

    .. _vega-datasets:
        https://github.com/vega/vega-datasets
    """

    _reader: _Reader[IntoDataFrameT, IntoFrameT]

    @overload
    @classmethod
    def from_backend(
        cls, backend_name: Literal["polars"], /
    ) -> Loader[pl.DataFrame, pl.LazyFrame]: ...

    @overload
    @classmethod
    def from_backend(
        cls, backend_name: Literal["pandas", "pandas[pyarrow]"], /
    ) -> Loader[pd.DataFrame, pd.DataFrame]: ...

    @overload
    @classmethod
    def from_backend(
        cls, backend_name: Literal["pyarrow"], /
    ) -> Loader[pa.Table, pa.Table]: ...

    @classmethod
    def from_backend(cls, backend_name: _Backend, /) -> Loader[Any, Any]:
        """
        Initialize a new loader, with the specified backend.

        Parameters
        ----------
        backend_name
            DataFrame package/config used to return data.

            * *polars*: Using `polars defaults`_
            * *pandas*: Using `pandas defaults`_.
            * *pandas[pyarrow]*: Using ``dtype_backend="pyarrow"``
            * *pyarrow*: (*Experimental*)

            .. warning::
                Most datasets use a `JSON format not supported`_ by ``pyarrow``

        .. _polars defaults:
            https://docs.pola.rs/api/python/stable/reference/io.html
        .. _pandas defaults:
            https://pandas.pydata.org/docs/reference/io.html
        .. _JSON format not supported:
            https://arrow.apache.org/docs/python/json.html#reading-json-files

        Examples
        --------
        Using ``polars``:

            from altair.datasets import Loader

            data = Loader.from_backend("polars")
            cars = data("cars")

            >>> type(cars)  # doctest: +SKIP
            polars.dataframe.frame.DataFrame

        Using ``pandas``:

            data = Loader.from_backend("pandas")
            cars = data("cars")

            >>> type(cars)  # doctest: +SKIP
            pandas.core.frame.DataFrame

        Using ``pandas``, backed by ``pyarrow`` dtypes:

            data = Loader.from_backend("pandas[pyarrow]")
            cars = data("cars", tag="v1.29.0")

            >>> type(cars)  # doctest: +SKIP
            pandas.core.frame.DataFrame

            >>> cars.dtypes  # doctest: +SKIP
            Name                string[pyarrow]
            Miles_per_Gallon    double[pyarrow]
            Cylinders            int64[pyarrow]
            Displacement        double[pyarrow]
            Horsepower           int64[pyarrow]
            Weight_in_lbs        int64[pyarrow]
            Acceleration        double[pyarrow]
            Year                string[pyarrow]
            Origin              string[pyarrow]
            dtype: object
        """
        obj = Loader.__new__(Loader)
        obj._reader = backend(backend_name)
        return obj

    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: Version | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        """
        Get a remote dataset and load as tabular data.

        Parameters
        ----------
        name
            Name of the dataset/`Path.stem`_.
        suffix
            File extension/`Path.suffix`_.

            .. note::
                Only needed if ``name`` is available in multiple formats.
        tag
            Version identifier for a `vega-datasets release`_.
        **kwds
            Arguments passed to the underlying read function.

        .. _Path.stem:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
        .. _Path.suffix:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix
        .. _vega-datasets release:
            https://github.com/vega/vega-datasets/releases

        Examples
        --------
        Using ``polars``:

            from altair.datasets import Loader

            data = Loader.from_backend("polars")
            source = data("stocks", tag="v2.10.0")

            >>> source.columns  # doctest: +SKIP
            ['symbol', 'date', 'price']

            >>> source  # doctest: +SKIP
            shape: (560, 3)
            ┌────────┬────────────┬────────┐
            │ symbol ┆ date       ┆ price  │
            │ ---    ┆ ---        ┆ ---    │
            │ str    ┆ str        ┆ f64    │
            ╞════════╪════════════╪════════╡
            │ MSFT   ┆ Jan 1 2000 ┆ 39.81  │
            │ MSFT   ┆ Feb 1 2000 ┆ 36.35  │
            │ MSFT   ┆ Mar 1 2000 ┆ 43.22  │
            │ MSFT   ┆ Apr 1 2000 ┆ 28.37  │
            │ MSFT   ┆ May 1 2000 ┆ 25.45  │
            │ …      ┆ …          ┆ …      │
            │ AAPL   ┆ Nov 1 2009 ┆ 199.91 │
            │ AAPL   ┆ Dec 1 2009 ┆ 210.73 │
            │ AAPL   ┆ Jan 1 2010 ┆ 192.06 │
            │ AAPL   ┆ Feb 1 2010 ┆ 204.62 │
            │ AAPL   ┆ Mar 1 2010 ┆ 223.02 │
            └────────┴────────────┴────────┘

        Using ``pandas``:

            data = Loader.from_backend("pandas")
            source = data("stocks", tag="v2.10.0")

            >>> source.columns  # doctest: +SKIP
            Index(['symbol', 'date', 'price'], dtype='object')

            >>> source  # doctest: +SKIP
                symbol        date   price
            0     MSFT  Jan 1 2000   39.81
            1     MSFT  Feb 1 2000   36.35
            2     MSFT  Mar 1 2000   43.22
            3     MSFT  Apr 1 2000   28.37
            4     MSFT  May 1 2000   25.45
            ..     ...         ...     ...
            555   AAPL  Nov 1 2009  199.91
            556   AAPL  Dec 1 2009  210.73
            557   AAPL  Jan 1 2010  192.06
            558   AAPL  Feb 1 2010  204.62
            559   AAPL  Mar 1 2010  223.02

            [560 rows x 3 columns]

        Using ``pyarrow``:

            data = Loader.from_backend("pyarrow")
            source = data("stocks", tag="v2.10.0")

            >>> source.column_names  # doctest: +SKIP
            ['symbol', 'date', 'price']

            >>> source  # doctest: +SKIP
            pyarrow.Table
            symbol: string
            date: string
            price: double
            ----
            symbol: [["MSFT","MSFT","MSFT","MSFT","MSFT",...,"AAPL","AAPL","AAPL","AAPL","AAPL"]]
            date: [["Jan 1 2000","Feb 1 2000","Mar 1 2000","Apr 1 2000","May 1 2000",...,"Nov 1 2009","Dec 1 2009","Jan 1 2010","Feb 1 2010","Mar 1 2010"]]
            price: [[39.81,36.35,43.22,28.37,25.45,...,199.91,210.73,192.06,204.62,223.02]]
        """
        return self._reader.dataset(name, suffix, tag=tag, **kwds)

    def url(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: Version | None = None,
    ) -> str:
        """
        Return the address of a remote dataset.

        Parameters
        ----------
        name
            Name of the dataset/`Path.stem`_.
        suffix
            File extension/`Path.suffix`_.

            .. note::
                Only needed if ``name`` is available in multiple formats.
        tag
            Version identifier for a `vega-datasets release`_.

        .. _Path.stem:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
        .. _Path.suffix:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix
        .. _vega-datasets release:
            https://github.com/vega/vega-datasets/releases

        Examples
        --------
        The returned url will always point to an accessible dataset:

            import altair as alt
            from altair.datasets import Loader

            data = Loader.from_backend("polars")
            >>> data.url("cars", tag="v2.9.0")  # doctest: +SKIP
            'https://cdn.jsdelivr.net/npm/vega-datasets@v2.9.0/data/cars.json'

        We can pass the result directly to a chart:

            url = data.url("cars", tag="v2.9.0")
            alt.Chart(url).mark_point().encode(x="Horsepower:Q", y="Miles_per_Gallon:Q")
        """
        return self._reader.url(name, suffix, tag=tag)

    @property
    def cache_dir(self) -> Path | None:
        """
        Returns path to datasets cache.

        By default, this can be configured using the environment variable:

            "ALTAIR_DATASETS_DIR"

        You *may* also set this directly, but the value will **not** persist between sessions:

            from pathlib import Path

            from altair.datasets import Loader

            data = Loader.from_backend("polars")
            data.cache_dir = Path.home() / ".altair_cache"

            >>> data.cache_dir.relative_to(Path.home()).as_posix()  # doctest: +SKIP
            '.altair_cache'
        """
        return self._reader._cache

    @cache_dir.setter
    def cache_dir(self, source: StrPath, /) -> None:
        import os

        os.environ[self._reader._ENV_VAR] = str(source)

    def __repr__(self) -> str:
        return f"{type(self).__name__}[{self._reader._name}]"


@final
class _Load(Loader[IntoDataFrameT, IntoFrameT]):
    @overload
    def __call__(  # pyright: ignore[reportOverlappingOverload]
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        tag: Version | None = ...,
        backend: None = ...,
        **kwds: Any,
    ) -> IntoDataFrameT: ...
    @overload
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        tag: Version | None = ...,
        backend: Literal["polars"] = ...,
        **kwds: Any,
    ) -> pl.DataFrame: ...
    @overload
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        tag: Version | None = ...,
        backend: Literal["pandas", "pandas[pyarrow]"] = ...,
        **kwds: Any,
    ) -> pd.DataFrame: ...
    @overload
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        tag: Version | None = ...,
        backend: Literal["pyarrow"] = ...,
        **kwds: Any,
    ) -> pa.Table: ...
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: Version | None = None,
        backend: _Backend | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT | pl.DataFrame | pd.DataFrame | pa.Table:
        if backend is None:
            return super().__call__(name, suffix, tag, **kwds)
        else:
            return self.from_backend(backend)(name, suffix, tag=tag, **kwds)


class UrlCache(Generic[_KT, _VT]):
    """
    `csv`_, `gzip`_ -based, lazy url lookup.

    Operates on a subset of available datasets:
    - Only the latest version
    - Excludes `.parquet`, which `cannot be read via url`_
    - Name collisions are pre-resolved
        - Only provide the smallest (e.g. ``weather.json`` instead of ``weather.csv``)

    .. _csv:
        https://docs.python.org/3/library/csv.html
    .. _gzip:
        https://docs.python.org/3/library/gzip.html
    .. _cannot be read via url:
        https://github.com/vega/vega/issues/3961
    """

    def __init__(
        self,
        fp: Path,
        /,
        *,
        columns: tuple[str, str] = ("dataset_name", "url_npm"),
        tp: type[MutableMapping[_KT, _VT]] = dict["_KT", "_VT"],
    ) -> None:
        self.fp: Path = fp
        self.columns: tuple[str, str] = columns
        self._mapping: MutableMapping[_KT, _VT] = tp()

    def read(self) -> Any:
        import csv
        import gzip

        with gzip.open(self.fp, mode="rb") as f:
            b_lines = f.readlines()
        reader = csv.reader((bs.decode() for bs in b_lines), dialect=csv.unix_dialect)
        header = tuple(next(reader))
        if header != self.columns:
            msg = f"Expected header to match {self.columns!r},\n" f"but got: {header!r}"
            raise ValueError(msg)
        return dict(reader)

    def __getitem__(self, key: _KT, /) -> _VT:
        if url := self.get(key, None):
            return url

        from altair.datasets._typing import Dataset

        if key in get_args(Dataset):
            msg = f"{key!r} cannot be loaded via url."
            raise TypeError(msg)
        else:
            msg = f"{key!r} does not refer to a known dataset."
            raise TypeError(msg)

    def get(self, key: _KT, default: _T) -> _VT | _T:
        if not self._mapping:
            self._mapping.update(self.read())
        return self._mapping.get(key, default)


url_cache: UrlCache[Dataset | LiteralString, str] = UrlCache(_URL)
load: _Load[Any, Any]


def __getattr__(name):
    if name == "load":
        from altair.datasets._readers import infer_backend

        reader = infer_backend()
        global load
        load = _Load.__new__(_Load)
        load._reader = reader
        return load
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
