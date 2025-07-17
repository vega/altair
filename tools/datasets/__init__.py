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
from typing import TYPE_CHECKING, Any, ClassVar, Literal

from tools import fs
from tools.codemod import ruff
from tools.datasets.npm import Npm
from tools.datasets.stub_generator import generate_stub_file
from tools.schemapi import utils

if TYPE_CHECKING:
    import sys
    from collections.abc import Mapping

    import polars as pl

    from tools.datasets import datapackage

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    _PathAlias: TypeAlias = Literal[
        "typing", "metadata-csv", "metadata", "schemas", "stub"
    ]
    PathMap: TypeAlias = Mapping[_PathAlias, Path]

__all__ = ["app"]

HEADER_COMMENT = """\
# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.
"""


class Application:
    """Top-level context."""

    OUT_DIR: ClassVar[Path] = fs.REPO_ROOT / "altair" / "datasets"

    def __init__(self) -> None:
        METADATA = "metadata"
        out_meta = self.OUT_DIR / "_metadata"
        self.paths = types.MappingProxyType["_PathAlias", Path](
            {
                "typing": self.OUT_DIR / "_typing.py",
                "metadata-csv": out_meta / f"{METADATA}.csv.gz",
                "metadata": out_meta / f"{METADATA}.parquet",
                "schemas": out_meta / "schemas.json.gz",
                "stub": self.OUT_DIR / "__init__.pyi",
            }
        )
        self._npm: Npm = Npm(self.paths)

    @property
    def npm(self) -> Npm:
        return self._npm

    def refresh(self, tag: Any, /, *, include_typing: bool = False) -> pl.DataFrame:
        """
        Update and sync all dataset metadata files.

        Parameters
        ----------
        tag
            Branch or release version to build against.
        include_typing
            Regenerate ``altair.datasets._typing``.
        """
        print("Syncing datasets ...")
        dpkg = self.npm.datapackage(tag=tag)
        self.write_parquet(dpkg.core, self.paths["metadata"])
        self.write_json_gzip(dpkg.schemas(), self.paths["schemas"])
        self.write_csv_gzip(dpkg.metadata_csv(), self.paths["metadata-csv"])
        print("Finished updating datasets.")

        if include_typing:
            self.generate_typing(dpkg)
            # Generate stub file after typing is updated
            generate_stub_file(dpkg)
        return dpkg.core.collect()

    def reset(self) -> None:
        """Remove all metadata files."""
        fs.rm(*self.paths.values())

    def read(self, name: _PathAlias, /) -> pl.DataFrame:
        """Read existing metadata from file."""
        return self.scan(name).collect()

    def scan(self, name: _PathAlias, /) -> pl.LazyFrame:
        """Scan existing metadata from file."""
        import polars as pl

        fp = self.paths[name]
        if fp.suffix == ".parquet":
            return pl.scan_parquet(fp)
        elif ".csv" in fp.suffixes:
            return pl.scan_csv(fp)
        elif ".json" in fp.suffixes:
            return pl.read_json(fp).lazy()
        else:
            msg = (
                f"Unable to read {fp.name!r} as tabular data.\nSuffixes: {fp.suffixes}"
            )
            raise NotImplementedError(msg)

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
        fp.touch()
        with gzip.GzipFile(fp, mode="wb", mtime=0) as f:
            f.write(json.dumps(obj).encode())

    def write_parquet(self, frame: pl.DataFrame | pl.LazyFrame, fp: Path, /) -> None:
        """Write ``frame`` to ``fp``, with some extra safety."""
        fp.touch()
        df = frame.lazy().collect()
        df.write_parquet(fp, compression="zstd", compression_level=17)

    def generate_typing(self, dpkg: datapackage.DataPackage) -> None:
        indent = " " * 4
        NAME = "Dataset"
        EXT = "Extension"
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
            "from typing import Literal, TYPE_CHECKING",
            utils.import_typing_extensions((3, 14), "TypedDict"),
            utils.import_typing_extensions((3, 11), "LiteralString"),
            utils.import_typing_extensions((3, 10), "TypeAlias"),
            "\n",
            f"__all__ = {[NAME, EXT, dpkg._NAME_TYPED_DICT]}\n",
            utils.spell_literal_alias(NAME, dpkg.dataset_names()),
            utils.spell_literal_alias(EXT, dpkg.extensions()),
            dpkg.typed_dict(),
            utils.spell_literal_alias(FIELD, FIELD_TYPES),
            '"""\n'
            "String representation of `frictionless`_ `Field Types`_.\n\n"
            f".. _frictionless:\n{indent}https://github.com/frictionlessdata/frictionless-py\n"
            f".. _Field Types:\n{indent}https://datapackage.org/standard/table-schema/#field-types\n"
            '"""\n',
        )
        ruff.write_lint_format(self.paths["typing"], contents)


app = Application()
