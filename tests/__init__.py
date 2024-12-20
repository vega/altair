from __future__ import annotations

import pkgutil
import re
import sys
from importlib.util import find_spec
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

from tests import examples_arguments_syntax, examples_methods_syntax

if TYPE_CHECKING:
    from collections.abc import Callable, Collection, Iterator, Mapping
    from re import Pattern

    if sys.version_info >= (3, 11):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from _pytest.mark import ParameterSet

    MarksType: TypeAlias = (
        "pytest.MarkDecorator | Collection[pytest.MarkDecorator | pytest.Mark]"
    )


def windows_has_tzdata() -> bool:
    """
    From PyArrow: python/pyarrow/tests/util.py.

    This is the default location where tz.cpp will look for (until we make
    this configurable at run-time)

    Skip test on Windows when the tz database is not configured.

    See https://github.com/vega/altair/issues/3050.
    """
    return (Path.home() / "Downloads" / "tzdata").exists()


slow: pytest.MarkDecorator = pytest.mark.slow()
"""
Custom ``pytest.mark`` decorator.

By default **all** tests are run.

Slow tests can be **excluded** using::

    >>> hatch run test-fast  # doctest: +SKIP

To run **only** slow tests use::

    >>> hatch run test-slow  # doctest: +SKIP

Either script can accept ``pytest`` args::

    >>> hatch run test-slow --durations=25  # doctest: +SKIP
"""

skip_requires_ipython: pytest.MarkDecorator = pytest.mark.skipif(
    find_spec("IPython") is None, reason="`IPython` not installed."
)
"""
``pytest.mark.skipif`` decorator.

Applies when `IPython`_ import would fail.

.. _IPython:
   https://github.com/ipython/ipython
"""

skip_requires_vl_convert: pytest.MarkDecorator = pytest.mark.skipif(
    find_spec("vl_convert") is None, reason="`vl_convert` not installed."
)
"""
``pytest.mark.skipif`` decorator.

Applies when `vl-convert`_ import would fail.

.. _vl-convert:
   https://github.com/vega/vl-convert
"""

skip_requires_vegafusion: pytest.MarkDecorator = pytest.mark.skipif(
    find_spec("vegafusion") is None, reason="`vegafusion` not installed."
)
"""
``pytest.mark.skipif`` decorator.

Applies when `vegafusion`_ import would fail.

.. _vegafusion:
    https://github.com/vega/vegafusion
"""


def skip_requires_pyarrow(
    fn: Callable[..., Any] | None = None, /, *, requires_tzdata: bool = False
) -> Callable[..., Any]:
    """
    ``pytest.mark.skipif`` decorator.

    Applies when `pyarrow`_ import would fail.

    Additionally, we mark as expected to fail on `Windows`.

    https://github.com/vega/altair/issues/3050

    .. _pyarrow:
    https://pypi.org/project/pyarrow/
    """
    composed = pytest.mark.skipif(
        find_spec("pyarrow") is None, reason="`pyarrow` not installed."
    )
    if requires_tzdata:
        composed = pytest.mark.xfail(
            sys.platform == "win32" and not windows_has_tzdata(),
            reason="Timezone database is not installed on Windows",
        )(composed)

    def wrap(test_fn: Callable[..., Any], /) -> Callable[..., Any]:
        return composed(test_fn)

    if fn is None:
        return wrap
    else:
        return wrap(fn)


def id_func_str_only(val) -> str:
    """
    Ensures the generated test-id name uses only `filename` and not `source`.

    Without this, the name is repr(source code)-filename
    """
    if not isinstance(val, str):
        return ""
    else:
        return val


def _wrap_mark_specs(
    pattern_marks: Mapping[Pattern[str] | str, MarksType], /
) -> dict[Pattern[str], MarksType]:
    return {
        (re.compile(p) if not isinstance(p, re.Pattern) else p): marks
        for p, marks in pattern_marks.items()
    }


def _fill_marks(
    mark_specs: dict[Pattern[str], MarksType], string: str, /
) -> MarksType | tuple[()]:
    it = (v for k, v in mark_specs.items() if k.search(string))
    return next(it, ())


def _distributed_examples(
    *exclude_prefixes: str, marks: Mapping[Pattern[str] | str, MarksType] | None = None
) -> Iterator[ParameterSet]:
    """
    Yields ``pytest.mark.parametrize`` arguments for all examples.

    Parameters
    ----------
    *exclude_prefixes
        Any file starting with these will be **skipped**.
    marks
        Mapping of ``re.search(..., )`` patterns to ``pytest.param(marks=...)``.

        The **first** match (if any) will be inserted into ``marks``.
    """
    RE_NAME: Pattern[str] = re.compile(r"^tests\.(.*)")
    mark_specs = _wrap_mark_specs(marks) if marks else {}

    for pkg in [examples_arguments_syntax, examples_methods_syntax]:
        pkg_name = pkg.__name__
        if match := RE_NAME.match(pkg_name):
            pkg_name_unqual: str = match.group(1)
        else:
            msg = f"Failed to match pattern {RE_NAME.pattern!r} against {pkg_name!r}"
            raise ValueError(msg)
        for _, mod_name, is_pkg in pkgutil.iter_modules(pkg.__path__):
            if not (is_pkg or mod_name.startswith(exclude_prefixes)):
                file_name = f"{mod_name}.py"
                msg_name = f"{pkg_name_unqual}.{file_name}"
                if source := pkgutil.get_data(pkg_name, file_name):
                    yield pytest.param(
                        source, msg_name, marks=_fill_marks(mark_specs, msg_name)
                    )
                else:
                    msg = (
                        f"Failed to get source data from `{pkg_name}.{file_name}`.\n"
                        f"pkgutil.get_data(...) returned: {pkgutil.get_data(pkg_name, file_name)!r}"
                    )
                    raise TypeError(msg)


ignore_DataFrameGroupBy: pytest.MarkDecorator = pytest.mark.filterwarnings(
    "ignore:DataFrameGroupBy.apply.*:DeprecationWarning"
)
"""
``pytest.mark.filterwarnings`` decorator.

Hides ``pandas`` warning(s)::

    "ignore:DataFrameGroupBy.apply.*:DeprecationWarning"
"""


distributed_examples: pytest.MarkDecorator = pytest.mark.parametrize(
    ("source", "filename"),
    tuple(
        _distributed_examples(
            "_",
            "interval_selection_map_quakes",
            marks={
                "beckers_barley.+facet": slow,
                "lasagna_plot": slow,
                "line_chart_with_cumsum_faceted": slow,
                "layered_bar_chart": slow,
                "multiple_interactions": slow,
                "layered_histogram": slow,
                "stacked_bar_chart_with_text": slow,
                "bar_chart_with_labels": slow,
                "interactive_cross_highlight": slow,
                "wind_vector_map": slow,
                r"\.point_map\.py": slow,
                "line_chart_with_color_datum": slow,
            },
        )
    ),
    ids=id_func_str_only,
)
"""
``pytest.mark.parametrize`` decorator.

Provides **all** examples, using both `arguments` & `methods` syntax.

The decorated test can evaluate each resulting chart via::

    from altair.utils.execeval import eval_block

    @distributed_examples
    def test_some_stuff(source: Any, filename: str) -> None:
        chart: ChartType | None = eval_block(source)
        ... # Perform any assertions

Notes
-----
- See `#3431 comment`_ for performance benefit.
- `interval_selection_map_quakes` requires `#3418`_ fix

.. _#3431 comment:
   https://github.com/vega/altair/pull/3431#issuecomment-2168508048
.. _#3418:
   https://github.com/vega/altair/issues/3418
"""
