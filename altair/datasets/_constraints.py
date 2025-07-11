"""Set-like guards for matching metadata to an implementation."""

from __future__ import annotations

from collections.abc import Set
from itertools import chain
from typing import TYPE_CHECKING, Any

from narwhals.stable import v1 as nw

if TYPE_CHECKING:
    import sys
    from collections.abc import Iterable, Iterator

    from altair.datasets._typing import Metadata

    if sys.version_info >= (3, 12):
        from typing import Unpack
    else:
        from typing_extensions import Unpack
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

__all__ = [
    "Items",
    "MetaIs",
    "is_arrow",
    "is_csv",
    "is_json",
    "is_meta",
    "is_not_tabular",
    "is_parquet",
    "is_spatial",
    "is_topo",
    "is_tsv",
]

Items: TypeAlias = Set[tuple[str, Any]]


class MetaIs(Set[tuple[str, Any]]):
    _requires: frozenset[tuple[str, Any]]

    def __init__(self, kwds: frozenset[tuple[str, Any]], /) -> None:
        object.__setattr__(self, "_requires", kwds)

    @classmethod
    def from_metadata(cls, meta: Metadata, /) -> MetaIs:
        return cls(frozenset(meta.items()))

    def to_metadata(self) -> Metadata:
        if TYPE_CHECKING:

            def collect(**kwds: Unpack[Metadata]) -> Metadata:
                return kwds

            return collect(**dict(self))
        return dict(self)

    def to_expr(self) -> nw.Expr:
        """Convert constraint into a narwhals expression."""
        if not self:
            msg = f"Unable to convert an empty set to an expression:\n\n{self!r}"
            raise TypeError(msg)
        return nw.all_horizontal(nw.col(name) == val for name, val in self)

    def isdisjoint(self, other: Iterable[Any]) -> bool:
        return super().isdisjoint(other)

    def issubset(self, other: Iterable[Any]) -> bool:
        return self._requires.issubset(other)

    def __call__(self, meta: Items, /) -> bool:
        return self._requires <= meta

    def __hash__(self) -> int:
        return hash(self._requires)

    def __contains__(self, x: object) -> bool:
        return self._requires.__contains__(x)

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        yield from self._requires

    def __len__(self) -> int:
        return self._requires.__len__()

    def __setattr__(self, name: str, value: Any):
        msg = (
            f"{type(self).__name__!r} is immutable.\n"
            f"Could not assign self.{name} = {value}"
        )
        raise TypeError(msg)

    def __repr__(self) -> str:
        items = dict(self)
        if not items:
            contents = "<placeholder>"
        elif suffix := items.pop("suffix", None):
            contents = ", ".join(
                chain([f"'*{suffix}'"], (f"{k}={v!r}" for k, v in items.items()))
            )
        else:
            contents = ", ".join(f"{k}={v!r}" for k, v in items.items())
        return f"is_meta({contents})"


def is_meta(**kwds: Unpack[Metadata]) -> MetaIs:
    return MetaIs.from_metadata(kwds)


is_csv = is_meta(suffix=".csv")
is_json = is_meta(suffix=".json")
is_tsv = is_meta(suffix=".tsv")
is_arrow = is_meta(suffix=".arrow")
is_parquet = is_meta(suffix=".parquet")
is_spatial = is_meta(is_spatial=True)
is_topo = is_meta(is_topo=True)
is_not_tabular = is_meta(is_tabular=False)
