import pandas as pd
from IPython.display import display
from typing import Callable, Dict, Union

from ...utils import PluginRegistry
from ..data import to_values, limit_rows


# The MIME type for Vega-Lite 2.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v2+json'


SpecType = dict
MimeBundleType = Dict[str, object]
RendererType = Callable[[SpecType], MimeBundleType]

renderers = PluginRegistry[RendererType]()



def default_renderer(spec):
    assert isinstance(spec, dict)
    bundle = {}
    bundle['text/plain'] = '<altair.VegaLite object>'
    data = spec['data']
    spec['data'] = to_values(limit_rows(data))
    bundle[VEGALITE_MIME_TYPE] = spec
    return bundle

renderers.register('default', default_renderer)
renderers.enable('default')



class VegaLite(object):

    def __init__(self, spec, validate) -> None:
        self.spec = spec
        self.validate = validate
        self._validate()
    
    def _validate(self) -> None:
        pass

    def _repr_mimebundle_(self, include, exclude):
        """Return a MIME bundle for display in Jupyter frontends."""
        return renderers.get()(self.spec)



def vegalite(spec: dict, validate=True):
    display(VegaLite(spec, validate=validate))


