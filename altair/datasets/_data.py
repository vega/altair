"""
Data object interface for Altair datasets.

This module provides a `data` object that allows accessing datasets as attributes
and calling them with backend options, similar to the vega_datasets interface.
"""

from __future__ import annotations

import inspect
import typing as t
from typing import TYPE_CHECKING

from altair.datasets._loader import Loader

if TYPE_CHECKING:
    import pandas as pd
    import polars as pl
    import pyarrow as pa

    from altair.datasets._reader import _Backend


class DatasetAccessor:
    """
    Accessor for individual datasets that can be called with backend options.

    This object provides access to a specific dataset with support for
    different backends and autocompletion.

    Call this object to load the dataset:
        dataset_accessor(engine="polars", **kwds)

    Parameters for __call__:
        engine : {"polars", "pandas", "pandas[pyarrow]", "pyarrow"}, optional
            The backend to use for loading the dataset.
        **kwds : Any
            Additional arguments passed to the loader.

    Examples
    --------
    >>> from altair.datasets import data
    >>>
    >>> # Load with default backend
    >>> cars_df = data.cars()
    >>>
    >>> # Load with specific backend
    >>> cars_polars = data.cars(engine="polars")
    >>> cars_pandas = data.cars(engine="pandas")
    >>> # Note: pandas[pyarrow] backend requires pyarrow package
    >>>
    >>> # Get URL
    >>> url = data.cars.url
    >>>
    >>> # Use explicit load method
    >>> cars_df = data.cars.load(engine="polars")
    """

    def __init__(self, name: str, default_backend: _Backend = "pandas"):
        self._name = name
        self._default_backend = default_backend
        self._default_loader: Loader[t.Any, t.Any] | None = None

        # Create a proper signature for better IDE support
        self.__signature__ = inspect.signature(self._call_impl)

        # Set docstring for Jupyter autocompletion
        docstring = f"""Load the '{name}' dataset.

Parameters
----------
engine : {{"polars", "pandas", "pandas[pyarrow]", "pyarrow"}}, optional
    The backend to use for loading the dataset.
**kwds : Any
    Additional arguments passed to the loader.

Returns
-------
DataFrame or Table
    The loaded dataset.

Examples
--------
>>> data.{name}()  # Load with default backend
>>> data.{name}(engine="polars")  # Load with specific backend
>>> data.{name}.url  # Get dataset URL
>>> data.{name}.load(engine="polars")  # Explicit load method
"""

        # Set docstring for better Jupyter support
        self.__doc__ = docstring

    def _call_impl(
        self,
        *,
        engine: _Backend | None = None,
        **kwds: t.Any,
    ) -> t.Any:
        """Internal implementation of the call method."""
        if engine is None:
            if self._default_loader is None:
                self._default_loader = Loader.from_backend(self._default_backend)
            return self._default_loader(self._name, **kwds)
        else:
            loader = Loader.from_backend(engine)
            return loader(self._name, **kwds)

    @property
    def url(self) -> str:
        """
        Get the URL for this dataset.

        Returns
        -------
        str
            The URL of the dataset.

        Examples
        --------
        >>> from altair.datasets import data
        >>> cars_url = data.cars.url
        >>> print(cars_url)
        https://cdn.jsdelivr.net/npm/vega-datasets@v3.2.0/data/cars.json
        """
        if self._default_loader is None:
            self._default_loader = Loader.from_backend(self._default_backend)
        return self._default_loader.url(self._name)

    def load(self, *, engine: _Backend | None = None, **kwds: t.Any) -> t.Any:
        """
        Load the dataset with the specified engine.

        This method provides the same functionality as calling the accessor directly,
        but with more explicit parameter autocompletion in some IDEs.

        Parameters
        ----------
        engine : {"polars", "pandas", "pandas[pyarrow]", "pyarrow"}, optional
            The backend to use for loading the dataset.
        **kwds : Any
            Additional arguments passed to the loader.

        Returns
        -------
        DataFrame or Table
            The loaded dataset.

        Examples
        --------
        >>> from altair.datasets import data
        >>> cars_df = data.cars.load(engine="polars")
        >>> movies_df = data.movies.load(engine="pandas")
        """
        return self._call_impl(engine=engine, **kwds)

    def __repr__(self) -> str:
        """String representation of the dataset accessor."""
        return (
            f"DatasetAccessor('{self._name}', default_engine='{self._default_backend}')"
        )

    @t.overload
    def __call__(
        self,
        *,
        engine: t.Literal["polars"],
        **kwds: t.Any,
    ) -> pl.DataFrame: ...

    @t.overload
    def __call__(
        self,
        *,
        engine: t.Literal["pandas", "pandas[pyarrow]"],
        **kwds: t.Any,
    ) -> pd.DataFrame: ...

    @t.overload
    def __call__(
        self,
        *,
        engine: t.Literal["pyarrow"],
        **kwds: t.Any,
    ) -> pa.Table: ...

    @t.overload
    def __call__(
        self,
        *,
        engine: _Backend | None = None,
        **kwds: t.Any,
    ) -> t.Any: ...

    def __call__(
        self,
        *,
        engine: _Backend | None = None,
        **kwds: t.Any,
    ) -> t.Any:
        """
        Load the dataset with the specified engine.

        Parameters
        ----------
        engine : {{"polars", "pandas", "pandas[pyarrow]", "pyarrow"}}, optional
            The backend to use for loading the dataset.
        **kwds
            Additional arguments passed to the loader.

        Returns
        -------
        The loaded dataset as a DataFrame/Table from the specified engine.

        Examples
        --------
        >>> from altair.datasets import data
        >>>
        >>> # Load with default engine
        >>> df = data.cars()
        >>>
        >>> # Load with specific engine
        >>> df = data.cars(engine="polars")
        """
        return self._call_impl(engine=engine, **kwds)


