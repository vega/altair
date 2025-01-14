"""API-related data structures."""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Literal

if sys.version_info >= (3, 14):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import NotRequired, Required
    else:
        from typing_extensions import NotRequired, Required
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    import polars as pl

    from altair.datasets._typing import Dataset, FlFieldStr


CsvDialect: TypeAlias = Mapping[
    Literal["csv"], Mapping[Literal["delimiter"], Literal["\t"]]
]
JsonDialect: TypeAlias = Mapping[
    Literal[r"json"], Mapping[Literal["keyed"], Literal[True]]
]


class Field(TypedDict):
    """https://datapackage.org/standard/table-schema/#field."""

    name: str
    type: FlFieldStr
    description: NotRequired[str]


class Schema(TypedDict):
    """https://datapackage.org/standard/table-schema/#properties."""

    fields: Sequence[Field]


class Source(TypedDict, total=False):
    title: str
    path: Required[str]
    email: str
    version: str


class License(TypedDict):
    name: str
    path: str
    title: NotRequired[str]


class Resource(TypedDict):
    """https://datapackage.org/standard/data-resource/#properties."""

    name: Dataset
    type: Literal["table", "file", r"json"]
    description: NotRequired[str]
    licenses: NotRequired[Sequence[License]]
    sources: NotRequired[Sequence[Source]]
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
    dialect: NotRequired[CsvDialect | JsonDialect]
    schema: NotRequired[Schema]


class Contributor(TypedDict, total=False):
    title: str
    givenName: str
    familyName: str
    path: str
    email: str
    roles: Sequence[str]
    organization: str


class Package(TypedDict):
    """
    A subset of the `Data Package`_ standard.

    .. _Data Package:
        https://datapackage.org/standard/data-package/#properties
    """

    name: Literal["vega-datasets"]
    version: str
    homepage: str
    description: str
    licenses: Sequence[License]
    contributors: Sequence[Contributor]
    sources: Sequence[Source]
    created: str
    resources: Sequence[Resource]


class ParsedPackage(TypedDict):
    """Minimal representations to write to disk."""

    features: pl.DataFrame
    schemas: Mapping[Dataset, Mapping[str, FlFieldStr]]
