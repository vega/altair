try:
    import traitlets as T
except ImportError:
    from IPython.utils import traitlets as T
    


def parse_shorthand(sh):
    result = {}
    a= sh.split(':')
    if len(a)==2:
        result['type'] = a[1]
        b = a[0]
    elif len(a)==1:
        b = a[0]
    else:
        raise ValueError('Not valid shorthand')
    if b.endswith(')'):
        agg, name = b[0:-1].split('(')
    else:
        agg, name = None, b
    if agg is not None:
        result['aggregate']=agg
    if name is not None:
        result['name']=name
    return result


class Data(T.HasTraits):
                    
    formatType = T.Enum(['json','csv'], default_value='json')
    url = T.Unicode()
    data = T.List([])

class Scale(T.HasTraits):
    pass

class Axis(T.HasTraits):
    pass

class Band(T.HasTraits):
    pass

class Legend(T.HasTraits):
    pass

class SortItems(T.HasTraits):
    name = T.Unicode()
    aggregate = T.Enum(['avg','sum','min','max','count'])
    reverse = T.Bool(False)
    
class Position(T.HasTraits):
    
    name = T.Unicode('')
    type = T.Enum(['N','O','Q','T'])
    aggregate = T.Enum(['avg','sum','median','min','max','count'])
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'])
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    scale = T.Instance(Scale)
    axis = T.Instance(Axis)
    band = T.Instance(Band)
    sort = T.List(T.Instance(SortItems))

class Index(T.HasTraits):
    
    name = T.Unicode('')
    type = T.Enum(['N','O','Q','T'])
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'])
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    aggregate = T.Enum(['count'])
    padding = T.CFloat(0.1)
    sort = T.List(T.Instance(SortItems))
    axis = T.Instance(Axis)
    height = T.CInt(150)

class Size(T.HasTraits):
    name = T.Unicode('')
    type = T.Enum(['N','O','Q','T'])
    aggregate = T.Enum(['avg','sum','median','min','max','count'])
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'])
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    scale = T.Instance(Scale)
    legend = T.Instance(Legend)
    value = T.CInt(30)
    sort = T.List(T.Instance(SortItems))

class Color(T.HasTraits):
    name = T.Unicode('')
    type = T.Enum(['N','O','Q','T'])
    aggregate = T.Enum(['avg','sum','median','min','max','count'])
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'])
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    scale = T.Instance(Scale)
    legend = T.Instance(Legend)
    value = T.Unicode('#4682b4')
    opacity = T.Float(1.0)
    sort = T.List(T.Instance(SortItems))

class Shape(T.HasTraits):
    name = T.Unicode('')
    type = T.Enum(['N','O','Q','T'])
    aggregate = T.Enum(['count'])
    timeUnit = T.Enum(['year','month','day','date','hours','minutes','seconds'])
    bin = T.Union([T.Bool(),T.Int()], default_value=False)
    legend = T.Instance(Legend)
    value = T.Enum(['circle','square','cross','diamond','triangle-up','triangle-down'], default_value='circle')
    filled = T.Bool(False)
    sort = T.List(T.Instance(SortItems))
    
class Encoding(T.HasTraits):
    
    x = T.Union([T.Instance(Position),T.Unicode()])
    y = T.Union([T.Instance(Position),T.Unicode()])
    row = T.Union([T.Instance(Index),T.Unicode()])
    col = T.Union([T.Instance(Index),T.Unicode()])
    size = T.Instance(Size)
    color = T.Instance(Color)
    shape = T.Instance(Shape)
                
    def _x_changed(self, name, old, new):
        if isinstance(new, unicode):
            result = parse_shorthand(new)
            self.x = Position(**result)

    def _y_changed(self, name, old, new):
        if isinstance(new, unicode):
            result = parse_shorthand(new)
            self.y = Position(**result)

    def _row_changed(self, name, old, new):
        if isinstance(new, unicode):
            result = parse_shorthand(new)
            self.row = Index(**result)

    def _col_changed(self, name, old, new):
        if isinstance(new, unicode):
            result = parse_shorthand(new)
            self.col = Index(**result)


class Viz(T.HasTraits):
    
    marktype = T.Enum(['point','tick','bar','line',
                     'area','circle','square','text'], default_value='point')
    _data = T.Instance(Data, allow_none=True)
    data = T.Any()
    encoding = T.Instance(Encoding)
    # _encoding = T.Union([T.Instance(Encoding),T.Dict])
    
    # def __encoding_changed(self, name, old, new):
    #     if isinstance(new, dict):
    #         self._encoding = Encoding(**new)
    
    def __init__(self, data, **kwargs):
        kwargs['data'] = data
        super(Viz,self).__init__(self, **kwargs)
    
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

    def mark_live(self):
        return self.mark('area')

    def mark_circle(self):
        return self.mark('circle')

    def mark_square(self):
        return self.mark('square')

    def mark_text(self):
        return self.mark('text')
