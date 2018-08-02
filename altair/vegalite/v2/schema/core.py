# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import SchemaBase, Undefined

import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, 'vega-lite-schema.json').decode('utf-8'))


class VegaLiteSchema(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return VegaLiteSchema.__subclasses__()


class Root(VegaLiteSchema):
    """Root schema wrapper

    anyOf(:class:`TopLevelFacetedUnitSpec`, :class:`TopLevelFacetSpec`,
    :class:`TopLevelLayerSpec`, :class:`TopLevelRepeatSpec`, :class:`TopLevelVConcatSpec`,
    :class:`TopLevelHConcatSpec`)
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

    aggregate : List(:class:`AggregatedFieldDef`)
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

    Mapping(required=[op, as])

    Attributes
    ----------

    op : :class:`AggregateOp`
        The aggregation operations to apply to the fields, such as sum, average or count.
        See the `full list of supported aggregation operations
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__
        for more information.
    field : string
        The data field for which to compute aggregate function. This is required for all
        aggregation operations except ``"count"``.
    as : string
        The output field names to use for each aggregated field.
    """
    _schema = {'$ref': '#/definitions/AggregatedFieldDef'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, **kwds):
        super(AggregatedFieldDef, self).__init__(op=op, field=field, **kwds)


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

    anyOf(:class:`Mark`, :class:`MarkDef`)
    """
    _schema = {'$ref': '#/definitions/AnyMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(AnyMark, self).__init__(*args, **kwds)


class AreaConfig(VegaLiteSchema):
    """AreaConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    line : anyOf(boolean, :class:`OverlayMarkDef`)
        A flag for overlaying line on top of area marks, or an object defining the
        properties of the overlayed lines.


        If this value is an empty object ( ``{}`` ) or ``true``, lines with default
        properties will be used.

        If this value is ``false``, no lines would be automatically added to area marks.

        **Default value:** ``false``.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    point : anyOf(boolean, :class:`OverlayMarkDef`, enum('transparent'))
        A flag for overlaying points on top of line or area marks, or an object defining the
        properties of the overlayed points.


        If this property is ``"transparent"``, transparent points will be used (for
        enhancing tooltips and selections).

        If this property is an empty object ( ``{}`` ) or ``true``, filled points with
        default properties will be used.

        If this property is ``false``, no points would be automatically added to line or
        area marks.

        **Default value:** ``false``.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/AreaConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 cornerRadius=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined,
                 ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined,
                 font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                 href=Undefined, interpolate=Undefined, limit=Undefined, line=Undefined,
                 opacity=Undefined, orient=Undefined, point=Undefined, radius=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeCap=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeJoin=Undefined,
                 strokeMiterLimit=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined,
                 tension=Undefined, text=Undefined, theta=Undefined, tooltip=Undefined, **kwds):
        super(AreaConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color,
                                         cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx,
                                         dy=dy, ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                         filled=filled, font=font, fontSize=fontSize,
                                         fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                                         interpolate=interpolate, limit=limit, line=line,
                                         opacity=opacity, orient=orient, point=point, radius=radius,
                                         shape=shape, size=size, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta, tooltip=tooltip,
                                         **kwds)


class AutoSizeParams(VegaLiteSchema):
    """AutoSizeParams schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    contains : enum('content', 'padding')
        Determines how size calculation should be performed, one of ``"content"`` or
        ``"padding"``. The default setting ( ``"content"`` ) interprets the width and height
        settings as the data rectangle (plotting) dimensions, to which padding is then
        added. In contrast, the ``"padding"`` setting includes the padding within the view
        size calculations, such that the width and height settings indicate the **total**
        intended size of the view.

        **Default value** : ``"content"``
    resize : boolean
        A boolean flag indicating if autosize layout should be re-calculated on every view
        update.

        **Default value** : ``false``
    type : :class:`AutosizeType`
        The sizing format type. One of ``"pad"``, ``"fit"`` or ``"none"``. See the `autosize
        type <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ documentation for
        descriptions of each.

        **Default value** : ``"pad"``
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
        part of the axis.

        **Default value:** ``true``
    format : string
        The formatting pattern for labels. This is D3's `number format pattern
        <https://github.com/d3/d3-format#locale_format>`__ for quantitative fields and D3's
        `time format pattern <https://github.com/d3/d3-time-format#locale_format>`__ for
        time field.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more information.

        **Default value:**  derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for
        quantitative fields and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for temporal
        fields.
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis

        **Default value:** ``true`` for `continuous scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ that are not
        binned; otherwise, ``false``.
    labelAngle : float
        The rotation angle of the axis labels.

        **Default value:** ``-90`` for nominal and ordinal fields; ``0`` otherwise.
    labelBound : anyOf(boolean, float)
        Indicates if labels should be hidden if they exceed the axis range. If ``false``
        (the default) no bounds overlap analysis is performed. If ``true``, labels will be
        hidden if they exceed the axis range by more than 1 pixel. If this property is a
        number, it specifies the pixel tolerance: the maximum amount by which a label
        bounding box may exceed the axis range.

        **Default value:** ``false``.
    labelFlush : anyOf(boolean, float)
        Indicates if the first and last axis labels should be aligned flush with the scale
        range. Flush alignment for a horizontal axis will left-align the first label and
        right-align the last label. For vertical axes, bottom and top text baselines are
        applied instead. If this property is a number, it also indicates the number of
        pixels by which to offset the first and last labels; for example, a value of 2 will
        flush-align the first and last labels and also push them 2 pixels outward from the
        center of the axis. The additional adjustment can sometimes help the labels better
        visually group with corresponding axis ticks.

        **Default value:** ``true`` for axis of a continuous x-scale. Otherwise, ``false``.
    labelOverlap : anyOf(boolean, enum('parity'), enum('greedy'))
        The strategy to use for resolving overlap of axis labels. If ``false`` (the
        default), no overlap reduction is attempted. If set to ``true`` or ``"parity"``, a
        strategy of removing every other label is used (this works well for standard linear
        axes). If set to ``"greedy"``, a linear scan of the labels is performed, removing
        any labels that overlaps with the last visible label (this often works better for
        log-scaled axes).

        **Default value:** ``true`` for non-nominal fields with non-log scales; ``"greedy"``
        for log scales; otherwise ``false``.
    labelPadding : float
        The padding, in pixels, between axis and text labels.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.

        **Default value:**  ``true``.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines
        a maximum offset value for axis titles.

        **Default value:** ``undefined``.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines
        a minimum offset value for axis titles.

        **Default value:** ``30`` for y-axis; ``undefined`` for x-axis.
    offset : float
        The offset, in pixels, by which to displace the axis from the edge of the enclosing
        group or data rectangle.

        **Default value:** derived from the `axis config
        <https://vega.github.io/vega-lite/docs/config.html#facet-scale-config>`__ 's
        ``offset`` ( ``0`` by default)
    orient : :class:`AxisOrient`
        The orientation of the axis. One of ``"top"``, ``"bottom"``, ``"left"`` or
        ``"right"``. The orientation can be used to further specialize the axis type (e.g.,
        a y axis oriented for the right edge of the chart).

        **Default value:** ``"bottom"`` for x-axes and ``"left"`` for y-axes.
    position : float
        The anchor position of the axis in pixels. For x-axis with top or bottom
        orientation, this sets the axis group x coordinate. For y-axis with left or right
        orientation, this sets the axis group y coordinate.

        **Default value** : ``0``
    tickCount : float
        A desired number of ticks, for axes visualizing quantitative scales. The resulting
        number may be different so that values are "nice" (multiples of 2, 5, 10) and lie
        within the underlying scale's range.
    tickSize : float
        The size in pixels of axis ticks.
    ticks : boolean
        Boolean value that determines whether the axis should include ticks.
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    titleMaxLength : float
        Max length for axis title if the title is automatically generated from the field's
        description.
    titlePadding : float
        The padding, in pixels, between title and axis.
    values : anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`))
        Explicitly set the visible axis tick values.
    zindex : float
        A non-positive integer indicating z-index of the axis.
        If zindex is 0, axes should be drawn behind all chart elements.
        To put them in front, use ``"zindex = 1"``.

        **Default value:** ``1`` (in front of the marks) for actual axis and ``0`` (behind
        the marks) for grids.
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
        An interpolation fraction indicating where, for ``band`` scales, axis ticks should
        be positioned. A value of ``0`` places ticks at the left edge of their bands. A
        value of ``0.5`` places ticks in the middle of their bands.
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as
        part of the axis.

        **Default value:** ``true``
    domainColor : string
        Color of axis domain line.

        **Default value:**  (none, using Vega default).
    domainWidth : float
        Stroke width of axis domain line

        **Default value:**  (none, using Vega default).
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis

        **Default value:** ``true`` for `continuous scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ that are not
        binned; otherwise, ``false``.
    gridColor : string
        Color of gridlines.
    gridDash : List(float)
        The offset (in pixels) into which to begin drawing with the grid dash array.
    gridOpacity : float
        The stroke opacity of grid (value between [0,1])

        **Default value:** ( ``1`` by default)
    gridWidth : float
        The grid width, in pixels.
    labelAngle : float
        The rotation angle of the axis labels.

        **Default value:** ``-90`` for nominal and ordinal fields; ``0`` otherwise.
    labelBound : anyOf(boolean, float)
        Indicates if labels should be hidden if they exceed the axis range. If ``false``
        (the default) no bounds overlap analysis is performed. If ``true``, labels will be
        hidden if they exceed the axis range by more than 1 pixel. If this property is a
        number, it specifies the pixel tolerance: the maximum amount by which a label
        bounding box may exceed the axis range.

        **Default value:** ``false``.
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
        visually group with corresponding axis ticks.

        **Default value:** ``true`` for axis of a continuous x-scale. Otherwise, ``false``.
    labelFont : string
        The font of the tick label.
    labelFontSize : float
        The font size of the label, in pixels.
    labelLimit : float
        Maximum allowed pixel width of axis tick labels.
    labelOverlap : anyOf(boolean, enum('parity'), enum('greedy'))
        The strategy to use for resolving overlap of axis labels. If ``false`` (the
        default), no overlap reduction is attempted. If set to ``true`` or ``"parity"``, a
        strategy of removing every other label is used (this works well for standard linear
        axes). If set to ``"greedy"``, a linear scan of the labels is performed, removing
        any labels that overlaps with the last visible label (this often works better for
        log-scaled axes).

        **Default value:** ``true`` for non-nominal fields with non-log scales; ``"greedy"``
        for log scales; otherwise ``false``.
    labelPadding : float
        The padding, in pixels, between axis and text labels.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.

        **Default value:**  ``true``.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines
        a maximum offset value for axis titles.

        **Default value:** ``undefined``.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines
        a minimum offset value for axis titles.

        **Default value:** ``30`` for y-axis; ``undefined`` for x-axis.
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.

        **Default value:**  ``false``
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
        Font of the title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
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

    x : :class:`ResolveMode`

    y : :class:`ResolveMode`

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

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    binSpacing : float
        Offset between bars for binned field.  Ideal value for this is either 0 (Preferred
        by statisticians) or 1 (Vega-Lite Default, D3 example style).

        **Default value:** ``1``
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    continuousBandSize : float
        The default size of the bars on continuous scales.

        **Default value:** ``5``
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    discreteBandSize : float
        The size of the bars.  If unspecified, the default size is  ``bandSize-1``,
        which provides 1 pixel offset between bars.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/BarConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined,
                 color=Undefined, continuousBandSize=Undefined, cornerRadius=Undefined,
                 cursor=Undefined, dir=Undefined, discreteBandSize=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined,
                 opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, tooltip=Undefined, **kwds):
        super(BarConfig, self).__init__(align=align, angle=angle, baseline=baseline,
                                        binSpacing=binSpacing, color=color,
                                        continuousBandSize=continuousBandSize,
                                        cornerRadius=cornerRadius, cursor=cursor, dir=dir,
                                        discreteBandSize=discreteBandSize, dx=dx, dy=dy,
                                        ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                        filled=filled, font=font, fontSize=fontSize,
                                        fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                                        interpolate=interpolate, limit=limit, opacity=opacity,
                                        orient=orient, radius=radius, shape=shape, size=size,
                                        stroke=stroke, strokeCap=strokeCap, strokeDash=strokeDash,
                                        strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                        strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                        strokeWidth=strokeWidth, tension=tension, text=text,
                                        theta=theta, tooltip=tooltip, **kwds)


class Baseline(VegaLiteSchema):
    """Baseline schema wrapper

    enum('top', 'middle', 'bottom')
    """
    _schema = {'$ref': '#/definitions/Baseline'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Baseline, self).__init__(*args)


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

    anchor : float
        A value in the binned domain at which to anchor the bins, shifting the bin
        boundaries if necessary to ensure that a boundary aligns with the anchor value.

        **Default Value:** the minimum bin extent value
    base : float
        The number base to use for automatic bin determination (default is base 10).

        **Default value:** ``10``
    divide : List(float)
        Scale factors indicating allowable subdivisions. The default value is [5, 2], which
        indicates that for base 10 numbers (the default base), the method may consider
        dividing bin sizes by 5 and/or 2. For example, for an initial step size of 10, the
        method can check if bin sizes of 2 (= 10/5), 5 (= 10/2), or 1 (= 10/(5*2)) might
        also satisfy the given constraints.

        **Default value:** ``[5, 2]``
    extent : List(float)
        A two-element ( ``[min, max]`` ) array indicating the range of desired bin values.
    maxbins : float
        Maximum number of bins.

        **Default value:** ``6`` for ``row``, ``column`` and ``shape`` channels; ``10`` for
        other channels
    minstep : float
        A minimum allowable step size (particularly useful for integer values).
    nice : boolean
        If true (the default), attempts to make the bin boundaries use human-friendly
        boundaries, such as multiples of ten.
    step : float
        An exact step size to use between bins.

        **Note:** If provided, options such as maxbins will be ignored.
    steps : List(float)
        An array of allowable step sizes to choose from.
    """
    _schema = {'$ref': '#/definitions/BinParams'}
    _rootschema = Root._schema

    def __init__(self, anchor=Undefined, base=Undefined, divide=Undefined, extent=Undefined,
                 maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined,
                 **kwds):
        super(BinParams, self).__init__(anchor=anchor, base=base, divide=divide, extent=extent,
                                        maxbins=maxbins, minstep=minstep, nice=nice, step=step,
                                        steps=steps, **kwds)


class BinTransform(VegaLiteSchema):
    """BinTransform schema wrapper

    Mapping(required=[bin, field, as])

    Attributes
    ----------

    bin : anyOf(boolean, :class:`BinParams`)
        An object indicating bin properties, or simply ``true`` for using default bin
        parameters.
    field : string
        The data field to bin.
    as : anyOf(string, List(string))
        The output fields at which to write the start and end bin values.
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
        The fill color of the interval mark.

        **Default value:** ``#333333``
    fillOpacity : float
        The fill opacity of the interval mark (a value between 0 and 1).

        **Default value:** ``0.125``
    stroke : string
        The stroke color of the interval mark.

        **Default value:** ``#ffffff``
    strokeDash : List(float)
        An array of alternating stroke and space lengths,
        for creating dashed or dotted lines.
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
        A `expression <https://vega.github.io/vega-lite/docs/types.html#expression>`__
        string. Use the variable ``datum`` to refer to the current data object.
    as : string
        The field for storing the computed formula value.
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

    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.

        **Default value:**


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its y-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the height will
          be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For y-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the height is `determined by the range step, paddings, and the
          cardinality of the field mapped to y-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__. Otherwise, if the
          ``rangeStep`` is ``null``, the height will be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``y`` channel, the ``height`` will be the value of
          ``rangeStep``.

        **Note** : For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.

        **Default value:** This will be determined by the following rules:


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its x-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the width will
          be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For x-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the width is `determined by the range step, paddings, and the
          cardinality of the field mapped to x-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__.   Otherwise, if the
          ``rangeStep`` is ``null``, the width will be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``x`` channel, the ``width`` will be the value of
          `config.scale.textXRangeStep
          <https://vega.github.io/vega-lite/docs/size.html#default-width-and-height>`__ for
          ``text`` mark and the value of ``rangeStep`` for other marks.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
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

    anyOf(:class:`ConditionalPredicateFieldDef`, :class:`ConditionalSelectionFieldDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalFieldDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalFieldDef, self).__init__(*args, **kwds)


class ConditionalMarkPropFieldDef(VegaLiteSchema):
    """ConditionalMarkPropFieldDef schema wrapper

    anyOf(:class:`ConditionalPredicateMarkPropFieldDef`,
    :class:`ConditionalSelectionMarkPropFieldDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalMarkPropFieldDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDef, self).__init__(*args, **kwds)


class ConditionalTextFieldDef(VegaLiteSchema):
    """ConditionalTextFieldDef schema wrapper

    anyOf(:class:`ConditionalPredicateTextFieldDef`, :class:`ConditionalSelectionTextFieldDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalTextFieldDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalTextFieldDef, self).__init__(*args, **kwds)


