import pytest

import altair.vegalite.v5 as alt
from altair.vegalite.v5.theme import VEGA_THEMES


@pytest.fixture
def chart():
    return alt.Chart("data.csv").mark_bar().encode(x="x:Q")


def test_vega_themes(chart):
    for theme in VEGA_THEMES:
        with alt.themes.enable(theme):
            dct = chart.to_dict()
        assert dct["usermeta"] == {"embedOptions": {"theme": theme}}
        assert dct["config"] == {
            "view": {"continuousWidth": 300, "continuousHeight": 300}
        }
