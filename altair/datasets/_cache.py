from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar, get_args

import narwhals.stable.v1 as nw
from narwhals.stable.v1.typing import IntoDataFrameT, IntoFrameT

if sys.version_info >= (3, 12):
    from typing import Protocol
else:
    from typing_extensions import Protocol

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping, MutableMapping
    from io import IOBase
    from typing import Any, Final

    from _typeshed import StrPath
    from narwhals.stable.v1.dtypes import DType

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from altair.datasets._readers import _Reader
    from altair.datasets._typing import Dataset, FlFieldStr

    _Dataset: TypeAlias = "Dataset | LiteralString"  # noqa: TC008
    _FlSchema: TypeAlias = Mapping[str, FlFieldStr]

__all__ = ["DatasetCache", "UrlCache", "url_cache"]


_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

_URL: Final[Path] = Path(__file__).parent / "_metadata" / "url.csv.gz"
_SCHEMA: Final[Path] = Path(__file__).parent / "_metadata" / "schemas.json.gz"

_FIELD_TO_DTYPE: Mapping[FlFieldStr, type[DType]] = {
    "integer": nw.Int64,
    "number": nw.Float64,
    "boolean": nw.Boolean,
    "string": nw.String,
    "object": nw.Struct,
    "array": nw.List,
    "date": nw.Date,
    "datetime": nw.Datetime,
    # "time": nw.Time, (Not Implemented, but we don't have any cases using it anyway)
    "duration": nw.Duration,
}
"""
Similar to an inverted `pl.datatypes.convert.dtype_to_ffiname`_.

But using the string repr of ``frictionless`` `Field Types`_ to `narwhals.dtypes`_.

.. _pl.datatypes.convert.dtype_to_ffiname:
    https://github.com/pola-rs/polars/blob/85d078c066860e012f5e7e611558e6382b811b82/py-polars/polars/datatypes/convert.py#L139-L165
.. _Field Types:
    https://datapackage.org/standard/table-schema/#field-types
.. _narwhals.dtypes:
    https://narwhals-dev.github.io/narwhals/api-reference/dtypes/
"""

_DTYPE_TO_FIELD: Mapping[type[DType], FlFieldStr] = {
    v: k for k, v in _FIELD_TO_DTYPE.items()
}


class CompressedCache(Protocol[_KT, _VT]):
    fp: Path
    _mapping: MutableMapping[_KT, _VT]

    def read(self) -> Any: ...
    def __getitem__(self, key: _KT, /) -> _VT: ...

    def __enter__(self) -> IOBase:
        import gzip

        return gzip.open(self.fp, mode="rb").__enter__()

    def __exit__(self, *args) -> None:
        return

    def get(self, key: _KT, default: _T, /) -> _VT | _T:
        if not self._mapping:
            self._mapping.update(self.read())
        return self._mapping.get(key, default)


