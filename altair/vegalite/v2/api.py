import six

import pandas as pd

from .data import data_transformers, pipe
from .schema import core, channels, Undefined
from ...utils import infer_vegalite_type, parse_shorthand_plus_data, use_signature
from .display import renderers


class TopLevelMixin(object):
    def to_dict(self, *args, **kwargs):
        self.data = pipe(self.data, data_transformers.get())
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
        if args:
            raise NotImplementedError()
        for prop, field in list(kwargs.items()):
            # TODO: this logic should be put into to_dict somehow
            if isinstance(field, six.string_types):
                attrs = parse_shorthand_plus_data(field, self.data)
                cls = getattr(channels, prop.title())
                kwargs[prop] = cls(**attrs)
        # TODO: update nested values rather than overwriting them
        self.encoding = core.EncodingWithFacet(*args, **kwargs)
        return self

    def interactive(self):
        """Make chart axes interactive"""
        self.selection = {'grid': {'bind': 'scales', 'type': 'interval'}}
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
