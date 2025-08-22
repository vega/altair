"""
Load example datasets *remotely* from `vega-datasets`_.

Provides **70+** datasets, used throughout our `Example Gallery`_.

You can learn more about each dataset at `datapackage.md`_.

Examples
--------
**Primary Interface - Data Object**::

    from altair.datasets import data

    # Load with default engine (pandas)
    cars_df = data.cars()

    # Load with specific engine
    cars_polars = data.cars(engine="polars")
    cars_pyarrow = data.cars(engine="pyarrow")

    # Get URL
    cars_url = data.cars.url

    # Set default engine for all datasets
    data.set_default_engine("polars")
    movies_df = data.movies()  # Uses polars engine

    # List available datasets
    available_datasets = data.list_datasets()

**Expert Interface - Loader**::

    from altair.datasets import Loader

    load = Loader.from_backend("polars")
    load("penguins")
    load.url("penguins")

This method also provides *precise* <kbd>Tab</kbd> completions on the returned object::

    load("cars").<Tab>
    #            bottom_k
    #            drop
    #            drop_in_place
    #            drop_nans
    #            dtypes
    #            ...

**Expert Interface - Direct Functions**::

    from altair.datasets import load, url

    # Load a dataset
    cars_df = load("cars", backend="polars")

    # Get dataset URL
    cars_url = url("cars")

.. note::
   Requires installation of either `polars`_, `pandas`_, or `pyarrow`_.

.. _vega-datasets:
    https://github.com/vega/vega-datasets
.. _Example Gallery:
    https://altair-viz.github.io/gallery/index.html#example-gallery
.. _datapackage.md:
    https://github.com/vega/vega-datasets/blob/main/datapackage.md
.. _polars:
    https://docs.pola.rs/user-guide/installation/
.. _pandas:
    https://pandas.pydata.org/docs/getting_started/install.html
.. _pyarrow:
    https://arrow.apache.org/docs/python/install.html
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from altair.datasets._loader import Loader as Loader

if TYPE_CHECKING:
    import sys
    from typing import Any

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString

    from altair.datasets._data import DataObject
    from altair.datasets._loader import _Load
    from altair.datasets._typing import Dataset, Extension


load: _Load[Any, Any]
"""
Get a remote dataset and load as tabular data.

This is an expert interface. For most users, the data object interface is recommended::

    from altair.datasets import data
    cars = data.cars(engine="polars")

For full <kbd>Tab</kbd> completions, instead use::

    from altair.datasets import Loader
    load = Loader.from_backend("polars")
    cars = load("cars")
    movies = load("movies")

Alternatively, specify ``backend`` during a call::

    from altair.datasets import load
    cars = load("cars", backend="polars")
    movies = load("movies", backend="polars")
"""

data: DataObject


def url(
    name: Dataset | LiteralString,
    suffix: Extension | None = None,
    /,
) -> str:
    """
    Return the address of a remote dataset.

    This is an expert interface. For most users, the data object interface is recommended::

        from altair.datasets import data

        cars_url = data.cars.url

    Parameters
    ----------
    name
        Name of the dataset/`Path.stem`_.
    suffix
        File extension/`Path.suffix`_.

        .. note::
            Only needed if ``name`` is available in multiple formats.

    Returns
    -------
    ``str``

    .. _Path.stem:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
    .. _Path.suffix:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix
    """
    from altair.datasets._exceptions import AltairDatasetsError

    try:
        from altair.datasets._loader import load

        url = load.url(name, suffix)
    except AltairDatasetsError:
        from altair.datasets._cache import csv_cache

        url = csv_cache.url(name)

    return url


def __getattr__(name):
    if name == "data":
        from altair.datasets._data import data

        return data
    elif name == "load":
        from altair.datasets._loader import load

        return load
    elif name == "__all__":
        # Define __all__ dynamically to avoid ruff errors
        return ["Loader", "data", "load", "url"]
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
