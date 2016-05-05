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

import .schema


class ShorthandMixin(object):

class PositionChannelDef(schema.PositionChannelDef, ShorthandMixin):

    skip = ['shorthand']

    shorthand = T.Unicode('')

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(PositionChannelDef, self).__init__(**kwargs)

    def _infer_type(self, data):
        if self.type is None and self.field in data:
            self.type = infer_vegalite_type(data[self.field])

    def _shorthand_changed(self, name, old, new):
        # TODO: if name of shorthand changed, should it reset all properties of obj?
        D = parse_shorthand(self.shorthand)
        for key, val in D.items():
            setattr(self, key, val)

    def to_dict(self):
        if not self.field:
            return None
        return super(PositionChannelDef, self).to_dict()


class X(PositionChannelDef):
    channel_name = 'x'


class Y(PositionChannelDef):
    channel_name = 'y'


class Row(PositionChannelDef):
    channel_name = 'row'


class Col(PositionChannelDef):
    channel_name = 'col'


class ChannelDefWithLegend(spec.ChannelDefWithLegend):

    skip = ['shorthand']

    shorthand = T.Unicode('')

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(PositionChannelDef, self).__init__(**kwargs)

    def _infer_type(self, data):
        if self.type is None and self.name in data:
            self.type = infer_vegalite_type(data[self.name])

    def _shorthand_changed(self, name, old, new):
        # TODO: if name of shorthand changed, should it reset all properties of obj?
        D = parse_shorthand(self.shorthand)
        for key, val in D.items():
            setattr(self, key, val)

    def to_dict(self):
        if not self.name:
            return None
        return super(PositionChannelDef, self).to_dict()


class Color(ChannelDefWithLegend):
    channel_name = 'color'


class Size(ChannelDefWithLegend):
    channel_name = 'size'
    
    
class Shape(ChannelDefWithLegend):
    channel_name = 'shape'


class Field(schema.FieldDef):
    
    skip = ['shorthand']

    shorthand = T.Unicode('')

    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        super(Field, self).__init__(**kwargs)

    def _infer_type(self, data):
        if self.type is None and self.name in data:
            self.type = infer_vegalite_type(data[self.name])

    def _shorthand_changed(self, name, old, new):
        # TODO: if name of shorthand changed, should it reset all properties of obj?
        D = parse_shorthand(self.shorthand)
        for key, val in D.items():
            setattr(self, key, val)

    def to_dict(self):
        if not self.name:
            return None
        return super(Field, self).to_dict()
    


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


class Encoding(schema.Encoding):
    # TODO: add test and detail
    
    x = T.Union([T.Instance(X), T.Unicode()],
                default_value=None, allow_none=True)
    y = T.Union([T.Instance(Y), T.Unicode()],
                default_value=None, allow_none=True)
    row = T.Union([T.Instance(Row), T.Unicode()],
                  default_value=None, allow_none=True)
    col = T.Union([T.Instance(Col), T.Unicode()],
                  default_value=None, allow_none=True)
    color = T.Union([T.Instance(Color), T.Unicode()],
                    default_value=None, allow_none=True)
    size = T.Union([T.Instance(Size), T.Unicode()],
                   default_value=None, allow_none=True)
    shape = T.Union([T.Instance(Shape), T.Unicode()],
                    default_value=None, allow_none=True)
    detail = T.Union([T.Instance(Detail), T.Unicode()],
                     default_value=None, allow_none=True)
    text = T.Union([T.Instance(Text), T.Unicode()],
                   default_value=None, allow_none=True)

    parent = T.Instance(BaseObject, default_value=None, allow_none=True)

    skip = ['parent', 'config']

    def _infer_types(self, data):
        for attr in ['x', 'y', 'row', 'col', 'size', 'color', 'shape', 'detail', 'text']:
            val = getattr(self, attr)
            if val is not None:
                val._infer_type(data)

    def _x_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.x = X(new, config=self.config)
        if getattr(self.parent, 'data', None) is not None:
            self.x._infer_type(self.parent.data)

    def _y_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.y = Y(new, config=self.config)
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

    def _size_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.size = Size(new)
        if getattr(self.parent, 'data', None) is not None:
            self.size._infer_type(self.parent.data)

    def _color_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.color = Color(new)
        if getattr(self.parent, 'data', None) is not None:
            self.color._infer_type(self.parent.data)

    def _shape_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.shape = Shape(new)
        if self.parent is not None:
            self.shape._infer_type(self.parent.data)

    def _detail_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.detail = Detail(new)
        if self.parent is not None:
            self.detail._infer_type(self.parent.data)

    def _text_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.text = Text(new)
        if self.parent is not None:
            self.text._infer_type(self.parent.data)


class Viz(BaseObject):

    marktype = T.Enum(['point', 'tick', 'bar', 'line',
                      'area', 'circle', 'square', 'text'],
                      default_value='point')
    encoding = T.Instance(spec.Encoding, default_value=None, allow_none=True)
    config = T.Instance(spec.Config, allow_none=True)

    def _config_default(self):
        return Config()

    _data = T.Instance(Data, default_value=None, allow_none=True)
    data = DataFrameTrait(default_value=None, allow_none=True)

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

    skip = ['data', '_data', 'vlconfig']

    def __init__(self, data, **kwargs):
        kwargs['data'] = data
        super(Viz, self).__init__(**kwargs)

    def to_dict(self):
        D = super(Viz, self).to_dict()
        D['data'] = self._data.to_dict()
        D['config'] = self.vlconfig.to_dict()
        return D

    def encode(self, **kwargs):
        self.encoding = Encoding(**kwargs)
        return self

    def configure(self, **kwargs):
        """Set chart configuration"""
        self.config = spec.Config(**kwargs)
        return self

    def set_single_dims(self, width, height):
        """
        Helper function for setting single-widths

        Parameters
        ----------
        width: int
        height: int
        """
        self.vlconfig.width = width
        self.vlconfig.height = height
        self.vlconfig.singleWidth = int(width * 0.75)
        self.vlconfig.singleHeight = int(height * 0.75)

        if self.encoding.x.type in ('N', 'O'):
            self.encoding.x.band = Band(size=int(width/10))

        if self.encoding.y.type in ('N', 'O'):
            self.encoding.y.band = Band(size=int(height/10))
        return self

    def mark(self, mt):
        """
        Set mark to given string value.

        Parameters
        ----------
        mt: str
        """
        self.marktype = mt
        return self

    def point(self):
        return self.mark('point')

    def tick(self):
        return self.mark('tick')

    def bar(self):
        return self.mark('bar')

    def line(self):
        return self.mark('line')

    def area(self):
        return self.mark('area')

    def circle(self):
        return self.mark('circle')

    def square(self):
        return self.mark('square')

    def text(self):
        return self.mark('text')

    def hist(self, bins=10, **kwargs):
        """
        Render histogram with given `bins`.

        Parameters
        ----------
        bins: int, default 10
        """

        self.marktype = "bar"

        config = Config()

        config.Y.type = "Q"
        config.Y.aggregate = "count"

        # We're making sure a y-change is triggered
        self.encoding = Encoding(config=config, y='', **kwargs)

        if isinstance(kwargs.get("x"), str):
            self.encoding.x.bin = Bin(maxbins=bins)

        # Hack: y.name should be "*", but version weirdness
        self.encoding.y.name = self.encoding.x.name

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
