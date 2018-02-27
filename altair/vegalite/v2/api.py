import six

import pandas as pd

from .schema import *
from .schema import core, channels, mixins, Undefined

from .data import data_transformers, pipe
from ...utils import (infer_vegalite_type, parse_shorthand_plus_data,
                      use_signature, update_nested)
from .display import renderers


SCHEMA_URL = "https://vega.github.io/schema/vega-lite/v2.json"


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
        return {"selection": name}

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
        name = "selector{0:03d}".format(selection.counter)
        selection.counter += 1
    return SelectionMapping(**{name: SelectionDef(**kwds)})

selection.counter = 1


def condition(predicate, if_true, if_false):
    """A conditional attribute or encoding

    Parameters
    ----------
    predicate: SelectionMapping, LogicalOperandPredicate, or string
        the selection predicate or test predicate for the condition.
        if a string is passed, it will be treated as a test operand.
    if_true:
        the spec or object to use if the selection predicate is true
    if_false:
        the spec or object to use if the selection predicate is false

    Returns
    -------
    spec: dict or SchemaBase
        the spec that describes the condition
    """
    if isinstance(predicate, SelectionMapping):
        if len(predicate._kwds) != 1:
            raise NotImplementedError("multiple keys in SelectionMapping")
        prop = 'selection'
        val = list(predicate._kwds.keys())[0]
    elif isinstance(predicate, (LogicalOperandPredicate, six.string_types)):
        prop = 'test'
        val = predicate
    else:
        raise NotImplementedError("condition predicate of type {0}"
                                  "".format(type(predicate)))

    if isinstance(if_true, SchemaBase):
        condition = if_true.copy()
        setattr(condition, prop, val)
    elif isinstance(if_true, six.string_types):
        condition = {prop: val, 'field': if_true}
    else:
        condition = dict({prop: val}, **if_true)

    if isinstance(if_false, SchemaBase):
        selection = if_false.copy()
        selection.condition = condition
    elif isinstance(if_false, six.string_types):
        selection = dict(condition=condition, field=if_false)
    else:
        selection = dict(condition=condition, **if_false)

    return selection


#--------------------------------------------------------------------
# Top-level objects

class TopLevelMixin(object):
    _default_spec_values = {"config": {"view": {"width": 400, "height": 300}}}

    def _prepare_data(self):
        if isinstance(self.data, (dict, core.Data, core.InlineData,
                                  core.UrlData, core.NamedData)):
            pass
        elif isinstance(self.data, pd.DataFrame):
            self.data = pipe(self.data, data_transformers.get())
        elif isinstance(self.data, six.string_types):
            self.data = core.UrlData(self.data)

    def to_dict(self, *args, **kwargs):
        copy = self.copy()
        original_data = getattr(copy, 'data', Undefined)
        copy._prepare_data()

        # We make use of two context markers:
        # - 'data' points to the data that should be referenced for column type
        #   inference.
        # - 'top_level' is a boolean flag that is assumed to be true; if it's
        #   true then a "$schema" arg is added to the dict.
        context = kwargs.get('context', {}).copy()
        is_top_level = context.get('top_level', True)

        context['top_level'] = False
        if original_data is not Undefined:
            context['data'] = original_data
        kwargs['context'] = context

        dct = super(TopLevelMixin, copy).to_dict(*args, **kwargs)

        if is_top_level:
            # since this is top-level we add $schema if it's missing
            if '$schema' not in dct:
                dct['$schema'] = SCHEMA_URL

            # add default values if present
            if copy._default_spec_values:
                dct = update_nested(copy._default_spec_values, dct, copy=True)
        return dct

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


class Chart(TopLevelMixin, mixins.MarkMethodMixin, core.TopLevelFacetedUnitSpec):
    def __init__(self, data=Undefined, encoding=Undefined, mark=Undefined,
                 width=Undefined, height=Undefined, **kwargs):
        super(Chart, self).__init__(data=data, encoding=encoding, mark=mark,
                                    width=width, height=height, **kwargs)


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

        def wrap_in_channel_class(obj, prop):
            clsname = prop.title()
            if isinstance(obj, SchemaBase):
                return obj

            if isinstance(obj, six.string_types):
                pass
            elif 'values' in obj:
                clsname += 'Values'
            cls = getattr(channels, clsname)

            # Do not validate now, because it will be validated later
            return cls.from_dict(obj, validate=False)

        for prop, field in list(kwargs.items()):
            kwargs[prop] = field = wrap_in_channel_class(field, prop)
            if getattr(field, 'condition', Undefined) is not Undefined:
                field['condition'] = wrap_in_channel_class(field['condition'], prop)

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
    def __init__(self, hconcat=(), **kwargs):
        # TODO: move common data to top level?
        # TODO: check for conflicting interaction
        super(HConcatChart, self).__init__(hconcat=list(hconcat), **kwargs)

    def __ior__(self, other):
        self.hconcat.append(other)
        return self

    def __or__(self, other):
        copy = self.copy()
        copy.hconcat.append(other)
        return copy

    # TODO: think about the most useful class API here


def hconcat(*charts, **kwargs):
    """Concatenate charts horizontally"""
    return HConcatChart(charts, **kwargs)


class VConcatChart(TopLevelMixin, core.TopLevelVConcatSpec):
    def __init__(self, vconcat=(), **kwargs):
        # TODO: move common data to top level?
        # TODO: check for conflicting interaction
        super(VConcatChart, self).__init__(vconcat=list(vconcat), **kwargs)

    def __iand__(self, other):
        self.vconcat.append(other)
        return self

    def __and__(self, other):
        copy = self.copy()
        copy.vconcat.append(other)
        return copy

    # TODO: think about the most useful class API here


def vconcat(*charts, **kwargs):
    """Concatenate charts vertically"""
    return VConcatChart(charts, **kwargs)


class LayerChart(TopLevelMixin, core.TopLevelLayerSpec):
    def __init__(self, layer=(), **kwargs):
        # TODO: move common data to top level?
        # TODO: check for conflicting interaction
        super(LayerChart, self).__init__(layer=list(layer), **kwargs)

    def __iadd__(self, other):
        self.layer.append(other)
        return self

    def __add__(self, other):
        copy = self.copy()
        copy.layer.append(other)
        return copy

    # TODO: think about the most useful class API here


def layer(*charts, **kwargs):
    """layer multiple charts"""
    return LayerChart(charts, **kwargs)
