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
import pkgutil
import sys
from typing import Any, Iterable, Iterator
import re
import pytest

import altair as alt
from altair.utils.execeval import eval_block
from tests import examples_arguments_syntax
from tests import examples_methods_syntax

try:
    import vl_convert as vlc  # noqa: F401, RUF100
except ImportError:
    vlc = None


VL_CONVERT_AVAILABLE = "vl_convert" in sys.modules


def iter_examples_filenames(syntax_module) -> Iterator[str]:
    for _importer, modname, ispkg in pkgutil.iter_modules(syntax_module.__path__):
        if not (
            ispkg
            or modname.startswith("_")
            # Temporarily skip this test until https://github.com/vega/altair/issues/3418
            # is fixed
            or modname == "interval_selection_map_quakes"
        ):
            yield f"{modname}.py"


def _distributed_examples() -> Iterator[tuple[Any, str]]:
    # `pytest.mark.parametrize` over 2 modules produces 2x workers
    # - This raises the total jobs from 400 -> 1200
    # - Preventing the three tests from blocking everything else
    RE_NAME: re.Pattern[str] = re.compile(r"^tests\.(.*)")

    for module in [examples_arguments_syntax, examples_methods_syntax]:
        for filename in iter_examples_filenames(module):
            name = module.__name__
            source = pkgutil.get_data(name, filename)
            yield source, f"{RE_NAME.match(name).group(1)}.{filename}"  # type: ignore[union-attr]


distributed_examples: Iterable[tuple[Any, str]] = tuple(_distributed_examples())
"""Tried using as a `fixture`, but wasn't able to combine with `@pytest.mark.parametrize`."""


def id_func(val) -> str:
    """
    Ensures the generated test-id name uses only `filename` and not `source`.

    Without this, the name is repr(source code)-filename
    """
    if not isinstance(val, str):
        return ""
    else:
        return val


@pytest.mark.filterwarnings(
    "ignore:'M' is deprecated.*:FutureWarning",
    "ignore:DataFrameGroupBy.apply.*:DeprecationWarning",
)
@pytest.mark.parametrize(("source", "filename"), distributed_examples, ids=id_func)
def test_render_examples_to_chart(source, filename) -> None:
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


@pytest.mark.filterwarnings(
    "ignore:'M' is deprecated.*:FutureWarning",
    "ignore:DataFrameGroupBy.apply.*:DeprecationWarning",
)
@pytest.mark.parametrize(("source", "filename"), distributed_examples, ids=id_func)
def test_from_and_to_json_roundtrip(source, filename) -> None:
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


@pytest.mark.filterwarnings(
    "ignore:'M' is deprecated.*:FutureWarning",
    "ignore:DataFrameGroupBy.apply.*:DeprecationWarning",
)
@pytest.mark.parametrize(("source", "filename"), distributed_examples, ids=id_func)
@pytest.mark.skipif(
    not VL_CONVERT_AVAILABLE,
    reason="vl_convert not importable; cannot run mimebundle tests",
)
def test_render_examples_to_png(source, filename) -> None:
    chart = eval_block(source)
    if chart is None:
        msg = f"Example file {filename} should define chart in its final statement."
        raise ValueError(msg)
    out = io.BytesIO()
    chart.save(out, format="png", engine="vl-convert")
    assert out.getvalue().startswith(b"\x89PNG")