class ConditionalValueDef(VegaLiteSchema):
    """ConditionalValueDef schema wrapper

    anyOf(:class:`ConditionalPredicateValueDef`, :class:`ConditionalSelectionValueDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalValueDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalValueDef, self).__init__(*args, **kwds)


class ConditionalPredicateFieldDef(VegaLiteSchema):
    """ConditionalPredicateFieldDef schema wrapper

    Mapping(required=[test, type])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(ConditionalPredicateFieldDef, self).__init__(test=test, type=type, aggregate=aggregate,
                                                           bin=bin, field=field, timeUnit=timeUnit,
                                                           title=title, **kwds)


class ConditionalPredicateMarkPropFieldDef(VegaLiteSchema):
    """ConditionalPredicateMarkPropFieldDef schema wrapper

    Mapping(required=[test, type])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(ConditionalPredicateMarkPropFieldDef, self).__init__(test=test, type=type,
                                                                   aggregate=aggregate, bin=bin,
                                                                   field=field, legend=legend,
                                                                   scale=scale, sort=sort,
                                                                   timeUnit=timeUnit, title=title,
                                                                   **kwds)


class ConditionalPredicateTextFieldDef(VegaLiteSchema):
    """ConditionalPredicateTextFieldDef schema wrapper

    Mapping(required=[test, type])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The `formatting pattern <https://vega.github.io/vega-lite/docs/format.html>`__ for a
        text field. If not defined, this will be determined automatically.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(ConditionalPredicateTextFieldDef, self).__init__(test=test, type=type,
                                                               aggregate=aggregate, bin=bin,
                                                               field=field, format=format,
                                                               timeUnit=timeUnit, title=title, **kwds)


class ConditionalPredicateValueDef(VegaLiteSchema):
    """ConditionalPredicateValueDef schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`

    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
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

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(ConditionalSelectionFieldDef, self).__init__(selection=selection, type=type,
                                                           aggregate=aggregate, bin=bin, field=field,
                                                           timeUnit=timeUnit, title=title, **kwds)


class ConditionalSelectionMarkPropFieldDef(VegaLiteSchema):
    """ConditionalSelectionMarkPropFieldDef schema wrapper

    Mapping(required=[selection, type])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(ConditionalSelectionMarkPropFieldDef, self).__init__(selection=selection, type=type,
                                                                   aggregate=aggregate, bin=bin,
                                                                   field=field, legend=legend,
                                                                   scale=scale, sort=sort,
                                                                   timeUnit=timeUnit, title=title,
                                                                   **kwds)


class ConditionalSelectionTextFieldDef(VegaLiteSchema):
    """ConditionalSelectionTextFieldDef schema wrapper

    Mapping(required=[selection, type])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The `formatting pattern <https://vega.github.io/vega-lite/docs/format.html>`__ for a
        text field. If not defined, this will be determined automatically.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(ConditionalSelectionTextFieldDef, self).__init__(selection=selection, type=type,
                                                               aggregate=aggregate, bin=bin,
                                                               field=field, format=format,
                                                               timeUnit=timeUnit, title=title, **kwds)


class ConditionalSelectionValueDef(VegaLiteSchema):
    """ConditionalSelectionValueDef schema wrapper

    Mapping(required=[selection, value])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
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

    area : :class:`AreaConfig`
        Area-Specific Config
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    axis : :class:`AxisConfig`
        Axis configuration, which determines default properties for all ``x`` and ``y``
        `axes <https://vega.github.io/vega-lite/docs/axis.html>`__. For a full list of axis
        configuration options, please see the `corresponding section of the axis
        documentation <https://vega.github.io/vega-lite/docs/axis.html#config>`__.
    axisBand : :class:`VgAxisConfig`
        Specific axis config for axes with "band" scales.
    axisBottom : :class:`VgAxisConfig`
        Specific axis config for x-axis along the bottom edge of the chart.
    axisLeft : :class:`VgAxisConfig`
        Specific axis config for y-axis along the left edge of the chart.
    axisRight : :class:`VgAxisConfig`
        Specific axis config for y-axis along the right edge of the chart.
    axisTop : :class:`VgAxisConfig`
        Specific axis config for x-axis along the top edge of the chart.
    axisX : :class:`VgAxisConfig`
        X-axis specific config.
    axisY : :class:`VgAxisConfig`
        Y-axis specific config.
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    bar : :class:`BarConfig`
        Bar-Specific Config
    circle : :class:`MarkConfig`
        Circle-Specific Config
    countTitle : string
        Default axis and legend title for count fields.

        **Default value:** ``'Number of Records'``.
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    fieldTitle : enum('verbal', 'functional', 'plain')
        Defines how Vega-Lite generates title for fields.  There are three possible styles:


        * ``"verbal"`` (Default) - displays function in a verbal style (e.g., "Sum of
          field", "Year-month of date", "field (binned)").
        * ``"function"`` - displays function using parentheses and capitalized texts (e.g.,
          "SUM(field)", "YEARMONTH(date)", "BIN(field)").
        * ``"plain"`` - displays only the field name without functions (e.g., "field",
          "date", "field").
    geoshape : :class:`MarkConfig`
        Geoshape-Specific Config
    header : :class:`HeaderConfig`
        Header configuration, which determines default properties for all `header
        <https://vega.github.io/vega-lite/docs/header.html>`__. For a full list of header
        configuration options, please see the `corresponding section of in the header
        documentation <https://vega.github.io/vega-lite/docs/header.html#config>`__.
    invalidValues : enum('filter', None)
        Defines how Vega-Lite should handle invalid values ( ``null`` and ``NaN`` ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
    legend : :class:`LegendConfig`
        Legend configuration, which determines default properties for all `legends
        <https://vega.github.io/vega-lite/docs/legend.html>`__. For a full list of legend
        configuration options, please see the `corresponding section of in the legend
        documentation <https://vega.github.io/vega-lite/docs/legend.html#config>`__.
    line : :class:`LineConfig`
        Line-Specific Config
    mark : :class:`MarkConfig`
        Mark Config
    numberFormat : string
        D3 Number format for axis labels and text tables. For example "s" for SI units. Use
        `D3's number format pattern <https://github.com/d3/d3-format#locale_format>`__.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    point : :class:`MarkConfig`
        Point-Specific Config
    projection : :class:`ProjectionConfig`
        Projection configuration, which determines default properties for all `projections
        <https://vega.github.io/vega-lite/docs/projection.html>`__. For a full list of
        projection configuration options, please see the `corresponding section of the
        projection documentation
        <https://vega.github.io/vega-lite/docs/projection.html#config>`__.
    range : :class:`RangeConfig`
        An object hash that defines default range arrays or schemes for using with scales.
        For a full list of scale range configuration options, please see the `corresponding
        section of the scale documentation
        <https://vega.github.io/vega-lite/docs/scale.html#config>`__.
    rect : :class:`MarkConfig`
        Rect-Specific Config
    rule : :class:`MarkConfig`
        Rule-Specific Config
    scale : :class:`ScaleConfig`
        Scale configuration determines default properties for all `scales
        <https://vega.github.io/vega-lite/docs/scale.html>`__. For a full list of scale
        configuration options, please see the `corresponding section of the scale
        documentation <https://vega.github.io/vega-lite/docs/scale.html#config>`__.
    selection : :class:`SelectionConfig`
        An object hash for defining default properties for each type of selections.
    square : :class:`MarkConfig`
        Square-Specific Config
    stack : :class:`StackOffset`
        Default stack offset for stackable mark.
    style : :class:`StyleConfigIndex`
        An object hash that defines key-value mappings to determine default properties for
        marks with a given `style
        <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.  The keys represent
        styles names; the values have to be valid `mark configuration objects
        <https://vega.github.io/vega-lite/docs/mark.html#config>`__.
    text : :class:`TextConfig`
        Text-Specific Config
    tick : :class:`TickConfig`
        Tick-Specific Config
    timeFormat : string
        Default datetime format for axis and legend labels. The format can be set directly
        on each axis and legend. Use `D3's time format pattern
        <https://github.com/d3/d3-time-format#locale_format>`__.

        **Default value:** ``''`` (The format will be automatically determined).
    title : :class:`VgTitleConfig`
        Title configuration, which determines default properties for all `titles
        <https://vega.github.io/vega-lite/docs/title.html>`__. For a full list of title
        configuration options, please see the `corresponding section of the title
        documentation <https://vega.github.io/vega-lite/docs/title.html#config>`__.
    trail : :class:`LineConfig`
        Trail-Specific Config
    view : :class:`ViewConfig`
        Default properties for `single view plots
        <https://vega.github.io/vega-lite/docs/spec.html#single>`__.
    """
    _schema = {'$ref': '#/definitions/Config'}
    _rootschema = Root._schema

    def __init__(self, area=Undefined, autosize=Undefined, axis=Undefined, axisBand=Undefined,
                 axisBottom=Undefined, axisLeft=Undefined, axisRight=Undefined, axisTop=Undefined,
                 axisX=Undefined, axisY=Undefined, background=Undefined, bar=Undefined,
                 circle=Undefined, countTitle=Undefined, datasets=Undefined, fieldTitle=Undefined,
                 geoshape=Undefined, header=Undefined, invalidValues=Undefined, legend=Undefined,
                 line=Undefined, mark=Undefined, numberFormat=Undefined, padding=Undefined,
                 point=Undefined, projection=Undefined, range=Undefined, rect=Undefined, rule=Undefined,
                 scale=Undefined, selection=Undefined, square=Undefined, stack=Undefined,
                 style=Undefined, text=Undefined, tick=Undefined, timeFormat=Undefined, title=Undefined,
                 trail=Undefined, view=Undefined, **kwds):
        super(Config, self).__init__(area=area, autosize=autosize, axis=axis, axisBand=axisBand,
                                     axisBottom=axisBottom, axisLeft=axisLeft, axisRight=axisRight,
                                     axisTop=axisTop, axisX=axisX, axisY=axisY, background=background,
                                     bar=bar, circle=circle, countTitle=countTitle, datasets=datasets,
                                     fieldTitle=fieldTitle, geoshape=geoshape, header=header,
                                     invalidValues=invalidValues, legend=legend, line=line, mark=mark,
                                     numberFormat=numberFormat, padding=padding, point=point,
                                     projection=projection, range=range, rect=rect, rule=rule,
                                     scale=scale, selection=selection, square=square, stack=stack,
                                     style=style, text=text, tick=tick, timeFormat=timeFormat,
                                     title=title, trail=trail, view=view, **kwds)


class CsvDataFormat(VegaLiteSchema):
    """CsvDataFormat schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    parse : anyOf(enum('auto'), :class:`Parse`, None)
        If set to ``"auto"`` (the default), perform automatic type inference to determine
        the desired data types.
        If set to ``null``, disable type inference based on the spec and only use type
        inference based on the data.
        Alternatively, a parsing directive object can be provided for explicit data types.
        Each property of the object corresponds to a field name, and the value to the
        desired data type (one of ``"number"``, ``"boolean"``, ``"date"``, or null (do not
        parse the field)).
        For example, ``"parse": {"modified_on": "date"}`` parses the ``modified_on`` field
        in each input record a Date value.

        For ``"date"``, we parse data based using Javascript's `Date.parse()
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse>`__.
        For Specific date formats can be provided (e.g., ``{foo: 'date:"%m%d%Y"'}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: 'utc:"%m%d%Y"'}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    type : enum('csv', 'tsv')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.
        The default format type is determined by the extension of the file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/CsvDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, type=Undefined, **kwds):
        super(CsvDataFormat, self).__init__(parse=parse, type=type, **kwds)


class Cursor(VegaLiteSchema):
    """Cursor schema wrapper

    enum('auto', 'default', 'none', 'context-menu', 'help', 'pointer', 'progress', 'wait',
    'cell', 'crosshair', 'text', 'vertical-text', 'alias', 'copy', 'move', 'no-drop',
    'not-allowed', 'e-resize', 'n-resize', 'ne-resize', 'nw-resize', 's-resize', 'se-resize',
    'sw-resize', 'w-resize', 'ew-resize', 'ns-resize', 'nesw-resize', 'nwse-resize',
    'col-resize', 'row-resize', 'all-scroll', 'zoom-in', 'zoom-out', 'grab', 'grabbing')
    """
    _schema = {'$ref': '#/definitions/Cursor'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Cursor, self).__init__(*args)


class Data(VegaLiteSchema):
    """Data schema wrapper

    anyOf(:class:`UrlData`, :class:`InlineData`, :class:`NamedData`)
    """
    _schema = {'$ref': '#/definitions/Data'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Data, self).__init__(*args, **kwds)


class DataFormat(VegaLiteSchema):
    """DataFormat schema wrapper

    anyOf(:class:`CsvDataFormat`, :class:`DsvDataFormat`, :class:`JsonDataFormat`,
    :class:`TopoDataFormat`)
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
    ``day`` cannot be combined with other date.
    We accept string for month and day names.

    Attributes
    ----------

    date : float
        Integer value representing the date from 1-31.
    day : anyOf(:class:`Day`, string)
        Value representing the day of a week.  This can be one of: (1) integer value --
        ``1`` represents Monday; (2) case-insensitive day name (e.g., ``"Monday"`` );  (3)
        case-insensitive, 3-character short day name (e.g., ``"Mon"`` ).   :raw-html:`<br/>`
        **Warning:** A DateTime definition object with ``day`` ** should not be combined
        with ``year``, ``quarter``, ``month``, or ``date``.
    hours : float
        Integer value representing the hour of a day from 0-23.
    milliseconds : float
        Integer value representing the millisecond segment of time.
    minutes : float
        Integer value representing the minute segment of time from 0-59.
    month : anyOf(:class:`Month`, string)
        One of: (1) integer value representing the month from ``1`` - ``12``. ``1``
        represents January;  (2) case-insensitive month name (e.g., ``"January"`` );  (3)
        case-insensitive, 3-character short month name (e.g., ``"Jan"`` ).
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


class Dir(VegaLiteSchema):
    """Dir schema wrapper

    enum('ltr', 'rtl')
    """
    _schema = {'$ref': '#/definitions/Dir'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Dir, self).__init__(*args)


class DsvDataFormat(VegaLiteSchema):
    """DsvDataFormat schema wrapper

    Mapping(required=[delimiter])

    Attributes
    ----------

    delimiter : string
        The delimiter between records. The delimiter must be a single character (i.e., a
        single 16-bit code unit); so, ASCII delimiters are fine, but emoji delimiters are
        not.
    parse : anyOf(enum('auto'), :class:`Parse`, None)
        If set to ``"auto"`` (the default), perform automatic type inference to determine
        the desired data types.
        If set to ``null``, disable type inference based on the spec and only use type
        inference based on the data.
        Alternatively, a parsing directive object can be provided for explicit data types.
        Each property of the object corresponds to a field name, and the value to the
        desired data type (one of ``"number"``, ``"boolean"``, ``"date"``, or null (do not
        parse the field)).
        For example, ``"parse": {"modified_on": "date"}`` parses the ``modified_on`` field
        in each input record a Date value.

        For ``"date"``, we parse data based using Javascript's `Date.parse()
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse>`__.
        For Specific date formats can be provided (e.g., ``{foo: 'date:"%m%d%Y"'}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: 'utc:"%m%d%Y"'}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    type : enum('dsv')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.
        The default format type is determined by the extension of the file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/DsvDataFormat'}
    _rootschema = Root._schema

    def __init__(self, delimiter=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(DsvDataFormat, self).__init__(delimiter=delimiter, parse=parse, type=type, **kwds)


class Encoding(VegaLiteSchema):
    """Encoding schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        Color of the marks – either fill or stroke color based on  the ``filled`` property
        of mark definition.
        By default, ``color`` represents fill color for ``"area"``, ``"bar"``, ``"tick"``,
        ``"text"``, ``"trail"``, ``"circle"``, and ``"square"`` / stroke color for
        ``"line"`` and ``"point"``.

        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:*
        1) For fine-grained control over both fill and stroke colors of the marks, please
        use the ``fill`` and ``stroke`` channels.  If either ``fill`` or ``stroke`` channel
        is specified, ``color`` channel will be ignored.
        2) See the scale documentation for more information about customizing `color scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__.
    detail : anyOf(:class:`FieldDef`, List(:class:`FieldDef`))
        Additional levels of detail for grouping data in aggregate views and
        in line, trail, and area marks without mapping data to a specific visual channel.
    fill : anyOf(:class:`MarkPropFieldDefWithCondition`, :class:`MarkPropValueDefWithCondition`)
        Fill color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* When using ``fill`` channel, ``color`` channel will be ignored. To customize
        both fill and stroke, please use ``fill`` and ``stroke`` channels (not ``fill`` and
        ``color`` ).
    href : anyOf(:class:`FieldDefWithCondition`, :class:`ValueDefWithCondition`)
        A URL to load upon mouse click.
    key : :class:`FieldDef`
        A data field to use as a unique key for data binding. When a visualization’s data is
        updated, the key value will be used to match data elements to existing mark
        instances. Use a key channel to enable object constancy for transitions over dynamic
        data.
    latitude : :class:`FieldDef`
        Latitude position of geographically projected marks.
    latitude2 : :class:`FieldDef`
        Latitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    longitude : :class:`FieldDef`
        Longitude position of geographically projected marks.
    longitude2 : :class:`FieldDef`
        Longitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    opacity : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        Opacity of the marks – either can be a value or a range.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``opacity`` property.
    order : anyOf(:class:`OrderFieldDef`, List(:class:`OrderFieldDef`), :class:`ValueDef`)
        Order of the marks.


        * For stacked marks, this ``order`` channel encodes `stack order
          <https://vega.github.io/vega-lite/docs/stack.html#order>`__.
        * For line and trail marks, this ``order`` channel encodes order of data points in
          the lines. This can be useful for creating `a connected scatterplot
          <https://vega.github.io/vega-lite/examples/connected_scatterplot.html>`__.
          Setting ``order`` to ``{"value": null}`` makes the line marks use the original
          order in the data sources.
        * Otherwise, this ``order`` channel encodes layer order of the marks.

        **Note** : In aggregate plots, ``order`` field should be ``aggregate`` d to avoid
        creating additional aggregation grouping.
    shape : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        For ``point`` marks the supported values are
        ``"circle"`` (default), ``"square"``, ``"cross"``, ``"diamond"``, ``"triangle-up"``,
        or ``"triangle-down"``, or else a custom SVG path string.
        For ``geoshape`` marks it should be a field definition of the geojson data

        **Default value:** If undefined, the default shape depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#point-config>`__ 's ``shape``
        property.
    size : anyOf(:class:`MarkPropFieldDefWithCondition`, :class:`MarkPropValueDefWithCondition`)
        Size of the mark.


        * For ``"point"``, ``"square"`` and ``"circle"``, – the symbol size, or pixel area
          of the mark.
        * For ``"bar"`` and ``"tick"`` – the bar and tick's size.
        * For ``"text"`` – the text's font size.
        * Size is unsupported for ``"line"``, ``"area"``, and ``"rect"``. (Use ``"trail"``
          instead of line with varying size)
    stroke : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        Stroke color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* When using ``stroke`` channel, ``color`` channel will be ignored. To
        customize both stroke and fill, please use ``stroke`` and ``fill`` channels (not
        ``stroke`` and ``color`` ).
    text : anyOf(:class:`TextFieldDefWithCondition`, :class:`TextValueDefWithCondition`)
        Text of the ``text`` mark.
    tooltip : anyOf(:class:`TextFieldDefWithCondition`, :class:`TextValueDefWithCondition`,
    List(:class:`TextFieldDef`))
        The tooltip text to show upon mouse hover.
    x : anyOf(:class:`PositionFieldDef`, :class:`ValueDef`)
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"``.
    x2 : anyOf(:class:`FieldDef`, :class:`ValueDef`)
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.
    y : anyOf(:class:`PositionFieldDef`, :class:`ValueDef`)
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"``.
    y2 : anyOf(:class:`FieldDef`, :class:`ValueDef`)
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.
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


class EncodingSortField(VegaLiteSchema):
    """EncodingSortField schema wrapper

    Mapping(required=[op])
    A sort definition for sorting a discrete scale in an encoding field definition.

    Attributes
    ----------

    op : :class:`AggregateOp`
        An `aggregate operation
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__ to perform on the
        field prior to sorting (e.g., ``"count"``, ``"mean"`` and ``"median"`` ).
        This property is required in cases where the sort field and the data reference field
        do not match.
        The input data objects will be aggregated, grouped by the encoded data field.

        For a full list of operations, please see the documentation for `aggregate
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__.
    field : anyOf(string, :class:`RepeatRef`)
        The data `field <https://vega.github.io/vega-lite/docs/field.html>`__ to sort by.

        **Default value:** If unspecified, defaults to the field specified in the outer data
        reference.
    order : :class:`SortOrder`
        The sort order. One of ``"ascending"`` (default), ``"descending"``, or ``null`` (no
        not sort).
    """
    _schema = {'$ref': '#/definitions/EncodingSortField'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, order=Undefined, **kwds):
        super(EncodingSortField, self).__init__(op=op, field=field, order=order, **kwds)


class EncodingWithFacet(VegaLiteSchema):
    """EncodingWithFacet schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        Color of the marks – either fill or stroke color based on  the ``filled`` property
        of mark definition.
        By default, ``color`` represents fill color for ``"area"``, ``"bar"``, ``"tick"``,
        ``"text"``, ``"trail"``, ``"circle"``, and ``"square"`` / stroke color for
        ``"line"`` and ``"point"``.

        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:*
        1) For fine-grained control over both fill and stroke colors of the marks, please
        use the ``fill`` and ``stroke`` channels.  If either ``fill`` or ``stroke`` channel
        is specified, ``color`` channel will be ignored.
        2) See the scale documentation for more information about customizing `color scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__.
    column : :class:`FacetFieldDef`
        Horizontal facets for trellis plots.
    detail : anyOf(:class:`FieldDef`, List(:class:`FieldDef`))
        Additional levels of detail for grouping data in aggregate views and
        in line, trail, and area marks without mapping data to a specific visual channel.
    fill : anyOf(:class:`MarkPropFieldDefWithCondition`, :class:`MarkPropValueDefWithCondition`)
        Fill color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* When using ``fill`` channel, ``color`` channel will be ignored. To customize
        both fill and stroke, please use ``fill`` and ``stroke`` channels (not ``fill`` and
        ``color`` ).
    href : anyOf(:class:`FieldDefWithCondition`, :class:`ValueDefWithCondition`)
        A URL to load upon mouse click.
    key : :class:`FieldDef`
        A data field to use as a unique key for data binding. When a visualization’s data is
        updated, the key value will be used to match data elements to existing mark
        instances. Use a key channel to enable object constancy for transitions over dynamic
        data.
    latitude : :class:`FieldDef`
        Latitude position of geographically projected marks.
    latitude2 : :class:`FieldDef`
        Latitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    longitude : :class:`FieldDef`
        Longitude position of geographically projected marks.
    longitude2 : :class:`FieldDef`
        Longitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    opacity : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        Opacity of the marks – either can be a value or a range.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``opacity`` property.
    order : anyOf(:class:`OrderFieldDef`, List(:class:`OrderFieldDef`), :class:`ValueDef`)
        Order of the marks.


        * For stacked marks, this ``order`` channel encodes `stack order
          <https://vega.github.io/vega-lite/docs/stack.html#order>`__.
        * For line and trail marks, this ``order`` channel encodes order of data points in
          the lines. This can be useful for creating `a connected scatterplot
          <https://vega.github.io/vega-lite/examples/connected_scatterplot.html>`__.
          Setting ``order`` to ``{"value": null}`` makes the line marks use the original
          order in the data sources.
        * Otherwise, this ``order`` channel encodes layer order of the marks.

        **Note** : In aggregate plots, ``order`` field should be ``aggregate`` d to avoid
        creating additional aggregation grouping.
    row : :class:`FacetFieldDef`
        Vertical facets for trellis plots.
    shape : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        For ``point`` marks the supported values are
        ``"circle"`` (default), ``"square"``, ``"cross"``, ``"diamond"``, ``"triangle-up"``,
        or ``"triangle-down"``, or else a custom SVG path string.
        For ``geoshape`` marks it should be a field definition of the geojson data

        **Default value:** If undefined, the default shape depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#point-config>`__ 's ``shape``
        property.
    size : anyOf(:class:`MarkPropFieldDefWithCondition`, :class:`MarkPropValueDefWithCondition`)
        Size of the mark.


        * For ``"point"``, ``"square"`` and ``"circle"``, – the symbol size, or pixel area
          of the mark.
        * For ``"bar"`` and ``"tick"`` – the bar and tick's size.
        * For ``"text"`` – the text's font size.
        * Size is unsupported for ``"line"``, ``"area"``, and ``"rect"``. (Use ``"trail"``
          instead of line with varying size)
    stroke : anyOf(:class:`MarkPropFieldDefWithCondition`,
    :class:`MarkPropValueDefWithCondition`)
        Stroke color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* When using ``stroke`` channel, ``color`` channel will be ignored. To
        customize both stroke and fill, please use ``stroke`` and ``fill`` channels (not
        ``stroke`` and ``color`` ).
    text : anyOf(:class:`TextFieldDefWithCondition`, :class:`TextValueDefWithCondition`)
        Text of the ``text`` mark.
    tooltip : anyOf(:class:`TextFieldDefWithCondition`, :class:`TextValueDefWithCondition`,
    List(:class:`TextFieldDef`))
        The tooltip text to show upon mouse hover.
    x : anyOf(:class:`PositionFieldDef`, :class:`ValueDef`)
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"``.
    x2 : anyOf(:class:`FieldDef`, :class:`ValueDef`)
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.
    y : anyOf(:class:`PositionFieldDef`, :class:`ValueDef`)
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"``.
    y2 : anyOf(:class:`FieldDef`, :class:`ValueDef`)
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.
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

    layer : List(anyOf(:class:`LayerSpec`, :class:`CompositeUnitSpec`))
        Layer or single view specifications to be layered.

        **Note** : Specifications inside ``layer`` cannot use ``row`` and ``column``
        channels as layering facet specifications is not allowed.
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A shared key-value mapping between encoding channels and definition of fields in the
        underlying layers.
    height : float
        The height of a visualization.

        **Default value:**


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its y-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the height will
          be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For y-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the height is `determined by the range step, paddings, and the
          cardinality of the field mapped to y-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__. Otherwise, if the
          ``rangeStep`` is ``null``, the height will be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``y`` channel, the ``height`` will be the value of
          ``rangeStep``.

        **Note** : For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of the geographic projection shared by underlying
        layers.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for layers.
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.

        **Default value:** This will be determined by the following rules:


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its x-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the width will
          be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For x-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the width is `determined by the range step, paddings, and the
          cardinality of the field mapped to x-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__.   Otherwise, if the
          ``rangeStep`` is ``null``, the width will be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``x`` channel, the ``width`` will be the value of
          `config.scale.textXRangeStep
          <https://vega.github.io/vega-lite/docs/size.html#default-width-and-height>`__ for
          ``text`` mark and the value of ``rangeStep`` for other marks.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
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

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    header : :class:`Header`
        An object defining properties of a facet's header.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FacetFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(FacetFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                            header=header, sort=sort, timeUnit=timeUnit, title=title,
                                            **kwds)


class FacetMapping(VegaLiteSchema):
    """FacetMapping schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : :class:`FacetFieldDef`
        Horizontal facets for trellis plots.
    row : :class:`FacetFieldDef`
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

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(FieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                       timeUnit=timeUnit, title=title, **kwds)


class FieldDefWithCondition(VegaLiteSchema):
    """FieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(FieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                    condition=condition, field=field, timeUnit=timeUnit,
                                                    title=title, **kwds)


class MarkPropFieldDefWithCondition(VegaLiteSchema):
    """MarkPropFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/MarkPropFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(MarkPropFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                            condition=condition, field=field,
                                                            legend=legend, scale=scale, sort=sort,
                                                            timeUnit=timeUnit, title=title, **kwds)


class TextFieldDefWithCondition(VegaLiteSchema):
    """TextFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The `formatting pattern <https://vega.github.io/vega-lite/docs/format.html>`__ for a
        text field. If not defined, this will be determined automatically.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/TextFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(TextFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                        condition=condition, field=field, format=format,
                                                        timeUnit=timeUnit, title=title, **kwds)


class FieldEqualPredicate(VegaLiteSchema):
    """FieldEqualPredicate schema wrapper

    Mapping(required=[equal, field])

    Attributes
    ----------

    equal : anyOf(string, float, boolean, :class:`DateTime`)
        The value that the field should be equal to.
    field : string
        Field to be filtered.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldEqualPredicate'}
    _rootschema = Root._schema

    def __init__(self, equal=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldEqualPredicate, self).__init__(equal=equal, field=field, timeUnit=timeUnit, **kwds)


class FieldGTEPredicate(VegaLiteSchema):
    """FieldGTEPredicate schema wrapper

    Mapping(required=[field, gte])

    Attributes
    ----------

    field : string
        Field to be filtered.
    gte : anyOf(string, float, :class:`DateTime`)
        The value that the field should be greater than or equals to.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldGTEPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, gte=Undefined, timeUnit=Undefined, **kwds):
        super(FieldGTEPredicate, self).__init__(field=field, gte=gte, timeUnit=timeUnit, **kwds)


class FieldGTPredicate(VegaLiteSchema):
    """FieldGTPredicate schema wrapper

    Mapping(required=[field, gt])

    Attributes
    ----------

    field : string
        Field to be filtered.
    gt : anyOf(string, float, :class:`DateTime`)
        The value that the field should be greater than.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldGTPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, gt=Undefined, timeUnit=Undefined, **kwds):
        super(FieldGTPredicate, self).__init__(field=field, gt=gt, timeUnit=timeUnit, **kwds)


class FieldLTEPredicate(VegaLiteSchema):
    """FieldLTEPredicate schema wrapper

    Mapping(required=[field, lte])

    Attributes
    ----------

    field : string
        Field to be filtered.
    lte : anyOf(string, float, :class:`DateTime`)
        The value that the field should be less than or equals to.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldLTEPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, lte=Undefined, timeUnit=Undefined, **kwds):
        super(FieldLTEPredicate, self).__init__(field=field, lte=lte, timeUnit=timeUnit, **kwds)


class FieldLTPredicate(VegaLiteSchema):
    """FieldLTPredicate schema wrapper

    Mapping(required=[field, lt])

    Attributes
    ----------

    field : string
        Field to be filtered.
    lt : anyOf(string, float, :class:`DateTime`)
        The value that the field should be less than.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldLTPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, lt=Undefined, timeUnit=Undefined, **kwds):
        super(FieldLTPredicate, self).__init__(field=field, lt=lt, timeUnit=timeUnit, **kwds)


