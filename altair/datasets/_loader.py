from __future__ import annotations

from typing import TYPE_CHECKING, Generic, final, overload

from narwhals.stable.v1.typing import IntoDataFrameT, IntoFrameT

from altair.datasets._readers import _Reader, backend

if TYPE_CHECKING:
    import sys
    from typing import Any, Literal

    import pandas as pd
    import polars as pl
    import pyarrow as pa

    from altair.datasets._cache import DatasetCache

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from altair.datasets._readers import _Backend
    from altair.datasets._typing import Dataset, Extension


__all__ = ["Loader", "load"]


class Loader(Generic[IntoDataFrameT, IntoFrameT]):
    """
    Load examples **remotely** from `vega-datasets`_, with caching.

    A new ``Loader`` must be initialized by specifying a backend:

        from altair.datasets import Loader

        load = Loader.from_backend("polars")
        >>> load  # doctest: +SKIP
        Loader[polars]

    .. _vega-datasets:
        https://github.com/vega/vega-datasets
    """

    _reader: _Reader[IntoDataFrameT, IntoFrameT]

    @overload
    @classmethod
    def from_backend(
        cls, backend_name: Literal["polars"] = ..., /
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
    def from_backend(cls, backend_name: _Backend = "polars", /) -> Loader[Any, Any]:
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

            load = Loader.from_backend("polars")
            cars = load("cars")

            >>> type(cars)  # doctest: +SKIP
            polars.dataframe.frame.DataFrame

        Using ``pandas``:

            load = Loader.from_backend("pandas")
            cars = load("cars")

            >>> type(cars)  # doctest: +SKIP
            pandas.core.frame.DataFrame

        Using ``pandas``, backed by ``pyarrow`` dtypes:

            load = Loader.from_backend("pandas[pyarrow]")
            cars = load("cars")

            >>> type(cars)  # doctest: +SKIP
            pandas.core.frame.DataFrame

            >>> cars.dtypes  # doctest: +SKIP
            Name                       string[pyarrow]
            Miles_per_Gallon           double[pyarrow]
            Cylinders                   int64[pyarrow]
            Displacement               double[pyarrow]
            Horsepower                  int64[pyarrow]
            Weight_in_lbs               int64[pyarrow]
            Acceleration               double[pyarrow]
            Year                timestamp[ns][pyarrow]
            Origin                     string[pyarrow]
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
        **kwds
            Arguments passed to the underlying read function.

        .. _Path.stem:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
        .. _Path.suffix:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix

        Examples
        --------
        Using ``polars``:

            from altair.datasets import Loader

            load = Loader.from_backend("polars")
            source = load("iowa-electricity")

            >>> source.columns  # doctest: +SKIP
            ['year', 'source', 'net_generation']

            >>> source  # doctest: +SKIP
            shape: (51, 3)
            ┌────────────┬──────────────┬────────────────┐
            │ year       ┆ source       ┆ net_generation │
            │ ---        ┆ ---          ┆ ---            │
            │ date       ┆ str          ┆ i64            │
            ╞════════════╪══════════════╪════════════════╡
            │ 2001-01-01 ┆ Fossil Fuels ┆ 35361          │
            │ 2002-01-01 ┆ Fossil Fuels ┆ 35991          │
            │ 2003-01-01 ┆ Fossil Fuels ┆ 36234          │
            │ 2004-01-01 ┆ Fossil Fuels ┆ 36205          │
            │ 2005-01-01 ┆ Fossil Fuels ┆ 36883          │
            │ …          ┆ …            ┆ …              │
            │ 2013-01-01 ┆ Renewables   ┆ 16476          │
            │ 2014-01-01 ┆ Renewables   ┆ 17452          │
            │ 2015-01-01 ┆ Renewables   ┆ 19091          │
            │ 2016-01-01 ┆ Renewables   ┆ 21241          │
            │ 2017-01-01 ┆ Renewables   ┆ 21933          │
            └────────────┴──────────────┴────────────────┘

        Using ``pandas``:

            load = Loader.from_backend("pandas")
            source = load("iowa-electricity")

            >>> source.columns  # doctest: +SKIP
            Index(['year', 'source', 'net_generation'], dtype='object')

            >>> source  # doctest: +SKIP
                     year        source  net_generation
            0  2001-01-01  Fossil Fuels           35361
            1  2002-01-01  Fossil Fuels           35991
            2  2003-01-01  Fossil Fuels           36234
            3  2004-01-01  Fossil Fuels           36205
            4  2005-01-01  Fossil Fuels           36883
            ..        ...           ...             ...
            46 2013-01-01    Renewables           16476
            47 2014-01-01    Renewables           17452
            48 2015-01-01    Renewables           19091
            49 2016-01-01    Renewables           21241
            50 2017-01-01    Renewables           21933

            [51 rows x 3 columns]

        Using ``pyarrow``:

            load = Loader.from_backend("pyarrow")
            source = load("iowa-electricity")

            >>> source.column_names  # doctest: +SKIP
            ['year', 'source', 'net_generation']

            >>> source  # doctest: +SKIP
            pyarrow.Table
            year: date32[day]
            source: string
            net_generation: int64
            ----
            year: [[2001-01-01,2002-01-01,2003-01-01,2004-01-01,2005-01-01,...,2013-01-01,2014-01-01,2015-01-01,2016-01-01,2017-01-01]]
            source: [["Fossil Fuels","Fossil Fuels","Fossil Fuels","Fossil Fuels","Fossil Fuels",...,"Renewables","Renewables","Renewables","Renewables","Renewables"]]
            net_generation: [[35361,35991,36234,36205,36883,...,16476,17452,19091,21241,21933]]
        """
        return self._reader.dataset(name, suffix, **kwds)

    def url(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
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

        .. _Path.stem:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
        .. _Path.suffix:
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix

        Examples
        --------
        The returned url will always point to an accessible dataset:

            import altair as alt
            from altair.datasets import Loader

            load = Loader.from_backend("polars")
            >>> load.url("cars")  # doctest: +SKIP
            'https://cdn.jsdelivr.net/npm/vega-datasets@v2.11.0/data/cars.json'

        We can pass the result directly to a chart:

            url = load.url("cars")
            alt.Chart(url).mark_point().encode(x="Horsepower:Q", y="Miles_per_Gallon:Q")
        """
        return self._reader.url(name, suffix)

    @property
    def cache(self) -> DatasetCache[IntoDataFrameT, IntoFrameT]:
        """
        Caching of remote dataset requests.

        Configure cache path:

            self.cache.path = "..."

        Download the latest datasets *ahead-of-time*:

            self.cache.download_all()

        Remove all downloaded datasets:

            self.cache.clear()

        Disable caching:

            self.cache.path = None
        """
        return self._reader.cache

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
        backend: None = ...,
        **kwds: Any,
    ) -> IntoDataFrameT: ...
    @overload
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        backend: Literal["polars"] = ...,
        **kwds: Any,
    ) -> pl.DataFrame: ...
    @overload
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        backend: Literal["pandas", "pandas[pyarrow]"] = ...,
        **kwds: Any,
    ) -> pd.DataFrame: ...
    @overload
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = ...,
        /,
        backend: Literal["pyarrow"] = ...,
        **kwds: Any,
    ) -> pa.Table: ...
    def __call__(
        self,
        name: Dataset | LiteralString,
        suffix: Extension | None = None,
        /,
        backend: _Backend | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT | pl.DataFrame | pd.DataFrame | pa.Table:
        if backend is None:
            return super().__call__(name, suffix, **kwds)
        else:
            return self.from_backend(backend)(name, suffix, **kwds)


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
