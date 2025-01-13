"""
Metadata generation from `vega/vega-datasets`_.

Inspired by `altair-viz/vega_datasets`_.

The core interface of this package is provided by::

    tools.datasets.app

.. _vega/vega-datasets:
    https://github.com/vega/vega-datasets
.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import gzip
import json
import types
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

import polars as pl
from polars import col

from tools.codemod import ruff
from tools.datasets.github import GitHub
from tools.datasets.npm import Npm
from tools.schemapi import utils

if TYPE_CHECKING:
    import sys
    from collections.abc import Mapping

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    _PathAlias: TypeAlias = Literal[
        "npm_tags",
        "gh_tags",
        "gh_trees",
        "typing",
        "url",
        "dpkg_features",
        "dpkg_schemas",
    ]

__all__ = ["app"]

HEADER_COMMENT = """\
# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.
"""


class Application:
    """
    Top-level context.

    Parameters
    ----------
    out_dir_tools, out_dir_altair
        Directories to store ``.parquet`` metadata files.
    out_fp_typing
        Path to write metadata-derived typing module.
    write_schema
        Produce addtional ``...-schema.json`` files that describe table columns.
    trees_gh
        ``GitHub.trees`` metadata file name.
    tags_gh
        ``GitHub.tags`` metadata file name.
    tags_npm
        ``Npm.tags`` metadata file name.
    kwds_gh, kwds_npm
        Arguments passed to corresponding constructor.

    See Also
    --------
    - tools.datasets.github.GitHub
    - tools.datasets.npm.Npm
    """

    def __init__(
        self,
        out_dir_tools: Path,
        out_dir_altair: Path,
        out_fp_typing: Path,
        *,
        write_schema: bool,
        trees_gh: str = "metadata",
        tags_gh: str = "tags",
        tags_npm: str = "tags_npm",
        kwds_gh: Mapping[str, Any] | None = None,
        kwds_npm: Mapping[str, Any] | None = None,
    ) -> None:
        out_dir_tools.mkdir(exist_ok=True)
        kwds_gh = kwds_gh or {}
        kwds_npm = kwds_npm or {}
        self._write_schema: bool = write_schema
        self._npm: Npm = Npm(out_dir_tools, name_tags=tags_npm, **kwds_npm)
        self._github: GitHub = GitHub(
            out_dir_tools,
            out_dir_altair,
            name_tags=tags_gh,
            name_trees=trees_gh,
            npm_cdn_url=self._npm.url.CDN,
            **kwds_gh,
        )
        self.paths = types.MappingProxyType["_PathAlias", Path](
            {
                "npm_tags": self.npm._paths["tags"],
                "gh_tags": self.github._paths["tags"],
                "gh_trees": self.github._paths["trees"],
                "typing": out_fp_typing,
                "url": out_dir_altair / "url.csv.gz",
                "dpkg_features": out_dir_altair / "datapackage_features.parquet",
                "dpkg_schemas": out_dir_altair / "datapackage_schemas.json.gz",
            }
        )

    @property
    def github(self) -> GitHub:
        return self._github

    @property
    def npm(self) -> Npm:
        return self._npm

    def refresh(
        self, *, include_typing: bool = False, frozen: bool = False
    ) -> pl.DataFrame:
        """
        Update and sync all dataset metadata files.

        Parameters
        ----------
        include_typing
            Regenerate ``altair.datasets._typing``.
        frozen
            Don't perform any requests or attempt to check for new versions.

            .. note::
                **Temporary** measure to work from ``main`` until `vega-datasets@3`_.

        .. _vega-datasets@3:
            https://github.com/vega/vega-datasets/issues/654
        """
        if not frozen:
            print("Syncing datasets ...")
            npm_tags = self.npm.tags()
            self.write_parquet(npm_tags, self.paths["npm_tags"])

            gh_tags = self.github.refresh_tags(npm_tags)
            self.write_parquet(gh_tags, self.paths["gh_tags"])

            gh_trees = self.github.refresh_trees(gh_tags)
            self.write_parquet(gh_trees, self.paths["gh_trees"])

            npm_urls_min = (
                gh_trees.lazy()
                .filter(col("tag") == col("tag").first(), col("suffix") != ".parquet")
                .filter(col("size") == col("size").min().over("dataset_name"))
                .select("dataset_name", "url_npm")
            )
            self.write_csv_gzip(npm_urls_min, self.paths["url"])
        else:
            print("Reusing frozen metadata ...")
            gh_trees = pl.read_parquet(self.paths["gh_trees"])

        package = self.npm.datapackage(frozen=frozen)
        self.write_parquet(package["features"], self.paths["dpkg_features"])
        self.write_json_gzip(package["schemas"], self.paths["dpkg_schemas"])

        if include_typing:
            self.generate_typing()
        return gh_trees

    def reset(self) -> None:
        """Remove all metadata files."""
        for fp in self.paths.values():
            fp.unlink(missing_ok=True)

    def read(self, name: _PathAlias, /) -> pl.DataFrame:
        """Read existing metadata from file."""
        return pl.read_parquet(self.paths[name])

    def scan(self, name: _PathAlias, /) -> pl.LazyFrame:
        """Scan existing metadata from file."""
        return pl.scan_parquet(self.paths[name])

    def write_csv_gzip(self, frame: pl.DataFrame | pl.LazyFrame, fp: Path, /) -> None:
        """
        Write ``frame`` as a `gzip`_ compressed `csv`_ file.

        - *Much smaller* than a regular ``.csv``.
        - Still readable using ``stdlib`` modules.

        .. _gzip:
            https://docs.python.org/3/library/gzip.html
        .. _csv:
            https://docs.python.org/3/library/csv.html
        """
        if fp.suffix != ".gz":
            fp = fp.with_suffix(".csv.gz")
        if not fp.exists():
            fp.touch()
        df = frame.lazy().collect()
        buf = BytesIO()
        with gzip.GzipFile(fp, mode="wb", mtime=0) as f:
            df.write_csv(buf)
            f.write(buf.getbuffer())

    def write_json_gzip(self, obj: Any, fp: Path, /) -> None:
        """
        Write ``obj`` as a `gzip`_ compressed ``json`` file.

        .. _gzip:
            https://docs.python.org/3/library/gzip.html
        """
        if fp.suffix != ".gz":
            fp = fp.with_suffix(".json.gz")
        if not fp.exists():
            fp.touch()

        with gzip.GzipFile(fp, mode="wb", mtime=0) as f:
            f.write(json.dumps(obj).encode())

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

    def generate_typing(self) -> None:
        from tools.generate_schema_wrapper import UNIVERSAL_TYPED_DICT

        tags = self.scan("gh_tags").select("tag").collect().to_series()
        metadata_schema = self.scan("gh_trees").collect_schema().to_python()

        DATASET_NAME = "dataset_name"
        names = (
            self.scan("gh_trees")
            .filter("ext_supported")
            .unique(DATASET_NAME)
            .select(DATASET_NAME)
            .sort(DATASET_NAME)
            .collect()
            .to_series()
        )
        indent = " " * 4
        NAME = "Dataset"
        TAG = "Version"
        LATEST = "VERSION_LATEST"
        LATEST_TAG = f"{tags.first()!r}"
        EXT = "Extension"
        EXTENSION_TYPES = ".csv", ".json", ".tsv", ".arrow", ".parquet"
        EXTENSION_SUFFIXES = "EXTENSION_SUFFIXES"
        EXTENSION_TYPE_TP = (
            f"tuple[{', '.join(f'Literal[{el!r}]' for el in EXTENSION_TYPES)}]"
        )
        EXTENSION_GUARD = "is_ext_read"
        METADATA_TD = "Metadata"
        DESCRIPTION_DEFAULT = "_description_"
        NOTE_SEP = f"\n\n{indent * 2}.. note::\n{indent * 3}"

        name_collision = (
            f"Dataset is available via multiple formats.{NOTE_SEP}"
            "Requires specifying a preference in calls to ``data(name, suffix=...)``"
        )
        sha = (
            f"Unique hash for the dataset.{NOTE_SEP}"
            f"If the dataset did *not* change between ``v1.0.0``-``v2.0.0``;\n\n{indent * 3}"
            f"then all ``tag``(s) in this range would **share** this value."
        )
        links = (
            f".. _Path.stem:\n{indent * 2}https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem\n"
            f".. _Path.name:\n{indent * 2}https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name\n"
            f".. _Path.suffix:\n{indent * 2}https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix\n"
            f".. _vega-datasets release:\n{indent * 2}https://github.com/vega/vega-datasets/releases"
        )
        import textwrap

        examples = f"""\
        Examples
        --------
        ``{METADATA_TD}`` keywords form constraints to filter a table like the below sample:

        ```
        shape: (2_879, 9)
        ┌───────────┬──────────┬──────────┬──────────┬───┬────────┬─────────┬──────────┐
        │ dataset_n ┆ ext_supp ┆ file_nam ┆ name_col ┆ … ┆ suffix ┆ tag     ┆ url_npm  │
        │ a…        ┆ or…      ┆ e        ┆ li…      ┆   ┆ ---    ┆ ---     ┆ ---      │
        │ ---       ┆ ---      ┆ ---      ┆ ---      ┆   ┆ str    ┆ enum    ┆ str      │
        │ str       ┆ bool     ┆ str      ┆ bool     ┆   ┆        ┆         ┆          │
        ╞═══════════╪══════════╪══════════╪══════════╪═══╪════════╪═════════╪══════════╡
        │ cars      ┆ true     ┆ cars.jso ┆ false    ┆ … ┆ .json  ┆ v1.21.0 ┆ https:// │
        │           ┆          ┆ n        ┆          ┆   ┆        ┆         ┆ cd…      │
        │ flights-2 ┆ true     ┆ flights- ┆ true     ┆ … ┆ .arrow ┆ v1.31.1 ┆ https:// │
        │ 0…        ┆          ┆ 20…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ flights-2 ┆ true     ┆ flights- ┆ false    ┆ … ┆ .json  ┆ v2.9.0  ┆ https:// │
        │ 0…        ┆          ┆ 20…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ unemploym ┆ true     ┆ unemploy ┆ false    ┆ … ┆ .json  ┆ v2.7.0  ┆ https:// │
        │ e…        ┆          ┆ me…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ ffox      ┆ false    ┆ ffox.png ┆ false    ┆ … ┆ .png   ┆ v2.5.2  ┆ https:// │
        │           ┆          ┆          ┆          ┆   ┆        ┆         ┆ cd…      │
        │ …         ┆ …        ┆ …        ┆ …        ┆ … ┆ …      ┆ …       ┆ …        │
        │ flights-a ┆ true     ┆ flights- ┆ false    ┆ … ┆ .csv   ┆ v1.18.0 ┆ https:// │
        │ i…        ┆          ┆ ai…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ income    ┆ true     ┆ income.j ┆ false    ┆ … ┆ .json  ┆ v1.21.0 ┆ https:// │
        │           ┆          ┆ so…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ burtin    ┆ true     ┆ burtin.j ┆ false    ┆ … ┆ .json  ┆ v2.8.0  ┆ https:// │
        │           ┆          ┆ so…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ flights-5 ┆ true     ┆ flights- ┆ false    ┆ … ┆ .json  ┆ v1.8.0  ┆ https:// │
        │ k         ┆          ┆ 5k…      ┆          ┆   ┆        ┆         ┆ cd…      │
        │ wheat     ┆ true     ┆ wheat.js ┆ false    ┆ … ┆ .json  ┆ v1.18.0 ┆ https:// │
        │           ┆          ┆ on       ┆          ┆   ┆        ┆         ┆ cd…      │
        └───────────┴──────────┴──────────┴──────────┴───┴────────┴─────────┴──────────┘
        ```
        """

        descriptions: dict[str, str] = {
            "dataset_name": "Name of the dataset/`Path.stem`_.",
            "ext_supported": "Dataset can be read as tabular data.",
            "file_name": "Equivalent to `Path.name`_.",
            "name_collision": name_collision,
            "sha": sha,
            "size": "File size (*bytes*).",
            "suffix": "File extension/`Path.suffix`_.",
            "tag": "Version identifier for a `vega-datasets release`_.",
            "url_npm": "Remote url used to access dataset.",
        }
        metadata_doc = (
            f"\n{indent}".join(
                f"{param}\n{indent * 2}{descriptions.get(param, DESCRIPTION_DEFAULT)}"
                for param in metadata_schema
            )
            + f"\n\n{links}\n\n"
            f"{textwrap.indent(textwrap.dedent(examples), indent)}"
        )

        FIELD = "FlFieldStr"
        FIELD_TYPES = (
            "integer",
            "number",
            "boolean",
            "string",
            "object",
            "array",
            "date",
            "datetime",
            "time",
            "duration",
        )

        contents = (
            f"{HEADER_COMMENT}",
            "from __future__ import annotations\n",
            "import sys",
            "from typing import Any, Literal, TYPE_CHECKING",
            utils.import_typing_extensions((3, 14), "TypedDict"),
            utils.import_typing_extensions((3, 13), "TypeIs"),
            utils.import_typing_extensions((3, 10), "TypeAlias"),
            "\n",
            f"__all__ = {[NAME, TAG, EXT, METADATA_TD, EXTENSION_GUARD, EXTENSION_SUFFIXES, LATEST]}\n\n"
            f"{NAME}: TypeAlias = {utils.spell_literal(names)}",
            f"{TAG}: TypeAlias = {utils.spell_literal(tags)}",
            f"{EXT}: TypeAlias = {utils.spell_literal(EXTENSION_TYPES)}",
            f"{LATEST}: Literal[{LATEST_TAG}] = {LATEST_TAG}",
            f"{EXTENSION_SUFFIXES}: {EXTENSION_TYPE_TP} = {EXTENSION_TYPES!r}",
            f"def {EXTENSION_GUARD}(suffix: Any) -> TypeIs[{EXT}]:\n"
            f"{indent}return suffix in set({EXTENSION_TYPES!r})\n",
            UNIVERSAL_TYPED_DICT.format(
                name=METADATA_TD,
                metaclass_kwds=", total=False",
                td_args=f"\n{indent}".join(
                    f"{param}: {tp.__name__}" for param, tp in metadata_schema.items()
                ),
                summary="Full schema for ``metadata.parquet``.",
                doc=metadata_doc,
                comment="",
            ),
            f"{FIELD}: TypeAlias = {utils.spell_literal(FIELD_TYPES)}\n"
            '"""\n'
            "String representation of `frictionless`_ `Field Types`_.\n\n"
            f".. _frictionless:\n{indent}https://github.com/frictionlessdata/frictionless-py\n"
            f".. _Field Types:\n{indent}https://datapackage.org/standard/table-schema/#field-types\n"
            '"""\n',
        )
        ruff.write_lint_format(self.paths["typing"], contents)


_alt_datasets = Path(__file__).parent.parent.parent / "altair" / "datasets"
app = Application(
    Path(__file__).parent / "_metadata",
    _alt_datasets / "_metadata",
    _alt_datasets / "_typing.py",
    write_schema=False,
)


# This is the tag in http://github.com/vega/vega-datasets from
# which the datasets in this repository are sourced.
_OLD_SOURCE_TAG = "v1.29.0"  # 5 years ago
_CURRENT_SOURCE_TAG = "v2.9.0"
