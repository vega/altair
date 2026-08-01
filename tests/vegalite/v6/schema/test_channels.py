from __future__ import annotations

import datetime as dt
from collections import deque
from typing import TYPE_CHECKING

import pytest

from altair.utils.schemapi import SchemaValidationError
from altair.vegalite.v6.schema import channels as alt
from altair.vegalite.v6.schema.core import DateTime

if TYPE_CHECKING:
    from collections.abc import Sequence

    from altair.vegalite.v6.schema._typing import Temporal


def test_channels_typing() -> None:
    """
    Ensuring static typing aligns with `SchemaValidationError`(s).

    Important
    ---------
    Unless a comment says otherwise, **every** ``# (type|pyright): ignore`` **is intentional**.

    Notes
    -----
    - *Non-exhaustive*, focusing on several repeated patterns.
    - Not generated from the schema
        - To avoid leaking logic defined during generation
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

    assert angle.sort("ascending").to_dict()
    assert angle.sort("-fillOpacity").to_dict()
    assert angle.sort(None)
    assert angle.sort(nums).to_dict()
    assert angle.sort(range_nums).to_dict()
    assert angle.sort(deque(nums)).to_dict()
    assert angle.sort(dates).to_dict()
    assert angle.sort(dates_mixed).to_dict()

    # NOTE: Triggering static and runtime errors
    invariant_sequence = angle.sort([*nums, *dates])  # type: ignore
    with pytest.raises(SchemaValidationError):
        invariant_sequence.to_dict()

    positional_as_keyword = angle.sort(_="ascending")  # type: ignore[call-overload]
    with pytest.raises(
        SchemaValidationError,
        match=r"'{'_': 'ascending'}' is an invalid value for `sort`",
    ):
        positional_as_keyword.to_dict()

    keyword_as_positional = angle.sort("field:Q", "min", "descending")  # type: ignore[call-overload]
    with pytest.raises(SchemaValidationError):
        keyword_as_positional.to_dict()
    angle.sort(field="field:Q", op="min", order="descending")

    # NOTE: Doesn't raise `SchemaValidationError`
    # - `"ascending"` is silently ignored when positional
    # - Caught as invalid statically, but not at runtime
    bad = angle.sort("x", "ascending").to_dict()  # type: ignore[call-overload]
    good = angle.sort(encoding="x", order="ascending").to_dict()
    assert isinstance(bad, dict)
    assert isinstance(good, dict)
    with pytest.raises(
        AssertionError, match=r"'x' == {'encoding': 'x', 'order': 'ascending'}"
    ):
        assert bad["sort"] == good["sort"]
