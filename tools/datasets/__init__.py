"""
Adapted from `altair-viz/vega_datasets`_.

.. _altair-viz/vega_datasets:
    https://github.com/altair-viz/vega_datasets
"""

from __future__ import annotations

import json
import types
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

import polars as pl

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

    _PathAlias: TypeAlias = Literal["npm_tags", "gh_tags", "gh_trees"]

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
        self._paths = types.MappingProxyType["_PathAlias", Path](
            {
                "npm_tags": self.npm._paths["tags"],
                "gh_tags": self.github._paths["tags"],
                "gh_trees": self.github._paths["trees"],
            }
        )
        self._fp_typing: Path = out_fp_typing

    @property
    def github(self) -> GitHub:
        return self._github

    @property
    def npm(self) -> Npm:
        return self._npm

    def refresh(self, *, include_typing: bool = False) -> pl.DataFrame:
        """
        Update and sync all dataset metadata files.

        Parameters
        ----------
        include_typing
            Regenerate ``altair.datasets._typing``.
        """
        print("Syncing datasets ...")
        npm_tags = self.npm.tags()
        self.write_parquet(npm_tags, self._paths["npm_tags"])

        gh_tags = self.github.refresh_tags(npm_tags)
        self.write_parquet(gh_tags, self._paths["gh_tags"])

        gh_trees = self.github.refresh_trees(gh_tags)
        self.write_parquet(gh_trees, self._paths["gh_trees"])

        if include_typing:
            self.generate_typing(self._fp_typing)
        return gh_trees

    def reset(self) -> None:
        """Remove all metadata files."""
        for fp in self._paths.values():
            fp.unlink(missing_ok=True)

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

    def generate_typing(self, output: Path, /) -> None:
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
        NAME = "DatasetName"
        TAG = "VersionTag"
        EXT = "Extension"
        METADATA_TD = "Metadata"
        DESCRIPTION_DEFAULT = "_description_"
        NOTE_SEP = f"\n\n{indent * 2}" f".. note::\n{indent * 3}"

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
            + f"\n\n{links}"
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
