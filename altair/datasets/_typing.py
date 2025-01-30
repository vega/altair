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


__all__ = ["Dataset", "Extension", "Metadata"]

Dataset: TypeAlias = Literal[
    "7zip",
    "airports",
    "annual-precip",
    "anscombe",
    "barley",
    "birdstrikes",
    "budget",
    "budgets",
    "burtin",
    "cars",
    "co2-concentration",
    "countries",
    "crimea",
    "disasters",
    "driving",
    "earthquakes",
    "ffox",
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
    "gimp",
    "github",
    "global-temp",
    "income",
    "iowa-electricity",
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
    "seattle-weather",
    "seattle-weather-hourly-normals",
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
    "weekly-weather",
    "wheat",
    "windvectors",
    "world-110m",
    "zipcodes",
]
Extension: TypeAlias = Literal[".arrow", ".csv", ".json", ".parquet", ".png", ".tsv"]


class Metadata(TypedDict, total=False):
    """
    Full schema for ``metadata.parquet``.

    Parameters
    ----------
    dataset_name
        Name of the dataset/`Path.stem`_.
    suffix
        File extension/`Path.suffix`_.
    file_name
        Equivalent to `Path.name`_.
    bytes
        File size in *bytes*.
    is_image
        Only accessible via url.
    is_tabular
        Can be read as tabular data.
    is_geo
        `GeoJSON`_ format.
    is_topo
        `TopoJSON`_ format.
    is_spatial
        Any geospatial format. Only natively supported by ``polars``.
    is_json
        Not supported natively by ``pyarrow``.
    has_schema
        Data types available for improved ``pandas`` parsing.
    sha
        Unique hash for the dataset.

        .. note::
            E.g. if the dataset did *not* change between ``v1.0.0``-``v2.0.0``;

            then this value would remain stable.
    url
        Remote url used to access dataset.

    .. _Path.stem:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
    .. _Path.name:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name
    .. _Path.suffix:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix
    .. _GeoJSON:
        https://en.wikipedia.org/wiki/GeoJSON
    .. _TopoJSON:
        https://en.wikipedia.org/wiki/GeoJSON#TopoJSON


    Examples
    --------
    ``Metadata`` keywords form constraints to filter a table like the below sample:

    ```
    shape: (73, 13)
    ┌────────────────┬────────┬────────────────┬───┬───────────────┬───────────────┐
    │ dataset_name   ┆ suffix ┆ file_name      ┆ … ┆ sha           ┆ url           │
    │ ---            ┆ ---    ┆ ---            ┆   ┆ ---           ┆ ---           │
    │ str            ┆ str    ┆ str            ┆   ┆ str           ┆ str           │
    ╞════════════════╪════════╪════════════════╪═══╪═══════════════╪═══════════════╡
    │ 7zip           ┆ .png   ┆ 7zip.png       ┆ … ┆ 6586d6c00887c ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ d48850099c17… ┆ sdelivr.net/… │
    │ airports       ┆ .csv   ┆ airports.csv   ┆ … ┆ 608ba6d51fa70 ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 584c3fa1d31e… ┆ sdelivr.net/… │
    │ annual-precip  ┆ .json  ┆ annual-precip. ┆ … ┆ 719e73406cfc0 ┆ https://cdn.j │
    │                ┆        ┆ json           ┆   ┆ 8f16dda65151… ┆ sdelivr.net/… │
    │ anscombe       ┆ .json  ┆ anscombe.json  ┆ … ┆ 11ae97090b626 ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 3bdf0c866115… ┆ sdelivr.net/… │
    │ barley         ┆ .json  ┆ barley.json    ┆ … ┆ 8dc50de2509b6 ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ e197ce95c24c… ┆ sdelivr.net/… │
    │ …              ┆ …      ┆ …              ┆ … ┆ …             ┆ …             │
    │ weekly-weather ┆ .json  ┆ weekly-weather ┆ … ┆ bd42a3e2403e7 ┆ https://cdn.j │
    │                ┆        ┆ .json          ┆   ┆ ccd6baaa89f9… ┆ sdelivr.net/… │
    │ wheat          ┆ .json  ┆ wheat.json     ┆ … ┆ cde46b43fc82f ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 4c3c2a37ddcf… ┆ sdelivr.net/… │
    │ windvectors    ┆ .csv   ┆ windvectors.cs ┆ … ┆ ed686b0ba613a ┆ https://cdn.j │
    │                ┆        ┆ v              ┆   ┆ bd59d09fcd94… ┆ sdelivr.net/… │
    │ world-110m     ┆ .json  ┆ world-110m.jso ┆ … ┆ a1ce852de6f27 ┆ https://cdn.j │
    │                ┆        ┆ n              ┆   ┆ 13c94c0c2840… ┆ sdelivr.net/… │
    │ zipcodes       ┆ .csv   ┆ zipcodes.csv   ┆ … ┆ d3df33e12be0d ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 0544c95f1bd4… ┆ sdelivr.net/… │
    └────────────────┴────────┴────────────────┴───┴───────────────┴───────────────┘
    ```
    """

    dataset_name: str
    suffix: str
    file_name: str
    bytes: int
    is_image: bool
    is_tabular: bool
    is_geo: bool
    is_topo: bool
    is_spatial: bool
    is_json: bool
    has_schema: bool
    sha: str
    url: str


FlFieldStr: TypeAlias = Literal[
    "integer",
    "number",
    "boolean",
    "string",
    "object",
    "array",
    "date",
    "datetime",
    "time",
    "duration",
]
"""
String representation of `frictionless`_ `Field Types`_.

.. _frictionless:
    https://github.com/frictionlessdata/frictionless-py
.. _Field Types:
    https://datapackage.org/standard/table-schema/#field-types
"""
