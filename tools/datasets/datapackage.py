"""
``frictionless`` `datapackage`_ parsing.

.. _datapackage:
    https://datapackage.org/
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

import polars as pl
from polars import col
from polars import selectors as cs

from tools.datasets.models import ParsedPackage
from tools.schemapi import utils

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Mapping, Sequence

    from altair.datasets._typing import Dataset, FlFieldStr
    from tools.datasets.models import FlPackage


__all__ = ["parse_package"]


DATASET_NAME: Literal["dataset_name"] = "dataset_name"

# # NOTE: Flag columns
# Storing these instead of the full **56KB** `datapackage.json`
FEATURES: Sequence[pl.Expr] = (
    (col("format") == "png").alias("is_image"),
    (col("type") == "table").alias("is_tabular"),
    (col("format") == "geojson").alias("is_geo"),
    (col("format") == "topojson").alias("is_topo"),
    col("format").is_in(("geojson", "topojson")).alias("is_spatial"),
    (col("format").str.contains("json")).alias("is_json"),
)


def parse_package(pkg: FlPackage, base_url: str, /) -> ParsedPackage:
    return ParsedPackage(
        features=extract_features(pkg, base_url), schemas=extract_schemas(pkg)
    )


def extract_schemas(pkg: FlPackage, /) -> Mapping[Dataset, Mapping[str, FlFieldStr]]:
    """Reduce all datasets with schemas to a minimal mapping."""
    m: Any = {
        Path(rsrc["path"]).stem: {f["name"]: f["type"] for f in s["fields"]}
        for rsrc in pkg["resources"]
        if (s := rsrc.get("schema"))
    }
    return m


def extract_features(pkg: FlPackage, base_url: str, /) -> pl.DataFrame:
    EXCLUDE = (
        "name",
        "type",
        "format",
        "scheme",
        "mediatype",
        "encoding",
        "dialect",
        "schema",
        "sources",
        "licenses",
        "hash",
        "description",
        "path",
    )
    return (
        pl.LazyFrame(pkg["resources"])
        .with_columns(
            path_stem("path").alias(DATASET_NAME),
            cs.exclude("name"),
        )
        .select(
            DATASET_NAME,
            path_suffix("path").alias("suffix"),
            col("path").alias("file_name"),
            ~cs.by_name(DATASET_NAME, EXCLUDE),
            *FEATURES,
            col("schema").is_not_null().alias("has_schema"),
            col("hash").str.split(":").list.last().alias("sha"),
            pl.concat_str(pl.lit(base_url), "path").alias("url"),
        )
        .sort(DATASET_NAME, "bytes")
        .collect()
    )


def path_stem(column: str | pl.Expr, /) -> pl.Expr:
    """
    The final path component, minus its last suffix.

    Needed since `Resource.name`_ must be lowercase.

    .. _Resource.name:
        https://specs.frictionlessdata.io/data-resource/#name
    """
    path = col(column) if isinstance(column, str) else column
    rfind = (path.str.len_bytes() - 1) - path.str.reverse().str.find(r"\.")
    return path.str.head(rfind)


def path_suffix(column: str | pl.Expr, /) -> pl.Expr:
    """
    The final component's last suffix.

    This includes the leading period. For example: '.txt'.
    """
    path = col(column) if isinstance(column, str) else column
    return path.str.tail(path.str.reverse().str.find(r"\.") + 1)


def features_typing(frame: pl.LazyFrame | pl.DataFrame, /) -> Iterator[str]:
    """
    Current plan is to use type aliases in overloads.

    - ``Tabular`` can be treated interchangeably
    - ``Image`` can only work with ``url``
    - ``(Spatial|Geo|Topo)`` can be read with ``polars``
        - A future version may implement dedicated support https://github.com/vega/altair/pull/3631#discussion_r1845931955
    - ``Json`` should warn when using the ``pyarrow`` backend
    """
    guards = deque[str]()
    ldf = frame.lazy()
    for feat in FEATURES:
        guard_name = feat.meta.output_name()
        alias_name = guard_name.removeprefix("is_").capitalize()
        members = ldf.filter(guard_name).select(DATASET_NAME).collect().to_series()
        guards.append(guard_literal(alias_name, guard_name, members))
        yield f"{alias_name}: TypeAlias = {utils.spell_literal(members)}"
    yield from guards


def guard_literal(alias_name: str, guard_name: str, members: Iterable[str], /) -> str:
    """Type narrowing function, all members must be literal strings."""
    return (
        f"def {guard_name}(obj: Any) -> TypeIs[{alias_name}]:\n"
        f"    return obj in set({sorted(set(members))!r})\n"
    )
