"""API-related data structures."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Literal, NamedTuple

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if TYPE_CHECKING:
    import time

    if sys.version_info >= (3, 11):
        from typing import LiteralString, Required
    else:
        from typing_extensions import LiteralString, Required


class GitHubUrl(NamedTuple):
    BASE: LiteralString
    RATE: LiteralString
    REPO: LiteralString
    TAGS: LiteralString
    TREES: LiteralString


class NpmUrl(NamedTuple):
    CDN: LiteralString
    TAGS: LiteralString


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


class NpmVersion(TypedDict):
    version: str
    links: dict[Literal["self", "entrypoints", "stats"], str]


class NpmPackageMetadataResponse(TypedDict):
    """
    Response from `Get package metadata`_.

    Using:

        headers={"Accept": "application/json"}

    .. _Get package metadata:
        https://data.jsdelivr.com/v1/packages/npm/vega-datasets
    """

    type: str
    name: str
    tags: dict[Literal["canary", "next", "latest"], str]
    versions: list[NpmVersion]
    links: dict[Literal["stats"], str]


class ParsedTree(TypedDict):
    file_name: str
    dataset_name: str
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