class FieldOneOfPredicate(VegaLiteSchema):
    """FieldOneOfPredicate schema wrapper

    Mapping(required=[field, oneOf])

    Attributes
    ----------

    field : string
        Field to be filtered.
    oneOf : anyOf(List(string), List(float), List(boolean), List(:class:`DateTime`))
        A set of values that the ``field`` 's value should be a member of,
        for a data item included in the filtered data.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
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
        Field to be filtered.
    range : List(anyOf(float, :class:`DateTime`, None))
        An array of inclusive minimum and maximum values
        for a field value of a data item to be included in the filtered data.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
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

    filter : :class:`LogicalOperandPredicate`
        The ``filter`` property must be one of the predicate definitions:

        1) an `expression <https://vega.github.io/vega-lite/docs/types.html#expression>`__
        string,
        where ``datum`` can be used to refer to the current data object

        2) one of the field predicates: `equal
        <https://vega.github.io/vega-lite/docs/filter.html#equal-predicate>`__,
        `lt <https://vega.github.io/vega-lite/docs/filter.html#lt-predicate>`__,
        `lte <https://vega.github.io/vega-lite/docs/filter.html#lte-predicate>`__,
        `gt <https://vega.github.io/vega-lite/docs/filter.html#gt-predicate>`__,
        `gte <https://vega.github.io/vega-lite/docs/filter.html#gte-predicate>`__,
        `range <https://vega.github.io/vega-lite/docs/filter.html#range-predicate>`__,
        or `oneOf <https://vega.github.io/vega-lite/docs/filter.html#one-of-predicate>`__.

        3) a `selection predicate
        <https://vega.github.io/vega-lite/docs/filter.html#selection-predicate>`__

        4) a logical operand that combines (1), (2), or (3).
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

    anyOf(:class:`FontWeightString`, :class:`FontWeightNumber`)
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

    facet : :class:`FacetMapping`
        An object that describes mappings between ``row`` and ``column`` channels and their
        field definitions.
    spec : anyOf(:class:`LayerSpec`, :class:`CompositeUnitSpec`)
        A specification of the view that gets faceted.
    align : anyOf(:class:`VgLayoutAlign`, :class:`RowColVgLayoutAlign`)
        The alignment to apply to grid rows and columns.
        The supported string values are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        Alternatively, an object value of the form ``{"row": string, "column": string}`` can
        be used to supply different alignments for rows and columns.

        **Default value:** ``"all"``.
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : anyOf(boolean, :class:`RowColboolean`)
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        An object value of the form ``{"row": boolean, "column": boolean}`` can be used to
        supply different centering values for rows and columns.

        **Default value:** ``false``
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for facets.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/FacetSpec'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, spec=Undefined, align=Undefined, bounds=Undefined,
                 center=Undefined, data=Undefined, description=Undefined, name=Undefined,
                 resolve=Undefined, spacing=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, align=align, bounds=bounds,
                                        center=center, data=data, description=description, name=name,
                                        resolve=resolve, spacing=spacing, title=title,
                                        transform=transform, **kwds)


class HConcatSpec(VegaLiteSchema):
    """HConcatSpec schema wrapper

    Mapping(required=[hconcat])

    Attributes
    ----------

    hconcat : List(:class:`Spec`)
        A list of views that should be concatenated and put into a row.
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : boolean
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        **Default value:** ``false``
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for horizontally concatenated charts.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/HConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, bounds=Undefined, center=Undefined, data=Undefined,
                 description=Undefined, name=Undefined, resolve=Undefined, spacing=Undefined,
                 title=Undefined, transform=Undefined, **kwds):
        super(HConcatSpec, self).__init__(hconcat=hconcat, bounds=bounds, center=center, data=data,
                                          description=description, name=name, resolve=resolve,
                                          spacing=spacing, title=title, transform=transform, **kwds)


