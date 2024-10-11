"""
Adapted from `altair-viz/vega_datasets`_.

.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import json
import os
import random
import sys
import tempfile
import time
import urllib.request
import warnings
from functools import cached_property, partial
from itertools import islice
from pathlib import Path
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Iterable,
    Iterator,
    Literal,
    NamedTuple,
    Sequence,
    cast,
    get_args,
)
from urllib.request import urlopen

import polars as pl

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if TYPE_CHECKING:
    from email.message import Message
    from typing import MutableMapping, TypeVar
    from urllib.request import OpenerDirector, Request

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs
    if sys.version_info >= (3, 11):
        from typing import LiteralString, Required
    else:
        from typing_extensions import LiteralString, Required
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from tools.schemapi.utils import OneOrSeq

    _Frame = TypeVar("_Frame", pl.DataFrame, pl.LazyFrame)
    _PathName: TypeAlias = Literal["dir", "tags", "trees"]


_ItemSlice: TypeAlias = (
    "tuple[int | None, int | Literal['url_npm', 'url_github'] | None]"
)
"""Query result scalar selection."""

_NPM_BASE_URL = "https://cdn.jsdelivr.net/npm/vega-datasets@"
_SUB_DIR = "data"
_SEM_VER_FIELDS: tuple[
    Literal["major"], Literal["minor"], Literal["patch"], Literal["pre_release"]
] = "major", "minor", "patch", "pre_release"


def _is_str(obj: Any) -> TypeIs[str]:
    return isinstance(obj, str)


class GitHubUrl(NamedTuple):
    BASE: LiteralString
    RATE: LiteralString
    REPO: LiteralString
    TAGS: LiteralString
    TREES: LiteralString


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


class ReParsedTag(ParsedTag):
    major: int
    minor: int
    patch: int
    pre_release: int | None
    is_pre_release: bool


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


class ParsedTree(TypedDict):
    file_name: str
    name_js: str
    name_py: str
    suffix: str
    size: int
    url: str
    ext_supported: bool
    tag: str


class QueryTree(TypedDict, total=False):
    file_name: str
    name_js: Required[str]
    name_py: str
    suffix: str
    size: int
    url: str
    ext_supported: bool
    tag: str


class ParsedTreesResponse(TypedDict):
    tag: str
    url: str
    tree: list[ParsedTree]


class GitHubRateLimit(TypedDict):
    limit: int
    used: int
    remaining: int
    reset: int


class ParsedRateLimit(GitHubRateLimit):
    reset_time: time.struct_time
    is_limited: bool
    is_auth: bool


class GitHubRateLimitResources(TypedDict, total=False):
    """
    A subset of response from `Get rate limit status for the authenticated user`_.

    .. _Get rate limit status for the authenticated user:
        https://docs.github.com/en/rest/rate-limit/rate-limit?apiVersion=2022-11-28#get-rate-limit-status-for-the-authenticated-user
    """

    core: Required[GitHubRateLimit]
    search: Required[GitHubRateLimit]
    graphql: GitHubRateLimit
    integration_manifest: GitHubRateLimit
    code_search: GitHubRateLimit


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
        write_schema: bool,
        base_url: LiteralString = "https://api.github.com/",
    ) -> None:
        # When ``write_schema``, addtional ``...-schema.json`` file(s) are produced
        # that describes column types - in a non-binary format.
        self._write_schema: bool = write_schema
        output_dir.mkdir(exist_ok=True)
        self._paths: dict[_PathName, Path] = {
            "dir": output_dir,
            "tags": output_dir / f"{name_tags}.parquet",
            "trees": output_dir / f"{name_trees}.parquet",
        }
        repo = f"{base_url}repos/vega/vega-datasets/"
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

    def rate_limit(self) -> ParsedRateLimit:
        return self.parse.rate_limit(self.req.rate_limit())

    def tags(self, n_head: int | None, *, warn_lower: bool = False) -> pl.DataFrame:
        tags = self.req.tags(n_head or self.req._TAGS_MAX_PAGE, warn_lower=warn_lower)
        return pl.DataFrame(self.parse.tags(tags)).pipe(_with_sem_ver)

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

    def refresh(
        self, fp_tags: Path | None = None, fp_trees: Path | None = None
    ) -> pl.DataFrame:
        """
        Use known tags to discover and update missing trees metadata.

        Aims to stay well-within API rate limits, both for authenticated ad unauthenticated users.
        """
        rate_limit = self.rate_limit()
        if rate_limit["is_limited"]:
            raise NotImplementedError(rate_limit)
        fp_tags = fp_tags or self._paths["tags"]
        fp_trees = fp_trees or self._paths["trees"]
        IS_AUTH = rate_limit["is_auth"]
        UNAUTH_LIMIT = self.req._UNAUTH_TREES_LIMIT

        tags = (
            self._refresh_tags(fp_tags)
            if IS_AUTH or rate_limit["remaining"] > UNAUTH_LIMIT
            else pl.read_parquet(fp_tags)
        )
        trees = pl.read_parquet(fp_trees)

        missing_trees = tags.join(
            trees.select(pl.col("tag").unique()), on="tag", how="anti"
        )
        if missing_trees.is_empty():
            print(f"Already up-to-date {fp_trees!s}")
            return trees
        else:
            it = islice(
                missing_trees.iter_rows(named=True), None if IS_AUTH else UNAUTH_LIMIT
            )
            missing = cast("Iterator[ReParsedTag]", it)
            fresh_rows = self._trees_batched(missing)
            print(
                f"Finished collection.\n"
                f"Writing {fresh_rows.height} new rows to {fp_trees!s}"
            )
            refreshed = pl.concat((trees, fresh_rows)).pipe(_sort_sem_ver)
            _write_parquet(refreshed, fp_trees, write_schema=self._write_schema)
            return refreshed

    def _trees_batched(self, tags: Iterable[str | ParsedTag], /) -> pl.DataFrame:
        rate_limit = self.rate_limit()
        if rate_limit["is_limited"]:
            raise NotImplementedError(rate_limit)
        elif not isinstance(tags, Sequence):
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

    def _refresh_tags(
        self, fp: Path | None = None, *, limit_new: int | None = None
    ) -> pl.DataFrame:
        n_new_tags: int = 0
        fp = fp or self._paths["tags"]
        if not fp.exists():
            print(f"Initializing {fp!s}")
            tags = self.tags(limit_new)
            n_new_tags = tags.height
        else:
            print("Checking for new tags")
            prev = pl.scan_parquet(fp)
            curr_latest = self.tags(1)
            if curr_latest.equals(prev.pipe(_sort_sem_ver).head(1).collect()):
                print(f"Already up-to-date {fp!s}")
                return prev.collect()
            else:
                print(f"Refreshing {fp!s}")
                prev_eager = prev.collect()
                tags = (
                    pl.concat((self.tags(limit_new), prev_eager), how="vertical")
                    .unique("sha")
                    .pipe(_sort_sem_ver)
                )
                n_new_tags = tags.height - prev_eager.height
        print(f"Collected {n_new_tags} new tags")
        _write_parquet(tags, fp, write_schema=self._write_schema)
        return tags


GitHub = _GitHub(
    Path(__file__).parent / "_vega_datasets_data",
    name_trees="metadata_full",
    name_tags="tags",
    write_schema=True,
)

#######################################################################################


def _tag_from(s: str, /) -> str:
    # - Actual tag
    # - Trees url (using ref name)
    # - npm url (works w/o the `v` prefix)
    trees_url = GitHub.url.TREES
    if s.startswith("v"):
        return s
    elif s.startswith(trees_url):
        return s.replace(trees_url, "")
    elif s.startswith(_NPM_BASE_URL):
        s, _ = s.replace(_NPM_BASE_URL, "").split("/")
        return s if s.startswith("v") else f"v{s}"
    else:
        raise TypeError(s)


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


def _sort_sem_ver(frame: _Frame, /) -> _Frame:
    """Sort ``frame``, displaying in descending release order."""
    return frame.sort(_SEM_VER_FIELDS, descending=True)


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

    # BUG: # 1.6.0 exists on GH but not npm?
    def __call__(
        self,
        name: str,
        ext: ExtSupported | None = None,
        /,
        tag: LiteralString | Literal["latest"] | None = None,
    ):
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
        return GitHub.query.url_from(**q)


data = DataLoader()
