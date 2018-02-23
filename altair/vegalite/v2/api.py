import six

import pandas as pd

from .schema import *
from .schema import core, channels, Undefined

from .data import data_transformers, pipe
from ...utils import infer_vegalite_type, parse_shorthand_plus_data, use_signature
from .display import renderers


def _get_channels_mapping():
    mapping = {}
    for attr in dir(channels):
        cls = getattr(channels, attr)
        if isinstance(cls, type) and issubclass(cls, SchemaBase):
            mapping[cls] = attr.replace('Value', '').lower()
    return mapping


# -------------------------------------------------------------------------
# Tools for working with selections
class SelectionMapping(SchemaBase):
    """A mapping of selection names to selection definitions"""
    _schema = {
        'type': 'object',
        'additionalPropeties': {'$ref': '#/definitions/SelectionDef'}
    }
    _rootschema = Root._schema

    def ref(self, name=None):
        """Return a named selection reference.

        If the mapping contains only one selection, then the name need not
        be specified.
        """
        if name is None and len(self._kwds) == 1:
            name = list(self._kwds.keys())[0]
        if name not in self._kwds:
            raise ValueError("'{0}' is not a valid selection name "
                             "in this mapping".format(name))
        return {'selection': name}

    def __add__(self, other):
        if isinstance(other, SelectionMapping):
            copy = self.copy()
            copy._kwds.update(other._kwds)
            return copy
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SelectionMapping):
            self._kwds.update(other._kwds)
        else:
            return NotImplemented

def selection(name=None, **kwds):
    """Create a named selection.

    Parameters
    ----------
    name : string (optional)
        The name of the selection. If not specified, a unique name will be
        created.
    **kwds :
        additional keywords will be used to construct a SelectionDef instance
        that controls the selection.

    Returns
    -------
    selection: SelectionMapping
        The SelectionMapping object that can be used in chart creation.
    """
    if name is None:
        name = "selector{0:02d}".format(selection.counter)
        selection.counter += 1
    return SelectionMapping(**{name: SelectionDef(**kwds)})

selection.counter = 1


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

    def __and__(self, other):
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

    @use_signature(core.MarkDef)
    def mark_area(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='area', **kwargs)
        else:
            copy.mark = 'area'
        return copy

    @use_signature(core.MarkDef)
    def mark_bar(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='bar', **kwargs)
        else:
            copy.mark = 'bar'
        return copy

    @use_signature(core.MarkDef)
    def mark_line(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='line', **kwargs)
        else:
            copy.mark = 'line'
        return copy

    @use_signature(core.MarkDef)
    def mark_point(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='point', **kwargs)
        else:
            copy.mark = 'point'
        return copy

    @use_signature(core.MarkDef)
    def mark_text(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='text', **kwargs)
        else:
            copy.mark = 'text'
        return copy

    @use_signature(core.MarkDef)
    def mark_tick(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='tick', **kwargs)
        else:
            copy.mark = 'tick'
        return copy

    @use_signature(core.MarkDef)
    def mark_rect(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='rect', **kwargs)
        else:
            copy.mark = 'rect'
        return copy

    @use_signature(core.MarkDef)
    def mark_rule(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='rule', **kwargs)
        else:
            copy.mark = 'rule'
        return copy

    @use_signature(core.MarkDef)
    def mark_circle(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='circle', **kwargs)
        else:
            copy.mark = 'circle'
        return copy

    @use_signature(core.MarkDef)
    def mark_square(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='square', **kwargs)
        else:
            copy.mark = 'square'
        return copy

    @use_signature(core.MarkDef)
    def mark_geoshape(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        if kwargs:
            copy.mark = core.MarkDef(type='geoshape', **kwargs)
        else:
            copy.mark = 'geoshape'
        return copy

    # TODO: add configure_* methods

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
        copy = self.copy(deep=True, ignore=['data'])

        # get a copy of the dict representation of the previous encoding
        encoding = copy.encoding
        if encoding is Undefined:
            encoding = {}
        elif isinstance(encoding, dict):
            pass
        else:
            encoding = {k: v for k, v in encoding._kwds.items()
                        if v is not Undefined}

        # update with the new encodings, and apply them to the copy
        encoding.update(kwargs)
        copy.encoding = core.EncodingWithFacet(**encoding)
        return copy

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
        copy = self.copy(deep=True, ignore=['data'])
        # TODO: don't overwrite previous selections?
        copy.selection = {name: {'bind': 'scales',
                                 'type': 'interval',
                                 'encodings': encodings}}
        return copy

    def properties(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        for key, val in kwargs.items():
            setattr(copy, key, val)
        return copy


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