class RepeatSpec(VegaLiteSchema):
    """RepeatSpec schema wrapper

    Mapping(required=[repeat, spec])

    Attributes
    ----------

    repeat : :class:`Repeat`
        An object that describes what fields should be repeated into views that are laid out
        as a ``row`` or ``column``.
    spec : :class:`Spec`

    align : anyOf(:class:`VgLayoutAlign`, :class:`RowColVgLayoutAlign`)
        The alignment to apply to grid rows and columns.
        The supported string values are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        Alternatively, an object value of the form ``{"row": string, "column": string}`` can
        be used to supply different alignments for rows and columns.

        **Default value:** ``"all"``.
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : anyOf(boolean, :class:`RowColboolean`)
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        An object value of the form ``{"row": boolean, "column": boolean}`` can be used to
        supply different centering values for rows and columns.

        **Default value:** ``false``
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale and legend resolutions for repeated charts.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/RepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, align=Undefined, bounds=Undefined,
                 center=Undefined, data=Undefined, description=Undefined, name=Undefined,
                 resolve=Undefined, spacing=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(RepeatSpec, self).__init__(repeat=repeat, spec=spec, align=align, bounds=bounds,
                                         center=center, data=data, description=description, name=name,
                                         resolve=resolve, spacing=spacing, title=title,
                                         transform=transform, **kwds)


class Spec(VegaLiteSchema):
    """Spec schema wrapper

    anyOf(:class:`CompositeUnitSpec`, :class:`LayerSpec`, :class:`FacetSpec`,
    :class:`RepeatSpec`, :class:`VConcatSpec`, :class:`HConcatSpec`)
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

    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.

        **Default value:**


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its y-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the height will
          be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For y-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the height is `determined by the range step, paddings, and the
          cardinality of the field mapped to y-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__. Otherwise, if the
          ``rangeStep`` is ``null``, the height will be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``y`` channel, the ``height`` will be the value of
          ``rangeStep``.

        **Note** : For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.

        **Default value:** This will be determined by the following rules:


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its x-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the width will
          be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For x-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the width is `determined by the range step, paddings, and the
          cardinality of the field mapped to x-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__.   Otherwise, if the
          ``rangeStep`` is ``null``, the width will be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``x`` channel, the ``width`` will be the value of
          `config.scale.textXRangeStep
          <https://vega.github.io/vega-lite/docs/size.html#default-width-and-height>`__ for
          ``text`` mark and the value of ``rangeStep`` for other marks.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
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

    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`EncodingWithFacet`
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.

        **Default value:**


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its y-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the height will
          be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For y-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the height is `determined by the range step, paddings, and the
          cardinality of the field mapped to y-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__. Otherwise, if the
          ``rangeStep`` is ``null``, the height will be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``y`` channel, the ``height`` will be the value of
          ``rangeStep``.

        **Note** : For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.

        **Default value:** This will be determined by the following rules:


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its x-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the width will
          be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For x-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the width is `determined by the range step, paddings, and the
          cardinality of the field mapped to x-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__.   Otherwise, if the
          ``rangeStep`` is ``null``, the width will be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``x`` channel, the ``width`` will be the value of
          `config.scale.textXRangeStep
          <https://vega.github.io/vega-lite/docs/size.html#default-width-and-height>`__ for
          ``text`` mark and the value of ``rangeStep`` for other marks.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
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

    vconcat : List(:class:`Spec`)
        A list of views that should be concatenated and put into a column.
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : boolean
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        **Default value:** ``false``
    data : :class:`Data`
        An object describing the data source
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for vertically concatenated charts.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/VConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, bounds=Undefined, center=Undefined, data=Undefined,
                 description=Undefined, name=Undefined, resolve=Undefined, spacing=Undefined,
                 title=Undefined, transform=Undefined, **kwds):
        super(VConcatSpec, self).__init__(vconcat=vconcat, bounds=bounds, center=center, data=data,
                                          description=description, name=name, resolve=resolve,
                                          spacing=spacing, title=title, transform=transform, **kwds)


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
        The formatting pattern for labels. This is D3's `number format pattern
        <https://github.com/d3/d3-format#locale_format>`__ for quantitative fields and D3's
        `time format pattern <https://github.com/d3/d3-time-format#locale_format>`__ for
        time field.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more information.

        **Default value:**  derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for
        quantitative fields and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for temporal
        fields.
    labelAngle : float
        The rotation angle of the header labels.

        **Default value:** ``0``.
    labelColor : string
        The color of the header label, can be in hex color code or regular color name.
    labelFont : string
        The font of the header label.
    labelFontSize : float
        The font size of the header label, in pixels.
    labelLimit : float
        The maximum length of the header label in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    titleAnchor : string
        The anchor position for placing the title. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with an orientation of top these anchor positions map to a
        left-, center-, or right-aligned title.

        **Default value:** ``"middle"`` for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.
        ``"start"`` for other composite views.

        **Note:** `For now <https://github.com/vega/vega-lite/issues/2875>`__, ``anchor`` is
        only customizable only for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.  For other composite
        views, ``anchor`` is always ``"start"``.
    titleAngle : float
        The rotation angle of the header title.

        **Default value:** ``0``.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for the header title. One of ``"top"``, ``"bottom"``,
        ``"middle"``.

        **Default value:** ``"middle"``
    titleColor : string
        Color of the header title, can be in hex color code or regular color name.
    titleFont : string
        Font of the header title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the header title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the header title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        The maximum length of the header title in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    """
    _schema = {'$ref': '#/definitions/Header'}
    _rootschema = Root._schema

    def __init__(self, format=Undefined, labelAngle=Undefined, labelColor=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, title=Undefined,
                 titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined,
                 titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined,
                 titleFontWeight=Undefined, titleLimit=Undefined, **kwds):
        super(Header, self).__init__(format=format, labelAngle=labelAngle, labelColor=labelColor,
                                     labelFont=labelFont, labelFontSize=labelFontSize,
                                     labelLimit=labelLimit, title=title, titleAnchor=titleAnchor,
                                     titleAngle=titleAngle, titleBaseline=titleBaseline,
                                     titleColor=titleColor, titleFont=titleFont,
                                     titleFontSize=titleFontSize, titleFontWeight=titleFontWeight,
                                     titleLimit=titleLimit, **kwds)


class HeaderConfig(VegaLiteSchema):
    """HeaderConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    labelAngle : float
        The rotation angle of the header labels.

        **Default value:** ``0``.
    labelColor : string
        The color of the header label, can be in hex color code or regular color name.
    labelFont : string
        The font of the header label.
    labelFontSize : float
        The font size of the header label, in pixels.
    labelLimit : float
        The maximum length of the header label in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    titleAnchor : string
        The anchor position for placing the title. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with an orientation of top these anchor positions map to a
        left-, center-, or right-aligned title.

        **Default value:** ``"middle"`` for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.
        ``"start"`` for other composite views.

        **Note:** `For now <https://github.com/vega/vega-lite/issues/2875>`__, ``anchor`` is
        only customizable only for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.  For other composite
        views, ``anchor`` is always ``"start"``.
    titleAngle : float
        The rotation angle of the header title.

        **Default value:** ``0``.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for the header title. One of ``"top"``, ``"bottom"``,
        ``"middle"``.

        **Default value:** ``"middle"``
    titleColor : string
        Color of the header title, can be in hex color code or regular color name.
    titleFont : string
        Font of the header title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the header title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the header title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        The maximum length of the header title in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    """
    _schema = {'$ref': '#/definitions/HeaderConfig'}
    _rootschema = Root._schema

    def __init__(self, labelAngle=Undefined, labelColor=Undefined, labelFont=Undefined,
                 labelFontSize=Undefined, labelLimit=Undefined, titleAnchor=Undefined,
                 titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined,
                 titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined,
                 titleLimit=Undefined, **kwds):
        super(HeaderConfig, self).__init__(labelAngle=labelAngle, labelColor=labelColor,
                                           labelFont=labelFont, labelFontSize=labelFontSize,
                                           labelLimit=labelLimit, titleAnchor=titleAnchor,
                                           titleAngle=titleAngle, titleBaseline=titleBaseline,
                                           titleColor=titleColor, titleFont=titleFont,
                                           titleFontSize=titleFontSize, titleFontWeight=titleFontWeight,
                                           titleLimit=titleLimit, **kwds)


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

    values : :class:`InlineDataset`
        The full data set, included inline. This can be an array of objects or primitive
        values, an object, or a string.
        Arrays of primitive values are ingested as objects with a ``data`` property. Strings
        are parsed according to the specified format type.
    format : :class:`DataFormat`
        An object that specifies the format for parsing the data.
    name : string
        Provide a placeholder name and bind data at runtime.
    """
    _schema = {'$ref': '#/definitions/InlineData'}
    _rootschema = Root._schema

    def __init__(self, values=Undefined, format=Undefined, name=Undefined, **kwds):
        super(InlineData, self).__init__(values=values, format=format, name=name, **kwds)


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
        Establishes a two-way binding between the interval selection and the scales
        used within the same view. This allows a user to interactively pan and
        zoom the view.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to
        fall within the selection.
    mark : :class:`BrushConfig`
        An interval selection also adds a rectangle mark to depict the
        extents of the interval. The ``mark`` property can be used to customize the
        appearance of the mark.
    on : :class:`VgEventStream`
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.
    translate : anyOf(string, boolean)
        When truthy, allows a user to interactively move an interval selection
        back-and-forth. Can be ``true``, ``false`` (to disable panning), or a
        `Vega event stream definition <https://vega.github.io/vega/docs/event-streams/>`__
        which must include a start and end event to trigger continuous panning.

        **Default value:** ``true``, which corresponds to
        ``[mousedown, window:mouseup] > window:mousemove!`` which corresponds to
        clicks and dragging within an interval selection to reposition it.
    zoom : anyOf(string, boolean)
        When truthy, allows a user to interactively resize an interval selection.
        Can be ``true``, ``false`` (to disable zooming), or a `Vega event stream
        definition <https://vega.github.io/vega/docs/event-streams/>`__. Currently,
        only ``wheel`` events are supported.

        **Default value:** ``true``, which corresponds to ``wheel!``.
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
        Establishes a two-way binding between the interval selection and the scales
        used within the same view. This allows a user to interactively pan and
        zoom the view.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to
        fall within the selection.
    mark : :class:`BrushConfig`
        An interval selection also adds a rectangle mark to depict the
        extents of the interval. The ``mark`` property can be used to customize the
        appearance of the mark.
    on : :class:`VgEventStream`
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.
    translate : anyOf(string, boolean)
        When truthy, allows a user to interactively move an interval selection
        back-and-forth. Can be ``true``, ``false`` (to disable panning), or a
        `Vega event stream definition <https://vega.github.io/vega/docs/event-streams/>`__
        which must include a start and end event to trigger continuous panning.

        **Default value:** ``true``, which corresponds to
        ``[mousedown, window:mouseup] > window:mousemove!`` which corresponds to
        clicks and dragging within an interval selection to reposition it.
    zoom : anyOf(string, boolean)
        When truthy, allows a user to interactively resize an interval selection.
        Can be ``true``, ``false`` (to disable zooming), or a `Vega event stream
        definition <https://vega.github.io/vega/docs/event-streams/>`__. Currently,
        only ``wheel`` events are supported.

        **Default value:** ``true``, which corresponds to ``wheel!``.
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

    parse : anyOf(enum('auto'), :class:`Parse`, None)
        If set to ``"auto"`` (the default), perform automatic type inference to determine
        the desired data types.
        If set to ``null``, disable type inference based on the spec and only use type
        inference based on the data.
        Alternatively, a parsing directive object can be provided for explicit data types.
        Each property of the object corresponds to a field name, and the value to the
        desired data type (one of ``"number"``, ``"boolean"``, ``"date"``, or null (do not
        parse the field)).
        For example, ``"parse": {"modified_on": "date"}`` parses the ``modified_on`` field
        in each input record a Date value.

        For ``"date"``, we parse data based using Javascript's `Date.parse()
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse>`__.
        For Specific date formats can be provided (e.g., ``{foo: 'date:"%m%d%Y"'}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: 'utc:"%m%d%Y"'}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    property : string
        The JSON property containing the desired data.
        This parameter can be used when the loaded JSON file may have surrounding structure
        or meta-data.
        For example ``"property": "values.features"`` is equivalent to retrieving
        ``json.values.features``
        from the loaded JSON object.
    type : enum('json')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.
        The default format type is determined by the extension of the file URL.
        If no extension is detected, ``"json"`` will be used by default.
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
        The formatting pattern for labels. This is D3's `number format pattern
        <https://github.com/d3/d3-format#locale_format>`__ for quantitative fields and D3's
        `time format pattern <https://github.com/d3/d3-time-format#locale_format>`__ for
        time field.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more information.

        **Default value:**  derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for
        quantitative fields and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for temporal
        fields.
    offset : float
        The offset, in pixels, by which to displace the legend from the edge of the
        enclosing group or data rectangle.

        **Default value:**  ``0``
    orient : :class:`LegendOrient`
        The orientation of the legend, which determines how the legend is positioned within
        the scene. One of "left", "right", "top-left", "top-right", "bottom-left",
        "bottom-right", "none".

        **Default value:** ``"right"``
    padding : float
        The padding, in pixels, between the legend and axis.
    tickCount : float
        The desired number of tick values for quantitative legends.
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : enum('symbol', 'gradient')
        The type of the legend. Use ``"symbol"`` to create a discrete legend and
        ``"gradient"`` for a continuous color gradient.

        **Default value:** ``"gradient"`` for non-binned quantitative fields and temporal
        fields; ``"symbol"`` otherwise.
    values : anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`))
        Explicitly set the visible legend values.
    zindex : float
        A non-positive integer indicating z-index of the legend.
        If zindex is 0, legend should be drawn behind all chart elements.
        To put them in front, use zindex = 1.
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
        The font size of legend label.

        **Default value:** ``10``.
    labelLimit : float
        Maximum allowed pixel width of axis tick labels.
    labelOffset : float
        The offset of the legend label.
    offset : float
        The offset, in pixels, by which to displace the legend from the edge of the
        enclosing group or data rectangle.

        **Default value:**  ``0``
    orient : :class:`LegendOrient`
        The orientation of the legend, which determines how the legend is positioned within
        the scene. One of "left", "right", "top-left", "top-right", "bottom-left",
        "bottom-right", "none".

        **Default value:** ``"right"``
    padding : float
        The padding, in pixels, between the legend and axis.
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.

        **Default value:**  ``false``
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
    titleFontWeight : :class:`FontWeight`
        The font weight of the legend title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
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

    color : :class:`ResolveMode`

    fill : :class:`ResolveMode`

    opacity : :class:`ResolveMode`

    shape : :class:`ResolveMode`

    size : :class:`ResolveMode`

    stroke : :class:`ResolveMode`

    """
    _schema = {'$ref': '#/definitions/LegendResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, fill=Undefined, opacity=Undefined, shape=Undefined,
                 size=Undefined, stroke=Undefined, **kwds):
        super(LegendResolveMap, self).__init__(color=color, fill=fill, opacity=opacity, shape=shape,
                                               size=size, stroke=stroke, **kwds)


class LineConfig(VegaLiteSchema):
    """LineConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    point : anyOf(boolean, :class:`OverlayMarkDef`, enum('transparent'))
        A flag for overlaying points on top of line or area marks, or an object defining the
        properties of the overlayed points.


        If this property is ``"transparent"``, transparent points will be used (for
        enhancing tooltips and selections).

        If this property is an empty object ( ``{}`` ) or ``true``, filled points with
        default properties will be used.

        If this property is ``false``, no points would be automatically added to line or
        area marks.

        **Default value:** ``false``.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/LineConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 cornerRadius=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined,
                 ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined,
                 font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                 href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined,
                 orient=Undefined, point=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, tooltip=Undefined, **kwds):
        super(LineConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color,
                                         cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx,
                                         dy=dy, ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                         filled=filled, font=font, fontSize=fontSize,
                                         fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                                         interpolate=interpolate, limit=limit, opacity=opacity,
                                         orient=orient, point=point, radius=radius, shape=shape,
                                         size=size, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta, tooltip=tooltip,
                                         **kwds)


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

    and : List(:class:`LogicalOperandPredicate`)

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

    and : List(:class:`SelectionOperand`)

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

    not : :class:`LogicalOperandPredicate`

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

    not : :class:`SelectionOperand`

    """
    _schema = {'$ref': '#/definitions/SelectionNot'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionNot, self).__init__(**kwds)


class LogicalOperandPredicate(VegaLiteSchema):
    """LogicalOperandPredicate schema wrapper

    anyOf(:class:`LogicalNotPredicate`, :class:`LogicalAndPredicate`,
    :class:`LogicalOrPredicate`, :class:`Predicate`)
    """
    _schema = {'$ref': '#/definitions/LogicalOperand<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LogicalOperandPredicate, self).__init__(*args, **kwds)


class SelectionOperand(VegaLiteSchema):
    """SelectionOperand schema wrapper

    anyOf(:class:`SelectionNot`, :class:`SelectionAnd`, :class:`SelectionOr`, string)
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

    or : List(:class:`LogicalOperandPredicate`)

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

    or : List(:class:`SelectionOperand`)

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

    data : :class:`Data`
        Secondary data source to lookup in.
    key : string
        Key in data to lookup.
    fields : List(string)
        Fields in foreign data to lookup.
        If not specified, the entire object is queried.
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
        The default value to use if lookup fails.

        **Default value:** ``null``
    as : anyOf(string, List(string))
        The field or fields for storing the computed formula value.
        If ``from.fields`` is specified, the transform will use the same names for ``as``.
        If ``from.fields`` is not specified, ``as`` has to be a string and we put the whole
        object into the data under the specified name.
    from : :class:`LookupData`
        Secondary data reference.
    """
    _schema = {'$ref': '#/definitions/LookupTransform'}
    _rootschema = Root._schema

    def __init__(self, lookup=Undefined, default=Undefined, **kwds):
        super(LookupTransform, self).__init__(lookup=lookup, default=default, **kwds)


class Mark(VegaLiteSchema):
    """Mark schema wrapper

    enum('area', 'bar', 'line', 'trail', 'point', 'text', 'tick', 'rect', 'rule', 'circle',
    'square', 'geoshape')
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

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/MarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 cornerRadius=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined,
                 ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined,
                 font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                 href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined,
                 orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 tooltip=Undefined, **kwds):
        super(MarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color,
                                         cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx,
                                         dy=dy, ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                         filled=filled, font=font, fontSize=fontSize,
                                         fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                                         interpolate=interpolate, limit=limit, opacity=opacity,
                                         orient=orient, radius=radius, shape=shape, size=size,
                                         stroke=stroke, strokeCap=strokeCap, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                         strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, tooltip=tooltip, **kwds)


class MarkDef(VegaLiteSchema):
    """MarkDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`Mark`
        The mark type.
        One of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"geoshape"``, ``"rule"``, and ``"text"``.
    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    binSpacing : float
        Offset between bars for binned field.  Ideal value for this is either 0 (Preferred
        by statisticians) or 1 (Vega-Lite Default, D3 example style).

        **Default value:** ``1``
    clip : boolean
        Whether a mark be clipped to the enclosing group’s width and height.
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    line : anyOf(boolean, :class:`OverlayMarkDef`)
        A flag for overlaying line on top of area marks, or an object defining the
        properties of the overlayed lines.


        If this value is an empty object ( ``{}`` ) or ``true``, lines with default
        properties will be used.

        If this value is ``false``, no lines would be automatically added to area marks.

        **Default value:** ``false``.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    point : anyOf(boolean, :class:`OverlayMarkDef`, enum('transparent'))
        A flag for overlaying points on top of line or area marks, or an object defining the
        properties of the overlayed points.


        If this property is ``"transparent"``, transparent points will be used (for
        enhancing tooltips and selections).

        If this property is an empty object ( ``{}`` ) or ``true``, filled points with
        default properties will be used.

        If this property is ``false``, no points would be automatically added to line or
        area marks.

        **Default value:** ``false``.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    style : anyOf(string, List(string))
        A string or array of strings indicating the name of custom styles to apply to the
        mark. A style is a named collection of mark property defaults defined within the
        `style configuration
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__. If style is an
        array, later styles will override earlier styles. Any `mark properties
        <https://vega.github.io/vega-lite/docs/encoding.html#mark-prop>`__ explicitly
        defined within the ``encoding`` will override a style default.

        **Default value:** The mark's name.  For example, a bar mark will have style
        ``"bar"`` by default.
        **Note:** Any specified style will augment the default style. For example, a bar
        mark with ``"style": "foo"`` will receive from ``config.style.bar`` and
        ``config.style.foo`` (the specified style ``"foo"`` has higher precedence).
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    thickness : float
        Thickness of the tick mark.

        **Default value:**  ``1``
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    x2Offset : float
        Offset for x2-position.
    xOffset : float
        Offset for x-position.
    y2Offset : float
        Offset for y2-position.
    yOffset : float
        Offset for y-position.
    """
    _schema = {'$ref': '#/definitions/MarkDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, align=Undefined, angle=Undefined, baseline=Undefined,
                 binSpacing=Undefined, clip=Undefined, color=Undefined, cornerRadius=Undefined,
                 cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined,
                 fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined,
                 interpolate=Undefined, limit=Undefined, line=Undefined, opacity=Undefined,
                 orient=Undefined, point=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined,
                 text=Undefined, theta=Undefined, thickness=Undefined, tooltip=Undefined,
                 x2Offset=Undefined, xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        super(MarkDef, self).__init__(type=type, align=align, angle=angle, baseline=baseline,
                                      binSpacing=binSpacing, clip=clip, color=color,
                                      cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx, dy=dy,
                                      ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                      filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle,
                                      fontWeight=fontWeight, href=href, interpolate=interpolate,
                                      limit=limit, line=line, opacity=opacity, orient=orient,
                                      point=point, radius=radius, shape=shape, size=size, stroke=stroke,
                                      strokeCap=strokeCap, strokeDash=strokeDash,
                                      strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                      strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                      strokeWidth=strokeWidth, style=style, tension=tension, text=text,
                                      theta=theta, thickness=thickness, tooltip=tooltip,
                                      x2Offset=x2Offset, xOffset=xOffset, y2Offset=y2Offset,
                                      yOffset=yOffset, **kwds)


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
        By default, all data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to
        fall within the selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        See the `nearest transform <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation for more information.
    on : :class:`VgEventStream`
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.
    toggle : anyOf(string, boolean)
        Controls whether data values should be toggled or only ever inserted into
        multi selections. Can be ``true``, ``false`` (for insertion only), or a
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__.

        **Default value:** ``true``, which corresponds to ``event.shiftKey`` (i.e.,
        data values are toggled when a user interacts with the shift-key pressed).

        See the `toggle transform <https://vega.github.io/vega-lite/docs/toggle.html>`__
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
        By default, all data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to
        fall within the selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        See the `nearest transform <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation for more information.
    on : :class:`VgEventStream`
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.
    toggle : anyOf(string, boolean)
        Controls whether data values should be toggled or only ever inserted into
        multi selections. Can be ``true``, ``false`` (for insertion only), or a
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__.

        **Default value:** ``true``, which corresponds to ``event.shiftKey`` (i.e.,
        data values are toggled when a user interacts with the shift-key pressed).

        See the `toggle transform <https://vega.github.io/vega-lite/docs/toggle.html>`__
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

    anyOf(:class:`LocalMultiTimeUnit`, :class:`UtcMultiTimeUnit`)
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
    format : :class:`DataFormat`
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

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    sort : :class:`SortOrder`
        The sort order. One of ``"ascending"`` (default) or ``"descending"``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/OrderFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(OrderFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                            sort=sort, timeUnit=timeUnit, title=title, **kwds)


class Orient(VegaLiteSchema):
    """Orient schema wrapper

    enum('horizontal', 'vertical')
    """
    _schema = {'$ref': '#/definitions/Orient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Orient, self).__init__(*args)


class OverlayMarkDef(VegaLiteSchema):
    """OverlayMarkDef schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    clip : boolean
        Whether a mark be clipped to the enclosing group’s width and height.
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    style : anyOf(string, List(string))
        A string or array of strings indicating the name of custom styles to apply to the
        mark. A style is a named collection of mark property defaults defined within the
        `style configuration
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__. If style is an
        array, later styles will override earlier styles. Any `mark properties
        <https://vega.github.io/vega-lite/docs/encoding.html#mark-prop>`__ explicitly
        defined within the ``encoding`` will override a style default.

        **Default value:** The mark's name.  For example, a bar mark will have style
        ``"bar"`` by default.
        **Note:** Any specified style will augment the default style. For example, a bar
        mark with ``"style": "foo"`` will receive from ``config.style.bar`` and
        ``config.style.foo`` (the specified style ``"foo"`` has higher precedence).
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    x2Offset : float
        Offset for x2-position.
    xOffset : float
        Offset for x-position.
    y2Offset : float
        Offset for y2-position.
    yOffset : float
        Offset for y-position.
    """
    _schema = {'$ref': '#/definitions/OverlayMarkDef'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined,
                 color=Undefined, cornerRadius=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined,
                 opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined,
                 text=Undefined, theta=Undefined, tooltip=Undefined, x2Offset=Undefined,
                 xOffset=Undefined, y2Offset=Undefined, yOffset=Undefined, **kwds):
        super(OverlayMarkDef, self).__init__(align=align, angle=angle, baseline=baseline, clip=clip,
                                             color=color, cornerRadius=cornerRadius, cursor=cursor,
                                             dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                             fillOpacity=fillOpacity, filled=filled, font=font,
                                             fontSize=fontSize, fontStyle=fontStyle,
                                             fontWeight=fontWeight, href=href, interpolate=interpolate,
                                             limit=limit, opacity=opacity, orient=orient, radius=radius,
                                             shape=shape, size=size, stroke=stroke, strokeCap=strokeCap,
                                             strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                             strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                             strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                             style=style, tension=tension, text=text, theta=theta,
                                             tooltip=tooltip, x2Offset=x2Offset, xOffset=xOffset,
                                             y2Offset=y2Offset, yOffset=yOffset, **kwds)


class Padding(VegaLiteSchema):
    """Padding schema wrapper

    anyOf(float, Mapping(required=[]))
    """
    _schema = {'$ref': '#/definitions/Padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Padding, self).__init__(*args, **kwds)


class Parse(VegaLiteSchema):
    """Parse schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/Parse'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(Parse, self).__init__(**kwds)


