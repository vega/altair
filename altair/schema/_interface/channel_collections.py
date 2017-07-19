# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-68-g3ada237
# - date: 2017-07-19 11:12:59

import traitlets as T
from . import jstraitlets as jst
from . import schema


def _localname(name):
    return '.'.join(__name__.split('.')[:-1] + ['named_channels', name])


class Encoding(schema.Encoding):
    """Object for storing channel encodings

    Attributes
    ----------
    x: object
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    x2: object
        X2 coordinates for ranged `bar`, `rule`, `area`
    y2: object
        Y2 coordinates for ranged `bar`, `rule`, `area`
    detail: object
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    shape: object
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
    size: object
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: object
        Text of the `text` mark.
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
    order: object
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    row: object
        Vertical facets for trellis plots.
    column: object
        Horizontal facets for trellis plots.
    path: object
        Order of data points in line marks.
    label: object
        
    opacity: object
        Opacity of the marks – either can be a value or in a range.
    """
    channel_names = ['x', 'x2', 'y2', 'detail', 'shape', 'size', 'text', 'y', 'color', 'order', 'row', 'column', 'path', 'label', 'opacity']
    skip = ['channel_names']
    
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    label = jst.JSONInstance(_localname('Label'))
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')


class UnitEncoding(schema.UnitEncoding):
    """Object for storing channel encodings

    Attributes
    ----------
    x: object
        X coordinates for `point`, `circle`, `square`,
        `line`, `rule`, `text`, and `tick`
        (or to width and height for `bar` and `area` marks).
    x2: object
        X2 coordinates for ranged `bar`, `rule`, `area`
    y2: object
        Y2 coordinates for ranged `bar`, `rule`, `area`
    detail: object
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    shape: object
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
    size: object
        Size of the mark.
        - For `point`, `square` and `circle`
        – the symbol size, or pixel area of the mark.
        - For `bar` and `tick` – the bar and tick's size.
        - For `text` – the text's font size.
        - Size is currently unsupported for `line` and `area`.
    text: object
        Text of the `text` mark.
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
    order: object
        Layer order for non-stacked marks, or stack order for stacked
        marks.
    path: object
        Order of data points in line marks.
    label: object
        
    opacity: object
        Opacity of the marks – either can be a value or in a range.
    """
    channel_names = ['x', 'x2', 'y2', 'detail', 'shape', 'size', 'text', 'y', 'color', 'order', 'path', 'label', 'opacity']
    skip = ['channel_names']
    
    x = jst.JSONInstance(_localname('X'), help='X coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    x2 = jst.JSONInstance(_localname('X2'), help='X2 coordinates for ranged `bar`, `rule`, `area`')
    y2 = jst.JSONInstance(_localname('Y2'), help='Y2 coordinates for ranged `bar`, `rule`, `area`')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    shape = jst.JSONInstance(_localname('Shape'), help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONInstance(_localname('Size'), help='Size of the mark. - For `point`, `square` and `circle` – the [...]')
    text = jst.JSONInstance(_localname('Text'), help='Text of the `text` mark.')
    y = jst.JSONInstance(_localname('Y'), help='Y coordinates for `point`, `circle`, `square`, `line`, `rule`, [...]')
    color = jst.JSONInstance(_localname('Color'), help='Color of the marks – either fill or stroke color based on mark [...]')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Layer order for non-stacked marks, or stack order for stacked marks.')
    path = jst.JSONAnyOf([jst.JSONInstance(_localname('Path')), jst.JSONArray(jst.JSONInstance(_localname('Path')))], help='Order of data points in line marks.')
    label = jst.JSONInstance(_localname('Label'))
    opacity = jst.JSONInstance(_localname('Opacity'), help='Opacity of the marks – either can be a value or in a range.')


class Facet(schema.Facet):
    """Object for storing channel encodings

    Attributes
    ----------
    column: object
        
    row: object
        
    """
    channel_names = ['column', 'row']
    skip = ['channel_names']
    
    column = jst.JSONInstance(_localname('Column'))
    row = jst.JSONInstance(_localname('Row'))


