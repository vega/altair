"""Utilities for registering and working with themes."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Callable

from .plugin_registry import PluginRegistry

if sys.version_info >= (3, 11):
    from typing import LiteralString
else:
    from typing_extensions import LiteralString

if TYPE_CHECKING:
    from altair.utils.plugin_registry import PluginEnabler
    from altair.vegalite.v5.theme import AltairThemes, VegaThemes

ThemeType = Callable[..., dict]


class ThemeRegistry(PluginRegistry[ThemeType, dict]):
    def enable(
        self, name: LiteralString | AltairThemes | VegaThemes | None = None, **options
    ) -> PluginEnabler:
        """
        Enable a theme by name.

        This can be either called directly, or used as a context manager.

        Parameters
        ----------
        name : string (optional)
            The name of the theme to enable. If not specified, then use the
            current active name.
        **options :
            Any additional parameters will be passed to the theme as keyword
            arguments

        Returns
        -------
        PluginEnabler:
            An object that allows enable() to be used as a context manager

        Notes
        -----
        Default `vega` themes can be previewed at https://vega.github.io/vega-themes/
        """
        return super().enable(name, **options)
