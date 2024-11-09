from __future__ import annotations

from typing import TYPE_CHECKING, Generic, overload

from narwhals.typing import IntoDataFrameT, IntoFrameT

from altair.datasets._readers import _Reader, get_backend

if TYPE_CHECKING:
    import sys
    from pathlib import Path
    from typing import Any, Literal

    import pandas as pd
    import polars as pl
    import pyarrow as pa
    from _typeshed import StrPath

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from altair.datasets._readers import _Backend
    from altair.datasets._typing import DatasetName, Extension, VersionTag

__all__ = ["Loader", "data"]


class Loader(Generic[IntoDataFrameT, IntoFrameT]):
    """
    Load examples **remotely** from `vega-datasets`_, with *optional* caching.

    .. _vega-datasets:
        https://github.com/vega/vega-datasets
    """

    _reader: _Reader[IntoDataFrameT, IntoFrameT]

    def url(
        self,
        name: DatasetName | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: VersionTag | None = None,
    ) -> str:
        """Return the address of a remote dataset."""
        return self._reader.url(name, suffix, tag=tag)

    def __call__(
        self,
        name: DatasetName | LiteralString,
        suffix: Extension | None = None,
        /,
        tag: VersionTag | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        """Get a remote dataset and load as tabular data."""
        return self._reader.dataset(name, suffix, tag=tag, **kwds)

    def __repr__(self) -> str:
        return f"{type(self).__name__}[{type(self._reader).__name__}]"

    @overload
    @classmethod
    def with_backend(
        cls, backend: Literal["polars", "polars[pyarrow]"], /
    ) -> Loader[pl.DataFrame, pl.LazyFrame]: ...

    @overload
    @classmethod
    def with_backend(
        cls, backend: Literal["pandas", "pandas[pyarrow]"], /
    ) -> Loader[pd.DataFrame, pd.DataFrame]: ...

    @overload
    @classmethod
    def with_backend(
        cls, backend: Literal["pyarrow"], /
    ) -> Loader[pa.Table, pa.Table]: ...

    @classmethod
    def with_backend(cls, backend: _Backend, /) -> Loader[Any, Any]:
        """
        Initialize a new loader, with the specified backend.

        Parameters
        ----------
        backend
            DataFrame package/config used to return data.

            * *polars*: Using `polars defaults`_
            * *polars[pyarrow]*: Using ``use_pyarrow=True``
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

            data = Loader.with_backend("polars")
            cars = data("cars")

            type(cars)
            polars.dataframe.frame.DataFrame

        Using ``pandas``:

            data = Loader.with_backend("pandas")
            cars = data("cars")

            type(cars)
            pandas.core.frame.DataFrame

        Using ``pandas``, backed by ``pyarrow`` dtypes:

            data = Loader.with_backend("pandas[pyarrow]")
            cars = data("cars", tag="v1.29.0")

            type(cars)
            pandas.core.frame.DataFrame

            cars.dtypes
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
        obj._reader = get_backend(backend)
        return obj

    @property
    def cache_dir(self) -> Path | None:
        """
        Returns path to datasets cache.

        By default, this can be configured using the environment variable:

            "ALTAIR_DATASETS_DIR"

        You *may* also set this directly, but the value will **not** persist between sessions:

            from pathlib import Path

            from altair.datasets import Loader

            data = Loader.with_backend("polars")
            data.cache_dir = Path.home() / ".altair_cache"

            data.cache_dir.relative_to(Path.home()).as_posix()
            '.altair_cache'
        """
        return self._reader._cache

    @cache_dir.setter
    def cache_dir(self, source: StrPath, /) -> None:
        import os

        os.environ[self._reader._ENV_VAR] = str(source)


def __getattr__(name):
    if name == "data":
        global data
        data = Loader.with_backend("pandas")
        from altair.utils.deprecation import deprecated_warn

        deprecated_warn(
            "Added only for backwards compatibility with `altair-viz/vega_datasets`.",
            version="5.5.0",
            alternative="altair.datasets.Loader.with_backend(...)",
            stacklevel=3,
        )
        return data
    else:
        raise AttributeError(name)
