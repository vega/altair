from typing import Any

import pytest

import altair.vegalite.v5 as alt
from altair.vegalite.v5.schema._typing import is_color_hex
from altair.vegalite.v5.theme import VEGA_THEMES


@pytest.fixture
def chart():
    return alt.Chart("data.csv").mark_bar().encode(x="x:Q")


def test_vega_themes(chart):
    for theme in VEGA_THEMES:
        with alt.themes.enable(theme):  # pyright: ignore
            dct = chart.to_dict()
        assert dct["usermeta"] == {"embedOptions": {"theme": theme}}
        assert dct["config"] == {
            "view": {"continuousWidth": 300, "continuousHeight": 300}
        }


@pytest.mark.parametrize(
    ("color_code", "valid"),
    [
        ("#FFFFFF", True),
        ("##ff6347", False),
        ("#EE82EE", True),
        ("#1ec9a0", True),
        ("#19B_71", False),
        ("#00#761", False),
        ("123455", False),
        ("#6a5acd ", False),
        ("#f8f8f899", True),
        ("#6a5acd6E", True),
    ],
)
def test_is_color_hex(color_code: Any, *, valid: bool) -> None:
    assert is_color_hex(color_code) == valid
