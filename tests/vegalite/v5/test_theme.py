from __future__ import annotations

import json
from collections.abc import Mapping, Set
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Literal, TypeVar, cast, get_args

import pytest

import altair.vegalite.v5 as alt
from altair import theme
from altair.theme import ConfigKwds, ThemeConfig
from altair.vegalite.v5 import schema
from altair.vegalite.v5.schema._typing import VegaThemes, is_color_hex
from altair.vegalite.v5.theme import VEGA_THEMES
from tests import slow

if TYPE_CHECKING:
    import sys

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

T = TypeVar("T")

_Config: TypeAlias = Literal["config"]
_PartialThemeConfig: TypeAlias = Mapping[_Config, ConfigKwds]
"""Represents ``ThemeConfig``, but **only** using the ``"config"`` key."""


@pytest.fixture
def chart() -> alt.Chart:
    return alt.Chart("data.csv").mark_bar().encode(x="x:Q")


def test_vega_themes(chart) -> None:
    for theme_name in VEGA_THEMES:
        with theme.enable(theme_name):
            dct = chart.to_dict()
        assert dct["usermeta"] == {"embedOptions": {"theme": theme_name}}
        assert dct["config"] == {
            "view": {"continuousWidth": 300, "continuousHeight": 300}
        }


@slow
def test_theme_remote_lambda() -> None:
    """
    Compatibility test for ``lambda`` usage in `dash-vega-components`_.

    A ``lambda`` here is to fetch the remote resource **once**, wrapping the result in a function.

    .. _dash-vega-components:
        https://github.com/vega/dash-vega-components/blob/c3e8cae873580bc7a52bc01daea1f27a7df02b8b/example_app.py#L13-L17
    """
    import altair as alt  # noqa: I001
    from urllib.request import urlopen
    import json

    URL = "https://gist.githubusercontent.com/binste/b4042fa76a89d72d45cbbb9355ec6906/raw/e36f79d722bcd9dd954389b1753a2d4a18113227/altair_theme.json"
    with urlopen(URL) as response:
        custom_theme = json.load(response)

    alt.theme.register("remote_binste", enable=True)(lambda: custom_theme)
    assert alt.theme.active == "remote_binste"

    # NOTE: A decorator-compatible way to define an "anonymous" function
    @alt.theme.register("remote_binste_2", enable=True)
    def _():
        return custom_theme

    assert alt.theme.active == "remote_binste_2"

    decorated_theme = alt.theme.get()
    alt.theme.enable("remote_binste")
    assert alt.theme.active == "remote_binste"
    lambda_theme = alt.theme.get()

    assert decorated_theme
    assert lambda_theme
    assert decorated_theme() == lambda_theme()


def test_theme_register_decorator() -> None:
    @theme.register("unique name", enable=True)
    def custom_theme() -> ThemeConfig:
        return {"height": 400, "width": 700}

    assert theme._themes.active == "unique name" == theme.active
    registered = theme._themes.get()
    assert registered is not None
    assert registered == theme.get()
    assert registered() == {"height": 400, "width": 700} == custom_theme()


def test_theme_unregister() -> None:
    @theme.register("big square", enable=True)
    def custom_theme() -> ThemeConfig:
        return {"height": 1000, "width": 1000}

    assert theme.active == "big square"
    fn = theme.unregister("big square")
    assert fn() == custom_theme()
    assert theme.active == theme._themes.active
    # BUG: https://github.com/vega/altair/issues/3619
    # assert theme.active != "big square"

    with pytest.raises(
        TypeError, match=r"Found no theme named 'big square' in registry."
    ):
        theme.unregister("big square")


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