class PositionFieldDef(VegaLiteSchema):
    """PositionFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels.
        If ``null``, the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    stack : anyOf(:class:`StackOffset`, None)
        Type of stacking offset if the field should be stacked.
        ``stack`` is only applicable for ``x`` and ``y`` channels with continuous domains.
        For example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * `"zero"`: stacking with baseline offset at zero value of the scale (for creating
          typical stacked [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and
          `area <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__.
          :raw-html:`<br/>`
        - ``"center"`` - stacking with center baseline (for `streamgraph
        <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar`` or ``area`` ;
        (2) the stacked measure channel (x or y) has a linear scale;
        (3) At least one of non-position channels mapped to an unaggregated field that is
        different from x and y.  Otherwise, ``null`` by default.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/PositionFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(PositionFieldDef, self).__init__(type=type, aggregate=aggregate, axis=axis, bin=bin,
                                               field=field, scale=scale, sort=sort, stack=stack,
                                               timeUnit=timeUnit, title=title, **kwds)


class Predicate(VegaLiteSchema):
    """Predicate schema wrapper

    anyOf(:class:`FieldEqualPredicate`, :class:`FieldRangePredicate`,
    :class:`FieldOneOfPredicate`, :class:`FieldLTPredicate`, :class:`FieldGTPredicate`,
    :class:`FieldLTEPredicate`, :class:`FieldGTEPredicate`, :class:`SelectionPredicate`, string)
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
        longitude and latitude in degrees.

        **Default value:** ``[0, 0]``
    clipAngle : float
        Sets the projection’s clipping circle radius to the specified angle in degrees. If
        ``null``, switches to `antimeridian <http://bl.ocks.org/mbostock/3788999>`__ cutting
        rather than small-circle clipping.
    clipExtent : List(List(float))
        Sets the projection’s viewport clip extent to the specified bounds in pixels. The
        extent bounds are specified as an array ``[[x0, y0], [x1, y1]]``, where ``x0`` is
        the left-side of the viewport, ``y0`` is the top, ``x1`` is the right and ``y1`` is
        the bottom. If ``null``, no viewport clipping is performed.
    coefficient : float

    distance : float

    fraction : float

    lobes : float

    parallel : float

    precision : Mapping(required=[length])
        Sets the threshold for the projection’s `adaptive resampling
        <http://bl.ocks.org/mbostock/3795544>`__ to the specified value in pixels. This
        value corresponds to the `Douglas–Peucker distance
        <http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm>`__.
        If precision is not specified, returns the projection’s current resampling precision
        which defaults to ``√0.5 ≅ 0.70710…``.
    radius : float

    ratio : float

    rotate : List(float)
        Sets the projection’s three-axis rotation to the specified angles, which must be a
        two- or three-element array of numbers [ ``lambda``, ``phi``, ``gamma`` ] specifying
        the rotation angles in degrees about each spherical axis. (These correspond to yaw,
        pitch and roll.)

        **Default value:** ``[0, 0, 0]``
    spacing : float

    tilt : float

    type : :class:`ProjectionType`
        The cartographic projection to use. This value is case-insensitive, for example
        ``"albers"`` and ``"Albers"`` indicate the same projection type. You can find all
        valid projection types `in the documentation
        <https://vega.github.io/vega-lite/docs/projection.html#projection-types>`__.

        **Default value:** ``mercator``
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
        longitude and latitude in degrees.

        **Default value:** ``[0, 0]``
    clipAngle : float
        Sets the projection’s clipping circle radius to the specified angle in degrees. If
        ``null``, switches to `antimeridian <http://bl.ocks.org/mbostock/3788999>`__ cutting
        rather than small-circle clipping.
    clipExtent : List(List(float))
        Sets the projection’s viewport clip extent to the specified bounds in pixels. The
        extent bounds are specified as an array ``[[x0, y0], [x1, y1]]``, where ``x0`` is
        the left-side of the viewport, ``y0`` is the top, ``x1`` is the right and ``y1`` is
        the bottom. If ``null``, no viewport clipping is performed.
    coefficient : float

    distance : float

    fraction : float

    lobes : float

    parallel : float

    precision : Mapping(required=[length])
        Sets the threshold for the projection’s `adaptive resampling
        <http://bl.ocks.org/mbostock/3795544>`__ to the specified value in pixels. This
        value corresponds to the `Douglas–Peucker distance
        <http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm>`__.
        If precision is not specified, returns the projection’s current resampling precision
        which defaults to ``√0.5 ≅ 0.70710…``.
    radius : float

    ratio : float

    rotate : List(float)
        Sets the projection’s three-axis rotation to the specified angles, which must be a
        two- or three-element array of numbers [ ``lambda``, ``phi``, ``gamma`` ] specifying
        the rotation angles in degrees about each spherical axis. (These correspond to yaw,
        pitch and roll.)

        **Default value:** ``[0, 0, 0]``
    spacing : float

    tilt : float

    type : :class:`ProjectionType`
        The cartographic projection to use. This value is case-insensitive, for example
        ``"albers"`` and ``"Albers"`` indicate the same projection type. You can find all
        valid projection types `in the documentation
        <https://vega.github.io/vega-lite/docs/projection.html#projection-types>`__.

        **Default value:** ``mercator``
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

    category : anyOf(List(string), :class:`VgScheme`)
        Default range for *nominal* (categorical) fields.
    diverging : anyOf(List(string), :class:`VgScheme`)
        Default range for diverging *quantitative* fields.
    heatmap : anyOf(List(string), :class:`VgScheme`)
        Default range for *quantitative* heatmaps.
    ordinal : anyOf(List(string), :class:`VgScheme`)
        Default range for *ordinal* fields.
    ramp : anyOf(List(string), :class:`VgScheme`)
        Default range for *quantitative* and *temporal* fields.
    symbol : List(string)
        Default range palette for the ``shape`` channel.
    """
    _schema = {'$ref': '#/definitions/RangeConfig'}
    _rootschema = Root._schema

    def __init__(self, category=Undefined, diverging=Undefined, heatmap=Undefined, ordinal=Undefined,
                 ramp=Undefined, symbol=Undefined, **kwds):
        super(RangeConfig, self).__init__(category=category, diverging=diverging, heatmap=heatmap,
                                          ordinal=ordinal, ramp=ramp, symbol=symbol, **kwds)


class RangeConfigValue(VegaLiteSchema):
    """RangeConfigValue schema wrapper

    anyOf(List(anyOf(float, string)), :class:`VgScheme`, Mapping(required=[step]))
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
    mapping from ``scale``, ``axis``, and ``legend`` to a mapping from channels to resolutions.

    Attributes
    ----------

    axis : :class:`AxisResolveMap`

    legend : :class:`LegendResolveMap`

    scale : :class:`ScaleResolveMap`

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


