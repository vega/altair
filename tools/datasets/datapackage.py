"""
``frictionless`` `datapackage`_ parsing.

.. _datapackage:
    https://datapackage.org/
"""

from __future__ import annotations

import textwrap
from collections import deque
from functools import cached_property
from typing import TYPE_CHECKING, Any, ClassVar, Literal

import polars as pl
from polars import col

from tools.schemapi import utils

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Mapping, Sequence
    from pathlib import Path

    from altair.datasets._typing import Dataset, FlFieldStr
    from tools.datasets.models import Package, Resource


__all__ = ["DataPackage"]

INDENT = " " * 4


class Column:
    def __init__(
        self, name: str, expr: pl.Expr, /, doc: str = "_description_", tp_str: str = ""
    ) -> None:
        self._name: str = name
        self._expr: pl.Expr = expr
        self._doc: str = doc
        self._tp_str: str = tp_str

    @property
    def expr(self) -> pl.Expr:
        return self._expr.alias(self._name)

    @property
    def doc(self) -> str:
        return f"{self._name}\n{INDENT * 2}{self._doc}"

    def is_feature(self) -> bool:
        return self._name.startswith("is_")


class DataPackage:
    NAME: ClassVar[Literal["dataset_name"]] = "dataset_name"
    """
    Main user-facing column name.

    - Does not include file extension
    - Preserves case of original file name
    """

    sort_by: str | Sequence[str] = "dataset_name", "bytes"
    """Key(s) used to ensure output is deterministic."""

    _NAME_TYPED_DICT: ClassVar[Literal["Metadata"]] = "Metadata"
    _columns: ClassVar[Sequence[Column]]
    _links: ClassVar[Sequence[str]]

    def __init__(self, pkg: Package, base_url: str, path: Path, /) -> None:
        self._pkg: Package = pkg
        self._base_url: str = base_url
        self._path: Path = path

    @classmethod
    def with_columns(cls, *columns: Column) -> type[DataPackage]:
        cls._columns = columns
        return cls

    @classmethod
    def with_links(cls, *links: str) -> type[DataPackage]:
        cls._links = links
        return cls

    @property
    def columns(self) -> Iterator[Column]:
        yield from self._columns
        yield self._url

    @cached_property
    def core(self) -> pl.LazyFrame:
        """A minimal, tabular view of ``datapackage.json``."""
        return pl.LazyFrame(self._resources).select(self._exprs).sort(self.sort_by)

    def schemas(self) -> Mapping[Dataset, Mapping[str, FlFieldStr]]:
        """Reduce all datasets with schemas to a minimal mapping."""
        m: Any = {
            rsrc["name"]: {f["name"]: f["type"] for f in s["fields"]}
            for rsrc in self._resources
            if (s := rsrc.get("schema"))
        }
        return m

    def dataset_names(self) -> Iterable[str]:
        return self.core.select(col(self.NAME).unique().sort()).collect().to_series()

    def extensions(self) -> tuple[str, ...]:
        return tuple(
            self.core.select(col("suffix").unique().sort())
            .collect()
            .to_series()
            .to_list()
        )

    # TODO: Collect, then raise if cannot guarantee uniqueness
    def metadata_csv(self) -> pl.LazyFrame:
        """Variant with duplicate dataset names removed."""
        return self.core.filter(col("suffix") != ".arrow").sort(self.NAME)

    def typed_dict(self) -> str:
        from tools.generate_schema_wrapper import UNIVERSAL_TYPED_DICT

        return UNIVERSAL_TYPED_DICT.format(
            name=self._NAME_TYPED_DICT,
            metaclass_kwds=", total=False",
            td_args=self._metadata_td_args,
            summary=f"Full schema for ``{self._path.name}``.",
            doc=self._metadata_doc,
            comment="",
        )

    @property
    def _exprs(self) -> Iterator[pl.Expr]:
        return (column.expr for column in self.columns)

    @property
    def _docs(self) -> Iterator[str]:
        return (column.doc for column in self.columns)

    @property
    def _resources(self) -> Sequence[Resource]:
        return self._pkg["resources"]

    @property
    def _metadata_doc(self) -> str:
        NLINDENT = f"\n{INDENT}"
        return (
            f"{NLINDENT.join(self._docs)}\n\n{''.join(self._links)}\n"
            f"{textwrap.indent(self._metadata_examples, INDENT)}"
            f"{INDENT}"
        )

    @property
    def _metadata_examples(self) -> str:
        with pl.Config(fmt_str_lengths=25, tbl_cols=5, tbl_width_chars=80):
            table = repr(self.core.collect())
        return (
            f"\nExamples"
            f"\n--------\n"
            f"``{self._NAME_TYPED_DICT}`` keywords form constraints to filter a table like the below sample:\n\n"
            f"```\n{table}\n```\n"
        )

    @property
    def _metadata_td_args(self) -> str:
        schema = self.core.collect_schema().to_python()
        return f"\n{INDENT}".join(
            f"{column._name}: {column._tp_str or tp.__name__}"
            for column, tp in zip(self.columns, schema.values())
        )

    @property
    def _url(self) -> Column:
        expr = pl.concat_str(pl.lit(self._base_url), "path")
        return Column("url", expr, "Remote url used to access dataset.")

    def features_typing(self, frame: pl.LazyFrame | pl.DataFrame, /) -> Iterator[str]:
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
        for column in self.columns:
            if not column.is_feature():
                continue
            guard_name = column._name
            alias_name = guard_name.removeprefix("is_").capitalize()
            members = ldf.filter(guard_name).select(self.NAME).collect().to_series()
            guards.append(guard_literal(alias_name, guard_name, members))
            yield utils.spell_literal_alias(alias_name, members)
        yield from guards


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