def carbonwhite_theme() -> ThemeConfig:
    """
    Only including **1/4** of `carbon`_ , which gives sufficient structural coverage.

    .. _carbon:
        https://github.com/vega/vega-themes/blob/5f1a5c5b22cc462cf3d46894212152b71cfe964f/src/carbongen.ts
    """
    return ThemeConfig(
        config={
            "arc": {"fill": "#6929c4"},
            "area": {"fill": "#6929c4"},
            "axis": {
                "grid": True,
                "gridColor": "#e0e0e0",
                "labelAngle": 0,
                "labelColor": "#525252",
                "labelFont": 'IBM Plex Sans Condensed, system-ui, -apple-system, BlinkMacSystemFont, ".SFNSText-Regular", sans-serif',
                "labelFontSize": 12,
                "labelFontWeight": 400,
                "titleColor": "#161616",
                "titleFontSize": 12,
                "titleFontWeight": 600,
            },
            "axisX": {"titlePadding": 10},
            "axisY": {"titlePadding": 2.5},
            "background": "#ffffff",
            "circle": {"fill": "#6929c4"},
            "range": {
                "category": [
                    "#6929c4",
                    "#1192e8",
                    "#005d5d",
                    "#9f1853",
                    "#fa4d56",
                    "#570408",
                    "#198038",
                    "#002d9c",
                    "#ee538b",
                    "#b28600",
                    "#009d9a",
                    "#012749",
                    "#8a3800",
                    "#a56eff",
                ],
                "diverging": [
                    "#750e13",
                    "#a2191f",
                    "#da1e28",
                    "#fa4d56",
                    "#ff8389",
                    "#ffb3b8",
                    "#ffd7d9",
                    "#fff1f1",
                    "#e5f6ff",
                    "#bae6ff",
                    "#82cfff",
                    "#33b1ff",
                    "#1192e8",
                    "#0072c3",
                    "#00539a",
                    "#003a6d",
                ],
                "heatmap": [
                    "#f6f2ff",
                    "#e8daff",
                    "#d4bbff",
                    "#be95ff",
                    "#a56eff",
                    "#8a3ffc",
                    "#6929c4",
                    "#491d8b",
                    "#31135e",
                    "#1c0f30",
                ],
            },
            "rect": {"fill": "#6929c4"},
            "style": {
                "guide-label": {
                    "fill": "#525252",
                    "font": 'IBM Plex Sans,system-ui,-apple-system,BlinkMacSystemFont,".sfnstext-regular",sans-serif',
                    "fontWeight": 400,
                },
                "guide-title": {
                    "fill": "#525252",
                    "font": 'IBM Plex Sans,system-ui,-apple-system,BlinkMacSystemFont,".sfnstext-regular",sans-serif',
                    "fontWeight": 400,
                },
            },  # type: ignore[typeddict-unknown-key]
            "title": {
                "anchor": "start",
                "color": "#161616",
                "dy": -15,
                "font": 'IBM Plex Sans,system-ui,-apple-system,BlinkMacSystemFont,".sfnstext-regular",sans-serif',
                "fontSize": 16,
                "fontWeight": 600,
            },
            "view": {"fill": "#ffffff", "stroke": "#ffffff"},
        }
    )


def dark_theme() -> ThemeConfig:
    return ThemeConfig(
        config=ConfigKwds(
            axis={"domainColor": "#fff", "gridColor": "#888", "tickColor": "#fff"},
            background="#333",
            style={
                "guide-label": {"fill": "#fff"},
                "guide-title": {"fill": "#fff"},
            },  # type: ignore[typeddict-unknown-key]
            title={"color": "#fff", "subtitleColor": "#fff"},
            view={"stroke": "#888"},
        )
    )


def excel_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#4572a7"},
            "area": {"fill": "#4572a7"},
            "axis": {
                "bandPosition": 0.5,
                "grid": True,
                "gridColor": "#000000",
                "gridOpacity": 1,
                "gridWidth": 0.5,
                "labelPadding": 10,
                "tickSize": 5,
                "tickWidth": 0.5,
            },
            "axisBand": {"grid": False, "tickExtra": True},
            "background": "#fff",
            "legend": {
                "labelBaseline": "middle",
                "labelFontSize": 11,
                "symbolSize": 50,
                "symbolType": "square",
            },
            "line": {"stroke": "#4572a7", "strokeWidth": 2},
            "range": {
                "category": [
                    "#4572a7",
                    "#aa4643",
                    "#8aa453",
                    "#71598e",
                    "#4598ae",
                    "#d98445",
                    "#94aace",
                    "#d09393",
                    "#b9cc98",
                    "#a99cbc",
                ]
            },
            "rect": {"fill": "#4572a7"},
        }
    }


