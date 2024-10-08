"""
Adapted from `altair-viz/vega_datasets`_.

.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import json
import os
import tempfile
import warnings
from functools import cached_property, partial
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, TypedDict
from urllib.request import Request, urlopen

import polars as pl

if TYPE_CHECKING:
    import sys

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from tools.schemapi.utils import OneOrSeq


_ItemSlice: TypeAlias = "tuple[int | None, int | str | None]"
"""Query result scalar selection."""

_GITHUB_URL = "https://api.github.com/"
_GITHUB_VEGA_DATASETS_URL = f"{_GITHUB_URL}repos/vega/vega-datasets/"
_GITHUB_TAGS_URL = f"{_GITHUB_VEGA_DATASETS_URL}tags"
_GITHUB_TREES_URL = f"{_GITHUB_VEGA_DATASETS_URL}git/trees/"
_NPM_BASE_URL = "https://cdn.jsdelivr.net/npm/vega-datasets@"
_SUB_DIR = "data"
_TAGS_MAX_PAGE: Literal[100] = 100
_SEM_VER_FIELDS: tuple[
    Literal["major"], Literal["minor"], Literal["patch"], Literal["pre_release"]
] = "major", "minor", "patch", "pre_release"


def _is_str(obj: Any) -> TypeIs[str]:
    return isinstance(obj, str)


class GitHubTag(TypedDict):
    name: str
    node_id: str
    commit: dict[Literal["sha", "url"], str]
    zipball_url: str
    tarball_url: str


class ParsedTag(TypedDict):
    tag: str
    sha: str
    trees_url: str


class GitHubTree(TypedDict):
    """
    A single file's metadata within the response of `Get a tree`_.

    .. _Get a tree:
        https://docs.github.com/en/rest/git/trees?apiVersion=2022-11-28#get-a-tree
    """

    path: str
    mode: str
    type: str
    sha: str
    size: int
    url: str


class GitHubTreesResponse(TypedDict):
    """
    Response from `Get a tree`_.

    Describes directory metadata, with files stored in ``"tree"``.

    .. _Get a tree:
        https://docs.github.com/en/rest/git/trees?apiVersion=2022-11-28#get-a-tree
    """

    sha: str
    url: str
    tree: list[GitHubTree]
    truncated: bool


class GitHubBlobResponse(TypedDict):
    """
    Response from `Get a blob`_.

    Obtained by following ``GitHubTree["url"]``.

    .. _Get a blob:
        https://docs.github.com/en/rest/git/blobs?apiVersion=2022-11-28#get-a-blob
    """

    content: str
    sha: str
    node_id: str
    size: int | None
    encoding: str
    url: str


class ParsedTree(TypedDict):
    file_name: str
    name_js: str
    name_py: str
    suffix: str
    size: int
    url: str
    ext_supported: bool


class ParsedTreesResponse(TypedDict):
    tag: str
    url: str
    tree: list[ParsedTree]


def _request_github(url: str, /, *, raw: bool = False) -> Request:
    """
    Wrap a request url with a `personal access token`_ - if set as an env var.

    By default the endpoint returns json, specify raw to get blob data.
    See `Media types`_.

    .. _personal access token:
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    .. _Media types:
        https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28#media-types
    """
    headers = {}
    if tok := os.environ.get("VEGA_GITHUB_TOKEN"):
        headers["Authorization"] = tok
    if raw:
        headers["Accept"] = "application/vnd.github.raw+json"
    return Request(url, headers=headers)


def _request_trees(tag: str | Any, /) -> GitHubTreesResponse:
    """
    For a given ``tag``, perform 2x requests to get directory metadata.

    Returns response unchanged - but with annotations.
    """
    if _is_str(tag):
        url = tag if tag.startswith(_GITHUB_TREES_URL) else f"{_GITHUB_TREES_URL}{tag}"
    else:
        url = tag["trees_url"]
    with urlopen(_request_github(url)) as response:
        content: GitHubTreesResponse = json.load(response)
    query = (tree["url"] for tree in content["tree"] if tree["path"] == _SUB_DIR)
    if data_url := next(query, None):
        with urlopen(data_url) as response:
            data_dir: GitHubTreesResponse = json.load(response)
        return data_dir
    else:
        raise FileNotFoundError


def _request_tags(n: int = 30, *, warn_lower: bool) -> list[GitHubTag]:
    """https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-tags."""
    if n < 1 or n > _TAGS_MAX_PAGE:
        raise ValueError(n)
    with urlopen(_request_github(f"{_GITHUB_TAGS_URL}?per_page={n}")) as response:
        content: list[GitHubTag] = json.load(response)
    if warn_lower and len(content) < n:
        earliest = response[-1]["name"]
        n_response = len(content)
        msg = f"Requested {n=} tags, but got {n_response}\n" f"{earliest=}"
        warnings.warn(msg, stacklevel=3)
    return content


def _parse_tag(tag: GitHubTag, /) -> ParsedTag:
    sha = tag["commit"]["sha"]
    return ParsedTag(tag=tag["name"], sha=sha, trees_url=f"{_GITHUB_TREES_URL}{sha}")


def _with_sem_ver(df: pl.DataFrame, *, col_tag: str = "tag") -> pl.DataFrame:
    """
    Extracts components of a `SemVer`_ string into sortable columns.

    .. _SemVer:
        https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions
    """
    fields = pl.col(_SEM_VER_FIELDS)
    pattern = r"""(?x)
        v(?<major>[[:digit:]]*)\.
        (?<minor>[[:digit:]]*)\.
        (?<patch>[[:digit:]]*)
        (\-next\.)?
        (?<pre_release>[[:digit:]]*)?
    """
    sem_ver = pl.col(col_tag).str.extract_groups(pattern).struct.field(*_SEM_VER_FIELDS)
    return (
        df.lazy()
        .with_columns(sem_ver)
        .with_columns(pl.when(fields.str.len_chars() > 0).then(fields).cast(pl.Int64))
        .with_columns(is_pre_release=pl.col("pre_release").is_not_null())
        .collect()
    )


def request_tags_to_df(n_head: int | None, *, warn_lower: bool = False) -> pl.DataFrame:
    response = _request_tags(n=n_head or _TAGS_MAX_PAGE, warn_lower=warn_lower)
    return pl.DataFrame([_parse_tag(tag) for tag in response]).pipe(_with_sem_ver)


def _parse_tree(tree: GitHubTree, /) -> ParsedTree:
    """For a single tree (file) convert to an IR with only relevant properties."""
    path = Path(tree["path"])
    return ParsedTree(
        file_name=path.name,
        name_js=path.stem,
        name_py=_js_to_py(path.stem),
        suffix=path.suffix,
        size=tree["size"],
        url=tree["url"],
        ext_supported=is_ext_supported(path.suffix),
    )


def _parse_trees_response(
    tree: GitHubTreesResponse, /, tag: str
) -> ParsedTreesResponse:
    """For a tree response (directory of files) convert to an IR with only relevant properties."""
    return ParsedTreesResponse(
        tag=tag, url=tree["url"], tree=[_parse_tree(t) for t in tree["tree"]]
    )


def request_trees_to_df(tag: str, /) -> pl.DataFrame:
    response = _request_trees(tag)
    parsed = _parse_trees_response(response, tag=tag)
    df = (
        pl.DataFrame(parsed["tree"])
        .lazy()
        .rename({"url": "url_github"})
        .with_columns(name_collision=pl.col("name_py").is_duplicated(), tag=pl.lit(tag))
        .with_columns(
            url_npm=pl.concat_str(
                pl.lit(_NPM_BASE_URL),
                pl.col("tag"),
                pl.lit(f"/{_SUB_DIR}/"),
                pl.col("file_name"),
            )
        )
        .collect()
    )
    return df.select(*sorted(df.columns))


def request_trees_to_df_batched(*tags: str, delay: int = 5) -> pl.DataFrame:
    import random
    import time

    dfs: list[pl.DataFrame] = []
    for tag in tags:
        time.sleep(delay + random.triangular())
        dfs.append(request_trees_to_df(tag))
    return pl.concat(dfs)


def _write_parquet(
    frame: pl.DataFrame | pl.LazyFrame, fp: Path, /, *, write_schema: bool
) -> None:
    """
    Write ``frame`` to ``fp``, with some extra safety.

    When ``write_schema``, an addtional ``...-schema.json`` file is produced
    that describes the metadata columns.
    """
    if not fp.exists():
        fp.touch()
    df = frame.lazy().collect()
    df.write_parquet(fp, compression="zstd", compression_level=17)
    if write_schema:
        schema = {name: tp.__name__ for name, tp in df.schema.to_python().items()}
        fp_schema = fp.with_name(f"{fp.stem}-schema.json")
        if not fp_schema.exists():
            fp_schema.touch()
        with fp_schema.open("w") as f:
            json.dump(schema, f, indent=2)


def collect_metadata(tag: str, /, fp: Path, *, write_schema: bool = True) -> None:
    """
    Retrieve directory info for a given version ``tag``, writing to ``fp``.

    When ``write_schema``, an addtional ``...-schema.json`` file is produced
    that describes the metadata columns.
    """
    metadata = request_trees_to_df(tag)
    _write_parquet(metadata, fp, write_schema=write_schema)


def collect_tags(
    n_head: int | None, fp: Path, *, warn_lower: bool = False, write_schema: bool = True
):
    tags = request_tags_to_df(n_head, warn_lower=warn_lower)
    _write_parquet(tags, fp, write_schema=write_schema)


def refresh_tags(fp: Path, *, limit_new: int = 10) -> pl.DataFrame:
    if fp.exists():
        print("Checking for new tags")
        prev = pl.read_parquet(fp)
        prev_latest = prev.sort(_SEM_VER_FIELDS, descending=True).head(1)
        curr_latest = request_tags_to_df(1)
        if curr_latest.equals(prev_latest):
            print(f"Already up-to-date {fp!s}")
            return prev
        else:
            # Work out how far behind?
            print(f"Refreshing {fp!s}")
            fresh = (
                pl.concat((request_tags_to_df(limit_new), prev), how="vertical")
                .unique("sha")
                .sort(_SEM_VER_FIELDS, descending=True)
            )
            _write_parquet(fresh, fp, write_schema=True)
            print(f"Collected {fresh.height - prev.height} new tags")
            return fresh
    else:
        print(f"Initializing {fp!s}")
        collect_tags(None, fp)
        return pl.read_parquet(fp)


def url_from(
    fp: Path,
    *predicates: OneOrSeq[str | pl.Expr],
    item: _ItemSlice = (0, "url_npm"),
    **constraints: Any,
) -> str:
    """Querying multi-version trees metadata for `npm` url to fetch."""
    if fp.suffix != ".parquet":
        raise NotImplementedError(fp.suffix)
    items = pl.scan_parquet(fp).filter(*predicates, **constraints).collect()
    if items.is_empty():
        msg = f"Found no results for:\n" f"{predicates!r}\n{constraints!r}"
        raise NotImplementedError(msg)
    r = items.item(*item)
    if _is_str(r):
        return r
    else:
        msg = f"Expected 'str' but got {type(r).__name__!r} from {r!r}."
        raise TypeError(msg)


# This is the tag in http://github.com/vega/vega-datasets from
# which the datasets in this repository are sourced.
_OLD_SOURCE_TAG = "v1.29.0"  # 5 years ago
_CURRENT_SOURCE_TAG = "v2.9.0"

ExtSupported: TypeAlias = Literal[".csv", ".json", ".tsv", ".arrow"]
"""
- `'flights-200k.(arrow|json)'` key collison using stem
"""


def is_ext_supported(suffix: str) -> TypeIs[ExtSupported]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}


def _py_to_js(s: str, /):
    return s.replace("_", "-")


def _js_to_py(s: str, /):
    return s.replace("-", "_")


class Dataset:
    read_fn: ClassVar[dict[ExtSupported, Callable[..., pl.DataFrame]]] = {
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
            self.extension: ExtSupported = suffix
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


DATASET_NAMES_USED = (
    "airports",
    "anscombe",
    "barley",
    "cars",
    "co2_concentration",
    "countries",
    "disasters",
    "driving",
    "earthquakes",
    "flights_2k",
    "flights_5k",
    "flights_airport",
    "gapminder_health_income",
    "github",
    "income",
    "iowa_electricity",
    "iris",
    "jobs",
    "londonBoroughs",
    "londonCentroids",
    "londonTubeLines",
    "monarchs",
    "movies",
    "normal_2d",
    "ohlc",
    "population",
    "population_engineers_hurricanes",
    "seattle_weather",
    "sp500",
    "stocks",
    "unemployment",
    "unemployment_across_industries",
    "us_10m",
    "us_employment",
    "us_state_capitals",
    "us_unemployment",
    "wheat",
    "windvectors",
    "world_110m",
    "zipcodes",
)
"""Every name that is referenced in *at least* one example/test."""


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


data = DataLoader()
