# The contents of this file are automatically generated
# 2018-02-12 15:12:33

from . import core
from altair.utils import parse_shorthand


class Color(core.MarkPropFieldDefWithCondition):
    """Color channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Color, self).__init__(**kwds)


class ColorValue(core.MarkPropValueDefWithCondition):
    """Color channel"""
    def __init__(self, value, *args, **kwargs):
        super(ColorValue, self).__init__(value=value, *args, **kwargs)


class Column(core.FacetFieldDef):
    """Column channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Column, self).__init__(**kwds)


class Detail(core.FieldDef):
    """Detail channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Detail, self).__init__(**kwds)


class Href(core.FieldDefWithCondition):
    """Href channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Href, self).__init__(**kwds)


class HrefValue(core.ValueDefWithCondition):
    """Href channel"""
    def __init__(self, value, *args, **kwargs):
        super(HrefValue, self).__init__(value=value, *args, **kwargs)


class Opacity(core.MarkPropFieldDefWithCondition):
    """Opacity channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Opacity, self).__init__(**kwds)


class OpacityValue(core.MarkPropValueDefWithCondition):
    """Opacity channel"""
    def __init__(self, value, *args, **kwargs):
        super(OpacityValue, self).__init__(value=value, *args, **kwargs)


class Order(core.OrderFieldDef):
    """Order channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Order, self).__init__(**kwds)


class Row(core.FacetFieldDef):
    """Row channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Row, self).__init__(**kwds)


class Shape(core.MarkPropFieldDefWithCondition):
    """Shape channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Shape, self).__init__(**kwds)


class ShapeValue(core.MarkPropValueDefWithCondition):
    """Shape channel"""
    def __init__(self, value, *args, **kwargs):
        super(ShapeValue, self).__init__(value=value, *args, **kwargs)


class Size(core.MarkPropFieldDefWithCondition):
    """Size channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Size, self).__init__(**kwds)


class SizeValue(core.MarkPropValueDefWithCondition):
    """Size channel"""
    def __init__(self, value, *args, **kwargs):
        super(SizeValue, self).__init__(value=value, *args, **kwargs)


class Text(core.TextFieldDefWithCondition):
    """Text channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Text, self).__init__(**kwds)


class TextValue(core.TextValueDefWithCondition):
    """Text channel"""
    def __init__(self, value, *args, **kwargs):
        super(TextValue, self).__init__(value=value, *args, **kwargs)


class Tooltip(core.TextFieldDefWithCondition):
    """Tooltip channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Tooltip, self).__init__(**kwds)


class TooltipValue(core.TextValueDefWithCondition):
    """Tooltip channel"""
    def __init__(self, value, *args, **kwargs):
        super(TooltipValue, self).__init__(value=value, *args, **kwargs)


class X(core.PositionFieldDef):
    """X channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(X, self).__init__(**kwds)


class XValue(core.ValueDef):
    """X channel"""
    def __init__(self, value, *args, **kwargs):
        super(XValue, self).__init__(value=value, *args, **kwargs)


class X2(core.FieldDef):
    """X2 channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(X2, self).__init__(**kwds)


class X2Value(core.ValueDef):
    """X2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(X2Value, self).__init__(value=value, *args, **kwargs)


class Y(core.PositionFieldDef):
    """Y channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Y, self).__init__(**kwds)


class YValue(core.ValueDef):
    """Y channel"""
    def __init__(self, value, *args, **kwargs):
        super(YValue, self).__init__(value=value, *args, **kwargs)


class Y2(core.FieldDef):
    """Y2 channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Y2, self).__init__(**kwds)


class Y2Value(core.ValueDef):
    """Y2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(Y2Value, self).__init__(value=value, *args, **kwargs)
