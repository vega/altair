"""
Adapted from `altair-viz/vega_datasets`_.

.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import json
import types
from pathlib import Path
from typing import TYPE_CHECKING, Any, Generic, Literal, overload

import polars as pl
from narwhals.typing import IntoDataFrameT, IntoFrameT

from tools.codemod import ruff
from tools.datasets._io import get_backend
from tools.datasets.github import GitHub
from tools.datasets.npm import Npm
from tools.schemapi import utils

if TYPE_CHECKING:
    import sys
    from collections.abc import Mapping

    import pandas as pd

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from tools.datasets._io import _Backend, _Reader
    from tools.datasets._typing import DatasetName, Extension, VersionTag

    _PathAlias: TypeAlias = Literal["npm_tags", "gh_tags", "gh_trees"]

    WorkInProgress: TypeAlias = Any

__all__ = ["app", "data"]

HEADER_COMMENT = """\
# The contents of this file are automatically written by
# tools/datasets.__init__.py. Do not modify directly.
"""


class Application:
    """
    Top-level context.

    When ``write_schema``, addtional ``...-schema.json`` files are produced
    that describes the metadata columns.
    """

    def __init__(
        self,
        output_dir: Path,
        *,
        write_schema: bool,
        trees_gh: str = "metadata",
        tags_gh: str = "tags",
        tags_npm: str = "tags_npm",
        kwds_gh: Mapping[str, Any] | None = None,
        kwds_npm: Mapping[str, Any] | None = None,
    ) -> None:
        output_dir.mkdir(exist_ok=True)
        kwds_gh = kwds_gh or {}
        kwds_npm = kwds_npm or {}
        self._write_schema: bool = write_schema
        self._github: GitHub = GitHub(
            output_dir, name_tags=tags_gh, name_trees=trees_gh, **kwds_gh
        )
        self._npm: Npm = Npm(output_dir, name_tags=tags_npm, **kwds_npm)
        self._paths = types.MappingProxyType["_PathAlias", Path](
            {
                "npm_tags": self.npm._paths["tags"],
                "gh_tags": self.github._paths["tags"],
                "gh_trees": self.github._paths["trees"],
            }
        )

    @property
    def github(self) -> GitHub:
        return self._github

    @property
    def npm(self) -> Npm:
        return self._npm

    def refresh(self) -> pl.DataFrame:
        npm_tags = self.npm.tags()
        self.write_parquet(npm_tags, self._paths["npm_tags"])

        gh_tags = self.github.refresh_tags(npm_tags)
        self.write_parquet(gh_tags, self._paths["gh_tags"])

        gh_trees = self.github.refresh_trees(gh_tags)
        self.write_parquet(gh_trees, self._paths["gh_trees"])
        return gh_trees

    def read(self, name: _PathAlias, /) -> pl.DataFrame:
        """Read existing metadata from file."""
        return pl.read_parquet(self._from_alias(name))

    def scan(self, name: _PathAlias, /) -> pl.LazyFrame:
        """Scan existing metadata from file."""
        return pl.scan_parquet(self._from_alias(name))

    def _from_alias(self, name: _PathAlias, /) -> Path:
        if name not in {"npm_tags", "gh_tags", "gh_trees"}:
            msg = f'Expected one of {["npm_tags", "gh_tags", "gh_trees"]!r}, but got: {name!r}'
            raise TypeError(msg)
        else:
            return self._paths[name]

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


app = Application(Path(__file__).parent / "_metadata", write_schema=True)


# This is the tag in http://github.com/vega/vega-datasets from
# which the datasets in this repository are sourced.
_OLD_SOURCE_TAG = "v1.29.0"  # 5 years ago
_CURRENT_SOURCE_TAG = "v2.9.0"


def generate_datasets_typing(application: Application, output: Path, /) -> None:
    from tools.generate_schema_wrapper import UNIVERSAL_TYPED_DICT

    app = application
    tags = app.scan("gh_tags").select("tag").collect().to_series()
    metadata_schema = app.scan("gh_trees").collect_schema().to_python()

    DATASET_NAME = "dataset_name"
    names = (
        app.scan("gh_trees")
        .filter("ext_supported")
        .unique(DATASET_NAME)
        .select(DATASET_NAME)
        .sort(DATASET_NAME)
        .collect()
        .to_series()
    )
    indent = " " * 4
    NAME = "DatasetName"
    TAG = "VersionTag"
    EXT = "Extension"
    METADATA_TD = "Metadata"
    DESCRIPTION_DEFAULT = "_description_"
    NOTE_SEP = f"\n\n{indent * 2}" f".. note::\n{indent * 3}"

    name_collision = (
        f"Dataset is available via multiple ``suffix``(s).{NOTE_SEP}"
        "Requires specifying a preference in calls to ``data(ext=...)``."
    )
    sha = (
        f"Unique hash for the dataset.{NOTE_SEP}"
        f"If the dataset did *not* change between ``v1.0.0``-``v2.0.0``;\n\n{indent * 3}"
        f"then all ``tag``(s) in this range would **share** this value."
    )
    descriptions: dict[str, str] = {
        "dataset_name": "Equivalent to ``Pathlib.Path.stem``.",
        "ext_supported": "Dataset can be read as tabular data.",
        "file_name": "Equivalent to ``Pathlib.Path.name``.",
        "name_collision": name_collision,
        "sha": sha,
        "size": "File size (*bytes*).",
        "suffix": f"File extension.{NOTE_SEP}Equivalent to ``Pathlib.Path.suffix``",
        "tag": "``vega-datasets`` release version.",
        "url_npm": "Remote url used to access dataset.",
    }
    metadata_doc = f"\n{indent}".join(
        f"{param}\n{indent * 2}{descriptions.get(param, DESCRIPTION_DEFAULT)}"
        for param in metadata_schema
    )

    contents = (
        f"{HEADER_COMMENT}",
        "from __future__ import annotations\n",
        "import sys",
        "from typing import Literal, TYPE_CHECKING",
        utils.import_typing_extensions((3, 14), "TypedDict"),
        utils.import_typing_extensions((3, 10), "TypeAlias"),
        "\n",
        f"__all__ = {[NAME, TAG, EXT, METADATA_TD]}\n\n"
        f"{NAME}: TypeAlias = {utils.spell_literal(names)}",
        f"{TAG}: TypeAlias = {utils.spell_literal(tags)}",
        f'{EXT}: TypeAlias = {utils.spell_literal([".csv", ".json", ".tsv", ".arrow"])}',
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
    )
    ruff.write_lint_format(output, contents)


class DataLoader(Generic[IntoDataFrameT, IntoFrameT]):
    _reader: _Reader[IntoDataFrameT, IntoFrameT]

    def url(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
    ) -> str:
        """Return the address of a remote dataset."""
        return self._reader.url(name, ext, tag=tag)

    def __call__(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
        **kwds: Any,
    ) -> IntoDataFrameT:
        """Get a remote dataset and load as tabular data."""
        return self._reader.dataset(name, ext, tag=tag, **kwds)

    @overload
    @classmethod
    def with_backend(
        cls, backend: Literal["polars", "polars[pyarrow]"], /
    ) -> DataLoader[pl.DataFrame, pl.LazyFrame]: ...

    @overload
    @classmethod
    def with_backend(
        cls, backend: Literal["pandas", "pandas[pyarrow]"], /
    ) -> DataLoader[pd.DataFrame, pd.DataFrame]: ...

    @classmethod
    def with_backend(cls, backend: _Backend, /) -> DataLoader[Any, Any]:
        """
        Initialize a new loader, using the specified backend.

        Parameters
        ----------
        backend
            DataFrame package/config used to return data.

            * *polars*: _
            * *polars[pyarrow]*: Using ``use_pyarrow=True``
            * *pandas*: _
            * *pandas[pyarrow]*: Using ``dtype_backend="pyarrow"``
        """
        obj = DataLoader.__new__(DataLoader)
        obj._reader = get_backend(backend)
        return obj


data = DataLoader.with_backend("polars")
