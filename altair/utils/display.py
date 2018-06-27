import json
import pkgutil
import textwrap
from typing import Callable, Dict

from jsonschema import validate

from .plugin_registry import PluginRegistry


# ==============================================================================
# Renderer registry
# ==============================================================================
MimeBundleType = Dict[str, object]
RendererType = Callable[..., MimeBundleType]


class RendererRegistry(PluginRegistry[RendererType]):
    entrypoint_err_messages = {
        'notebook': textwrap.dedent(
            """
            To use the 'notebook' renderer, you must install the vega package
            and the associated Jupyter extension.
            See https://altair-viz.github.io/getting_started/installation.html
            for more information.
            """),
        'vegascope': textwrap.dedent(
            """
            To use the 'vegascope' renderer, you must install the vegascope
            package; see http://github.com/diana-hep/vegascope/
            for more information.
            """),
    }

# ==============================================================================
# VegaLite v1/v2 renderer logic
# ==============================================================================



class Displayable(object):
    """A base display class for VegaLite v1/v2.

    This class takes a VegaLite v1/v2 spec and does the following:

    1. Optionally validates the spec against a schema.
    2. Uses the RendererPlugin to grab a renderer and call it when the
       IPython/Jupyter display method (_repr_mimebundle_) is called.

    The spec passed to this class must be fully schema compliant and already
    have the data portion of the spec fully processed and ready to serialize.
    In practice, this means, the data portion of the spec should have been passed
    through appropriate data model transformers.
    """

    renderers = None
    schema_path = ('altair', '')

    def __init__(self, spec, validate=False):
        # type: (dict, bool) ->: None
        self.spec = spec
        self.validate = validate
        self._validate()

    def _validate(self):
        # type: () -> None
        """Validate the spec against the schema."""
        schema_dict = json.loads(pkgutil.get_data(*self.schema_path).decode('utf-8'))
        validate(self.spec, schema_dict)

    def _repr_mimebundle_(self, include, exclude):
        """Return a MIME bundle for display in Jupyter frontends."""
        if self.renderers is not None:
            return self.renderers.get()(self.spec)
        else:
            return {}


def default_renderer_base(spec, mime_type, str_repr, **options):
    """A default renderer for Vega or VegaLite that works for modern frontends.

    This renderer works with modern frontends (JupyterLab, nteract) that know
    how to render the custom VegaLite MIME type listed above.
    """
    assert isinstance(spec, dict)
    bundle = {}
    metadata = {}

    bundle[mime_type] = spec
    bundle['text/plain'] = str_repr
    if options:
        metadata[mime_type] = options
    return bundle, metadata


def json_renderer_base(spec, str_repr, **options):
    """A renderer that returns a MIME type of application/json.

    In JupyterLab/nteract this is rendered as a nice JSON tree.
    """
    return default_renderer_base(spec, mime_type='application/json',
                                 str_repr=str_repr, **options)
