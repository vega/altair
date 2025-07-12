from collections.abc import Callable
from typing import Any

from altair.utils import PluginRegistry

# ==============================================================================
# Vega-Lite to Vega compiler registry
# ==============================================================================
VegaLiteCompilerType = Callable[[dict[str, Any]], dict[str, Any]]


class VegaLiteCompilerRegistry(PluginRegistry[VegaLiteCompilerType, dict[str, Any]]):
    pass
