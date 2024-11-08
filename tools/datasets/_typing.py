# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.

from __future__ import annotations

import sys
from typing import Literal

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


__all__ = ["DatasetName", "Extension", "Metadata", "VersionTag"]

DatasetName: TypeAlias = Literal[
    "airports",
    "annual-precip",
    "anscombe",
    "barley",
    "birdstrikes",
    "budget",
    "budgets",
    "burtin",
    "cars",
    "climate",
    "co2-concentration",
    "countries",
    "crimea",
    "disasters",
    "driving",
    "earthquakes",
    "flare",
    "flare-dependencies",
    "flights-10k",
    "flights-200k",
    "flights-20k",
    "flights-2k",
    "flights-3m",
    "flights-5k",
    "flights-airport",
    "football",
    "gapminder",
    "gapminder-health-income",
    "github",
    "global-temp",
    "graticule",
    "income",
    "iowa-electricity",
    "iris",
    "jobs",
    "la-riots",
    "londonBoroughs",
    "londonCentroids",
    "londonTubeLines",
    "lookup_groups",
    "lookup_people",
    "miserables",
    "monarchs",
    "movies",
    "normal-2d",
    "obesity",
    "ohlc",
    "penguins",
    "platformer-terrain",
    "points",
    "political-contributions",
    "population",
    "population_engineers_hurricanes",
    "seattle-temps",
    "seattle-weather",
    "seattle-weather-hourly-normals",
    "sf-temps",
    "sp500",
    "sp500-2000",
    "stocks",
    "udistrict",
    "unemployment",
    "unemployment-across-industries",
    "uniform-2d",
    "us-10m",
    "us-employment",
    "us-state-capitals",
    "volcano",
    "weather",
    "weball26",
    "wheat",
    "windvectors",
    "world-110m",
    "zipcodes",
]
VersionTag: TypeAlias = Literal[
    "v2.9.0",
    "v2.8.1",
    "v2.8.0",
    "v2.7.0",
    "v2.5.4",
    "v2.5.3",
    "v2.5.3-next.0",
    "v2.5.2",
    "v2.5.2-next.0",
    "v2.5.1",
    "v2.5.1-next.0",
    "v2.5.0",
    "v2.5.0-next.0",
    "v2.4.0",
    "v2.3.1",
    "v2.3.0",
    "v2.1.0",
    "v2.0.0",
    "v1.31.1",
    "v1.31.0",
    "v1.30.4",
    "v1.30.3",
    "v1.30.2",
    "v1.30.1",
    "v1.29.0",
    "v1.24.0",
    "v1.22.0",
    "v1.21.1",
    "v1.21.0",
    "v1.20.0",
    "v1.19.0",
    "v1.18.0",
    "v1.17.0",
    "v1.16.0",
    "v1.15.0",
    "v1.14.0",
    "v1.12.0",
    "v1.11.0",
    "v1.10.0",
    "v1.8.0",
    "v1.7.0",
    "v1.5.0",
]
Extension: TypeAlias = Literal[".csv", ".json", ".tsv", ".arrow"]


class Metadata(TypedDict, total=False):
    """
    Full schema for ``metadata.parquet``.

    Parameters
    ----------
    dataset_name
        Equivalent to ``Pathlib.Path.stem``.
    ext_supported
        Dataset can be read as tabular data.
    file_name
        Equivalent to ``Pathlib.Path.name``.
    name_collision
        Dataset is available via multiple ``suffix``(s).

        .. note::
            Requires specifying a preference in calls to ``data(ext=...)``.
    sha
        Unique hash for the dataset.

        .. note::
            If the dataset did *not* change between ``v1.0.0``-``v2.0.0``;

            then all ``tag``(s) in this range would **share** this value.
    size
        File size (*bytes*).
    suffix
        File extension.

        .. note::
            Equivalent to ``Pathlib.Path.suffix``
    tag
        ``vega-datasets`` release version.
    url_npm
        Remote url used to access dataset.
    """

    dataset_name: str
    ext_supported: bool
    file_name: str
    name_collision: bool
    sha: str
    size: int
    suffix: str
    tag: str
    url_npm: str
