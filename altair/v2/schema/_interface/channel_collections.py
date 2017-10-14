# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-120-g7d42848
# - date: 2017-10-14 14:01:07

import traitlets as T
from . import jstraitlets as jst
from . import schema


def _localname(name):
    return '.'.join(__name__.split('.')[:-1] + ['named_channels', name])


class Encoding(schema.Encoding):
    """Object for storing channel encodings

    Attributes
    ----------
    color: Color
        Color of the marks – either fill or stroke color based on mark
        type.
        (By default, fill color for `area`, `bar`, `tick`, `text`,
        `circle`, and `square` /
        stroke color for `line` and `point`.)
    detail: AnyOf([Detail, Array(Detail)])
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    opacity: Opacity
        Opacity of the marks – either can be a value or a range.
    order: AnyOf([Order, Array(Order)])
        stack order for stacked marks or order of data points in line
        marks.
    shape: Shape
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
    size: Size
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: Text
        Text of the `text` mark.
    tooltip: Tooltip
        The tooltip text to show upon mouse hover.
    x: AnyOf([X, NumberValueDef])
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    x2: AnyOf([X2, NumberValueDef])
        X2 coordinates for ranged `bar`, `rule`, `area`.
    y: AnyOf([Y, NumberValueDef])
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    y2: AnyOf([Y2, NumberValueDef])
        Y2 coordinates for ranged `bar`, `rule`, `area`.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['color', 'detail', 'opacity', 'order', 'shape', 'size', 'text', 'tooltip', 'x', 'x2', 'y', 'y2']
    
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or a range.')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='stack order for stacked marks or order of data points in line marks.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    tooltip = jst.JSONInstance(_localname('Tooltip'), help='The tooltip text to show upon mouse hover.')
    x = jst.JSONAnyOf([jst.JSONInstance(_localname('X')), jst.JSONInstance(_localname('NumberValueDef'))], help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    x2 = jst.JSONAnyOf([jst.JSONInstance(_localname('X2')), jst.JSONInstance(_localname('NumberValueDef'))], help='X2 coordinates for ranged `bar`, `rule`, `area`.')
    y = jst.JSONAnyOf([jst.JSONInstance(_localname('Y')), jst.JSONInstance(_localname('NumberValueDef'))], help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    y2 = jst.JSONAnyOf([jst.JSONInstance(_localname('Y2')), jst.JSONInstance(_localname('NumberValueDef'))], help='Y2 coordinates for ranged `bar`, `rule`, `area`.')


class EncodingWithFacet(schema.EncodingWithFacet):
    """Object for storing channel encodings

    Attributes
    ----------
    color: Color
        Color of the marks – either fill or stroke color based on mark
        type.
        (By default, fill color for `area`, `bar`, `tick`, `text`,
        `circle`, and `square` /
        stroke color for `line` and `point`.)
    column: Column
        Horizontal facets for trellis plots.
    detail: AnyOf([Detail, Array(Detail)])
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    opacity: Opacity
        Opacity of the marks – either can be a value or a range.
    order: AnyOf([Order, Array(Order)])
        stack order for stacked marks or order of data points in line
        marks.
    row: Row
        Vertical facets for trellis plots.
    shape: Shape
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
    size: Size
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: Text
        Text of the `text` mark.
    tooltip: Tooltip
        The tooltip text to show upon mouse hover.
    x: AnyOf([X, NumberValueDef])
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    x2: AnyOf([X2, NumberValueDef])
        X2 coordinates for ranged `bar`, `rule`, `area`.
    y: AnyOf([Y, NumberValueDef])
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    y2: AnyOf([Y2, NumberValueDef])
        Y2 coordinates for ranged `bar`, `rule`, `area`.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['color', 'column', 'detail', 'opacity', 'order', 'row', 'shape', 'size', 'text', 'tooltip', 'x', 'x2', 'y', 'y2']
    
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or a range.')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='stack order for stacked marks or order of data points in line marks.')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    tooltip = jst.JSONInstance(_localname('Tooltip'), help='The tooltip text to show upon mouse hover.')
    x = jst.JSONAnyOf([jst.JSONInstance(_localname('X')), jst.JSONInstance(_localname('NumberValueDef'))], help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    x2 = jst.JSONAnyOf([jst.JSONInstance(_localname('X2')), jst.JSONInstance(_localname('NumberValueDef'))], help='X2 coordinates for ranged `bar`, `rule`, `area`.')
    y = jst.JSONAnyOf([jst.JSONInstance(_localname('Y')), jst.JSONInstance(_localname('NumberValueDef'))], help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    y2 = jst.JSONAnyOf([jst.JSONInstance(_localname('Y2')), jst.JSONInstance(_localname('NumberValueDef'))], help='Y2 coordinates for ranged `bar`, `rule`, `area`.')


class Facet(schema.Facet):
    """Object for storing channel encodings

    Attributes
    ----------
    column: Column
        Horizontal facets for trellis plots.
    row: Row
        Vertical facets for trellis plots.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['column', 'row']
    
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')


