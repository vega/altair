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


__all__ = [
    "EXTENSION_SUFFIXES",
    "Dataset",
    "Extension",
    "Metadata",
    "Version",
    "is_ext_read",
]

Dataset: TypeAlias = Literal[
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
Version: TypeAlias = Literal[
    "v2.11.0",
    "v2.10.0",
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
Extension: TypeAlias = Literal[".csv", ".json", ".tsv", ".arrow", ".parquet"]
EXTENSION_SUFFIXES = (".csv", ".json", ".tsv", ".arrow", ".parquet")


def is_ext_read(suffix: Any) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow", ".parquet"}


class Metadata(TypedDict, total=False):
    """
    Full schema for ``metadata.parquet``.

    Parameters
    ----------
    dataset_name
        Name of the dataset/`Path.stem`_.
    ext_supported
        Dataset can be read as tabular data.
    file_name
        Equivalent to `Path.name`_.
    name_collision
        Dataset is available via multiple formats.

        .. note::
            Requires specifying a preference in calls to ``data(name, suffix=...)``
    sha
        Unique hash for the dataset.

        .. note::
            If the dataset did *not* change between ``v1.0.0``-``v2.0.0``;

            then all ``tag``(s) in this range would **share** this value.
    size
        File size (*bytes*).
    suffix
        File extension/`Path.suffix`_.
    tag
        Version identifier for a `vega-datasets release`_.
    url_npm
        Remote url used to access dataset.

    .. _Path.stem:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
    .. _Path.name:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name
    .. _Path.suffix:
        https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix
    .. _vega-datasets release:
        https://github.com/vega/vega-datasets/releases

    Examples
    --------
    ``Metadata`` keywords form constraints to filter a table like the below sample:

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
    ext_supported: bool
    file_name: str
    name_collision: bool
    sha: str
    size: int
    suffix: str
    tag: str
    url_npm: str