def fivethirtyeight_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#30a2da"},
            "area": {"fill": "#30a2da"},
            "axis": {
                "domainColor": "#cbcbcb",
                "grid": True,
                "gridColor": "#cbcbcb",
                "gridWidth": 1,
                "labelColor": "#999",
                "labelFontSize": 10,
                "labelPadding": 4,
                "tickColor": "#cbcbcb",
                "tickSize": 10,
                "titleColor": "#333",
                "titleFontSize": 14,
                "titlePadding": 10,
            },
            "axisBand": {"grid": False},
            "background": "#f0f0f0",
            "bar": {"binSpacing": 2, "fill": "#30a2da", "stroke": None},
            "legend": {
                "labelColor": "#333",
                "labelFontSize": 11,
                "padding": 1,
                "symbolSize": 30,
                "symbolType": "square",
                "titleColor": "#333",
                "titleFontSize": 14,
                "titlePadding": 10,
            },
            "line": {"stroke": "#30a2da", "strokeWidth": 2},
            "point": {"filled": True, "shape": "circle"},
            "range": {
                "category": [
                    "#30a2da",
                    "#fc4f30",
                    "#e5ae38",
                    "#6d904f",
                    "#8b8b8b",
                    "#b96db8",
                    "#ff9e27",
                    "#56cc60",
                    "#52d2ca",
                    "#52689e",
                    "#545454",
                    "#9fe4f8",
                ],
                "diverging": [
                    "#cc0020",
                    "#e77866",
                    "#f6e7e1",
                    "#d6e8ed",
                    "#91bfd9",
                    "#1d78b5",
                ],
                "heatmap": ["#d6e8ed", "#cee0e5", "#91bfd9", "#549cc6", "#1d78b5"],
            },
            "rect": {"fill": "#30a2da"},
            "title": {
                "anchor": "start",
                "fontSize": 24,
                "fontWeight": 600,
                "offset": 20,
            },
        }
    }


def ggplot2_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#000"},
            "area": {"fill": "#000"},
            "axis": {
                "domain": False,
                "grid": True,
                "gridColor": "#FFFFFF",
                "gridOpacity": 1,
                "labelColor": "#7F7F7F",
                "labelPadding": 4,
                "tickColor": "#7F7F7F",
                "tickSize": 5.67,
                "titleFontSize": 16,
                "titleFontWeight": "normal",
            },
            "legend": {
                "labelBaseline": "middle",
                "labelFontSize": 11,
                "symbolSize": 40,
            },
            "line": {"stroke": "#000"},
            "range": {
                "category": [
                    "#000000",
                    "#7F7F7F",
                    "#1A1A1A",
                    "#999999",
                    "#333333",
                    "#B0B0B0",
                    "#4D4D4D",
                    "#C9C9C9",
                    "#666666",
                    "#DCDCDC",
                ]
            },
            "rect": {"fill": "#000"},
        }
    }


