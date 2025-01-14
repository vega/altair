# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.

from __future__ import annotations

import sys
from typing import Any, Literal

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if sys.version_info >= (3, 13):
    from typing import TypeIs
else:
    from typing_extensions import TypeIs

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


__all__ = ["EXTENSION_SUFFIXES", "Dataset", "Extension", "Metadata", "is_ext_read"]

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
Extension: TypeAlias = Literal[".arrow", ".csv", ".json", ".parquet", ".tsv"]
EXTENSION_SUFFIXES: tuple[
    Literal[".arrow"],
    Literal[".csv"],
    Literal[".json"],
    Literal[".parquet"],
    Literal[".tsv"],
] = (".arrow", ".csv", ".json", ".parquet", ".tsv")


def is_ext_read(suffix: Any) -> TypeIs[Extension]:
    return suffix in {".arrow", ".csv", ".json", ".parquet", ".tsv"}


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
        _description_
    is_tabular
        Can be read as tabular data.
    is_geo
        _description_
    is_topo
        _description_
    is_spatial
        _description_
    is_json
        _description_
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


    Examples
    --------
    ``Metadata`` keywords form constraints to filter a table like the below sample:

    ### FIXME: NEEDS UPDATING TO DATAPACKAGE VERSION

    ```
    shape: (2_879, 9)
    ┌───────────┬──────────┬──────────┬──────────┬───┬────────┬─────────┬──────────┐
    │ dataset_n ┆ ext_supp ┆ file_nam ┆ name_col ┆ … ┆ suffix ┆ tag     ┆ url_npm  │
    │ a…        ┆ or…      ┆ e        ┆ li…      ┆   ┆ ---    ┆ ---     ┆ ---      │
    │ ---       ┆ ---      ┆ ---      ┆ ---      ┆   ┆ str    ┆ enum    ┆ str      │
    │ str       ┆ bool     ┆ str      ┆ bool     ┆   ┆        ┆         ┆          │
    ╞═══════════╪══════════╪══════════╪══════════╪═══╪════════╪═════════╪══════════╡
    │ cars      ┆ true     ┆ cars.jso ┆ false    ┆ … ┆ .json  ┆ v1.21.0 ┆ https:// │
    │           ┆          ┆ n        ┆          ┆   ┆        ┆         ┆ cd…      │
    │ flights-2 ┆ true     ┆ flights- ┆ true     ┆ … ┆ .arrow ┆ v1.31.1 ┆ https:// │
    │ 0…        ┆          ┆ 20…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ flights-2 ┆ true     ┆ flights- ┆ false    ┆ … ┆ .json  ┆ v2.9.0  ┆ https:// │
    │ 0…        ┆          ┆ 20…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ unemploym ┆ true     ┆ unemploy ┆ false    ┆ … ┆ .json  ┆ v2.7.0  ┆ https:// │
    │ e…        ┆          ┆ me…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ ffox      ┆ false    ┆ ffox.png ┆ false    ┆ … ┆ .png   ┆ v2.5.2  ┆ https:// │
    │           ┆          ┆          ┆          ┆   ┆        ┆         ┆ cd…      │
    │ …         ┆ …        ┆ …        ┆ …        ┆ … ┆ …      ┆ …       ┆ …        │
    │ flights-a ┆ true     ┆ flights- ┆ false    ┆ … ┆ .csv   ┆ v1.18.0 ┆ https:// │
    │ i…        ┆          ┆ ai…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ income    ┆ true     ┆ income.j ┆ false    ┆ … ┆ .json  ┆ v1.21.0 ┆ https:// │
    │           ┆          ┆ so…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ burtin    ┆ true     ┆ burtin.j ┆ false    ┆ … ┆ .json  ┆ v2.8.0  ┆ https:// │
    │           ┆          ┆ so…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ flights-5 ┆ true     ┆ flights- ┆ false    ┆ … ┆ .json  ┆ v1.8.0  ┆ https:// │
    │ k         ┆          ┆ 5k…      ┆          ┆   ┆        ┆         ┆ cd…      │
    │ wheat     ┆ true     ┆ wheat.js ┆ false    ┆ … ┆ .json  ┆ v1.18.0 ┆ https:// │
    │           ┆          ┆ on       ┆          ┆   ┆        ┆         ┆ cd…      │
    └───────────┴──────────┴──────────┴──────────┴───┴────────┴─────────┴──────────┘
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
