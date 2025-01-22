"""
Load example datasets *remotely* from `vega-datasets`_.

Provides over **70+** datasets, used throughout our `Example Gallery`_.

You can learn more about each dataset at `datapackage.md`_.

Examples
--------
Load a dataset as a ``DataFrame``/``Table``::

    from altair.datasets import load

    load("cars")

.. note::
   Requires installation of either `polars`_, `pandas`_, or `pyarrow`_.

Get the remote address of a dataset and use directly in a :class:`altair.Chart`::

    import altair as alt
    from altair.datasets import url

    source = url("co2-concentration")
    alt.Chart(source).mark_line(tooltip=True).encode(x="Date:T", y="CO2:Q")

.. note::
   Works without any additional dependencies.

For greater control over the backend library use::

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

from altair.datasets._loader import Loader

if TYPE_CHECKING:
    import sys
    from typing import Any

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString

    from altair.datasets._loader import _Load
    from altair.datasets._typing import Dataset, Extension


__all__ = ["Loader", "load", "url"]


load: _Load[Any, Any]
"""
Get a remote dataset and load as tabular data.

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


def url(
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
    if name == "load":
        from altair.datasets._loader import load

        return load
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
