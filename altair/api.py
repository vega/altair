"""
Main API for Vega-lite spec generation.

DSL mapping Vega types to IPython traitlets.
"""

try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T

from .utils import (
    parse_shorthand, infer_vegalite_type,
    sanitize_dataframe, dataframe_to_json
)
from ._py3k_compat import string_types

import pandas as pd

from . import schema

from .schema import AggregateOp
from .schema import AxisConfig
from .schema import AxisOrient
from .schema import CellConfig
from .schema import Config
from .schema import DataFormat
from .schema import FacetConfig
from .schema import FacetGridConfig
from .schema import FacetScaleConfig
from .schema import FontStyle
from .schema import FontWeight
from .schema import HorizontalAlign
from .schema import LegendConfig
from .schema import MarkConfig
from .schema import NiceTime
from .schema import Scale
from .schema import ScaleConfig
from .schema import SortField
from .schema import SortOrder
from .schema import StackOffset
from .schema import TimeUnit
from .schema import Transform
from .schema import VerticalAlign
from .schema import Data

from .utils import INV_TYPECODE_MAP, TYPE_ABBR

#*************************************************************************
# Channels
#*************************************************************************


class _ChannelMixin(object):

    def _infer_type(self, data):
        if isinstance(data, pd.DataFrame):
            if not self.type and self.field in data:
                self.type = infer_vegalite_type(data[self.field])
        if data is None:
            self.type = ''

    def to_dict(self):
        if not self.field:
            return None
        return super(_ChannelMixin, self).to_dict()


class PositionChannelDef(schema.PositionChannelDef, _ChannelMixin):

    skip = ['shorthand']

    shorthand = T.Unicode('')
    type = T.Union([schema.Type(), T.Unicode()],
                   allow_none=True, default_value=None)

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(PositionChannelDef, self).__init__(**kwargs)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]


class X(PositionChannelDef):
    channel_name = 'x'


class Y(PositionChannelDef):
    channel_name = 'y'


class Row(PositionChannelDef):
    channel_name = 'row'


class Column(PositionChannelDef):
    channel_name = 'column'


class ChannelDefWithLegend(schema.ChannelDefWithLegend, _ChannelMixin):

    skip = ['shorthand']

    shorthand = T.Unicode('')
    type = T.Union([schema.Type(), T.Unicode()],
                   allow_none=True, default_value=None)

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(ChannelDefWithLegend, self).__init__(**kwargs)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]


class Color(ChannelDefWithLegend):
    channel_name = 'color'


class Size(ChannelDefWithLegend):
    channel_name = 'size'
    
    
class Shape(ChannelDefWithLegend):
    channel_name = 'shape'


class Field(schema.FieldDef, _ChannelMixin):

    skip = ['shorthand']

    shorthand = T.Unicode('')
    type = T.Union([schema.Type(), T.Unicode()],
                   allow_none=True, default_value=None)

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(Field, self).__init__(**kwargs)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]


class Text(Field):
    channel_name = 'text'


class Label(Field):
    channel_name = 'label'


class Detail(Field):
    channel_name = 'detail'


class OrderChannel(schema.OrderChannelDef, _ChannelMixin):

    skip = ['shorthand']

    shorthand = T.Unicode('')
    type = T.Union([schema.Type(), T.Unicode()],
                   allow_none=True, default_value=None)

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(OrderChannel, self).__init__(**kwargs)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]


class Order(OrderChannel):
    channel_name = 'detail'


class Path(OrderChannel):
    channel_name = 'path'
    

#*************************************************************************
# Aliases
#*************************************************************************


class Axis(schema.AxisProperties):
    pass


class Bin(schema.BinProperties):
    pass


class Legend(schema.LegendProperties):
    pass


class Formula(schema.VgFormula):
    
    def __init__(self, field, **kwargs):
        kwargs['field'] = field
        super(Formula, self).__init__(**kwargs)


#*************************************************************************
# Encoding
#*************************************************************************


CHANNEL_CLASSES = {
    'x': X,
    'y': Y,
    'row': Row,
    'column': Column,
    'color': Color,
    'size': Size,
    'shape': Shape,
    'detail': Detail,
    'text': Text,
    'label': Label,
    'path': Path,
    'order': Order
    
}

CHANNEL_NAMES = list(CHANNEL_CLASSES.keys())

MARK_TYPES = [
    "area",
    "bar",
    "line",
    "point",
    "text",
    "tick",
    "circle",
    "square"
]


