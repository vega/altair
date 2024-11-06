"""
Adapted from `altair-viz/vega_datasets`_.

.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import json
import os
import random
import tempfile
import time
import urllib.request
import warnings
from collections.abc import Iterable, Iterator, Sequence
from functools import cached_property, partial
from itertools import islice
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Callable, ClassVar, Literal, cast, get_args
from urllib.request import urlopen

import polars as pl

from tools.datasets import semver
from tools.datasets.models import (
    GitHubRateLimitResources,
    GitHubTag,
    GitHubTree,
    GitHubTreesResponse,
    GitHubUrl,
    NpmPackageMetadataResponse,
    NpmUrl,
    ParsedRateLimit,
    ParsedTag,
    ParsedTree,
    QueryTree,
    ReParsedTag,
)

if TYPE_CHECKING:
    import sys
    from collections.abc import Mapping, MutableMapping
    from email.message import Message
    from urllib.request import OpenerDirector, Request

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
    from tools.schemapi.utils import OneOrSeq

    _PathName: TypeAlias = Literal["dir", "tags", "trees"]
    WorkInProgress: TypeAlias = Any


_ItemSlice: TypeAlias = (
    "tuple[int | None, int | Literal['url_npm', 'url_github'] | None]"
)
"""Query result scalar selection."""

_NPM_BASE_URL = "https://cdn.jsdelivr.net/npm/vega-datasets@"
_SUB_DIR = "data"


def _is_str(obj: Any) -> TypeIs[str]:
    return isinstance(obj, str)


class _ErrorHandler(urllib.request.BaseHandler):
    """
    Adds `rate limit`_ info to a forbidden error.

    .. _rate limit:
        https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    """

    def http_error_default(
        self, req: Request, fp: IO[bytes] | None, code: int, msg: str, hdrs: Message
    ):
        if code == 403 and (reset := hdrs.get("X-RateLimit-Reset", None)):
            limit = hdrs.get("X-RateLimit-Limit", "")
            remaining = hdrs.get("X-RateLimit-Remaining", "")
            msg = (
                f"{msg}\n\nFailed to balance rate limit.\n"
                f"{limit=}, {remaining=}\n"
                f"Reset: {time.localtime(int(reset))!r}"
            )
        raise urllib.request.HTTPError(req.full_url, code, msg, hdrs, fp)


class _GitHubRequestNamespace:
    """
    Fetching resources from the `GitHub API`_.

    .. _GitHub API:
        https://docs.github.com/en/rest/about-the-rest-api/about-the-rest-api?apiVersion=2022-11-28
    """

    _ENV_VAR: LiteralString = "VEGA_GITHUB_TOKEN"
    _TAGS_MAX_PAGE: Literal[100] = 100
    _VERSION: LiteralString = "2022-11-28"
    _UNAUTH_RATE_LIMIT: Literal[60] = 60
    _TAGS_COST: Literal[1] = 1
    _TREES_COST: Literal[2] = 2
    _UNAUTH_DELAY: Literal[5] = 5
    _AUTH_DELAY: Literal[1] = 1
    _UNAUTH_TREES_LIMIT: Literal[10] = 10

    def __init__(self, gh: _GitHub, /) -> None:
        self._gh = gh

    @property
    def url(self) -> GitHubUrl:
        return self._gh.url

    def rate_limit(self) -> GitHubRateLimitResources:
        """https://docs.github.com/en/rest/rate-limit/rate-limit?apiVersion=2022-11-28#get-rate-limit-status-for-the-authenticated-user."""
        with self._gh._opener.open(self._request(self.url.RATE)) as response:
            content: GitHubRateLimitResources = json.load(response)["resources"]
        return content

    def tags(self, n: int, *, warn_lower: bool) -> list[GitHubTag]:
        """https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-tags."""
        if n < 1 or n > self._TAGS_MAX_PAGE:
            raise ValueError(n)
        req = self._request(f"{self.url.TAGS}?per_page={n}")
        with self._gh._opener.open(req) as response:
            content: list[GitHubTag] = json.load(response)
        if warn_lower and len(content) < n:
            earliest = response[-1]["name"]
            n_response = len(content)
            msg = f"Requested {n=} tags, but got {n_response}\n" f"{earliest=}"
            warnings.warn(msg, stacklevel=3)
        return content

    def trees(self, tag: str | ParsedTag, /) -> GitHubTreesResponse:
        """
        For a given ``tag``, perform **2x requests** to get directory metadata.

        Returns response unchanged - but with annotations.
        """
        if _is_str(tag):
            url = tag if tag.startswith(self.url.TREES) else f"{self.url.TREES}{tag}"
        else:
            url = tag["trees_url"]
        with self._gh._opener.open(self._request(url)) as response:
            content: GitHubTreesResponse = json.load(response)
        query = (tree["url"] for tree in content["tree"] if tree["path"] == _SUB_DIR)
        if data_url := next(query, None):
            with self._gh._opener.open(self._request(data_url)) as response:
                data_dir: GitHubTreesResponse = json.load(response)
            return data_dir
        else:
            raise FileNotFoundError

    def _request(self, url: str, /, *, raw: bool = False) -> Request:
        """
        Wrap a request url with a `personal access token`_ - if set as an env var.

        By default the endpoint returns json, specify raw to get blob data.
        See `Media types`_.

        .. _personal access token:
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
        .. _Media types:
        https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28#media-types
        """
        headers: MutableMapping[str, str] = {"X-GitHub-Api-Version": self._VERSION}
        if tok := os.environ.get(self._ENV_VAR):
            headers["Authorization"] = (
                tok if tok.startswith("Bearer ") else f"Bearer {tok}"
            )
        if raw:
            headers["Accept"] = "application/vnd.github.raw+json"
        return urllib.request.Request(url, headers=headers)


