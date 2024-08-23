from __future__ import annotations

import pkgutil
import re
from importlib.util import find_spec
from typing import TYPE_CHECKING

import pytest

from tests import examples_arguments_syntax, examples_methods_syntax

if TYPE_CHECKING:
    from re import Pattern
    from typing import Any, Iterator

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


skip_requires_vl_convert: pytest.MarkDecorator = pytest.mark.skipif(
    find_spec("vl_convert") is None, reason="`vl_convert` not installed."
)
"""
``pytest.mark.skipif`` decorator.

Applies when `vl-convert`_ import would fail.

.. _vl-convert:
   https://github.com/vega/vl-convert
"""


skip_requires_pyarrow: pytest.MarkDecorator = pytest.mark.skipif(
    find_spec("pyarrow") is None, reason="`pyarrow` not installed."
)
"""
``pytest.mark.skipif`` decorator.

Applies when `pyarrow`_ import would fail.

.. _pyarrow:
   https://pypi.org/project/pyarrow/
"""


def id_func_str_only(val) -> str:
    """
    Ensures the generated test-id name uses only `filename` and not `source`.

    Without this, the name is repr(source code)-filename
    """
    if not isinstance(val, str):
        return ""
    else:
        return val


def _distributed_examples(*exclude_prefixes: str) -> Iterator[tuple[Any, str]]:
    RE_NAME: Pattern[str] = re.compile(r"^tests\.(.*)")

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
                    yield source, msg_name
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
    tuple(_distributed_examples("_", "interval_selection_map_quakes")),
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
