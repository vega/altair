import json
import os
from typing import Callable, Dict, Union

from jsonschema import validate


#==============================================================================
# VegaLite v1/v2 renderer logic
#==============================================================================


# Custom types for the renderer APIs.
SpecType = dict
MimeBundleType = Dict[str, object]
RendererType = Callable[[SpecType], MimeBundleType]


class VegaLiteBase(object):
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
    schema_path = ''

    def __init__(self, spec, validate=False) -> None:
        self.spec = spec
        self.validate = validate
        self._validate()
    
    def _validate(self) -> None:
        """Validate the spec against the schema."""
        with open(self.schema_path) as f:
            schema_dict = json.load(f)
        validate(self.spec, schema_dict)

    def _repr_mimebundle_(self, include, exclude):
        """Return a MIME bundle for display in Jupyter frontends."""
        if self.renderers is not None:
            return self.renderers.get()(self.spec)
        else:
            return {'text/plain': 'WOW'}