class DataObject:
    """
    Main data object that provides access to all datasets as attributes.

    This is the primary interface for loading Altair datasets. It provides
    a simple, intuitive way to access datasets with autocompletion support.

    Examples
    --------
    >>> from altair.datasets import data
    >>>
    >>> # Access datasets as attributes with autocompletion
    >>> cars_df = data.cars()
    >>> movies_df = data.movies(engine="pandas")
    >>>
    >>> # Get URLs
    >>> cars_url = data.cars.url
    >>> movies_url = data.movies.url
    >>>
    >>> # Set default engine for all datasets
    >>> data.set_default_engine("polars")
    >>> penguins_df = data.penguins()  # Uses polars engine
    >>>
    >>> # List available datasets
    >>> available_datasets = data.list_datasets()
    >>> print(f"Available datasets: {len(available_datasets)}")
    Available datasets: 72
    """

    def __init__(self, default_backend: _Backend = "pandas"):
        self._default_backend = default_backend
        self._accessors: dict[str, DatasetAccessor] = {}
        self._dataset_names: list[str] | None = None

    def _get_dataset_names(self) -> list[str]:
        """Get the list of available dataset names from metadata."""
        if self._dataset_names is None:
            try:
                from altair.datasets._cache import CsvCache

                cache = CsvCache()
                self._dataset_names = list(cache.mapping.keys())
            except Exception:
                # Fallback if metadata is not available
                self._dataset_names = []
        return self._dataset_names

    def __dir__(self) -> list[str]:
        """Return list of available attributes for autocompletion."""
        standard_attrs = list(super().__dir__())
        dataset_names = self._get_dataset_names()
        return standard_attrs + dataset_names

    def __getattr__(self, name: str) -> DatasetAccessor:
        """Get a dataset accessor for the given name."""
        dataset_names = self._get_dataset_names()
        if name not in dataset_names:
            available_datasets = dataset_names[:10]
            if len(dataset_names) > 10:
                available_datasets.append("...")
            error_msg = (
                f"Dataset '{name}' not found. Available datasets: {available_datasets}"
            )
            raise AttributeError(error_msg)

        self._accessors[name] = DatasetAccessor(name, self._default_backend)
        return self._accessors[name]

    def set_default_engine(self, engine: _Backend) -> None:
        """
        Set the default engine for all datasets.

        Parameters
        ----------
        engine : {"polars", "pandas", "pandas[pyarrow]", "pyarrow"}
            The backend to use as default for all datasets.

        Examples
        --------
        >>> from altair.datasets import data
        >>> data.set_default_engine("polars")
        >>> # Now all datasets will use polars by default
        >>> cars_df = data.cars()  # Uses polars
        >>> movies_df = data.movies()  # Uses polars
        """
        self._default_backend = engine
        # Clear cached accessors so they use the new default
        self._accessors.clear()

    def list_datasets(self) -> list[str]:
        """
        Get a list of all available dataset names.

        Returns
        -------
        list[str]
            List of available dataset names.

        Examples
        --------
        >>> from altair.datasets import data
        >>> datasets = data.list_datasets()
        >>> print(f"Available datasets: {len(datasets)}")
        Available datasets: 72
        >>> print(datasets[:5])  # First 5 datasets
        ['airports', 'annual_precip', 'anscombe', 'barley', 'birdstrikes']
        """
        return self._get_dataset_names()

    def get_default_engine(self) -> _Backend:
        """
        Get the current default engine.

        Returns
        -------
        str
            The current default engine.

        Examples
        --------
        >>> from altair.datasets import data
        >>> data.set_default_engine("pandas")
        >>> print(data.get_default_engine())
        pandas
        >>> data.set_default_engine("polars")
        >>> print(data.get_default_engine())
        polars
        """
        return self._default_backend

    def __repr__(self) -> str:
        """String representation of the data object."""
        dataset_count = len(self._get_dataset_names())
        return f"AltairDataObject(default_engine='{self._default_backend}', datasets={dataset_count})"


# Create the main data object
data = DataObject()