class _GitHubParseNamespace:
    """
    Transform responses into intermediate representations.

    Where relevant:
    - Adding cheap to compute metadata
    - Dropping information that we don't need for the task
    """

    def __init__(self, gh: _GitHub, /) -> None:
        self._gh = gh

    @property
    def url(self) -> GitHubUrl:
        return self._gh.url

    def rate_limit(self, rate_limit: GitHubRateLimitResources, /) -> ParsedRateLimit:
        core = rate_limit["core"]
        reset = core["reset"]
        return ParsedRateLimit(
            **core,
            reset_time=time.localtime(reset),
            is_limited=core["remaining"] == 0,
            is_auth=core["limit"] > self._gh.req._UNAUTH_RATE_LIMIT,
        )

    def tag(self, tag: GitHubTag, /) -> ParsedTag:
        sha = tag["commit"]["sha"]
        return ParsedTag(tag=tag["name"], sha=sha, trees_url=f"{self.url.TREES}{sha}")

    def tags(self, tags: list[GitHubTag], /) -> list[ParsedTag]:
        return [self.tag(t) for t in tags]

    def tree(self, tree: GitHubTree, tag: str, /) -> ParsedTree:
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
            tag=tag,
        )

    def trees(self, tree: GitHubTreesResponse, /, tag: str) -> list[ParsedTree]:
        """For a tree response (directory of files) convert to an IR with only relevant properties."""
        return [self.tree(t, tag) for t in tree["tree"]]


class _GitHubQueryNamespace:
    """**WIP** Interfacing with the cached metadata."""

    def __init__(self, gh: _GitHub, /) -> None:
        self._gh = gh

    @property
    def paths(self) -> dict[_PathName, Path]:
        return self._gh._paths

    def url_from(
        self,
        *predicates: OneOrSeq[str | pl.Expr],
        item: _ItemSlice = (0, "url_npm"),
        **constraints: Any,
    ) -> str:
        """Querying multi-version trees metadata for `npm` url to fetch."""
        fp = self.paths["trees"]
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


