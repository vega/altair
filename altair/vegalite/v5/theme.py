"""Tools for enabling and registering chart themes."""

from __future__ import annotations

import sys
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Dict, Final, Literal, TypeVar

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


from altair.utils.theme import ThemeRegistry

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    # If you add a theme here, also add it in `VEGA_THEMES` below.
    _ThemeName: TypeAlias = Literal[
        "default",
        "carbonwhite",
        "carbong10",
        "carbong90",
        "carbong100",
        "dark",
        "excel",
        "fivethirtyeight",
        "ggplot2",
        "googlecharts",
        "latimes",
        "opaque",
        "powerbi",
        "quartz",
        "urbaninstitute",
        "vox",
    ]

# If you add a theme here, also add it in `_ThemeName` above.
VEGA_THEMES: list[LiteralString] = [
    "carbonwhite",
    "carbong10",
    "carbong90",
    "carbong100",
    "dark",
    "excel",
    "fivethirtyeight",
    "ggplot2",
    "googlecharts",
    "latimes",
    "powerbi",
    "quartz",
    "urbaninstitute",
    "vox",
]


P = ParamSpec("P")
R = TypeVar("R", bound=Dict[str, Any])


class VegaTheme:
    """Implementation of a builtin vega theme."""

    def __init__(self, theme: str) -> None:
        self.theme = theme

    def __call__(self) -> dict[str, dict[str, dict[str, str | int]]]:
        return {
            "usermeta": {"embedOptions": {"theme": self.theme}},
            "config": {"view": {"continuousWidth": 300, "continuousHeight": 300}},
        }

    def __repr__(self) -> str:
        return f"VegaTheme({self.theme!r})"


# The entry point group that can be used by other packages to declare other
# themes that will be auto-detected. Explicit registration is also
# allowed by the PluginRegistry API.
ENTRY_POINT_GROUP: Final = "altair.vegalite.v5.theme"
themes = ThemeRegistry(entry_point_group=ENTRY_POINT_GROUP)

themes.register(
    "default",
    lambda: {"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}},
)
themes.register(
    "opaque",
    lambda: {
        "config": {
            "background": "white",
            "view": {"continuousWidth": 300, "continuousHeight": 300},
        }
    },
)
themes.register("none", dict)

for theme in VEGA_THEMES:
    themes.register(theme, VegaTheme(theme))

themes.enable("default")


def register_theme(
    name: LiteralString, *, enable: bool
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator for registering a theme function.

    Parameters
    ----------
    name
        Unique name assigned in ``alt.themes``.
    enable
        Auto-enable the wrapped theme.

    Examples
    --------
    Register and enable a theme::

        from __future__ import annotations

        from typing import Any
        import altair as alt


        @alt.register_theme("param_font_size", enable=True)
        def custom_theme() -> dict[str, Any]:
            sizes = 12, 14, 16, 18, 20
            return {
                "autosize": {"contains": "content", "resize": True},
                "background": "#F3F2F1",
                "config": {
                    "axisX": {"labelFontSize": sizes[1], "titleFontSize": sizes[1]},
                    "axisY": {"labelFontSize": sizes[1], "titleFontSize": sizes[1]},
                    "font": "'Lato', 'Segoe UI', Tahoma, Verdana, sans-serif",
                    "headerColumn": {"labelFontSize": sizes[1]},
                    "headerFacet": {"labelFontSize": sizes[1]},
                    "headerRow": {"labelFontSize": sizes[1]},
                    "legend": {"labelFontSize": sizes[0], "titleFontSize": sizes[1]},
                    "text": {"fontSize": sizes[0]},
                    "title": {"fontSize": sizes[-1]},
                },
                "height": {"step": 28},
                "width": 350,
            }

    Until another theme has been enabled, all charts will use defaults set in ``custom_theme``::

        from vega_datasets import data

        source = data.stocks()
        lines = (
            alt.Chart(source, title=alt.Title("Stocks"))
            .mark_line()
            .encode(x="date:T", y="price:Q", color="symbol:N")
        )
        lines.interactive(bind_y=False)

    """

    def decorate(func: Callable[P, R], /) -> Callable[P, R]:
        themes.register(name, func)
        if enable:
            themes.enable(name)

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs)

        return wrapper

    return decorate
