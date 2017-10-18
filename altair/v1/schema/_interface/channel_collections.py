# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-157-g91fdb9b
# - date: 2017-10-17 17:01:04

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
    column: Column
        Horizontal facets for trellis plots.
    detail: AnyOf([Detail, Array(Detail)])
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    label: Label
        
    opacity: Opacity
        Opacity of the marks – either can be a value or in a range.
    order: AnyOf([Order, Array(Order)])
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    path: AnyOf([Path, Array(Path)])
        Order of data points in line marks.
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
    x: X
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    x2: X2
        X2 coordinates for ranged `bar`, `rule`, `area`
    y: Y
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    y2: Y2
        Y2 coordinates for ranged `bar`, `rule`, `area`
    """
    _skip_on_export = ['channel_names']
    channel_names = ['color', 'column', 'detail', 'label', 'opacity', 'order', 'path', 'row', 'shape', 'size', 'text', 'x', 'x2', 'y', 'y2']
    
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    label = jst.JSONInstance(_localname('Label'))
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')


class UnitEncoding(schema.UnitEncoding):
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
    label: Label
        
    opacity: Opacity
        Opacity of the marks – either can be a value or in a range.
    order: AnyOf([Order, Array(Order)])
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    path: AnyOf([Path, Array(Path)])
        Order of data points in line marks.
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
    x: X
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    x2: X2
        X2 coordinates for ranged `bar`, `rule`, `area`
    y: Y
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    y2: Y2
        Y2 coordinates for ranged `bar`, `rule`, `area`
    """
    _skip_on_export = ['channel_names']
    channel_names = ['color', 'detail', 'label', 'opacity', 'order', 'path', 'shape', 'size', 'text', 'x', 'x2', 'y', 'y2']
    
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    label = jst.JSONInstance(_localname('Label'))
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')


class Facet(schema.Facet):
    """Object for storing channel encodings

    Attributes
    ----------
    column: Column
        
    row: Row
        
    """
    _skip_on_export = ['channel_names']
    channel_names = ['column', 'row']
    
    column = jst.JSONInstance(_localname('Column'))
    row = jst.JSONInstance(_localname('Row'))


