# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-72-ge93cbd1
# - date: 2017-07-31 13:54:43

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
    color: object
        Color of the marks – either fill or stroke color based on mark
        type.
        (By default, fill color for `area`, `bar`, `tick`, `text`,
        `circle`, and `square` /
        stroke color for `line` and `point`.)
    order: object
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    path: object
        Order of data points in line marks.
    size: object
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: object
        Text of the `text` mark.
    column: object
        Horizontal facets for trellis plots.
    row: object
        Vertical facets for trellis plots.
    label: object
        
    y2: object
        Y2 coordinates for ranged `bar`, `rule`, `area`
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
    y: object
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    detail: object
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['x2', 'color', 'order', 'path', 'size', 'text', 'column', 'row', 'label', 'y2', 'opacity', 'shape', 'x', 'y', 'detail']
    
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')
    label = jst.JSONInstance(_localname('Label'))
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')


class UnitEncoding(schema.UnitEncoding):
    """Object for storing channel encodings

    Attributes
    ----------
    x2: object
        X2 coordinates for ranged `bar`, `rule`, `area`
    color: object
        Color of the marks – either fill or stroke color based on mark
        type.
        (By default, fill color for `area`, `bar`, `tick`, `text`,
        `circle`, and `square` /
        stroke color for `line` and `point`.)
    order: object
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    path: object
        Order of data points in line marks.
    size: object
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: object
        Text of the `text` mark.
    label: object
        
    y2: object
        Y2 coordinates for ranged `bar`, `rule`, `area`
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
    y: object
        Y coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    detail: object
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['x2', 'color', 'order', 'path', 'size', 'text', 'label', 'y2', 'opacity', 'shape', 'x', 'y', 'detail']
    
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    label = jst.JSONInstance(_localname('Label'))
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')


class Facet(schema.Facet):
    """Object for storing channel encodings

    Attributes
    ----------
    column: object
        
    row: object
        
    """
    _skip_on_export = ['channel_names']
    channel_names = ['column', 'row']
    
    column = jst.JSONInstance(_localname('Column'))
    row = jst.JSONInstance(_localname('Row'))