class RowColVgLayoutAlign(VegaLiteSchema):
    """RowColVgLayoutAlign schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : :class:`VgLayoutAlign`

    row : :class:`VgLayoutAlign`

    """
    _schema = {'$ref': '#/definitions/RowCol<VgLayoutAlign>'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(RowColVgLayoutAlign, self).__init__(column=column, row=row, **kwds)


class RowColboolean(VegaLiteSchema):
    """RowColboolean schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : boolean

    row : boolean

    """
    _schema = {'$ref': '#/definitions/RowCol<boolean>'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(RowColboolean, self).__init__(column=column, row=row, **kwds)


class RowColnumber(VegaLiteSchema):
    """RowColnumber schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : float

    row : float

    """
    _schema = {'$ref': '#/definitions/RowCol<number>'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(RowColnumber, self).__init__(column=column, row=row, **kwds)


class Scale(VegaLiteSchema):
    """Scale schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    base : float
        The logarithm base of the ``log`` scale (default ``10`` ).
    clamp : boolean
        If ``true``, values that exceed the data domain are clamped to either the minimum or
        maximum range value

        **Default value:** derived from the `scale config
        <https://vega.github.io/vega-lite/docs/config.html#scale-config>`__ 's ``clamp`` (
        ``true`` by default).
    domain : anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`),
    enum('unaggregated'), :class:`SelectionDomain`)
        Customized domain values.

        For *quantitative* fields, ``domain`` can take the form of a two-element array with
        minimum and maximum values.  `Piecewise scales
        <https://vega.github.io/vega-lite/docs/scale.html#piecewise>`__ can be created by
        providing a ``domain`` with more than two entries.
        If the input field is aggregated, ``domain`` can also be a string value
        ``"unaggregated"``, indicating that the domain should include the raw data values
        prior to the aggregation.

        For *temporal* fields, ``domain`` can be a two-element array minimum and maximum
        values, in the form of either timestamps or the `DateTime definition objects
        <https://vega.github.io/vega-lite/docs/types.html#datetime>`__.

        For *ordinal* and *nominal* fields, ``domain`` can be an array that lists valid
        input values.

        The ``selection`` property can be used to `interactively determine
        <https://vega.github.io/vega-lite/docs/selection.html#scale-domains>`__ the scale
        domain.
    exponent : float
        The exponent of the ``pow`` scale.
    interpolate : anyOf(:class:`ScaleInterpolate`, :class:`ScaleInterpolateParams`)
        The interpolation method for range values. By default, a general interpolator for
        numbers, dates, strings and colors (in RGB space) is used. For color ranges, this
        property allows interpolation in alternative color spaces. Legal values include
        ``rgb``, ``hsl``, ``hsl-long``, ``lab``, ``hcl``, ``hcl-long``, ``cubehelix`` and
        ``cubehelix-long`` ('-long' variants use longer paths in polar coordinate spaces).
        If object-valued, this property accepts an object with a string-valued *type*
        property and an optional numeric *gamma* property applicable to rgb and cubehelix
        interpolators. For more, see the `d3-interpolate documentation
        <https://github.com/d3/d3-interpolate>`__.

        **Note:** Sequential scales do not support ``interpolate`` as they have a fixed
        interpolator.  Since Vega-Lite uses sequential scales for quantitative fields by
        default, you have to set the scale ``type`` to other quantitative scale type such as
        ``"linear"`` to customize ``interpolate``.
    nice : anyOf(boolean, float, :class:`NiceTime`, Mapping(required=[interval, step]))
        Extending the domain so that it starts and ends on nice round values. This method
        typically modifies the scale’s domain, and may only extend the bounds to the nearest
        round value. Nicing is useful if the domain is computed from data and may be
        irregular. For example, for a domain of *[0.201479…, 0.996679…]*, a nice domain
        might be *[0.2, 1.0]*.

        For quantitative scales such as linear, ``nice`` can be either a boolean flag or a
        number. If ``nice`` is a number, it will represent a desired tick count. This allows
        greater control over the step size used to extend the bounds, guaranteeing that the
        returned ticks will exactly cover the domain.

        For temporal fields with time and utc scales, the ``nice`` value can be a string
        indicating the desired time interval. Legal values are ``"millisecond"``,
        ``"second"``, ``"minute"``, ``"hour"``, ``"day"``, ``"week"``, ``"month"``, and
        ``"year"``. Alternatively, ``time`` and ``utc`` scales can accept an object-valued
        interval specifier of the form ``{"interval": "month", "step": 3}``, which includes
        a desired number of interval steps. Here, the domain would snap to quarter (Jan,
        Apr, Jul, Oct) boundaries.

        **Default value:** ``true`` for unbinned *quantitative* fields; ``false`` otherwise.
    padding : float
        For * `continuous <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ *
        scales, expands the scale domain to accommodate the specified number of pixels on
        each of the scale range. The scale range must represent pixels for this parameter to
        function as intended. Padding adjustment is performed prior to all other
        adjustments, including the effects of the zero, nice, domainMin, and domainMax
        properties.

        For * `band <https://vega.github.io/vega-lite/docs/scale.html#band>`__ * scales,
        shortcut for setting ``paddingInner`` and ``paddingOuter`` to the same value.

        For * `point <https://vega.github.io/vega-lite/docs/scale.html#point>`__ * scales,
        alias for ``paddingOuter``.

        **Default value:** For *continuous* scales, derived from the `scale config
        <https://vega.github.io/vega-lite/docs/scale.html#config>`__ 's
        ``continuousPadding``.
        For *band and point* scales, see ``paddingInner`` and ``paddingOuter``.
    paddingInner : float
        The inner padding (spacing) within each band step of band scales, as a fraction of
        the step size. This value must lie in the range [0,1].

        For point scale, this property is invalid as point scales do not have internal band
        widths (only step sizes between bands).

        **Default value:** derived from the `scale config
        <https://vega.github.io/vega-lite/docs/scale.html#config>`__ 's
        ``bandPaddingInner``.
    paddingOuter : float
        The outer padding (spacing) at the ends of the range of band and point scales,
        as a fraction of the step size. This value must lie in the range [0,1].

        **Default value:** derived from the `scale config
        <https://vega.github.io/vega-lite/docs/scale.html#config>`__ 's ``bandPaddingOuter``
        for band scales and ``pointPadding`` for point scales.
    range : anyOf(List(float), List(string), string)
        The range of the scale. One of:


        A string indicating a `pre-defined named scale range
        <https://vega.github.io/vega-lite/docs/scale.html#range-config>`__ (e.g., example,
        ``"symbol"``, or ``"diverging"`` ).

        For `continuous scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, two-element array
        indicating  minimum and maximum values, or an array with more than two entries for
        specifying a `piecewise scale
        <https://vega.github.io/vega-lite/docs/scale.html#piecewise>`__.

        For `discrete <https://vega.github.io/vega-lite/docs/scale.html#discrete>`__ and
        `discretizing <https://vega.github.io/vega-lite/docs/scale.html#discretizing>`__
        scales, an array of desired output values.

        **Notes:**

        1) For `sequential <https://vega.github.io/vega-lite/docs/scale.html#sequential>`__,
        `ordinal <https://vega.github.io/vega-lite/docs/scale.html#ordinal>`__, and
        discretizing color scales, you can also specify a color `scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__ instead of ``range``.

        2) Any directly specified ``range`` for ``x`` and ``y`` channels will be ignored.
        Range can be customized via the view's corresponding `size
        <https://vega.github.io/vega-lite/docs/size.html>`__ ( ``width`` and ``height`` ) or
        via `range steps and paddings properties <#range-step>`__ for `band <#band>`__ and
        `point <#point>`__ scales.
    rangeStep : anyOf(float, None)
        The distance between the starts of adjacent bands or points in `band
        <https://vega.github.io/vega-lite/docs/scale.html#band>`__ and `point
        <https://vega.github.io/vega-lite/docs/scale.html#point>`__ scales.

        If ``rangeStep`` is ``null`` or if the view contains the scale's corresponding `size
        <https://vega.github.io/vega-lite/docs/size.html>`__ ( ``width`` for ``x`` scales
        and ``height`` for ``y`` scales), ``rangeStep`` will be automatically determined to
        fit the size of the view.

        **Default value:**  derived the `scale config
        <https://vega.github.io/vega-lite/docs/config.html#scale-config>`__ 's
        ``textXRangeStep`` ( ``90`` by default) for x-scales of ``text`` marks and
        ``rangeStep`` ( ``21`` by default) for x-scales of other marks and y-scales.

        **Warning** : If ``rangeStep`` is ``null`` and the cardinality of the scale's domain
        is higher than ``width`` or ``height``, the rangeStep might become less than one
        pixel and the mark might not appear correctly.
    round : boolean
        If ``true``, rounds numeric output values to integers. This can be helpful for
        snapping to the pixel grid.

        **Default value:** ``false``.
    scheme : anyOf(string, :class:`SchemeParams`)
        A string indicating a color `scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__ name (e.g.,
        ``"category10"`` or ``"viridis"`` ) or a `scheme parameter object
        <https://vega.github.io/vega-lite/docs/scale.html#scheme-params>`__.

        Discrete color schemes may be used with `discrete
        <https://vega.github.io/vega-lite/docs/scale.html#discrete>`__ or `discretizing
        <https://vega.github.io/vega-lite/docs/scale.html#discretizing>`__ scales.
        Continuous color schemes are intended for use with `sequential
        <https://vega.github.io/vega-lite/docs/scales.html#sequential>`__ scales.

        For the full list of supported schemes, please refer to the `Vega Scheme
        <https://vega.github.io/vega/docs/schemes/#reference>`__ reference.
    type : :class:`ScaleType`
        The type of scale.  Vega-Lite supports the following categories of scale types:

        1) `Continuous Scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ -- mapping
        continuous domains to continuous output ranges ( `"linear"
        <https://vega.github.io/vega-lite/docs/scale.html#linear>`__, `"pow"
        <https://vega.github.io/vega-lite/docs/scale.html#pow>`__, `"sqrt"
        <https://vega.github.io/vega-lite/docs/scale.html#sqrt>`__, `"log"
        <https://vega.github.io/vega-lite/docs/scale.html#log>`__, `"time"
        <https://vega.github.io/vega-lite/docs/scale.html#time>`__, `"utc"
        <https://vega.github.io/vega-lite/docs/scale.html#utc>`__, `"sequential"
        <https://vega.github.io/vega-lite/docs/scale.html#sequential>`__ ).

        2) `Discrete Scales <https://vega.github.io/vega-lite/docs/scale.html#discrete>`__
        -- mapping discrete domains to discrete ( `"ordinal"
        <https://vega.github.io/vega-lite/docs/scale.html#ordinal>`__ ) or continuous (
        `"band" <https://vega.github.io/vega-lite/docs/scale.html#band>`__ and `"point"
        <https://vega.github.io/vega-lite/docs/scale.html#point>`__ ) output ranges.

        3) `Discretizing Scales
        <https://vega.github.io/vega-lite/docs/scale.html#discretizing>`__ -- mapping
        continuous domains to discrete output ranges ( `"bin-linear"
        <https://vega.github.io/vega-lite/docs/scale.html#bin-linear>`__ and `"bin-ordinal"
        <https://vega.github.io/vega-lite/docs/scale.html#bin-ordinal>`__ ).

        **Default value:** please see the `scale type table
        <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
    zero : boolean
        If ``true``, ensures that a zero baseline value is included in the scale domain.

        **Default value:** ``true`` for x and y channels if the quantitative field is not
        binned and no custom ``domain`` is provided; ``false`` otherwise.

        **Note:** Log, time, and utc scales do not support ``zero``.
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
        Default inner padding for ``x`` and ``y`` band-ordinal scales.

        **Default value:** ``0.1``
    bandPaddingOuter : float
        Default outer padding for ``x`` and ``y`` band-ordinal scales.
        If not specified, by default, band scale's paddingOuter is paddingInner/2.
    clamp : boolean
        If true, values that exceed the data domain are clamped to either the minimum or
        maximum range value
    continuousPadding : float
        Default padding for continuous scales.

        **Default:** ``5`` for continuous x-scale of a vertical bar and continuous y-scale
        of a horizontal bar.; ``0`` otherwise.
    maxBandSize : float
        The default max value for mapping quantitative fields to bar's size/bandSize.

        If undefined (default), we will use the scale's ``rangeStep`` - 1.
    maxFontSize : float
        The default max value for mapping quantitative fields to text's size/fontSize.

        **Default value:** ``40``
    maxOpacity : float
        Default max opacity for mapping a field to opacity.

        **Default value:** ``0.8``
    maxSize : float
        Default max value for point size scale.
    maxStrokeWidth : float
        Default max strokeWidth for the scale of strokeWidth for rule and line marks and of
        size for trail marks.

        **Default value:** ``4``
    minBandSize : float
        The default min value for mapping quantitative fields to bar and tick's
        size/bandSize scale with zero=false.

        **Default value:** ``2``
    minFontSize : float
        The default min value for mapping quantitative fields to tick's size/fontSize scale
        with zero=false

        **Default value:** ``8``
    minOpacity : float
        Default minimum opacity for mapping a field to opacity.

        **Default value:** ``0.3``
    minSize : float
        Default minimum value for point size scale with zero=false.

        **Default value:** ``9``
    minStrokeWidth : float
        Default minimum strokeWidth for the scale of strokeWidth for rule and line marks and
        of size for trail marks with zero=false.

        **Default value:** ``1``
    pointPadding : float
        Default outer padding for ``x`` and ``y`` point-ordinal scales.

        **Default value:** ``0.5``
    rangeStep : anyOf(float, None)
        Default range step for band and point scales of (1) the ``y`` channel
        and (2) the ``x`` channel when the mark is not ``text``.

        **Default value:** ``21``
    round : boolean
        If true, rounds numeric output values to integers.
        This can be helpful for snapping to the pixel grid.
        (Only available for ``x``, ``y``, and ``size`` scales.)
    textXRangeStep : float
        Default range step for ``x`` band and point scales of text marks.

        **Default value:** ``90``
    useUnaggregatedDomain : boolean
        Use the source data range before aggregation as scale domain instead of aggregated
        data for aggregate axis.

        This is equivalent to setting ``domain`` to ``"unaggregate"`` for aggregated
        *quantitative* fields by default.

        This property only works with aggregate functions that produce values within the raw
        data domain ( ``"mean"``, ``"average"``, ``"median"``, ``"q1"``, ``"q3"``,
        ``"min"``, ``"max"`` ). For other aggregations that produce values outside of the
        raw data domain (e.g. ``"count"``, ``"sum"`` ), this property is ignored.

        **Default value:** ``false``
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

    color : :class:`ResolveMode`

    fill : :class:`ResolveMode`

    opacity : :class:`ResolveMode`

    shape : :class:`ResolveMode`

    size : :class:`ResolveMode`

    stroke : :class:`ResolveMode`

    x : :class:`ResolveMode`

    y : :class:`ResolveMode`

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
        A color scheme name for sequential/ordinal scales (e.g., ``"category10"`` or
        ``"viridis"`` ).

        For the full list of supported schemes, please refer to the `Vega Scheme
        <https://vega.github.io/vega/docs/schemes/#reference>`__ reference.
    extent : List(float)
        For sequential and diverging schemes only, determines the extent of the color range
        to use. For example ``[0.2, 1]`` will rescale the color scheme such that color
        values in the range *[0, 0.2)* are excluded from the scheme.
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

    interval : :class:`IntervalSelectionConfig`
        The default definition for an `interval
        <https://vega.github.io/vega-lite/docs/selection.html#type>`__ selection. All
        properties and transformations
        for an interval selection definition (except ``type`` ) may be specified here.

        For instance, setting ``interval`` to ``{"translate": false}`` disables the ability
        to move
        interval selections by default.
    multi : :class:`MultiSelectionConfig`
        The default definition for a `multi
        <https://vega.github.io/vega-lite/docs/selection.html#type>`__ selection. All
        properties and transformations
        for a multi selection definition (except ``type`` ) may be specified here.

        For instance, setting ``multi`` to ``{"toggle": "event.altKey"}`` adds additional
        values to
        multi selections when clicking with the alt-key pressed by default.
    single : :class:`SingleSelectionConfig`
        The default definition for a `single
        <https://vega.github.io/vega-lite/docs/selection.html#type>`__ selection. All
        properties and transformations
        for a single selection definition (except ``type`` ) may be specified here.

        For instance, setting ``single`` to ``{"on": "dblclick"}`` populates single
        selections on double-click by default.
    """
    _schema = {'$ref': '#/definitions/SelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, interval=Undefined, multi=Undefined, single=Undefined, **kwds):
        super(SelectionConfig, self).__init__(interval=interval, multi=multi, single=single, **kwds)


class SelectionDef(VegaLiteSchema):
    """SelectionDef schema wrapper

    anyOf(:class:`SingleSelection`, :class:`MultiSelection`, :class:`IntervalSelection`)
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

    selection : :class:`SelectionOperand`
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

    bind : anyOf(:class:`VgBinding`, Mapping(required=[]))
        Establish a two-way binding between a single selection and input elements
        (also known as dynamic query widgets). A binding takes the form of
        Vega's `input element binding definition
        <https://vega.github.io/vega/docs/signals/#bind>`__
        or can be a mapping between projected field/encodings and binding definitions.

        See the `bind transform <https://vega.github.io/vega-lite/docs/bind.html>`__
        documentation for more information.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to
        fall within the selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        See the `nearest transform <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation for more information.
    on : :class:`VgEventStream`
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.
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

    bind : anyOf(:class:`VgBinding`, Mapping(required=[]))
        Establish a two-way binding between a single selection and input elements
        (also known as dynamic query widgets). A binding takes the form of
        Vega's `input element binding definition
        <https://vega.github.io/vega/docs/signals/#bind>`__
        or can be a mapping between projected field/encodings and binding definitions.

        See the `bind transform <https://vega.github.io/vega-lite/docs/bind.html>`__
        documentation for more information.
    empty : enum('all', 'none')
        By default, all data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.
    fields : List(string)
        An array of field names whose values must match for a data tuple to
        fall within the selection.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        See the `nearest transform <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation for more information.
    on : :class:`VgEventStream`
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.
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

    anyOf(:class:`LocalSingleTimeUnit`, :class:`UtcSingleTimeUnit`)
    """
    _schema = {'$ref': '#/definitions/SingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SingleTimeUnit, self).__init__(*args, **kwds)


class Sort(VegaLiteSchema):
    """Sort schema wrapper

    anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`), :class:`SortOrder`,
    :class:`EncodingSortField`, None)
    """
    _schema = {'$ref': '#/definitions/Sort'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Sort, self).__init__(*args, **kwds)


class SortField(VegaLiteSchema):
    """SortField schema wrapper

    Mapping(required=[field])
    A sort definition for transform

    Attributes
    ----------

    field : string
        The name of the field to sort.
    order : :class:`VgComparatorOrder`
        Whether to sort the field in ascending or descending order.
    """
    _schema = {'$ref': '#/definitions/SortField'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, order=Undefined, **kwds):
        super(SortField, self).__init__(field=field, order=order, **kwds)


class SortOrder(VegaLiteSchema):
    """SortOrder schema wrapper

    anyOf(:class:`VgComparatorOrder`, None)
    """
    _schema = {'$ref': '#/definitions/SortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SortOrder, self).__init__(*args, **kwds)


class StackOffset(VegaLiteSchema):
    """StackOffset schema wrapper

    enum('zero', 'center', 'normalize')
    """
    _schema = {'$ref': '#/definitions/StackOffset'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)


class StrokeCap(VegaLiteSchema):
    """StrokeCap schema wrapper

    enum('butt', 'round', 'square')
    """
    _schema = {'$ref': '#/definitions/StrokeCap'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StrokeCap, self).__init__(*args)


class StrokeJoin(VegaLiteSchema):
    """StrokeJoin schema wrapper

    enum('miter', 'round', 'bevel')
    """
    _schema = {'$ref': '#/definitions/StrokeJoin'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StrokeJoin, self).__init__(*args)


class StyleConfigIndex(VegaLiteSchema):
    """StyleConfigIndex schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/StyleConfigIndex'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(StyleConfigIndex, self).__init__(**kwds)


class TextBaseline(VegaLiteSchema):
    """TextBaseline schema wrapper

    anyOf(enum('alphabetic'), :class:`Baseline`)
    """
    _schema = {'$ref': '#/definitions/TextBaseline'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TextBaseline, self).__init__(*args, **kwds)


class TextConfig(VegaLiteSchema):
    """TextConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/TextConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined,
                 cornerRadius=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined,
                 ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined,
                 font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                 href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined,
                 orient=Undefined, radius=Undefined, shape=Undefined, shortTimeLabels=Undefined,
                 size=Undefined, stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, tooltip=Undefined, **kwds):
        super(TextConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color,
                                         cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx,
                                         dy=dy, ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                         filled=filled, font=font, fontSize=fontSize,
                                         fontStyle=fontStyle, fontWeight=fontWeight, href=href,
                                         interpolate=interpolate, limit=limit, opacity=opacity,
                                         orient=orient, radius=radius, shape=shape,
                                         shortTimeLabels=shortTimeLabels, size=size, stroke=stroke,
                                         strokeCap=strokeCap, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                         strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, tooltip=tooltip, **kwds)


class TextFieldDef(VegaLiteSchema):
    """TextFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The `formatting pattern <https://vega.github.io/vega-lite/docs/format.html>`__ for a
        text field. If not defined, this will be determined automatically.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/TextFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 format=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(TextFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                           format=format, timeUnit=timeUnit, title=title, **kwds)


class TickConfig(VegaLiteSchema):
    """TickConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    bandSize : float
        The width of the ticks.

        **Default value:**  2/3 of rangeStep.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : string
        Default color.  Note that ``fill`` and ``stroke`` have higher precedence than
        ``color`` and will override ``color``.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``true`` for all marks except ``point`` and ``false`` for
        ``point``.

        **Applicable for:** ``bar``, ``point``, ``circle``, ``square``, and ``area`` marks.

        **Note:** This property cannot be used in a `style config
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    thickness : float
        Thickness of the tick mark.

        **Default value:**  ``1``
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/TickConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, bandSize=Undefined, baseline=Undefined,
                 color=Undefined, cornerRadius=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined,
                 opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, thickness=Undefined, tooltip=Undefined, **kwds):
        super(TickConfig, self).__init__(align=align, angle=angle, bandSize=bandSize, baseline=baseline,
                                         color=color, cornerRadius=cornerRadius, cursor=cursor, dir=dir,
                                         dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         href=href, interpolate=interpolate, limit=limit,
                                         opacity=opacity, orient=orient, radius=radius, shape=shape,
                                         size=size, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta, thickness=thickness,
                                         tooltip=tooltip, **kwds)


class TimeUnit(VegaLiteSchema):
    """TimeUnit schema wrapper

    anyOf(:class:`SingleTimeUnit`, :class:`MultiTimeUnit`)
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
    timeUnit : :class:`TimeUnit`
        The timeUnit.
    as : string
        The output field to write the timeUnit value.
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
    anchor : :class:`Anchor`
        The anchor position for placing the title. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with an orientation of top these anchor positions map to a
        left-, center-, or right-aligned title.

        **Default value:** ``"middle"`` for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.
        ``"start"`` for other composite views.

        **Note:** `For now <https://github.com/vega/vega-lite/issues/2875>`__, ``anchor`` is
        only customizable only for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.  For other composite
        views, ``anchor`` is always ``"start"``.
    offset : float
        The orthogonal offset in pixels by which to displace the title from its position
        along the edge of the chart.
    orient : :class:`TitleOrient`
        The orientation of the title relative to the chart. One of ``"top"`` (the default),
        ``"bottom"``, ``"left"``, or ``"right"``.
    style : anyOf(string, List(string))
        A `mark style property <https://vega.github.io/vega-lite/docs/config.html#style>`__
        to apply to the title text mark.

        **Default value:** ``"group-title"``.
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

    layer : List(anyOf(:class:`LayerSpec`, :class:`CompositeUnitSpec`))
        Layer or single view specifications to be layered.

        **Note** : Specifications inside ``layer`` cannot use ``row`` and ``column``
        channels as layering facet specifications is not allowed.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    config : :class:`Config`
        Vega-Lite configuration object.  This property can only be defined at the top-level
        of a specification.
    data : :class:`Data`
        An object describing the data source
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A shared key-value mapping between encoding channels and definition of fields in the
        underlying layers.
    height : float
        The height of a visualization.

        **Default value:**


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its y-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the height will
          be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For y-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the height is `determined by the range step, paddings, and the
          cardinality of the field mapped to y-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__. Otherwise, if the
          ``rangeStep`` is ``null``, the height will be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``y`` channel, the ``height`` will be the value of
          ``rangeStep``.

        **Note** : For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    projection : :class:`Projection`
        An object defining properties of the geographic projection shared by underlying
        layers.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for layers.
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.

        **Default value:** This will be determined by the following rules:


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its x-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the width will
          be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For x-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the width is `determined by the range step, paddings, and the
          cardinality of the field mapped to x-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__.   Otherwise, if the
          ``rangeStep`` is ``null``, the width will be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``x`` channel, the ``width`` will be the value of
          `config.scale.textXRangeStep
          <https://vega.github.io/vega-lite/docs/size.html#default-width-and-height>`__ for
          ``text`` mark and the value of ``rangeStep`` for other marks.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v2.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
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

    hconcat : List(:class:`Spec`)
        A list of views that should be concatenated and put into a row.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : boolean
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        **Default value:** ``false``
    config : :class:`Config`
        Vega-Lite configuration object.  This property can only be defined at the top-level
        of a specification.
    data : :class:`Data`
        An object describing the data source
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for horizontally concatenated charts.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v2.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelHConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, autosize=Undefined, background=Undefined, bounds=Undefined,
                 center=Undefined, config=Undefined, data=Undefined, datasets=Undefined,
                 description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined,
                 spacing=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelHConcatSpec, self).__init__(hconcat=hconcat, autosize=autosize,
                                                  background=background, bounds=bounds, center=center,
                                                  config=config, data=data, datasets=datasets,
                                                  description=description, name=name, padding=padding,
                                                  resolve=resolve, spacing=spacing, title=title,
                                                  transform=transform, **kwds)


class TopLevelRepeatSpec(VegaLiteSchema):
    """TopLevelRepeatSpec schema wrapper

    Mapping(required=[repeat, spec])

    Attributes
    ----------

    repeat : :class:`Repeat`
        An object that describes what fields should be repeated into views that are laid out
        as a ``row`` or ``column``.
    spec : :class:`Spec`

    align : anyOf(:class:`VgLayoutAlign`, :class:`RowColVgLayoutAlign`)
        The alignment to apply to grid rows and columns.
        The supported string values are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        Alternatively, an object value of the form ``{"row": string, "column": string}`` can
        be used to supply different alignments for rows and columns.

        **Default value:** ``"all"``.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : anyOf(boolean, :class:`RowColboolean`)
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        An object value of the form ``{"row": boolean, "column": boolean}`` can be used to
        supply different centering values for rows and columns.

        **Default value:** ``false``
    config : :class:`Config`
        Vega-Lite configuration object.  This property can only be defined at the top-level
        of a specification.
    data : :class:`Data`
        An object describing the data source
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale and legend resolutions for repeated charts.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v2.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelRepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, align=Undefined, autosize=Undefined,
                 background=Undefined, bounds=Undefined, center=Undefined, config=Undefined,
                 data=Undefined, datasets=Undefined, description=Undefined, name=Undefined,
                 padding=Undefined, resolve=Undefined, spacing=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(TopLevelRepeatSpec, self).__init__(repeat=repeat, spec=spec, align=align,
                                                 autosize=autosize, background=background,
                                                 bounds=bounds, center=center, config=config, data=data,
                                                 datasets=datasets, description=description, name=name,
                                                 padding=padding, resolve=resolve, spacing=spacing,
                                                 title=title, transform=transform, **kwds)


class TopLevelVConcatSpec(VegaLiteSchema):
    """TopLevelVConcatSpec schema wrapper

    Mapping(required=[vconcat])

    Attributes
    ----------

    vconcat : List(:class:`Spec`)
        A list of views that should be concatenated and put into a column.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : boolean
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        **Default value:** ``false``
    config : :class:`Config`
        Vega-Lite configuration object.  This property can only be defined at the top-level
        of a specification.
    data : :class:`Data`
        An object describing the data source
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for vertically concatenated charts.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v2.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelVConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, autosize=Undefined, background=Undefined, bounds=Undefined,
                 center=Undefined, config=Undefined, data=Undefined, datasets=Undefined,
                 description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined,
                 spacing=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelVConcatSpec, self).__init__(vconcat=vconcat, autosize=autosize,
                                                  background=background, bounds=bounds, center=center,
                                                  config=config, data=data, datasets=datasets,
                                                  description=description, name=name, padding=padding,
                                                  resolve=resolve, spacing=spacing, title=title,
                                                  transform=transform, **kwds)


class TopLevelFacetSpec(VegaLiteSchema):
    """TopLevelFacetSpec schema wrapper

    Mapping(required=[data, facet, spec])

    Attributes
    ----------

    data : :class:`Data`
        An object describing the data source
    facet : :class:`FacetMapping`
        An object that describes mappings between ``row`` and ``column`` channels and their
        field definitions.
    spec : anyOf(:class:`LayerSpec`, :class:`CompositeUnitSpec`)
        A specification of the view that gets faceted.
    align : anyOf(:class:`VgLayoutAlign`, :class:`RowColVgLayoutAlign`)
        The alignment to apply to grid rows and columns.
        The supported string values are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        Alternatively, an object value of the form ``{"row": string, "column": string}`` can
        be used to supply different alignments for rows and columns.

        **Default value:** ``"all"``.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : anyOf(boolean, :class:`RowColboolean`)
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        An object value of the form ``{"row": boolean, "column": boolean}`` can be used to
        supply different centering values for rows and columns.

        **Default value:** ``false``
    config : :class:`Config`
        Vega-Lite configuration object.  This property can only be defined at the top-level
        of a specification.
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for facets.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : ``10``
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v2.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelFacetSpec'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, facet=Undefined, spec=Undefined, align=Undefined,
                 autosize=Undefined, background=Undefined, bounds=Undefined, center=Undefined,
                 config=Undefined, datasets=Undefined, description=Undefined, name=Undefined,
                 padding=Undefined, resolve=Undefined, spacing=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(TopLevelFacetSpec, self).__init__(data=data, facet=facet, spec=spec, align=align,
                                                autosize=autosize, background=background, bounds=bounds,
                                                center=center, config=config, datasets=datasets,
                                                description=description, name=name, padding=padding,
                                                resolve=resolve, spacing=spacing, title=title,
                                                transform=transform, **kwds)


class TopLevelFacetedUnitSpec(VegaLiteSchema):
    """TopLevelFacetedUnitSpec schema wrapper

    Mapping(required=[data, mark])

    Attributes
    ----------

    data : :class:`Data`
        An object describing the data source
    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        Sets how the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.
        ``"fit"`` is only supported for single and layered views that don't use
        ``rangeStep``.

        **Default value** : ``pad``
    background : string
        CSS color property to use as the background of visualization.

        **Default value:** none (transparent)
    config : :class:`Config`
        Vega-Lite configuration object.  This property can only be defined at the top-level
        of a specification.
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`EncodingWithFacet`
        A key-value mapping between encoding channels and definition of fields.
    height : float
        The height of a visualization.

        **Default value:**


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its y-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the height will
          be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For y-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the height is `determined by the range step, paddings, and the
          cardinality of the field mapped to y-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__. Otherwise, if the
          ``rangeStep`` is ``null``, the height will be the value of `config.view.height
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``y`` channel, the ``height`` will be the value of
          ``rangeStep``.

        **Note** : For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle.  If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(string, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    width : float
        The width of a visualization.

        **Default value:** This will be determined by the following rules:


        * If a view's `autosize
          <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ type is ``"fit"`` or
          its x-channel has a `continuous scale
          <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__, the width will
          be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * For x-axis with a band or point scale: if `rangeStep
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__ is a numeric value or
          unspecified, the width is `determined by the range step, paddings, and the
          cardinality of the field mapped to x-channel
          <https://vega.github.io/vega-lite/docs/scale.html#band>`__.   Otherwise, if the
          ``rangeStep`` is ``null``, the width will be the value of `config.view.width
          <https://vega.github.io/vega-lite/docs/spec.html#config>`__.
        * If no field is mapped to ``x`` channel, the ``width`` will be the value of
          `config.scale.textXRangeStep
          <https://vega.github.io/vega-lite/docs/size.html#default-width-and-height>`__ for
          ``text`` mark and the value of ``rangeStep`` for other marks.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view.

        **See also:** The documentation for `width and height
        <https://vega.github.io/vega-lite/docs/size.html>`__ contains more examples.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v2.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
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


class TopLevelSpec(VegaLiteSchema):
    """TopLevelSpec schema wrapper

    anyOf(:class:`TopLevelFacetedUnitSpec`, :class:`TopLevelFacetSpec`,
    :class:`TopLevelLayerSpec`, :class:`TopLevelRepeatSpec`, :class:`TopLevelVConcatSpec`,
    :class:`TopLevelHConcatSpec`)
    """
    _schema = {'$ref': '#/definitions/TopLevelSpec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TopLevelSpec, self).__init__(*args, **kwds)


class TopoDataFormat(VegaLiteSchema):
    """TopoDataFormat schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    feature : string
        The name of the TopoJSON object set to convert to a GeoJSON feature collection.
        For example, in a map of the world, there may be an object set named
        ``"countries"``.
        Using the feature property, we can extract this set and generate a GeoJSON feature
        object for each country.
    mesh : string
        The name of the TopoJSON object set to convert to mesh.
        Similar to the ``feature`` option, ``mesh`` extracts a named TopoJSON object set.
        Unlike the ``feature`` option, the corresponding geo data is returned as a single,
        unified mesh instance, not as individual GeoJSON features.
        Extracting a mesh is useful for more efficiently drawing borders or other geographic
        elements that you do not need to associate with specific regions such as individual
        countries, states or counties.
    parse : anyOf(enum('auto'), :class:`Parse`, None)
        If set to ``"auto"`` (the default), perform automatic type inference to determine
        the desired data types.
        If set to ``null``, disable type inference based on the spec and only use type
        inference based on the data.
        Alternatively, a parsing directive object can be provided for explicit data types.
        Each property of the object corresponds to a field name, and the value to the
        desired data type (one of ``"number"``, ``"boolean"``, ``"date"``, or null (do not
        parse the field)).
        For example, ``"parse": {"modified_on": "date"}`` parses the ``modified_on`` field
        in each input record a Date value.

        For ``"date"``, we parse data based using Javascript's `Date.parse()
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse>`__.
        For Specific date formats can be provided (e.g., ``{foo: 'date:"%m%d%Y"'}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: 'utc:"%m%d%Y"'}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    type : enum('topojson')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.
        The default format type is determined by the extension of the file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/TopoDataFormat'}
    _rootschema = Root._schema

    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(TopoDataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, type=type, **kwds)


class Transform(VegaLiteSchema):
    """Transform schema wrapper

    anyOf(:class:`FilterTransform`, :class:`CalculateTransform`, :class:`LookupTransform`,
    :class:`BinTransform`, :class:`TimeUnitTransform`, :class:`AggregateTransform`,
    :class:`WindowTransform`)
    """
    _schema = {'$ref': '#/definitions/Transform'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Transform, self).__init__(*args, **kwds)


class Type(VegaLiteSchema):
    """Type schema wrapper

    anyOf(:class:`BasicType`, :class:`GeoType`)
    Constants and utilities for data type :raw-html:`<br>`
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
        An URL from which to load the data set. Use the ``format.type`` property
        to ensure the loaded data is correctly parsed.
    format : :class:`DataFormat`
        An object that specifies the format for parsing the data.
    name : string
        Provide a placeholder name and bind data at runtime.
    """
    _schema = {'$ref': '#/definitions/UrlData'}
    _rootschema = Root._schema

    def __init__(self, url=Undefined, format=Undefined, name=Undefined, **kwds):
        super(UrlData, self).__init__(url=url, format=format, name=name, **kwds)


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
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDef'}
    _rootschema = Root._schema

    def __init__(self, value=Undefined, **kwds):
        super(ValueDef, self).__init__(value=value, **kwds)


class ValueDefWithCondition(VegaLiteSchema):
    """ValueDefWithCondition schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
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

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
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

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalTextFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
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
        An interpolation fraction indicating where, for ``band`` scales, axis ticks should
        be positioned. A value of ``0`` places ticks at the left edge of their bands. A
        value of ``0.5`` places ticks in the middle of their bands.
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as
        part of the axis.

        **Default value:** ``true``
    domainColor : string
        Color of axis domain line.

        **Default value:**  (none, using Vega default).
    domainWidth : float
        Stroke width of axis domain line

        **Default value:**  (none, using Vega default).
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis

        **Default value:** ``true`` for `continuous scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ that are not
        binned; otherwise, ``false``.
    gridColor : string
        Color of gridlines.
    gridDash : List(float)
        The offset (in pixels) into which to begin drawing with the grid dash array.
    gridOpacity : float
        The stroke opacity of grid (value between [0,1])

        **Default value:** ( ``1`` by default)
    gridWidth : float
        The grid width, in pixels.
    labelAngle : float
        The rotation angle of the axis labels.

        **Default value:** ``-90`` for nominal and ordinal fields; ``0`` otherwise.
    labelBound : anyOf(boolean, float)
        Indicates if labels should be hidden if they exceed the axis range. If ``false``
        (the default) no bounds overlap analysis is performed. If ``true``, labels will be
        hidden if they exceed the axis range by more than 1 pixel. If this property is a
        number, it specifies the pixel tolerance: the maximum amount by which a label
        bounding box may exceed the axis range.

        **Default value:** ``false``.
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
        visually group with corresponding axis ticks.

        **Default value:** ``true`` for axis of a continuous x-scale. Otherwise, ``false``.
    labelFont : string
        The font of the tick label.
    labelFontSize : float
        The font size of the label, in pixels.
    labelLimit : float
        Maximum allowed pixel width of axis tick labels.
    labelOverlap : anyOf(boolean, enum('parity'), enum('greedy'))
        The strategy to use for resolving overlap of axis labels. If ``false`` (the
        default), no overlap reduction is attempted. If set to ``true`` or ``"parity"``, a
        strategy of removing every other label is used (this works well for standard linear
        axes). If set to ``"greedy"``, a linear scan of the labels is performed, removing
        any labels that overlaps with the last visible label (this often works better for
        log-scaled axes).

        **Default value:** ``true`` for non-nominal fields with non-log scales; ``"greedy"``
        for log scales; otherwise ``false``.
    labelPadding : float
        The padding, in pixels, between axis and text labels.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.

        **Default value:**  ``true``.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines
        a maximum offset value for axis titles.

        **Default value:** ``undefined``.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines
        a minimum offset value for axis titles.

        **Default value:** ``30`` for y-axis; ``undefined`` for x-axis.
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
        Font of the title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
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

    anyOf(:class:`VgCheckboxBinding`, :class:`VgRadioBinding`, :class:`VgSelectBinding`,
    :class:`VgRangeBinding`, :class:`VgGenericBinding`)
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


class VgComparatorOrder(VegaLiteSchema):
    """VgComparatorOrder schema wrapper

    enum('ascending', 'descending')
    """
    _schema = {'$ref': '#/definitions/VgComparatorOrder'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VgComparatorOrder, self).__init__(*args)


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


class VgLayoutAlign(VegaLiteSchema):
    """VgLayoutAlign schema wrapper

    enum('none', 'each', 'all')
    """
    _schema = {'$ref': '#/definitions/VgLayoutAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VgLayoutAlign, self).__init__(*args)


class VgMarkConfig(VegaLiteSchema):
    """VgMarkConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cursor : :class:`Cursor`
        The mouse cursor used over the mark. Any valid `CSS cursor type
        <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#Values>`__ can be used.
    dir : :class:`Dir`
        The direction of the text. One of ``"ltr"`` (left-to-right) or ``"rtl"``
        (right-to-left). This property determines on which side is truncated in response to
        the limit parameter.

        **Default value:** ``"ltr"``
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : string
        Default Fill Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    font : string
        The typeface to set the text in (e.g., ``"Helvetica Neue"`` ).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., ``"italic"`` ).
    fontWeight : :class:`FontWeight`
        The font weight.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    href : string
        A URL to load upon mouse click. If defined, the mark acts as a hyperlink.
    interpolate : :class:`Interpolate`
        The line interpolation method to use for line and area marks. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : alternate between horizontal and vertical segments, as in a step
          function.
        * ``"step-before"`` : alternate between vertical and horizontal segments, as in a
          step function.
        * ``"step-after"`` : alternate between horizontal and vertical segments, as in a
          step function.
        * ``"basis"`` : a B-spline, with control point duplication on the ends.
        * ``"basis-open"`` : an open B-spline; may not intersect the start or end.
        * ``"basis-closed"`` : a closed B-spline, as in a loop.
        * ``"cardinal"`` : a Cardinal spline, with control point duplication on the ends.
        * ``"cardinal-open"`` : an open Cardinal spline; may not intersect the start or end,
          but will intersect other control points.
        * ``"cardinal-closed"`` : a closed Cardinal spline, as in a loop.
        * ``"bundle"`` : equivalent to basis, except the tension parameter is used to
          straighten the spline.
        * ``"monotone"`` : cubic interpolation that preserves monotonicity in y.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.
        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick
        should be applied to x or y dimension.
        * For area, this property determines the orient property of the Vega output.
        * For line and trail marks, this property determines the sort order of the points in
          the line
        if ``config.sortLineBy`` is not specified.
        For stacked charts, this is always determined by the orientation of the stack;
        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the ``x`` and ``y`` properties.
    shape : string
        The default symbol shape to use. One of: ``"circle"`` (default), ``"square"``,
        ``"cross"``, ``"diamond"``, ``"triangle-up"``, or ``"triangle-down"``, or a custom
        SVG path.

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : string
        Default Stroke Color.  This has higher precedence than ``config.color``

        **Default value:** (None)
    strokeCap : :class:`StrokeCap`
        The stroke cap for line ending style. One of ``"butt"``, ``"round"``, or
        ``"square"``.

        **Default value:** ``"square"``
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of ``"miter"``, ``"round"`` or ``"bevel"``.

        **Default value:** ``"miter"``
    strokeMiterLimit : float
        The miter limit at which to bevel a line join.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** ``1``
    strokeWidth : float
        The stroke width, in pixels.
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : string
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Mapping(required=[])
        The tooltip text to show upon mouse hover.
    """
    _schema = {'$ref': '#/definitions/VgMarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, cornerRadius=Undefined,
                 cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined,
                 fill=Undefined, fillOpacity=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined,
                 limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeCap=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeJoin=Undefined,
                 strokeMiterLimit=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined,
                 tension=Undefined, text=Undefined, theta=Undefined, tooltip=Undefined, **kwds):
        super(VgMarkConfig, self).__init__(align=align, angle=angle, baseline=baseline,
                                           cornerRadius=cornerRadius, cursor=cursor, dir=dir, dx=dx,
                                           dy=dy, ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                           font=font, fontSize=fontSize, fontStyle=fontStyle,
                                           fontWeight=fontWeight, href=href, interpolate=interpolate,
                                           limit=limit, opacity=opacity, orient=orient, radius=radius,
                                           shape=shape, size=size, stroke=stroke, strokeCap=strokeCap,
                                           strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                           strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                           strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                           tension=tension, text=text, theta=theta, tooltip=tooltip,
                                           **kwds)


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

    anchor : :class:`Anchor`
        The anchor position for placing the title. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with an orientation of top these anchor positions map to a
        left-, center-, or right-aligned title.

        **Default value:** ``"middle"`` for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.
        ``"start"`` for other composite views.

        **Note:** `For now <https://github.com/vega/vega-lite/issues/2875>`__, ``anchor`` is
        only customizable only for `single
        <https://vega.github.io/vega-lite/docs/spec.html>`__ and `layered
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views.  For other composite
        views, ``anchor`` is always ``"start"``.
    angle : float
        Angle in degrees of title text.
    baseline : :class:`VerticalAlign`
        Vertical text baseline for title text.
    color : string
        Text color for title text.
    font : string
        Font name for title text.
    fontSize : float
        Font size in pixels for title text.

        **Default value:** ``10``.
    fontWeight : :class:`FontWeight`
        Font weight for title text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    limit : float
        The maximum allowed length in pixels of legend labels.
    offset : float
        Offset in pixels of the title from the chart body and axes.
    orient : :class:`TitleOrient`
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
        The fill color.

        **Default value:** (none)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** (none)
    height : float
        The default height of the single plot or each plot in a trellis plot when the
        visualization has a continuous (non-ordinal) y-scale with ``rangeStep`` = ``null``.

        **Default value:** ``200``
    stroke : string
        The stroke color.

        **Default value:** (none)
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.

        **Default value:** (none)
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.

        **Default value:** (none)
    strokeJoin : :class:`StrokeJoin`
        The stroke line join method. One of miter (default), round or bevel.

        **Default value:** 'miter'
    strokeMiterLimit : float
        The stroke line join method. One of miter (default), round or bevel.

        **Default value:** 'miter'
    strokeOpacity : float
        The stroke opacity (value between [0,1]).

        **Default value:** (none)
    strokeWidth : float
        The stroke width, in pixels.

        **Default value:** (none)
    width : float
        The default width of the single plot or each plot in a trellis plot when the
        visualization has a continuous (non-ordinal) x-scale or ordinal x-scale with
        ``rangeStep`` = ``null``.

        **Default value:** ``200``
    """
    _schema = {'$ref': '#/definitions/ViewConfig'}
    _rootschema = Root._schema

    def __init__(self, clip=Undefined, fill=Undefined, fillOpacity=Undefined, height=Undefined,
                 stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, width=Undefined, **kwds):
        super(ViewConfig, self).__init__(clip=clip, fill=fill, fillOpacity=fillOpacity, height=height,
                                         stroke=stroke, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                         strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, width=width, **kwds)


class WindowFieldDef(VegaLiteSchema):
    """WindowFieldDef schema wrapper

    Mapping(required=[op, as])

    Attributes
    ----------

    op : anyOf(:class:`AggregateOp`, :class:`WindowOnlyOp`)
        The window or aggregation operations to apply within a window, including ``rank``,
        ``lead``, ``sum``, ``average`` or ``count``. See the list of all supported
        operations `here <https://vega.github.io/vega-lite/docs/window.html#ops>`__.
    field : string
        The data field for which to compute the aggregate or window function. This can be
        omitted for window functions that do not operate over a field such as ``count``,
        ``rank``, ``dense_rank``.
    param : float
        Parameter values for the window functions. Parameter values can be omitted for
        operations that do not accept a parameter.

        See the list of all supported operations and their parameters `here
        <https://vega.github.io/vega-lite/docs/transforms/window.html>`__.
    as : string
        The output name for the window operation.
    """
    _schema = {'$ref': '#/definitions/WindowFieldDef'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, param=Undefined, **kwds):
        super(WindowFieldDef, self).__init__(op=op, field=field, param=param, **kwds)


class WindowOnlyOp(VegaLiteSchema):
    """WindowOnlyOp schema wrapper

    enum('row_number', 'rank', 'dense_rank', 'percent_rank', 'cume_dist', 'ntile', 'lag',
    'lead', 'first_value', 'last_value', 'nth_value')
    """
    _schema = {'$ref': '#/definitions/WindowOnlyOp'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(WindowOnlyOp, self).__init__(*args)


class WindowTransform(VegaLiteSchema):
    """WindowTransform schema wrapper

    Mapping(required=[window])

    Attributes
    ----------

    window : List(:class:`WindowFieldDef`)
        The definition of the fields in the window, and what calculations to use.
    frame : List(anyOf(None, float))
        A frame specification as a two-element array indicating how the sliding window
        should proceed. The array entries should either be a number indicating the offset
        from the current data object, or null to indicate unbounded rows preceding or
        following the current data object. The default value is ``[null, 0]``, indicating
        that the sliding window includes the current object and all preceding objects. The
        value ``[-5, 5]`` indicates that the window should include five objects preceding
        and five objects following the current object. Finally, ``[null, null]`` indicates
        that the window frame should always include all data objects. The only operators
        affected are the aggregation operations and the ``first_value``, ``last_value``, and
        ``nth_value`` window operations. The other window operations are not affected by
        this.

        **Default value:** :  ``[null, 0]`` (includes the current object and all preceding
        objects)
    groupby : List(string)
        The data fields for partitioning the data objects into separate windows. If
        unspecified, all data points will be in a single group.
    ignorePeers : boolean
        Indicates if the sliding window frame should ignore peer values. (Peer values are
        those considered identical by the sort criteria). The default is false, causing the
        window frame to expand to include all peer values. If set to true, the window frame
        will be defined by offset values only. This setting only affects those operations
        that depend on the window frame, namely aggregation operations and the first_value,
        last_value, and nth_value window operations.

        **Default value:** ``false``
    sort : List(:class:`SortField`)
        A sort field definition for sorting data objects within a window. If two data
        objects are considered equal by the comparator, they are considered “peer” values of
        equal rank. If sort is not specified, the order is undefined: data objects are
        processed in the order they are observed and none are considered peers (the
        ignorePeers parameter is ignored and treated as if set to ``true`` ).
    """
    _schema = {'$ref': '#/definitions/WindowTransform'}
    _rootschema = Root._schema

    def __init__(self, window=Undefined, frame=Undefined, groupby=Undefined, ignorePeers=Undefined,
                 sort=Undefined, **kwds):
        super(WindowTransform, self).__init__(window=window, frame=frame, groupby=groupby,
                                              ignorePeers=ignorePeers, sort=sort, **kwds)