def guard_literal(alias_name: str, guard_name: str, members: Iterable[str], /) -> str:
    """Type narrowing function, all members must be literal strings."""
    return (
        f"def {guard_name}(obj: Any) -> TypeIs[{alias_name}]:\n"
        f"    return obj in set({sorted(set(members))!r})\n"
    )


PATHLIB = "https://docs.python.org/3/library/pathlib.html"
GEOJSON = "https://en.wikipedia.org/wiki/GeoJSON"


def link(name: str, url: str, /) -> str:
    return f"{INDENT}.. _{name}:\n{INDENT * 2}{url}\n"


def note(s: str, /) -> str:
    return f"\n\n{INDENT * 2}.. note::\n{INDENT * 3}{s}"


fmt = col("format")
DataPackage.with_columns(
    Column(
        "dataset_name",
        col("name"),
        "Name of the dataset from the resource name field.",
        tp_str="Dataset | LiteralString",
    ),
    Column(
        "suffix",
        path_suffix("path"),
        "File extension/`Path.suffix`_.",
        tp_str="Extension",
    ),
    Column("file_name", col("path"), "Equivalent to `Path.name`_."),
    Column("bytes", col("bytes"), "File size in *bytes*."),
    Column("is_image", fmt == "png", "Only accessible via url."),
    Column("is_tabular", col("type") == "table", "Can be read as tabular data."),
    Column("is_geo", fmt == "geojson", "`GeoJSON`_ format."),
    Column("is_topo", fmt == "topojson", "`TopoJSON`_ format."),
    Column(
        "is_spatial",
        fmt.is_in(("geojson", "topojson")),
        "Any geospatial format. Only natively supported by ``polars``.",
    ),
    Column(
        "is_json", fmt.str.contains("json"), "Not supported natively by ``pyarrow``."
    ),
    Column(
        "has_schema",
        col("schema").is_not_null(),
        "Data types available for improved ``pandas`` parsing.",
    ),
    Column(
        "sha",
        col("hash").str.split(":").list.last(),
        doc=(
            "Unique hash for the dataset."
            + note(
                f"E.g. if the dataset did *not* change between ``v1.0.0``-``v2.0.0``;\n\n{INDENT * 3}"
                f"then this value would remain stable."
            )
        ),
    ),
)
DataPackage.with_links(
    link("Path.stem", f"{PATHLIB}#pathlib.PurePath.stem"),
    link("Path.name", f"{PATHLIB}#pathlib.PurePath.name"),
    link("Path.suffix", f"{PATHLIB}#pathlib.PurePath.suffix"),
    link("GeoJSON", GEOJSON),
    link("TopoJSON", f"{GEOJSON}#TopoJSON"),
)
