# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import SchemaBase, Undefined

import os
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, 'vega-lite-schema.json')) as f:
        return json.load(f)


class VegaLiteSchema(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return VegaLiteSchema.__subclasses__()


class Root(VegaLiteSchema):
    """Root schema wrapper
    
    anyOf(TopLevelFacetedUnitSpec, TopLevelFacetSpec, TopLevelLayerSpec, TopLevelRepeatSpec, 
    TopLevelVConcatSpec, TopLevelHConcatSpec)
    """
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)


class Aggregate(VegaLiteSchema):
    """Aggregate schema wrapper
    
    enum('argmax', 'argmin', 'average', 'count', 'distinct', 'max', 'mean', 'median', 'min', 
    'missing', 'q1', 'q3', 'ci0', 'ci1', 'stderr', 'stdev', 'stdevp', 'sum', 'valid', 'values', 
    'variance', 'variancep')
    """
    _schema = {'$ref': '#/definitions/Aggregate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Aggregate, self).__init__(*args)


class AggregateOp(VegaLiteSchema):
    """AggregateOp schema wrapper
    
    enum('argmax', 'argmin', 'average', 'count', 'distinct', 'max', 'mean', 'median', 'min', 
    'missing', 'q1', 'q3', 'ci0', 'ci1', 'stderr', 'stdev', 'stdevp', 'sum', 'valid', 'values', 
    'variance', 'variancep')
    """
    _schema = {'$ref': '#/definitions/AggregateOp'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AggregateOp, self).__init__(*args)


class AggregateTransform(VegaLiteSchema):
    """AggregateTransform schema wrapper
    
    Mapping(required=[aggregate])
    
    Attributes
    ----------
    aggregate : List(AggregatedFieldDef)
        Array of objects that define fields to aggregate.
    groupby : List(string)
        The data fields to group by. If not specified, a single group containing all data 
        objects will be used.
    """
    _schema = {'$ref': '#/definitions/AggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, groupby=Undefined, **kwds):
        super(AggregateTransform, self).__init__(aggregate=aggregate, groupby=groupby, **kwds)


class AggregatedFieldDef(VegaLiteSchema):
    """AggregatedFieldDef schema wrapper
    
    Mapping(required=[op, field, as])
    
    Attributes
    ----------
    field : string
        The data field for which to compute aggregate function.
    op : AggregateOp
        The aggregation operations to apply to the fields, such as sum, average or count. 
        See the [full list of supported aggregation 
        operations](https://vega.github.io/vega-lite/docs/aggregate.html#ops) for more 
        information.
    """
    _schema = {'$ref': '#/definitions/AggregatedFieldDef'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, op=Undefined, **kwds):
        super(AggregatedFieldDef, self).__init__(field=field, op=op, **kwds)


class Anchor(VegaLiteSchema):
    """Anchor schema wrapper
    
    enum('start', 'middle', 'end')
    """
    _schema = {'$ref': '#/definitions/Anchor'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Anchor, self).__init__(*args)


class AnyMark(VegaLiteSchema):
    """AnyMark schema wrapper
    
    anyOf(Mark, MarkDef)
    """
    _schema = {'$ref': '#/definitions/AnyMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(AnyMark, self).__init__(*args, **kwds)


class AutoSizeParams(VegaLiteSchema):
    """AutoSizeParams schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    contains : enum('content', 'padding')
        Determines how size calculation should be performed, one of `"content"` or 
        `"padding"`. The default setting (`"content"`) interprets the width and height 
        settings as the data rectangle (plotting) dimensions, to which padding is then 
        added. In contrast, the `"padding"` setting includes the padding within the view 
        size calculations, such that the width and height settings indicate the **total** 
        intended size of the view.  __Default value__: `"content"`
    resize : boolean
        A boolean flag indicating if autosize layout should be re-calculated on every view 
        update.  __Default value__: `false`
    type : AutosizeType
        The sizing format type. One of `"pad"`, `"fit"` or `"none"`. See the [autosize 
        type](https://vega.github.io/vega-lite/docs/size.html#autosize) documentation for 
        descriptions of each.  __Default value__: `"pad"`
    """
    _schema = {'$ref': '#/definitions/AutoSizeParams'}
    _rootschema = Root._schema

    def __init__(self, contains=Undefined, resize=Undefined, type=Undefined, **kwds):
        super(AutoSizeParams, self).__init__(contains=contains, resize=resize, type=type, **kwds)


class AutosizeType(VegaLiteSchema):
    """AutosizeType schema wrapper
    
    enum('pad', 'fit', 'none')
    """
    _schema = {'$ref': '#/definitions/AutosizeType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AutosizeType, self).__init__(*args)


class Axis(VegaLiteSchema):
    """Axis schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as 
        part of the axis.  __Default value:__ `true`
    format : string
        The formatting pattern for labels. This is D3's [number format 
        pattern](https://github.com/d3/d3-format#locale_format) for quantitative fields and 
        D3's [time format pattern](https://github.com/d3/d3-time-format#locale_format) for 
        time field.  See the [format documentation](format.html) for more information.  
        __Default value:__  derived from [numberFormat](config.html#format) config for 
        quantitative fields and from [timeFormat](config.html#format) config for temporal 
        fields.
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis  
        __Default value:__ `true` for [continuous scales](scale.html#continuous) that are 
        not binned; otherwise, `false`.
    labelAngle : float
        The rotation angle of the axis labels.  __Default value:__ `-90` for nominal and 
        ordinal fields; `0` otherwise.
    labelBound : anyOf(boolean, float)
        Indicates if labels should be hidden if they exceed the axis range. If `false `(the 
        default) no bounds overlap analysis is performed. If `true`, labels will be hidden 
        if they exceed the axis range by more than 1 pixel. If this property is a number, it
         specifies the pixel tolerance: the maximum amount by which a label bounding box may
         exceed the axis range.  __Default value:__ `false`.
    labelFlush : anyOf(boolean, float)
        Indicates if the first and last axis labels should be aligned flush with the scale 
        range. Flush alignment for a horizontal axis will left-align the first label and 
        right-align the last label. For vertical axes, bottom and top text baselines are 
        applied instead. If this property is a number, it also indicates the number of 
        pixels by which to offset the first and last labels; for example, a value of 2 will 
        flush-align the first and last labels and also push them 2 pixels outward from the 
        center of the axis. The additional adjustment can sometimes help the labels better 
        visually group with corresponding axis ticks.  __Default value:__ `true` for axis of
         a continuous x-scale. Otherwise, `false`.
    labelOverlap : anyOf(boolean, enum('parity'), enum('greedy'))
        The strategy to use for resolving overlap of axis labels. If `false` (the default), 
        no overlap reduction is attempted. If set to `true` or `"parity"`, a strategy of 
        removing every other label is used (this works well for standard linear axes). If 
        set to `"greedy"`, a linear scan of the labels is performed, removing any labels 
        that overlaps with the last visible label (this often works better for log-scaled 
        axes).  __Default value:__ `true` for non-nominal fields with non-log scales; 
        `"greedy"` for log scales; otherwise `false`.
    labelPadding : float
        The padding, in pixels, between axis and text labels.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.  
        __Default value:__  `true`.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines 
        a maximum offset value for axis titles.  __Default value:__ `undefined`.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines 
        a minimum offset value for axis titles.  __Default value:__ `30` for y-axis; 
        `undefined` for x-axis.
    offset : float
        The offset, in pixels, by which to displace the axis from the edge of the enclosing 
        group or data rectangle.  __Default value:__ derived from the [axis 
        config](config.html#facet-scale-config)'s `offset` (`0` by default)
    orient : AxisOrient
        The orientation of the axis. One of `"top"`, `"bottom"`, `"left"` or `"right"`. The 
        orientation can be used to further specialize the axis type (e.g., a y axis oriented
         for the right edge of the chart).  __Default value:__ `"bottom"` for x-axes and 
        `"left"` for y-axes.
    position : float
        The anchor position of the axis in pixels. For x-axis with top or bottom 
        orientation, this sets the axis group x coordinate. For y-axis with left or right 
        orientation, this sets the axis group y coordinate.  __Default value__: `0`
    tickCount : float
        A desired number of ticks, for axes visualizing quantitative scales. The resulting 
        number may be different so that values are "nice" (multiples of 2, 5, 10) and lie 
        within the underlying scale's range.
    tickSize : float
        The size in pixels of axis ticks.
    ticks : boolean
        Boolean value that determines whether the axis should include ticks.
    title : anyOf(string, None)
        A title for the field. If `null`, the title will be removed.  __Default value:__  
        derived from the field's name and transformation function (`aggregate`, `bin` and 
        `timeUnit`).  If the field has an aggregate function, the function is displayed as a
         part of the title (e.g., `"Sum of Profit"`). If the field is binned or has a time 
        unit applied, the applied function will be denoted in parentheses (e.g., `"Profit 
        (binned)"`, `"Transaction Date (year-month)"`).  Otherwise, the title is simply the 
        field name.  __Note__: You can customize the default field title format by providing
         the [`fieldTitle` property in the [config](config.html) or [`fieldTitle` function 
        via the `compile` function's options](compile.html#field-title).
    titleMaxLength : float
        Max length for axis title if the title is automatically generated from the field's 
        description.
    titlePadding : float
        The padding, in pixels, between title and axis.
    values : anyOf(List(float), List(DateTime))
        Explicitly set the visible axis tick values.
    zindex : float
        A non-positive integer indicating z-index of the axis. If zindex is 0, axes should 
        be drawn behind all chart elements. To put them in front, use `"zindex = 1"`.  
        __Default value:__ `1` (in front of the marks) for actual axis and `0` (behind the 
        marks) for grids.
    """
    _schema = {'$ref': '#/definitions/Axis'}
    _rootschema = Root._schema

    def __init__(self, domain=Undefined, format=Undefined, grid=Undefined, labelAngle=Undefined,
                 labelBound=Undefined, labelFlush=Undefined, labelOverlap=Undefined,
                 labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined,
                 offset=Undefined, orient=Undefined, position=Undefined, tickCount=Undefined,
                 tickSize=Undefined, ticks=Undefined, title=Undefined, titleMaxLength=Undefined,
                 titlePadding=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(Axis, self).__init__(domain=domain, format=format, grid=grid, labelAngle=labelAngle,
                                   labelBound=labelBound, labelFlush=labelFlush,
                                   labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels,
                                   maxExtent=maxExtent, minExtent=minExtent, offset=offset,
                                   orient=orient, position=position, tickCount=tickCount,
                                   tickSize=tickSize, ticks=ticks, title=title,
                                   titleMaxLength=titleMaxLength, titlePadding=titlePadding,
                                   values=values, zindex=zindex, **kwds)


class AxisConfig(VegaLiteSchema):
    """AxisConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    bandPosition : float
        An interpolation fraction indicating where, for `band` scales, axis ticks should be 
        positioned. A value of `0` places ticks at the left edge of their bands. A value of 
        `0.5` places ticks in the middle of their bands.
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as 
        part of the axis.  __Default value:__ `true`
    domainColor : string
        Color of axis domain line.  __Default value:__  (none, using Vega default).
    domainWidth : float
        Stroke width of axis domain line  __Default value:__  (none, using Vega default).
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis  
        __Default value:__ `true` for [continuous scales](scale.html#continuous) that are 
        not binned; otherwise, `false`.
    gridColor : string
        Color of gridlines.
    gridDash : List(float)
        The offset (in pixels) into which to begin drawing with the grid dash array.
    gridOpacity : float
        The stroke opacity of grid (value between [0,1])  __Default value:__ (`1` by 
        default)
    gridWidth : float
        The grid width, in pixels.
    labelAngle : float
        The rotation angle of the axis labels.  __Default value:__ `-90` for nominal and 
        ordinal fields; `0` otherwise.
    labelBound : anyOf(boolean, float)
        Indicates if labels should be hidden if they exceed the axis range. If `false `(the 
        default) no bounds overlap analysis is performed. If `true`, labels will be hidden 
        if they exceed the axis range by more than 1 pixel. If this property is a number, it
         specifies the pixel tolerance: the maximum amount by which a label bounding box may
         exceed the axis range.  __Default value:__ `false`.
    labelColor : string
        The color of the tick label, can be in hex color code or regular color name.
    labelFlush : anyOf(boolean, float)
        Indicates if the first and last axis labels should be aligned flush with the scale 
        range. Flush alignment for a horizontal axis will left-align the first label and 
        right-align the last label. For vertical axes, bottom and top text baselines are 
        applied instead. If this property is a number, it also indicates the number of 
        pixels by which to offset the first and last labels; for example, a value of 2 will 
        flush-align the first and last labels and also push them 2 pixels outward from the 
        center of the axis. The additional adjustment can sometimes help the labels better 
        visually group with corresponding axis ticks.  __Default value:__ `true` for axis of
         a continuous x-scale. Otherwise, `false`.
    labelFont : string
        The font of the tick label.
    labelFontSize : float
        The font size of the label, in pixels.
    labelLimit : float
        Maximum allowed pixel width of axis tick labels.
    labelOverlap : anyOf(boolean, enum('parity'), enum('greedy'))
        The strategy to use for resolving overlap of axis labels. If `false` (the default), 
        no overlap reduction is attempted. If set to `true` or `"parity"`, a strategy of 
        removing every other label is used (this works well for standard linear axes). If 
        set to `"greedy"`, a linear scan of the labels is performed, removing any labels 
        that overlaps with the last visible label (this often works better for log-scaled 
        axes).  __Default value:__ `true` for non-nominal fields with non-log scales; 
        `"greedy"` for log scales; otherwise `false`.
    labelPadding : float
        The padding, in pixels, between axis and text labels.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.  
        __Default value:__  `true`.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines 
        a maximum offset value for axis titles.  __Default value:__ `undefined`.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines 
        a minimum offset value for axis titles.  __Default value:__ `30` for y-axis; 
        `undefined` for x-axis.
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.  __Default value:__  
        `false`
    tickColor : string
        The color of the axis's tick.
    tickRound : boolean
        Boolean flag indicating if pixel position values should be rounded to the nearest 
        integer.
    tickSize : float
        The size in pixels of axis ticks.
    tickWidth : float
        The width, in pixels, of ticks.
    ticks : boolean
        Boolean value that determines whether the axis should include ticks.
    titleAlign : string
        Horizontal text alignment of axis titles.
    titleAngle : float
        Angle in degrees of axis titles.
    titleBaseline : string
        Vertical text baseline for axis titles.
    titleColor : string
        Color of the title, can be in hex color code or regular color name.
    titleFont : string
        Font of the title. (e.g., `"Helvetica Neue"`).
    titleFontSize : float
        Font size of the title.
    titleFontWeight : FontWeight
        Font weight of the title. This can be either a string (e.g `"bold"`, `"normal"`) or 
        a number (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = 
        `700`).
    titleLimit : float
        Maximum allowed pixel width of axis titles.
    titleMaxLength : float
        Max length for axis title if the title is automatically generated from the field's 
        description.
    titlePadding : float
        The padding, in pixels, between title and axis.
    titleX : float
        X-coordinate of the axis title relative to the axis group.
    titleY : float
        Y-coordinate of the axis title relative to the axis group.
    """
    _schema = {'$ref': '#/definitions/AxisConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined,
                 domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined,
                 gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined,
                 labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined,
                 labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined,
                 labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined,
                 shortTimeLabels=Undefined, tickColor=Undefined, tickRound=Undefined,
                 tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined,
                 titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined,
                 titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined,
                 titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined,
                 titleX=Undefined, titleY=Undefined, **kwds):
        super(AxisConfig, self).__init__(bandPosition=bandPosition, domain=domain,
                                         domainColor=domainColor, domainWidth=domainWidth, grid=grid,
                                         gridColor=gridColor, gridDash=gridDash,
                                         gridOpacity=gridOpacity, gridWidth=gridWidth,
                                         labelAngle=labelAngle, labelBound=labelBound,
                                         labelColor=labelColor, labelFlush=labelFlush,
                                         labelFont=labelFont, labelFontSize=labelFontSize,
                                         labelLimit=labelLimit, labelOverlap=labelOverlap,
                                         labelPadding=labelPadding, labels=labels, maxExtent=maxExtent,
                                         minExtent=minExtent, shortTimeLabels=shortTimeLabels,
                                         tickColor=tickColor, tickRound=tickRound, tickSize=tickSize,
                                         tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign,
                                         titleAngle=titleAngle, titleBaseline=titleBaseline,
                                         titleColor=titleColor, titleFont=titleFont,
                                         titleFontSize=titleFontSize, titleFontWeight=titleFontWeight,
                                         titleLimit=titleLimit, titleMaxLength=titleMaxLength,
                                         titlePadding=titlePadding, titleX=titleX, titleY=titleY, **kwds)


class AxisOrient(VegaLiteSchema):
    """AxisOrient schema wrapper
    
    enum('top', 'right', 'left', 'bottom')
    """
    _schema = {'$ref': '#/definitions/AxisOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AxisOrient, self).__init__(*args)


class AxisResolveMap(VegaLiteSchema):
    """AxisResolveMap schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    x : ResolveMode
    
    y : ResolveMode
    
    """
    _schema = {'$ref': '#/definitions/AxisResolveMap'}
    _rootschema = Root._schema

    def __init__(self, x=Undefined, y=Undefined, **kwds):
        super(AxisResolveMap, self).__init__(x=x, y=y, **kwds)


class BarConfig(VegaLiteSchema):
    """BarConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    align : HorizontalAlign
        The horizontal alignment of the text. One of `"left"`, `"right"`, `"center"`.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : VerticalAlign
        The vertical alignment of the text. One of `"top"`, `"middle"`, `"bottom"`.  
        __Default value:__ `"middle"`
    binSpacing : float
        Offset between bar for binned field.  Ideal value for this is either 0 (Preferred by
         statisticians) or 1 (Vega-Lite Default, D3 example style).  __Default value:__ `1`
    color : string
        Default color.  Note that `fill` and `stroke` have higher precedence than `color` 
        and will override `color`.  __Default value:__ <span style="color: 
        #4682b4;">&#9632;</span> `"#4682b4"`  __Note:__ This property cannot be used in a 
        [style config](mark.html#style-config).
    continuousBandSize : float
        The default size of the bars on continuous scales.  __Default value:__ `5`
    cursor : enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 
    'wait', 'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop', 
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize', 
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize', 
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
        The mouse cursor used over the mark. Any valid [CSS cursor 
        type](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values) can be used.
    discreteBandSize : float
        The size of the bars.  If unspecified, the default size is  `bandSize-1`, which 
        provides 1 pixel offset between bars.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ `1`
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.  
        __Default value:__ `true` for all marks except `point` and `false` for `point`.  
        __Applicable for:__ `bar`, `point`, `circle`, `square`, and `area` marks.  __Note:__
         This property cannot be used in a [style config](mark.html#style-config).
    font : string
        The typeface to set the text in (e.g., `"Helvetica Neue"`).
    fontSize : float
        The font size, in pixels.
    fontStyle : FontStyle
        The font style (e.g., `"italic"`).
    fontWeight : FontWeight
        The font weight. This can be either a string (e.g `"bold"`, `"normal"`) or a number 
        (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = `700`).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : Interpolate
        The line interpolation method to use for line and area marks. One of the following: 
        - `"linear"`: piecewise linear segments, as in a polyline. - `"linear-closed"`: 
        close the linear segments to form a polygon. - `"step"`: alternate between 
        horizontal and vertical segments, as in a step function. - `"step-before"`: 
        alternate between vertical and horizontal segments, as in a step function. - 
        `"step-after"`: alternate between horizontal and vertical segments, as in a step 
        function. - `"basis"`: a B-spline, with control point duplication on the ends. - 
        `"basis-open"`: an open B-spline; may not intersect the start or end. - 
        `"basis-closed"`: a closed B-spline, as in a loop. - `"cardinal"`: a Cardinal 
        spline, with control point duplication on the ends. - `"cardinal-open"`: an open 
        Cardinal spline; may not intersect the start or end, but will intersect other 
        control points. - `"cardinal-closed"`: a closed Cardinal spline, as in a loop. - 
        `"bundle"`: equivalent to basis, except the tension parameter is used to straighten 
        the spline. - `"monotone"`: cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels (default 0, indicating no limit). The 
        text value will be automatically truncated if the rendered size exceeds the limit.
    opacity : float
        The overall opacity (value between [0,1]).  __Default value:__ `0.7` for 
        non-aggregate plots with `point`, `tick`, `circle`, or `square` marks or layered 
        `bar` charts and `1` otherwise.
    orient : Orient
        The orientation of a non-stacked bar, tick, area, and line charts. The value is 
        either horizontal (default) or vertical. - For bar, rule and tick, this determines 
        whether the size of the bar and tick should be applied to x or y dimension. - For 
        area, this property determines the orient property of the Vega output. - For line, 
        this property determines the sort order of the points in the line if 
        `config.sortLineBy` is not specified. For stacked charts, this is always determined 
        by the orientation of the stack; therefore explicitly specified value will be 
        ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin 
        determined by the `x` and `y` properties.
    shape : string
        The default symbol shape to use. One of: `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or a custom SVG path.
          __Default value:__ `"circle"`
    size : float
        The pixel area each the point/circle/square. For example: in the case of circles, 
        the radius is determined in part by the square root of the size value.  __Default 
        value:__ `30`
    stroke : string
        Default Stroke Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ `1`
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area 
        marks).
    text : string
        Placeholder text if the `text` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by 
        the `x` and `y` properties. Values for `theta` follow the same convention of `arc` 
        mark `startAngle` and `endAngle` properties: angles are measured in radians, with 
        `0` indicating "north".
    """
    _schema = {'$ref': '#/definitions/BarConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                 color=Undefined, continuousBandSize=Undefined, cursor=Undefined,
                 discreteBandSize=Undefined, dx=Undefined, dy=Undefined, fill=Undefined,
                 fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                 limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined,
                 tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(BarConfig, self).__init__(align=align, angle=angle, baseline=baseline,
                                        binSpacing=binSpacing, color=color,
                                        continuousBandSize=continuousBandSize, cursor=cursor,
                                        discreteBandSize=discreteBandSize, dx=dx, dy=dy, fill=fill,
                                        fillOpacity=fillOpacity, filled=filled, font=font,
                                        fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                        href=href, interpolate=interpolate, limit=limit,
                                        opacity=opacity, orient=orient, radius=radius, shape=shape,
                                        size=size, stroke=stroke, strokeDash=strokeDash,
                                        strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                        strokeWidth=strokeWidth, tension=tension, text=text,
                                        theta=theta, **kwds)


class BasicType(VegaLiteSchema):
    """BasicType schema wrapper
    
    enum('quantitative', 'ordinal', 'temporal', 'nominal')
    """
    _schema = {'$ref': '#/definitions/BasicType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(BasicType, self).__init__(*args)


class BinParams(VegaLiteSchema):
    """BinParams schema wrapper
    
    Mapping(required=[])
    Binning properties or boolean flag for determining whether to bin data or not.
    
    Attributes
    ----------
    base : float
        The number base to use for automatic bin determination (default is base 10).  
        __Default value:__ `10`
    divide : List(float)
        Scale factors indicating allowable subdivisions. The default value is [5, 2], which 
        indicates that for base 10 numbers (the default base), the method may consider 
        dividing bin sizes by 5 and/or 2. For example, for an initial step size of 10, the 
        method can check if bin sizes of 2 (= 10/5), 5 (= 10/2), or 1 (= 10/(5*2)) might 
        also satisfy the given constraints.  __Default value:__ `[5, 2]`
    extent : List(float)
        A two-element (`[min, max]`) array indicating the range of desired bin values.
    maxbins : float
        Maximum number of bins.  __Default value:__ `6` for `row`, `column` and `shape` 
        channels; `10` for other channels
    minstep : float
        A minimum allowable step size (particularly useful for integer values).
    nice : boolean
        If true (the default), attempts to make the bin boundaries use human-friendly 
        boundaries, such as multiples of ten.
    step : float
        An exact step size to use between bins.  __Note:__ If provided, options such as 
        maxbins will be ignored.
    steps : List(float)
        An array of allowable step sizes to choose from.
    """
    _schema = {'$ref': '#/definitions/BinParams'}
    _rootschema = Root._schema

    def __init__(self, base=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined,
                 minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(BinParams, self).__init__(base=base, divide=divide, extent=extent, maxbins=maxbins,
                                        minstep=minstep, nice=nice, step=step, steps=steps, **kwds)


class BinTransform(VegaLiteSchema):
    """BinTransform schema wrapper
    
    Mapping(required=[bin, field, as])
    
    Attributes
    ----------
    bin : anyOf(boolean, BinParams)
        An object indicating bin properties, or simply `true` for using default bin 
        parameters.
    field : string
        The data field to bin.
    """
    _schema = {'$ref': '#/definitions/BinTransform'}
    _rootschema = Root._schema

    def __init__(self, bin=Undefined, field=Undefined, **kwds):
        super(BinTransform, self).__init__(bin=bin, field=field, **kwds)


class BrushConfig(VegaLiteSchema):
    """BrushConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    fill : string
        The fill color of the interval mark.  __Default value:__ `#333333`
    fillOpacity : float
        The fill opacity of the interval mark (a value between 0 and 1).  __Default value:__
         `0.125`
    stroke : string
        The stroke color of the interval mark.  __Default value:__ `#ffffff`
    strokeDash : List(float)
        An array of alternating stroke and space lengths, for creating dashed or dotted 
        lines.
    strokeDashOffset : float
        The offset (in pixels) with which to begin drawing the stroke dash array.
    strokeOpacity : float
        The stroke opacity of the interval mark (a value between 0 and 1).
    strokeWidth : float
        The stroke width of the interval mark.
    """
    _schema = {'$ref': '#/definitions/BrushConfig'}
    _rootschema = Root._schema

    def __init__(self, fill=Undefined, fillOpacity=Undefined, stroke=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, **kwds):
        super(BrushConfig, self).__init__(fill=fill, fillOpacity=fillOpacity, stroke=stroke,
                                          strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                          strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, **kwds)


class CalculateTransform(VegaLiteSchema):
    """CalculateTransform schema wrapper
    
    Mapping(required=[calculate, as])
    
    Attributes
    ----------
    calculate : string
        A [expression](https://vega.github.io/vega-lite/docs/types.html#expression) string. 
        Use the variable `datum` to refer to the current data object.
    """
    _schema = {'$ref': '#/definitions/CalculateTransform'}
    _rootschema = Root._schema

    def __init__(self, calculate=Undefined, **kwds):
        super(CalculateTransform, self).__init__(calculate=calculate, **kwds)


class CompositeUnitSpec(VegaLiteSchema):
    """CompositeUnitSpec schema wrapper
    
    Mapping(required=[mark])
    
    Attributes
    ----------
    mark : AnyMark
        A string describing the mark type (one of `"bar"`, `"circle"`, `"square"`, `"tick"`,
         `"line"`, * `"area"`, `"point"`, `"rule"`, `"geoshape"`, and `"text"`) or a [mark 
        definition object](https://vega.github.io/vega-lite/docs/mark.html#mark-def).
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : Encoding
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.  __Default value:__ - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its y-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the height will
         be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - 
        For y-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the height is [determined by the range step, paddings, and the
         cardinality of the field mapped to 
        y-channel](https://vega.github.io/vega-lite/docs/scale.html#band). Otherwise, if the
         `rangeStep` is `null`, the height will be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - If
         no field is mapped to `y` channel, the `height` will be the value of `rangeStep`.  
        __Note__: For plots with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the height of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : Projection
        An object defining properties of geographic projection.  Works with `"geoshape"` 
        marks and `"point"` or `"line"` marks that have `latitude` and `"longitude"` 
        channels.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.  __Default value:__ This will be determined by the 
        following rules:  - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its x-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the width will 
        be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - For
         x-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the width is [determined by the range step, paddings, and the 
        cardinality of the field mapped to 
        x-channel](https://vega.github.io/vega-lite/docs/scale.html#band).   Otherwise, if 
        the `rangeStep` is `null`, the width will be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - If 
        no field is mapped to `x` channel, the `width` will be the value of 
        [`config.scale.textXRangeStep`](https://vega.github.io/vega-lite/docs/size.html#default-width-and-height)
         for `text` mark and the value of `rangeStep` for other marks.  __Note:__ For plots 
        with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the width of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    """
    _schema = {'$ref': '#/definitions/CompositeUnitSpec'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, selection=Undefined,
                 title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(CompositeUnitSpec, self).__init__(mark=mark, data=data, description=description,
                                                encoding=encoding, height=height, name=name,
                                                projection=projection, selection=selection, title=title,
                                                transform=transform, width=width, **kwds)


class ConditionalFieldDef(VegaLiteSchema):
    """ConditionalFieldDef schema wrapper
    
    anyOf(ConditionalPredicateFieldDef, ConditionalSelectionFieldDef)
    """
    _schema = {'$ref': '#/definitions/Conditional<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalFieldDef, self).__init__(*args, **kwds)


class ConditionalMarkPropFieldDef(VegaLiteSchema):
    """ConditionalMarkPropFieldDef schema wrapper
    
    anyOf(ConditionalPredicateMarkPropFieldDef, ConditionalSelectionMarkPropFieldDef)
    """
    _schema = {'$ref': '#/definitions/Conditional<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDef, self).__init__(*args, **kwds)


class ConditionalTextFieldDef(VegaLiteSchema):
    """ConditionalTextFieldDef schema wrapper
    
    anyOf(ConditionalPredicateTextFieldDef, ConditionalSelectionTextFieldDef)
    """
    _schema = {'$ref': '#/definitions/Conditional<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalTextFieldDef, self).__init__(*args, **kwds)


class ConditionalValueDef(VegaLiteSchema):
    """ConditionalValueDef schema wrapper
    
    anyOf(ConditionalPredicateValueDef, ConditionalSelectionValueDef)
    """
    _schema = {'$ref': '#/definitions/Conditional<ValueDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalValueDef, self).__init__(*args, **kwds)


class ConditionalPredicateFieldDef(VegaLiteSchema):
    """ConditionalPredicateFieldDef schema wrapper
    
    Mapping(required=[test, type])
    
    Attributes
    ----------
    test : LogicalOperandPredicate
    
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateFieldDef, self).__init__(test=test, type=type, aggregate=aggregate,
                                                           bin=bin, field=field, timeUnit=timeUnit,
                                                           **kwds)


class ConditionalPredicateMarkPropFieldDef(VegaLiteSchema):
    """ConditionalPredicateMarkPropFieldDef schema wrapper
    
    Mapping(required=[test, type])
    
    Attributes
    ----------
    test : LogicalOperandPredicate
    
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding 
        channel will be removed.  __Default value:__ If undefined, default [legend 
        properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : anyOf(Scale, None)
        An object defining properties of the channel's scale, which is the function that 
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
         (pixels, colors, sizes) of the encoding channels.  If `null`, the scale will be 
        [disabled and the data value will be directly 
        encoded](https://vega.github.io/vega-lite/docs/scale.html#disable).  __Default 
        value:__ If undefined, default [scale 
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, 
        `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can
         also be a [sort field definition 
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default 
        value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 **kwds):
        super(ConditionalPredicateMarkPropFieldDef, self).__init__(test=test, type=type,
                                                                   aggregate=aggregate, bin=bin,
                                                                   field=field, legend=legend,
                                                                   scale=scale, sort=sort,
                                                                   timeUnit=timeUnit, **kwds)


class ConditionalPredicateTextFieldDef(VegaLiteSchema):
    """ConditionalPredicateTextFieldDef schema wrapper
    
    Mapping(required=[test, type])
    
    Attributes
    ----------
    test : LogicalOperandPredicate
    
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html) for a 
        text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateTextFieldDef, self).__init__(test=test, type=type,
                                                               aggregate=aggregate, bin=bin,
                                                               field=field, format=format,
                                                               timeUnit=timeUnit, **kwds)


class ConditionalPredicateValueDef(VegaLiteSchema):
    """ConditionalPredicateValueDef schema wrapper
    
    Mapping(required=[test, value])
    
    Attributes
    ----------
    test : LogicalOperandPredicate
    
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values 
        between `0` to `1` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDef, self).__init__(test=test, value=value, **kwds)


class ConditionalSelectionFieldDef(VegaLiteSchema):
    """ConditionalSelectionFieldDef schema wrapper
    
    Mapping(required=[selection, type])
    
    Attributes
    ----------
    selection : SelectionOperand
        A [selection name](https://vega.github.io/vega-lite/docs/selection.html), or a 
        series of [composed 
        selections](https://vega.github.io/vega-lite/docs/selection.html#compose).
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionFieldDef, self).__init__(selection=selection, type=type,
                                                           aggregate=aggregate, bin=bin, field=field,
                                                           timeUnit=timeUnit, **kwds)


class ConditionalSelectionMarkPropFieldDef(VegaLiteSchema):
    """ConditionalSelectionMarkPropFieldDef schema wrapper
    
    Mapping(required=[selection, type])
    
    Attributes
    ----------
    selection : SelectionOperand
        A [selection name](https://vega.github.io/vega-lite/docs/selection.html), or a 
        series of [composed 
        selections](https://vega.github.io/vega-lite/docs/selection.html#compose).
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding 
        channel will be removed.  __Default value:__ If undefined, default [legend 
        properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : anyOf(Scale, None)
        An object defining properties of the channel's scale, which is the function that 
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
         (pixels, colors, sizes) of the encoding channels.  If `null`, the scale will be 
        [disabled and the data value will be directly 
        encoded](https://vega.github.io/vega-lite/docs/scale.html#disable).  __Default 
        value:__ If undefined, default [scale 
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, 
        `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can
         also be a [sort field definition 
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default 
        value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 **kwds):
        super(ConditionalSelectionMarkPropFieldDef, self).__init__(selection=selection, type=type,
                                                                   aggregate=aggregate, bin=bin,
                                                                   field=field, legend=legend,
                                                                   scale=scale, sort=sort,
                                                                   timeUnit=timeUnit, **kwds)


class ConditionalSelectionTextFieldDef(VegaLiteSchema):
    """ConditionalSelectionTextFieldDef schema wrapper
    
    Mapping(required=[selection, type])
    
    Attributes
    ----------
    selection : SelectionOperand
        A [selection name](https://vega.github.io/vega-lite/docs/selection.html), or a 
        series of [composed 
        selections](https://vega.github.io/vega-lite/docs/selection.html#compose).
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html) for a 
        text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionTextFieldDef, self).__init__(selection=selection, type=type,
                                                               aggregate=aggregate, bin=bin,
                                                               field=field, format=format,
                                                               timeUnit=timeUnit, **kwds)


class ConditionalSelectionValueDef(VegaLiteSchema):
    """ConditionalSelectionValueDef schema wrapper
    
    Mapping(required=[selection, value])
    
    Attributes
    ----------
    selection : SelectionOperand
        A [selection name](https://vega.github.io/vega-lite/docs/selection.html), or a 
        series of [composed 
        selections](https://vega.github.io/vega-lite/docs/selection.html#compose).
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values 
        between `0` to `1` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionValueDef, self).__init__(selection=selection, value=value, **kwds)


class Config(VegaLiteSchema):
    """Config schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    area : MarkConfig
        Area-Specific Config 
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    axis : AxisConfig
        Axis configuration, which determines default properties for all `x` and `y` 
        [axes](axis.html). For a full list of axis configuration options, please see the 
        [corresponding section of the axis documentation](axis.html#config).
    axisBand : VgAxisConfig
        Specific axis config for axes with "band" scales.
    axisBottom : VgAxisConfig
        Specific axis config for x-axis along the bottom edge of the chart.
    axisLeft : VgAxisConfig
        Specific axis config for y-axis along the left edge of the chart.
    axisRight : VgAxisConfig
        Specific axis config for y-axis along the right edge of the chart.
    axisTop : VgAxisConfig
        Specific axis config for x-axis along the top edge of the chart.
    axisX : VgAxisConfig
        X-axis specific config.
    axisY : VgAxisConfig
        Y-axis specific config.
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    bar : BarConfig
        Bar-Specific Config 
    circle : MarkConfig
        Circle-Specific Config 
    countTitle : string
        Default axis and legend title for count fields.  __Default value:__ `'Number of 
        Records'`.
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    fieldTitle : enum('verbal', 'functional', 'plain')
        Defines how Vega-Lite generates title for fields.  There are three possible styles: 
        - `"verbal"` (Default) - displays function in a verbal style (e.g., "Sum of field", 
        "Year-month of date", "field (binned)"). - `"function"` - displays function using 
        parentheses and capitalized texts (e.g., "SUM(field)", "YEARMONTH(date)", 
        "BIN(field)"). - `"plain"` - displays only the field name without functions (e.g., 
        "field", "date", "field").
    geoshape : MarkConfig
        Geoshape-Specific Config 
    invalidValues : enum('filter', None)
        Defines how Vega-Lite should handle invalid values (`null` and `NaN`). - If set to 
        `"filter"` (default), all data items with null values are filtered. - If `null`, all
         data items are included. In this case, invalid values will be interpreted as 
        zeroes.
    legend : LegendConfig
        Legend configuration, which determines default properties for all 
        [legends](legend.html). For a full list of legend configuration options, please see 
        the [corresponding section of in the legend documentation](legend.html#config).
    line : MarkConfig
        Line-Specific Config 
    mark : MarkConfig
        Mark Config 
    numberFormat : string
        D3 Number format for axis labels and text tables. For example "s" for SI units. Use 
        [D3's number format pattern](https://github.com/d3/d3-format#locale_format).
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    point : MarkConfig
        Point-Specific Config 
    projection : ProjectionConfig
        Projection configuration, which determines default properties for all 
        [projections](projection.html). For a full list of projection configuration options,
         please see the [corresponding section of the projection 
        documentation](projection.html#config).
    range : RangeConfig
        An object hash that defines default range arrays or schemes for using with scales. 
        For a full list of scale range configuration options, please see the [corresponding 
        section of the scale documentation](scale.html#config).
    rect : MarkConfig
        Rect-Specific Config 
    rule : MarkConfig
        Rule-Specific Config 
    scale : ScaleConfig
        Scale configuration determines default properties for all [scales](scale.html). For 
        a full list of scale configuration options, please see the [corresponding section of
         the scale documentation](scale.html#config).
    selection : SelectionConfig
        An object hash for defining default properties for each type of selections. 
    square : MarkConfig
        Square-Specific Config 
    stack : StackOffset
        Default stack offset for stackable mark. 
    style : StyleConfigIndex
        An object hash that defines key-value mappings to determine default properties for 
        marks with a given [style](mark.html#mark-def).  The keys represent styles names; 
        the value are valid [mark configuration objects](mark.html#config).  
    text : TextConfig
        Text-Specific Config 
    tick : TickConfig
        Tick-Specific Config 
    timeFormat : string
        Default datetime format for axis and legend labels. The format can be set directly 
        on each axis and legend. Use [D3's time format 
        pattern](https://github.com/d3/d3-time-format#locale_format).  __Default value:__ 
        `'%b %d, %Y'`.
    title : VgTitleConfig
        Title configuration, which determines default properties for all 
        [titles](title.html). For a full list of title configuration options, please see the
         [corresponding section of the title documentation](title.html#config).
    view : ViewConfig
        Default properties for [single view plots](spec.html#single). 
    """
    _schema = {'$ref': '#/definitions/Config'}
    _rootschema = Root._schema

    def __init__(self, area=Undefined, autosize=Undefined, axis=Undefined, axisBand=Undefined,
                 axisBottom=Undefined, axisLeft=Undefined, axisRight=Undefined, axisTop=Undefined,
                 axisX=Undefined, axisY=Undefined, background=Undefined, bar=Undefined,
                 circle=Undefined, countTitle=Undefined, datasets=Undefined, fieldTitle=Undefined,
                 geoshape=Undefined, invalidValues=Undefined, legend=Undefined, line=Undefined,
                 mark=Undefined, numberFormat=Undefined, padding=Undefined, point=Undefined,
                 projection=Undefined, range=Undefined, rect=Undefined, rule=Undefined, scale=Undefined,
                 selection=Undefined, square=Undefined, stack=Undefined, style=Undefined,
                 text=Undefined, tick=Undefined, timeFormat=Undefined, title=Undefined, view=Undefined,
                 **kwds):
        super(Config, self).__init__(area=area, autosize=autosize, axis=axis, axisBand=axisBand,
                                     axisBottom=axisBottom, axisLeft=axisLeft, axisRight=axisRight,
                                     axisTop=axisTop, axisX=axisX, axisY=axisY, background=background,
                                     bar=bar, circle=circle, countTitle=countTitle, datasets=datasets,
                                     fieldTitle=fieldTitle, geoshape=geoshape,
                                     invalidValues=invalidValues, legend=legend, line=line, mark=mark,
                                     numberFormat=numberFormat, padding=padding, point=point,
                                     projection=projection, range=range, rect=rect, rule=rule,
                                     scale=scale, selection=selection, square=square, stack=stack,
                                     style=style, text=text, tick=tick, timeFormat=timeFormat,
                                     title=title, view=view, **kwds)


class CsvDataFormat(VegaLiteSchema):
    """CsvDataFormat schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    parse : anyOf(enum('auto'), Mapping(required=[]))
        If set to auto (the default), perform automatic type inference to determine the 
        desired data types. Alternatively, a parsing directive object can be provided for 
        explicit data types. Each property of the object corresponds to a field name, and 
        the value to the desired data type (one of `"number"`, `"boolean"` or `"date"`). For
         example, `"parse": {"modified_on": "date"}` parses the `modified_on` field in each 
        input record a Date value.  For `"date"`, we parse data based using Javascript's 
        [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse).
         For Specific date formats can be provided (e.g., `{foo: 'date:"%m%d%Y"'}`), using 
        the [d3-time-format syntax](https://github.com/d3/d3-time-format#locale_format). UTC
         date format parsing is supported similarly (e.g., `{foo: 'utc:"%m%d%Y"'}`). See 
        more about [UTC time](timeunit.html#utc)
    type : enum('csv', 'tsv')
        Type of input data: `"json"`, `"csv"`, `"tsv"`. The default format type is 
        determined by the extension of the file URL. If no extension is detected, `"json"` 
        will be used by default.
    """
    _schema = {'$ref': '#/definitions/CsvDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, type=Undefined, **kwds):
        super(CsvDataFormat, self).__init__(parse=parse, type=type, **kwds)


class Data(VegaLiteSchema):
    """Data schema wrapper
    
    anyOf(UrlData, InlineData, NamedData)
    """
    _schema = {'$ref': '#/definitions/Data'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Data, self).__init__(*args, **kwds)


class DataFormat(VegaLiteSchema):
    """DataFormat schema wrapper
    
    anyOf(CsvDataFormat, JsonDataFormat, TopoDataFormat)
    """
    _schema = {'$ref': '#/definitions/DataFormat'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(DataFormat, self).__init__(*args, **kwds)


class Datasets(VegaLiteSchema):
    """Datasets schema wrapper
    
    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/Datasets'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(Datasets, self).__init__(**kwds)


class DateTime(VegaLiteSchema):
    """DateTime schema wrapper
    
    Mapping(required=[])
    Object for defining datetime in Vega-Lite Filter.
    If both month and quarter are provided, month has higher precedence.
    `day` cannot be combined with other date.
    We accept string for month and day names.
    
    Attributes
    ----------
    date : float
        Integer value representing the date from 1-31.
    day : anyOf(Day, string)
        Value representing the day of a week.  This can be one of: (1) integer value -- `1` 
        represents Monday; (2) case-insensitive day name (e.g., `"Monday"`);  (3) 
        case-insensitive, 3-character short day name (e.g., `"Mon"`).   <br/> **Warning:** A
         DateTime definition object with `day`** should not be combined with `year`, 
        `quarter`, `month`, or `date`.
    hours : float
        Integer value representing the hour of a day from 0-23.
    milliseconds : float
        Integer value representing the millisecond segment of time.
    minutes : float
        Integer value representing the minute segment of time from 0-59.
    month : anyOf(Month, string)
        One of: (1) integer value representing the month from `1`-`12`. `1` represents 
        January;  (2) case-insensitive month name (e.g., `"January"`);  (3) 
        case-insensitive, 3-character short month name (e.g., `"Jan"`). 
    quarter : float
        Integer value representing the quarter of the year (from 1-4).
    seconds : float
        Integer value representing the second segment (0-59) of a time value
    utc : boolean
        A boolean flag indicating if date time is in utc time. If false, the date time is in
         local time
    year : float
        Integer value representing the year.
    """
    _schema = {'$ref': '#/definitions/DateTime'}
    _rootschema = Root._schema

    def __init__(self, date=Undefined, day=Undefined, hours=Undefined, milliseconds=Undefined,
                 minutes=Undefined, month=Undefined, quarter=Undefined, seconds=Undefined,
                 utc=Undefined, year=Undefined, **kwds):
        super(DateTime, self).__init__(date=date, day=day, hours=hours, milliseconds=milliseconds,
                                       minutes=minutes, month=month, quarter=quarter, seconds=seconds,
                                       utc=utc, year=year, **kwds)


class Day(VegaLiteSchema):
    """Day schema wrapper
    
    float
    """
    _schema = {'$ref': '#/definitions/Day'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Day, self).__init__(*args)


class DictInlineDataset(VegaLiteSchema):
    """DictInlineDataset schema wrapper
    
    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/Dict<InlineDataset>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(DictInlineDataset, self).__init__(**kwds)


class Encoding(VegaLiteSchema):
    """Encoding schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    color : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Color of the marks – either fill or stroke color based on  the `filled` property of 
        mark definition. By default, `color` represents fill color for `"area"`, `"bar"`, 
        `"tick"`, `"text"`, `"circle"`, and `"square"` / stroke color for `"line"` and 
        `"point"`.  __Default value:__ If undefined, the default color depends on [mark 
        config](config.html#mark)'s `color` property.  _Note:_ 1) For fine-grained control 
        over both fill and stroke colors of the marks, please use the `fill` and `stroke` 
        channels. 2) See the scale documentation for more information about customizing 
        [color scheme](scale.html#scheme).
    detail : anyOf(FieldDef, List(FieldDef))
        Additional levels of detail for grouping data in aggregate views and in line and 
        area marks without mapping data to a specific visual channel.
    fill : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Fill color of the marks. __Default value:__ If undefined, the default color depends 
        on [mark config](config.html#mark)'s `color` property.  _Note:_ The `fill` channel 
        has higher precedence than `color` and will override color value.
    href : anyOf(FieldDefWithCondition, ValueDefWithCondition)
        A URL to load upon mouse click.
    key : FieldDef
        A data field to use as a unique key for data binding. When a visualization’s data is
         updated, the key value will be used to match data elements to existing mark 
        instances. Use a key channel to enable object constancy for transitions over dynamic
         data.
    latitude : FieldDef
        Latitude position of geographically projected marks.
    latitude2 : FieldDef
        Latitude-2 position for geographically projected ranged `"area"`, `"bar"`, `"rect"`,
         and  `"rule"`.
    longitude : FieldDef
        Longitude position of geographically projected marks.
    longitude2 : FieldDef
        Longitude-2 position for geographically projected ranged `"area"`, `"bar"`, 
        `"rect"`, and  `"rule"`.
    opacity : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Opacity of the marks – either can be a value or a range.  __Default value:__ If 
        undefined, the default opacity depends on [mark config](config.html#mark)'s 
        `opacity` property.
    order : anyOf(OrderFieldDef, List(OrderFieldDef))
        Order of the marks. - For stacked marks, this `order` channel encodes stack order. -
         For line marks, this `order` channel encodes order of data points in the lines. 
        This can be useful for creating [a connected 
        scatterplot](https://vega.github.io/vega-lite/examples/layer_connected_scatterplot.html).
         - Otherwise, this `order` channel encodes layer order of the marks.  __Note__: In 
        aggregate plots, `order` field should be `aggregate`d to avoid creating additional 
        aggregation grouping.
    shape : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        For `point` marks the supported values are `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or else a custom SVG 
        path string. For `geoshape` marks it should be a field definition of the geojson 
        data  __Default value:__ If undefined, the default shape depends on [mark 
        config](config.html#point-config)'s `shape` property.
    size : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Size of the mark. - For `"point"`, `"square"` and `"circle"`, – the symbol size, or 
        pixel area of the mark. - For `"bar"` and `"tick"` – the bar and tick's size. - For 
        `"text"` – the text's font size. - Size is currently unsupported for `"line"`, 
        `"area"`, and `"rect"`.
    stroke : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Stroke color of the marks. __Default value:__ If undefined, the default color 
        depends on [mark config](config.html#mark)'s `color` property.  _Note:_ The `stroke`
         channel has higher precedence than `color` and will override color value.
    text : anyOf(TextFieldDefWithCondition, TextValueDefWithCondition)
        Text of the `text` mark.
    tooltip : anyOf(TextFieldDefWithCondition, TextValueDefWithCondition)
        The tooltip text to show upon mouse hover.
    x : anyOf(PositionFieldDef, ValueDef)
        X coordinates of the marks, or width of horizontal `"bar"` and `"area"`.
    x2 : anyOf(FieldDef, ValueDef)
        X2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and  `"rule"`.
    y : anyOf(PositionFieldDef, ValueDef)
        Y coordinates of the marks, or height of vertical `"bar"` and `"area"`.
    y2 : anyOf(FieldDef, ValueDef)
        Y2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and  `"rule"`.
    """
    _schema = {'$ref': '#/definitions/Encoding'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, detail=Undefined, fill=Undefined, href=Undefined, key=Undefined,
                 latitude=Undefined, latitude2=Undefined, longitude=Undefined, longitude2=Undefined,
                 opacity=Undefined, order=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined,
                 y2=Undefined, **kwds):
        super(Encoding, self).__init__(color=color, detail=detail, fill=fill, href=href, key=key,
                                       latitude=latitude, latitude2=latitude2, longitude=longitude,
                                       longitude2=longitude2, opacity=opacity, order=order, shape=shape,
                                       size=size, stroke=stroke, text=text, tooltip=tooltip, x=x, x2=x2,
                                       y=y, y2=y2, **kwds)


class EncodingWithFacet(VegaLiteSchema):
    """EncodingWithFacet schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    color : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Color of the marks – either fill or stroke color based on  the `filled` property of 
        mark definition. By default, `color` represents fill color for `"area"`, `"bar"`, 
        `"tick"`, `"text"`, `"circle"`, and `"square"` / stroke color for `"line"` and 
        `"point"`.  __Default value:__ If undefined, the default color depends on [mark 
        config](config.html#mark)'s `color` property.  _Note:_ 1) For fine-grained control 
        over both fill and stroke colors of the marks, please use the `fill` and `stroke` 
        channels. 2) See the scale documentation for more information about customizing 
        [color scheme](scale.html#scheme).
    column : FacetFieldDef
        Horizontal facets for trellis plots.
    detail : anyOf(FieldDef, List(FieldDef))
        Additional levels of detail for grouping data in aggregate views and in line and 
        area marks without mapping data to a specific visual channel.
    fill : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Fill color of the marks. __Default value:__ If undefined, the default color depends 
        on [mark config](config.html#mark)'s `color` property.  _Note:_ The `fill` channel 
        has higher precedence than `color` and will override color value.
    href : anyOf(FieldDefWithCondition, ValueDefWithCondition)
        A URL to load upon mouse click.
    key : FieldDef
        A data field to use as a unique key for data binding. When a visualization’s data is
         updated, the key value will be used to match data elements to existing mark 
        instances. Use a key channel to enable object constancy for transitions over dynamic
         data.
    latitude : FieldDef
        Latitude position of geographically projected marks.
    latitude2 : FieldDef
        Latitude-2 position for geographically projected ranged `"area"`, `"bar"`, `"rect"`,
         and  `"rule"`.
    longitude : FieldDef
        Longitude position of geographically projected marks.
    longitude2 : FieldDef
        Longitude-2 position for geographically projected ranged `"area"`, `"bar"`, 
        `"rect"`, and  `"rule"`.
    opacity : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Opacity of the marks – either can be a value or a range.  __Default value:__ If 
        undefined, the default opacity depends on [mark config](config.html#mark)'s 
        `opacity` property.
    order : anyOf(OrderFieldDef, List(OrderFieldDef))
        Order of the marks. - For stacked marks, this `order` channel encodes stack order. -
         For line marks, this `order` channel encodes order of data points in the lines. 
        This can be useful for creating [a connected 
        scatterplot](https://vega.github.io/vega-lite/examples/layer_connected_scatterplot.html).
         - Otherwise, this `order` channel encodes layer order of the marks.  __Note__: In 
        aggregate plots, `order` field should be `aggregate`d to avoid creating additional 
        aggregation grouping.
    row : FacetFieldDef
        Vertical facets for trellis plots.
    shape : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        For `point` marks the supported values are `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or else a custom SVG 
        path string. For `geoshape` marks it should be a field definition of the geojson 
        data  __Default value:__ If undefined, the default shape depends on [mark 
        config](config.html#point-config)'s `shape` property.
    size : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Size of the mark. - For `"point"`, `"square"` and `"circle"`, – the symbol size, or 
        pixel area of the mark. - For `"bar"` and `"tick"` – the bar and tick's size. - For 
        `"text"` – the text's font size. - Size is currently unsupported for `"line"`, 
        `"area"`, and `"rect"`.
    stroke : anyOf(MarkPropFieldDefWithCondition, MarkPropValueDefWithCondition)
        Stroke color of the marks. __Default value:__ If undefined, the default color 
        depends on [mark config](config.html#mark)'s `color` property.  _Note:_ The `stroke`
         channel has higher precedence than `color` and will override color value.
    text : anyOf(TextFieldDefWithCondition, TextValueDefWithCondition)
        Text of the `text` mark.
    tooltip : anyOf(TextFieldDefWithCondition, TextValueDefWithCondition)
        The tooltip text to show upon mouse hover.
    x : anyOf(PositionFieldDef, ValueDef)
        X coordinates of the marks, or width of horizontal `"bar"` and `"area"`.
    x2 : anyOf(FieldDef, ValueDef)
        X2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and  `"rule"`.
    y : anyOf(PositionFieldDef, ValueDef)
        Y coordinates of the marks, or height of vertical `"bar"` and `"area"`.
    y2 : anyOf(FieldDef, ValueDef)
        Y2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and  `"rule"`.
    """
    _schema = {'$ref': '#/definitions/EncodingWithFacet'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, column=Undefined, detail=Undefined, fill=Undefined,
                 href=Undefined, key=Undefined, latitude=Undefined, latitude2=Undefined,
                 longitude=Undefined, longitude2=Undefined, opacity=Undefined, order=Undefined,
                 row=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, text=Undefined,
                 tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(EncodingWithFacet, self).__init__(color=color, column=column, detail=detail, fill=fill,
                                                href=href, key=key, latitude=latitude,
                                                latitude2=latitude2, longitude=longitude,
                                                longitude2=longitude2, opacity=opacity, order=order,
                                                row=row, shape=shape, size=size, stroke=stroke,
                                                text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2,
                                                **kwds)


class LayerSpec(VegaLiteSchema):
    """LayerSpec schema wrapper
    
    Mapping(required=[layer])
    Layer Spec with encoding and projection
    
    Attributes
    ----------
    layer : List(anyOf(LayerSpec, CompositeUnitSpec))
        Layer or single view specifications to be layered.  __Note__: Specifications inside 
        `layer` cannot use `row` and `column` channels as layering facet specifications is 
        not allowed.
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : Encoding
        A shared key-value mapping between encoding channels and definition of fields in the
         underlying layers.
    height : float
        The height of a visualization.  __Default value:__ - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its y-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the height will
         be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - 
        For y-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the height is [determined by the range step, paddings, and the
         cardinality of the field mapped to 
        y-channel](https://vega.github.io/vega-lite/docs/scale.html#band). Otherwise, if the
         `rangeStep` is `null`, the height will be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - If
         no field is mapped to `y` channel, the `height` will be the value of `rangeStep`.  
        __Note__: For plots with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the height of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : Projection
        An object defining properties of the geographic projection shared by underlying 
        layers.
    resolve : Resolve
        Scale, axis, and legend resolutions for layers.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.  __Default value:__ This will be determined by the 
        following rules:  - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its x-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the width will 
        be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - For
         x-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the width is [determined by the range step, paddings, and the 
        cardinality of the field mapped to 
        x-channel](https://vega.github.io/vega-lite/docs/scale.html#band).   Otherwise, if 
        the `rangeStep` is `null`, the width will be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - If 
        no field is mapped to `x` channel, the `width` will be the value of 
        [`config.scale.textXRangeStep`](https://vega.github.io/vega-lite/docs/size.html#default-width-and-height)
         for `text` mark and the value of `rangeStep` for other marks.  __Note:__ For plots 
        with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the width of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    """
    _schema = {'$ref': '#/definitions/LayerSpec'}
    _rootschema = Root._schema

    def __init__(self, layer=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, resolve=Undefined,
                 title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(LayerSpec, self).__init__(layer=layer, data=data, description=description,
                                        encoding=encoding, height=height, name=name,
                                        projection=projection, resolve=resolve, title=title,
                                        transform=transform, width=width, **kwds)


class FacetFieldDef(VegaLiteSchema):
    """FacetFieldDef schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    header : Header
        An object defining properties of a facet's header.
    sort : SortOrder
        Sort order for a facet field. This can be `"ascending"`, `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/FacetFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(FacetFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                            header=header, sort=sort, timeUnit=timeUnit, **kwds)


class FacetMapping(VegaLiteSchema):
    """FacetMapping schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    column : FacetFieldDef
        Horizontal facets for trellis plots.
    row : FacetFieldDef
        Vertical facets for trellis plots.
    """
    _schema = {'$ref': '#/definitions/FacetMapping'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(FacetMapping, self).__init__(column=column, row=row, **kwds)


class FieldDef(VegaLiteSchema):
    """FieldDef schema wrapper
    
    Mapping(required=[type])
    Definition object for a data field, its type and transformation of an encoding channel.
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/FieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, **kwds):
        super(FieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                       timeUnit=timeUnit, **kwds)


class FieldDefWithCondition(VegaLiteSchema):
    """FieldDefWithCondition schema wrapper
    
    Mapping(required=[type])
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, List(ConditionalValueDef))
        One or more value definition(s) with a selection predicate.  __Note:__ A field 
        definition's `condition` property can only contain [value 
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since 
        Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                    condition=condition, field=field, timeUnit=timeUnit,
                                                    **kwds)


class MarkPropFieldDefWithCondition(VegaLiteSchema):
    """MarkPropFieldDefWithCondition schema wrapper
    
    Mapping(required=[type])
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, List(ConditionalValueDef))
        One or more value definition(s) with a selection predicate.  __Note:__ A field 
        definition's `condition` property can only contain [value 
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since 
        Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding 
        channel will be removed.  __Default value:__ If undefined, default [legend 
        properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : anyOf(Scale, None)
        An object defining properties of the channel's scale, which is the function that 
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
         (pixels, colors, sizes) of the encoding channels.  If `null`, the scale will be 
        [disabled and the data value will be directly 
        encoded](https://vega.github.io/vega-lite/docs/scale.html#disable).  __Default 
        value:__ If undefined, default [scale 
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, 
        `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can
         also be a [sort field definition 
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default 
        value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/MarkPropFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 **kwds):
        super(MarkPropFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                            condition=condition, field=field,
                                                            legend=legend, scale=scale, sort=sort,
                                                            timeUnit=timeUnit, **kwds)


class TextFieldDefWithCondition(VegaLiteSchema):
    """TextFieldDefWithCondition schema wrapper
    
    Mapping(required=[type])
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, List(ConditionalValueDef))
        One or more value definition(s) with a selection predicate.  __Note:__ A field 
        definition's `condition` property can only contain [value 
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since 
        Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html) for a 
        text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/TextFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(TextFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                        condition=condition, field=field, format=format,
                                                        timeUnit=timeUnit, **kwds)


class FieldEqualPredicate(VegaLiteSchema):
    """FieldEqualPredicate schema wrapper
    
    Mapping(required=[field, equal])
    
    Attributes
    ----------
    equal : anyOf(string, float, boolean, DateTime)
        The value that the field should be equal to.
    field : string
        Field to be filtered.
    timeUnit : TimeUnit
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldEqualPredicate'}
    _rootschema = Root._schema

    def __init__(self, equal=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldEqualPredicate, self).__init__(equal=equal, field=field, timeUnit=timeUnit, **kwds)


class FieldOneOfPredicate(VegaLiteSchema):
    """FieldOneOfPredicate schema wrapper
    
    Mapping(required=[field, oneOf])
    
    Attributes
    ----------
    field : string
        Field to be filtered
    oneOf : anyOf(List(string), List(float), List(boolean), List(DateTime))
        A set of values that the `field`'s value should be a member of, for a data item 
        included in the filtered data.
    timeUnit : TimeUnit
        time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldOneOfPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, oneOf=Undefined, timeUnit=Undefined, **kwds):
        super(FieldOneOfPredicate, self).__init__(field=field, oneOf=oneOf, timeUnit=timeUnit, **kwds)


class FieldRangePredicate(VegaLiteSchema):
    """FieldRangePredicate schema wrapper
    
    Mapping(required=[field, range])
    
    Attributes
    ----------
    field : string
        Field to be filtered
    range : List(anyOf(float, DateTime, None))
        An array of inclusive minimum and maximum values for a field value of a data item to
         be included in the filtered data.
    timeUnit : TimeUnit
        time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldRangePredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, range=Undefined, timeUnit=Undefined, **kwds):
        super(FieldRangePredicate, self).__init__(field=field, range=range, timeUnit=timeUnit, **kwds)


class FilterTransform(VegaLiteSchema):
    """FilterTransform schema wrapper
    
    Mapping(required=[filter])
    
    Attributes
    ----------
    filter : LogicalOperandPredicate
        The `filter` property must be one of the predicate definitions: (1) an 
        [expression](https://vega.github.io/vega-lite/docs/types.html#expression) string, 
        where `datum` can be used to refer to the current data object; (2) one of the field 
        predicates: [equal 
        predicate](https://vega.github.io/vega-lite/docs/filter.html#equal-predicate); 
        [range predicate](filter.html#range-predicate), [one-of 
        predicate](https://vega.github.io/vega-lite/docs/filter.html#one-of-predicate); (3) 
        a [selection 
        predicate](https://vega.github.io/vega-lite/docs/filter.html#selection-predicate); 
        or (4) a logical operand that combines (1), (2), or (3).
    """
    _schema = {'$ref': '#/definitions/FilterTransform'}
    _rootschema = Root._schema

    def __init__(self, filter=Undefined, **kwds):
        super(FilterTransform, self).__init__(filter=filter, **kwds)


class FontStyle(VegaLiteSchema):
    """FontStyle schema wrapper
    
    enum('normal', 'italic')
    """
    _schema = {'$ref': '#/definitions/FontStyle'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontStyle, self).__init__(*args)


class FontWeight(VegaLiteSchema):
    """FontWeight schema wrapper
    
    anyOf(FontWeightString, FontWeightNumber)
    """
    _schema = {'$ref': '#/definitions/FontWeight'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(FontWeight, self).__init__(*args, **kwds)


class FontWeightNumber(VegaLiteSchema):
    """FontWeightNumber schema wrapper
    
    float
    """
    _schema = {'$ref': '#/definitions/FontWeightNumber'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontWeightNumber, self).__init__(*args)


class FontWeightString(VegaLiteSchema):
    """FontWeightString schema wrapper
    
    enum('normal', 'bold')
    """
    _schema = {'$ref': '#/definitions/FontWeightString'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontWeightString, self).__init__(*args)


class FacetSpec(VegaLiteSchema):
    """FacetSpec schema wrapper
    
    Mapping(required=[facet, spec])
    
    Attributes
    ----------
    facet : FacetMapping
        An object that describes mappings between `row` and `column` channels and their 
        field definitions.
    spec : anyOf(LayerSpec, CompositeUnitSpec)
        A specification of the view that gets faceted.
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : Resolve
        Scale, axis, and legend resolutions for facets.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/FacetSpec'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, spec=Undefined, data=Undefined, description=Undefined,
                 name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, data=data, description=description,
                                        name=name, resolve=resolve, title=title, transform=transform,
                                        **kwds)


class HConcatSpec(VegaLiteSchema):
    """HConcatSpec schema wrapper
    
    Mapping(required=[hconcat])
    
    Attributes
    ----------
    hconcat : List(Spec)
        A list of views that should be concatenated and put into a row.
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : Resolve
        Scale, axis, and legend resolutions for horizontally concatenated charts.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/HConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, data=Undefined, description=Undefined, name=Undefined,
                 resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(HConcatSpec, self).__init__(hconcat=hconcat, data=data, description=description,
                                          name=name, resolve=resolve, title=title, transform=transform,
                                          **kwds)


class RepeatSpec(VegaLiteSchema):
    """RepeatSpec schema wrapper
    
    Mapping(required=[repeat, spec])
    
    Attributes
    ----------
    repeat : Repeat
        An object that describes what fields should be repeated into views that are laid out
         as a `row` or `column`.
    spec : Spec
    
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : Resolve
        Scale and legend resolutions for repeated charts.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/RepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, data=Undefined, description=Undefined,
                 name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(RepeatSpec, self).__init__(repeat=repeat, spec=spec, data=data, description=description,
                                         name=name, resolve=resolve, title=title, transform=transform,
                                         **kwds)


class Spec(VegaLiteSchema):
    """Spec schema wrapper
    
    anyOf(CompositeUnitSpec, LayerSpec, FacetSpec, RepeatSpec, VConcatSpec, HConcatSpec)
    """
    _schema = {'$ref': '#/definitions/Spec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Spec, self).__init__(*args, **kwds)


class CompositeUnitSpecAlias(VegaLiteSchema):
    """CompositeUnitSpecAlias schema wrapper
    
    Mapping(required=[mark])
    
    Attributes
    ----------
    mark : AnyMark
        A string describing the mark type (one of `"bar"`, `"circle"`, `"square"`, `"tick"`,
         `"line"`, * `"area"`, `"point"`, `"rule"`, `"geoshape"`, and `"text"`) or a [mark 
        definition object](https://vega.github.io/vega-lite/docs/mark.html#mark-def).
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : Encoding
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.  __Default value:__ - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its y-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the height will
         be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - 
        For y-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the height is [determined by the range step, paddings, and the
         cardinality of the field mapped to 
        y-channel](https://vega.github.io/vega-lite/docs/scale.html#band). Otherwise, if the
         `rangeStep` is `null`, the height will be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - If
         no field is mapped to `y` channel, the `height` will be the value of `rangeStep`.  
        __Note__: For plots with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the height of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : Projection
        An object defining properties of geographic projection.  Works with `"geoshape"` 
        marks and `"point"` or `"line"` marks that have `latitude` and `"longitude"` 
        channels.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.  __Default value:__ This will be determined by the 
        following rules:  - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its x-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the width will 
        be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - For
         x-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the width is [determined by the range step, paddings, and the 
        cardinality of the field mapped to 
        x-channel](https://vega.github.io/vega-lite/docs/scale.html#band).   Otherwise, if 
        the `rangeStep` is `null`, the width will be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - If 
        no field is mapped to `x` channel, the `width` will be the value of 
        [`config.scale.textXRangeStep`](https://vega.github.io/vega-lite/docs/size.html#default-width-and-height)
         for `text` mark and the value of `rangeStep` for other marks.  __Note:__ For plots 
        with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the width of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    """
    _schema = {'$ref': '#/definitions/CompositeUnitSpecAlias'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, selection=Undefined,
                 title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(CompositeUnitSpecAlias, self).__init__(mark=mark, data=data, description=description,
                                                     encoding=encoding, height=height, name=name,
                                                     projection=projection, selection=selection,
                                                     title=title, transform=transform, width=width,
                                                     **kwds)


class FacetedCompositeUnitSpecAlias(VegaLiteSchema):
    """FacetedCompositeUnitSpecAlias schema wrapper
    
    Mapping(required=[mark])
    
    Attributes
    ----------
    mark : AnyMark
        A string describing the mark type (one of `"bar"`, `"circle"`, `"square"`, `"tick"`,
         `"line"`, * `"area"`, `"point"`, `"rule"`, `"geoshape"`, and `"text"`) or a [mark 
        definition object](https://vega.github.io/vega-lite/docs/mark.html#mark-def).
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : EncodingWithFacet
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.  __Default value:__ - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its y-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the height will
         be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - 
        For y-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the height is [determined by the range step, paddings, and the
         cardinality of the field mapped to 
        y-channel](https://vega.github.io/vega-lite/docs/scale.html#band). Otherwise, if the
         `rangeStep` is `null`, the height will be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - If
         no field is mapped to `y` channel, the `height` will be the value of `rangeStep`.  
        __Note__: For plots with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the height of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : Projection
        An object defining properties of geographic projection.  Works with `"geoshape"` 
        marks and `"point"` or `"line"` marks that have `latitude` and `"longitude"` 
        channels.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.  __Default value:__ This will be determined by the 
        following rules:  - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its x-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the width will 
        be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - For
         x-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the width is [determined by the range step, paddings, and the 
        cardinality of the field mapped to 
        x-channel](https://vega.github.io/vega-lite/docs/scale.html#band).   Otherwise, if 
        the `rangeStep` is `null`, the width will be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - If 
        no field is mapped to `x` channel, the `width` will be the value of 
        [`config.scale.textXRangeStep`](https://vega.github.io/vega-lite/docs/size.html#default-width-and-height)
         for `text` mark and the value of `rangeStep` for other marks.  __Note:__ For plots 
        with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the width of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    """
    _schema = {'$ref': '#/definitions/FacetedCompositeUnitSpecAlias'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, selection=Undefined,
                 title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(FacetedCompositeUnitSpecAlias, self).__init__(mark=mark, data=data,
                                                            description=description, encoding=encoding,
                                                            height=height, name=name,
                                                            projection=projection, selection=selection,
                                                            title=title, transform=transform,
                                                            width=width, **kwds)


class VConcatSpec(VegaLiteSchema):
    """VConcatSpec schema wrapper
    
    Mapping(required=[vconcat])
    
    Attributes
    ----------
    vconcat : List(Spec)
        A list of views that should be concatenated and put into a column.
    data : Data
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : Resolve
        Scale, axis, and legend resolutions for vertically concatenated charts.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/VConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, data=Undefined, description=Undefined, name=Undefined,
                 resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(VConcatSpec, self).__init__(vconcat=vconcat, data=data, description=description,
                                          name=name, resolve=resolve, title=title, transform=transform,
                                          **kwds)


class GeoType(VegaLiteSchema):
    """GeoType schema wrapper
    
    enum('latitude', 'longitude', 'geojson')
    """
    _schema = {'$ref': '#/definitions/GeoType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(GeoType, self).__init__(*args)


class Header(VegaLiteSchema):
    """Header schema wrapper
    
    Mapping(required=[])
    Headers of row / column channels for faceted plots.
    
    Attributes
    ----------
    format : string
        The formatting pattern for labels. This is D3's [number format 
        pattern](https://github.com/d3/d3-format#locale_format) for quantitative fields and 
        D3's [time format pattern](https://github.com/d3/d3-time-format#locale_format) for 
        time field.  See the [format documentation](format.html) for more information.  
        __Default value:__  derived from [numberFormat](config.html#format) config for 
        quantitative fields and from [timeFormat](config.html#format) config for temporal 
        fields.
    labelAngle : float
        The rotation angle of the header labels.  __Default value:__ `0`.
    title : anyOf(string, None)
        A title for the field. If `null`, the title will be removed.  __Default value:__  
        derived from the field's name and transformation function (`aggregate`, `bin` and 
        `timeUnit`).  If the field has an aggregate function, the function is displayed as a
         part of the title (e.g., `"Sum of Profit"`). If the field is binned or has a time 
        unit applied, the applied function will be denoted in parentheses (e.g., `"Profit 
        (binned)"`, `"Transaction Date (year-month)"`).  Otherwise, the title is simply the 
        field name.  __Note__: You can customize the default field title format by providing
         the [`fieldTitle` property in the [config](config.html) or [`fieldTitle` function 
        via the `compile` function's options](compile.html#field-title).
    """
    _schema = {'$ref': '#/definitions/Header'}
    _rootschema = Root._schema

    def __init__(self, format=Undefined, labelAngle=Undefined, title=Undefined, **kwds):
        super(Header, self).__init__(format=format, labelAngle=labelAngle, title=title, **kwds)


class HorizontalAlign(VegaLiteSchema):
    """HorizontalAlign schema wrapper
    
    enum('left', 'right', 'center')
    """
    _schema = {'$ref': '#/definitions/HorizontalAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(HorizontalAlign, self).__init__(*args)


class InlineData(VegaLiteSchema):
    """InlineData schema wrapper
    
    Mapping(required=[values])
    
    Attributes
    ----------
    values : InlineDataset
        The full data set, included inline. This can be an array of objects or primitive 
        values or a string. Arrays of primitive values are ingested as objects with a `data`
         property. Strings are parsed according to the specified format type.
    format : DataFormat
        An object that specifies the format for parsing the data values.
    """
    _schema = {'$ref': '#/definitions/InlineData'}
    _rootschema = Root._schema

    def __init__(self, values=Undefined, format=Undefined, **kwds):
        super(InlineData, self).__init__(values=values, format=format, **kwds)


class InlineDataset(VegaLiteSchema):
    """InlineDataset schema wrapper
    
    anyOf(List(float), List(string), List(boolean), List(Mapping(required=[])), string, 
    Mapping(required=[]))
    """
    _schema = {'$ref': '#/definitions/InlineDataset'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(InlineDataset, self).__init__(*args, **kwds)


class Interpolate(VegaLiteSchema):
    """Interpolate schema wrapper
    
    enum('linear', 'linear-closed', 'step', 'step-before', 'step-after', 'basis', 'basis-open', 
    'basis-closed', 'cardinal', 'cardinal-open', 'cardinal-closed', 'bundle', 'monotone')
    """
    _schema = {'$ref': '#/definitions/Interpolate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Interpolate, self).__init__(*args)


class IntervalSelection(VegaLiteSchema):
    """IntervalSelection schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : enum('interval')
    
    bind : enum('scales')
        Establishes a two-way binding between the interval selection and the scales used 
        within the same view. This allows a user to interactively pan and zoom the view.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection. When 
        set to `none`, empty selections contain no data values.
    encodings : List(SingleDefChannel)
        An array of encoding channels. The corresponding data field values must match for a 
        data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to fall within the 
        selection.
    mark : BrushConfig
        An interval selection also adds a rectangle mark to depict the extents of the 
        interval. The `mark` property can be used to customize the appearance of the mark.
    on : VgEventStream
        A [Vega event stream](https://vega.github.io/vega/docs/event-streams/) (object or 
        selector) that triggers the selection. For interval selections, the event stream 
        must specify a [start and 
        end](https://vega.github.io/vega/docs/event-streams/#between-filters).
    resolve : SelectionResolution
        With layered and multi-view displays, a strategy that determines how selections' 
        data queries are resolved when applied in a filter transform, conditional encoding 
        rule, or scale domain.
    translate : anyOf(string, boolean)
        When truthy, allows a user to interactively move an interval selection 
        back-and-forth. Can be `true`, `false` (to disable panning), or a [Vega event stream
         definition](https://vega.github.io/vega/docs/event-streams/) which must include a 
        start and end event to trigger continuous panning.  __Default value:__ `true`, which
         corresponds to `[mousedown, window:mouseup] > window:mousemove!` which corresponds 
        to clicks and dragging within an interval selection to reposition it.
    zoom : anyOf(string, boolean)
        When truthy, allows a user to interactively resize an interval selection. Can be 
        `true`, `false` (to disable zooming), or a [Vega event stream 
        definition](https://vega.github.io/vega/docs/event-streams/). Currently, only 
        `wheel` events are supported.   __Default value:__ `true`, which corresponds to 
        `wheel!`.
    """
    _schema = {'$ref': '#/definitions/IntervalSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, empty=Undefined, encodings=Undefined,
                 fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined,
                 zoom=Undefined, **kwds):
        super(IntervalSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings,
                                                fields=fields, mark=mark, on=on, resolve=resolve,
                                                translate=translate, zoom=zoom, **kwds)


class IntervalSelectionConfig(VegaLiteSchema):
    """IntervalSelectionConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    bind : enum('scales')
        Establishes a two-way binding between the interval selection and the scales used 
        within the same view. This allows a user to interactively pan and zoom the view.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection. When 
        set to `none`, empty selections contain no data values.
    encodings : List(SingleDefChannel)
        An array of encoding channels. The corresponding data field values must match for a 
        data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to fall within the 
        selection.
    mark : BrushConfig
        An interval selection also adds a rectangle mark to depict the extents of the 
        interval. The `mark` property can be used to customize the appearance of the mark.
    on : VgEventStream
        A [Vega event stream](https://vega.github.io/vega/docs/event-streams/) (object or 
        selector) that triggers the selection. For interval selections, the event stream 
        must specify a [start and 
        end](https://vega.github.io/vega/docs/event-streams/#between-filters).
    resolve : SelectionResolution
        With layered and multi-view displays, a strategy that determines how selections' 
        data queries are resolved when applied in a filter transform, conditional encoding 
        rule, or scale domain.
    translate : anyOf(string, boolean)
        When truthy, allows a user to interactively move an interval selection 
        back-and-forth. Can be `true`, `false` (to disable panning), or a [Vega event stream
         definition](https://vega.github.io/vega/docs/event-streams/) which must include a 
        start and end event to trigger continuous panning.  __Default value:__ `true`, which
         corresponds to `[mousedown, window:mouseup] > window:mousemove!` which corresponds 
        to clicks and dragging within an interval selection to reposition it.
    zoom : anyOf(string, boolean)
        When truthy, allows a user to interactively resize an interval selection. Can be 
        `true`, `false` (to disable zooming), or a [Vega event stream 
        definition](https://vega.github.io/vega/docs/event-streams/). Currently, only 
        `wheel` events are supported.   __Default value:__ `true`, which corresponds to 
        `wheel!`.
    """
    _schema = {'$ref': '#/definitions/IntervalSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined,
                 mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined,
                 **kwds):
        super(IntervalSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings,
                                                      fields=fields, mark=mark, on=on, resolve=resolve,
                                                      translate=translate, zoom=zoom, **kwds)


class JsonDataFormat(VegaLiteSchema):
    """JsonDataFormat schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    parse : anyOf(enum('auto'), Mapping(required=[]))
        If set to auto (the default), perform automatic type inference to determine the 
        desired data types. Alternatively, a parsing directive object can be provided for 
        explicit data types. Each property of the object corresponds to a field name, and 
        the value to the desired data type (one of `"number"`, `"boolean"` or `"date"`). For
         example, `"parse": {"modified_on": "date"}` parses the `modified_on` field in each 
        input record a Date value.  For `"date"`, we parse data based using Javascript's 
        [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse).
         For Specific date formats can be provided (e.g., `{foo: 'date:"%m%d%Y"'}`), using 
        the [d3-time-format syntax](https://github.com/d3/d3-time-format#locale_format). UTC
         date format parsing is supported similarly (e.g., `{foo: 'utc:"%m%d%Y"'}`). See 
        more about [UTC time](timeunit.html#utc)
    property : string
        The JSON property containing the desired data. This parameter can be used when the 
        loaded JSON file may have surrounding structure or meta-data. For example 
        `"property": "values.features"` is equivalent to retrieving `json.values.features` 
        from the loaded JSON object.
    type : enum('json')
        Type of input data: `"json"`, `"csv"`, `"tsv"`. The default format type is 
        determined by the extension of the file URL. If no extension is detected, `"json"` 
        will be used by default.
    """
    _schema = {'$ref': '#/definitions/JsonDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, property=Undefined, type=Undefined, **kwds):
        super(JsonDataFormat, self).__init__(parse=parse, property=property, type=type, **kwds)


class Legend(VegaLiteSchema):
    """Legend schema wrapper
    
    Mapping(required=[])
    Properties of a legend or boolean flag for determining whether to show it.
    
    Attributes
    ----------
    entryPadding : float
        Padding (in pixels) between legend entries in a symbol legend.
    format : string
        The formatting pattern for labels. This is D3's [number format 
        pattern](https://github.com/d3/d3-format#locale_format) for quantitative fields and 
        D3's [time format pattern](https://github.com/d3/d3-time-format#locale_format) for 
        time field.  See the [format documentation](format.html) for more information.  
        __Default value:__  derived from [numberFormat](config.html#format) config for 
        quantitative fields and from [timeFormat](config.html#format) config for temporal 
        fields.
    offset : float
        The offset, in pixels, by which to displace the legend from the edge of the 
        enclosing group or data rectangle.  __Default value:__  `0`
    orient : LegendOrient
        The orientation of the legend, which determines how the legend is positioned within 
        the scene. One of "left", "right", "top-left", "top-right", "bottom-left", 
        "bottom-right", "none".  __Default value:__ `"right"`
    padding : float
        The padding, in pixels, between the legend and axis.
    tickCount : float
        The desired number of tick values for quantitative legends.
    title : anyOf(string, None)
        A title for the field. If `null`, the title will be removed.  __Default value:__  
        derived from the field's name and transformation function (`aggregate`, `bin` and 
        `timeUnit`).  If the field has an aggregate function, the function is displayed as a
         part of the title (e.g., `"Sum of Profit"`). If the field is binned or has a time 
        unit applied, the applied function will be denoted in parentheses (e.g., `"Profit 
        (binned)"`, `"Transaction Date (year-month)"`).  Otherwise, the title is simply the 
        field name.  __Note__: You can customize the default field title format by providing
         the [`fieldTitle` property in the [config](config.html) or [`fieldTitle` function 
        via the `compile` function's options](compile.html#field-title).
    type : enum('symbol', 'gradient')
        The type of the legend. Use `"symbol"` to create a discrete legend and `"gradient"` 
        for a continuous color gradient.  __Default value:__ `"gradient"` for non-binned 
        quantitative fields and temporal fields; `"symbol"` otherwise.
    values : anyOf(List(float), List(string), List(DateTime))
        Explicitly set the visible legend values.
    zindex : float
        A non-positive integer indicating z-index of the legend. If zindex is 0, legend 
        should be drawn behind all chart elements. To put them in front, use zindex = 1.
    """
    _schema = {'$ref': '#/definitions/Legend'}
    _rootschema = Root._schema

    def __init__(self, entryPadding=Undefined, format=Undefined, offset=Undefined, orient=Undefined,
                 padding=Undefined, tickCount=Undefined, title=Undefined, type=Undefined,
                 values=Undefined, zindex=Undefined, **kwds):
        super(Legend, self).__init__(entryPadding=entryPadding, format=format, offset=offset,
                                     orient=orient, padding=padding, tickCount=tickCount, title=title,
                                     type=type, values=values, zindex=zindex, **kwds)


class LegendConfig(VegaLiteSchema):
    """LegendConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    cornerRadius : float
        Corner radius for the full legend.
    entryPadding : float
        Padding (in pixels) between legend entries in a symbol legend.
    fillColor : string
        Background fill color for the full legend.
    gradientHeight : float
        The height of the gradient, in pixels.
    gradientLabelBaseline : string
        Text baseline for color ramp gradient labels.
    gradientLabelLimit : float
        The maximum allowed length in pixels of color ramp gradient labels.
    gradientLabelOffset : float
        Vertical offset in pixels for color ramp gradient labels.
    gradientStrokeColor : string
        The color of the gradient stroke, can be in hex color code or regular color name.
    gradientStrokeWidth : float
        The width of the gradient stroke, in pixels.
    gradientWidth : float
        The width of the gradient, in pixels.
    labelAlign : string
        The alignment of the legend label, can be left, middle or right.
    labelBaseline : string
        The position of the baseline of legend label, can be top, middle or bottom.
    labelColor : string
        The color of the legend label, can be in hex color code or regular color name.
    labelFont : string
        The font of the legend label.
    labelFontSize : float
        The font size of legend label.  __Default value:__ `10`.
    labelLimit : float
        Maximum allowed pixel width of axis tick labels.
    labelOffset : float
        The offset of the legend label.
    offset : float
        The offset, in pixels, by which to displace the legend from the edge of the 
        enclosing group or data rectangle.  __Default value:__  `0`
    orient : LegendOrient
        The orientation of the legend, which determines how the legend is positioned within 
        the scene. One of "left", "right", "top-left", "top-right", "bottom-left", 
        "bottom-right", "none".  __Default value:__ `"right"`
    padding : float
        The padding, in pixels, between the legend and axis.
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.  __Default value:__  
        `false`
    strokeColor : string
        Border stroke color for the full legend.
    strokeDash : List(float)
        Border stroke dash pattern for the full legend.
    strokeWidth : float
        Border stroke width for the full legend.
    symbolColor : string
        The color of the legend symbol,
    symbolSize : float
        The size of the legend symbol, in pixels.
    symbolStrokeWidth : float
        The width of the symbol's stroke.
    symbolType : string
        Default shape type (such as "circle") for legend symbols.
    titleAlign : string
        Horizontal text alignment for legend titles.
    titleBaseline : string
        Vertical text baseline for legend titles.
    titleColor : string
        The color of the legend title, can be in hex color code or regular color name.
    titleFont : string
        The font of the legend title.
    titleFontSize : float
        The font size of the legend title.
    titleFontWeight : FontWeight
        The font weight of the legend title. This can be either a string (e.g `"bold"`, 
        `"normal"`) or a number (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` 
        and `"bold"` = `700`).
    titleLimit : float
        Maximum allowed pixel width of axis titles.
    titlePadding : float
        The padding, in pixels, between title and legend.
    """
    _schema = {'$ref': '#/definitions/LegendConfig'}
    _rootschema = Root._schema

    def __init__(self, cornerRadius=Undefined, entryPadding=Undefined, fillColor=Undefined,
                 gradientHeight=Undefined, gradientLabelBaseline=Undefined,
                 gradientLabelLimit=Undefined, gradientLabelOffset=Undefined,
                 gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientWidth=Undefined,
                 labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined,
                 labelOffset=Undefined, offset=Undefined, orient=Undefined, padding=Undefined,
                 shortTimeLabels=Undefined, strokeColor=Undefined, strokeDash=Undefined,
                 strokeWidth=Undefined, symbolColor=Undefined, symbolSize=Undefined,
                 symbolStrokeWidth=Undefined, symbolType=Undefined, titleAlign=Undefined,
                 titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined,
                 titlePadding=Undefined, **kwds):
        super(LegendConfig, self).__init__(cornerRadius=cornerRadius, entryPadding=entryPadding,
                                           fillColor=fillColor, gradientHeight=gradientHeight,
                                           gradientLabelBaseline=gradientLabelBaseline,
                                           gradientLabelLimit=gradientLabelLimit,
                                           gradientLabelOffset=gradientLabelOffset,
                                           gradientStrokeColor=gradientStrokeColor,
                                           gradientStrokeWidth=gradientStrokeWidth,
                                           gradientWidth=gradientWidth, labelAlign=labelAlign,
                                           labelBaseline=labelBaseline, labelColor=labelColor,
                                           labelFont=labelFont, labelFontSize=labelFontSize,
                                           labelLimit=labelLimit, labelOffset=labelOffset,
                                           offset=offset, orient=orient, padding=padding,
                                           shortTimeLabels=shortTimeLabels, strokeColor=strokeColor,
                                           strokeDash=strokeDash, strokeWidth=strokeWidth,
                                           symbolColor=symbolColor, symbolSize=symbolSize,
                                           symbolStrokeWidth=symbolStrokeWidth, symbolType=symbolType,
                                           titleAlign=titleAlign, titleBaseline=titleBaseline,
                                           titleColor=titleColor, titleFont=titleFont,
                                           titleFontSize=titleFontSize, titleFontWeight=titleFontWeight,
                                           titleLimit=titleLimit, titlePadding=titlePadding, **kwds)


class LegendOrient(VegaLiteSchema):
    """LegendOrient schema wrapper
    
    enum('left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'none')
    """
    _schema = {'$ref': '#/definitions/LegendOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LegendOrient, self).__init__(*args)


class LegendResolveMap(VegaLiteSchema):
    """LegendResolveMap schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    color : ResolveMode
    
    fill : ResolveMode
    
    opacity : ResolveMode
    
    shape : ResolveMode
    
    size : ResolveMode
    
    stroke : ResolveMode
    
    """
    _schema = {'$ref': '#/definitions/LegendResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, fill=Undefined, opacity=Undefined, shape=Undefined,
                 size=Undefined, stroke=Undefined, **kwds):
        super(LegendResolveMap, self).__init__(color=color, fill=fill, opacity=opacity, shape=shape,
                                               size=size, stroke=stroke, **kwds)


class LocalMultiTimeUnit(VegaLiteSchema):
    """LocalMultiTimeUnit schema wrapper
    
    enum('yearquarter', 'yearquartermonth', 'yearmonth', 'yearmonthdate', 'yearmonthdatehours', 
    'yearmonthdatehoursminutes', 'yearmonthdatehoursminutesseconds', 'quartermonth', 
    'monthdate', 'hoursminutes', 'hoursminutesseconds', 'minutesseconds', 'secondsmilliseconds')
    """
    _schema = {'$ref': '#/definitions/LocalMultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LocalMultiTimeUnit, self).__init__(*args)


class LocalSingleTimeUnit(VegaLiteSchema):
    """LocalSingleTimeUnit schema wrapper
    
    enum('year', 'quarter', 'month', 'day', 'date', 'hours', 'minutes', 'seconds', 
    'milliseconds')
    """
    _schema = {'$ref': '#/definitions/LocalSingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LocalSingleTimeUnit, self).__init__(*args)


class LogicalAndPredicate(VegaLiteSchema):
    """LogicalAndPredicate schema wrapper
    
    Mapping(required=[and])
    
    Attributes
    ----------
    """
    _schema = {'$ref': '#/definitions/LogicalAnd<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(LogicalAndPredicate, self).__init__(**kwds)


class SelectionAnd(VegaLiteSchema):
    """SelectionAnd schema wrapper
    
    Mapping(required=[and])
    
    Attributes
    ----------
    """
    _schema = {'$ref': '#/definitions/SelectionAnd'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionAnd, self).__init__(**kwds)


class LogicalNotPredicate(VegaLiteSchema):
    """LogicalNotPredicate schema wrapper
    
    Mapping(required=[not])
    
    Attributes
    ----------
    """
    _schema = {'$ref': '#/definitions/LogicalNot<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(LogicalNotPredicate, self).__init__(**kwds)


class SelectionNot(VegaLiteSchema):
    """SelectionNot schema wrapper
    
    Mapping(required=[not])
    
    Attributes
    ----------
    """
    _schema = {'$ref': '#/definitions/SelectionNot'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionNot, self).__init__(**kwds)


class LogicalOperandPredicate(VegaLiteSchema):
    """LogicalOperandPredicate schema wrapper
    
    anyOf(LogicalNotPredicate, LogicalAndPredicate, LogicalOrPredicate, Predicate)
    """
    _schema = {'$ref': '#/definitions/LogicalOperand<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LogicalOperandPredicate, self).__init__(*args, **kwds)


class SelectionOperand(VegaLiteSchema):
    """SelectionOperand schema wrapper
    
    anyOf(SelectionNot, SelectionAnd, SelectionOr, string)
    """
    _schema = {'$ref': '#/definitions/SelectionOperand'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionOperand, self).__init__(*args, **kwds)


class LogicalOrPredicate(VegaLiteSchema):
    """LogicalOrPredicate schema wrapper
    
    Mapping(required=[or])
    
    Attributes
    ----------
    """
    _schema = {'$ref': '#/definitions/LogicalOr<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(LogicalOrPredicate, self).__init__(**kwds)


class SelectionOr(VegaLiteSchema):
    """SelectionOr schema wrapper
    
    Mapping(required=[or])
    
    Attributes
    ----------
    """
    _schema = {'$ref': '#/definitions/SelectionOr'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionOr, self).__init__(**kwds)


class LookupData(VegaLiteSchema):
    """LookupData schema wrapper
    
    Mapping(required=[data, key])
    
    Attributes
    ----------
    data : Data
        Secondary data source to lookup in.
    key : string
        Key in data to lookup.
    fields : List(string)
        Fields in foreign data to lookup. If not specified, the entire object is queried.
    """
    _schema = {'$ref': '#/definitions/LookupData'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, key=Undefined, fields=Undefined, **kwds):
        super(LookupData, self).__init__(data=data, key=key, fields=fields, **kwds)


class LookupTransform(VegaLiteSchema):
    """LookupTransform schema wrapper
    
    Mapping(required=[lookup, from])
    
    Attributes
    ----------
    lookup : string
        Key in primary data source.
    default : string
        The default value to use if lookup fails.  __Default value:__ `null`
    """
    _schema = {'$ref': '#/definitions/LookupTransform'}
    _rootschema = Root._schema

    def __init__(self, lookup=Undefined, default=Undefined, **kwds):
        super(LookupTransform, self).__init__(lookup=lookup, default=default, **kwds)


class Mark(VegaLiteSchema):
    """Mark schema wrapper
    
    enum('area', 'bar', 'line', 'point', 'text', 'tick', 'rect', 'rule', 'circle', 'square', 
    'geoshape')
    All types of primitive marks.
    """
    _schema = {'$ref': '#/definitions/Mark'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Mark, self).__init__(*args)


class MarkConfig(VegaLiteSchema):
    """MarkConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    align : HorizontalAlign
        The horizontal alignment of the text. One of `"left"`, `"right"`, `"center"`.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : VerticalAlign
        The vertical alignment of the text. One of `"top"`, `"middle"`, `"bottom"`.  
        __Default value:__ `"middle"`
    color : string
        Default color.  Note that `fill` and `stroke` have higher precedence than `color` 
        and will override `color`.  __Default value:__ <span style="color: 
        #4682b4;">&#9632;</span> `"#4682b4"`  __Note:__ This property cannot be used in a 
        [style config](mark.html#style-config).
    cursor : enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 
    'wait', 'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop', 
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize', 
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize', 
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
        The mouse cursor used over the mark. Any valid [CSS cursor 
        type](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values) can be used.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ `1`
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.  
        __Default value:__ `true` for all marks except `point` and `false` for `point`.  
        __Applicable for:__ `bar`, `point`, `circle`, `square`, and `area` marks.  __Note:__
         This property cannot be used in a [style config](mark.html#style-config).
    font : string
        The typeface to set the text in (e.g., `"Helvetica Neue"`).
    fontSize : float
        The font size, in pixels.
    fontStyle : FontStyle
        The font style (e.g., `"italic"`).
    fontWeight : FontWeight
        The font weight. This can be either a string (e.g `"bold"`, `"normal"`) or a number 
        (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = `700`).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : Interpolate
        The line interpolation method to use for line and area marks. One of the following: 
        - `"linear"`: piecewise linear segments, as in a polyline. - `"linear-closed"`: 
        close the linear segments to form a polygon. - `"step"`: alternate between 
        horizontal and vertical segments, as in a step function. - `"step-before"`: 
        alternate between vertical and horizontal segments, as in a step function. - 
        `"step-after"`: alternate between horizontal and vertical segments, as in a step 
        function. - `"basis"`: a B-spline, with control point duplication on the ends. - 
        `"basis-open"`: an open B-spline; may not intersect the start or end. - 
        `"basis-closed"`: a closed B-spline, as in a loop. - `"cardinal"`: a Cardinal 
        spline, with control point duplication on the ends. - `"cardinal-open"`: an open 
        Cardinal spline; may not intersect the start or end, but will intersect other 
        control points. - `"cardinal-closed"`: a closed Cardinal spline, as in a loop. - 
        `"bundle"`: equivalent to basis, except the tension parameter is used to straighten 
        the spline. - `"monotone"`: cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels (default 0, indicating no limit). The 
        text value will be automatically truncated if the rendered size exceeds the limit.
    opacity : float
        The overall opacity (value between [0,1]).  __Default value:__ `0.7` for 
        non-aggregate plots with `point`, `tick`, `circle`, or `square` marks or layered 
        `bar` charts and `1` otherwise.
    orient : Orient
        The orientation of a non-stacked bar, tick, area, and line charts. The value is 
        either horizontal (default) or vertical. - For bar, rule and tick, this determines 
        whether the size of the bar and tick should be applied to x or y dimension. - For 
        area, this property determines the orient property of the Vega output. - For line, 
        this property determines the sort order of the points in the line if 
        `config.sortLineBy` is not specified. For stacked charts, this is always determined 
        by the orientation of the stack; therefore explicitly specified value will be 
        ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin 
        determined by the `x` and `y` properties.
    shape : string
        The default symbol shape to use. One of: `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or a custom SVG path.
          __Default value:__ `"circle"`
    size : float
        The pixel area each the point/circle/square. For example: in the case of circles, 
        the radius is determined in part by the square root of the size value.  __Default 
        value:__ `30`
    stroke : string
        Default Stroke Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ `1`
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area 
        marks).
    text : string
        Placeholder text if the `text` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by 
        the `x` and `y` properties. Values for `theta` follow the same convention of `arc` 
        mark `startAngle` and `endAngle` properties: angles are measured in radians, with 
        `0` indicating "north".
    """
    _schema = {'$ref': '#/definitions/MarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined,
                 opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, **kwds):
        super(MarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color,
                                         cursor=cursor, dx=dx, dy=dy, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         href=href, interpolate=interpolate, limit=limit,
                                         opacity=opacity, orient=orient, radius=radius, shape=shape,
                                         size=size, stroke=stroke, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, **kwds)


class MarkDef(VegaLiteSchema):
    """MarkDef schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : Mark
        The mark type. One of `"bar"`, `"circle"`, `"square"`, `"tick"`, `"line"`, `"area"`,
         `"point"`, `"geoshape"`, `"rule"`, and `"text"`.
    align : HorizontalAlign
        The horizontal alignment of the text. One of `"left"`, `"right"`, `"center"`.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : VerticalAlign
        The vertical alignment of the text. One of `"top"`, `"middle"`, `"bottom"`.  
        __Default value:__ `"middle"`
    clip : boolean
        Whether a mark be clipped to the enclosing group’s width and height.
    color : string
        Default color.  Note that `fill` and `stroke` have higher precedence than `color` 
        and will override `color`.  __Default value:__ <span style="color: 
        #4682b4;">&#9632;</span> `"#4682b4"`  __Note:__ This property cannot be used in a 
        [style config](mark.html#style-config).
    cursor : enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 
    'wait', 'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop', 
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize', 
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize', 
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
        The mouse cursor used over the mark. Any valid [CSS cursor 
        type](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values) can be used.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ `1`
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.  
        __Default value:__ `true` for all marks except `point` and `false` for `point`.  
        __Applicable for:__ `bar`, `point`, `circle`, `square`, and `area` marks.  __Note:__
         This property cannot be used in a [style config](mark.html#style-config).
    font : string
        The typeface to set the text in (e.g., `"Helvetica Neue"`).
    fontSize : float
        The font size, in pixels.
    fontStyle : FontStyle
        The font style (e.g., `"italic"`).
    fontWeight : FontWeight
        The font weight. This can be either a string (e.g `"bold"`, `"normal"`) or a number 
        (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = `700`).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : Interpolate
        The line interpolation method to use for line and area marks. One of the following: 
        - `"linear"`: piecewise linear segments, as in a polyline. - `"linear-closed"`: 
        close the linear segments to form a polygon. - `"step"`: alternate between 
        horizontal and vertical segments, as in a step function. - `"step-before"`: 
        alternate between vertical and horizontal segments, as in a step function. - 
        `"step-after"`: alternate between horizontal and vertical segments, as in a step 
        function. - `"basis"`: a B-spline, with control point duplication on the ends. - 
        `"basis-open"`: an open B-spline; may not intersect the start or end. - 
        `"basis-closed"`: a closed B-spline, as in a loop. - `"cardinal"`: a Cardinal 
        spline, with control point duplication on the ends. - `"cardinal-open"`: an open 
        Cardinal spline; may not intersect the start or end, but will intersect other 
        control points. - `"cardinal-closed"`: a closed Cardinal spline, as in a loop. - 
        `"bundle"`: equivalent to basis, except the tension parameter is used to straighten 
        the spline. - `"monotone"`: cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels (default 0, indicating no limit). The 
        text value will be automatically truncated if the rendered size exceeds the limit.
    opacity : float
        The overall opacity (value between [0,1]).  __Default value:__ `0.7` for 
        non-aggregate plots with `point`, `tick`, `circle`, or `square` marks or layered 
        `bar` charts and `1` otherwise.
    orient : Orient
        The orientation of a non-stacked bar, tick, area, and line charts. The value is 
        either horizontal (default) or vertical. - For bar, rule and tick, this determines 
        whether the size of the bar and tick should be applied to x or y dimension. - For 
        area, this property determines the orient property of the Vega output. - For line, 
        this property determines the sort order of the points in the line if 
        `config.sortLineBy` is not specified. For stacked charts, this is always determined 
        by the orientation of the stack; therefore explicitly specified value will be 
        ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin 
        determined by the `x` and `y` properties.
    shape : string
        The default symbol shape to use. One of: `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or a custom SVG path.
          __Default value:__ `"circle"`
    size : float
        The pixel area each the point/circle/square. For example: in the case of circles, 
        the radius is determined in part by the square root of the size value.  __Default 
        value:__ `30`
    stroke : string
        Default Stroke Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ `1`
    strokeWidth : float
        The stroke width, in pixels.
    style : anyOf(string, List(string))
        A string or array of strings indicating the name of custom styles to apply to the 
        mark. A style is a named collection of mark property defaults defined within the 
        [style configuration](mark.html#style-config). If style is an array, later styles 
        will override earlier styles. Any [mark properties](encoding.html#mark-prop) 
        explicitly defined within the `encoding` will override a style default.  __Default 
        value:__ The mark's name.  For example, a bar mark will have style `"bar"` by 
        default. __Note:__ Any specified style will augment the default style. For example, 
        a bar mark with `"style": "foo"` will receive from `config.style.bar` and 
        `config.style.foo` (the specified style `"foo"` has higher precedence).
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area 
        marks).
    text : string
        Placeholder text if the `text` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by 
        the `x` and `y` properties. Values for `theta` follow the same convention of `arc` 
        mark `startAngle` and `endAngle` properties: angles are measured in radians, with 
        `0` indicating "north".
    """
    _schema = {'$ref': '#/definitions/MarkDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, align=Undefined, angle=Undefined, baseline=Undefined,
                 clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined,
                 fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                 interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, **kwds):
        super(MarkDef, self).__init__(type=type, align=align, angle=angle, baseline=baseline, clip=clip,
                                      color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                                      fillOpacity=fillOpacity, filled=filled, font=font,
                                      fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                      href=href, interpolate=interpolate, limit=limit, opacity=opacity,
                                      orient=orient, radius=radius, shape=shape, size=size,
                                      stroke=stroke, strokeDash=strokeDash,
                                      strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                      strokeWidth=strokeWidth, style=style, tension=tension, text=text,
                                      theta=theta, **kwds)


class Month(VegaLiteSchema):
    """Month schema wrapper
    
    float
    """
    _schema = {'$ref': '#/definitions/Month'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Month, self).__init__(*args)


class MultiSelection(VegaLiteSchema):
    """MultiSelection schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : enum('multi')
    
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection. When 
        set to `none`, empty selections contain no data values.
    encodings : List(SingleDefChannel)
        An array of encoding channels. The corresponding data field values must match for a 
        data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to fall within the 
        selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete 
        selection. The data value _nearest_ the mouse cursor is added to the selection.  See
         the [nearest transform](nearest.html) documentation for more information.
    on : VgEventStream
        A [Vega event stream](https://vega.github.io/vega/docs/event-streams/) (object or 
        selector) that triggers the selection. For interval selections, the event stream 
        must specify a [start and 
        end](https://vega.github.io/vega/docs/event-streams/#between-filters).
    resolve : SelectionResolution
        With layered and multi-view displays, a strategy that determines how selections' 
        data queries are resolved when applied in a filter transform, conditional encoding 
        rule, or scale domain.
    toggle : anyOf(string, boolean)
        Controls whether data values should be toggled or only ever inserted into multi 
        selections. Can be `true`, `false` (for insertion only), or a [Vega 
        expression](https://vega.github.io/vega/docs/expressions/).  __Default value:__ 
        `true`, which corresponds to `event.shiftKey` (i.e., data values are toggled when a 
        user interacts with the shift-key pressed).  See the [toggle transform](toggle.html)
         documentation for more information.
    """
    _schema = {'$ref': '#/definitions/MultiSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined,
                 nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelection, self).__init__(type=type, empty=empty, encodings=encodings, fields=fields,
                                             nearest=nearest, on=on, resolve=resolve, toggle=toggle,
                                             **kwds)


class MultiSelectionConfig(VegaLiteSchema):
    """MultiSelectionConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection. When 
        set to `none`, empty selections contain no data values.
    encodings : List(SingleDefChannel)
        An array of encoding channels. The corresponding data field values must match for a 
        data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to fall within the 
        selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete 
        selection. The data value _nearest_ the mouse cursor is added to the selection.  See
         the [nearest transform](nearest.html) documentation for more information.
    on : VgEventStream
        A [Vega event stream](https://vega.github.io/vega/docs/event-streams/) (object or 
        selector) that triggers the selection. For interval selections, the event stream 
        must specify a [start and 
        end](https://vega.github.io/vega/docs/event-streams/#between-filters).
    resolve : SelectionResolution
        With layered and multi-view displays, a strategy that determines how selections' 
        data queries are resolved when applied in a filter transform, conditional encoding 
        rule, or scale domain.
    toggle : anyOf(string, boolean)
        Controls whether data values should be toggled or only ever inserted into multi 
        selections. Can be `true`, `false` (for insertion only), or a [Vega 
        expression](https://vega.github.io/vega/docs/expressions/).  __Default value:__ 
        `true`, which corresponds to `event.shiftKey` (i.e., data values are toggled when a 
        user interacts with the shift-key pressed).  See the [toggle transform](toggle.html)
         documentation for more information.
    """
    _schema = {'$ref': '#/definitions/MultiSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined,
                 on=Undefined, resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelectionConfig, self).__init__(empty=empty, encodings=encodings, fields=fields,
                                                   nearest=nearest, on=on, resolve=resolve,
                                                   toggle=toggle, **kwds)


class MultiTimeUnit(VegaLiteSchema):
    """MultiTimeUnit schema wrapper
    
    anyOf(LocalMultiTimeUnit, UtcMultiTimeUnit)
    """
    _schema = {'$ref': '#/definitions/MultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(MultiTimeUnit, self).__init__(*args, **kwds)


class NamedData(VegaLiteSchema):
    """NamedData schema wrapper
    
    Mapping(required=[name])
    
    Attributes
    ----------
    name : string
        Provide a placeholder name and bind data at runtime.
    format : DataFormat
        An object that specifies the format for parsing the data.
    """
    _schema = {'$ref': '#/definitions/NamedData'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, format=Undefined, **kwds):
        super(NamedData, self).__init__(name=name, format=format, **kwds)


class NiceTime(VegaLiteSchema):
    """NiceTime schema wrapper
    
    enum('second', 'minute', 'hour', 'day', 'week', 'month', 'year')
    """
    _schema = {'$ref': '#/definitions/NiceTime'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(NiceTime, self).__init__(*args)


class OrderFieldDef(VegaLiteSchema):
    """OrderFieldDef schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    sort : SortOrder
        The sort order. One of `"ascending"` (default) or `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/OrderFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, **kwds):
        super(OrderFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                            sort=sort, timeUnit=timeUnit, **kwds)


class Orient(VegaLiteSchema):
    """Orient schema wrapper
    
    enum('horizontal', 'vertical')
    """
    _schema = {'$ref': '#/definitions/Orient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Orient, self).__init__(*args)


class Padding(VegaLiteSchema):
    """Padding schema wrapper
    
    anyOf(float, Mapping(required=[]))
    """
    _schema = {'$ref': '#/definitions/Padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Padding, self).__init__(*args, **kwds)


class PositionFieldDef(VegaLiteSchema):
    """PositionFieldDef schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, 
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, 
        `"longitude"`, and `"geojson"`) when a [geographic 
        projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).  __Default value:__ `undefined` (None)
    axis : anyOf(Axis, None)
        An object defining properties of axis's gridlines, ticks and labels. If `null`, the 
        axis for the encoding channel will be removed.  __Default value:__ If undefined, 
        default [axis properties](https://vega.github.io/vega-lite/docs/axis.html) are 
        applied.
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning 
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, 
        default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be
         applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data 
        value or an object defining iterated values from the 
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ 
        Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., 
        `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or 
        brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., 
        `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field 
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field`
         is not required if `aggregate` is `count`.
    scale : anyOf(Scale, None)
        An object defining properties of the channel's scale, which is the function that 
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
         (pixels, colors, sizes) of the encoding channels.  If `null`, the scale will be 
        [disabled and the data value will be directly 
        encoded](https://vega.github.io/vega-lite/docs/scale.html#disable).  __Default 
        value:__ If undefined, default [scale 
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, 
        `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can
         also be a [sort field definition 
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default 
        value:__ `"ascending"`
    stack : anyOf(StackOffset, None)
        Type of stacking offset if the field should be stacked. `stack` is only applicable 
        for `x` and `y` channels with continuous domains. For example, `stack` of `y` can be
         used to customize stacking for a vertical bar chart.  `stack` can be one of the 
        following values: - `"zero"`: stacking with baseline offset at zero value of the 
        scale (for creating typical stacked 
        [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and 
        [area](https://vega.github.io/vega-lite/docs/stack.html#area) chart). - 
        `"normalize"` - stacking with normalized domain (for creating [normalized stacked 
        bar and area charts](https://vega.github.io/vega-lite/docs/stack.html#normalized). 
        <br/> -`"center"` - stacking with center baseline (for 
        [streamgraph](https://vega.github.io/vega-lite/docs/stack.html#streamgraph)). - 
        `null` - No-stacking. This will produce layered 
        [bar](https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart) and area 
        chart.  __Default value:__ `zero` for plots with all of the following conditions are
         true: (1) the mark is `bar` or `area`; (2) the stacked measure channel (x or y) has
         a linear scale; (3) At least one of non-position channels mapped to an unaggregated
         field that is different from x and y.  Otherwise, `null` by default.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a 
        temporal field that gets casted as 
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ 
        `undefined` (None)
    """
    _schema = {'$ref': '#/definitions/PositionFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined,
                 **kwds):
        super(PositionFieldDef, self).__init__(type=type, aggregate=aggregate, axis=axis, bin=bin,
                                               field=field, scale=scale, sort=sort, stack=stack,
                                               timeUnit=timeUnit, **kwds)


class Predicate(VegaLiteSchema):
    """Predicate schema wrapper
    
    anyOf(FieldEqualPredicate, FieldRangePredicate, FieldOneOfPredicate, SelectionPredicate, 
    string)
    """
    _schema = {'$ref': '#/definitions/Predicate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Predicate, self).__init__(*args, **kwds)


class Projection(VegaLiteSchema):
    """Projection schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    center : List(float)
        Sets the projection’s center to the specified center, a two-element array of 
        longitude and latitude in degrees.  __Default value:__ `[0, 0]`
    clipAngle : float
        Sets the projection’s clipping circle radius to the specified angle in degrees. If 
        `null`, switches to [antimeridian](http://bl.ocks.org/mbostock/3788999) cutting 
        rather than small-circle clipping.
    clipExtent : List(List(float))
        Sets the projection’s viewport clip extent to the specified bounds in pixels. The 
        extent bounds are specified as an array `[[x0, y0], [x1, y1]]`, where `x0` is the 
        left-side of the viewport, `y0` is the top, `x1` is the right and `y1` is the 
        bottom. If `null`, no viewport clipping is performed.
    coefficient : float
    
    distance : float
    
    fraction : float
    
    lobes : float
    
    parallel : float
    
    precision : Mapping(required=[length])
        Sets the threshold for the projection’s [adaptive 
        resampling](http://bl.ocks.org/mbostock/3795544) to the specified value in pixels. 
        This value corresponds to the [Douglas–Peucker 
        distance](http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm).
         If precision is not specified, returns the projection’s current resampling 
        precision which defaults to `√0.5 ≅ 0.70710…`.
    radius : float
    
    ratio : float
    
    rotate : List(float)
        Sets the projection’s three-axis rotation to the specified angles, which must be a 
        two- or three-element array of numbers [`lambda`, `phi`, `gamma`] specifying the 
        rotation angles in degrees about each spherical axis. (These correspond to yaw, 
        pitch and roll.)  __Default value:__ `[0, 0, 0]`
    spacing : float
    
    tilt : float
    
    type : ProjectionType
        The cartographic projection to use. This value is case-insensitive, for example 
        `"albers"` and `"Albers"` indicate the same projection type. You can find all valid 
        projection types [in the 
        documentation](https://vega.github.io/vega-lite/docs/projection.html#projection-types).
          __Default value:__ `mercator`
    """
    _schema = {'$ref': '#/definitions/Projection'}
    _rootschema = Root._schema

    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined,
                 coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined,
                 parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined,
                 rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined, **kwds):
        super(Projection, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent,
                                         coefficient=coefficient, distance=distance, fraction=fraction,
                                         lobes=lobes, parallel=parallel, precision=precision,
                                         radius=radius, ratio=ratio, rotate=rotate, spacing=spacing,
                                         tilt=tilt, type=type, **kwds)


class ProjectionConfig(VegaLiteSchema):
    """ProjectionConfig schema wrapper
    
    Mapping(required=[])
    Any property of Projection can be in config
    
    Attributes
    ----------
    center : List(float)
        Sets the projection’s center to the specified center, a two-element array of 
        longitude and latitude in degrees.  __Default value:__ `[0, 0]`
    clipAngle : float
        Sets the projection’s clipping circle radius to the specified angle in degrees. If 
        `null`, switches to [antimeridian](http://bl.ocks.org/mbostock/3788999) cutting 
        rather than small-circle clipping.
    clipExtent : List(List(float))
        Sets the projection’s viewport clip extent to the specified bounds in pixels. The 
        extent bounds are specified as an array `[[x0, y0], [x1, y1]]`, where `x0` is the 
        left-side of the viewport, `y0` is the top, `x1` is the right and `y1` is the 
        bottom. If `null`, no viewport clipping is performed.
    coefficient : float
    
    distance : float
    
    fraction : float
    
    lobes : float
    
    parallel : float
    
    precision : Mapping(required=[length])
        Sets the threshold for the projection’s [adaptive 
        resampling](http://bl.ocks.org/mbostock/3795544) to the specified value in pixels. 
        This value corresponds to the [Douglas–Peucker 
        distance](http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm).
         If precision is not specified, returns the projection’s current resampling 
        precision which defaults to `√0.5 ≅ 0.70710…`.
    radius : float
    
    ratio : float
    
    rotate : List(float)
        Sets the projection’s three-axis rotation to the specified angles, which must be a 
        two- or three-element array of numbers [`lambda`, `phi`, `gamma`] specifying the 
        rotation angles in degrees about each spherical axis. (These correspond to yaw, 
        pitch and roll.)  __Default value:__ `[0, 0, 0]`
    spacing : float
    
    tilt : float
    
    type : ProjectionType
        The cartographic projection to use. This value is case-insensitive, for example 
        `"albers"` and `"Albers"` indicate the same projection type. You can find all valid 
        projection types [in the 
        documentation](https://vega.github.io/vega-lite/docs/projection.html#projection-types).
          __Default value:__ `mercator`
    """
    _schema = {'$ref': '#/definitions/ProjectionConfig'}
    _rootschema = Root._schema

    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined,
                 coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined,
                 parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined,
                 rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined, **kwds):
        super(ProjectionConfig, self).__init__(center=center, clipAngle=clipAngle,
                                               clipExtent=clipExtent, coefficient=coefficient,
                                               distance=distance, fraction=fraction, lobes=lobes,
                                               parallel=parallel, precision=precision, radius=radius,
                                               ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt,
                                               type=type, **kwds)


class ProjectionType(VegaLiteSchema):
    """ProjectionType schema wrapper
    
    enum('albers', 'albersUsa', 'azimuthalEqualArea', 'azimuthalEquidistant', 'conicConformal', 
    'conicEqualArea', 'conicEquidistant', 'equirectangular', 'gnomonic', 'mercator', 
    'orthographic', 'stereographic', 'transverseMercator')
    """
    _schema = {'$ref': '#/definitions/ProjectionType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ProjectionType, self).__init__(*args)


class RangeConfig(VegaLiteSchema):
    """RangeConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    category : anyOf(List(string), VgScheme)
        Default range for _nominal_ (categorical) fields.
    diverging : anyOf(List(string), VgScheme)
        Default range for diverging _quantitative_ fields.
    heatmap : anyOf(List(string), VgScheme)
        Default range for _quantitative_ heatmaps.
    ordinal : anyOf(List(string), VgScheme)
        Default range for _ordinal_ fields.
    ramp : anyOf(List(string), VgScheme)
        Default range for _quantitative_ and _temporal_ fields.
    symbol : List(string)
        Default range palette for the `shape` channel.
    """
    _schema = {'$ref': '#/definitions/RangeConfig'}
    _rootschema = Root._schema

    def __init__(self, category=Undefined, diverging=Undefined, heatmap=Undefined, ordinal=Undefined,
                 ramp=Undefined, symbol=Undefined, **kwds):
        super(RangeConfig, self).__init__(category=category, diverging=diverging, heatmap=heatmap,
                                          ordinal=ordinal, ramp=ramp, symbol=symbol, **kwds)


class RangeConfigValue(VegaLiteSchema):
    """RangeConfigValue schema wrapper
    
    anyOf(List(anyOf(float, string)), VgScheme, Mapping(required=[step]))
    """
    _schema = {'$ref': '#/definitions/RangeConfigValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(RangeConfigValue, self).__init__(*args, **kwds)


class Repeat(VegaLiteSchema):
    """Repeat schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    column : List(string)
        Horizontal repeated views.
    row : List(string)
        Vertical repeated views.
    """
    _schema = {'$ref': '#/definitions/Repeat'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(Repeat, self).__init__(column=column, row=row, **kwds)


class RepeatRef(VegaLiteSchema):
    """RepeatRef schema wrapper
    
    Mapping(required=[repeat])
    Reference to a repeated value.
    
    Attributes
    ----------
    repeat : enum('row', 'column')
    
    """
    _schema = {'$ref': '#/definitions/RepeatRef'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, **kwds):
        super(RepeatRef, self).__init__(repeat=repeat, **kwds)


class Resolve(VegaLiteSchema):
    """Resolve schema wrapper
    
    Mapping(required=[])
    Defines how scales, axes, and legends from different specs should be combined. Resolve is a 
    mapping from `scale`, `axis`, and `legend` to a mapping from channels to resolutions.
    
    Attributes
    ----------
    axis : AxisResolveMap
    
    legend : LegendResolveMap
    
    scale : ScaleResolveMap
    
    """
    _schema = {'$ref': '#/definitions/Resolve'}
    _rootschema = Root._schema

    def __init__(self, axis=Undefined, legend=Undefined, scale=Undefined, **kwds):
        super(Resolve, self).__init__(axis=axis, legend=legend, scale=scale, **kwds)


class ResolveMode(VegaLiteSchema):
    """ResolveMode schema wrapper
    
    enum('independent', 'shared')
    """
    _schema = {'$ref': '#/definitions/ResolveMode'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ResolveMode, self).__init__(*args)


class Scale(VegaLiteSchema):
    """Scale schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    base : float
        The logarithm base of the `log` scale (default `10`).
    clamp : boolean
        If `true`, values that exceed the data domain are clamped to either the minimum or 
        maximum range value  __Default value:__ derived from the [scale 
        config](config.html#scale-config)'s `clamp` (`true` by default).
    domain : anyOf(List(float), List(string), List(boolean), List(DateTime), 
    enum('unaggregated'), SelectionDomain)
        Customized domain values.  For _quantitative_ fields, `domain` can take the form of 
        a two-element array with minimum and maximum values.  [Piecewise 
        scales](scale.html#piecewise) can be created by providing a `domain` with more than 
        two entries. If the input field is aggregated, `domain` can also be a string value 
        `"unaggregated"`, indicating that the domain should include the raw data values 
        prior to the aggregation.  For _temporal_ fields, `domain` can be a two-element 
        array minimum and maximum values, in the form of either timestamps or the [DateTime 
        definition objects](types.html#datetime).  For _ordinal_ and _nominal_ fields, 
        `domain` can be an array that lists valid input values.  The `selection` property 
        can be used to [interactively determine](selection.html#scale-domains) the scale 
        domain.
    exponent : float
        The exponent of the `pow` scale.
    interpolate : anyOf(ScaleInterpolate, ScaleInterpolateParams)
        The interpolation method for range values. By default, a general interpolator for 
        numbers, dates, strings and colors (in RGB space) is used. For color ranges, this 
        property allows interpolation in alternative color spaces. Legal values include 
        `rgb`, `hsl`, `hsl-long`, `lab`, `hcl`, `hcl-long`, `cubehelix` and `cubehelix-long`
         ('-long' variants use longer paths in polar coordinate spaces). If object-valued, 
        this property accepts an object with a string-valued _type_ property and an optional
         numeric _gamma_ property applicable to rgb and cubehelix interpolators. For more, 
        see the [d3-interpolate documentation](https://github.com/d3/d3-interpolate).  
        __Note:__ Sequential scales do not support `interpolate` as they have a fixed 
        interpolator.  Since Vega-Lite uses sequential scales for quantitative fields by 
        default, you have to set the scale `type` to other quantitative scale type such as 
        `"linear"` to customize `interpolate`.
    nice : anyOf(boolean, float, NiceTime, Mapping(required=[interval, step]))
        Extending the domain so that it starts and ends on nice round values. This method 
        typically modifies the scale’s domain, and may only extend the bounds to the nearest
         round value. Nicing is useful if the domain is computed from data and may be 
        irregular. For example, for a domain of _[0.201479…, 0.996679…]_, a nice domain 
        might be _[0.2, 1.0]_.  For quantitative scales such as linear, `nice` can be either
         a boolean flag or a number. If `nice` is a number, it will represent a desired tick
         count. This allows greater control over the step size used to extend the bounds, 
        guaranteeing that the returned ticks will exactly cover the domain.  For temporal 
        fields with time and utc scales, the `nice` value can be a string indicating the 
        desired time interval. Legal values are `"millisecond"`, `"second"`, `"minute"`, 
        `"hour"`, `"day"`, `"week"`, `"month"`, and `"year"`. Alternatively, `time` and 
        `utc` scales can accept an object-valued interval specifier of the form 
        `{"interval": "month", "step": 3}`, which includes a desired number of interval 
        steps. Here, the domain would snap to quarter (Jan, Apr, Jul, Oct) boundaries.  
        __Default value:__ `true` for unbinned _quantitative_ fields; `false` otherwise.
    padding : float
        For _[continuous](scale.html#continuous)_ scales, expands the scale domain to 
        accommodate the specified number of pixels on each of the scale range. The scale 
        range must represent pixels for this parameter to function as intended. Padding 
        adjustment is performed prior to all other adjustments, including the effects of 
        the zero, nice, domainMin, and domainMax properties.  For _[band](scale.html#band)_ 
        scales, shortcut for setting `paddingInner` and `paddingOuter` to the same value.  
        For _[point](scale.html#point)_ scales, alias for `paddingOuter`.  __Default 
        value:__ For _continuous_ scales, derived from the [scale 
        config](scale.html#config)'s `continuousPadding`. For _band and point_ scales, see 
        `paddingInner` and `paddingOuter`.
    paddingInner : float
        The inner padding (spacing) within each band step of band scales, as a fraction of 
        the step size. This value must lie in the range [0,1].  For point scale, this 
        property is invalid as point scales do not have internal band widths (only step 
        sizes between bands).  __Default value:__ derived from the [scale 
        config](scale.html#config)'s `bandPaddingInner`.
    paddingOuter : float
        The outer padding (spacing) at the ends of the range of band and point scales, as a 
        fraction of the step size. This value must lie in the range [0,1].  __Default 
        value:__ derived from the [scale config](scale.html#config)'s `bandPaddingOuter` for
         band scales and `pointPadding` for point scales.
    range : anyOf(List(float), List(string), string)
        The range of the scale. One of:  - A string indicating a [pre-defined named scale 
        range](scale.html#range-config) (e.g., example, `"symbol"`, or `"diverging"`).  - 
        For [continuous scales](scale.html#continuous), two-element array indicating  
        minimum and maximum values, or an array with more than two entries for specifying a 
        [piecewise scale](scale.html#piecewise).  - For [discrete](scale.html#discrete) and 
        [discretizing](scale.html#discretizing) scales, an array of desired output values.  
        __Notes:__  1) For [sequential](scale.html#sequential), 
        [ordinal](scale.html#ordinal), and discretizing color scales, you can also specify a
         color [`scheme`](scale.html#scheme) instead of `range`.  2) Any directly specified 
        `range` for `x` and `y` channels will be ignored. Range can be customized via the 
        view's corresponding [size](size.html) (`width` and `height`) or via [range steps 
        and paddings properties](#range-step) for [band](#band) and [point](#point) scales.
    rangeStep : anyOf(float, None)
        The distance between the starts of adjacent bands or points in 
        [band](scale.html#band) and [point](scale.html#point) scales.  If `rangeStep` is 
        `null` or if the view contains the scale's corresponding [size](size.html) (`width` 
        for `x` scales and `height` for `y` scales), `rangeStep` will be automatically 
        determined to fit the size of the view.  __Default value:__  derived the [scale 
        config](config.html#scale-config)'s `textXRangeStep` (`90` by default) for x-scales 
        of `text` marks and `rangeStep` (`21` by default) for x-scales of other marks and 
        y-scales.  __Warning__: If `rangeStep` is `null` and the cardinality of the scale's 
        domain is higher than `width` or `height`, the rangeStep might become less than one 
        pixel and the mark might not appear correctly.
    round : boolean
        If `true`, rounds numeric output values to integers. This can be helpful for 
        snapping to the pixel grid.  __Default value:__ `false`.
    scheme : anyOf(string, SchemeParams)
        A string indicating a color [scheme](scale.html#scheme) name (e.g., `"category10"` 
        or `"viridis"`) or a [scheme parameter object](scale.html#scheme-params).  Discrete 
        color schemes may be used with [discrete](scale.html#discrete) or 
        [discretizing](scale.html#discretizing) scales. Continuous color schemes are 
        intended for use with [sequential](scales.html#sequential) scales.  For the full 
        list of supported scheme, please refer to the [Vega 
        Scheme](https://vega.github.io/vega/docs/schemes/#reference) reference.
    type : ScaleType
        The type of scale.  Vega-Lite supports the following categories of scale types:  1) 
        [**Continuous Scales**](scale.html#continuous) -- mapping continuous domains to 
        continuous output ranges ([`"linear"`](scale.html#linear), 
        [`"pow"`](scale.html#pow), [`"sqrt"`](scale.html#sqrt), [`"log"`](scale.html#log), 
        [`"time"`](scale.html#time), [`"utc"`](scale.html#utc), 
        [`"sequential"`](scale.html#sequential)).  2) [**Discrete 
        Scales**](scale.html#discrete) -- mapping discrete domains to discrete 
        ([`"ordinal"`](scale.html#ordinal)) or continuous ([`"band"`](scale.html#band) and 
        [`"point"`](scale.html#point)) output ranges.  3) [**Discretizing 
        Scales**](scale.html#discretizing) -- mapping continuous domains to discrete output 
        ranges ([`"bin-linear"`](scale.html#bin-linear) and 
        [`"bin-ordinal"`](scale.html#bin-ordinal)).  __Default value:__ please see the 
        [scale type table](scale.html#type).
    zero : boolean
        If `true`, ensures that a zero baseline value is included in the scale domain.  
        __Default value:__ `true` for x and y channels if the quantitative field is not 
        binned and no custom `domain` is provided; `false` otherwise.  __Note:__ Log, time, 
        and utc scales do not support `zero`.
    """
    _schema = {'$ref': '#/definitions/Scale'}
    _rootschema = Root._schema

    def __init__(self, base=Undefined, clamp=Undefined, domain=Undefined, exponent=Undefined,
                 interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined,
                 paddingOuter=Undefined, range=Undefined, rangeStep=Undefined, round=Undefined,
                 scheme=Undefined, type=Undefined, zero=Undefined, **kwds):
        super(Scale, self).__init__(base=base, clamp=clamp, domain=domain, exponent=exponent,
                                    interpolate=interpolate, nice=nice, padding=padding,
                                    paddingInner=paddingInner, paddingOuter=paddingOuter, range=range,
                                    rangeStep=rangeStep, round=round, scheme=scheme, type=type,
                                    zero=zero, **kwds)


class ScaleConfig(VegaLiteSchema):
    """ScaleConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    bandPaddingInner : float
        Default inner padding for `x` and `y` band-ordinal scales.  __Default value:__ `0.1`
    bandPaddingOuter : float
        Default outer padding for `x` and `y` band-ordinal scales. If not specified, by 
        default, band scale's paddingOuter is paddingInner/2.
    clamp : boolean
        If true, values that exceed the data domain are clamped to either the minimum or 
        maximum range value
    continuousPadding : float
        Default padding for continuous scales.  __Default:__ `5` for continuous x-scale of a
         vertical bar and continuous y-scale of a horizontal bar.; `0` otherwise.
    maxBandSize : float
        The default max value for mapping quantitative fields to bar's size/bandSize.  If 
        undefined (default), we will use the scale's `rangeStep` - 1.
    maxFontSize : float
        The default max value for mapping quantitative fields to text's size/fontSize.  
        __Default value:__ `40`
    maxOpacity : float
        Default max opacity for mapping a field to opacity.  __Default value:__ `0.8`
    maxSize : float
        Default max value for point size scale.
    maxStrokeWidth : float
        Default max strokeWidth for strokeWidth  (or rule/line's size) scale.  __Default 
        value:__ `4`
    minBandSize : float
        The default min value for mapping quantitative fields to bar and tick's 
        size/bandSize scale with zero=false.  __Default value:__ `2`
    minFontSize : float
        The default min value for mapping quantitative fields to tick's size/fontSize scale 
        with zero=false  __Default value:__ `8`
    minOpacity : float
        Default minimum opacity for mapping a field to opacity.  __Default value:__ `0.3`
    minSize : float
        Default minimum value for point size scale with zero=false.  __Default value:__ `9`
    minStrokeWidth : float
        Default minimum strokeWidth for strokeWidth (or rule/line's size) scale with 
        zero=false.  __Default value:__ `1`
    pointPadding : float
        Default outer padding for `x` and `y` point-ordinal scales.  __Default value:__ 
        `0.5`
    rangeStep : anyOf(float, None)
        Default range step for band and point scales of (1) the `y` channel and (2) the `x` 
        channel when the mark is not `text`.  __Default value:__ `21`
    round : boolean
        If true, rounds numeric output values to integers. This can be helpful for snapping 
        to the pixel grid. (Only available for `x`, `y`, and `size` scales.)
    textXRangeStep : float
        Default range step for `x` band and point scales of text marks.  __Default value:__ 
        `90`
    useUnaggregatedDomain : boolean
        Use the source data range before aggregation as scale domain instead of aggregated 
        data for aggregate axis.  This is equivalent to setting `domain` to `"unaggregate"` 
        for aggregated _quantitative_ fields by default.  This property only works with 
        aggregate functions that produce values within the raw data domain (`"mean"`, 
        `"average"`, `"median"`, `"q1"`, `"q3"`, `"min"`, `"max"`). For other aggregations 
        that produce values outside of the raw data domain (e.g. `"count"`, `"sum"`), this 
        property is ignored.  __Default value:__ `false`
    """
    _schema = {'$ref': '#/definitions/ScaleConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPaddingInner=Undefined, bandPaddingOuter=Undefined, clamp=Undefined,
                 continuousPadding=Undefined, maxBandSize=Undefined, maxFontSize=Undefined,
                 maxOpacity=Undefined, maxSize=Undefined, maxStrokeWidth=Undefined,
                 minBandSize=Undefined, minFontSize=Undefined, minOpacity=Undefined, minSize=Undefined,
                 minStrokeWidth=Undefined, pointPadding=Undefined, rangeStep=Undefined, round=Undefined,
                 textXRangeStep=Undefined, useUnaggregatedDomain=Undefined, **kwds):
        super(ScaleConfig, self).__init__(bandPaddingInner=bandPaddingInner,
                                          bandPaddingOuter=bandPaddingOuter, clamp=clamp,
                                          continuousPadding=continuousPadding, maxBandSize=maxBandSize,
                                          maxFontSize=maxFontSize, maxOpacity=maxOpacity,
                                          maxSize=maxSize, maxStrokeWidth=maxStrokeWidth,
                                          minBandSize=minBandSize, minFontSize=minFontSize,
                                          minOpacity=minOpacity, minSize=minSize,
                                          minStrokeWidth=minStrokeWidth, pointPadding=pointPadding,
                                          rangeStep=rangeStep, round=round,
                                          textXRangeStep=textXRangeStep,
                                          useUnaggregatedDomain=useUnaggregatedDomain, **kwds)


class ScaleInterpolate(VegaLiteSchema):
    """ScaleInterpolate schema wrapper
    
    enum('rgb', 'lab', 'hcl', 'hsl', 'hsl-long', 'hcl-long', 'cubehelix', 'cubehelix-long')
    """
    _schema = {'$ref': '#/definitions/ScaleInterpolate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ScaleInterpolate, self).__init__(*args)


class ScaleInterpolateParams(VegaLiteSchema):
    """ScaleInterpolateParams schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : enum('rgb', 'cubehelix', 'cubehelix-long')
    
    gamma : float
    
    """
    _schema = {'$ref': '#/definitions/ScaleInterpolateParams'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, gamma=Undefined, **kwds):
        super(ScaleInterpolateParams, self).__init__(type=type, gamma=gamma, **kwds)


class ScaleResolveMap(VegaLiteSchema):
    """ScaleResolveMap schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    color : ResolveMode
    
    fill : ResolveMode
    
    opacity : ResolveMode
    
    shape : ResolveMode
    
    size : ResolveMode
    
    stroke : ResolveMode
    
    x : ResolveMode
    
    y : ResolveMode
    
    """
    _schema = {'$ref': '#/definitions/ScaleResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, fill=Undefined, opacity=Undefined, shape=Undefined,
                 size=Undefined, stroke=Undefined, x=Undefined, y=Undefined, **kwds):
        super(ScaleResolveMap, self).__init__(color=color, fill=fill, opacity=opacity, shape=shape,
                                              size=size, stroke=stroke, x=x, y=y, **kwds)


class ScaleType(VegaLiteSchema):
    """ScaleType schema wrapper
    
    enum('linear', 'bin-linear', 'log', 'pow', 'sqrt', 'time', 'utc', 'sequential', 'ordinal', 
    'bin-ordinal', 'point', 'band')
    """
    _schema = {'$ref': '#/definitions/ScaleType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ScaleType, self).__init__(*args)


class SchemeParams(VegaLiteSchema):
    """SchemeParams schema wrapper
    
    Mapping(required=[name])
    
    Attributes
    ----------
    name : string
        A color scheme name for sequential/ordinal scales (e.g., `"category10"` or 
        `"viridis"`).  For the full list of supported scheme, please refer to the [Vega 
        Scheme](https://vega.github.io/vega/docs/schemes/#reference) reference.
    extent : List(float)
        For sequential and diverging schemes only, determines the extent of the color range 
        to use. For example `[0.2, 1]` will rescale the color scheme such that color values 
        in the range _[0, 0.2)_ are excluded from the scheme.
    """
    _schema = {'$ref': '#/definitions/SchemeParams'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, extent=Undefined, **kwds):
        super(SchemeParams, self).__init__(name=name, extent=extent, **kwds)


class SelectionConfig(VegaLiteSchema):
    """SelectionConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    interval : IntervalSelectionConfig
        The default definition for an [`interval`](selection.html#type) selection. All 
        properties and transformations for an interval selection definition (except `type`) 
        may be specified here.  For instance, setting `interval` to `{"translate": false}` 
        disables the ability to move interval selections by default.
    multi : MultiSelectionConfig
        The default definition for a [`multi`](selection.html#type) selection. All 
        properties and transformations for a multi selection definition (except `type`) may 
        be specified here.  For instance, setting `multi` to `{"toggle": "event.altKey"}` 
        adds additional values to multi selections when clicking with the alt-key pressed by
         default.
    single : SingleSelectionConfig
        The default definition for a [`single`](selection.html#type) selection. All 
        properties and transformations   for a single selection definition (except `type`) 
        may be specified here.  For instance, setting `single` to `{"on": "dblclick"}` 
        populates single selections on double-click by default.
    """
    _schema = {'$ref': '#/definitions/SelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, interval=Undefined, multi=Undefined, single=Undefined, **kwds):
        super(SelectionConfig, self).__init__(interval=interval, multi=multi, single=single, **kwds)


class SelectionDef(VegaLiteSchema):
    """SelectionDef schema wrapper
    
    anyOf(SingleSelection, MultiSelection, IntervalSelection)
    """
    _schema = {'$ref': '#/definitions/SelectionDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionDef, self).__init__(*args, **kwds)


class SelectionDomain(VegaLiteSchema):
    """SelectionDomain schema wrapper
    
    anyOf(Mapping(required=[selection]), Mapping(required=[selection]))
    """
    _schema = {'$ref': '#/definitions/SelectionDomain'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionDomain, self).__init__(*args, **kwds)


class SelectionPredicate(VegaLiteSchema):
    """SelectionPredicate schema wrapper
    
    Mapping(required=[selection])
    
    Attributes
    ----------
    selection : SelectionOperand
        Filter using a selection name.
    """
    _schema = {'$ref': '#/definitions/SelectionPredicate'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, **kwds):
        super(SelectionPredicate, self).__init__(selection=selection, **kwds)


class SelectionResolution(VegaLiteSchema):
    """SelectionResolution schema wrapper
    
    enum('global', 'union', 'intersect')
    """
    _schema = {'$ref': '#/definitions/SelectionResolution'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SelectionResolution, self).__init__(*args)


class SingleDefChannel(VegaLiteSchema):
    """SingleDefChannel schema wrapper
    
    enum('x', 'y', 'x2', 'y2', 'longitude', 'latitude', 'longitude2', 'latitude2', 'row', 
    'column', 'color', 'fill', 'stroke', 'size', 'shape', 'opacity', 'text', 'tooltip', 'href', 
    'key')
    """
    _schema = {'$ref': '#/definitions/SingleDefChannel'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SingleDefChannel, self).__init__(*args)


class SingleSelection(VegaLiteSchema):
    """SingleSelection schema wrapper
    
    Mapping(required=[type])
    
    Attributes
    ----------
    type : enum('single')
    
    bind : anyOf(VgBinding, Mapping(required=[]))
        Establish a two-way binding between a single selection and input elements (also 
        known as dynamic query widgets). A binding takes the form of Vega's [input element 
        binding definition](https://vega.github.io/vega/docs/signals/#bind) or can be a 
        mapping between projected field/encodings and binding definitions.  See the [bind 
        transform](bind.html) documentation for more information.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection. When 
        set to `none`, empty selections contain no data values.
    encodings : List(SingleDefChannel)
        An array of encoding channels. The corresponding data field values must match for a 
        data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to fall within the 
        selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete 
        selection. The data value _nearest_ the mouse cursor is added to the selection.  See
         the [nearest transform](nearest.html) documentation for more information.
    on : VgEventStream
        A [Vega event stream](https://vega.github.io/vega/docs/event-streams/) (object or 
        selector) that triggers the selection. For interval selections, the event stream 
        must specify a [start and 
        end](https://vega.github.io/vega/docs/event-streams/#between-filters).
    resolve : SelectionResolution
        With layered and multi-view displays, a strategy that determines how selections' 
        data queries are resolved when applied in a filter transform, conditional encoding 
        rule, or scale domain.
    """
    _schema = {'$ref': '#/definitions/SingleSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, empty=Undefined, encodings=Undefined,
                 fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, **kwds):
        super(SingleSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings,
                                              fields=fields, nearest=nearest, on=on, resolve=resolve,
                                              **kwds)


class SingleSelectionConfig(VegaLiteSchema):
    """SingleSelectionConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    bind : anyOf(VgBinding, Mapping(required=[]))
        Establish a two-way binding between a single selection and input elements (also 
        known as dynamic query widgets). A binding takes the form of Vega's [input element 
        binding definition](https://vega.github.io/vega/docs/signals/#bind) or can be a 
        mapping between projected field/encodings and binding definitions.  See the [bind 
        transform](bind.html) documentation for more information.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection. When 
        set to `none`, empty selections contain no data values.
    encodings : List(SingleDefChannel)
        An array of encoding channels. The corresponding data field values must match for a 
        data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to fall within the 
        selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete 
        selection. The data value _nearest_ the mouse cursor is added to the selection.  See
         the [nearest transform](nearest.html) documentation for more information.
    on : VgEventStream
        A [Vega event stream](https://vega.github.io/vega/docs/event-streams/) (object or 
        selector) that triggers the selection. For interval selections, the event stream 
        must specify a [start and 
        end](https://vega.github.io/vega/docs/event-streams/#between-filters).
    resolve : SelectionResolution
        With layered and multi-view displays, a strategy that determines how selections' 
        data queries are resolved when applied in a filter transform, conditional encoding 
        rule, or scale domain.
    """
    _schema = {'$ref': '#/definitions/SingleSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined,
                 nearest=Undefined, on=Undefined, resolve=Undefined, **kwds):
        super(SingleSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings,
                                                    fields=fields, nearest=nearest, on=on,
                                                    resolve=resolve, **kwds)


class SingleTimeUnit(VegaLiteSchema):
    """SingleTimeUnit schema wrapper
    
    anyOf(LocalSingleTimeUnit, UtcSingleTimeUnit)
    """
    _schema = {'$ref': '#/definitions/SingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SingleTimeUnit, self).__init__(*args, **kwds)


class SortField(VegaLiteSchema):
    """SortField schema wrapper
    
    Mapping(required=[op])
    
    Attributes
    ----------
    op : AggregateOp
        An [aggregate operation](aggregate.html#ops) to perform on the field prior to 
        sorting (e.g., `"count"`, `"mean"` and `"median"`). This property is required in 
        cases where the sort field and the data reference field do not match. The input data
         objects will be aggregated, grouped by the encoded data field.  For a full list of 
        operations, please see the documentation for [aggregate](aggregate.html#ops).
    field : anyOf(string, RepeatRef)
        The data [field](field.html) to sort by.  __Default value:__ If unspecified, 
        defaults to the field specified in the outer data reference.
    order : SortOrder
        The sort order. One of `"ascending"` (default) or `"descending"`.
    """
    _schema = {'$ref': '#/definitions/SortField'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, order=Undefined, **kwds):
        super(SortField, self).__init__(op=op, field=field, order=order, **kwds)


class SortOrder(VegaLiteSchema):
    """SortOrder schema wrapper
    
    enum('ascending', 'descending', None)
    """
    _schema = {'$ref': '#/definitions/SortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SortOrder, self).__init__(*args)


class StackOffset(VegaLiteSchema):
    """StackOffset schema wrapper
    
    enum('zero', 'center', 'normalize')
    """
    _schema = {'$ref': '#/definitions/StackOffset'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)


class StyleConfigIndex(VegaLiteSchema):
    """StyleConfigIndex schema wrapper
    
    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/StyleConfigIndex'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(StyleConfigIndex, self).__init__(**kwds)


class TextConfig(VegaLiteSchema):
    """TextConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    align : HorizontalAlign
        The horizontal alignment of the text. One of `"left"`, `"right"`, `"center"`.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : VerticalAlign
        The vertical alignment of the text. One of `"top"`, `"middle"`, `"bottom"`.  
        __Default value:__ `"middle"`
    color : string
        Default color.  Note that `fill` and `stroke` have higher precedence than `color` 
        and will override `color`.  __Default value:__ <span style="color: 
        #4682b4;">&#9632;</span> `"#4682b4"`  __Note:__ This property cannot be used in a 
        [style config](mark.html#style-config).
    cursor : enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 
    'wait', 'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop', 
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize', 
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize', 
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
        The mouse cursor used over the mark. Any valid [CSS cursor 
        type](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values) can be used.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ `1`
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.  
        __Default value:__ `true` for all marks except `point` and `false` for `point`.  
        __Applicable for:__ `bar`, `point`, `circle`, `square`, and `area` marks.  __Note:__
         This property cannot be used in a [style config](mark.html#style-config).
    font : string
        The typeface to set the text in (e.g., `"Helvetica Neue"`).
    fontSize : float
        The font size, in pixels.
    fontStyle : FontStyle
        The font style (e.g., `"italic"`).
    fontWeight : FontWeight
        The font weight. This can be either a string (e.g `"bold"`, `"normal"`) or a number 
        (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = `700`).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : Interpolate
        The line interpolation method to use for line and area marks. One of the following: 
        - `"linear"`: piecewise linear segments, as in a polyline. - `"linear-closed"`: 
        close the linear segments to form a polygon. - `"step"`: alternate between 
        horizontal and vertical segments, as in a step function. - `"step-before"`: 
        alternate between vertical and horizontal segments, as in a step function. - 
        `"step-after"`: alternate between horizontal and vertical segments, as in a step 
        function. - `"basis"`: a B-spline, with control point duplication on the ends. - 
        `"basis-open"`: an open B-spline; may not intersect the start or end. - 
        `"basis-closed"`: a closed B-spline, as in a loop. - `"cardinal"`: a Cardinal 
        spline, with control point duplication on the ends. - `"cardinal-open"`: an open 
        Cardinal spline; may not intersect the start or end, but will intersect other 
        control points. - `"cardinal-closed"`: a closed Cardinal spline, as in a loop. - 
        `"bundle"`: equivalent to basis, except the tension parameter is used to straighten 
        the spline. - `"monotone"`: cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels (default 0, indicating no limit). The 
        text value will be automatically truncated if the rendered size exceeds the limit.
    opacity : float
        The overall opacity (value between [0,1]).  __Default value:__ `0.7` for 
        non-aggregate plots with `point`, `tick`, `circle`, or `square` marks or layered 
        `bar` charts and `1` otherwise.
    orient : Orient
        The orientation of a non-stacked bar, tick, area, and line charts. The value is 
        either horizontal (default) or vertical. - For bar, rule and tick, this determines 
        whether the size of the bar and tick should be applied to x or y dimension. - For 
        area, this property determines the orient property of the Vega output. - For line, 
        this property determines the sort order of the points in the line if 
        `config.sortLineBy` is not specified. For stacked charts, this is always determined 
        by the orientation of the stack; therefore explicitly specified value will be 
        ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin 
        determined by the `x` and `y` properties.
    shape : string
        The default symbol shape to use. One of: `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or a custom SVG path.
          __Default value:__ `"circle"`
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.
    size : float
        The pixel area each the point/circle/square. For example: in the case of circles, 
        the radius is determined in part by the square root of the size value.  __Default 
        value:__ `30`
    stroke : string
        Default Stroke Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ `1`
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area 
        marks).
    text : string
        Placeholder text if the `text` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by 
        the `x` and `y` properties. Values for `theta` follow the same convention of `arc` 
        mark `startAngle` and `endAngle` properties: angles are measured in radians, with 
        `0` indicating "north".
    """
    _schema = {'$ref': '#/definitions/TextConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined,
                 opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined,
                 shortTimeLabels=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined,
                 tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(TextConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color,
                                         cursor=cursor, dx=dx, dy=dy, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         href=href, interpolate=interpolate, limit=limit,
                                         opacity=opacity, orient=orient, radius=radius, shape=shape,
                                         shortTimeLabels=shortTimeLabels, size=size, stroke=stroke,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta, **kwds)


class TickConfig(VegaLiteSchema):
    """TickConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    align : HorizontalAlign
        The horizontal alignment of the text. One of `"left"`, `"right"`, `"center"`.
    angle : float
        The rotation angle of the text, in degrees.
    bandSize : float
        The width of the ticks.  __Default value:__  2/3 of rangeStep.
    baseline : VerticalAlign
        The vertical alignment of the text. One of `"top"`, `"middle"`, `"bottom"`.  
        __Default value:__ `"middle"`
    color : string
        Default color.  Note that `fill` and `stroke` have higher precedence than `color` 
        and will override `color`.  __Default value:__ <span style="color: 
        #4682b4;">&#9632;</span> `"#4682b4"`  __Note:__ This property cannot be used in a 
        [style config](mark.html#style-config).
    cursor : enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 
    'wait', 'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop', 
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize', 
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize', 
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
        The mouse cursor used over the mark. Any valid [CSS cursor 
        type](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values) can be used.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ `1`
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.  
        __Default value:__ `true` for all marks except `point` and `false` for `point`.  
        __Applicable for:__ `bar`, `point`, `circle`, `square`, and `area` marks.  __Note:__
         This property cannot be used in a [style config](mark.html#style-config).
    font : string
        The typeface to set the text in (e.g., `"Helvetica Neue"`).
    fontSize : float
        The font size, in pixels.
    fontStyle : FontStyle
        The font style (e.g., `"italic"`).
    fontWeight : FontWeight
        The font weight. This can be either a string (e.g `"bold"`, `"normal"`) or a number 
        (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = `700`).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : Interpolate
        The line interpolation method to use for line and area marks. One of the following: 
        - `"linear"`: piecewise linear segments, as in a polyline. - `"linear-closed"`: 
        close the linear segments to form a polygon. - `"step"`: alternate between 
        horizontal and vertical segments, as in a step function. - `"step-before"`: 
        alternate between vertical and horizontal segments, as in a step function. - 
        `"step-after"`: alternate between horizontal and vertical segments, as in a step 
        function. - `"basis"`: a B-spline, with control point duplication on the ends. - 
        `"basis-open"`: an open B-spline; may not intersect the start or end. - 
        `"basis-closed"`: a closed B-spline, as in a loop. - `"cardinal"`: a Cardinal 
        spline, with control point duplication on the ends. - `"cardinal-open"`: an open 
        Cardinal spline; may not intersect the start or end, but will intersect other 
        control points. - `"cardinal-closed"`: a closed Cardinal spline, as in a loop. - 
        `"bundle"`: equivalent to basis, except the tension parameter is used to straighten 
        the spline. - `"monotone"`: cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels (default 0, indicating no limit). The 
        text value will be automatically truncated if the rendered size exceeds the limit.
    opacity : float
        The overall opacity (value between [0,1]).  __Default value:__ `0.7` for 
        non-aggregate plots with `point`, `tick`, `circle`, or `square` marks or layered 
        `bar` charts and `1` otherwise.
    orient : Orient
        The orientation of a non-stacked bar, tick, area, and line charts. The value is 
        either horizontal (default) or vertical. - For bar, rule and tick, this determines 
        whether the size of the bar and tick should be applied to x or y dimension. - For 
        area, this property determines the orient property of the Vega output. - For line, 
        this property determines the sort order of the points in the line if 
        `config.sortLineBy` is not specified. For stacked charts, this is always determined 
        by the orientation of the stack; therefore explicitly specified value will be 
        ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin 
        determined by the `x` and `y` properties.
    shape : string
        The default symbol shape to use. One of: `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or a custom SVG path.
          __Default value:__ `"circle"`
    size : float
        The pixel area each the point/circle/square. For example: in the case of circles, 
        the radius is determined in part by the square root of the size value.  __Default 
        value:__ `30`
    stroke : string
        Default Stroke Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ `1`
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area 
        marks).
    text : string
        Placeholder text if the `text` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by 
        the `x` and `y` properties. Values for `theta` follow the same convention of `arc` 
        mark `startAngle` and `endAngle` properties: angles are measured in radians, with 
        `0` indicating "north".
    thickness : float
        Thickness of the tick mark.  __Default value:__  `1`
    """
    _schema = {'$ref': '#/definitions/TickConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, bandSize=Undefined, baseline=Undefined,
                 color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined,
                 fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                 limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined,
                 tension=Undefined, text=Undefined, theta=Undefined, thickness=Undefined, **kwds):
        super(TickConfig, self).__init__(align=align, angle=angle, bandSize=bandSize, baseline=baseline,
                                         color=color, cursor=cursor, dx=dx, dy=dy, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         href=href, interpolate=interpolate, limit=limit,
                                         opacity=opacity, orient=orient, radius=radius, shape=shape,
                                         size=size, stroke=stroke, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, thickness=thickness, **kwds)


class TimeUnit(VegaLiteSchema):
    """TimeUnit schema wrapper
    
    anyOf(SingleTimeUnit, MultiTimeUnit)
    """
    _schema = {'$ref': '#/definitions/TimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TimeUnit, self).__init__(*args, **kwds)


class TimeUnitTransform(VegaLiteSchema):
    """TimeUnitTransform schema wrapper
    
    Mapping(required=[timeUnit, field, as])
    
    Attributes
    ----------
    field : string
        The data field to apply time unit.
    timeUnit : TimeUnit
        The timeUnit.
    """
    _schema = {'$ref': '#/definitions/TimeUnitTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, timeUnit=Undefined, **kwds):
        super(TimeUnitTransform, self).__init__(field=field, timeUnit=timeUnit, **kwds)


class TitleOrient(VegaLiteSchema):
    """TitleOrient schema wrapper
    
    enum('top', 'bottom', 'left', 'right')
    """
    _schema = {'$ref': '#/definitions/TitleOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TitleOrient, self).__init__(*args)


class TitleParams(VegaLiteSchema):
    """TitleParams schema wrapper
    
    Mapping(required=[text])
    
    Attributes
    ----------
    text : string
        The title text.
    anchor : Anchor
        The anchor position for placing the title. One of `"start"`, `"middle"`, or `"end"`.
         For example, with an orientation of top these anchor positions map to a left-, 
        center-, or right-aligned title.  __Default value:__ `"middle"` for 
        [single](spec.html) and [layered](layer.html) views. `"start"` for other composite 
        views.  __Note:__ [For now](https://github.com/vega/vega-lite/issues/2875), `anchor`
         is only customizable only for [single](spec.html) and [layered](layer.html) views.
          For other composite views, `anchor` is always `"start"`.
    offset : float
        The orthogonal offset in pixels by which to displace the title from its position 
        along the edge of the chart.
    orient : TitleOrient
        The orientation of the title relative to the chart. One of `"top"` (the default), 
        `"bottom"`, `"left"`, or `"right"`.
    style : anyOf(string, List(string))
        A [mark style property](config.html#style) to apply to the title text mark.  
        __Default value:__ `"group-title"`.
    """
    _schema = {'$ref': '#/definitions/TitleParams'}
    _rootschema = Root._schema

    def __init__(self, text=Undefined, anchor=Undefined, offset=Undefined, orient=Undefined,
                 style=Undefined, **kwds):
        super(TitleParams, self).__init__(text=text, anchor=anchor, offset=offset, orient=orient,
                                          style=style, **kwds)


class TopLevelLayerSpec(VegaLiteSchema):
    """TopLevelLayerSpec schema wrapper
    
    Mapping(required=[layer])
    
    Attributes
    ----------
    layer : List(anyOf(LayerSpec, CompositeUnitSpec))
        Layer or single view specifications to be layered.  __Note__: Specifications inside 
        `layer` cannot use `row` and `column` channels as layering facet specifications is 
        not allowed.
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    config : Config
        Vega-Lite configuration object.  This property can only be defined at the top-level 
        of a specification.
    data : Data
        An object describing the data source
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    description : string
        Description of this mark for commenting purpose.
    encoding : Encoding
        A shared key-value mapping between encoding channels and definition of fields in the
         underlying layers.
    height : float
        The height of a visualization.  __Default value:__ - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its y-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the height will
         be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - 
        For y-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the height is [determined by the range step, paddings, and the
         cardinality of the field mapped to 
        y-channel](https://vega.github.io/vega-lite/docs/scale.html#band). Otherwise, if the
         `rangeStep` is `null`, the height will be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - If
         no field is mapped to `y` channel, the `height` will be the value of `rangeStep`.  
        __Note__: For plots with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the height of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    name : string
        Name of the visualization for later reference.
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    projection : Projection
        An object defining properties of the geographic projection shared by underlying 
        layers.
    resolve : Resolve
        Scale, axis, and legend resolutions for layers.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.  __Default value:__ This will be determined by the 
        following rules:  - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its x-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the width will 
        be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - For
         x-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the width is [determined by the range step, paddings, and the 
        cardinality of the field mapped to 
        x-channel](https://vega.github.io/vega-lite/docs/scale.html#band).   Otherwise, if 
        the `rangeStep` is `null`, the width will be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - If 
        no field is mapped to `x` channel, the `width` will be the value of 
        [`config.scale.textXRangeStep`](https://vega.github.io/vega-lite/docs/size.html#default-width-and-height)
         for `text` mark and the value of `rangeStep` for other marks.  __Note:__ For plots 
        with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the width of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    """
    _schema = {'$ref': '#/definitions/TopLevelLayerSpec'}
    _rootschema = Root._schema

    def __init__(self, layer=Undefined, autosize=Undefined, background=Undefined, config=Undefined,
                 data=Undefined, datasets=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, padding=Undefined, projection=Undefined,
                 resolve=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(TopLevelLayerSpec, self).__init__(layer=layer, autosize=autosize, background=background,
                                                config=config, data=data, datasets=datasets,
                                                description=description, encoding=encoding,
                                                height=height, name=name, padding=padding,
                                                projection=projection, resolve=resolve, title=title,
                                                transform=transform, width=width, **kwds)


class TopLevelHConcatSpec(VegaLiteSchema):
    """TopLevelHConcatSpec schema wrapper
    
    Mapping(required=[hconcat])
    
    Attributes
    ----------
    hconcat : List(Spec)
        A list of views that should be concatenated and put into a row.
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    config : Config
        Vega-Lite configuration object.  This property can only be defined at the top-level 
        of a specification.
    data : Data
        An object describing the data source
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    resolve : Resolve
        Scale, axis, and legend resolutions for horizontally concatenated charts.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/TopLevelHConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, autosize=Undefined, background=Undefined, config=Undefined,
                 data=Undefined, datasets=Undefined, description=Undefined, name=Undefined,
                 padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelHConcatSpec, self).__init__(hconcat=hconcat, autosize=autosize,
                                                  background=background, config=config, data=data,
                                                  datasets=datasets, description=description, name=name,
                                                  padding=padding, resolve=resolve, title=title,
                                                  transform=transform, **kwds)


class TopLevelRepeatSpec(VegaLiteSchema):
    """TopLevelRepeatSpec schema wrapper
    
    Mapping(required=[repeat, spec])
    
    Attributes
    ----------
    repeat : Repeat
        An object that describes what fields should be repeated into views that are laid out
         as a `row` or `column`.
    spec : Spec
    
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    config : Config
        Vega-Lite configuration object.  This property can only be defined at the top-level 
        of a specification.
    data : Data
        An object describing the data source
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    resolve : Resolve
        Scale and legend resolutions for repeated charts.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/TopLevelRepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, autosize=Undefined, background=Undefined,
                 config=Undefined, data=Undefined, datasets=Undefined, description=Undefined,
                 name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(TopLevelRepeatSpec, self).__init__(repeat=repeat, spec=spec, autosize=autosize,
                                                 background=background, config=config, data=data,
                                                 datasets=datasets, description=description, name=name,
                                                 padding=padding, resolve=resolve, title=title,
                                                 transform=transform, **kwds)


class TopLevelVConcatSpec(VegaLiteSchema):
    """TopLevelVConcatSpec schema wrapper
    
    Mapping(required=[vconcat])
    
    Attributes
    ----------
    vconcat : List(Spec)
        A list of views that should be concatenated and put into a column.
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    config : Config
        Vega-Lite configuration object.  This property can only be defined at the top-level 
        of a specification.
    data : Data
        An object describing the data source
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    resolve : Resolve
        Scale, axis, and legend resolutions for vertically concatenated charts.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/TopLevelVConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, autosize=Undefined, background=Undefined, config=Undefined,
                 data=Undefined, datasets=Undefined, description=Undefined, name=Undefined,
                 padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelVConcatSpec, self).__init__(vconcat=vconcat, autosize=autosize,
                                                  background=background, config=config, data=data,
                                                  datasets=datasets, description=description, name=name,
                                                  padding=padding, resolve=resolve, title=title,
                                                  transform=transform, **kwds)


class TopLevelFacetSpec(VegaLiteSchema):
    """TopLevelFacetSpec schema wrapper
    
    Mapping(required=[data, facet, spec])
    
    Attributes
    ----------
    data : Data
        An object describing the data source
    facet : FacetMapping
        An object that describes mappings between `row` and `column` channels and their 
        field definitions.
    spec : anyOf(LayerSpec, CompositeUnitSpec)
        A specification of the view that gets faceted.
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    config : Config
        Vega-Lite configuration object.  This property can only be defined at the top-level 
        of a specification.
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    resolve : Resolve
        Scale, axis, and legend resolutions for facets.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/TopLevelFacetSpec'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, facet=Undefined, spec=Undefined, autosize=Undefined,
                 background=Undefined, config=Undefined, datasets=Undefined, description=Undefined,
                 name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(TopLevelFacetSpec, self).__init__(data=data, facet=facet, spec=spec, autosize=autosize,
                                                background=background, config=config, datasets=datasets,
                                                description=description, name=name, padding=padding,
                                                resolve=resolve, title=title, transform=transform,
                                                **kwds)


class TopLevelFacetedUnitSpec(VegaLiteSchema):
    """TopLevelFacetedUnitSpec schema wrapper
    
    Mapping(required=[data, mark])
    
    Attributes
    ----------
    data : Data
        An object describing the data source
    mark : AnyMark
        A string describing the mark type (one of `"bar"`, `"circle"`, `"square"`, `"tick"`,
         `"line"`, * `"area"`, `"point"`, `"rule"`, `"geoshape"`, and `"text"`) or a [mark 
        definition object](https://vega.github.io/vega-lite/docs/mark.html#mark-def).
    autosize : anyOf(AutosizeType, AutoSizeParams)
        Sets how the visualization size should be determined. If a string, should be one of 
        `"pad"`, `"fit"` or `"none"`. Object values can additionally specify parameters for 
        content sizing and automatic resizing. `"fit"` is only supported for single and 
        layered views that don't use `rangeStep`.  __Default value__: `pad`
    background : string
        CSS color property to use as the background of visualization.  __Default value:__ 
        none (transparent)
    config : Config
        Vega-Lite configuration object.  This property can only be defined at the top-level 
        of a specification.
    datasets : Datasets
        A global data store for named datasets. This is a mapping from names to inline 
        datasets. This can be an array of objects or primitive values or a string. Arrays of
         primitive values are ingested as objects with a `data` property.
    description : string
        Description of this mark for commenting purpose.
    encoding : EncodingWithFacet
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.  __Default value:__ - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its y-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the height will
         be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - 
        For y-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the height is [determined by the range step, paddings, and the
         cardinality of the field mapped to 
        y-channel](https://vega.github.io/vega-lite/docs/scale.html#band). Otherwise, if the
         `rangeStep` is `null`, the height will be the value of 
        [`config.view.height`](https://vega.github.io/vega-lite/docs/spec.html#config). - If
         no field is mapped to `y` channel, the `height` will be the value of `rangeStep`.  
        __Note__: For plots with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the height of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    name : string
        Name of the visualization for later reference.
    padding : Padding
        The default visualization padding, in pixels, from the edge of the visualization 
        canvas to the data rectangle.  If a number, specifies padding for all sides. If an 
        object, the value should have the format `{"left": 5, "top": 5, "right": 5, 
        "bottom": 5}` to specify padding for each side of the visualization.  __Default 
        value__: `5`
    projection : Projection
        An object defining properties of geographic projection.  Works with `"geoshape"` 
        marks and `"point"` or `"line"` marks that have `latitude` and `"longitude"` 
        channels.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, TitleParams)
        Title for the plot.
    transform : List(Transform)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.  __Default value:__ This will be determined by the 
        following rules:  - If a view's 
        [`autosize`](https://vega.github.io/vega-lite/docs/size.html#autosize) type is 
        `"fit"` or its x-channel has a [continuous 
        scale](https://vega.github.io/vega-lite/docs/scale.html#continuous), the width will 
        be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - For
         x-axis with a band or point scale: if 
        [`rangeStep`](https://vega.github.io/vega-lite/docs/scale.html#band) is a numeric 
        value or unspecified, the width is [determined by the range step, paddings, and the 
        cardinality of the field mapped to 
        x-channel](https://vega.github.io/vega-lite/docs/scale.html#band).   Otherwise, if 
        the `rangeStep` is `null`, the width will be the value of 
        [`config.view.width`](https://vega.github.io/vega-lite/docs/spec.html#config). - If 
        no field is mapped to `x` channel, the `width` will be the value of 
        [`config.scale.textXRangeStep`](https://vega.github.io/vega-lite/docs/size.html#default-width-and-height)
         for `text` mark and the value of `rangeStep` for other marks.  __Note:__ For plots 
        with [`row` and `column` 
        channels](https://vega.github.io/vega-lite/docs/encoding.html#facet), this 
        represents the width of a single view.  __See also:__ The documentation for [width 
        and height](https://vega.github.io/vega-lite/docs/size.html) contains more examples.
    """
    _schema = {'$ref': '#/definitions/TopLevelFacetedUnitSpec'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, mark=Undefined, autosize=Undefined, background=Undefined,
                 config=Undefined, datasets=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, padding=Undefined, projection=Undefined,
                 selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(TopLevelFacetedUnitSpec, self).__init__(data=data, mark=mark, autosize=autosize,
                                                      background=background, config=config,
                                                      datasets=datasets, description=description,
                                                      encoding=encoding, height=height, name=name,
                                                      padding=padding, projection=projection,
                                                      selection=selection, title=title,
                                                      transform=transform, width=width, **kwds)


class TopoDataFormat(VegaLiteSchema):
    """TopoDataFormat schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    feature : string
        The name of the TopoJSON object set to convert to a GeoJSON feature collection. For 
        example, in a map of the world, there may be an object set named `"countries"`. 
        Using the feature property, we can extract this set and generate a GeoJSON feature 
        object for each country.
    mesh : string
        The name of the TopoJSON object set to convert to mesh. Similar to the `feature` 
        option, `mesh` extracts a named TopoJSON object set.   Unlike the `feature` option, 
        the corresponding geo data is returned as a single, unified mesh instance, not as 
        individual GeoJSON features. Extracting a mesh is useful for more efficiently 
        drawing borders or other geographic elements that you do not need to associate with 
        specific regions such as individual countries, states or counties.
    parse : anyOf(enum('auto'), Mapping(required=[]))
        If set to auto (the default), perform automatic type inference to determine the 
        desired data types. Alternatively, a parsing directive object can be provided for 
        explicit data types. Each property of the object corresponds to a field name, and 
        the value to the desired data type (one of `"number"`, `"boolean"` or `"date"`). For
         example, `"parse": {"modified_on": "date"}` parses the `modified_on` field in each 
        input record a Date value.  For `"date"`, we parse data based using Javascript's 
        [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse).
         For Specific date formats can be provided (e.g., `{foo: 'date:"%m%d%Y"'}`), using 
        the [d3-time-format syntax](https://github.com/d3/d3-time-format#locale_format). UTC
         date format parsing is supported similarly (e.g., `{foo: 'utc:"%m%d%Y"'}`). See 
        more about [UTC time](timeunit.html#utc)
    type : enum('topojson')
        Type of input data: `"json"`, `"csv"`, `"tsv"`. The default format type is 
        determined by the extension of the file URL. If no extension is detected, `"json"` 
        will be used by default.
    """
    _schema = {'$ref': '#/definitions/TopoDataFormat'}
    _rootschema = Root._schema

    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(TopoDataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, type=type, **kwds)


class Transform(VegaLiteSchema):
    """Transform schema wrapper
    
    anyOf(FilterTransform, CalculateTransform, LookupTransform, BinTransform, TimeUnitTransform,
     AggregateTransform)
    """
    _schema = {'$ref': '#/definitions/Transform'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Transform, self).__init__(*args, **kwds)


class Type(VegaLiteSchema):
    """Type schema wrapper
    
    anyOf(BasicType, GeoType)
    Constants and utilities for data type  
     Data type based on level of measurement 
    """
    _schema = {'$ref': '#/definitions/Type'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Type, self).__init__(*args, **kwds)


class UrlData(VegaLiteSchema):
    """UrlData schema wrapper
    
    Mapping(required=[url])
    
    Attributes
    ----------
    url : string
        An URL from which to load the data set. Use the `format.type` property to ensure the
         loaded data is correctly parsed.
    format : DataFormat
        An object that specifies the format for parsing the data file.
    """
    _schema = {'$ref': '#/definitions/UrlData'}
    _rootschema = Root._schema

    def __init__(self, url=Undefined, format=Undefined, **kwds):
        super(UrlData, self).__init__(url=url, format=format, **kwds)


class UtcMultiTimeUnit(VegaLiteSchema):
    """UtcMultiTimeUnit schema wrapper
    
    enum('utcyearquarter', 'utcyearquartermonth', 'utcyearmonth', 'utcyearmonthdate', 
    'utcyearmonthdatehours', 'utcyearmonthdatehoursminutes', 
    'utcyearmonthdatehoursminutesseconds', 'utcquartermonth', 'utcmonthdate', 'utchoursminutes',
     'utchoursminutesseconds', 'utcminutesseconds', 'utcsecondsmilliseconds')
    """
    _schema = {'$ref': '#/definitions/UtcMultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(UtcMultiTimeUnit, self).__init__(*args)


class UtcSingleTimeUnit(VegaLiteSchema):
    """UtcSingleTimeUnit schema wrapper
    
    enum('utcyear', 'utcquarter', 'utcmonth', 'utcday', 'utcdate', 'utchours', 'utcminutes', 
    'utcseconds', 'utcmilliseconds')
    """
    _schema = {'$ref': '#/definitions/UtcSingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(UtcSingleTimeUnit, self).__init__(*args)


class ValueDef(VegaLiteSchema):
    """ValueDef schema wrapper
    
    Mapping(required=[value])
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values 
        between `0` to `1` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDef'}
    _rootschema = Root._schema

    def __init__(self, value=Undefined, **kwds):
        super(ValueDef, self).__init__(value=value, **kwds)


class ValueDefWithCondition(VegaLiteSchema):
    """ValueDefWithCondition schema wrapper
    
    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(ConditionalFieldDef, ConditionalValueDef, List(ConditionalValueDef))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/ValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class MarkPropValueDefWithCondition(VegaLiteSchema):
    """MarkPropValueDefWithCondition schema wrapper
    
    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(ConditionalMarkPropFieldDef, ConditionalValueDef, 
    List(ConditionalValueDef))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/MarkPropValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(MarkPropValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class TextValueDefWithCondition(VegaLiteSchema):
    """TextValueDefWithCondition schema wrapper
    
    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(ConditionalTextFieldDef, ConditionalValueDef, List(ConditionalValueDef))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/TextValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(TextValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class VerticalAlign(VegaLiteSchema):
    """VerticalAlign schema wrapper
    
    enum('top', 'middle', 'bottom')
    """
    _schema = {'$ref': '#/definitions/VerticalAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VerticalAlign, self).__init__(*args)


class VgAxisConfig(VegaLiteSchema):
    """VgAxisConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    bandPosition : float
        An interpolation fraction indicating where, for `band` scales, axis ticks should be 
        positioned. A value of `0` places ticks at the left edge of their bands. A value of 
        `0.5` places ticks in the middle of their bands.
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as 
        part of the axis.  __Default value:__ `true`
    domainColor : string
        Color of axis domain line.  __Default value:__  (none, using Vega default).
    domainWidth : float
        Stroke width of axis domain line  __Default value:__  (none, using Vega default).
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis  
        __Default value:__ `true` for [continuous scales](scale.html#continuous) that are 
        not binned; otherwise, `false`.
    gridColor : string
        Color of gridlines.
    gridDash : List(float)
        The offset (in pixels) into which to begin drawing with the grid dash array.
    gridOpacity : float
        The stroke opacity of grid (value between [0,1])  __Default value:__ (`1` by 
        default)
    gridWidth : float
        The grid width, in pixels.
    labelAngle : float
        The rotation angle of the axis labels.  __Default value:__ `-90` for nominal and 
        ordinal fields; `0` otherwise.
    labelBound : anyOf(boolean, float)
        Indicates if labels should be hidden if they exceed the axis range. If `false `(the 
        default) no bounds overlap analysis is performed. If `true`, labels will be hidden 
        if they exceed the axis range by more than 1 pixel. If this property is a number, it
         specifies the pixel tolerance: the maximum amount by which a label bounding box may
         exceed the axis range.  __Default value:__ `false`.
    labelColor : string
        The color of the tick label, can be in hex color code or regular color name.
    labelFlush : anyOf(boolean, float)
        Indicates if the first and last axis labels should be aligned flush with the scale 
        range. Flush alignment for a horizontal axis will left-align the first label and 
        right-align the last label. For vertical axes, bottom and top text baselines are 
        applied instead. If this property is a number, it also indicates the number of 
        pixels by which to offset the first and last labels; for example, a value of 2 will 
        flush-align the first and last labels and also push them 2 pixels outward from the 
        center of the axis. The additional adjustment can sometimes help the labels better 
        visually group with corresponding axis ticks.  __Default value:__ `true` for axis of
         a continuous x-scale. Otherwise, `false`.
    labelFont : string
        The font of the tick label.
    labelFontSize : float
        The font size of the label, in pixels.
    labelLimit : float
        Maximum allowed pixel width of axis tick labels.
    labelOverlap : anyOf(boolean, enum('parity'), enum('greedy'))
        The strategy to use for resolving overlap of axis labels. If `false` (the default), 
        no overlap reduction is attempted. If set to `true` or `"parity"`, a strategy of 
        removing every other label is used (this works well for standard linear axes). If 
        set to `"greedy"`, a linear scan of the labels is performed, removing any labels 
        that overlaps with the last visible label (this often works better for log-scaled 
        axes).  __Default value:__ `true` for non-nominal fields with non-log scales; 
        `"greedy"` for log scales; otherwise `false`.
    labelPadding : float
        The padding, in pixels, between axis and text labels.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.  
        __Default value:__  `true`.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines 
        a maximum offset value for axis titles.  __Default value:__ `undefined`.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines 
        a minimum offset value for axis titles.  __Default value:__ `30` for y-axis; 
        `undefined` for x-axis.
    tickColor : string
        The color of the axis's tick.
    tickRound : boolean
        Boolean flag indicating if pixel position values should be rounded to the nearest 
        integer.
    tickSize : float
        The size in pixels of axis ticks.
    tickWidth : float
        The width, in pixels, of ticks.
    ticks : boolean
        Boolean value that determines whether the axis should include ticks.
    titleAlign : string
        Horizontal text alignment of axis titles.
    titleAngle : float
        Angle in degrees of axis titles.
    titleBaseline : string
        Vertical text baseline for axis titles.
    titleColor : string
        Color of the title, can be in hex color code or regular color name.
    titleFont : string
        Font of the title. (e.g., `"Helvetica Neue"`).
    titleFontSize : float
        Font size of the title.
    titleFontWeight : FontWeight
        Font weight of the title. This can be either a string (e.g `"bold"`, `"normal"`) or 
        a number (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = 
        `700`).
    titleLimit : float
        Maximum allowed pixel width of axis titles.
    titleMaxLength : float
        Max length for axis title if the title is automatically generated from the field's 
        description.
    titlePadding : float
        The padding, in pixels, between title and axis.
    titleX : float
        X-coordinate of the axis title relative to the axis group.
    titleY : float
        Y-coordinate of the axis title relative to the axis group.
    """
    _schema = {'$ref': '#/definitions/VgAxisConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined,
                 domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined,
                 gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined,
                 labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined,
                 labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined,
                 labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined,
                 tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined,
                 ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined,
                 titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined,
                 titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined,
                 titlePadding=Undefined, titleX=Undefined, titleY=Undefined, **kwds):
        super(VgAxisConfig, self).__init__(bandPosition=bandPosition, domain=domain,
                                           domainColor=domainColor, domainWidth=domainWidth, grid=grid,
                                           gridColor=gridColor, gridDash=gridDash,
                                           gridOpacity=gridOpacity, gridWidth=gridWidth,
                                           labelAngle=labelAngle, labelBound=labelBound,
                                           labelColor=labelColor, labelFlush=labelFlush,
                                           labelFont=labelFont, labelFontSize=labelFontSize,
                                           labelLimit=labelLimit, labelOverlap=labelOverlap,
                                           labelPadding=labelPadding, labels=labels,
                                           maxExtent=maxExtent, minExtent=minExtent,
                                           tickColor=tickColor, tickRound=tickRound, tickSize=tickSize,
                                           tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign,
                                           titleAngle=titleAngle, titleBaseline=titleBaseline,
                                           titleColor=titleColor, titleFont=titleFont,
                                           titleFontSize=titleFontSize, titleFontWeight=titleFontWeight,
                                           titleLimit=titleLimit, titleMaxLength=titleMaxLength,
                                           titlePadding=titlePadding, titleX=titleX, titleY=titleY,
                                           **kwds)


class VgBinding(VegaLiteSchema):
    """VgBinding schema wrapper
    
    anyOf(VgCheckboxBinding, VgRadioBinding, VgSelectBinding, VgRangeBinding, VgGenericBinding)
    """
    _schema = {'$ref': '#/definitions/VgBinding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(VgBinding, self).__init__(*args, **kwds)


class VgCheckboxBinding(VegaLiteSchema):
    """VgCheckboxBinding schema wrapper
    
    Mapping(required=[input])
    
    Attributes
    ----------
    input : enum('checkbox')
    
    element : string
    
    """
    _schema = {'$ref': '#/definitions/VgCheckboxBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, element=Undefined, **kwds):
        super(VgCheckboxBinding, self).__init__(input=input, element=element, **kwds)


class VgEventStream(VegaLiteSchema):
    """VgEventStream schema wrapper
    
    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/VgEventStream'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(VgEventStream, self).__init__(**kwds)


class VgGenericBinding(VegaLiteSchema):
    """VgGenericBinding schema wrapper
    
    Mapping(required=[input])
    
    Attributes
    ----------
    input : string
    
    element : string
    
    """
    _schema = {'$ref': '#/definitions/VgGenericBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, element=Undefined, **kwds):
        super(VgGenericBinding, self).__init__(input=input, element=element, **kwds)


class VgMarkConfig(VegaLiteSchema):
    """VgMarkConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    align : HorizontalAlign
        The horizontal alignment of the text. One of `"left"`, `"right"`, `"center"`.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : VerticalAlign
        The vertical alignment of the text. One of `"top"`, `"middle"`, `"bottom"`.  
        __Default value:__ `"middle"`
    cursor : enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 
    'wait', 'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop', 
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize', 
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize', 
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
        The mouse cursor used over the mark. Any valid [CSS cursor 
        type](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values) can be used.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The 
        offset is applied after rotation by the _angle_ property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ `1`
    font : string
        The typeface to set the text in (e.g., `"Helvetica Neue"`).
    fontSize : float
        The font size, in pixels.
    fontStyle : FontStyle
        The font style (e.g., `"italic"`).
    fontWeight : FontWeight
        The font weight. This can be either a string (e.g `"bold"`, `"normal"`) or a number 
        (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` = `700`).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : Interpolate
        The line interpolation method to use for line and area marks. One of the following: 
        - `"linear"`: piecewise linear segments, as in a polyline. - `"linear-closed"`: 
        close the linear segments to form a polygon. - `"step"`: alternate between 
        horizontal and vertical segments, as in a step function. - `"step-before"`: 
        alternate between vertical and horizontal segments, as in a step function. - 
        `"step-after"`: alternate between horizontal and vertical segments, as in a step 
        function. - `"basis"`: a B-spline, with control point duplication on the ends. - 
        `"basis-open"`: an open B-spline; may not intersect the start or end. - 
        `"basis-closed"`: a closed B-spline, as in a loop. - `"cardinal"`: a Cardinal 
        spline, with control point duplication on the ends. - `"cardinal-open"`: an open 
        Cardinal spline; may not intersect the start or end, but will intersect other 
        control points. - `"cardinal-closed"`: a closed Cardinal spline, as in a loop. - 
        `"bundle"`: equivalent to basis, except the tension parameter is used to straighten 
        the spline. - `"monotone"`: cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels (default 0, indicating no limit). The 
        text value will be automatically truncated if the rendered size exceeds the limit.
    opacity : float
        The overall opacity (value between [0,1]).  __Default value:__ `0.7` for 
        non-aggregate plots with `point`, `tick`, `circle`, or `square` marks or layered 
        `bar` charts and `1` otherwise.
    orient : Orient
        The orientation of a non-stacked bar, tick, area, and line charts. The value is 
        either horizontal (default) or vertical. - For bar, rule and tick, this determines 
        whether the size of the bar and tick should be applied to x or y dimension. - For 
        area, this property determines the orient property of the Vega output. - For line, 
        this property determines the sort order of the points in the line if 
        `config.sortLineBy` is not specified. For stacked charts, this is always determined 
        by the orientation of the stack; therefore explicitly specified value will be 
        ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin 
        determined by the `x` and `y` properties.
    shape : string
        The default symbol shape to use. One of: `"circle"` (default), `"square"`, 
        `"cross"`, `"diamond"`, `"triangle-up"`, or `"triangle-down"`, or a custom SVG path.
          __Default value:__ `"circle"`
    size : float
        The pixel area each the point/circle/square. For example: in the case of circles, 
        the radius is determined in part by the square root of the size value.  __Default 
        value:__ `30`
    stroke : string
        Default Stroke Color.  This has higher precedence than config.color  __Default 
        value:__ (None)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ `1`
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area 
        marks).
    text : string
        Placeholder text if the `text` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by 
        the `x` and `y` properties. Values for `theta` follow the same convention of `arc` 
        mark `startAngle` and `endAngle` properties: angles are measured in radians, with 
        `0` indicating "north".
    """
    _schema = {'$ref': '#/definitions/VgMarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, cursor=Undefined,
                 dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                 interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(VgMarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, cursor=cursor,
                                           dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, font=font,
                                           fontSize=fontSize, fontStyle=fontStyle,
                                           fontWeight=fontWeight, href=href, interpolate=interpolate,
                                           limit=limit, opacity=opacity, orient=orient, radius=radius,
                                           shape=shape, size=size, stroke=stroke, strokeDash=strokeDash,
                                           strokeDashOffset=strokeDashOffset,
                                           strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                           tension=tension, text=text, theta=theta, **kwds)


class VgProjectionType(VegaLiteSchema):
    """VgProjectionType schema wrapper
    
    enum('albers', 'albersUsa', 'azimuthalEqualArea', 'azimuthalEquidistant', 'conicConformal', 
    'conicEqualArea', 'conicEquidistant', 'equirectangular', 'gnomonic', 'mercator', 
    'orthographic', 'stereographic', 'transverseMercator')
    """
    _schema = {'$ref': '#/definitions/VgProjectionType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VgProjectionType, self).__init__(*args)


class VgRadioBinding(VegaLiteSchema):
    """VgRadioBinding schema wrapper
    
    Mapping(required=[input, options])
    
    Attributes
    ----------
    input : enum('radio')
    
    options : List(string)
    
    element : string
    
    """
    _schema = {'$ref': '#/definitions/VgRadioBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, options=Undefined, element=Undefined, **kwds):
        super(VgRadioBinding, self).__init__(input=input, options=options, element=element, **kwds)


class VgRangeBinding(VegaLiteSchema):
    """VgRangeBinding schema wrapper
    
    Mapping(required=[input])
    
    Attributes
    ----------
    input : enum('range')
    
    element : string
    
    max : float
    
    min : float
    
    step : float
    
    """
    _schema = {'$ref': '#/definitions/VgRangeBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, element=Undefined, max=Undefined, min=Undefined, step=Undefined,
                 **kwds):
        super(VgRangeBinding, self).__init__(input=input, element=element, max=max, min=min, step=step,
                                             **kwds)


class VgScheme(VegaLiteSchema):
    """VgScheme schema wrapper
    
    Mapping(required=[scheme])
    
    Attributes
    ----------
    scheme : string
    
    count : float
    
    extent : List(float)
    
    """
    _schema = {'$ref': '#/definitions/VgScheme'}
    _rootschema = Root._schema

    def __init__(self, scheme=Undefined, count=Undefined, extent=Undefined, **kwds):
        super(VgScheme, self).__init__(scheme=scheme, count=count, extent=extent, **kwds)


class VgSelectBinding(VegaLiteSchema):
    """VgSelectBinding schema wrapper
    
    Mapping(required=[input, options])
    
    Attributes
    ----------
    input : enum('select')
    
    options : List(string)
    
    element : string
    
    """
    _schema = {'$ref': '#/definitions/VgSelectBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, options=Undefined, element=Undefined, **kwds):
        super(VgSelectBinding, self).__init__(input=input, options=options, element=element, **kwds)


class VgTitleConfig(VegaLiteSchema):
    """VgTitleConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    anchor : Anchor
        The anchor position for placing the title. One of `"start"`, `"middle"`, or `"end"`.
         For example, with an orientation of top these anchor positions map to a left-, 
        center-, or right-aligned title.  __Default value:__ `"middle"` for 
        [single](spec.html) and [layered](layer.html) views. `"start"` for other composite 
        views.  __Note:__ [For now](https://github.com/vega/vega-lite/issues/2875), `anchor`
         is only customizable only for [single](spec.html) and [layered](layer.html) views.
          For other composite views, `anchor` is always `"start"`.
    angle : float
        Angle in degrees of title text.
    baseline : VerticalAlign
        Vertical text baseline for title text.
    color : string
        Text color for title text.
    font : string
        Font name for title text.
    fontSize : float
        Font size in pixels for title text.  __Default value:__ `10`.
    fontWeight : FontWeight
        Font weight for title text. This can be either a string (e.g `"bold"`, `"normal"`) 
        or a number (`100`, `200`, `300`, ..., `900` where `"normal"` = `400` and `"bold"` =
         `700`).
    limit : float
        The maximum allowed length in pixels of legend labels.
    offset : float
        Offset in pixels of the title from the chart body and axes.
    orient : TitleOrient
        Default title orientation ("top", "bottom", "left", or "right")
    """
    _schema = {'$ref': '#/definitions/VgTitleConfig'}
    _rootschema = Root._schema

    def __init__(self, anchor=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 font=Undefined, fontSize=Undefined, fontWeight=Undefined, limit=Undefined,
                 offset=Undefined, orient=Undefined, **kwds):
        super(VgTitleConfig, self).__init__(anchor=anchor, angle=angle, baseline=baseline, color=color,
                                            font=font, fontSize=fontSize, fontWeight=fontWeight,
                                            limit=limit, offset=offset, orient=orient, **kwds)


class ViewConfig(VegaLiteSchema):
    """ViewConfig schema wrapper
    
    Mapping(required=[])
    
    Attributes
    ----------
    clip : boolean
        Whether the view should be clipped.
    fill : string
        The fill color.  __Default value:__ (none)
    fillOpacity : float
        The fill opacity (value between [0,1]).  __Default value:__ (none)
    height : float
        The default height of the single plot or each plot in a trellis plot when the 
        visualization has a continuous (non-ordinal) y-scale with `rangeStep` = `null`.  
        __Default value:__ `200`
    stroke : string
        The stroke color.  __Default value:__ (none)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.  
        __Default value:__ (none)
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.  
        __Default value:__ (none)
    strokeOpacity : float
        The stroke opacity (value between [0,1]).  __Default value:__ (none)
    strokeWidth : float
        The stroke width, in pixels.  __Default value:__ (none)
    width : float
        The default width of the single plot or each plot in a trellis plot when the 
        visualization has a continuous (non-ordinal) x-scale or ordinal x-scale with 
        `rangeStep` = `null`.  __Default value:__ `200`
    """
    _schema = {'$ref': '#/definitions/ViewConfig'}
    _rootschema = Root._schema

    def __init__(self, clip=Undefined, fill=Undefined, fillOpacity=Undefined, height=Undefined,
                 stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, width=Undefined, **kwds):
        super(ViewConfig, self).__init__(clip=clip, fill=fill, fillOpacity=fillOpacity, height=height,
                                         stroke=stroke, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, width=width, **kwds)

