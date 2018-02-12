import os

import pandas as pd
from IPython.display import display

from ...utils import PluginRegistry
from ..display import RendererType, VegaLiteBase


#==============================================================================
# VegaLite v1 renderer logic
#==============================================================================


# The MIME type for Vega-Lite 1.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v1+json'  # type: str

# The entry point group that can be used by other packages to declare other
# renderers that will be auto-detected. Explicit registration is also 
# allowed by the PluginRegistery API.
ENTRY_POINT_GROUP = 'altair.vegalite.v1.renderer'  # type: str

renderers = PluginRegistry[RendererType](entry_point_group=ENTRY_POINT_GROUP)


here = os.path.dirname(os.path.realpath(__file__))


def default_renderer(spec):
    """A default renderer for VegaLite 1 that works for modern frontends.

    This renderer works with modern frontends (JupyterLab, nteract) that know
    how to render the custom VegaLite MIME type listed above.
    """
    assert isinstance(spec, dict)
    bundle = {}
    metadata = {}
    bundle['text/plain'] = '<VegaLite object>'
    bundle[VEGALITE_MIME_TYPE] = spec
    return bundle, metadata


renderers.register('default', default_renderer)
renderers.enable('default')


class VegaLite(VegaLiteBase):
    """An IPython/Jupyter display class for rendering VegaLite 1."""

    renderers = renderers
    schema_path = os.path.join(here,'vega-lite-schema.json')


def vegalite(spec: dict, validate=True):
    """Render and optionally validate a VegaLite 1 spec.

    This will use the currently enabled renderer to render the spec.

    Parameters
    ==========
    spec: dict
        A fully compliant VegaLite 1 spec, with the data portion fully processed.
    validate: bool
        Should the spec be validated against the VegaLite 1 schema?
    """
    display(VegaLite(spec, validate=validate))
