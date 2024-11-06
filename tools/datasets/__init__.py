"""
Adapted from `altair-viz/vega_datasets`_.

.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import json
import tempfile
from functools import cached_property, partial
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal
from urllib.request import urlopen

import polars as pl

from tools.codemod import ruff
from tools.datasets.github import GitHub
from tools.datasets.models import QueryTree
from tools.datasets.npm import Npm
from tools.schemapi import utils

if TYPE_CHECKING:
    import sys
    from collections.abc import Mapping

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from tools.datasets._typing import DatasetName, Extension, VersionTag

    _PathAlias: TypeAlias = Literal["npm_tags", "gh_tags", "gh_trees"]

    WorkInProgress: TypeAlias = Any

__all__ = ["app", "data"]

HEADER_COMMENT = """\
# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.
"""


class Application:
    """
    Top-level context.

    When ``write_schema``, addtional ``...-schema.json`` files are produced
    that describes the metadata columns.
    """

    def __init__(
        self,
        output_dir: Path,
        *,
        write_schema: bool,
        trees_gh: str = "metadata",
        tags_gh: str = "tags",
        tags_npm: str = "tags_npm",
        kwds_gh: Mapping[str, Any] | None = None,
        kwds_npm: Mapping[str, Any] | None = None,
    ) -> None:
        output_dir.mkdir(exist_ok=True)
        kwds_gh = kwds_gh or {}
        kwds_npm = kwds_npm or {}
        self._write_schema: bool = write_schema
        self._github: GitHub = GitHub(
            output_dir, name_tags=tags_gh, name_trees=trees_gh, **kwds_gh
        )
        self._npm: Npm = Npm(output_dir, name_tags=tags_npm, **kwds_npm)

    @property
    def github(self) -> GitHub:
        return self._github

    @property
    def npm(self) -> Npm:
        return self._npm

    @property
    def _aliases(self) -> dict[_PathAlias, Path]:
        return {
            "npm_tags": self.npm._paths["tags"],
            "gh_tags": self.github._paths["tags"],
            "gh_trees": self.github._paths["trees"],
        }

    def refresh(self) -> pl.DataFrame:
        npm_tags = self.npm.tags()
        self.write_parquet(npm_tags, self.npm._paths["tags"])

        gh_tags = self.github.refresh_tags(npm_tags)
        self.write_parquet(gh_tags, self.github._paths["tags"])

        gh_trees = self.github.refresh_trees(gh_tags)
        self.write_parquet(gh_trees, self.github._paths["trees"])
        return gh_trees

    def read(self, name: _PathAlias, /) -> pl.DataFrame:
        """Read existing metadata from file."""
        return pl.read_parquet(self._from_alias(name))

    def scan(self, name: _PathAlias, /) -> pl.LazyFrame:
        """Scan existing metadata from file."""
        return pl.scan_parquet(self._from_alias(name))

    def _from_alias(self, name: _PathAlias, /) -> Path:
        if name not in {"npm_tags", "gh_tags", "gh_trees"}:
            msg = f'Expected one of {["npm_tags", "gh_tags", "gh_trees"]!r}, but got: {name!r}'
            raise TypeError(msg)
        else:
            return self._aliases[name]

    def write_parquet(self, frame: pl.DataFrame | pl.LazyFrame, fp: Path, /) -> None:
        """Write ``frame`` to ``fp``, with some extra safety."""
        if not fp.exists():
            fp.touch()
        df = frame.lazy().collect()
        df.write_parquet(fp, compression="zstd", compression_level=17)
        if self._write_schema:
            schema = {name: tp.__name__ for name, tp in df.schema.to_python().items()}
            fp_schema = fp.with_name(f"{fp.stem}-schema.json")
            if not fp_schema.exists():
                fp_schema.touch()
            with fp_schema.open("w") as f:
                json.dump(schema, f, indent=2)


app = Application(Path(__file__).parent / "_metadata", write_schema=True)


# This is the tag in http://github.com/vega/vega-datasets from
# which the datasets in this repository are sourced.
_OLD_SOURCE_TAG = "v1.29.0"  # 5 years ago
_CURRENT_SOURCE_TAG = "v2.9.0"


def generate_datasets_typing(application: Application, output: Path, /) -> None:
    app = application
    tags = app.scan("gh_tags").select("tag").collect().to_series()
    names = (
        app.scan("gh_trees")
        .filter("ext_supported")
        .unique("name_js")
        .select("name_js")
        .sort("name_js")
        .collect()
        .to_series()
    )
    NAME = "DatasetName"
    TAG = "VersionTag"
    EXT = "Extension"
    contents = (
        f"{HEADER_COMMENT}",
        "from __future__ import annotations\n",
        "import sys",
        "from typing import Literal, TYPE_CHECKING",
        utils.import_typing_extensions((3, 10), "TypeAlias"),
        "\n",
        f"__all__ = {[NAME, TAG, EXT]}\n\n"
        f"{NAME}: TypeAlias = {utils.spell_literal(names)}",
        f"{TAG}: TypeAlias = {utils.spell_literal(tags)}",
        f'{EXT}: TypeAlias = {utils.spell_literal([".csv", ".json", ".tsv", ".arrow"])}',
    )
    ruff.write_lint_format(output, contents)


def is_ext_supported(suffix: str) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}


def _py_to_js(s: str, /):
    return s.replace("_", "-")


def _js_to_py(s: str, /):
    return s.replace("-", "_")


class Dataset:
    read_fn: ClassVar[dict[Extension, Callable[..., pl.DataFrame]]] = {
        ".csv": pl.read_csv,
        ".json": pl.read_json,
        ".tsv": partial(pl.read_csv, separator="\t"),
        ".arrow": partial(pl.read_ipc, use_pyarrow=True),
    }

    def __init__(self, name: str, /, base_url: str) -> None:
        self.name: str = name
        file_name = DATASETS_JSON[_py_to_js(name)]["filename"]
        suffix = Path(file_name).suffix
        if is_ext_supported(suffix):
            self.extension: Extension = suffix
        else:
            raise NotImplementedError(suffix, file_name)

        self.url: str = f"{base_url}{file_name}"

    def __call__(self, **kwds: Any) -> pl.DataFrame:
        fn = self.read_fn[self.extension]
        with tempfile.NamedTemporaryFile() as tmp, urlopen(self.url) as f:
            tmp.write(f.read())
            content = fn(tmp, **kwds)
        return content

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(\n  "
            f"name={self.name!r},\n  "
            f"url={self.url!r}\n"
            ")"
        )


DATASETS_JSON = {
    # "7zip": {"filename": "7zip.png", "format": "png"},
    "airports": {"filename": "airports.csv", "format": "csv"},
    "annual-precip": {"filename": "annual-precip.json", "format": "json"},
    "anscombe": {"filename": "anscombe.json", "format": "json"},
    "barley": {"filename": "barley.json", "format": "json"},
    "birdstrikes": {"filename": "birdstrikes.json", "format": "json"},
    "budget": {"filename": "budget.json", "format": "json"},
    "budgets": {"filename": "budgets.json", "format": "json"},
    "burtin": {"filename": "burtin.json", "format": "json"},
    "cars": {"filename": "cars.json", "format": "json"},
    "climate": {"filename": "climate.json", "format": "json"},
    "co2-concentration": {"filename": "co2-concentration.csv", "format": "csv"},
    "countries": {"filename": "countries.json", "format": "json"},
    "crimea": {"filename": "crimea.json", "format": "json"},
    "disasters": {"filename": "disasters.csv", "format": "csv"},
    "driving": {"filename": "driving.json", "format": "json"},
    "earthquakes": {"filename": "earthquakes.json", "format": "json"},
    # "ffox": {"filename": "ffox.png", "format": "png"},
    "flare": {"filename": "flare.json", "format": "json"},
    "flare-dependencies": {"filename": "flare-dependencies.json", "format": "json"},
    "flights-10k": {"filename": "flights-10k.json", "format": "json"},
    "flights-200k": {"filename": "flights-200k.json", "format": "json"},
    "flights-20k": {"filename": "flights-20k.json", "format": "json"},
    "flights-2k": {"filename": "flights-2k.json", "format": "json"},
    "flights-3m": {"filename": "flights-3m.csv", "format": "csv"},
    "flights-5k": {"filename": "flights-5k.json", "format": "json"},
    "flights-airport": {"filename": "flights-airport.csv", "format": "csv"},
    "gapminder": {"filename": "gapminder.json", "format": "json"},
    "gapminder-health-income": {
        "filename": "gapminder-health-income.csv",
        "format": "csv",
    },
    # "gimp": {"filename": "gimp.png", "format": "png"},
    "github": {"filename": "github.csv", "format": "csv"},
    "graticule": {"filename": "graticule.json", "format": "json"},
    "income": {"filename": "income.json", "format": "json"},
    "iowa-electricity": {"filename": "iowa-electricity.csv", "format": "csv"},
    "iris": {"filename": "iris.json", "format": "json"},
    "jobs": {"filename": "jobs.json", "format": "json"},
    "la-riots": {"filename": "la-riots.csv", "format": "csv"},
    "londonBoroughs": {"filename": "londonBoroughs.json", "format": "json"},
    "londonCentroids": {"filename": "londonCentroids.json", "format": "json"},
    "londonTubeLines": {"filename": "londonTubeLines.json", "format": "json"},
    "lookup_groups": {"filename": "lookup_groups.csv", "format": "csv"},
    "lookup_people": {"filename": "lookup_people.csv", "format": "csv"},
    "miserables": {"filename": "miserables.json", "format": "json"},
    "monarchs": {"filename": "monarchs.json", "format": "json"},
    "movies": {"filename": "movies.json", "format": "json"},
    "normal-2d": {"filename": "normal-2d.json", "format": "json"},
    "obesity": {"filename": "obesity.json", "format": "json"},
    "ohlc": {"filename": "ohlc.json", "format": "json"},
    "points": {"filename": "points.json", "format": "json"},
    "population": {"filename": "population.json", "format": "json"},
    "population_engineers_hurricanes": {
        "filename": "population_engineers_hurricanes.csv",
        "format": "csv",
    },
    "seattle-temps": {"filename": "seattle-temps.csv", "format": "csv"},
    "seattle-weather": {"filename": "seattle-weather.csv", "format": "csv"},
    "sf-temps": {"filename": "sf-temps.csv", "format": "csv"},
    "sp500": {"filename": "sp500.csv", "format": "csv"},
    "stocks": {"filename": "stocks.csv", "format": "csv"},
    "udistrict": {"filename": "udistrict.json", "format": "json"},
    "unemployment": {"filename": "unemployment.tsv", "format": "tsv"},
    "unemployment-across-industries": {
        "filename": "unemployment-across-industries.json",
        "format": "json",
    },
    "uniform-2d": {"filename": "uniform-2d.json", "format": "json"},
    "us-10m": {"filename": "us-10m.json", "format": "json"},
    "us-employment": {"filename": "us-employment.csv", "format": "csv"},
    "us-state-capitals": {"filename": "us-state-capitals.json", "format": "json"},
    "volcano": {"filename": "volcano.json", "format": "json"},
    "weather": {"filename": "weather.json", "format": "json"},
    "weball26": {"filename": "weball26.json", "format": "json"},
    "wheat": {"filename": "wheat.json", "format": "json"},
    "windvectors": {"filename": "windvectors.csv", "format": "csv"},
    "world-110m": {"filename": "world-110m.json", "format": "json"},
    "zipcodes": {"filename": "zipcodes.csv", "format": "csv"},
}
"""Inlined `datasets.json`_.