class _GitHub:
    """
    Primary interface with the GitHub API.

    Maintains up-to-date metadata, describing **every** available dataset across **all known** releases.

    - Uses `tags`_, `trees`_, `rate_limit`_ endpoints.
    - Organizes distinct groups of operations into property accessor namespaces.


    .. _tags:
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-tags
    .. _trees:
        https://docs.github.com/en/rest/git/trees?apiVersion=2022-11-28#get-a-tree
    .. _rate_limit:
        https://docs.github.com/en/rest/rate-limit/rate-limit?apiVersion=2022-11-28#get-rate-limit-status-for-the-authenticated-user

    """

    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener(_ErrorHandler)

    def __init__(
        self,
        output_dir: Path,
        name_tags: str,
        name_trees: str,
        *,
        base_url: LiteralString = "https://api.github.com/",
        org: LiteralString = "vega",
        package: LiteralString = "vega-datasets",
    ) -> None:
        output_dir.mkdir(exist_ok=True)
        self._paths: dict[_PathName, Path] = {
            "dir": output_dir,
            "tags": output_dir / f"{name_tags}.parquet",
            "trees": output_dir / f"{name_trees}.parquet",
        }
        repo = f"{base_url}repos/{org}/{package}/"
        self._url = GitHubUrl(
            BASE=base_url,
            RATE=f"{base_url}rate_limit",
            REPO=repo,
            TAGS=f"{repo}tags",
            TREES=f"{repo}git/trees/",
        )

    @property
    def req(self) -> _GitHubRequestNamespace:
        return _GitHubRequestNamespace(self)

    @property
    def parse(self) -> _GitHubParseNamespace:
        return _GitHubParseNamespace(self)

    @property
    def query(self) -> _GitHubQueryNamespace:
        return _GitHubQueryNamespace(self)

    @property
    def url(self) -> GitHubUrl:
        return self._url

    def rate_limit(self, *, strict: bool = False) -> ParsedRateLimit:
        limit = self.parse.rate_limit(self.req.rate_limit())
        if strict and limit["is_limited"]:
            raise NotImplementedError(limit)
        return limit

    def tags(
        self, n_head: int | None = None, *, warn_lower: bool = False
    ) -> pl.DataFrame:
        tags = self.req.tags(n_head or self.req._TAGS_MAX_PAGE, warn_lower=warn_lower)
        return pl.DataFrame(self.parse.tags(tags)).pipe(semver.with_columns)

    def trees(self, tag: str | ParsedTag, /) -> pl.DataFrame:
        """Retrieve directory info for a given version ``tag``."""
        trees = self.req.trees(tag)
        tag_v = _tag_from(tag) if _is_str(tag) else tag["tag"]
        parsed = self.parse.trees(trees, tag=tag_v)
        df = (
            pl.DataFrame(parsed)
            .lazy()
            .rename({"url": "url_github"})
            .with_columns(name_collision=pl.col("name_py").is_duplicated())
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

    def refresh_trees(self, gh_tags: pl.DataFrame, /) -> pl.DataFrame:
        """
        Use known tags to discover and update missing trees metadata.

        Aims to stay well-within API rate limits, both for authenticated ad unauthenticated users.
        """
        rate_limit = self.rate_limit(strict=True)
        fp = self._paths["trees"]
        trees = pl.read_parquet(fp)
        missing_trees = gh_tags.join(
            trees.select(pl.col("tag").unique()), on="tag", how="anti"
        )
        if missing_trees.is_empty():
            print(f"Already up-to-date {fp!s}")
            return trees
        else:
            stop = None if rate_limit["is_auth"] else self.req._UNAUTH_TREES_LIMIT
            it = islice(missing_trees.iter_rows(named=True), stop)
            missing = cast("Iterator[ReParsedTag]", it)
            fresh_rows = self._trees_batched(missing)
            print(
                f"Finished collection.\n"
                f"Writing {fresh_rows.height} new rows to {fp!s}"
            )
            return pl.concat((trees, fresh_rows)).pipe(semver.sort)

    def refresh_tags(self, npm_tags: pl.DataFrame, /) -> pl.DataFrame:
        limit = self.rate_limit(strict=True)
        npm_tag_only = npm_tags.lazy().select("tag")
        fp = self._paths["tags"]
        if not limit["is_auth"] and limit["remaining"] <= self.req._TAGS_COST:
            return (
                pl.scan_parquet(fp).join(npm_tag_only, on="tag", how="inner").collect()
            )
        elif not fp.exists():
            print(f"Initializing {fp!s}")
            tags = (
                self.tags().lazy().join(npm_tag_only, on="tag", how="inner").collect()
            )
            print(f"Collected {tags.height} new tags")
            return tags
        else:
            print("Checking for new tags")
            prev = pl.scan_parquet(fp)
            latest = (
                self.tags(1).lazy().join(npm_tag_only, on="tag", how="inner").collect()
            )
            if latest.equals(prev.pipe(semver.sort).head(1).collect()):
                print(f"Already up-to-date {fp!s}")
                return prev.collect()
            print(f"Refreshing {fp!s}")
            prev_eager = prev.collect()
            tags = (
                pl.concat((self.tags(), prev_eager), how="vertical")
                .unique("sha")
                .pipe(semver.sort)
            )
            print(f"Collected {tags.height - prev_eager.height} new tags")
            return tags

    def _trees_batched(self, tags: Iterable[str | ParsedTag], /) -> pl.DataFrame:
        rate_limit = self.rate_limit(strict=True)
        if not isinstance(tags, Sequence):
            tags = tuple(tags)
        req = self.req
        n = len(tags)
        cost = req._TREES_COST * n
        if rate_limit["remaining"] < cost:
            raise NotImplementedError(rate_limit, cost)
        delay_secs = req._AUTH_DELAY if rate_limit["is_auth"] else req._UNAUTH_DELAY
        print(
            f"Collecting metadata for {n} missing releases.\n"
            f"Using {delay_secs=} between requests ..."
        )
        dfs: list[pl.DataFrame] = []
        for tag in tags:
            time.sleep(delay_secs + random.triangular())
            dfs.append(self.trees(tag))
        return pl.concat(dfs)


#######################################################################################


class _Npm:
    """https://www.jsdelivr.com/docs/data.jsdelivr.com#overview."""

    def __init__(
        self,
        output_dir: Path,
        name_tags: str,
        *,
        jsdelivr: Literal["jsdelivr"] = "jsdelivr",
        npm: Literal["npm"] = "npm",
        package: LiteralString = "vega-datasets",
        jsdelivr_version: LiteralString = "v1",
    ) -> None:
        output_dir.mkdir(exist_ok=True)
        self._paths: dict[Literal["tags"], Path] = {
            "tags": output_dir / f"{name_tags}.parquet"
        }
        self._url: NpmUrl = NpmUrl(
            CDN=f"https://cdn.{jsdelivr}.net/{npm}/{package}@",
            TAGS=f"https://data.{jsdelivr}.com/{jsdelivr_version}/packages/{npm}/{package}",
        )

    @property
    def url(self) -> NpmUrl:
        return self._url

    def tags(self) -> pl.DataFrame:
        """
        Request, parse tags from `Get package metadata`_.

        Notes
        -----
        - Ignores canary releases
        - ``npm`` can accept either, but this endpoint returns without "v":

            {tag}
            v{tag}

        .. _Get package metadata:
            https://www.jsdelivr.com/docs/data.jsdelivr.com#get-/v1/packages/npm/-package-
        """
        req = urllib.request.Request(
            self.url.TAGS, headers={"Accept": "application/json"}
        )
        with urllib.request.urlopen(req) as response:
            content: NpmPackageMetadataResponse = json.load(response)
        versions = [
            f"v{tag}"
            for v in content["versions"]
            if (tag := v["version"]) and semver.CANARY not in tag
        ]
        return pl.DataFrame({"tag": versions}).pipe(semver.with_columns)


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
        self._github: _GitHub = _GitHub(
            output_dir, name_tags=tags_gh, name_trees=trees_gh, **kwds_gh
        )
        self._npm: _Npm = _Npm(output_dir, name_tags=tags_npm, **kwds_npm)

    @property
    def github(self) -> _GitHub:
        return self._github

    @property
    def npm(self) -> _Npm:
        return self._npm

    def refresh(self) -> pl.DataFrame:
        npm_tags = self.npm.tags()
        self.write_parquet(npm_tags, self.npm._paths["tags"])

        gh_tags = self.github.refresh_tags(npm_tags)
        self.write_parquet(gh_tags, self.github._paths["tags"])

        gh_trees = self.github.refresh_trees(gh_tags)
        self.write_parquet(gh_trees, self.github._paths["trees"])
        return gh_trees

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


def _tag_from(s: str, /) -> str:
    # - Actual tag
    # - Trees url (using ref name)
    # - npm url (works w/o the `v` prefix)
    trees_url = app.github.url.TREES
    if s.startswith("v"):
        return s
    elif s.startswith(trees_url):
        return s.replace(trees_url, "")
    elif s.startswith(_NPM_BASE_URL):
        s, _ = s.replace(_NPM_BASE_URL, "").split("/")
        return s if s.startswith("v") else f"v{s}"
    else:
        raise TypeError(s)


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

    def __call__(
        self,
        name: str,
        ext: ExtSupported | None = None,
        /,
        tag: LiteralString | Literal["latest"] | None = None,
    ) -> WorkInProgress:
        """
        **WIP** Will be using this *instead of* attribute access.

        - Original supports this as well
        - Will only be using the actual (js_name)
        - Some have hyphens, others underscores
        """
        constraints: dict[Literal["tag", "suffix"], str] = {}
        if tag == "latest":
            raise NotImplementedError(tag)
        elif tag is not None:
            constraints["tag"] = tag
        if name.endswith(get_args(ExtSupported)):
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


data = DataLoader()