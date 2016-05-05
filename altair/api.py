"""
Main API for Vega-lite spec generation.

DSL mapping Vega types to IPython traitlets.
"""

try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T

from .utils import parse_shorthand, infer_vegalite_type, DataFrameTrait
from ._py3k_compat import string_types
from .renderer import Renderer

import pandas as pd

from . import schema


#*************************************************************************
# Channels
#*************************************************************************


class ChannelMixin(object):

    skip = ['shorthand']

    shorthand = T.Unicode('')

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(PositionChannelDef, self).__init__(**kwargs)

    def _infer_type(self, data):
        if self.type is None and self.field in data:
            self.type = infer_vegalite_type(data[self.field])

    def _shorthand_changed(self, name, old, new):
        D = parse_shorthand(self.shorthand)
        for key, val in D.items():
            setattr(self, key, val)

    def to_dict(self):
        if not self.field:
            return None
        return super(PositionChannelDef, self).to_dict()


class PositionChannelDef(schema.PositionChannelDef, ChannelMixin):
    pass


class X(PositionChannelDef):
    channel_name = 'x'


class Y(PositionChannelDef):
    channel_name = 'y'


class Row(PositionChannelDef):
    channel_name = 'row'


class Col(PositionChannelDef):
    channel_name = 'col'


class ChannelDefWithLegend(spec.ChannelDefWithLegend, ChannelMixin):
    pass


class Color(ChannelDefWithLegend):
    channel_name = 'color'


class Size(ChannelDefWithLegend):
    channel_name = 'size'
    
    
class Shape(ChannelDefWithLegend):
    channel_name = 'shape'


class Field(schema.FieldDef, ChannelMixin):
    channel_nane = 'field'
    

class OrderChannelDef(schema.OrderChannelDef, ChannelMixin):
    pass


class Order(OrderChannelDef):
    channel_name = 'order'


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


class Encoding(schema.Encoding):
    
    # Position channels
    x = T.Union([T.Instance(X), T.Unicode()],
                default_value=None, allow_none=True)
    y = T.Union([T.Instance(Y), T.Unicode()],
                default_value=None, allow_none=True)
    row = T.Union([T.Instance(Row), T.Unicode()],
                  default_value=None, allow_none=True)
    col = T.Union([T.Instance(Col), T.Unicode()],
                  default_value=None, allow_none=True)
                  
    # Channels with legends
    color = T.Union([T.Instance(Color), T.Unicode()],
                    default_value=None, allow_none=True)
    size = T.Union([T.Instance(Size), T.Unicode()],
                   default_value=None, allow_none=True)
    shape = T.Union([T.Instance(Shape), T.Unicode()],
                    default_value=None, allow_none=True)
                    
    # Field and order channels
    detail = T.Union([T.Instance(Field), T.List(T.Instance(Field)), T.Unicode()],
                     default_value=None, allow_none=True)
    text = T.Union([T.Instance(Field), T.Unicode()],
                   default_value=None, allow_none=True)
    label = T.Union([T.Instance(Field), T.Unicode()],
                   default_value=None, allow_none=True)
    path = T.Union([T.Instance(Order), T.List(T.Instance(Order)), T.Unicode()],
                   default_value=None, allow_none=True)
    order = T.Union([T.Instance(Order), T.List(T.Instance(Order)), T.Unicode()],
                   default_value=None, allow_none=True)


    parent = T.Instance(schema.BaseObject, default_value=None, allow_none=True)

    skip = ['parent']

    def _infer_types(self, data):
        for attr in ['x', 'y', 'row', 'col', 'color',
                     'size', 'shape', 'detail', 'text',
                     'label', 'path', 'order']:
            val = getattr(self, attr)
            if val is not None:
                val._infer_type(data)

    def _x_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.x = X(new)
        if getattr(self.parent, 'data', None) is not None:
            self.x._infer_type(self.parent.data)

    def _y_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.y = Y(new)
        if getattr(self.parent, 'data', None) is not None:
            self.y._infer_type(self.parent.data)

    def _row_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.row = Row(new)
        if getattr(self.parent, 'data', None) is not None:
            self.row._infer_type(self.parent.data)

    def _col_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.col = Col(new)
        if getattr(self.parent, 'data', None) is not None:
            self.col._infer_type(self.parent.data)

    def _color_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.color = Color(new)
        if getattr(self.parent, 'data', None) is not None:
            self.color._infer_type(self.parent.data)

    def _size_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.size = Size(new)
        if getattr(self.parent, 'data', None) is not None:
            self.size._infer_type(self.parent.data)

    def _shape_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.shape = Shape(new)
        if self.parent is not None:
            self.shape._infer_type(self.parent.data)

    def _detail_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.detail = Field(new)
        if self.parent is not None:
            self.detail._infer_type(self.parent.data)

    def _text_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.text = Field(new)
        if self.parent is not None:
            self.text._infer_type(self.parent.data)

    def _label_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.label = Field(new)
        if self.parent is not None:
            self.label._infer_type(self.parent.data)

    def _path_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.path = Order(new)
        if self.parent is not None:
            self.path._infer_type(self.parent.data)

    def _order_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.order = Order(new)
        if self.parent is not None:
            self.order._infer_type(self.parent.data)


