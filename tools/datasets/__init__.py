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
        "typing",
        "url",
        "metadata",
        "schemas",
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
    kwds_npm
        Arguments passed to corresponding constructor.

    See Also
    --------
    - tools.datasets.npm.Npm
    """

    def __init__(
        self,
        out_dir_tools: Path,
        out_dir_altair: Path,
        out_fp_typing: Path,
        *,
        kwds_npm: Mapping[str, Any] | None = None,
    ) -> None:
        out_dir_tools.mkdir(exist_ok=True)
        kwds_npm = kwds_npm or {}
        self._npm: Npm = Npm(out_dir_tools, **kwds_npm)
        self.paths = types.MappingProxyType["_PathAlias", Path](
            {
                "typing": out_fp_typing,
                "url": out_dir_altair / "url.csv.gz",
                "metadata": out_dir_altair / "metadata.parquet",
                "schemas": out_dir_altair / "schemas.json.gz",
            }
        )

    @property
    def npm(self) -> Npm:
        return self._npm

    def refresh(
        self, tag: Any, /, *, include_typing: bool = False, frozen: bool = False
    ) -> pl.DataFrame:
        """
        Update and sync all dataset metadata files.

        Parameters
        ----------
        tag
            Branch or release version to build against.
        include_typing
            Regenerate ``altair.datasets._typing``.
        frozen
            Don't perform any requests or attempt to check for new versions.

            .. note::
                **Temporary** measure to work from ``main`` until `vega-datasets@3`_.

        .. _vega-datasets@3:
            https://github.com/vega/vega-datasets/issues/654
        """
        print("Syncing datasets ...")
        package = self.npm.datapackage(tag=tag, frozen=frozen)
        self.write_parquet(package["features"], self.paths["metadata"])
        self.write_json_gzip(package["schemas"], self.paths["schemas"])
        # FIXME: 2-Part replacement
        # - [x] Switch source to `"metadata"` + refresh (easy)
        # - [ ] Rewriting `UrlCache` to operate on result rows (difficult)
        urls_min = (
            package["features"]
            .lazy()
            .filter(~(col("suffix").is_in((".parquet", ".arrow"))))
            .select("dataset_name", "url")
            .sort("dataset_name")
            .collect()
        )
        self.write_csv_gzip(urls_min, self.paths["url"])

        if include_typing:
            self.generate_typing()
        return package["features"]

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

    def generate_typing(self) -> None:
        from tools.generate_schema_wrapper import UNIVERSAL_TYPED_DICT

        dpkg = self.scan("metadata")
        metadata_schema = dpkg.collect_schema().to_python()

        DATASET_NAME = "dataset_name"
        names = (
            dpkg.unique(DATASET_NAME)
            .select(DATASET_NAME)
            .sort(DATASET_NAME)
            .collect()
            .to_series()
        )
        indent = " " * 4
        NAME = "Dataset"
        EXT = "Extension"
        EXT_TYPES = tuple(
            dpkg.filter(is_image=False)
            .select(col("suffix").unique().sort())
            .collect()
            .to_series()
            .to_list()
        )
        EXTENSION_SUFFIXES = "EXTENSION_SUFFIXES"
        EXTENSION_TYPE_TP = (
            f"tuple[{', '.join(f'Literal[{el!r}]' for el in EXT_TYPES)}]"
        )
        EXTENSION_GUARD = "is_ext_read"
        METADATA_TD = "Metadata"
        DESCRIPTION_DEFAULT = "_description_"
        NOTE_SEP = f"\n\n{indent * 2}.. note::\n{indent * 3}"

        sha = (
            f"Unique hash for the dataset.{NOTE_SEP}"
            f"E.g. if the dataset did *not* change between ``v1.0.0``-``v2.0.0``;\n\n{indent * 3}"
            f"then this value would remain stable."
        )
        links = (
            f".. _Path.stem:\n{indent * 2}https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem\n"
            f".. _Path.name:\n{indent * 2}https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name\n"
            f".. _Path.suffix:\n{indent * 2}https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix\n"
        )
        import textwrap

        examples = f"""\
        Examples
        --------
        ``{METADATA_TD}`` keywords form constraints to filter a table like the below sample:

        ### FIXME: NEEDS UPDATING TO DATAPACKAGE VERSION

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
            "suffix": "File extension/`Path.suffix`_.",
            "file_name": "Equivalent to `Path.name`_.",
            "bytes": "File size in *bytes*.",
            "is_tabular": "Can be read as tabular data.",
            "has_schema": "Data types available for improved ``pandas`` parsing.",
            "sha": sha,
            "url": "Remote url used to access dataset.",
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
            f"__all__ = {[NAME, EXT, METADATA_TD, EXTENSION_GUARD, EXTENSION_SUFFIXES]}\n\n"
            f"{NAME}: TypeAlias = {utils.spell_literal(names)}",
            f"{EXT}: TypeAlias = {utils.spell_literal(EXT_TYPES)}",
            f"{EXTENSION_SUFFIXES}: {EXTENSION_TYPE_TP} = {EXT_TYPES!r}",
            f"def {EXTENSION_GUARD}(suffix: Any) -> TypeIs[{EXT}]:\n"
            f"{indent}return suffix in set({EXT_TYPES!r})\n",
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
)


# This is the tag in http://github.com/vega/vega-datasets from
# which the datasets in this repository are sourced.
_OLD_SOURCE_TAG = "v1.29.0"  # 5 years ago
_CURRENT_SOURCE_TAG = "v2.9.0"
