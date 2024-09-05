import re

import pytest

from altair.utils.deprecation import (
    AltairDeprecationWarning,
    deprecated,
    deprecated_warn,
)


def test_deprecated_class():
    class Dummy:
        def __init__(self, *args) -> None:
            self.args = args

    OldChart = deprecated(version="2.0.0", alternative="LayerChart")(Dummy)

    with pytest.warns(AltairDeprecationWarning, match=r"altair=2\.0\.0.+LayerChart"):
        OldChart()


def test_deprecation_decorator():
    @deprecated(version="999", alternative="func_12345")
    def func(x):
        return x + 1

    with pytest.warns(
        AltairDeprecationWarning, match=r"altair=999.+func_12345 instead"
    ):
        y = func(1)
    assert y == 2


def test_deprecation_warn():
    with pytest.warns(
        AltairDeprecationWarning,
        match=re.compile(r"altair=3321.+this code path is a noop", flags=re.DOTALL),
    ):
        deprecated_warn("this code path is a noop", version="3321", stacklevel=1)
