from __future__ import annotations

import datetime as dt
from collections import deque
from typing import TYPE_CHECKING

import pytest

from altair.utils.schemapi import SchemaValidationError
from altair.vegalite.v5.schema import channels as alt
from altair.vegalite.v5.schema.core import DateTime

if TYPE_CHECKING:
    from collections.abc import Sequence

    from altair.vegalite.v5.schema._typing import Temporal


def test_channels_typing() -> None:
    """
    Ensuring static typing aligns with `SchemaValidationError`(s).

    **Non-exhaustive**, focusing on several repeated patterns.

    This **should not** be generated from the schema.
    """
    nums: list[int] = [1, 2, 3, 4, 5]
    range_nums: range = range(5)
    day: dt.date = dt.date(2024, 10, 27)
    dates: tuple[dt.date, ...] = tuple(day.replace(day.year + n) for n in range_nums)
    dates_mixed: Sequence[Temporal | DateTime] = (
        DateTime(year=2000),
        *dates,
        dt.datetime(2001, 1, 1),
    )

    angle = alt.Angle("field:Q")
    assert angle.to_dict()

    # NOTE: The `_` overloads should be changed to:
    #       def fn(self, _: tp, /) -> R
    assert angle.sort("ascending").to_dict()
    assert angle.sort("-fillOpacity").to_dict()
    assert angle.sort(None)
    assert angle.sort(nums).to_dict()
    assert angle.sort(range_nums).to_dict()
    assert angle.sort(deque(nums)).to_dict()
    assert angle.sort(dates).to_dict()
    assert angle.sort(dates_mixed).to_dict()

    # NOTE: Triggering the type error is intentional
    # DO NOT REMOVE IGNORE COMMENTS
    seq_invariant = angle.sort([*nums, *dates])  # type: ignore[arg-type] # pyright: ignore[reportCallIssue]
    with pytest.raises(SchemaValidationError):
        seq_invariant.to_dict()

    # FIXME: Any overloads that provide parameter names are incorrect (1)
    # - They need to specify they are keyword-only
    with pytest.raises(SchemaValidationError):
        angle.sort("field:Q", "min", "descending").to_dict()
    angle.sort(field="field:Q", op="min", order="descending")

    # FIXME: Any overloads that provide parameter names are incorrect (2)
    # - Doesn't raise `SchemaValidationError`
    # - `"ascending"` is silently ignored when positional
    bad = angle.sort("x", "ascending").to_dict()
    good = angle.sort(encoding="x", order="ascending").to_dict()
    assert isinstance(bad, dict)
    assert isinstance(good, dict)
    with pytest.raises(
        AssertionError, match=r"'x' == {'encoding': 'x', 'order': 'ascending'}"
    ):
        assert bad["sort"] == good["sort"]
