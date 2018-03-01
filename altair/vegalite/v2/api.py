import jsonschema
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


def value(value, **kwargs):
    """Specify a value for use in an encoding"""
    return dict(value=value, **kwargs)


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
        # convert to dict for now; the from_dict call below will wrap this
        # dict in the appropriate schema
        if_true = if_true.to_dict()
    elif isinstance(if_true, six.string_types):
        if_true = {'field': if_true}
    condition = dict({prop: val}, **if_true)

    if isinstance(if_false, SchemaBase):
        # For the selection, the channel definitions all allow selections
        # already. So use this SchemaBase wrapper if possible.
        selection = if_false.copy()
        selection.condition = condition
    elif isinstance(if_false, six.string_types):
        selection = dict(condition=condition, field=if_false)
    else:
        selection = dict(condition=condition, **if_false)

    return selection


#--------------------------------------------------------------------
# Top-level objects

class TopLevelMixin(mixins.ConfigMethodMixin):
    _default_spec_values = {"config": {"view": {"width": 400, "height": 300}}}
    _class_is_valid_at_instantiation = False

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

    def repeat(self, row=Undefined, column=Undefined, **kwargs):
        repeat = core.Repeat(row=row, column=column)
        return RepeatChart(spec=self, repeat=repeat, **kwargs)

    def properties(self, **kwargs):
        copy = self.copy(deep=True, ignore=['data'])
        for key, val in kwargs.items():
            setattr(copy, key, val)
        return copy

    def _add_transform(self, *transforms):
        copy = self.copy()
        if copy.transform is Undefined:
            copy.transform = list(transforms)
        else:
            copy.transform.extend(transforms)
        return copy

    @use_signature(AggregateTransform)
    def transform_aggregate(self, *args, **kwargs):
        return self._add_transform(AggregateTransform(*args, **kwargs))

    @use_signature(BinTransform)
    def transform_bin(self, *args, **kwargs):
        return self._add_transform(BinTransform(*args, **kwargs))

    @use_signature(CalculateTransform)
    def transform_calculate(self, as_, calculate, **kwargs):
        kwargs['as'] = as_
        kwargs['calculate'] = calculate
        return self._add_transform(CalculateTransform(**kwargs))

    @use_signature(FilterTransform)
    def transform_filter(self, filter, **kwargs):
        kwargs['filter'] = filter
        return self._add_transform(FilterTransform(**kwargs))

    @use_signature(LookupTransform)
    def transform_lookup(self, *args, **kwargs):
        return self._add_transform(LookupTransform(*args, **kwargs))

    @use_signature(TimeUnitTransform)
    def transform_timeunit(self, *args, **kwargs):
        return self._add_transform(TimeUnitTransform(*args, **kwargs))

    @use_signature(Resolve)
    def _set_resolve(self, **kwargs):
        copy = self.copy()
        if copy.resolve is Undefined:
            copy.resolve = Resolve()
        for key, val in kwargs.items():
            copy.resolve[key] = val
        return copy

    @use_signature(AxisResolveMap)
    def resolve_axis(self, *args, **kwargs):
        return self._set_resolve(axis=AxisResolveMap(*args, **kwargs))

    @use_signature(LegendResolveMap)
    def resolve_legend(self, *args, **kwargs):
        return self._set_resolve(legend=LegendResolveMap(*args, **kwargs))

    @use_signature(ScaleResolveMap)
    def resolve_scale(self, *args, **kwargs):
        return self._set_resolve(scale=ScaleResolveMap(*args, **kwargs))


# Encoding will contain channel objects that aren't valid at instantiation
core.EncodingWithFacet._class_is_valid_at_instantiation = False


class Chart(TopLevelMixin, mixins.MarkMethodMixin, core.TopLevelFacetedUnitSpec):
    def __init__(self, data=Undefined, encoding=Undefined, mark=Undefined,
                 width=Undefined, height=Undefined, **kwargs):
        super(Chart, self).__init__(data=data, encoding=encoding, mark=mark,
                                    width=width, height=height, **kwargs)

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
                obj = {'field': obj}

            # if obj is not a string or Schema, it must be a mapping
            if 'field' in obj:
                obj = obj.copy()
                obj.update(parse_shorthand(obj['field']))

            if 'value' in obj:
                clsname += 'Value'
            cls = getattr(channels, clsname)

            try:
                # Don't force validation here; some objects won't be valid until
                # they're created in the context of a chart.
                return cls.from_dict(obj, validate=False)
            except jsonschema.ValidationError:
                # our attempts at finding the correct class have failed
                return obj

        for prop, field in list(kwargs.items()):
            try:
                condition = field['condition']
            except (KeyError, TypeError):
                pass
            else:
                if condition is not Undefined:
                    field['condition'] = wrap_in_channel_class(condition, prop)
            kwargs[prop] = wrap_in_channel_class(field, prop)

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


class RepeatChart(TopLevelMixin, core.TopLevelRepeatSpec):
    def __init__(self, spec=Undefined, data=Undefined, repeat=Undefined, **kwargs):
        super(RepeatChart, self).__init__(spec=spec, data=data, repeat=repeat, **kwargs)

    def interactive(self):
        copy = self.copy()
        copy.spec = copy.spec.interactive()
        return copy


def repeat(repeater):
    """Tie a channel to the row or column within a repeated chart"""
    assert repeater in ['row', 'column']
    return core.RepeatRef(repeat=repeater)


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
