from __future__ import annotations

import pytest

import altair.vegalite.v5 as alt
from altair.vegalite.v5.theme import VEGA_THEMES, register_theme, themes


@pytest.fixture
def chart():
    return alt.Chart("data.csv").mark_bar().encode(x="x:Q")


def test_vega_themes(chart) -> None:
    for theme in VEGA_THEMES:
        with alt.themes.enable(theme):
            dct = chart.to_dict()
        assert dct["usermeta"] == {"embedOptions": {"theme": theme}}
        assert dct["config"] == {
            "view": {"continuousWidth": 300, "continuousHeight": 300}
        }


def test_register_theme_decorator() -> None:
    @register_theme("unique name", enable=True)
    def custom_theme() -> dict[str, int]:
        return {"height": 400, "width": 700}

    assert themes.active == "unique name"
    registered = themes.get()
    assert registered is not None
    assert registered() == {"height": 400, "width": 700} == custom_theme()