def googlecharts_theme() -> ThemeConfig:
    """``Padding`` definition `float | Map` needs to be stricter."""
    return {
        "config": {
            "arc": {"fill": "#3366CC"},
            "area": {"fill": "#3366CC"},
            "axis": {
                "domain": False,
                "grid": True,
                "gridColor": "#ccc",
                "tickColor": "#ccc",
            },
            "background": "#fff",
            "circle": {"fill": "#3366CC"},
            "padding": {
                "bottom": 10,
                "left": 10,
                "right": 10,
                "top": 10,
            },
            "range": {
                "category": [
                    "#4285F4",
                    "#DB4437",
                    "#F4B400",
                    "#0F9D58",
                    "#AB47BC",
                    "#00ACC1",
                    "#FF7043",
                    "#9E9D24",
                    "#5C6BC0",
                    "#F06292",
                    "#00796B",
                    "#C2185B",
                ],
                "heatmap": ["#c6dafc", "#5e97f6", "#2a56c6"],
            },
            "rect": {"fill": "#3366CC"},
            "style": {
                "group-title": {"font": "Arial, sans-serif", "fontSize": 12},
                "guide-label": {"font": "Arial, sans-serif", "fontSize": 12},
                "guide-title": {"font": "Arial, sans-serif", "fontSize": 12},
            },  # type: ignore[typeddict-unknown-key]
            "title": {
                "anchor": "start",
                "dy": -3,
                "font": "Arial, sans-serif",
                "fontSize": 14,
                "fontWeight": "bold",
            },
        }
    }


def latimes_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#82c6df"},
            "area": {"fill": "#82c6df"},
            "axis": {
                "labelFont": "Benton Gothic, sans-serif",
                "labelFontSize": 11.5,
                "labelFontWeight": "normal",
                "titleFont": "Benton Gothic Bold, sans-serif",
                "titleFontSize": 13,
                "titleFontWeight": "normal",
            },
            "axisX": {"labelAngle": 0, "labelPadding": 4, "tickSize": 3},
            "axisY": {
                "labelBaseline": "middle",
                "maxExtent": 45,
                "minExtent": 45,
                "tickSize": 2,
                "titleAlign": "left",
                "titleAngle": 0,
                "titleX": -45,
                "titleY": -11,
            },
            "background": "#ffffff",
            "legend": {
                "labelFont": "Benton Gothic, sans-serif",
                "labelFontSize": 11.5,
                "symbolType": "square",
                "titleFont": "Benton Gothic Bold, sans-serif",
                "titleFontSize": 13,
                "titleFontWeight": "normal",
            },
            "line": {"stroke": "#82c6df", "strokeWidth": 2},
            "range": {
                "category": [
                    "#ec8431",
                    "#829eb1",
                    "#c89d29",
                    "#3580b1",
                    "#adc839",
                    "#ab7fb4",
                ],
                "diverging": [
                    "#e68a4f",
                    "#f4bb6a",
                    "#f9e39c",
                    "#dadfe2",
                    "#a6b7c6",
                    "#849eae",
                ],
                "heatmap": [
                    "#fbf2c7",
                    "#f9e39c",
                    "#f8d36e",
                    "#f4bb6a",
                    "#e68a4f",
                    "#d15a40",
                    "#ab4232",
                ],
                "ordinal": [
                    "#fbf2c7",
                    "#f9e39c",
                    "#f8d36e",
                    "#f4bb6a",
                    "#e68a4f",
                    "#d15a40",
                    "#ab4232",
                ],
                "ramp": [
                    "#fbf2c7",
                    "#f9e39c",
                    "#f8d36e",
                    "#f4bb6a",
                    "#e68a4f",
                    "#d15a40",
                    "#ab4232",
                ],
            },
            "rect": {"fill": "#82c6df"},
            "title": {
                "anchor": "start",
                "color": "#000000",
                "font": "Benton Gothic Bold, sans-serif",
                "fontSize": 22,
                "fontWeight": "normal",
            },
        }
    }


