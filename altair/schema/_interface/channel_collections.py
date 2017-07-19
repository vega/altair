# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-69-ga13043b
# - date: 2017-07-19 14:16:39

import traitlets as T
from . import jstraitlets as jst
from . import schema


def _localname(name):
    return '.'.join(__name__.split('.')[:-1] + ['named_channels', name])


class Encoding(schema.Encoding):
    """Object for storing channel encodings

    Attributes
    ----------
    x2: object
        X2 coordinates for ranged `bar`, `rule`, `area`
    y2: object
        Y2 coordinates for ranged `bar`, `rule`, `area`
    column: object
        Horizontal facets for trellis plots.
    x: object
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    label: object
        
    detail: object
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    opacity: object
        Opacity of the marks – either can be a value or in a range.
    shape: object
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
    text: object
        Text of the `text` mark.
    size: object
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    path: object
        Order of data points in line marks.
    row: object
        Vertical facets for trellis plots.
    order: object
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    y: object
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    color: object
        Color of the marks – either fill or stroke color based on mark
        type.
        (By default, fill color for `area`, `bar`, `tick`, `text`,
        `circle`, and `square` /
        stroke color for `line` and `point`.)
    """
    channel_names = ['x2', 'y2', 'column', 'x', 'label', 'detail', 'opacity', 'shape', 'text', 'size', 'path', 'row', 'order', 'y', 'color']
    skip = ['channel_names']
    
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    label = jst.JSONInstance(_localname('Label'))
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')


class UnitEncoding(schema.UnitEncoding):
    """Object for storing channel encodings

    Attributes
    ----------
    x2: object
        X2 coordinates for ranged `bar`, `rule`, `area`
    y2: object
        Y2 coordinates for ranged `bar`, `rule`, `area`
    label: object
        
    detail: object
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    opacity: object
        Opacity of the marks – either can be a value or in a range.
    shape: object
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
    x: object
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    size: object
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: object
        Text of the `text` mark.
    order: object
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    y: object
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    color: object
        Color of the marks – either fill or stroke color based on mark
        type.
        (By default, fill color for `area`, `bar`, `tick`, `text`,
        `circle`, and `square` /
        stroke color for `line` and `point`.)
    path: object
        Order of data points in line marks.
    """
    channel_names = ['x2', 'y2', 'label', 'detail', 'opacity', 'shape', 'x', 'size', 'text', 'order', 'y', 'color', 'path']
    skip = ['channel_names']
    
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')
    label = jst.JSONInstance(_localname('Label'))
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')


class Facet(schema.Facet):
    """Object for storing channel encodings

    Attributes
    ----------
    row: object
        
    column: object
        
    """
    channel_names = ['row', 'column']
    skip = ['channel_names']
    
    row = jst.JSONInstance(_localname('Row'))
    column = jst.JSONInstance(_localname('Column'))


