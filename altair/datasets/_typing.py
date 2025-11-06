# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.

from __future__ import annotations

import sys
from typing import Literal

if sys.version_info >= (3, 15):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if sys.version_info >= (3, 11):
    from typing import LiteralString
else:
    from typing_extensions import LiteralString

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


__all__ = ["Dataset", "Extension", "Metadata"]

Dataset: TypeAlias = Literal[
    "airports",
    "annual_precip",
    "anscombe",
    "barley",
    "birdstrikes",
    "budget",
    "budgets",
    "burtin",
    "cars",
    "co2_concentration",
    "countries",
    "crimea",
    "disasters",
    "driving",
    "earthquakes",
    "ffox",
    "flare",
    "flare_dependencies",
    "flights_10k",
    "flights_200k_arrow",
    "flights_200k_json",
    "flights_20k",
    "flights_2k",
    "flights_3m",
    "flights_5k",
    "flights_airport",
    "football",
    "gapminder",
    "gapminder_health_income",
    "gimp",
    "github",
    "global_temp",
    "icon_7zip",
    "income",
    "iowa_electricity",
    "jobs",
    "la_riots",
    "london_boroughs",
    "london_centroids",
    "london_tube_lines",
    "lookup_groups",
    "lookup_people",
    "miserables",
    "monarchs",
    "movies",
    "normal_2d",
    "obesity",
    "ohlc",
    "penguins",
    "platformer_terrain",
    "political_contributions",
    "population",
    "population_engineers_hurricanes",
    "seattle_weather",
    "seattle_weather_hourly_normals",
    "sp500",
    "sp500_2000",
    "species",
    "stocks",
    "udistrict",
    "unemployment",
    "unemployment_across_industries",
    "uniform_2d",
    "us_10m",
    "us_employment",
    "us_state_capitals",
    "volcano",
    "weather",
    "weekly_weather",
    "wheat",
    "windvectors",
    "world_110m",
    "zipcodes",
]
Extension: TypeAlias = Literal[".arrow", ".csv", ".json", ".parquet", ".png", ".tsv"]


class Metadata(TypedDict, total=False):
    """
    Full schema for ``metadata.parquet``.

    Parameters
    ----------
    dataset_name
        Name of the dataset from the resource name field.
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
    │ airports       ┆ .csv   ┆ airports.csv   ┆ … ┆ 608ba6d51fa70 ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 584c3fa1d31e… ┆ sdelivr.net/… │
    │ annual_precip  ┆ .json  ┆ annual-precip. ┆ … ┆ 719e73406cfc0 ┆ https://cdn.j │
    │                ┆        ┆ json           ┆   ┆ 8f16dda65151… ┆ sdelivr.net/… │
    │ anscombe       ┆ .json  ┆ anscombe.json  ┆ … ┆ 11ae97090b626 ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 3bdf0c866115… ┆ sdelivr.net/… │
    │ barley         ┆ .json  ┆ barley.json    ┆ … ┆ 8dc50de2509b6 ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ e197ce95c24c… ┆ sdelivr.net/… │
    │ birdstrikes    ┆ .csv   ┆ birdstrikes.cs ┆ … ┆ 1b8b190c9bc02 ┆ https://cdn.j │
    │                ┆        ┆ v              ┆   ┆ ef7bcbfe5a8a… ┆ sdelivr.net/… │
    │ …              ┆ …      ┆ …              ┆ … ┆ …             ┆ …             │
    │ weekly_weather ┆ .json  ┆ weekly-weather ┆ … ┆ bd42a3e2403e7 ┆ https://cdn.j │
    │                ┆        ┆ .json          ┆   ┆ ccd6baaa89f9… ┆ sdelivr.net/… │
    │ wheat          ┆ .json  ┆ wheat.json     ┆ … ┆ cde46b43fc82f ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 4c3c2a37ddcf… ┆ sdelivr.net/… │
    │ windvectors    ┆ .csv   ┆ windvectors.cs ┆ … ┆ ed686b0ba613a ┆ https://cdn.j │
    │                ┆        ┆ v              ┆   ┆ bd59d09fcd94… ┆ sdelivr.net/… │
    │ world_110m     ┆ .json  ┆ world-110m.jso ┆ … ┆ a1ce852de6f27 ┆ https://cdn.j │
    │                ┆        ┆ n              ┆   ┆ 13c94c0c2840… ┆ sdelivr.net/… │
    │ zipcodes       ┆ .csv   ┆ zipcodes.csv   ┆ … ┆ d3df33e12be0d ┆ https://cdn.j │
    │                ┆        ┆                ┆   ┆ 0544c95f1bd4… ┆ sdelivr.net/… │
    └────────────────┴────────┴────────────────┴───┴───────────────┴───────────────┘
    ```
    """

    dataset_name: Dataset | LiteralString
    suffix: Extension
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
