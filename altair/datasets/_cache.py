from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar, get_args

import narwhals.stable.v1 as nw
from narwhals.stable.v1.dependencies import get_pyarrow
from narwhals.stable.v1.typing import IntoDataFrameT, IntoFrameT

from altair.datasets._typing import VERSION_LATEST

if TYPE_CHECKING:
    import sys
    from collections.abc import Iterator, MutableMapping
    from typing import Any, Final

    from _typeshed import StrPath

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from altair.datasets._readers import _Reader
    from altair.datasets._typing import Dataset

__all__ = ["DatasetCache", "UrlCache", "url_cache"]


_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

_URL: Final[Path] = Path(__file__).parent / "_metadata" / "url.csv.gz"


class UrlCache(Generic[_KT, _VT]):
    """
    `csv`_, `gzip`_ -based, lazy url lookup.

    Operates on a subset of available datasets:
    - Only the latest version
    - Excludes `.parquet`, which `cannot be read via url`_
    - Name collisions are pre-resolved
        - Only provide the smallest (e.g. ``weather.json`` instead of ``weather.csv``)

    .. _csv:
        https://docs.python.org/3/library/csv.html
    .. _gzip:
        https://docs.python.org/3/library/gzip.html
    .. _cannot be read via url:
        https://github.com/vega/vega/issues/3961
    """

    def __init__(
        self,
        fp: Path,
        /,
        *,
        columns: tuple[str, str] = ("dataset_name", "url_npm"),
        tp: type[MutableMapping[_KT, _VT]] = dict["_KT", "_VT"],
    ) -> None:
        self.fp: Path = fp
        self.columns: tuple[str, str] = columns
        self._mapping: MutableMapping[_KT, _VT] = tp()

    def read(self) -> Any:
        import csv
        import gzip

        with gzip.open(self.fp, mode="rb") as f:
            b_lines = f.readlines()
        reader = csv.reader((bs.decode() for bs in b_lines), dialect=csv.unix_dialect)
        header = tuple(next(reader))
        if header != self.columns:
            msg = f"Expected header to match {self.columns!r},\n" f"but got: {header!r}"
            raise ValueError(msg)
        return dict(reader)

    def __getitem__(self, key: _KT, /) -> _VT:
        if url := self.get(key, None):
            return url

        from altair.datasets._typing import Dataset

        if key in get_args(Dataset):
            msg = f"{key!r} cannot be loaded via url."
            raise TypeError(msg)
        else:
            msg = f"{key!r} does not refer to a known dataset."
            raise TypeError(msg)

    def get(self, key: _KT, default: _T) -> _VT | _T:
        if not self._mapping:
            self._mapping.update(self.read())
        return self._mapping.get(key, default)


class DatasetCache(Generic[IntoDataFrameT, IntoFrameT]):
    _ENV_VAR: ClassVar[LiteralString] = "ALTAIR_DATASETS_DIR"

    def __init__(self, reader: _Reader[IntoDataFrameT, IntoFrameT], /) -> None:
        self._rd: _Reader[IntoDataFrameT, IntoFrameT] = reader

    def clear(self) -> None:
        """Delete all previously cached datasets."""
        self._ensure_active()
        if self.is_empty():
            return None
        ser = (
            self._rd._scan_metadata()
            .select("sha", "suffix")
            .unique("sha")
            .select(nw.concat_str("sha", "suffix").alias("sha_suffix"))
            .collect()
            .get_column("sha_suffix")
        )
        names = set[str](
            ser.to_list() if nw.get_native_namespace(ser) is get_pyarrow() else ser
        )
        for fp in self:
            if fp.name in names:
                fp.unlink()

    def download_all(self) -> None:
        """
        Download any missing datasets for latest version.

        Requires **30-50MB** of disk-space.
        """
        stems = tuple(fp.stem for fp in self)
        latest = nw.col("tag") == nw.lit(VERSION_LATEST)
        predicates = (~(nw.col("sha").is_in(stems)), latest) if stems else (latest,)
        frame = (
            self._rd._scan_metadata(
                predicates, ext_supported=True, name_collision=False
            )
            .select("sha", "suffix", "url_npm")
            .unique("sha")
            .collect()
        )
        if frame.is_empty():
            print("Already downloaded all datasets")
            return None
        print(f"Downloading {len(frame)} missing datasets...")
        for row in frame.iter_rows(named=True):
            fp: Path = self.path / (row["sha"] + row["suffix"])
            with self._rd._opener.open(row["url_npm"]) as f:
                fp.touch()
                fp.write_bytes(f.read())
        print("Finished downloads")
        return None

    @property
    def path(self) -> Path:
        """
        Returns path to datasets cache.

        By default, this can be configured using the environment variable:

            "ALTAIR_DATASETS_DIR"

        You can set this for the current session via:

            >>> from pathlib import Path
            >>> from altair.datasets import load
            >>> load.cache.path = Path.home() / ".altair_cache"

            >>> load.cache.path.relative_to(Path.home()).as_posix()
            '.altair_cache'

        You can *later* disable caching via:

            >>> load.cache.path = None
        """
        self._ensure_active()
        fp = Path(os.environ[self._ENV_VAR])
        fp.mkdir(exist_ok=True)
        return fp

    @path.setter
    def path(self, source: StrPath | None, /) -> None:
        if source is not None:
            os.environ[self._ENV_VAR] = str(Path(source).resolve())
        else:
            os.environ.pop(self._ENV_VAR, None)

    def __iter__(self) -> Iterator[Path]:
        yield from self.path.iterdir()

    def __repr__(self) -> str:
        name = type(self).__name__
        if self.is_not_active():
            return f"{name}<UNSET>"
        else:
            return f"{name}<{self.path.as_posix()!r}>"

    def is_active(self) -> bool:
        return not self.is_not_active()

    def is_not_active(self) -> bool:
        return os.environ.get(self._ENV_VAR) is None

    def is_empty(self) -> bool:
        """Cache is active, but no files are stored in ``self.path``."""
        return next(iter(self), None) is None

    def _ensure_active(self) -> None:
        if self.is_not_active():
            msg = (
                f"Cache is unset.\n"
                f"To enable dataset caching, set the environment variable:\n"
                f"    {self._ENV_VAR!r}\n\n"
                f"You can set this for the current session via:\n"
                f"    from pathlib import Path\n"
                f"    from altair.datasets import load\n\n"
                f"    load.cache.path = Path.home() / '.altair_cache'"
            )
            raise ValueError(msg)


url_cache: UrlCache[Dataset | LiteralString, str] = UrlCache(_URL)
