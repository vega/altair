# The contents of this file are automatically generated
# 2018-02-12 13:47:17

from altair.vegalite.v2 import schema
from altair.utils import parse_shorthand


class Color(schema.MarkPropFieldDefWithCondition):
    """Color channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Color, self).__init__(**kwds)


class ColorValue(schema.MarkPropValueDefWithCondition):
    """Color channel"""
    def __init__(self, value, *args, **kwargs):
        super(ColorValue, self).__init__(value=value, *args, **kwargs)


class Column(schema.FacetFieldDef):
    """Column channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Column, self).__init__(**kwds)


class Detail(schema.FieldDef):
    """Detail channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Detail, self).__init__(**kwds)


class Href(schema.FieldDefWithCondition):
    """Href channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Href, self).__init__(**kwds)


class HrefValue(schema.ValueDefWithCondition):
    """Href channel"""
    def __init__(self, value, *args, **kwargs):
        super(HrefValue, self).__init__(value=value, *args, **kwargs)


class Opacity(schema.MarkPropFieldDefWithCondition):
    """Opacity channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Opacity, self).__init__(**kwds)


class OpacityValue(schema.MarkPropValueDefWithCondition):
    """Opacity channel"""
    def __init__(self, value, *args, **kwargs):
        super(OpacityValue, self).__init__(value=value, *args, **kwargs)


class Order(schema.OrderFieldDef):
    """Order channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Order, self).__init__(**kwds)


class Row(schema.FacetFieldDef):
    """Row channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Row, self).__init__(**kwds)


class Shape(schema.MarkPropFieldDefWithCondition):
    """Shape channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Shape, self).__init__(**kwds)


class ShapeValue(schema.MarkPropValueDefWithCondition):
    """Shape channel"""
    def __init__(self, value, *args, **kwargs):
        super(ShapeValue, self).__init__(value=value, *args, **kwargs)


class Size(schema.MarkPropFieldDefWithCondition):
    """Size channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Size, self).__init__(**kwds)


class SizeValue(schema.MarkPropValueDefWithCondition):
    """Size channel"""
    def __init__(self, value, *args, **kwargs):
        super(SizeValue, self).__init__(value=value, *args, **kwargs)


class Text(schema.TextFieldDefWithCondition):
    """Text channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Text, self).__init__(**kwds)


class TextValue(schema.TextValueDefWithCondition):
    """Text channel"""
    def __init__(self, value, *args, **kwargs):
        super(TextValue, self).__init__(value=value, *args, **kwargs)


class Tooltip(schema.TextFieldDefWithCondition):
    """Tooltip channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Tooltip, self).__init__(**kwds)


class TooltipValue(schema.TextValueDefWithCondition):
    """Tooltip channel"""
    def __init__(self, value, *args, **kwargs):
        super(TooltipValue, self).__init__(value=value, *args, **kwargs)


class X(schema.PositionFieldDef):
    """X channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(X, self).__init__(**kwds)


class XValue(schema.ValueDef):
    """X channel"""
    def __init__(self, value, *args, **kwargs):
        super(XValue, self).__init__(value=value, *args, **kwargs)


class X2(schema.FieldDef):
    """X2 channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(X2, self).__init__(**kwds)


class X2Value(schema.ValueDef):
    """X2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(X2Value, self).__init__(value=value, *args, **kwargs)


class Y(schema.PositionFieldDef):
    """Y channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Y, self).__init__(**kwds)


class YValue(schema.ValueDef):
    """Y channel"""
    def __init__(self, value, *args, **kwargs):
        super(YValue, self).__init__(value=value, *args, **kwargs)


class Y2(schema.FieldDef):
    """Y2 channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super(Y2, self).__init__(**kwds)


class Y2Value(schema.ValueDef):
    """Y2 channel"""
    def __init__(self, value, *args, **kwargs):
        super(Y2Value, self).__init__(value=value, *args, **kwargs)
