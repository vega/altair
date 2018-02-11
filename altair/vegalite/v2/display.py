import os

import pandas as pd
from IPython.display import display

from ...utils import PluginRegistry
from ..display import RendererType, VegaLiteBase

# The MIME type for Vega-Lite 2.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v1+json'
ENTRY_POINT_GROUP = 'altair.vegalite.v2.renderer'

renderers = PluginRegistry[RendererType](entry_point_group=ENTRY_POINT_GROUP)


here = os.path.dirname(os.path.realpath(__file__))


def default_renderer(spec):
    assert isinstance(spec, dict)
    bundle = {}
    metadata = {}
    bundle['text/plain'] = '<VegaLite object>'
    bundle[VEGALITE_MIME_TYPE] = spec
    return bundle, metadata


renderers.register('default', default_renderer)
renderers.enable('default')


class VegaLite(VegaLiteBase):

    renderers = renderers
    schema_path = os.path.join(here,'vega-lite-schema.json')


def vegalite(spec: dict, validate=True):
    display(VegaLite(spec, validate=validate))
