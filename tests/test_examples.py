"""
Note that this module dominates the testing time.

TODO
----
- Research how this could be done with fixtures.

Other optimization ideas
------------------
Cache the calls to `compile` in `altair.utils.execeval`
- The each file has every expression compiled 3x times
- Would immediately reduce to 1x
- Possible there are overlapping expressions between `examples_arguments_syntax` and `examples_methods_syntax`
    - Could lead to further performance gains
- All of the tests only call `eval_block` to operate on the finished chart
    - The need to execute the code is not what is being tested

"""

from __future__ import annotations

import io
from typing import Any

import altair as alt
from altair.utils.execeval import eval_block
from tests import (
    distributed_examples,
    ignore_DataFrameGroupBy,
    skip_requires_vl_convert,
    slow,
)


@ignore_DataFrameGroupBy
@distributed_examples
def test_render_examples_to_chart(source: Any, filename: str) -> None:
    chart = eval_block(source)
    if chart is None:
        msg = f"Example file {filename} should define chart in its final statement."
        raise ValueError(msg)
    try:
        assert isinstance(chart.to_dict(), dict)
    except Exception as err:
        msg = (
            f"Example file {filename} raised an exception when "
            f"converting to a dict: {err}"
        )
        raise AssertionError(msg) from err


@ignore_DataFrameGroupBy
@distributed_examples
def test_from_and_to_json_roundtrip(source: Any, filename: str) -> None:
    """
    Tests if the to_json and from_json work for all examples in the Example Gallery.

    (and by extension to_dict and from_dict)
    """
    chart = eval_block(source)
    if chart is None:
        msg = f"Example file {filename} should define chart in its final statement."
        raise ValueError(msg)
    try:
        first_json = chart.to_json()
        reconstructed_chart = alt.Chart.from_json(first_json)
        # As the chart objects are not
        # necessarily the same - they could use different objects to encode the same
        # information - we do not test for equality of the chart objects, but rather
        # for equality of the json strings.
        second_json = reconstructed_chart.to_json()
        assert first_json == second_json
    except Exception as err:
        msg = (
            f"Example file {filename} raised an exception when "
            f"doing a json conversion roundtrip: {err}"
        )
        raise AssertionError(msg) from err


@slow
@ignore_DataFrameGroupBy
@distributed_examples
@skip_requires_vl_convert
def test_render_examples_to_png(source: Any, filename: str) -> None:
    chart = eval_block(source)
    if chart is None:
        msg = f"Example file {filename} should define chart in its final statement."
        raise ValueError(msg)
    out = io.BytesIO()
    chart.save(out, format="png", engine="vl-convert")
    buf = out.getbuffer()
    prefix = buf[:4].tobytes()
    assert prefix == b"\x89PNG"
