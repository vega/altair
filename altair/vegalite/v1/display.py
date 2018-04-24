import os
import textwrap

from ...utils import PluginRegistry, headless, html
from ..display import Displayable
from ..display import default_renderer as default_renderer_base
from ..display import json_renderer as json_renderer_base
from ..display import RendererType

from .schema import SCHEMA_VERSION
VEGALITE_VERSION = SCHEMA_VERSION.lstrip('v')
VEGA_VERSION = '2'
VEGAEMBED_VERSION = '3'


# ==============================================================================
# VegaLite v1 renderer logic
# ==============================================================================


# The MIME type for Vega-Lite 1.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v1+json'  # type: str

# The entry point group that can be used by other packages to declare other
# renderers that will be auto-detected. Explicit registration is also
# allowed by the PluginRegistery API.
ENTRY_POINT_GROUP = 'altair.vegalite.v1.renderer'  # type: str

# The display message when rendering fails
DEFAULT_DISPLAY = """\
<VegaLite 1 object>

If you see this message, it means the renderer has not been properly enabled
for the frontend that you are using. For more information, see
https://altair-viz.github.io/user_guide/troubleshooting.html
"""

renderers = PluginRegistry[RendererType](entry_point_group=ENTRY_POINT_GROUP)
renderers.entrypoint_err_messages = {
    'notebook': textwrap.dedent(
        """
        To use the 'notebook' renderer, you must install the vega package
        and the associated Jupyter extension.
        See https://altair-viz.github.io/getting_started/installation.html
        for more information.
        """)
}


here = os.path.dirname(os.path.realpath(__file__))


def default_renderer(spec):
    return default_renderer_base(spec, VEGALITE_MIME_TYPE, DEFAULT_DISPLAY)


def json_renderer(spec):
    return json_renderer_base(spec, DEFAULT_DISPLAY)


def png_renderer(spec):
    return headless.spec_to_image_mimebundle(spec, format='png',
                                             mode='vega-lite',
                                             vega_version=VEGA_VERSION,
                                             vegaembed_version=VEGAEMBED_VERSION,
                                             vegalite_version=VEGALITE_VERSION)


def svg_renderer(spec):
    return headless.spec_to_image_mimebundle(spec, format='svg',
                                             mode='vega-lite',
                                             vega_version=VEGA_VERSION,
                                             vegaembed_version=VEGAEMBED_VERSION,
                                             vegalite_version=VEGALITE_VERSION)


def colab_renderer(spec):
    return html.spec_to_html_mimebundle(spec, mode='vega-lite',
                                        vega_version=VEGA_VERSION,
                                        vegaembed_version=VEGAEMBED_VERSION,
                                        vegalite_version=VEGALITE_VERSION)


renderers.register('default', default_renderer)
renderers.register('jupyterlab', default_renderer)
renderers.register('nteract', default_renderer)
renderers.register('json', json_renderer)
renderers.register('png', png_renderer)
renderers.register('svg', svg_renderer)
renderers.register('colab', colab_renderer)
renderers.enable('default')


class VegaLite(Displayable):
    """An IPython/Jupyter display class for rendering VegaLite 1."""

    renderers = renderers
    schema_path = (__name__, 'schema/vega-lite-schema.json')


def vegalite(spec, validate=True):
    """Render and optionally validate a VegaLite 1 spec.

    This will use the currently enabled renderer to render the spec.

    Parameters
    ==========
    spec: dict
        A fully compliant VegaLite 1 spec, with the data portion fully processed.
    validate: bool
        Should the spec be validated against the VegaLite 1 schema?
    """
    from IPython.display import display

    display(VegaLite(spec, validate=validate))
