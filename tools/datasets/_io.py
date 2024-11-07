"""
Will be part of the public ``alt.datasets`` subpackage.

- Interfacing with the cached metadata.
    - But not updating it
- Performing requests from those urls
- Dispatching read function on file extension

Note
----
- Building with ``polars`` first, then will work backwards with ``narwhals``.
    - Since ``narwhals`` is a subset of ``polars``
"""

from __future__ import annotations

import urllib.request
from functools import partial
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, TypeVar

import polars as pl

if TYPE_CHECKING:
    import sys
    from urllib.request import OpenerDirector

    from _typeshed import StrPath

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString

    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from narwhals import typing as nw_typing  # noqa: F401

    from tools.datasets._typing import DatasetName, Extension, VersionTag
    from tools.schemapi.utils import OneOrSeq

    _ExtensionScan: TypeAlias = Literal[".parquet"]

    ReadFn: TypeAlias = Callable[..., pl.DataFrame]
    ScanFn: TypeAlias = Callable[..., pl.LazyFrame]
    _T = TypeVar("_T")

__all__ = ["Reader"]

_ItemSlice: TypeAlias = (
    "tuple[int | None, int | Literal['url_npm', 'url_github'] | None]"
)
"""Query result scalar selection."""


class Reader:
    _read_fn: ClassVar[dict[Extension, ReadFn]] = {
        ".csv": pl.read_csv,
        ".json": pl.read_json,
        ".tsv": partial(pl.read_csv, separator="\t"),
        ".arrow": partial(pl.read_ipc, use_pyarrow=True),
    }
    _scan_fn: ClassVar[dict[_ExtensionScan, ScanFn]] = {".parquet": pl.scan_parquet}
    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()

    def __init__(self, fp_trees: Path, /) -> None:
        self._fp_trees: Path = fp_trees

    @classmethod
    def reader_from(cls, source: StrPath, /) -> ReadFn:
        suffix = validate_suffix(source, is_ext_supported)
        return cls._read_fn[suffix]

    @classmethod
    def scanner_from(cls, source: StrPath, /) -> ScanFn:
        suffix = validate_suffix(source, is_ext_scan)
        return cls._scan_fn[suffix]

    def url(
        self,
        name: DatasetName | LiteralString,
        ext: Extension | None = None,
        /,
        tag: VersionTag | Literal["latest"] | None = None,
    ) -> str:
        constraints: dict[str, str] = {}
        if tag == "latest":
            raise NotImplementedError(tag)
        elif tag is not None:
            constraints["tag"] = tag
        # NOTE: Probably need to remove/move this
        if name.endswith((".csv", ".json", ".tsv", ".arrow")):
            name, suffix = name.rsplit(".", maxsplit=1)
            suffix = "." + suffix
            if not is_ext_supported(suffix):
                raise TypeError(suffix)
            else:
                constraints["suffix"] = suffix
        elif ext is not None:
            if not is_ext_supported(ext):
                raise TypeError(ext)
            else:
                constraints["suffix"] = ext
        return self._url_from(item=(0, "url_npm"), dataset_name=name, **constraints)

    def _url_from(
        self,
        *predicates: OneOrSeq[str | pl.Expr],
        item: _ItemSlice = (0, "url_npm"),
        **constraints: Any,
    ) -> str:
        r"""
        Querying multi-version trees metadata for `npm` url to fetch.

        Parameters
        ----------
        \*predicates, \*\*constraints
            Passed directly to `pl.LazyFrame.filter`_.
        item
            Scalar selection args for `pl.DataFrame.item`_.

        .. _pl.LazyFrame.filter:
            https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.filter.html
        .. _pl.DataFrame.item:
            https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.item.html
        """
        source = self._fp_trees
        fn = self.scanner_from(self._fp_trees)
        results = fn(source).filter(*predicates, **constraints).collect()
        if not results.is_empty():
            url = results.item(*item)
            if isinstance(url, str):
                return url
            else:
                msg = f"Expected 'str' but got {type(url).__name__!r} from {url!r}."
                raise TypeError(msg)
        else:
            terms = "\n".join(f"{t!r}" for t in (predicates, constraints) if t)
            msg = f"Found no results for:\n{terms}"
            raise NotImplementedError(msg)

    def dataset(self, url: str, /, **kwds: Any) -> pl.DataFrame:
        """
        Fetch a remote dataset.

        Parameters
        ----------
        url
            Full path to a known dataset.
        **kwds
            Arguments passed to the underlying read function.
        """
        fn = self.reader_from(url)
        with self._opener.open(url) as f:
            return fn(f.read(), **kwds)


def validate_suffix(source: StrPath, guard: Callable[..., TypeIs[_T]], /) -> _T:
    suffix: Any = Path(source).suffix
    if guard(suffix):
        return suffix
    else:
        msg = f"Unexpected file extension {suffix!r}, from:\n{source}"
        raise TypeError(msg)


def is_ext_scan(suffix: Any) -> TypeIs[_ExtensionScan]:
    return suffix == ".parquet"


def is_ext_supported(suffix: Any) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}