def powerbi_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#118DFF"},
            "area": {"fill": "#118DFF", "line": True, "opacity": 0.6},
            "axis": {
                "domain": False,
                "grid": False,
                "labelColor": "#605E5C",
                "labelFontSize": 12,
                "ticks": False,
                "titleColor": "#252423",
                "titleFont": "wf_standard-font, helvetica, arial, sans-serif",
                "titleFontSize": 16,
                "titleFontWeight": "normal",
            },
            "axisBand": {"tickExtra": True},
            "axisQuantitative": {
                "grid": True,
                "gridColor": "#C8C6C4",
                "gridDash": [1, 5],
                "labelFlush": False,
                "tickCount": 3,
            },
            "axisX": {"labelPadding": 5},
            "axisY": {"labelPadding": 10},
            "background": "transparent",
            "bar": {"fill": "#118DFF"},
            "font": "Segoe UI",
            "header": {
                "labelColor": "#605E5C",
                "labelFont": "Segoe UI",
                "labelFontSize": 13.333333333333332,
                "titleColor": "#252423",
                "titleFont": "wf_standard-font, helvetica, arial, sans-serif",
                "titleFontSize": 16,
            },
            "legend": {
                "labelColor": "#605E5C",
                "labelFont": "Segoe UI",
                "labelFontSize": 13.333333333333332,
                "symbolSize": 75,
                "symbolType": "circle",
                "titleColor": "#605E5C",
                "titleFont": "Segoe UI",
                "titleFontWeight": "bold",
            },
            "line": {
                "stroke": "#118DFF",
                "strokeCap": "round",
                "strokeJoin": "round",
                "strokeWidth": 3,
            },
            "point": {"fill": "#118DFF", "filled": True, "size": 75},
            "range": {
                "category": [
                    "#118DFF",
                    "#12239E",
                    "#E66C37",
                    "#6B007B",
                    "#E044A7",
                    "#744EC2",
                    "#D9B300",
                    "#D64550",
                ],
                "diverging": ["#DEEFFF", "#118DFF"],
                "heatmap": ["#DEEFFF", "#118DFF"],
                "ordinal": [
                    "#DEEFFF",
                    "#c7e4ff",
                    "#b0d9ff",
                    "#9aceff",
                    "#83c3ff",
                    "#6cb9ff",
                    "#55aeff",
                    "#3fa3ff",
                    "#2898ff",
                    "#118DFF",
                ],
            },
            "rect": {"fill": "#118DFF"},
            "text": {"fill": "#605E5C", "font": "Segoe UI", "fontSize": 12},
            "view": {"stroke": "transparent"},
        }
    }


def quartz_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#ab5787"},
            "area": {"fill": "#ab5787"},
            "axis": {
                "domainColor": "#979797",
                "domainWidth": 0.5,
                "gridWidth": 0.2,
                "labelColor": "#979797",
                "tickColor": "#979797",
                "tickWidth": 0.2,
                "titleColor": "#979797",
            },
            "axisBand": {"grid": False},
            "axisX": {"grid": True, "tickSize": 10},
            "axisY": {"domain": False, "grid": True, "tickSize": 0},
            "background": "#f9f9f9",
            "legend": {
                "labelFontSize": 11,
                "padding": 1,
                "symbolSize": 30,
                "symbolType": "square",
            },
            "line": {"stroke": "#ab5787"},
            "range": {
                "category": [
                    "#ab5787",
                    "#51b2e5",
                    "#703c5c",
                    "#168dd9",
                    "#d190b6",
                    "#00609f",
                    "#d365ba",
                    "#154866",
                    "#666666",
                    "#c4c4c4",
                ]
            },
            "rect": {"fill": "#ab5787"},
        }
    }


