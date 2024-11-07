from __future__ import annotations

import json
import os
import random
import time
import urllib.request
import warnings
from collections.abc import Iterable, Iterator, Sequence
from itertools import islice
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, ClassVar, Literal, cast

import polars as pl

from tools.datasets import semver
from tools.datasets.models import (
    GitHubRateLimitResources,
    GitHubTag,
    GitHubTree,
    GitHubTreesResponse,
    GitHubUrl,
    ParsedRateLimit,
    ParsedTag,
    ParsedTree,
)

if TYPE_CHECKING:
    import sys
    from collections.abc import MutableMapping
    from email.message import Message
    from urllib.request import OpenerDirector, Request

    from tools.datasets._typing import Extension
    from tools.datasets.models import ReParsedTag
    from tools.schemapi.utils import OneOrSeq

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

    _PathName: TypeAlias = Literal["dir", "tags", "trees"]

__all__ = ["GitHub"]

_ItemSlice: TypeAlias = (
    "tuple[int | None, int | Literal['url_npm', 'url_github'] | None]"
)
"""Query result scalar selection."""

# TODO: Work on where these should live/be accessed
_NPM_BASE_URL = "https://cdn.jsdelivr.net/npm/vega-datasets@"
_SUB_DIR = "data"


def is_ext_supported(suffix: str) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}


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

    def __init__(self, gh: GitHub, /) -> None:
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

    def __init__(self, gh: GitHub, /) -> None:
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
            dataset_name=path.stem,
            suffix=path.suffix,
            size=tree["size"],
            url=tree["url"],
            ext_supported=is_ext_supported(path.suffix),
            tag=tag,
        )

    def trees(self, tree: GitHubTreesResponse, /, tag: str) -> list[ParsedTree]:
        """For a tree response (directory of files) convert to an IR with only relevant properties."""
        return [self.tree(t, tag) for t in tree["tree"]]

    def tag_from_str(self, s: str, /) -> str:
        # - Actual tag
        # - Trees url (using ref name)
        # - npm url (works w/o the `v` prefix)
        trees_url = self.url.TREES
        if s.startswith("v"):
            return s
        elif s.startswith(trees_url):
            return s.replace(trees_url, "")
        elif s.startswith(_NPM_BASE_URL):
            s, _ = s.replace(_NPM_BASE_URL, "").split("/")
            return s if s.startswith("v") else f"v{s}"
        else:
            raise TypeError(s)


class _GitHubQueryNamespace:
    """**WIP** Interfacing with the cached metadata."""

    def __init__(self, gh: GitHub, /) -> None:
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


class GitHub:
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
        tag_v = self.parse.tag_from_str(tag) if _is_str(tag) else tag["tag"]
        parsed = self.parse.trees(trees, tag=tag_v)
        df = (
            pl.DataFrame(parsed)
            .lazy()
            .rename({"url": "url_github"})
            .with_columns(name_collision=pl.col("dataset_name").is_duplicated())
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
            return pl.concat((trees, fresh_rows))

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
