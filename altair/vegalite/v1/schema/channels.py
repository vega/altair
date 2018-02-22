# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# 2018-02-22 11:15

from . import core
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand, parse_shorthand_plus_data


class Row(core.PositionChannelDef):
    """Row channel"""
    def __init__(self, field, **kwargs):
        super(Row, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Row, self).to_dict(validate=validate, ignore=ignore, context=context)


class Column(core.PositionChannelDef):
    """Column channel"""
    def __init__(self, field, **kwargs):
        super(Column, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Column, self).to_dict(validate=validate, ignore=ignore, context=context)


class X(core.PositionChannelDef):
    """X channel"""
    def __init__(self, field, **kwargs):
        super(X, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X, self).to_dict(validate=validate, ignore=ignore, context=context)


class Y(core.PositionChannelDef):
    """Y channel"""
    def __init__(self, field, **kwargs):
        super(Y, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y, self).to_dict(validate=validate, ignore=ignore, context=context)


class X2(core.FieldDef):
    """X2 channel"""
    def __init__(self, field, **kwargs):
        super(X2, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X2, self).to_dict(validate=validate, ignore=ignore, context=context)


class Y2(core.FieldDef):
    """Y2 channel"""
    def __init__(self, field, **kwargs):
        super(Y2, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y2, self).to_dict(validate=validate, ignore=ignore, context=context)


class Color(core.ChannelDefWithLegend):
    """Color channel"""
    def __init__(self, field, **kwargs):
        super(Color, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Color, self).to_dict(validate=validate, ignore=ignore, context=context)


class Opacity(core.ChannelDefWithLegend):
    """Opacity channel"""
    def __init__(self, field, **kwargs):
        super(Opacity, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Opacity, self).to_dict(validate=validate, ignore=ignore, context=context)


class Size(core.ChannelDefWithLegend):
    """Size channel"""
    def __init__(self, field, **kwargs):
        super(Size, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Size, self).to_dict(validate=validate, ignore=ignore, context=context)


class Shape(core.ChannelDefWithLegend):
    """Shape channel"""
    def __init__(self, field, **kwargs):
        super(Shape, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Shape, self).to_dict(validate=validate, ignore=ignore, context=context)


class Detail(core.FieldDef):
    """Detail channel"""
    def __init__(self, field, **kwargs):
        super(Detail, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Detail, self).to_dict(validate=validate, ignore=ignore, context=context)


class Text(core.FieldDef):
    """Text channel"""
    def __init__(self, field, **kwargs):
        super(Text, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Text, self).to_dict(validate=validate, ignore=ignore, context=context)


class Label(core.FieldDef):
    """Label channel"""
    def __init__(self, field, **kwargs):
        super(Label, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Label, self).to_dict(validate=validate, ignore=ignore, context=context)


class Path(core.OrderChannelDef):
    """Path channel"""
    def __init__(self, field, **kwargs):
        super(Path, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Path, self).to_dict(validate=validate, ignore=ignore, context=context)


class Order(core.OrderChannelDef):
    """Order channel"""
    def __init__(self, field, **kwargs):
        super(Order, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Order, self).to_dict(validate=validate, ignore=ignore, context=context)