def urbaninstitute_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#1696d2"},
            "area": {"fill": "#1696d2"},
            "axisX": {
                "domain": True,
                "domainColor": "#000000",
                "domainWidth": 1,
                "grid": False,
                "labelAngle": 0,
                "labelFont": "Lato",
                "labelFontSize": 12,
                "tickColor": "#000000",
                "tickSize": 5,
                "titleFont": "Lato",
                "titleFontSize": 12,
                "titlePadding": 10,
            },
            "axisY": {
                "domain": False,
                "domainWidth": 1,
                "grid": True,
                "gridColor": "#DEDDDD",
                "gridWidth": 1,
                "labelFont": "Lato",
                "labelFontSize": 12,
                "labelPadding": 8,
                "ticks": False,
                "titleAngle": 0,
                "titleFont": "Lato",
                "titleFontSize": 12,
                "titlePadding": 10,
                "titleX": 18,
                "titleY": -10,
            },
            "background": "#FFFFFF",
            "legend": {
                "labelFont": "Lato",
                "labelFontSize": 12,
                "offset": 10,
                "orient": "right",
                "symbolSize": 100,
                "titleFont": "Lato",
                "titleFontSize": 12,
                "titlePadding": 10,
            },
            "line": {"color": "#1696d2", "stroke": "#1696d2", "strokeWidth": 5},
            "point": {"filled": True},
            "range": {
                "category": [
                    "#1696d2",
                    "#ec008b",
                    "#fdbf11",
                    "#000000",
                    "#d2d2d2",
                    "#55b748",
                ],
                "diverging": [
                    "#ca5800",
                    "#fdbf11",
                    "#fdd870",
                    "#fff2cf",
                    "#cfe8f3",
                    "#73bfe2",
                    "#1696d2",
                    "#0a4c6a",
                ],
                "heatmap": [
                    "#ca5800",
                    "#fdbf11",
                    "#fdd870",
                    "#fff2cf",
                    "#cfe8f3",
                    "#73bfe2",
                    "#1696d2",
                    "#0a4c6a",
                ],
                "ordinal": [
                    "#cfe8f3",
                    "#a2d4ec",
                    "#73bfe2",
                    "#46abdb",
                    "#1696d2",
                    "#12719e",
                ],
                "ramp": [
                    "#CFE8F3",
                    "#A2D4EC",
                    "#73BFE2",
                    "#46ABDB",
                    "#1696D2",
                    "#12719E",
                    "#0A4C6A",
                    "#062635",
                ],
            },
            "rect": {"fill": "#1696d2"},
            "style": {"bar": {"fill": "#1696d2", "stroke": None}},
            "text": {
                "align": "center",
                "color": "#1696d2",
                "font": "Lato",
                "fontSize": 11,
                "fontWeight": 400,
                "size": 11,
            },
            "title": {"anchor": "start", "font": "Lato", "fontSize": 18},
            "trail": {
                "color": "#1696d2",
                "size": 1,
                "stroke": "#1696d2",
                "strokeWidth": 0,
            },
            "view": {"stroke": "transparent"},
        }
    }


def vox_theme() -> ThemeConfig:
    return {
        "config": {
            "arc": {"fill": "#3e5c69"},
            "area": {"fill": "#3e5c69"},
            "axis": {
                "domainWidth": 0.5,
                "grid": True,
                "labelPadding": 2,
                "tickSize": 5,
                "tickWidth": 0.5,
                "titleFontWeight": "normal",
            },
            "axisBand": {"grid": False},
            "axisX": {"gridWidth": 0.2},
            "axisY": {"gridDash": [3], "gridWidth": 0.4},
            "background": "#fff",
            "legend": {"labelFontSize": 11, "padding": 1, "symbolType": "square"},
            "line": {"stroke": "#3e5c69"},
            "range": {
                "category": [
                    "#3e5c69",
                    "#6793a6",
                    "#182429",
                    "#0570b0",
                    "#3690c0",
                    "#74a9cf",
                    "#a6bddb",
                    "#e2ddf2",
                ]
            },
            "rect": {"fill": "#3e5c69"},
        }
    }


