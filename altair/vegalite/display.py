import json
import os
from typing import Callable, Dict, Union

from jsonschema import validate

SpecType = dict
MimeBundleType = Dict[str, object]
RendererType = Callable[[SpecType], MimeBundleType]


class VegaLiteBase(object):

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
