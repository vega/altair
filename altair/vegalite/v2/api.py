import six

import pandas as pd

from .schema import *

from .data import data_transformers, pipe
from .schema import core, channels, Undefined
from ...utils import infer_vegalite_type, parse_shorthand_plus_data, use_signature
from .display import renderers


def _get_channels_mapping():
    mapping = {}
    for attr in dir(channels):
        cls = getattr(channels, attr)
        if isinstance(cls, type) and issubclass(cls, SchemaBase):
            mapping[cls] = attr.replace('Value', '').lower()
    return mapping


class TopLevelMixin(object):
    def _prepare_data(self):
        # TODO: it's a bit weird that to_dict, via _prepare_data,
        #       modifies the object. Should we create a copy first?
        if isinstance(self.data, (dict, core.Data, core.InlineData,
                                  core.UrlData, core.NamedData)):
            pass
        elif isinstance(self.data, pd.DataFrame):
            self.data = pipe(self.data, data_transformers.get())
        elif isinstance(self.data, six.string_types):
            self.data = core.UrlData(self.data)

    def to_dict(self, *args, **kwargs):
        original_data = getattr(self, 'data', Undefined)
        self._prepare_data()
        context = kwargs.get('context', {})
        if 'data' not in context and original_data is not Undefined:
            context['data'] = original_data
        kwargs['context'] = context
        return super(TopLevelMixin, self).to_dict(*args, **kwargs)

    # Layering and stacking

    def __add__(self, other):
        return LayerChart([self, other])

    def __sub__(self, other):
        return VConcatChart([self, other])

    def __or__(self, other):
        return HConcatChart([self, other])

    # Display-related methods

    def _repr_mimebundle_(self, include, exclude):
        """Return a MIME bundle for display in Jupyter frontends."""
        return renderers.get()(self.to_dict())

    def display(self):
        from vega3 import VegaLite
        return VegaLite(self.to_dict())


class Chart(TopLevelMixin, core.TopLevelFacetedUnitSpec):
    def __init__(self, data=Undefined, encoding=Undefined, mark=Undefined,
                 width=400, height=300, **kwargs):
        super(Chart, self).__init__(data=data, encoding=encoding, mark=mark,
                                    width=width, height=height, **kwargs)

    @use_signature(core.MarkConfig)
    def mark_area(self, *args, **kwargs):
        self.mark = 'area'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_bar(self, *args, **kwargs):
        self.mark = 'bar'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_line(self, *args, **kwargs):
        self.mark = 'line'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_point(self, *args, **kwargs):
        self.mark = 'point'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_text(self, *args, **kwargs):
        self.mark = 'text'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_tick(self, *args, **kwargs):
        self.mark = 'tick'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_rect(self, *args, **kwargs):
        self.mark = 'rect'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_rule(self, *args, **kwargs):
        self.mark = 'rule'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_circle(self, *args, **kwargs):
        self.mark = 'circle'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_square(self, *args, **kwargs):
        self.mark = 'square'
        self.configure_mark(*args, **kwargs)
        return self

    @use_signature(core.MarkConfig)
    def mark_geoshape(self, *args, **kwargs):
        self.mark = 'geoshape'
        self.configure_mark(*args, **kwargs)
        return self

    def configure_mark(self, *args, **kwargs):
        if args or kwargs:
            if self.config is Undefined:
                self.config = core.Config()
            self.config.mark = core.MarkConfig(*args, **kwargs)
        return self

    # TODO: add hooks for more configure functions

    def encode(self, *args, **kwargs):
        # First convert args to kwargs by inferring the class from the argument
        if args:
            mapping = _get_channels_mapping()
            for arg in args:
                encoding = mapping.get(type(arg), None)
                if encoding is None:
                    raise NotImplementedError("non-keyword arg of type {0}"
                                              "".format(type(arg)))
                if encoding in kwargs:
                    raise ValueError("encode: encoding {0} specified twice"
                                     "".format(encoding))
                kwargs[encoding] = arg

        for prop, field in list(kwargs.items()):
            if not isinstance(field, SchemaBase):
                cls = getattr(channels, prop.title())
                # Don't validate now, because field will be computed
                # as part of the to_dict() call.
                kwargs[prop] = cls.from_dict(field, validate=False)
        # TODO: update nested values rather than overwriting them
        self.encoding = core.EncodingWithFacet(**kwargs)
        return self

    def interactive(self, name='grid', bind_x=True, bind_y=True):
        """Make chart axes scales interactive

        Parameters
        ----------
        name : string
            The selection name to use for the axes scales. This name should be
            unique among all selections within the chart.
        """
        encodings = []
        if bind_x:
            encodings.append('x')
        if bind_y:
            encodings.append('y')
        self.selection = {name: {'bind': 'scales',
                                 'type': 'interval',
                                 'encodings': encodings}}
        return self


class HConcatChart(TopLevelMixin, core.TopLevelHConcatSpec):
    def __init__(self, hconcat, **kwargs):
        # TODO: move common data to top level?
        # TODO: check for conflicting interaction
        super(HConcatChart, self).__init__(hconcat=hconcat, **kwargs)

    # TODO: think about the most useful class API here


class VConcatChart(TopLevelMixin, core.TopLevelVConcatSpec):
    def __init__(self, vconcat, **kwargs):
        # TODO: move common data to top level?
        # TODO: check for conflicting interaction
        super(VConcatChart, self).__init__(vconcat=vconcat, **kwargs)

    # TODO: think about the most useful class API here

class LayerChart(TopLevelMixin, core.TopLevelLayerSpec):
    def __init__(self, layer, **kwargs):
        # TODO: move common data to top level?
        # TODO: check for conflicting interaction
        super(LayerChart, self).__init__(layer=layer, **kwargs)

    # TODO: think about the most useful class API here
