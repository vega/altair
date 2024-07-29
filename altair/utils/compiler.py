from typing import Callable, Dict, Any
from altair.utils import PluginRegistry

# ==============================================================================
# Vega-Lite to Vega compiler registry
# ==============================================================================
VegaLiteCompilerType = Callable[[Dict[str, Any]], Dict[str, Any]]


class VegaLiteCompilerRegistry(PluginRegistry[VegaLiteCompilerType, Dict[str, Any]]):
    pass
