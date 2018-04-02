import os
import textwrap

import pandas as pd
from IPython.display import display

from ...utils import PluginRegistry, headless, html
from ..display import Displayable
from ..display import default_renderer_base, json_renderer_base
from ..display import SpecType, MimeBundleType, RendererType
from . import api


#==============================================================================
# VegaLite v2 renderer logic
#==============================================================================


# The MIME type for Vega-Lite 2.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v2+json'  # type: str

# The entry point group that can be used by other packages to declare other
# renderers that will be auto-detected. Explicit registration is also
# allowed by the PluginRegistery API.
ENTRY_POINT_GROUP = 'altair.vegalite.v2.renderer'  # type: str

# The display message when rendering fails
DEFAULT_DISPLAY = """\
<VegaLite 2 object>

If you see this message, it means the renderer has not been properly enabled
for the frontend that you are using. For more information, see
https://altair-viz.github.io/getting_started/installation.html
"""

renderers = PluginRegistry[RendererType](entry_point_group=ENTRY_POINT_GROUP)
renderers.entrypoint_err_messages = {
    'notebook': textwrap.dedent(
        """
        To use the 'notebook' renderer, you must install the vega3 package
        and the associated Jupyter extension.
        See https://altair-viz.github.io/getting_started/installation.html
        for more information.
        """)
}


here = os.path.dirname(os.path.realpath(__file__))


def default_renderer(spec, metadata):
    return default_renderer_base(spec, mime_type=VEGALITE_MIME_TYPE,
                                 str_repr=DEFAULT_DISPLAY, metadata=metadata)


def json_renderer(spec, metadata):
    return json_renderer_base(spec, str_repr=DEFAULT_DISPLAY, metadata=metadata)


def png_renderer(spec, metadata):
    bundle = headless.spec_to_image_mimebundle(spec, format='png',
                                               mode='vega-lite',
                                               vega_version=api.VEGA_VERSION,
                                               vegaembed_version=api.VEGAEMBED_VERSION,
                                               vegalite_version=api.VEGALITE_VERSION)
    return bundle, metadata


def svg_renderer(spec, metadata):
    bundle = headless.spec_to_image_mimebundle(spec, format='svg',
                                               mode='vega-lite',
                                               vega_version=api.VEGA_VERSION,
                                               vegaembed_version=api.VEGAEMBED_VERSION,
                                               vegalite_version=api.VEGALITE_VERSION)
    return bundle, metadata


def colab_renderer(spec, metadata):
    bundle = html.spec_to_html_mimebundle(spec,
                                          mode='vega-lite',
                                          vega_version=api.VEGA_VERSION,
                                          vegaembed_version=api.VEGAEMBED_VERSION,
                                          vegalite_version=api.VEGALITE_VERSION)
    return bundle, metadata


renderers.register('default', default_renderer)
renderers.register('jupyterlab', default_renderer)
renderers.register('json', json_renderer)
renderers.register('png', png_renderer)
renderers.register('svg', svg_renderer)
renderers.register('colab', colab_renderer)
renderers.enable('default')


class VegaLite(Displayable):
    """An IPython/Jupyter display class for rendering VegaLite 2."""
    renderers = renderers
    schema_path = (__name__, 'schema/vega-lite-schema.json')


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
