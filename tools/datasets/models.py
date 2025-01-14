"""API-related data structures."""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Literal, NamedTuple

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if TYPE_CHECKING:
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


class NpmUrl(NamedTuple):
    CDN: LiteralString
    GH: LiteralString


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
    description: NotRequired[str]


class FlSchema(TypedDict):
    """https://datapackage.org/standard/table-schema/#properties."""

    fields: Sequence[FlField]


class FlSource(TypedDict, total=False):
    title: str
    path: Required[str]
    email: str
    version: str


class FlLicense(TypedDict):
    name: str
    path: str
    title: NotRequired[str]


class FlResource(TypedDict):
    """https://datapackage.org/standard/data-resource/#properties."""

    name: Dataset
    type: Literal["table", "file", r"json"]
    description: NotRequired[str]
    licenses: NotRequired[Sequence[FlLicense]]
    sources: NotRequired[Sequence[FlSource]]
    path: str
    scheme: Literal["file"]
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
    encoding: NotRequired[Literal["utf-8"]]
    hash: str
    bytes: int
    dialect: NotRequired[FlCsvDialect | FlJsonDialect]
    schema: NotRequired[FlSchema]


class Contributor(TypedDict, total=False):
    title: str
    givenName: str
    familyName: str
    path: str
    email: str
    roles: Sequence[str]
    organization: str


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
    licenses: Sequence[FlLicense]
    contributors: Sequence[Contributor]
    sources: Sequence[FlSource]
    created: str
    resources: Sequence[FlResource]


class ParsedPackage(TypedDict):
    """Minimal representations to write to disk."""

    features: pl.DataFrame
    schemas: Mapping[Dataset, Mapping[str, FlFieldStr]]
