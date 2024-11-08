from __future__ import annotations

from typing import TYPE_CHECKING, Generic, overload

from narwhals.typing import IntoDataFrameT, IntoFrameT

from altair.datasets._readers import _Reader, get_backend

if TYPE_CHECKING:
    import sys
    from typing import Any, Literal

    import pandas as pd
    import polars as pl
    import pyarrow as pa

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from altair.datasets._readers import _Backend
    from altair.datasets._typing import DatasetName, Extension, VersionTag

__all__ = ["Loader", "data"]


class Loader(Generic[IntoDataFrameT, IntoFrameT]):
    _reader: _Reader[IntoDataFrameT, IntoFrameT]

    def url(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
    ) -> str:
        """Return the address of a remote dataset."""
        return self._reader.url(name, ext, tag=tag)

    def __call__(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        """Get a remote dataset and load as tabular data."""
        return self._reader.dataset(name, ext, tag=tag, **kwds)

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
        Initialize a new loader, using the specified backend.

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
        """
        obj = Loader.__new__(Loader)
        obj._reader = get_backend(backend)
        return obj


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
