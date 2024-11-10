"""
Parsing/transforming semantic versioning strings.

.. _semantic versioning:
    https://semver.org/
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import polars as pl

if TYPE_CHECKING:
    from typing import TypeVar

    _Frame = TypeVar("_Frame", pl.DataFrame, pl.LazyFrame)

__all__ = ["CANARY", "sort", "with_columns"]

_SEM_VER_FIELDS: tuple[
    Literal["major"], Literal["minor"], Literal["patch"], Literal["pre_release"]
] = "major", "minor", "patch", "pre_release"
CANARY: Literal["--canary"] = "--canary"


def with_columns(frame: _Frame, /, *, col_tag: str = "tag") -> _Frame:
    """
    Extracts components of a `SemVer`_ string into sortable columns.

    .. _SemVer:
        https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions
    """
    fields = pl.col(_SEM_VER_FIELDS)
    pattern = r"""(?x)
        v?(?<major>[[:digit:]]*)\.
        (?<minor>[[:digit:]]*)\.
        (?<patch>[[:digit:]]*)
        (\-(next)?(beta)?\.)?
        (?<pre_release>[[:digit:]]*)?
    """
    sem_ver = pl.col(col_tag).str.extract_groups(pattern).struct.field(*_SEM_VER_FIELDS)
    ldf = (
        frame.lazy()
        .with_columns(sem_ver)
        .with_columns(pl.when(fields.str.len_chars() > 0).then(fields).cast(pl.Int64))
        .with_columns(is_pre_release=pl.col("pre_release").is_not_null())
    )
    if isinstance(frame, pl.DataFrame):
        return ldf.collect()
    else:
        return ldf


def tag_enum(frame: _Frame, /, *, col_tag: str = "tag") -> pl.Enum:
    """Extract an **ascending** order ``pl.Enum`` from ``col_tag``."""
    return pl.Enum(
        frame.lazy()
        .pipe(sort, descending=False)
        .select(col_tag)
        .collect()
        .get_column(col_tag)
    )


def sort(frame: _Frame, /, descending: bool = True) -> _Frame:
    """
    Sort ``frame``, displaying in release order.

    Parameters
    ----------
    descending
        By default, **most recent** is first.

    Notes
    -----
    Ensures pre release versions maintain order, always appearing before actual releases.
    """
    return frame.sort(_SEM_VER_FIELDS, descending=descending, nulls_last=not descending)