class UrlCache(CompressedCache[_KT, _VT]):
    """
    `csv`_, `gzip`_ -based, lazy url lookup.

    Operates on a subset of available datasets:
    - Excludes `.parquet`, which `cannot be read via url`_

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
        columns: tuple[str, str],
        tp: type[MutableMapping[_KT, _VT]] = dict["_KT", "_VT"],
    ) -> None:
        self.fp: Path = fp
        self.columns: tuple[str, str] = columns
        self._mapping: MutableMapping[_KT, _VT] = tp()

    def read(self) -> Any:
        import csv

        with self as f:
            b_lines = f.readlines()
        reader = csv.reader((bs.decode() for bs in b_lines), dialect=csv.unix_dialect)
        header = tuple(next(reader))
        if header != self.columns:
            msg = f"Expected header to match {self.columns!r},\nbut got: {header!r}"
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


class SchemaCache(CompressedCache["_Dataset", "_FlSchema"]):
    """
    `json`_, `gzip`_ -based, lazy schema lookup.

    - Primarily benefits ``pandas``, which needs some help identifying **temporal** columns.
    - Utilizes `data package`_ schema types.
    - All methods return falsy containers instead of exceptions

    .. _json:
        https://docs.python.org/3/library/json.html
    .. _gzip:
        https://docs.python.org/3/library/gzip.html
    .. _data package:
        https://github.com/vega/vega-datasets/pull/631
    """

    def __init__(
        self,
        fp: Path,
        /,
        *,
        tp: type[MutableMapping[_Dataset, _FlSchema]] = dict["_Dataset", "_FlSchema"],
    ) -> None:
        self.fp: Path = fp
        self._mapping: MutableMapping[_Dataset, _FlSchema] = tp()

    def read(self) -> Any:
        import json

        with self as f:
            return json.load(f)

    def __getitem__(self, key: _Dataset, /) -> _FlSchema:
        return self.get(key, {})

    def by_dtype(self, name: _Dataset, *dtypes: type[DType]) -> list[str]:
        """
        Return column names specfied in ``name``'s schema.

        Parameters
        ----------
        name
            Dataset name.
        *dtypes
            Optionally, only return columns matching the given data type(s).
        """
        if (match := self[name]) and dtypes:
            include = {_DTYPE_TO_FIELD[tp] for tp in dtypes}
            return [col for col, tp_str in match.items() if tp_str in include]
        else:
            return list(match)

    def schema(self, name: _Dataset, /) -> Mapping[str, DType]:
        return {
            column: _FIELD_TO_DTYPE[tp_str]() for column, tp_str in self[name].items()
        }

    def schema_cast(self, name: _Dataset, /) -> Iterator[nw.Expr]:
        """
        Can be passed directly to `.with_columns(...).

        BUG: `cars` doesnt work in either pandas backend
        """
        for column, dtype in self.schema(name).items():
            yield nw.col(column).cast(dtype)


class DatasetCache(Generic[IntoDataFrameT, IntoFrameT]):
    """Opt-out caching of remote dataset requests."""

    _ENV_VAR: ClassVar[LiteralString] = "ALTAIR_DATASETS_DIR"
    _XDG_CACHE: ClassVar[Path] = (
        Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "altair"
    ).resolve()

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
        names = set[str](ser.to_list())
        for fp in self:
            if fp.name in names:
                fp.unlink()

    def download_all(self) -> None:
        """
        Download any missing datasets for latest version.

        Requires **30-50MB** of disk-space.
        """
        stems = tuple(fp.stem for fp in self)
        predicates = (~(nw.col("sha").is_in(stems)),) if stems else ()
        frame = (
            self._rd._scan_metadata(predicates, is_image=False)
            .select("sha", "suffix", "url")
            .unique("sha")
            .collect()
        )
        if frame.is_empty():
            print("Already downloaded all datasets")
            return None
        print(f"Downloading {len(frame)} missing datasets...")
        for row in frame.iter_rows(named=True):
            fp: Path = self.path / (row["sha"] + row["suffix"])
            with self._rd._opener.open(row["url"]) as f:
                fp.touch()
                fp.write_bytes(f.read())
        print("Finished downloads")
        return None

    @property
    def path(self) -> Path:
        """
        Returns path to datasets cache.

        Defaults to (`XDG_CACHE_HOME`_):

            "$XDG_CACHE_HOME/altair/"

        But can be configured using the environment variable:

            "$ALTAIR_DATASETS_DIR"

        You can set this for the current session via:

            >>> from pathlib import Path
            >>> from altair.datasets import load
            >>> load.cache.path = Path.home() / ".altair_cache"

            >>> load.cache.path.relative_to(Path.home()).as_posix()
            '.altair_cache'

        You can *later* disable caching via:

            >>> load.cache.path = None

        .. _XDG_CACHE_HOME:
            https://specifications.freedesktop.org/basedir-spec/latest/#variables
        """
        self._ensure_active()
        fp = Path(usr) if (usr := os.environ.get(self._ENV_VAR)) else self._XDG_CACHE
        fp.mkdir(parents=True, exist_ok=True)
        return fp

    @path.setter
    def path(self, source: StrPath | None, /) -> None:
        if source is not None:
            os.environ[self._ENV_VAR] = str(Path(source).resolve())
        else:
            os.environ[self._ENV_VAR] = ""

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
        return os.environ.get(self._ENV_VAR) == ""

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


url_cache: UrlCache[Dataset | LiteralString, str] = UrlCache(
    _URL, columns=("dataset_name", "url")
)
schema_cache = SchemaCache(_SCHEMA)