def binste_altair_theme() -> ThemeConfig:
    """Copied from https://gist.github.com/binste/b4042fa76a89d72d45cbbb9355ec6906."""
    return ThemeConfig(
        config={
            "axis": {
                "labelFontSize": 16,
                "titleFontSize": 16,
                "titleFontWeight": "normal",
                "gridColor": "lightGray",
                "labelAngle": 0,
                "labelFlush": False,
                "labelPadding": 5,
            },
            "axisY": {
                "domain": False,
                "ticks": False,
                "labelPadding": 10,
                "titleAngle": 0,
                "titleY": -20,
                "titleAlign": "left",
                "titlePadding": 0,
            },
            "axisTemporal": {"grid": False},
            "axisDiscrete": {"ticks": False, "labelPadding": 10, "grid": False},
            "scale": {"barBandPaddingInner": 0.2},
            "header": {"labelFontSize": 16, "titleFontSize": 16},
            "legend": {
                "labelFontSize": 16,
                "titleFontSize": 16,
                "titleFontWeight": "normal",
            },
            "title": {
                "fontSize": 20,
                "fontStyle": "normal",
                "align": "left",
                "anchor": "start",
                "orient": "top",
                "fontWeight": 600,
                "offset": 10,
                "subtitlePadding": 3,
                "subtitleFontSize": 16,
            },
            "view": {
                "strokeWidth": 0,
                "continuousHeight": 350,
                "continuousWidth": 600,
                "step": 50,
            },
            "line": {"strokeWidth": 3.5},
            "text": {"fontSize": 16},
            "circle": {"size": 60},
            "point": {"size": 60},
            "square": {"size": 60},
        }
    )


def husky_theme() -> ThemeConfig:
    """
    Adapted from https://github.com/deppen8/husky-altair-theme/blob/46f680532ee38c44e656903d3f1affe11b9982bb/husky_theme.py.

    Keeps 2 errors present in the original (marked by `# type: ignore[...]`).
    """
    PURPLE = "#4b2e83"
    GOLD = "#b7a57a"
    METALLIC_GOLD = "#85754d"
    LIGHT_GRAY = "#d9d9d9"
    DARK_GRAY = "#444444"
    BLACK = "#000000"

    HEADER_FONT = "EncodeSans-Regular"
    BODY_FONT = "OpenSans-Regular"
    BODY_FONT_BOLD = "OpenSans-Bold"

    return ThemeConfig(
        config={
            "title": {
                "fontSize": 18,
                "font": HEADER_FONT,
                "anchor": "start",
                "color": PURPLE,
            },
            "axisX": {
                "domain": True,
                "domainColor": DARK_GRAY,
                "domainWidth": 1,
                "grid": True,
                "gridColor": LIGHT_GRAY,
                "gridWidth": 0.5,
                "labelFont": BODY_FONT,
                "labelFontSize": 12,
                "labelColor": DARK_GRAY,
                "labelAngle": 0,
                "tickColor": DARK_GRAY,
                "tickSize": 5,
                "titleFont": BODY_FONT_BOLD,
                "titleFontSize": 12,
            },
            "axisY": {
                "domain": True,
                "domainColor": DARK_GRAY,
                "grid": True,
                "gridColor": LIGHT_GRAY,
                "gridWidth": 0.5,
                "labelFont": BODY_FONT,
                "labelFontSize": 12,
                "labelAngle": 0,
                "ticks": True,
                "titleFont": BODY_FONT_BOLD,
                "titleFontSize": 12,
            },
            "header": {
                "labelFont": BODY_FONT,
                "labelFontSize": 16,
                "titleFont": BODY_FONT_BOLD,
                "titleFontSize": 16,
            },
            "range": {
                "category": [
                    PURPLE,
                    GOLD,
                    LIGHT_GRAY,
                    METALLIC_GOLD,
                    BLACK,
                    DARK_GRAY,
                ],
                "diverging": [PURPLE, "#c2a5cf", LIGHT_GRAY, GOLD, METALLIC_GOLD],
            },
            "legend": {
                "labelFont": BODY_FONT,
                "labelFontSize": 12,
                "symbolSize": 100,
                "titleFont": BODY_FONT_BOLD,
                "titleFontSize": 12,
            },
            "area": {
                "fill": PURPLE,
            },
            "circle": {"fill": PURPLE, "size": 40},
            "line": {
                "color": PURPLE,
                "stroke": PURPLE,
                "strokeWidth": 3,
            },
            "trail": {
                "color": PURPLE,
                "stroke": PURPLE,
                "strokeWidth": 0,
                "size": 1,
            },
            "path": {
                "stroke": PURPLE,
                "strokeWidth": 0.5,
            },  # type: ignore[typeddict-unknown-key]
            "point": {"color": PURPLE, "size": 40},
            "text": {
                "font": BODY_FONT,
                "color": PURPLE,
                "fontSize": 11,
                "align": "right",
                "size": 14,
            },
            "bar": {
                "size": 10,
                "binSpacing": 1,
                "continuousBandSize": 10,
                "fill": PURPLE,
                "stroke": False,  # type: ignore[typeddict-item]
            },
            "tick": {"color": PURPLE},
        },
    )


