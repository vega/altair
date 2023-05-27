from typing import Callable
from altair.utils import PluginRegistry

# ==============================================================================
# Vega-Lite to Vega compiler registry
# ==============================================================================
VegaLiteCompilerType = Callable


class VegaLiteCompilerRegistry(PluginRegistry[VegaLiteCompilerType]):
    pass