class Encoding(schema.Encoding):
    
    # Position channels
    x = T.Union([T.Instance(X), T.Unicode()],
                default_value=None, allow_none=True)
    y = T.Union([T.Instance(Y), T.Unicode()],
                default_value=None, allow_none=True)
    row = T.Union([T.Instance(Row), T.Unicode()],
                  default_value=None, allow_none=True)
    column = T.Union([T.Instance(Column), T.Unicode()],
                  default_value=None, allow_none=True)
                  
    # Channels with legends
    color = T.Union([T.Instance(Color), T.Unicode()],
                    default_value=None, allow_none=True)
    size = T.Union([T.Instance(Size), T.Unicode()],
                   default_value=None, allow_none=True)
    shape = T.Union([T.Instance(Shape), T.Unicode()],
                    default_value=None, allow_none=True)
                    
    # Field and order channels
    detail = T.Union([T.Instance(Detail), T.List(T.Instance(Detail)), T.Unicode()],
                     default_value=None, allow_none=True)
    text = T.Union([T.Instance(Text), T.Unicode()],
                   default_value=None, allow_none=True)
    label = T.Union([T.Instance(Label), T.Unicode()],
                   default_value=None, allow_none=True)
    path = T.Union([T.Instance(Path), T.List(T.Instance(Path)), T.Unicode()],
                   default_value=None, allow_none=True)
    order = T.Union([T.Instance(Order), T.List(T.Instance(Order)), T.Unicode()],
                   default_value=None, allow_none=True)


    parent = T.Instance(schema.BaseObject, default_value=None, allow_none=True)

    skip = ['parent']

    def _infer_types(self, data):
        for attr in CHANNEL_NAMES:
            val = getattr(self, attr)
            if val is not None:
                val._infer_type(data)
    
    @T.observe(*CHANNEL_NAMES)
    def _channel_changed(self, change):
        new = change['new']
        name = change['name']
        klass = CHANNEL_CLASSES[name]
        if isinstance(new, string_types):
            setattr(name, klass(new))
        if isinstance(self.parent, Layer):
            channel = getattr(self, name, None)
            if channel is not None:
                meth = getattr(channel, '_infer_type', None)
                if meth is not None:
                    meth(self.parent.data)


#*************************************************************************
# Encoding
#*************************************************************************


class Layer(schema.BaseObject):

    _data = None

    name = T.Unicode()
    description = T.Unicode()
    transform = T.Instance(schema.Transform, default_value=None, allow_none=True)
    mark = T.Enum(MARK_TYPES, default_value='point')
    encoding = T.Instance(Encoding, default_value=None, allow_none=True)
    config = T.Instance(schema.Config, allow_none=True)

    def _encoding_changed(self, name, old, new):
        if isinstance(new, Encoding):
            self.encoding.parent = self
            if isinstance(self.data, pd.DataFrame):
                self.encoding._infer_types(self.data)

    def _set_data(self, new):
        if not (isinstance(new, pd.DataFrame) or isinstance(new, Data) or new is None):
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))
        if self.encoding is not None:
            self.encoding._infer_types(new)
        self._data = new

    def _get_data(self):
        return self._data

    data = property(_get_data, _set_data)

    skip = ['data', '_data']

    def __init__(self, *args, **kwargs):
        super(Layer, self).__init__(**kwargs)
        if len(args)==1:
            self.data = args[0]

    def to_dict(self):
        D = super(Layer, self).to_dict()
        if isinstance(self.data, Data):
            D['data'] = self.data.to_dict()
        if isinstance(self.data, pd.DataFrame):
            values = sanitize_dataframe(self.data).to_dict(orient='records')
            D['data'] = Data(values=values).to_dict()
        return D

    def encode(self, *args, **kwargs):
        """Define the encoding for the Layer."""
        for item in args:
            if item.channel_name in kwargs:
                raise ValueError('Mulitple value for {0} provided'.format(item.channel_name))
            kwargs[item.channel_name] = item
        self.encoding = Encoding(**kwargs)
        return self

    def configure(self, **kwargs):
        """Set chart configuration"""
        self.config = schema.Config(**kwargs)
        return self

    def area(self):
        self.mark = 'area'
        return self

    def bar(self):
        self.mark = 'bar'
        return self

    def line(self):
        self.mark = 'line'
        return self

    def point(self):
        self.mark = 'point'
        return self

    def text(self):
        self.mark = 'text'
        return self

    def tick(self):
        self.mark = 'tick'
        return self

    def circle(self):
        self.mark = 'circle'
        return self

    def square(self):
        self.mark = 'square'
        return self

    def _ipython_display_(self):
        self.display()

    def display(self):
        from IPython.display import display
        from vega import VegaLite
        display(VegaLite(self.to_dict()))