#*************************************************************************
# Data
#*************************************************************************


class Data(schema.Data):

    formatType = T.Enum(['json', 'csv', 'tsv'], default_value='json')

    def to_dict(self):
        result = {'formatType': self.formatType,
                  'values': self.data.to_dict('records')}
        return result


#*************************************************************************
# Encoding
#*************************************************************************


class Viz(schema.BaseObject):

    name = T.Unicode()
    description = T.Unicode()
    _data = T.Instance(Data, default_value=None, allow_none=True)
    data = DataFrameTrait(default_value=None, allow_none=True)
    transform = T.Instance(schema.Transform, default_value=None, allow_none=True)
    mark = T.Enum(['area', 'bar', 'line', 'point',
                   'text', 'tick', 'circle', 'square'],
                  default_value='point')
    encoding = T.Instance(Encoding, default_value=None, allow_none=True)
    config = T.Instance(schema.Config, allow_none=True)

    def _encoding_changed(self, name, old, new):
        if isinstance(new, Encoding):
            self.encoding.parent = self
            if 'data' in self:
                self.encoding._infer_types(self.data)

    def _data_changed(self, name, old, new):
        if not isinstance(new, pd.DataFrame):
            self.data = pd.DataFrame(new)
            return
        self._data = Data(data=new)
        if self.encoding is not None:
            self.encoding._infer_types(self.data)

    skip = ['data', '_data']

    def __init__(self, data, **kwargs):
        kwargs['data'] = data
        super(Viz, self).__init__(**kwargs)

    def to_dict(self):
        D = super(Viz, self).to_dict()
        D['data'] = self._data.to_dict()
        return D

    def encode(self, **kwargs):
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

    def render(self, **kwargs):
        global _renderer
        return _renderer.render(self, **kwargs)


# Renderer logic

def _get_matplotlib_renderer():
    from .mpl import MatplotlibRenderer
    return MatplotlibRenderer()

def _get_lightning_renderer():
    from .lgn import LightningRenderer
    return LightningRenderer()

_renderers = {
    'matplotlib': _get_matplotlib_renderer,
    'lightning': _get_lightning_renderer
}


_renderer = None

def register_renderer(name, rfactory):
    """Register a renderer factory that creates renderer instances."""
    global _renderers
    _renderers[name] = rfactory

def use_renderer(r):
    """Use a particular renderer, registered by name or an actual Renderer instance."""
    global _renderer
    global _renderers
    if isinstance(r, Renderer):
        _renderer = r
    else:
        if r in _renderers:
            _renderer = _renderers[r]()
        else:
            raise ValueError('renderer could not be found: {0}').format(r)

def list_renderers():
    global _renderers
    return list(_renderers.keys())
