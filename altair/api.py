"""
Main API for Vega-lite spec generation
"""

try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T

from .utils import parse_shorthand
from ._py3k_compat import string_types

import pandas as pd


class BaseObject(T.HasTraits):
    
    def __contains__(self, key):
        value = getattr(self, key)
        if isinstance(value, pd.DataFrame):
            return True
        return (value is not None) and (not (not isinstance(value, bool) and not value))

    def to_dict(self):
        result = {}
        for k in self.traits():
            if k in self:
                v = getattr(self, k)
                if isinstance(v, BaseObject):
                    result[k] = v.to_dict()
                else:
                    result[k] = v
        return result

    def __repr__(self):
        return repr(self.to_dict())


class Data(BaseObject):

    formatType = T.Enum(['json','csv'], default_value='json')
    url = T.Unicode(default_value=None, allow_none=True)
    values = T.List(default_value=None, allow_none=True)
    
    def to_dict(self):
        result = {'formatType':self.formatType,
                  'values':self.data.to_dict('records')
                  }
        return result
    
class Scale(BaseObject):
    pass

class Axis(BaseObject):
    pass

class Band(BaseObject):
    pass

class Legend(BaseObject):
    pass

class SortItems(BaseObject):
    name = T.Unicode(default_value=None, allow_none=True)
    aggregate = T.Enum(['avg','sum','min','max','count'], default_value=True)
    reverse = T.Bool(False)

class Position(BaseObject):
    def __init__(self, name, **kwargs):
        kwargs.update(parse_shorthand(name))
        super(Position, self).__init__(self, **kwargs)

    name = T.Unicode('')
    type = T.Enum(['N','O','Q','T'], default_value=None, allow_none=True)
    aggregate = T.Enum(['avg','sum','median','min','max','count'], default_value=None, allow_none=True)
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'], default_value=None, allow_none=True)
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    scale = T.Instance(Scale, default_value=None, allow_none=True)
    axis = T.Instance(Axis, default_value=None, allow_none=True)
    band = T.Instance(Band, default_value=None, allow_none=True)
    sort = T.List(T.Instance(SortItems), defalut_value=None, allow_none=True)

class Index(BaseObject):
    def __init__(self, name, **kwargs):
        kwargs.update(parse_shorthand(name))
        super(Index, self).__init__(self, **kwargs)

    name = T.Unicode(default_value=None, allow_none=True)
    type = T.Enum(['N','O','Q','T'], default_value=None, allow_none=True)
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'], default_value=None, allow_none=True)
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    aggregate = T.Enum(['count'], default_value=None, allow_none=True)
    padding = T.CFloat(0.1)
    sort = T.List(T.Instance(SortItems), default_value=None, allow_none=True)
    axis = T.Instance(Axis, default_value=None, allow_none=True)
    height = T.CInt(150)

class Size(BaseObject):
    def __init__(self, name, **kwargs):
        kwargs.update(parse_shorthand(name))
        super(Size, self).__init__(self, **kwargs)

    name = T.Unicode(default_value=None, allow_none=True)
    type = T.Enum(['N','O','Q','T'], default_value=None, allow_none=True)
    aggregate = T.Enum(['avg','sum','median','min','max','count'], default_value=None, allow_none=True)
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'], default_value=None, allow_none=True)
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    scale = T.Instance(Scale, default_value=None, allow_none=True)
    legend = T.Instance(Legend, default_value=None, allow_none=True)
    value = T.CInt(30)
    sort = T.List(T.Instance(SortItems), default_value=None, allow_none=True)

class Color(BaseObject):
    def __init__(self, name, **kwargs):
        kwargs.update(parse_shorthand(name))
        super(Color, self).__init__(self, **kwargs)

    name = T.Unicode(default_value=None, allow_none=True)
    type = T.Enum(['N','O','Q','T'], default_value=None, allow_none=True)
    aggregate = T.Enum(['avg','sum','median','min','max','count'], default_value=None, allow_none=True)
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'], default_value=None, allow_none=True)
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    scale = T.Instance(Scale, default_value=None, allow_none=True)
    legend = T.Instance(Legend, default_value=None, allow_none=True)
    value = T.Unicode('#4682b4')
    opacity = T.Float(1.0)
    sort = T.List(T.Instance(SortItems), default_value=None, allow_none=True)

class Shape(BaseObject):
    def __init__(self, name, **kwargs):
        kwargs.update(parse_shorthand(name))
        super(Shape, self).__init__(self, **kwargs)

    name = T.Unicode(default_value=None, allow_none=True)
    type = T.Enum(['N','O','Q','T'], default_value=None, allow_none=True)
    aggregate = T.Enum(['count'], default_value=None, allow_none=True)
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'], default_value=None, allow_none=True)
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    legend = T.Instance(Legend, default_value=None, allow_none=True)
    value = T.Enum(['circle','square','cross','diamond','triangle-up','triangle-down'], default_value='circle')
    filled = T.Bool(False)
    sort = T.List(T.Instance(SortItems), default_value=None, allow_none=True)

class Encoding(BaseObject):

    x = T.Union([T.Instance(Position),T.Unicode()], default_value=None, allow_none=True)
    y = T.Union([T.Instance(Position),T.Unicode()], default_value=None, allow_none=True)
    row = T.Union([T.Instance(Index),T.Unicode()], default_value=None, allow_none=True)
    col = T.Union([T.Instance(Index),T.Unicode()], default_value=None, allow_none=True)
    size = T.Union([T.Instance(Size),T.Unicode()], default_value=None, allow_none=True)
    color = T.Union([T.Instance(Color),T.Unicode()], default_value=None, allow_none=True)
    shape = T.Union([T.Instance(Shape),T.Unicode()], default_value=None, allow_none=True)

    def _x_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.x = Position(new)

    def _y_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.y = Position(new)

    def _row_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.row = Index(new)

    def _col_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.col = Index(new)

    def _size_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.size = Size(new)

    def _color_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.color = Color(new)

    def _shape_changed(self, name, old, new):
        if isinstance(new, string_types):
            self.shape = Shape(new)



class Viz(BaseObject):

    marktype = T.Enum(['point','tick','bar','line',
                     'area','circle','square','text'], default_value='point')
    encoding = T.Instance(Encoding, default_value=None, allow_none=True)

    _data = T.Instance(Data, default_value=None, allow_none=True)
    data = T.Any(default_value=None, allow_none=True)
    
    def _data_changed(self, name, old, new):
        if not isinstance(new, pd.DataFrame):
            self.data = pd.DataFrame(new)
            return
        self._data = Data(data=new)

    def __init__(self, data, **kwargs):
        kwargs['data'] = data
        super(Viz,self).__init__(self, **kwargs)

    def to_dict(self):
        result = {}
        for k in self.traits():
            if k in self and k!='data':
                v = getattr(self, k)
                if k=='_data':
                    k='data'
                if isinstance(v, BaseObject):
                    result[k] = v.to_dict()
                else:
                    result[k] = v
        return result

    def encode(self, **kwargs):
        self.encoding = Encoding(**kwargs)
        return self

    def mark(self, mt):
        self.marktype = mt
        return self

    def mark_point(self):
        return self.mark('point')

    def mark_tick(self):
        return self.mark('tick')

    def mark_bar(self):
        return self.mark('bar')

    def mark_line(self):
        return self.mark('line')

    def mark_area(self):
        return self.mark('area')

    def mark_circle(self):
        return self.mark('circle')

    def mark_square(self):
        return self.mark('square')

    def mark_text(self):
        return self.mark('text')