- Excluding images

.. _datasets.json:
    https://github.com/altair-viz/vega_datasets/blob/136e850447b49031f04baa137ce5c37a6678bbb1/vega_datasets/datasets.json
"""


class DataLoader:
    source_tag: ClassVar[str] = "v2.9.0"
    _base_url_fmt: str = "https://cdn.jsdelivr.net/npm/vega-datasets@{0}/data/"

    @property
    def base_url(self) -> str:
        return self._base_url_fmt.format(self.source_tag)

    @cached_property
    def _dataset_names(self) -> list[str]:
        return sorted(DATASETS_JSON)

    @cached_property
    def _py_js_names(self) -> dict[str, str]:
        return {_js_to_py(name): name for name in self._dataset_names}

    def list_datasets(self) -> list[str]:
        return list(self._py_js_names)

    def __getattr__(self, name: str) -> Dataset:
        if name in self._py_js_names:
            return Dataset(self._py_js_names[name], self.base_url)
        else:
            msg = f"No dataset named {name!r}"
            raise AttributeError(msg)

    def __dir__(self) -> list[str]:
        return self.list_datasets()

    def url(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
    ) -> str:
        constraints: dict[Literal["tag", "suffix"], str] = {}
        if tag == "latest":
            raise NotImplementedError(tag)
        elif tag is not None:
            constraints["tag"] = tag
        if name.endswith((".csv", ".json", ".tsv", ".arrow")):
            name, suffix = name.rsplit(".", maxsplit=1)
            suffix = "." + suffix
            if not is_ext_supported(suffix):
                raise TypeError(suffix)
            else:
                constraints["suffix"] = suffix
        elif ext is not None:
            if not is_ext_supported(ext):
                raise TypeError(ext)
            else:
                constraints["suffix"] = ext
        q = QueryTree(name_js=name, **constraints)  # type: ignore[typeddict-item]
        return app.github.query.url_from(**q)

    def __call__(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
    ) -> WorkInProgress:
        """
        **WIP** Will be using this *instead of* attribute access.

        - Original supports this as well
        - Will only be using the actual (js_name)
        - Some have hyphens, others underscores
        """
        return self.url(name, ext, tag=tag)


data = DataLoader()
