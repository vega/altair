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
    from altair.datasets._typing import Dataset, Extension, Version


__all__ = ["Loader", "load", "url"]


load: _Load[Any, Any]
"""
For full IDE completions, instead use:

    from altair.datasets import Loader
    load = Loader.from_backend("polars")
    cars = load("cars")
    movies = load("movies")

Alternatively, specify ``backend`` during a call:

    from altair.datasets import load
    cars = load("cars", backend="polars")
    movies = load("movies", backend="polars")

Related
-------
- https://github.com/vega/altair/pull/3631#issuecomment-2480832609
- https://github.com/vega/altair/pull/3631#discussion_r1847111064
- https://github.com/vega/altair/pull/3631#discussion_r1847176465
"""


def url(
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

    Related
    -------
    - https://github.com/vega/altair/pull/3631#issuecomment-2484826592
    - https://github.com/vega/altair/pull/3631#issuecomment-2480832711
    - https://github.com/vega/altair/discussions/3150#discussioncomment-11280516
    - https://github.com/vega/altair/pull/3631#discussion_r1846662053
    """
    from altair.datasets._loader import load

    return load.url(name, suffix, tag=tag)


def __getattr__(name):
    if name == "load":
        from altair.datasets._loader import load

        return load
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
