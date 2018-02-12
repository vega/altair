import os

import pandas as pd
from IPython.display import display

from ...utils import PluginRegistry
from ..display import Displayable
from ..display import default_renderer as default_renderer_base
from ..display import json_renderer as json_renderer_base
from ..display import SpecType, MimeBundleType, RendererType


#==============================================================================
# VegaLite v2 renderer logic
#==============================================================================


# The MIME type for Vega-Lite 2.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v2+json'  # type: str

# The entry point group that can be used by other packages to declare other
# renderers that will be auto-detected. Explicit registration is also 
# allowed by the PluginRegistery API.
ENTRY_POINT_GROUP = 'altair.vegalite.v2.renderer'  # type: str

renderers = PluginRegistry[RendererType](entry_point_group=ENTRY_POINT_GROUP)


here = os.path.dirname(os.path.realpath(__file__))



def default_renderer(spec):
    return default_renderer_base(spec, VEGALITE_MIME_TYPE, '<VegaLite 2 object>')


def json_renderer(spec):
    return json_renderer_base(spec, '<VegaLite 2 object>')


renderers.register('default', default_renderer)
renderers.register('json', json_renderer)
renderers.enable('default')


class VegaLite(Displayable):
    """An IPython/Jupyter display class for rendering VegaLite 2."""

    renderers = renderers
    schema_path = os.path.join(here,'vega-lite-schema.json')


def vegalite(spec: dict, validate=True):
    """Render and optionally validate a VegaLite 2 spec.

    This will use the currently enabled renderer to render the spec.

    Parameters
    ==========
    spec: dict
        A fully compliant VegaLite 2 spec, with the data portion fully processed.
    validate: bool
        Should the spec be validated against the VegaLite 2 schema?
    """
    display(VegaLite(spec, validate=validate))