known_themes: pytest.MarkDecorator = pytest.mark.parametrize(
    "theme_func",
    [
        carbonwhite_theme,
        dark_theme,
        excel_theme,
        fivethirtyeight_theme,
        ggplot2_theme,
        googlecharts_theme,
        latimes_theme,
        powerbi_theme,
        quartz_theme,
        urbaninstitute_theme,
        vox_theme,
        binste_altair_theme,
        husky_theme,
    ],
)
"""
``pytest.mark.parametrize`` decorator.

Provides themes from `vega-themes`_ and `other sources`_.

Notes
-----
These are **redefined by hand** to run through a type checker.

.. _vega-themes:
   https://vega.github.io/vega-themes/
.. _other sources:
    https://github.com/vega/altair/issues/3519#issuecomment-2292010192
"""


@known_themes
def test_theme_config(theme_func: Callable[[], ThemeConfig], chart) -> None:
    """
    Simple-minded extra safety for themes.

    See ``(test_vega_themes|test_register_theme_decorator)`` for comprehensive suite.
    """
    name = cast("LiteralString", theme_func.__qualname__)
    theme.register(name, enable=True)(theme_func)
    assert chart.to_dict(validate=True)
    assert theme.get() == theme_func


# NOTE: There are roughly 70 keys
# - not really reasonable to create a literal that long for testing only
# - therefore, using `frozenset[str]`
@pytest.fixture(scope="session")
def config_keys() -> frozenset[str]:
    return ConfigKwds.__required_keys__.union(
        ConfigKwds.__optional_keys__,
        ConfigKwds.__readonly_keys__,  # type: ignore[attr-defined]
        ConfigKwds.__mutable_keys__,  # type: ignore[attr-defined]
    )


@pytest.fixture(scope="session")
def theme_name_keys() -> frozenset[VegaThemes]:
    return frozenset(get_args(VegaThemes))


@pytest.fixture(scope="session")
def themes_path() -> Path:
    return Path(schema.__file__).parent / "vega-themes.json"


def is_keyed_exact(obj: Any, other: Set[T]) -> TypeIs[Mapping[T, Any]]:
    return isinstance(obj, Mapping) and obj.keys() == other


def is_config_kwds(obj: Any, other: Any) -> TypeIs[ConfigKwds]:
    return isinstance(obj, Mapping) and obj.keys() <= other


def is_vega_theme(obj: Any, config_keys: Any) -> TypeIs[_PartialThemeConfig]:
    if is_keyed_exact(obj, frozenset[_Config]({"config"})):
        inner = obj["config"]
        return is_config_kwds(inner, config_keys)
    else:
        return False


def is_vega_theme_all(
    obj: Any, theme_name_keys: frozenset[VegaThemes], config_keys: frozenset[str]
) -> TypeIs[Mapping[VegaThemes, _PartialThemeConfig]]:
    return is_keyed_exact(obj, theme_name_keys) and all(
        is_vega_theme(definition, config_keys) for definition in obj.values()
    )


def test_vendored_vega_themes_json(
    themes_path: Path,
    theme_name_keys: frozenset[VegaThemes],
    config_keys: frozenset[str],
) -> None:
    """
    Ensure every vendored theme can be represented as a ``ThemeConfig`` type.

    Related
    -------
    - https://github.com/vega/altair/issues/3666#issuecomment-2450057530
    """
    with themes_path.open(encoding="utf-8") as f:
        content = json.load(f)

    assert is_vega_theme_all(content, theme_name_keys, config_keys)
