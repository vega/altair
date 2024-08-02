"""Utilities for registering and working with themes."""

from typing import Callable

from .plugin_registry import PluginRegistry

ThemeType = Callable[..., dict]


class ThemeRegistry(PluginRegistry[ThemeType, dict]):
    pass
