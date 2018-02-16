# The contents of this file are automatically generated
# 2018-02-16 06:27:48

from . import core
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand, parse_shorthand_plus_data


class Color(core.MarkPropFieldDefWithCondition):
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


class ColorValue(core.MarkPropValueDefWithCondition):
    """Color channel"""
    def __init__(self, value, *args, **kwargs):
        super(ColorValue, self).__init__(value=value, *args, **kwargs)


class Column(core.FacetFieldDef):
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


class Href(core.FieldDefWithCondition):
    """Href channel"""
    def __init__(self, field, **kwargs):
        super(Href, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Href, self).to_dict(validate=validate, ignore=ignore, context=context)


class HrefValue(core.ValueDefWithCondition):
    """Href channel"""
    def __init__(self, value, *args, **kwargs):
        super(HrefValue, self).__init__(value=value, *args, **kwargs)


class Opacity(core.MarkPropFieldDefWithCondition):
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


class OpacityValue(core.MarkPropValueDefWithCondition):
    """Opacity channel"""
    def __init__(self, value, *args, **kwargs):
        super(OpacityValue, self).__init__(value=value, *args, **kwargs)


class Order(core.OrderFieldDef):
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


class Row(core.FacetFieldDef):
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


class Shape(core.MarkPropFieldDefWithCondition):
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


class ShapeValue(core.MarkPropValueDefWithCondition):
    """Shape channel"""
    def __init__(self, value, *args, **kwargs):
        super(ShapeValue, self).__init__(value=value, *args, **kwargs)


class Size(core.MarkPropFieldDefWithCondition):
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


class SizeValue(core.MarkPropValueDefWithCondition):
    """Size channel"""
    def __init__(self, value, *args, **kwargs):
        super(SizeValue, self).__init__(value=value, *args, **kwargs)


class Text(core.TextFieldDefWithCondition):
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


class TextValue(core.TextValueDefWithCondition):
    """Text channel"""
    def __init__(self, value, *args, **kwargs):
        super(TextValue, self).__init__(value=value, *args, **kwargs)


class Tooltip(core.TextFieldDefWithCondition):
    """Tooltip channel"""
    def __init__(self, field, **kwargs):
        super(Tooltip, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Tooltip, self).to_dict(validate=validate, ignore=ignore, context=context)


class TooltipValue(core.TextValueDefWithCondition):
    """Tooltip channel"""
    def __init__(self, value, *args, **kwargs):
        super(TooltipValue, self).__init__(value=value, *args, **kwargs)


class X(core.PositionFieldDef):
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


class XValue(core.ValueDef):
    """X channel"""
    def __init__(self, value, *args, **kwargs):
        super(XValue, self).__init__(value=value, *args, **kwargs)


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


class X2Value(core.ValueDef):
    """X2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(X2Value, self).__init__(value=value, *args, **kwargs)


class Y(core.PositionFieldDef):
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


class YValue(core.ValueDef):
    """Y channel"""
    def __init__(self, value, *args, **kwargs):
        super(YValue, self).__init__(value=value, *args, **kwargs)


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


class Y2Value(core.ValueDef):
    """Y2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(Y2Value, self).__init__(value=value, *args, **kwargs)
