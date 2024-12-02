"""API-related data structures."""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, Literal, NamedTuple

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if TYPE_CHECKING:
    import time

    if sys.version_info >= (3, 11):
        from typing import LiteralString, NotRequired, Required
    else:
        from typing_extensions import LiteralString, NotRequired, Required
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    import polars as pl

    from altair.datasets._typing import Dataset, FlFieldStr

Map: TypeAlias = Mapping[str, Any]


class GitHubUrl(NamedTuple):
    BASE: LiteralString
    BLOBS: LiteralString
    RATE: LiteralString
    REPO: LiteralString
    TAGS: LiteralString
    TREES: LiteralString


class NpmUrl(NamedTuple):
    CDN: LiteralString
    TAGS: LiteralString
    GH: LiteralString


class GitHubTag(TypedDict):
    """
    A single release's metadata within the response of `List repository tags`_.

    .. _List repository tags:
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-tags.
    """

    name: str
    node_id: str
    commit: dict[Literal["sha", "url"], str]
    zipball_url: str
    tarball_url: str


class ParsedTag(TypedDict):
    tag: str
    sha: str
    trees_url: str


class SemVerTag(ParsedTag):
    """
    Extends ``ParsedTag`` with `semantic versioning`_.

    These values are extracted via:

        tools.datasets.with_columns

    Describes a row in the dataframe returned by:

        tools.datasets.GitHub.tags

    .. _semantic versioning:
        https://semver.org/
    """

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
    sha: str
    ext_supported: bool
    tag: str


class GitHubRateLimit(TypedDict):
    """
    An individual item in `Get rate limit status for the authenticated user`_.

    All categories share this schema.

    .. _Get rate limit status for the authenticated user:
        https://docs.github.com/en/rest/rate-limit/rate-limit?apiVersion=2022-11-28#get-rate-limit-status-for-the-authenticated-user
    """

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


#####################################################
# frictionless datapackage
#####################################################


FlCsvDialect: TypeAlias = Mapping[
    Literal["csv"], Mapping[Literal["delimiter"], Literal["\t"]]
]
FlJsonDialect: TypeAlias = Mapping[
    Literal[r"json"], Mapping[Literal["keyed"], Literal[True]]
]


class FlField(TypedDict):
    """https://datapackage.org/standard/table-schema/#field."""

    name: str
    type: FlFieldStr


class FlSchema(TypedDict):
    """https://datapackage.org/standard/table-schema/#properties."""

    fields: Sequence[FlField]


class FlResource(TypedDict):
    """https://datapackage.org/standard/data-resource/#properties."""

    name: Dataset
    type: Literal["table", "file", r"json"]
    path: str
    format: Literal[
        "arrow", "csv", "geojson", r"json", "parquet", "png", "topojson", "tsv"
    ]
    mediatype: Literal[
        "application/parquet",
        "application/vnd.apache.arrow.file",
        "image/png",
        "text/csv",
        "text/tsv",
        r"text/json",
        "text/geojson",
        "text/topojson",
    ]
    schema: NotRequired[FlSchema]
    scheme: Literal["file"]
    dialect: NotRequired[FlCsvDialect | FlJsonDialect]
    encoding: NotRequired[Literal["utf-8"]]


class FlPackage(TypedDict):
    """
    A subset of the `Data Package`_ standard.

    .. _Data Package:
        https://datapackage.org/standard/data-package/#properties
    """

    name: Literal["vega-datasets"]
    version: str
    homepage: str
    description: str
    licenses: Sequence[Map]
    contributors: Sequence[Map]
    sources: Sequence[Map]
    created: str
    resources: Sequence[FlResource]


class ParsedPackage(TypedDict):
    """Minimal representations to write to disk."""

    features: pl.DataFrame
    schemas: Mapping[Dataset, Mapping[str, FlFieldStr]]
