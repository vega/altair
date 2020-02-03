# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import SchemaBase, Undefined, _subclasses

import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, 'vega-lite-schema.json').decode('utf-8'))


class VegaLiteSchema(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return _subclasses(VegaLiteSchema)


class Root(VegaLiteSchema):
    """Root schema wrapper

    anyOf(:class:`TopLevelUnitSpec`, :class:`TopLevelFacetSpec`, :class:`TopLevelLayerSpec`,
    :class:`TopLevelRepeatSpec`, :class:`TopLevelConcatSpec`, :class:`TopLevelVConcatSpec`,
    :class:`TopLevelHConcatSpec`)
    A Vega-Lite top-level specification.
    This is the root class for all Vega-Lite specifications.
    (The json schema is generated from this type.)
    """
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)


class Aggregate(VegaLiteSchema):
    """Aggregate schema wrapper

    anyOf(:class:`NonArgAggregateOp`, :class:`ArgmaxDef`, :class:`ArgminDef`)
    """
    _schema = {'$ref': '#/definitions/Aggregate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Aggregate, self).__init__(*args, **kwds)


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


class AggregatedFieldDef(VegaLiteSchema):
    """AggregatedFieldDef schema wrapper

    Mapping(required=[op, as])

    Attributes
    ----------

    op : :class:`AggregateOp`
        The aggregation operation to apply to the fields (e.g., ``"sum"``, ``"average"``, or
        ``"count"`` ).
        See the `full list of supported aggregation operations
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__
        for more information.
    field : :class:`FieldName`
        The data field for which to compute aggregate function. This is required for all
        aggregation operations except ``"count"``.
    as : :class:`FieldName`
        The output field names to use for each aggregated field.
    """
    _schema = {'$ref': '#/definitions/AggregatedFieldDef'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, **kwds):
        super(AggregatedFieldDef, self).__init__(op=op, field=field, **kwds)


class Align(VegaLiteSchema):
    """Align schema wrapper

    enum('left', 'center', 'right')
    """
    _schema = {'$ref': '#/definitions/Align'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Align, self).__init__(*args)


class AnyMark(VegaLiteSchema):
    """AnyMark schema wrapper

    anyOf(:class:`CompositeMark`, :class:`CompositeMarkDef`, :class:`Mark`, :class:`MarkDef`)
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

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
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
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    """
    _schema = {'$ref': '#/definitions/AreaConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, baseline=Undefined,
                 color=Undefined, cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, height=Undefined, href=Undefined, interpolate=Undefined,
                 invalid=Undefined, limit=Undefined, line=Undefined, lineBreak=Undefined,
                 lineHeight=Undefined, opacity=Undefined, order=Undefined, orient=Undefined,
                 point=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 timeUnitBand=Undefined, timeUnitBandPosition=Undefined, tooltip=Undefined,
                 width=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(AreaConfig, self).__init__(align=align, angle=angle, aspect=aspect, baseline=baseline,
                                         color=color, cornerRadius=cornerRadius,
                                         cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                         cornerRadiusBottomRight=cornerRadiusBottomRight,
                                         cornerRadiusTopLeft=cornerRadiusTopLeft,
                                         cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                         dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         height=height, href=href, interpolate=interpolate,
                                         invalid=invalid, limit=limit, line=line, lineBreak=lineBreak,
                                         lineHeight=lineHeight, opacity=opacity, order=order,
                                         orient=orient, point=point, radius=radius, shape=shape,
                                         size=size, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta,
                                         timeUnitBand=timeUnitBand,
                                         timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                         width=width, x=x, x2=x2, y=y, y2=y2, **kwds)


class ArgmaxDef(Aggregate):
    """ArgmaxDef schema wrapper

    Mapping(required=[argmax])

    Attributes
    ----------

    argmax : string

    """
    _schema = {'$ref': '#/definitions/ArgmaxDef'}
    _rootschema = Root._schema

    def __init__(self, argmax=Undefined, **kwds):
        super(ArgmaxDef, self).__init__(argmax=argmax, **kwds)


class ArgminDef(Aggregate):
    """ArgminDef schema wrapper

    Mapping(required=[argmin])

    Attributes
    ----------

    argmin : string

    """
    _schema = {'$ref': '#/definitions/ArgminDef'}
    _rootschema = Root._schema

    def __init__(self, argmin=Undefined, **kwds):
        super(ArgminDef, self).__init__(argmin=argmin, **kwds)


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
        The sizing format type. One of ``"pad"``, ``"fit"``, ``"fit-x"``, ``"fit-y"``,  or
        ``"none"``. See the `autosize type
        <https://vega.github.io/vega-lite/docs/size.html#autosize>`__ documentation for
        descriptions of each.

        **Default value** : ``"pad"``
    """
    _schema = {'$ref': '#/definitions/AutoSizeParams'}
    _rootschema = Root._schema

    def __init__(self, contains=Undefined, resize=Undefined, type=Undefined, **kwds):
        super(AutoSizeParams, self).__init__(contains=contains, resize=resize, type=type, **kwds)


class AutosizeType(VegaLiteSchema):
    """AutosizeType schema wrapper

    anyOf(enum('pad'), enum('none'), :class:`FitType`)
    """
    _schema = {'$ref': '#/definitions/AutosizeType'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(AutosizeType, self).__init__(*args, **kwds)


class Axis(VegaLiteSchema):
    """Axis schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bandPosition : float
        An interpolation fraction indicating where, for ``band`` scales, axis ticks should
        be positioned. A value of ``0`` places ticks at the left edge of their bands. A
        value of ``0.5`` places ticks in the middle of their bands.

        **Default value:** ``0.5``
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as
        part of the axis.

        **Default value:** ``true``
    domainColor : anyOf(None, :class:`Color`)
        Color of axis domain line.

        **Default value:** ``"gray"``.
    domainDash : List(float)
        An array of alternating [stroke, space] lengths for dashed domain lines.
    domainDashOffset : float
        The pixel offset at which to start drawing with the domain dash array.
    domainOpacity : float
        Opacity of the axis domain line.
    domainWidth : float
        Stroke width of axis domain line

        **Default value:** ``1``
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis

        **Default value:** ``true`` for `continuous scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ that are not
        binned; otherwise, ``false``.
    gridColor : anyOf(anyOf(None, :class:`Color`), :class:`ConditionalAxisColor`)

    gridDash : anyOf(List(float), :class:`ConditionalAxisNumberArray`)

    gridDashOffset : anyOf(float, :class:`ConditionalAxisNumber`)

    gridOpacity : anyOf(float, :class:`ConditionalAxisNumber`)

    gridWidth : anyOf(float, :class:`ConditionalAxisNumber`)

    labelAlign : anyOf(:class:`Align`, :class:`ConditionalAxisNumber`)

    labelAngle : float
        The rotation angle of the axis labels.

        **Default value:** ``-90`` for nominal and ordinal fields; ``0`` otherwise.
    labelBaseline : anyOf(:class:`TextBaseline`, :class:`ConditionalAxisLabelBaseline`)

    labelBound : anyOf(float, boolean)
        Indicates if labels should be hidden if they exceed the axis range. If ``false``
        (the default) no bounds overlap analysis is performed. If ``true``, labels will be
        hidden if they exceed the axis range by more than 1 pixel. If this property is a
        number, it specifies the pixel tolerance: the maximum amount by which a label
        bounding box may exceed the axis range.

        **Default value:** ``false``.
    labelColor : anyOf(anyOf(None, :class:`Color`), :class:`ConditionalAxisColor`)

    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
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
    labelFlushOffset : float
        Indicates the number of pixels by which to offset flush-adjusted labels. For
        example, a value of ``2`` will push flush-adjusted labels 2 pixels outward from the
        center of the axis. Offsets can help the labels better visually group with
        corresponding axis ticks.

        **Default value:** ``0``.
    labelFont : anyOf(string, :class:`ConditionalAxisString`)

    labelFontSize : anyOf(float, :class:`ConditionalAxisNumber`)

    labelFontStyle : anyOf(:class:`FontStyle`, :class:`ConditionalAxisLabelFontStyle`)

    labelFontWeight : anyOf(:class:`FontWeight`, :class:`ConditionalAxisLabelFontWeight`)

    labelLimit : float
        Maximum allowed pixel width of axis tick labels.

        **Default value:** ``180``
    labelOpacity : anyOf(float, :class:`ConditionalAxisNumber`)

    labelOverlap : :class:`LabelOverlap`
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

        **Default value:** ``2``
    labelSeparation : float
        The minimum separation that must be between label bounding boxes for them to be
        considered non-overlapping (default ``0`` ). This property is ignored if
        *labelOverlap* resolution is not enabled.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.

        **Default value:** ``true``.
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
        a y-axis oriented towards the right edge of the chart).

        **Default value:** ``"bottom"`` for x-axes and ``"left"`` for y-axes.
    position : float
        The anchor position of the axis in pixels. For x-axes with top or bottom
        orientation, this sets the axis group x coordinate. For y-axes with left or right
        orientation, this sets the axis group y coordinate.

        **Default value** : ``0``
    tickBand : enum('center', 'extent')
        For band scales, indicates if ticks and grid lines should be placed at the center of
        a band (default) or at the band extents to indicate intervals.
    tickColor : anyOf(anyOf(None, :class:`Color`), :class:`ConditionalAxisColor`)

    tickCount : float
        A desired number of ticks, for axes visualizing quantitative scales. The resulting
        number may be different so that values are "nice" (multiples of 2, 5, 10) and lie
        within the underlying scale's range.

        **Default value** : Determine using a formula ``ceil(width/40)`` for x and
        ``ceil(height/40)`` for y.
    tickDash : anyOf(List(float), :class:`ConditionalAxisNumberArray`)

    tickDashOffset : anyOf(float, :class:`ConditionalAxisNumber`)

    tickExtra : boolean
        Boolean flag indicating if an extra axis tick should be added for the initial
        position of the axis. This flag is useful for styling axes for ``band`` scales such
        that ticks are placed on band boundaries rather in the middle of a band. Use in
        conjunction with ``"bandPosition": 1`` and an axis ``"padding"`` value of ``0``.
    tickMinStep : float
        The minimum desired step between axis ticks, in terms of scale domain values. For
        example, a value of ``1`` indicates that ticks should not be less than 1 unit apart.
        If ``tickMinStep`` is specified, the ``tickCount`` value will be adjusted, if
        necessary, to enforce the minimum step value.

        **Default value** : ``undefined``
    tickOffset : float
        Position offset in pixels to apply to ticks, labels, and gridlines.
    tickOpacity : anyOf(float, :class:`ConditionalAxisNumber`)

    tickRound : boolean
        Boolean flag indicating if pixel position values should be rounded to the nearest
        integer.

        **Default value:** ``true``
    tickSize : float
        The size in pixels of axis ticks.

        **Default value:** ``5``
    tickWidth : anyOf(float, :class:`ConditionalAxisNumber`)

    ticks : boolean
        Boolean value that determines whether the axis should include ticks.

        **Default value:** ``true``
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    titleAlign : :class:`Align`
        Horizontal text alignment of axis titles.
    titleAnchor : :class:`TitleAnchor`
        Text anchor position for placing axis titles.
    titleAngle : float
        Angle in degrees of axis titles.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for axis titles.
    titleColor : anyOf(None, :class:`Color`)
        Color of the title, can be in hex color code or regular color name.
    titleFont : string
        Font of the title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the title.
    titleFontStyle : :class:`FontStyle`
        Font style of the title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        Maximum allowed pixel width of axis titles.
    titleLineHeight : float
        Line height in pixels for multi-line title text.
    titleOpacity : float
        Opacity of the axis title.
    titlePadding : float
        The padding, in pixels, between title and axis.
    titleX : float
        X-coordinate of the axis title relative to the axis group.
    titleY : float
        Y-coordinate of the axis title relative to the axis group.
    translate : float
        Translation offset in pixels applied to the axis group mark x and y. If specified,
        overrides the default behavior of a 0.5 offset to pixel-align stroked lines.
    values : anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`))
        Explicitly set the visible axis tick values.
    zindex : float
        A non-negative integer indicating the z-index of the axis.
        If zindex is 0, axes should be drawn behind all chart elements.
        To put them in front, set ``zindex`` to ``1`` or more.

        **Default value:** ``0`` (behind the marks).
    """
    _schema = {'$ref': '#/definitions/Axis'}
    _rootschema = Root._schema

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined,
                 domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined,
                 domainWidth=Undefined, format=Undefined, formatType=Undefined, grid=Undefined,
                 gridColor=Undefined, gridDash=Undefined, gridDashOffset=Undefined,
                 gridOpacity=Undefined, gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined,
                 labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined,
                 labelExpr=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined,
                 labelFontWeight=Undefined, labelLimit=Undefined, labelOpacity=Undefined,
                 labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined,
                 labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined,
                 orient=Undefined, position=Undefined, tickBand=Undefined, tickColor=Undefined,
                 tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined, tickExtra=Undefined,
                 tickMinStep=Undefined, tickOffset=Undefined, tickOpacity=Undefined,
                 tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined,
                 title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined,
                 titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined,
                 titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined,
                 titlePadding=Undefined, titleX=Undefined, titleY=Undefined, translate=Undefined,
                 values=Undefined, zindex=Undefined, **kwds):
        super(Axis, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor,
                                   domainDash=domainDash, domainDashOffset=domainDashOffset,
                                   domainOpacity=domainOpacity, domainWidth=domainWidth, format=format,
                                   formatType=formatType, grid=grid, gridColor=gridColor,
                                   gridDash=gridDash, gridDashOffset=gridDashOffset,
                                   gridOpacity=gridOpacity, gridWidth=gridWidth, labelAlign=labelAlign,
                                   labelAngle=labelAngle, labelBaseline=labelBaseline,
                                   labelBound=labelBound, labelColor=labelColor, labelExpr=labelExpr,
                                   labelFlush=labelFlush, labelFlushOffset=labelFlushOffset,
                                   labelFont=labelFont, labelFontSize=labelFontSize,
                                   labelFontStyle=labelFontStyle, labelFontWeight=labelFontWeight,
                                   labelLimit=labelLimit, labelOpacity=labelOpacity,
                                   labelOverlap=labelOverlap, labelPadding=labelPadding,
                                   labelSeparation=labelSeparation, labels=labels, maxExtent=maxExtent,
                                   minExtent=minExtent, offset=offset, orient=orient, position=position,
                                   tickBand=tickBand, tickColor=tickColor, tickCount=tickCount,
                                   tickDash=tickDash, tickDashOffset=tickDashOffset,
                                   tickExtra=tickExtra, tickMinStep=tickMinStep, tickOffset=tickOffset,
                                   tickOpacity=tickOpacity, tickRound=tickRound, tickSize=tickSize,
                                   tickWidth=tickWidth, ticks=ticks, title=title, titleAlign=titleAlign,
                                   titleAnchor=titleAnchor, titleAngle=titleAngle,
                                   titleBaseline=titleBaseline, titleColor=titleColor,
                                   titleFont=titleFont, titleFontSize=titleFontSize,
                                   titleFontStyle=titleFontStyle, titleFontWeight=titleFontWeight,
                                   titleLimit=titleLimit, titleLineHeight=titleLineHeight,
                                   titleOpacity=titleOpacity, titlePadding=titlePadding, titleX=titleX,
                                   titleY=titleY, translate=translate, values=values, zindex=zindex,
                                   **kwds)


class AxisConfig(VegaLiteSchema):
    """AxisConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bandPosition : float
        An interpolation fraction indicating where, for ``band`` scales, axis ticks should
        be positioned. A value of ``0`` places ticks at the left edge of their bands. A
        value of ``0.5`` places ticks in the middle of their bands.

        **Default value:** ``0.5``
    domain : boolean
        A boolean flag indicating if the domain (the axis baseline) should be included as
        part of the axis.

        **Default value:** ``true``
    domainColor : anyOf(None, :class:`Color`)
        Color of axis domain line.

        **Default value:** ``"gray"``.
    domainDash : List(float)
        An array of alternating [stroke, space] lengths for dashed domain lines.
    domainDashOffset : float
        The pixel offset at which to start drawing with the domain dash array.
    domainOpacity : float
        Opacity of the axis domain line.
    domainWidth : float
        Stroke width of axis domain line

        **Default value:** ``1``
    grid : boolean
        A boolean flag indicating if grid lines should be included as part of the axis

        **Default value:** ``true`` for `continuous scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ that are not
        binned; otherwise, ``false``.
    gridColor : anyOf(anyOf(None, :class:`Color`), :class:`ConditionalAxisColor`)

    gridDash : anyOf(List(float), :class:`ConditionalAxisNumberArray`)

    gridDashOffset : anyOf(float, :class:`ConditionalAxisNumber`)

    gridOpacity : anyOf(float, :class:`ConditionalAxisNumber`)

    gridWidth : anyOf(float, :class:`ConditionalAxisNumber`)

    labelAlign : anyOf(:class:`Align`, :class:`ConditionalAxisNumber`)

    labelAngle : float
        The rotation angle of the axis labels.

        **Default value:** ``-90`` for nominal and ordinal fields; ``0`` otherwise.
    labelBaseline : anyOf(:class:`TextBaseline`, :class:`ConditionalAxisLabelBaseline`)

    labelBound : anyOf(float, boolean)
        Indicates if labels should be hidden if they exceed the axis range. If ``false``
        (the default) no bounds overlap analysis is performed. If ``true``, labels will be
        hidden if they exceed the axis range by more than 1 pixel. If this property is a
        number, it specifies the pixel tolerance: the maximum amount by which a label
        bounding box may exceed the axis range.

        **Default value:** ``false``.
    labelColor : anyOf(anyOf(None, :class:`Color`), :class:`ConditionalAxisColor`)

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
    labelFlushOffset : float
        Indicates the number of pixels by which to offset flush-adjusted labels. For
        example, a value of ``2`` will push flush-adjusted labels 2 pixels outward from the
        center of the axis. Offsets can help the labels better visually group with
        corresponding axis ticks.

        **Default value:** ``0``.
    labelFont : anyOf(string, :class:`ConditionalAxisString`)

    labelFontSize : anyOf(float, :class:`ConditionalAxisNumber`)

    labelFontStyle : anyOf(:class:`FontStyle`, :class:`ConditionalAxisLabelFontStyle`)

    labelFontWeight : anyOf(:class:`FontWeight`, :class:`ConditionalAxisLabelFontWeight`)

    labelLimit : float
        Maximum allowed pixel width of axis tick labels.

        **Default value:** ``180``
    labelOpacity : anyOf(float, :class:`ConditionalAxisNumber`)

    labelOverlap : :class:`LabelOverlap`
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

        **Default value:** ``2``
    labelSeparation : float
        The minimum separation that must be between label bounding boxes for them to be
        considered non-overlapping (default ``0`` ). This property is ignored if
        *labelOverlap* resolution is not enabled.
    labels : boolean
        A boolean flag indicating if labels should be included as part of the axis.

        **Default value:** ``true``.
    maxExtent : float
        The maximum extent in pixels that axis ticks and labels should use. This determines
        a maximum offset value for axis titles.

        **Default value:** ``undefined``.
    minExtent : float
        The minimum extent in pixels that axis ticks and labels should use. This determines
        a minimum offset value for axis titles.

        **Default value:** ``30`` for y-axis; ``undefined`` for x-axis.
    orient : :class:`AxisOrient`
        The orientation of the axis. One of ``"top"``, ``"bottom"``, ``"left"`` or
        ``"right"``. The orientation can be used to further specialize the axis type (e.g.,
        a y-axis oriented towards the right edge of the chart).

        **Default value:** ``"bottom"`` for x-axes and ``"left"`` for y-axes.
    tickBand : enum('center', 'extent')
        For band scales, indicates if ticks and grid lines should be placed at the center of
        a band (default) or at the band extents to indicate intervals.
    tickColor : anyOf(anyOf(None, :class:`Color`), :class:`ConditionalAxisColor`)

    tickDash : anyOf(List(float), :class:`ConditionalAxisNumberArray`)

    tickDashOffset : anyOf(float, :class:`ConditionalAxisNumber`)

    tickExtra : boolean
        Boolean flag indicating if an extra axis tick should be added for the initial
        position of the axis. This flag is useful for styling axes for ``band`` scales such
        that ticks are placed on band boundaries rather in the middle of a band. Use in
        conjunction with ``"bandPosition": 1`` and an axis ``"padding"`` value of ``0``.
    tickOffset : float
        Position offset in pixels to apply to ticks, labels, and gridlines.
    tickOpacity : anyOf(float, :class:`ConditionalAxisNumber`)

    tickRound : boolean
        Boolean flag indicating if pixel position values should be rounded to the nearest
        integer.

        **Default value:** ``true``
    tickSize : float
        The size in pixels of axis ticks.

        **Default value:** ``5``
    tickWidth : anyOf(float, :class:`ConditionalAxisNumber`)

    ticks : boolean
        Boolean value that determines whether the axis should include ticks.

        **Default value:** ``true``
    title : None
        Set to null to disable title for the axis, legend, or header.
    titleAlign : :class:`Align`
        Horizontal text alignment of axis titles.
    titleAnchor : :class:`TitleAnchor`
        Text anchor position for placing axis titles.
    titleAngle : float
        Angle in degrees of axis titles.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for axis titles.
    titleColor : anyOf(None, :class:`Color`)
        Color of the title, can be in hex color code or regular color name.
    titleFont : string
        Font of the title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the title.
    titleFontStyle : :class:`FontStyle`
        Font style of the title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        Maximum allowed pixel width of axis titles.
    titleLineHeight : float
        Line height in pixels for multi-line title text.
    titleOpacity : float
        Opacity of the axis title.
    titlePadding : float
        The padding, in pixels, between title and axis.
    titleX : float
        X-coordinate of the axis title relative to the axis group.
    titleY : float
        Y-coordinate of the axis title relative to the axis group.
    translate : float
        Translation offset in pixels applied to the axis group mark x and y. If specified,
        overrides the default behavior of a 0.5 offset to pixel-align stroked lines.
    """
    _schema = {'$ref': '#/definitions/AxisConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined,
                 domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined,
                 domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined,
                 gridDashOffset=Undefined, gridOpacity=Undefined, gridWidth=Undefined,
                 labelAlign=Undefined, labelAngle=Undefined, labelBaseline=Undefined,
                 labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined,
                 labelFlushOffset=Undefined, labelFont=Undefined, labelFontSize=Undefined,
                 labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined,
                 labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined,
                 labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined,
                 orient=Undefined, tickBand=Undefined, tickColor=Undefined, tickDash=Undefined,
                 tickDashOffset=Undefined, tickExtra=Undefined, tickOffset=Undefined,
                 tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined,
                 ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined,
                 titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined,
                 titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined,
                 titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined,
                 titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined,
                 translate=Undefined, **kwds):
        super(AxisConfig, self).__init__(bandPosition=bandPosition, domain=domain,
                                         domainColor=domainColor, domainDash=domainDash,
                                         domainDashOffset=domainDashOffset, domainOpacity=domainOpacity,
                                         domainWidth=domainWidth, grid=grid, gridColor=gridColor,
                                         gridDash=gridDash, gridDashOffset=gridDashOffset,
                                         gridOpacity=gridOpacity, gridWidth=gridWidth,
                                         labelAlign=labelAlign, labelAngle=labelAngle,
                                         labelBaseline=labelBaseline, labelBound=labelBound,
                                         labelColor=labelColor, labelFlush=labelFlush,
                                         labelFlushOffset=labelFlushOffset, labelFont=labelFont,
                                         labelFontSize=labelFontSize, labelFontStyle=labelFontStyle,
                                         labelFontWeight=labelFontWeight, labelLimit=labelLimit,
                                         labelOpacity=labelOpacity, labelOverlap=labelOverlap,
                                         labelPadding=labelPadding, labelSeparation=labelSeparation,
                                         labels=labels, maxExtent=maxExtent, minExtent=minExtent,
                                         orient=orient, tickBand=tickBand, tickColor=tickColor,
                                         tickDash=tickDash, tickDashOffset=tickDashOffset,
                                         tickExtra=tickExtra, tickOffset=tickOffset,
                                         tickOpacity=tickOpacity, tickRound=tickRound,
                                         tickSize=tickSize, tickWidth=tickWidth, ticks=ticks,
                                         title=title, titleAlign=titleAlign, titleAnchor=titleAnchor,
                                         titleAngle=titleAngle, titleBaseline=titleBaseline,
                                         titleColor=titleColor, titleFont=titleFont,
                                         titleFontSize=titleFontSize, titleFontStyle=titleFontStyle,
                                         titleFontWeight=titleFontWeight, titleLimit=titleLimit,
                                         titleLineHeight=titleLineHeight, titleOpacity=titleOpacity,
                                         titlePadding=titlePadding, titleX=titleX, titleY=titleY,
                                         translate=translate, **kwds)


class AxisOrient(VegaLiteSchema):
    """AxisOrient schema wrapper

    enum('top', 'bottom', 'left', 'right')
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


class BaseLegendLayout(VegaLiteSchema):
    """BaseLegendLayout schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    anchor : anyOf(:class:`TitleAnchor`, :class:`SignalRef`)
        The anchor point for legend orient group layout.
    bounds : :class:`LayoutBounds`
        The bounds calculation to use for legend orient group layout.
    center : anyOf(boolean, :class:`SignalRef`)
        A flag to center legends within a shared orient group.
    direction : anyOf(:class:`Orientation`, :class:`SignalRef`)
        The layout direction for legend orient group layout.
    margin : anyOf(float, :class:`SignalRef`)
        The pixel margin between legends within a orient group.
    offset : anyOf(float, :class:`SignalRef`)
        The pixel offset from the chart body for a legend orient group.
    """
    _schema = {'$ref': '#/definitions/BaseLegendLayout'}
    _rootschema = Root._schema

    def __init__(self, anchor=Undefined, bounds=Undefined, center=Undefined, direction=Undefined,
                 margin=Undefined, offset=Undefined, **kwds):
        super(BaseLegendLayout, self).__init__(anchor=anchor, bounds=bounds, center=center,
                                               direction=direction, margin=margin, offset=offset, **kwds)


class BaseMarkConfig(VegaLiteSchema):
    """BaseMarkConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

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
    height : float
        Height of the marks.
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
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        The pixel area each the point/circle/square.
        For example: in the case of circles, the radius is determined in part by the square
        root of the size value.

        **Default value:** ``30``
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    tooltip : Any
        The tooltip text to show upon mouse hover.
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    """
    _schema = {'$ref': '#/definitions/BaseMarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, baseline=Undefined,
                 cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                 height=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined,
                 lineBreak=Undefined, lineHeight=Undefined, opacity=Undefined, orient=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 tooltip=Undefined, width=Undefined, x=Undefined, x2=Undefined, y=Undefined,
                 y2=Undefined, **kwds):
        super(BaseMarkConfig, self).__init__(align=align, angle=angle, aspect=aspect, baseline=baseline,
                                             cornerRadius=cornerRadius,
                                             cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                             cornerRadiusBottomRight=cornerRadiusBottomRight,
                                             cornerRadiusTopLeft=cornerRadiusTopLeft,
                                             cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                             dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                             fillOpacity=fillOpacity, font=font, fontSize=fontSize,
                                             fontStyle=fontStyle, fontWeight=fontWeight, height=height,
                                             href=href, interpolate=interpolate, limit=limit,
                                             lineBreak=lineBreak, lineHeight=lineHeight,
                                             opacity=opacity, orient=orient, radius=radius, shape=shape,
                                             size=size, stroke=stroke, strokeCap=strokeCap,
                                             strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                             strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                             strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                             tension=tension, text=text, theta=theta, tooltip=tooltip,
                                             width=width, x=x, x2=x2, y=y, y2=y2, **kwds)


class BaseTitleNoValueRefs(VegaLiteSchema):
    """BaseTitleNoValueRefs schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        Horizontal text alignment for title text. One of ``"left"``, ``"center"``, or
        ``"right"``.
    anchor : :class:`TitleAnchor`
        The anchor position for placing the title and subtitle text. One of ``"start"``,
        ``"middle"``, or ``"end"``. For example, with an orientation of top these anchor
        positions map to a left-, center-, or right-aligned title.
    angle : float
        Angle in degrees of title and subtitle text.
    baseline : :class:`TextBaseline`
        Vertical text baseline for title and subtitle text. One of ``"top"``, ``"middle"``,
        ``"bottom"``, or ``"alphabetic"``.
    color : anyOf(None, :class:`Color`)
        Text color for title text.
    dx : float
        Delta offset for title and subtitle text x-coordinate.
    dy : float
        Delta offset for title and subtitle text y-coordinate.
    font : string
        Font name for title text.
    fontSize : float
        Font size in pixels for title text.
    fontStyle : :class:`FontStyle`
        Font style for title text.
    fontWeight : :class:`FontWeight`
        Font weight for title text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    frame : anyOf(:class:`TitleFrame`, string)
        The reference frame for the anchor position, one of ``"bounds"`` (to anchor relative
        to the full bounding box) or ``"group"`` (to anchor relative to the group width or
        height).
    limit : float
        The maximum allowed length in pixels of title and subtitle text.
    lineHeight : float
        Line height in pixels for multi-line title text.
    offset : float
        The orthogonal offset in pixels by which to displace the title group from its
        position along the edge of the chart.
    orient : :class:`TitleOrient`
        Default title orientation ( ``"top"``, ``"bottom"``, ``"left"``, or ``"right"`` )
    subtitleColor : anyOf(None, :class:`Color`)
        Text color for subtitle text.
    subtitleFont : string
        Font name for subtitle text.
    subtitleFontSize : float
        Font size in pixels for subtitle text.
    subtitleFontStyle : :class:`FontStyle`
        Font style for subtitle text.
    subtitleFontWeight : :class:`FontWeight`
        Font weight for subtitle text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    subtitleLineHeight : float
        Line height in pixels for multi-line subtitle text.
    subtitlePadding : float
        The padding in pixels between title and subtitle text.
    """
    _schema = {'$ref': '#/definitions/BaseTitleNoValueRefs'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, anchor=Undefined, angle=Undefined, baseline=Undefined,
                 color=Undefined, dx=Undefined, dy=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, frame=Undefined, limit=Undefined,
                 lineHeight=Undefined, offset=Undefined, orient=Undefined, subtitleColor=Undefined,
                 subtitleFont=Undefined, subtitleFontSize=Undefined, subtitleFontStyle=Undefined,
                 subtitleFontWeight=Undefined, subtitleLineHeight=Undefined, subtitlePadding=Undefined,
                 **kwds):
        super(BaseTitleNoValueRefs, self).__init__(align=align, anchor=anchor, angle=angle,
                                                   baseline=baseline, color=color, dx=dx, dy=dy,
                                                   font=font, fontSize=fontSize, fontStyle=fontStyle,
                                                   fontWeight=fontWeight, frame=frame, limit=limit,
                                                   lineHeight=lineHeight, offset=offset, orient=orient,
                                                   subtitleColor=subtitleColor,
                                                   subtitleFont=subtitleFont,
                                                   subtitleFontSize=subtitleFontSize,
                                                   subtitleFontStyle=subtitleFontStyle,
                                                   subtitleFontWeight=subtitleFontWeight,
                                                   subtitleLineHeight=subtitleLineHeight,
                                                   subtitlePadding=subtitlePadding, **kwds)


class BinExtent(VegaLiteSchema):
    """BinExtent schema wrapper

    anyOf(List([float, float]), :class:`SelectionExtent`)
    """
    _schema = {'$ref': '#/definitions/BinExtent'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(BinExtent, self).__init__(*args, **kwds)


class BinParams(VegaLiteSchema):
    """BinParams schema wrapper

    Mapping(required=[])
    Binning properties or boolean flag for determining whether to bin data or not.

    Attributes
    ----------

    anchor : float
        A value in the binned domain at which to anchor the bins, shifting the bin
        boundaries if necessary to ensure that a boundary aligns with the anchor value.

        **Default value:** the minimum bin extent value
    base : float
        The number base to use for automatic bin determination (default is base 10).

        **Default value:** ``10``
    binned : boolean
        When set to ``true``, Vega-Lite treats the input data as already binned.
    divide : List([float, float])
        Scale factors indicating allowable subdivisions. The default value is [5, 2], which
        indicates that for base 10 numbers (the default base), the method may consider
        dividing bin sizes by 5 and/or 2. For example, for an initial step size of 10, the
        method can check if bin sizes of 2 (= 10/5), 5 (= 10/2), or 1 (= 10/(5*2)) might
        also satisfy the given constraints.

        **Default value:** ``[5, 2]``
    extent : :class:`BinExtent`
        A two-element ( ``[min, max]`` ) array indicating the range of desired bin values.
    maxbins : float
        Maximum number of bins.

        **Default value:** ``6`` for ``row``, ``column`` and ``shape`` channels; ``10`` for
        other channels
    minstep : float
        A minimum allowable step size (particularly useful for integer values).
    nice : boolean
        If true, attempts to make the bin boundaries use human-friendly boundaries, such as
        multiples of ten.

        **Default value:** ``true``
    step : float
        An exact step size to use between bins.

        **Note:** If provided, options such as maxbins will be ignored.
    steps : List(float)
        An array of allowable step sizes to choose from.
    """
    _schema = {'$ref': '#/definitions/BinParams'}
    _rootschema = Root._schema

    def __init__(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined,
                 extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined,
                 steps=Undefined, **kwds):
        super(BinParams, self).__init__(anchor=anchor, base=base, binned=binned, divide=divide,
                                        extent=extent, maxbins=maxbins, minstep=minstep, nice=nice,
                                        step=step, steps=steps, **kwds)


class Binding(VegaLiteSchema):
    """Binding schema wrapper

    anyOf(:class:`BindCheckbox`, :class:`BindRadioSelect`, :class:`BindRange`,
    :class:`InputBinding`)
    """
    _schema = {'$ref': '#/definitions/Binding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Binding, self).__init__(*args, **kwds)


class BindCheckbox(Binding):
    """BindCheckbox schema wrapper

    Mapping(required=[input])

    Attributes
    ----------

    input : enum('checkbox')

    debounce : float

    element : :class:`Element`

    name : string

    type : string

    """
    _schema = {'$ref': '#/definitions/BindCheckbox'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, debounce=Undefined, element=Undefined, name=Undefined,
                 type=Undefined, **kwds):
        super(BindCheckbox, self).__init__(input=input, debounce=debounce, element=element, name=name,
                                           type=type, **kwds)


class BindRadioSelect(Binding):
    """BindRadioSelect schema wrapper

    Mapping(required=[input, options])

    Attributes
    ----------

    input : enum('radio', 'select')

    options : List(Any)

    debounce : float

    element : :class:`Element`

    labels : List(string)

    name : string

    type : string

    """
    _schema = {'$ref': '#/definitions/BindRadioSelect'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, options=Undefined, debounce=Undefined, element=Undefined,
                 labels=Undefined, name=Undefined, type=Undefined, **kwds):
        super(BindRadioSelect, self).__init__(input=input, options=options, debounce=debounce,
                                              element=element, labels=labels, name=name, type=type,
                                              **kwds)


class BindRange(Binding):
    """BindRange schema wrapper

    Mapping(required=[input])

    Attributes
    ----------

    input : enum('range')

    debounce : float

    element : :class:`Element`

    max : float

    min : float

    name : string

    step : float

    type : string

    """
    _schema = {'$ref': '#/definitions/BindRange'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, debounce=Undefined, element=Undefined, max=Undefined,
                 min=Undefined, name=Undefined, step=Undefined, type=Undefined, **kwds):
        super(BindRange, self).__init__(input=input, debounce=debounce, element=element, max=max,
                                        min=min, name=name, step=step, type=type, **kwds)


class BoxPlotConfig(VegaLiteSchema):
    """BoxPlotConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    box : anyOf(boolean, :class:`MarkConfig`)

    extent : anyOf(enum('min-max'), float)
        The extent of the whiskers. Available options include:


        * ``"min-max"`` : min and max are the lower and upper whiskers respectively.
        * A number representing multiple of the interquartile range. This number will be
          multiplied by the IQR to determine whisker boundary, which spans from the smallest
          data to the largest data within the range *[Q1 - k * IQR, Q3 + k * IQR]* where
          *Q1* and *Q3* are the first and third quartiles while *IQR* is the interquartile
          range ( *Q3-Q1* ).

        **Default value:** ``1.5``.
    median : anyOf(boolean, :class:`MarkConfig`)

    outliers : anyOf(boolean, :class:`MarkConfig`)

    rule : anyOf(boolean, :class:`MarkConfig`)

    size : float
        Size of the box and median tick of a box plot
    ticks : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/BoxPlotConfig'}
    _rootschema = Root._schema

    def __init__(self, box=Undefined, extent=Undefined, median=Undefined, outliers=Undefined,
                 rule=Undefined, size=Undefined, ticks=Undefined, **kwds):
        super(BoxPlotConfig, self).__init__(box=box, extent=extent, median=median, outliers=outliers,
                                            rule=rule, size=size, ticks=ticks, **kwds)


class BrushConfig(VegaLiteSchema):
    """BrushConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    fill : :class:`Color`
        The fill color of the interval mark.

        **Default value:** ``"#333333"``
    fillOpacity : float
        The fill opacity of the interval mark (a value between 0 and 1).

        **Default value:** ``0.125``
    stroke : :class:`Color`
        The stroke color of the interval mark.

        **Default value:** ``"#ffffff"``
    strokeDash : List(float)
        An array of alternating stroke and space lengths,
        for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) with which to begin drawing the stroke dash array.
    strokeOpacity : float
        The stroke opacity of the interval mark (a value between ``0`` and ``1`` ).
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


class Color(VegaLiteSchema):
    """Color schema wrapper

    anyOf(:class:`ColorName`, :class:`HexColor`, string)
    """
    _schema = {'$ref': '#/definitions/Color'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Color, self).__init__(*args, **kwds)


class ColorGradientFieldDefWithCondition(VegaLiteSchema):
    """ColorGradientFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnull`,
    List(:class:`ConditionalValueDefGradientstringnull`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ColorGradientFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(ColorGradientFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate,
                                                                 bin=bin, condition=condition,
                                                                 field=field, legend=legend,
                                                                 scale=scale, sort=sort,
                                                                 timeUnit=timeUnit, title=title, **kwds)


class ColorGradientValueDefWithCondition(VegaLiteSchema):
    """ColorGradientValueDefWithCondition schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`,
    :class:`ConditionalValueDefGradientstringnull`,
    List(:class:`ConditionalValueDefGradientstringnull`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(:class:`Gradient`, string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ColorGradientValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ColorGradientValueDefWithCondition, self).__init__(condition=condition, value=value,
                                                                 **kwds)


class ColorName(Color):
    """ColorName schema wrapper

    enum('black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia', 'green',
    'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'aqua', 'orange', 'aliceblue',
    'antiquewhite', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blueviolet',
    'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
    'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
    'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
    'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray',
    'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray',
    'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'gainsboro',
    'ghostwhite', 'gold', 'goldenrod', 'greenyellow', 'grey', 'honeydew', 'hotpink',
    'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen',
    'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray',
    'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue',
    'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'limegreen', 'linen',
    'magenta', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
    'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
    'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite',
    'oldlace', 'olivedrab', 'orangered', 'orchid', 'palegoldenrod', 'palegreen',
    'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum',
    'powderblue', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen',
    'seashell', 'sienna', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow',
    'springgreen', 'steelblue', 'tan', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat',
    'whitesmoke', 'yellowgreen', 'rebeccapurple')
    """
    _schema = {'$ref': '#/definitions/ColorName'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ColorName, self).__init__(*args)


class ColorScheme(VegaLiteSchema):
    """ColorScheme schema wrapper

    anyOf(:class:`Categorical`, :class:`SequentialSingleHue`, :class:`SequentialMultiHue`,
    :class:`Diverging`, :class:`Cyclical`)
    """
    _schema = {'$ref': '#/definitions/ColorScheme'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ColorScheme, self).__init__(*args, **kwds)


class Categorical(ColorScheme):
    """Categorical schema wrapper

    enum('accent', 'category10', 'category20', 'category20b', 'category20c', 'dark2', 'paired',
    'pastel1', 'pastel2', 'set1', 'set2', 'set3', 'tableau10', 'tableau20')
    """
    _schema = {'$ref': '#/definitions/Categorical'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Categorical, self).__init__(*args)


class CompositeMark(AnyMark):
    """CompositeMark schema wrapper

    anyOf(:class:`BoxPlot`, :class:`ErrorBar`, :class:`ErrorBand`)
    """
    _schema = {'$ref': '#/definitions/CompositeMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(CompositeMark, self).__init__(*args, **kwds)


class BoxPlot(CompositeMark):
    """BoxPlot schema wrapper

    enum('boxplot')
    """
    _schema = {'$ref': '#/definitions/BoxPlot'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(BoxPlot, self).__init__(*args)


class CompositeMarkDef(AnyMark):
    """CompositeMarkDef schema wrapper

    anyOf(:class:`BoxPlotDef`, :class:`ErrorBarDef`, :class:`ErrorBandDef`)
    """
    _schema = {'$ref': '#/definitions/CompositeMarkDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(CompositeMarkDef, self).__init__(*args, **kwds)


class BoxPlotDef(CompositeMarkDef):
    """BoxPlotDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`BoxPlot`
        The mark type. This could a primitive mark type
        (one of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"geoshape"``, ``"rule"``, and ``"text"`` )
        or a composite mark type ( ``"boxplot"``, ``"errorband"``, ``"errorbar"`` ).
    box : anyOf(boolean, :class:`MarkConfig`)

    clip : boolean
        Whether a composite mark be clipped to the enclosing group’s width and height.
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    extent : anyOf(enum('min-max'), float)
        The extent of the whiskers. Available options include:


        * ``"min-max"`` : min and max are the lower and upper whiskers respectively.
        * A number representing multiple of the interquartile range. This number will be
          multiplied by the IQR to determine whisker boundary, which spans from the smallest
          data to the largest data within the range *[Q1 - k * IQR, Q3 + k * IQR]* where
          *Q1* and *Q3* are the first and third quartiles while *IQR* is the interquartile
          range ( *Q3-Q1* ).

        **Default value:** ``1.5``.
    median : anyOf(boolean, :class:`MarkConfig`)

    opacity : float
        The opacity (value between [0,1]) of the mark.
    orient : :class:`Orientation`
        Orientation of the box plot. This is normally automatically determined based on
        types of fields on x and y channels. However, an explicit ``orient`` be specified
        when the orientation is ambiguous.

        **Default value:** ``"vertical"``.
    outliers : anyOf(boolean, :class:`MarkConfig`)

    rule : anyOf(boolean, :class:`MarkConfig`)

    size : float
        Size of the box and median tick of a box plot
    ticks : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/BoxPlotDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, box=Undefined, clip=Undefined, color=Undefined, extent=Undefined,
                 median=Undefined, opacity=Undefined, orient=Undefined, outliers=Undefined,
                 rule=Undefined, size=Undefined, ticks=Undefined, **kwds):
        super(BoxPlotDef, self).__init__(type=type, box=box, clip=clip, color=color, extent=extent,
                                         median=median, opacity=opacity, orient=orient,
                                         outliers=outliers, rule=rule, size=size, ticks=ticks, **kwds)


class CompositionConfig(VegaLiteSchema):
    """CompositionConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    spacing : float
        The default spacing in pixels between composed sub-views.

        **Default value** : ``20``
    """
    _schema = {'$ref': '#/definitions/CompositionConfig'}
    _rootschema = Root._schema

    def __init__(self, columns=Undefined, spacing=Undefined, **kwds):
        super(CompositionConfig, self).__init__(columns=columns, spacing=spacing, **kwds)


class ConditionalAxisColor(VegaLiteSchema):
    """ConditionalAxisColor schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefColornull`,
    List(:class:`ConditionalPredicateValueDefColornull`))

    value : anyOf(:class:`Color`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisColor'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisColor, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisLabelBaseline(VegaLiteSchema):
    """ConditionalAxisLabelBaseline schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefTextBaselinenull`,
    List(:class:`ConditionalPredicateValueDefTextBaselinenull`))

    value : anyOf(:class:`TextBaseline`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisLabelBaseline'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisLabelBaseline, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisLabelFontStyle(VegaLiteSchema):
    """ConditionalAxisLabelFontStyle schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefFontStylenull`,
    List(:class:`ConditionalPredicateValueDefFontStylenull`))

    value : anyOf(:class:`FontStyle`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisLabelFontStyle'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisLabelFontStyle, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisLabelFontWeight(VegaLiteSchema):
    """ConditionalAxisLabelFontWeight schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefFontWeightnull`,
    List(:class:`ConditionalPredicateValueDefFontWeightnull`))

    value : anyOf(:class:`FontWeight`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisLabelFontWeight'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisLabelFontWeight, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisNumber(VegaLiteSchema):
    """ConditionalAxisNumber schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefnumbernull`,
    List(:class:`ConditionalPredicateValueDefnumbernull`))

    value : anyOf(float, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisNumber'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisNumber, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisNumberArray(VegaLiteSchema):
    """ConditionalAxisNumberArray schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefnumbernull`,
    List(:class:`ConditionalPredicateValueDefnumbernull`))

    value : anyOf(List(float), None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisNumberArray'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisNumberArray, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisPropertyColornull(VegaLiteSchema):
    """ConditionalAxisPropertyColornull schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefColornull`,
    List(:class:`ConditionalPredicateValueDefColornull`))

    value : anyOf(:class:`Color`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisProperty<(Color|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisPropertyColornull, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisPropertyFontStylenull(VegaLiteSchema):
    """ConditionalAxisPropertyFontStylenull schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefFontStylenull`,
    List(:class:`ConditionalPredicateValueDefFontStylenull`))

    value : anyOf(:class:`FontStyle`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisProperty<(FontStyle|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisPropertyFontStylenull, self).__init__(condition=condition, value=value,
                                                                   **kwds)


class ConditionalAxisPropertyFontWeightnull(VegaLiteSchema):
    """ConditionalAxisPropertyFontWeightnull schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefFontWeightnull`,
    List(:class:`ConditionalPredicateValueDefFontWeightnull`))

    value : anyOf(:class:`FontWeight`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisProperty<(FontWeight|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisPropertyFontWeightnull, self).__init__(condition=condition, value=value,
                                                                    **kwds)


class ConditionalAxisPropertyTextBaselinenull(VegaLiteSchema):
    """ConditionalAxisPropertyTextBaselinenull schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefTextBaselinenull`,
    List(:class:`ConditionalPredicateValueDefTextBaselinenull`))

    value : anyOf(:class:`TextBaseline`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisProperty<(TextBaseline|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisPropertyTextBaselinenull, self).__init__(condition=condition, value=value,
                                                                      **kwds)


class ConditionalAxisPropertynumbernull(VegaLiteSchema):
    """ConditionalAxisPropertynumbernull schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateValueDefnumbernull`,
    List(:class:`ConditionalPredicateValueDefnumbernull`))

    value : anyOf(float, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisProperty<(number|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisPropertynumbernull, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisPropertystringnull(VegaLiteSchema):
    """ConditionalAxisPropertystringnull schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateStringValueDef`,
    List(:class:`ConditionalPredicateStringValueDef`))

    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisProperty<(string|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisPropertystringnull, self).__init__(condition=condition, value=value, **kwds)


class ConditionalAxisString(VegaLiteSchema):
    """ConditionalAxisString schema wrapper

    Mapping(required=[condition, value])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalPredicateStringValueDef`,
    List(:class:`ConditionalPredicateStringValueDef`))

    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalAxisString'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ConditionalAxisString, self).__init__(condition=condition, value=value, **kwds)


class ConditionalMarkPropFieldDef(VegaLiteSchema):
    """ConditionalMarkPropFieldDef schema wrapper

    anyOf(:class:`ConditionalPredicateMarkPropFieldDef`,
    :class:`ConditionalSelectionMarkPropFieldDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalMarkPropFieldDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDef, self).__init__(*args, **kwds)


class ConditionalMarkPropFieldDefTypeForShape(VegaLiteSchema):
    """ConditionalMarkPropFieldDefTypeForShape schema wrapper

    anyOf(:class:`ConditionalPredicateMarkPropFieldDefTypeForShape`,
    :class:`ConditionalSelectionMarkPropFieldDefTypeForShape`)
    """
    _schema = {'$ref': '#/definitions/ConditionalMarkPropFieldDef<TypeForShape>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDefTypeForShape, self).__init__(*args, **kwds)


class ConditionalNumberValueDef(VegaLiteSchema):
    """ConditionalNumberValueDef schema wrapper

    anyOf(:class:`ConditionalPredicateNumberValueDef`,
    :class:`ConditionalSelectionNumberValueDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalNumberValueDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalNumberValueDef, self).__init__(*args, **kwds)


class ConditionalPredicateMarkPropFieldDef(ConditionalMarkPropFieldDef):
    """ConditionalPredicateMarkPropFieldDef schema wrapper

    Mapping(required=[test, type])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
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


class ConditionalPredicateMarkPropFieldDefTypeForShape(ConditionalMarkPropFieldDefTypeForShape):
    """ConditionalPredicateMarkPropFieldDefTypeForShape schema wrapper

    Mapping(required=[test, type])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    type : :class:`TypeForShape`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef<TypeForShape>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(ConditionalPredicateMarkPropFieldDefTypeForShape, self).__init__(test=test, type=type,
                                                                               aggregate=aggregate,
                                                                               bin=bin, field=field,
                                                                               legend=legend,
                                                                               scale=scale, sort=sort,
                                                                               timeUnit=timeUnit,
                                                                               title=title, **kwds)


class ConditionalPredicateNumberValueDef(ConditionalNumberValueDef):
    """ConditionalPredicateNumberValueDef schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<NumberValueDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateNumberValueDef, self).__init__(test=test, value=value, **kwds)


class ConditionalPredicateValueDefColornull(VegaLiteSchema):
    """ConditionalPredicateValueDefColornull schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(:class:`Color`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<(Color|null)>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefColornull, self).__init__(test=test, value=value, **kwds)


class ConditionalPredicateValueDefFontStylenull(VegaLiteSchema):
    """ConditionalPredicateValueDefFontStylenull schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(:class:`FontStyle`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<(FontStyle|null)>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefFontStylenull, self).__init__(test=test, value=value, **kwds)


class ConditionalPredicateValueDefFontWeightnull(VegaLiteSchema):
    """ConditionalPredicateValueDefFontWeightnull schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(:class:`FontWeight`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<(FontWeight|null)>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefFontWeightnull, self).__init__(test=test, value=value, **kwds)


class ConditionalPredicateValueDefTextBaselinenull(VegaLiteSchema):
    """ConditionalPredicateValueDefTextBaselinenull schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(:class:`TextBaseline`, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<(TextBaseline|null)>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefTextBaselinenull, self).__init__(test=test, value=value,
                                                                           **kwds)


class ConditionalPredicateValueDefnumbernull(VegaLiteSchema):
    """ConditionalPredicateValueDefnumbernull schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(float, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<(number|null)>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefnumbernull, self).__init__(test=test, value=value, **kwds)


class ConditionalSelectionMarkPropFieldDef(ConditionalMarkPropFieldDef):
    """ConditionalSelectionMarkPropFieldDef schema wrapper

    Mapping(required=[selection, type])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
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


class ConditionalSelectionMarkPropFieldDefTypeForShape(ConditionalMarkPropFieldDefTypeForShape):
    """ConditionalSelectionMarkPropFieldDefTypeForShape schema wrapper

    Mapping(required=[selection, type])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    type : :class:`TypeForShape`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef<TypeForShape>>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(ConditionalSelectionMarkPropFieldDefTypeForShape, self).__init__(selection=selection,
                                                                               type=type,
                                                                               aggregate=aggregate,
                                                                               bin=bin, field=field,
                                                                               legend=legend,
                                                                               scale=scale, sort=sort,
                                                                               timeUnit=timeUnit,
                                                                               title=title, **kwds)


class ConditionalSelectionNumberValueDef(ConditionalNumberValueDef):
    """ConditionalSelectionNumberValueDef schema wrapper

    Mapping(required=[selection, value])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<NumberValueDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionNumberValueDef, self).__init__(selection=selection, value=value,
                                                                 **kwds)


class ConditionalStringFieldDef(VegaLiteSchema):
    """ConditionalStringFieldDef schema wrapper

    anyOf(:class:`ConditionalPredicateStringFieldDef`,
    :class:`ConditionalSelectionStringFieldDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalStringFieldDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalStringFieldDef, self).__init__(*args, **kwds)


class ConditionalPredicateStringFieldDef(ConditionalStringFieldDef):
    """ConditionalPredicateStringFieldDef schema wrapper

    Mapping(required=[test, type])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<StringFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, format=Undefined, formatType=Undefined, labelExpr=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(ConditionalPredicateStringFieldDef, self).__init__(test=test, type=type,
                                                                 aggregate=aggregate, bin=bin,
                                                                 field=field, format=format,
                                                                 formatType=formatType,
                                                                 labelExpr=labelExpr, timeUnit=timeUnit,
                                                                 title=title, **kwds)


class ConditionalSelectionStringFieldDef(ConditionalStringFieldDef):
    """ConditionalSelectionStringFieldDef schema wrapper

    Mapping(required=[selection, type])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<StringFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined,
                 field=Undefined, format=Undefined, formatType=Undefined, labelExpr=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(ConditionalSelectionStringFieldDef, self).__init__(selection=selection, type=type,
                                                                 aggregate=aggregate, bin=bin,
                                                                 field=field, format=format,
                                                                 formatType=formatType,
                                                                 labelExpr=labelExpr, timeUnit=timeUnit,
                                                                 title=title, **kwds)


class ConditionalStringValueDef(VegaLiteSchema):
    """ConditionalStringValueDef schema wrapper

    anyOf(:class:`ConditionalPredicateStringValueDef`,
    :class:`ConditionalSelectionStringValueDef`)
    """
    _schema = {'$ref': '#/definitions/ConditionalStringValueDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalStringValueDef, self).__init__(*args, **kwds)


class ConditionalPredicateStringValueDef(ConditionalStringValueDef):
    """ConditionalPredicateStringValueDef schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<StringValueDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateStringValueDef, self).__init__(test=test, value=value, **kwds)


class ConditionalSelectionStringValueDef(ConditionalStringValueDef):
    """ConditionalSelectionStringValueDef schema wrapper

    Mapping(required=[selection, value])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<StringValueDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionStringValueDef, self).__init__(selection=selection, value=value,
                                                                 **kwds)


class ConditionalValueDefGradientstringnull(VegaLiteSchema):
    """ConditionalValueDefGradientstringnull schema wrapper

    anyOf(:class:`ConditionalPredicateValueDefGradientstringnull`,
    :class:`ConditionalSelectionValueDefGradientstringnull`)
    """
    _schema = {'$ref': '#/definitions/ConditionalValueDef<(Gradient|string|null)>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalValueDefGradientstringnull, self).__init__(*args, **kwds)


class ConditionalPredicateValueDefGradientstringnull(ConditionalValueDefGradientstringnull):
    """ConditionalPredicateValueDefGradientstringnull schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : anyOf(:class:`Gradient`, string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<(Gradient|string|null)>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefGradientstringnull, self).__init__(test=test, value=value,
                                                                             **kwds)


class ConditionalSelectionValueDefGradientstringnull(ConditionalValueDefGradientstringnull):
    """ConditionalSelectionValueDefGradientstringnull schema wrapper

    Mapping(required=[selection, value])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    value : anyOf(:class:`Gradient`, string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef<(Gradient|string|null)>>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionValueDefGradientstringnull, self).__init__(selection=selection,
                                                                             value=value, **kwds)


class ConditionalValueDefText(VegaLiteSchema):
    """ConditionalValueDefText schema wrapper

    anyOf(:class:`ConditionalPredicateValueDefText`, :class:`ConditionalSelectionValueDefText`)
    """
    _schema = {'$ref': '#/definitions/ConditionalValueDef<Text>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalValueDefText, self).__init__(*args, **kwds)


class ConditionalPredicateValueDefText(ConditionalValueDefText):
    """ConditionalPredicateValueDefText schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : :class:`Text`
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<Text>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefText, self).__init__(test=test, value=value, **kwds)


class ConditionalSelectionValueDefText(ConditionalValueDefText):
    """ConditionalSelectionValueDefText schema wrapper

    Mapping(required=[selection, value])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    value : :class:`Text`
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef<Text>>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionValueDefText, self).__init__(selection=selection, value=value, **kwds)


class ConditionalValueDefstring(VegaLiteSchema):
    """ConditionalValueDefstring schema wrapper

    anyOf(:class:`ConditionalPredicateValueDefstring`,
    :class:`ConditionalSelectionValueDefstring`)
    """
    _schema = {'$ref': '#/definitions/ConditionalValueDef<string>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalValueDefstring, self).__init__(*args, **kwds)


class ConditionalPredicateValueDefstring(ConditionalValueDefstring):
    """ConditionalPredicateValueDefstring schema wrapper

    Mapping(required=[test, value])

    Attributes
    ----------

    test : :class:`LogicalOperandPredicate`
        Predicate for triggering the condition
    value : string
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef<string>>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDefstring, self).__init__(test=test, value=value, **kwds)


class ConditionalSelectionValueDefstring(ConditionalValueDefstring):
    """ConditionalSelectionValueDefstring schema wrapper

    Mapping(required=[selection, value])

    Attributes
    ----------

    selection : :class:`SelectionOperand`
        A `selection name <https://vega.github.io/vega-lite/docs/selection.html>`__, or a
        series of `composed selections
        <https://vega.github.io/vega-lite/docs/selection.html#compose>`__.
    value : string
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef<string>>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionValueDefstring, self).__init__(selection=selection, value=value,
                                                                 **kwds)


class Config(VegaLiteSchema):
    """Config schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    area : :class:`AreaConfig`
        Area-Specific Config
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    axis : :class:`AxisConfig`
        Axis configuration, which determines default properties for all ``x`` and ``y``
        `axes <https://vega.github.io/vega-lite/docs/axis.html>`__. For a full list of axis
        configuration options, please see the `corresponding section of the axis
        documentation <https://vega.github.io/vega-lite/docs/axis.html#config>`__.
    axisBand : :class:`AxisConfig`
        Specific axis config for axes with "band" scales.
    axisBottom : :class:`AxisConfig`
        Specific axis config for x-axis along the bottom edge of the chart.
    axisLeft : :class:`AxisConfig`
        Specific axis config for y-axis along the left edge of the chart.
    axisRight : :class:`AxisConfig`
        Specific axis config for y-axis along the right edge of the chart.
    axisTop : :class:`AxisConfig`
        Specific axis config for x-axis along the top edge of the chart.
    axisX : :class:`AxisConfig`
        X-axis specific config.
    axisY : :class:`AxisConfig`
        Y-axis specific config.
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
    bar : :class:`RectConfig`
        Bar-Specific Config
    boxplot : :class:`BoxPlotConfig`
        Box Config
    circle : :class:`MarkConfig`
        Circle-Specific Config
    concat : :class:`CompositionConfig`
        Default configuration for all concatenation view composition operators ( ``concat``,
        ``hconcat``, and ``vconcat`` )
    countTitle : string
        Default axis and legend title for count fields.

        **Default value:** ``'Count of Records``.
    errorband : :class:`ErrorBandConfig`
        ErrorBand Config
    errorbar : :class:`ErrorBarConfig`
        ErrorBar Config
    facet : :class:`CompositionConfig`
        Default configuration for the ``facet`` view composition operator
    fieldTitle : enum('verbal', 'functional', 'plain')
        Defines how Vega-Lite generates title for fields. There are three possible styles:


        * ``"verbal"`` (Default) - displays function in a verbal style (e.g., "Sum of
          field", "Year-month of date", "field (binned)").
        * ``"function"`` - displays function using parentheses and capitalized texts (e.g.,
          "SUM(field)", "YEARMONTH(date)", "BIN(field)").
        * ``"plain"`` - displays only the field name without functions (e.g., "field",
          "date", "field").
    geoshape : :class:`MarkConfig`
        Geoshape-Specific Config
    header : :class:`HeaderConfig`
        Header configuration, which determines default properties for all `headers
        <https://vega.github.io/vega-lite/docs/header.html>`__.

        For a full list of header configuration options, please see the `corresponding
        section of in the header documentation
        <https://vega.github.io/vega-lite/docs/header.html#config>`__.
    headerColumn : :class:`HeaderConfig`
        Header configuration, which determines default properties for column `headers
        <https://vega.github.io/vega-lite/docs/header.html>`__.

        For a full list of header configuration options, please see the `corresponding
        section of in the header documentation
        <https://vega.github.io/vega-lite/docs/header.html#config>`__.
    headerFacet : :class:`HeaderConfig`
        Header configuration, which determines default properties for non-row/column facet
        `headers <https://vega.github.io/vega-lite/docs/header.html>`__.

        For a full list of header configuration options, please see the `corresponding
        section of in the header documentation
        <https://vega.github.io/vega-lite/docs/header.html#config>`__.
    headerRow : :class:`HeaderConfig`
        Header configuration, which determines default properties for row `headers
        <https://vega.github.io/vega-lite/docs/header.html>`__.

        For a full list of header configuration options, please see the `corresponding
        section of in the header documentation
        <https://vega.github.io/vega-lite/docs/header.html#config>`__.
    image : :class:`RectConfig`
        Image-specific Config
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
        D3 Number format for guide labels and text marks. For example "s" for SI units. Use
        `D3's number format pattern <https://github.com/d3/d3-format#locale_format>`__.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle. If a number, specifies padding for all sides.
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
    rect : :class:`RectConfig`
        Rect-Specific Config
    repeat : :class:`CompositionConfig`
        Default configuration for the ``repeat`` view composition operator
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
    style : :class:`StyleConfigIndex`
        An object hash that defines key-value mappings to determine default properties for
        marks with a given `style
        <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__. The keys represent
        styles names; the values have to be valid `mark configuration objects
        <https://vega.github.io/vega-lite/docs/mark.html#config>`__.
    text : :class:`MarkConfig`
        Text-Specific Config
    tick : :class:`TickConfig`
        Tick-Specific Config
    timeFormat : string
        Default time format for raw time values (without time units) in text marks, legend
        labels and header labels.

        **Default value:** ``"%b %d, %Y"``
        **Note:** Axes automatically determine format each label automatically so this
        config would not affect axes.
    title : :class:`TitleConfig`
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
                 boxplot=Undefined, circle=Undefined, concat=Undefined, countTitle=Undefined,
                 errorband=Undefined, errorbar=Undefined, facet=Undefined, fieldTitle=Undefined,
                 geoshape=Undefined, header=Undefined, headerColumn=Undefined, headerFacet=Undefined,
                 headerRow=Undefined, image=Undefined, legend=Undefined, line=Undefined, mark=Undefined,
                 numberFormat=Undefined, padding=Undefined, point=Undefined, projection=Undefined,
                 range=Undefined, rect=Undefined, repeat=Undefined, rule=Undefined, scale=Undefined,
                 selection=Undefined, square=Undefined, style=Undefined, text=Undefined, tick=Undefined,
                 timeFormat=Undefined, title=Undefined, trail=Undefined, view=Undefined, **kwds):
        super(Config, self).__init__(area=area, autosize=autosize, axis=axis, axisBand=axisBand,
                                     axisBottom=axisBottom, axisLeft=axisLeft, axisRight=axisRight,
                                     axisTop=axisTop, axisX=axisX, axisY=axisY, background=background,
                                     bar=bar, boxplot=boxplot, circle=circle, concat=concat,
                                     countTitle=countTitle, errorband=errorband, errorbar=errorbar,
                                     facet=facet, fieldTitle=fieldTitle, geoshape=geoshape,
                                     header=header, headerColumn=headerColumn, headerFacet=headerFacet,
                                     headerRow=headerRow, image=image, legend=legend, line=line,
                                     mark=mark, numberFormat=numberFormat, padding=padding, point=point,
                                     projection=projection, range=range, rect=rect, repeat=repeat,
                                     rule=rule, scale=scale, selection=selection, square=square,
                                     style=style, text=text, tick=tick, timeFormat=timeFormat,
                                     title=title, trail=trail, view=view, **kwds)


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


class Cyclical(ColorScheme):
    """Cyclical schema wrapper

    enum('rainbow', 'sinebow')
    """
    _schema = {'$ref': '#/definitions/Cyclical'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Cyclical, self).__init__(*args)


class Data(VegaLiteSchema):
    """Data schema wrapper

    anyOf(:class:`DataSource`, :class:`Generator`)
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


class CsvDataFormat(DataFormat):
    """CsvDataFormat schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    parse : anyOf(:class:`Parse`, None)
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
        For Specific date formats can be provided (e.g., ``{foo: "date:'%m%d%Y'"}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: "utc:'%m%d%Y'"}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    type : enum('csv', 'tsv')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.

        **Default value:**  The default format type is determined by the extension of the
        file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/CsvDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, type=Undefined, **kwds):
        super(CsvDataFormat, self).__init__(parse=parse, type=type, **kwds)


class DataSource(Data):
    """DataSource schema wrapper

    anyOf(:class:`UrlData`, :class:`InlineData`, :class:`NamedData`)
    """
    _schema = {'$ref': '#/definitions/DataSource'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(DataSource, self).__init__(*args, **kwds)


class Datasets(VegaLiteSchema):
    """Datasets schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/Datasets'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(Datasets, self).__init__(**kwds)


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


class DictSelectionInit(VegaLiteSchema):
    """DictSelectionInit schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/Dict<SelectionInit>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(DictSelectionInit, self).__init__(**kwds)


class DictSelectionInitInterval(VegaLiteSchema):
    """DictSelectionInitInterval schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/Dict<SelectionInitInterval>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(DictSelectionInitInterval, self).__init__(**kwds)


class Dir(VegaLiteSchema):
    """Dir schema wrapper

    enum('ltr', 'rtl')
    """
    _schema = {'$ref': '#/definitions/Dir'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Dir, self).__init__(*args)


class Diverging(ColorScheme):
    """Diverging schema wrapper

    enum('blueorange', 'blueorange-3', 'blueorange-4', 'blueorange-5', 'blueorange-6',
    'blueorange-7', 'blueorange-8', 'blueorange-9', 'blueorange-10', 'blueorange-11',
    'brownbluegreen', 'brownbluegreen-3', 'brownbluegreen-4', 'brownbluegreen-5',
    'brownbluegreen-6', 'brownbluegreen-7', 'brownbluegreen-8', 'brownbluegreen-9',
    'brownbluegreen-10', 'brownbluegreen-11', 'purplegreen', 'purplegreen-3', 'purplegreen-4',
    'purplegreen-5', 'purplegreen-6', 'purplegreen-7', 'purplegreen-8', 'purplegreen-9',
    'purplegreen-10', 'purplegreen-11', 'pinkyellowgreen', 'pinkyellowgreen-3',
    'pinkyellowgreen-4', 'pinkyellowgreen-5', 'pinkyellowgreen-6', 'pinkyellowgreen-7',
    'pinkyellowgreen-8', 'pinkyellowgreen-9', 'pinkyellowgreen-10', 'pinkyellowgreen-11',
    'purpleorange', 'purpleorange-3', 'purpleorange-4', 'purpleorange-5', 'purpleorange-6',
    'purpleorange-7', 'purpleorange-8', 'purpleorange-9', 'purpleorange-10', 'purpleorange-11',
    'redblue', 'redblue-3', 'redblue-4', 'redblue-5', 'redblue-6', 'redblue-7', 'redblue-8',
    'redblue-9', 'redblue-10', 'redblue-11', 'redgrey', 'redgrey-3', 'redgrey-4', 'redgrey-5',
    'redgrey-6', 'redgrey-7', 'redgrey-8', 'redgrey-9', 'redgrey-10', 'redgrey-11',
    'redyellowblue', 'redyellowblue-3', 'redyellowblue-4', 'redyellowblue-5', 'redyellowblue-6',
    'redyellowblue-7', 'redyellowblue-8', 'redyellowblue-9', 'redyellowblue-10',
    'redyellowblue-11', 'redyellowgreen', 'redyellowgreen-3', 'redyellowgreen-4',
    'redyellowgreen-5', 'redyellowgreen-6', 'redyellowgreen-7', 'redyellowgreen-8',
    'redyellowgreen-9', 'redyellowgreen-10', 'redyellowgreen-11', 'spectral', 'spectral-3',
    'spectral-4', 'spectral-5', 'spectral-6', 'spectral-7', 'spectral-8', 'spectral-9',
    'spectral-10', 'spectral-11')
    """
    _schema = {'$ref': '#/definitions/Diverging'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Diverging, self).__init__(*args)


class DsvDataFormat(DataFormat):
    """DsvDataFormat schema wrapper

    Mapping(required=[delimiter])

    Attributes
    ----------

    delimiter : string
        The delimiter between records. The delimiter must be a single character (i.e., a
        single 16-bit code unit); so, ASCII delimiters are fine, but emoji delimiters are
        not.
    parse : anyOf(:class:`Parse`, None)
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
        For Specific date formats can be provided (e.g., ``{foo: "date:'%m%d%Y'"}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: "utc:'%m%d%Y'"}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    type : enum('dsv')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.

        **Default value:**  The default format type is determined by the extension of the
        file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/DsvDataFormat'}
    _rootschema = Root._schema

    def __init__(self, delimiter=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(DsvDataFormat, self).__init__(delimiter=delimiter, parse=parse, type=type, **kwds)


class Element(VegaLiteSchema):
    """Element schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/Element'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Element, self).__init__(*args)


class Encoding(VegaLiteSchema):
    """Encoding schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : anyOf(:class:`ColorGradientFieldDefWithCondition`,
    :class:`ColorGradientValueDefWithCondition`)
        Color of the marks – either fill or stroke color based on  the ``filled`` property
        of mark definition.
        By default, ``color`` represents fill color for ``"area"``, ``"bar"``, ``"tick"``,
        ``"text"``, ``"trail"``, ``"circle"``, and ``"square"`` / stroke color for
        ``"line"`` and ``"point"``.

        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:*
        1) For fine-grained control over both fill and stroke colors of the marks, please
        use the ``fill`` and ``stroke`` channels. The ``fill`` or ``stroke`` encodings have
        higher precedence than ``color``, thus may override the ``color`` encoding if
        conflicting encodings are specified.
        2) See the scale documentation for more information about customizing `color scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__.
    detail : anyOf(:class:`FieldDefWithoutScale`, List(:class:`FieldDefWithoutScale`))
        Additional levels of detail for grouping data in aggregate views and
        in line, trail, and area marks without mapping data to a specific visual channel.
    fill : anyOf(:class:`ColorGradientFieldDefWithCondition`,
    :class:`ColorGradientValueDefWithCondition`)
        Fill color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* The ``fill`` encoding has higher precedence than ``color``, thus may
        override the ``color`` encoding if conflicting encodings are specified.
    fillOpacity : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Fill opacity of the marks.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``fillOpacity``
        property.
    href : anyOf(:class:`StringFieldDefWithCondition`, :class:`StringValueDefWithCondition`)
        A URL to load upon mouse click.
    key : :class:`FieldDefWithoutScale`
        A data field to use as a unique key for data binding. When a visualization’s data is
        updated, the key value will be used to match data elements to existing mark
        instances. Use a key channel to enable object constancy for transitions over dynamic
        data.
    latitude : anyOf(:class:`LatLongFieldDef`, :class:`NumberValueDef`)
        Latitude position of geographically projected marks.
    latitude2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Latitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    longitude : anyOf(:class:`LatLongFieldDef`, :class:`NumberValueDef`)
        Longitude position of geographically projected marks.
    longitude2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Longitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    opacity : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Opacity of the marks.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``opacity`` property.
    order : anyOf(:class:`OrderFieldDef`, List(:class:`OrderFieldDef`), :class:`NumberValueDef`)
        Order of the marks.


        * For stacked marks, this ``order`` channel encodes `stack order
          <https://vega.github.io/vega-lite/docs/stack.html#order>`__.
        * For line and trail marks, this ``order`` channel encodes order of data points in
          the lines. This can be useful for creating `a connected scatterplot
          <https://vega.github.io/vega-lite/examples/connected_scatterplot.html>`__. Setting
          ``order`` to ``{"value": null}`` makes the line marks use the original order in
          the data sources.
        * Otherwise, this ``order`` channel encodes layer order of the marks.

        **Note** : In aggregate plots, ``order`` field should be ``aggregate`` d to avoid
        creating additional aggregation grouping.
    shape : anyOf(:class:`ShapeFieldDefWithCondition`, :class:`ShapeValueDefWithCondition`)
        Shape of the mark.


        #.
        For ``point`` marks the supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
        ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
        ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
        <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
        sizing, custom shape paths should be defined within a square bounding box with
        coordinates ranging from -1 to 1 along both the x and y dimensions.)

        #.
        For ``geoshape`` marks it should be a field definition of the geojson data

        **Default value:** If undefined, the default shape depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#point-config>`__ 's ``shape``
        property. ( ``"circle"`` if unset.)
    size : anyOf(:class:`NumericFieldDefWithCondition`, :class:`NumericValueDefWithCondition`)
        Size of the mark.


        * For ``"point"``, ``"square"`` and ``"circle"``, – the symbol size, or pixel area
          of the mark.
        * For ``"bar"`` and ``"tick"`` – the bar and tick's size.
        * For ``"text"`` – the text's font size.
        * Size is unsupported for ``"line"``, ``"area"``, and ``"rect"``. (Use ``"trail"``
          instead of line with varying size)
    stroke : anyOf(:class:`ColorGradientFieldDefWithCondition`,
    :class:`ColorGradientValueDefWithCondition`)
        Stroke color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* The ``stroke`` encoding has higher precedence than ``color``, thus may
        override the ``color`` encoding if conflicting encodings are specified.
    strokeOpacity : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Stroke opacity of the marks.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``strokeOpacity``
        property.
    strokeWidth : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Stroke width of the marks.

        **Default value:** If undefined, the default stroke width depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``strokeWidth``
        property.
    text : anyOf(:class:`TextFieldDefWithCondition`, :class:`TextValueDefWithCondition`)
        Text of the ``text`` mark.
    tooltip : anyOf(:class:`StringFieldDefWithCondition`, :class:`StringValueDefWithCondition`,
    List(:class:`StringFieldDef`), None)
        The tooltip text to show upon mouse hover. Specifying ``tooltip`` encoding overrides
        `the tooltip property in the mark definition
        <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip in Vega-Lite.
    url : anyOf(:class:`StringFieldDefWithCondition`, :class:`StringValueDefWithCondition`)
        The URL of an image mark.
    x : anyOf(:class:`PositionFieldDef`, :class:`XValueDef`)
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(:class:`SecondaryFieldDef`, :class:`XValueDef`)
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    xError : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Error value of x coordinates for error specified ``"errorbar"`` and ``"errorband"``.
    xError2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Secondary error value of x coordinates for error specified ``"errorbar"`` and
        ``"errorband"``.
    y : anyOf(:class:`PositionFieldDef`, :class:`YValueDef`)
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(:class:`SecondaryFieldDef`, :class:`YValueDef`)
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    yError : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Error value of y coordinates for error specified ``"errorbar"`` and ``"errorband"``.
    yError2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Secondary error value of y coordinates for error specified ``"errorbar"`` and
        ``"errorband"``.
    """
    _schema = {'$ref': '#/definitions/Encoding'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, detail=Undefined, fill=Undefined, fillOpacity=Undefined,
                 href=Undefined, key=Undefined, latitude=Undefined, latitude2=Undefined,
                 longitude=Undefined, longitude2=Undefined, opacity=Undefined, order=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, text=Undefined, tooltip=Undefined, url=Undefined, x=Undefined,
                 x2=Undefined, xError=Undefined, xError2=Undefined, y=Undefined, y2=Undefined,
                 yError=Undefined, yError2=Undefined, **kwds):
        super(Encoding, self).__init__(color=color, detail=detail, fill=fill, fillOpacity=fillOpacity,
                                       href=href, key=key, latitude=latitude, latitude2=latitude2,
                                       longitude=longitude, longitude2=longitude2, opacity=opacity,
                                       order=order, shape=shape, size=size, stroke=stroke,
                                       strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, text=text,
                                       tooltip=tooltip, url=url, x=x, x2=x2, xError=xError,
                                       xError2=xError2, y=y, y2=y2, yError=yError, yError2=yError2,
                                       **kwds)


class ErrorBand(CompositeMark):
    """ErrorBand schema wrapper

    enum('errorband')
    """
    _schema = {'$ref': '#/definitions/ErrorBand'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ErrorBand, self).__init__(*args)


class ErrorBandConfig(VegaLiteSchema):
    """ErrorBandConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    band : anyOf(boolean, :class:`MarkConfig`)

    borders : anyOf(boolean, :class:`MarkConfig`)

    extent : :class:`ErrorBarExtent`
        The extent of the band. Available options include:


        * ``"ci"`` : Extend the band to the confidence interval of the mean.
        * ``"stderr"`` : The size of band are set to the value of standard error, extending
          from the mean.
        * ``"stdev"`` : The size of band are set to the value of standard deviation,
          extending from the mean.
        * ``"iqr"`` : Extend the band to the q1 and q3.

        **Default value:** ``"stderr"``.
    interpolate : :class:`Interpolate`
        The line interpolation method for the error band. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : a piecewise constant function (a step function) consisting of
          alternating horizontal and vertical lines. The y-value changes at the midpoint of
          each pair of adjacent x-values.
        * ``"step-before"`` : a piecewise constant function (a step function) consisting of
          alternating horizontal and vertical lines. The y-value changes before the x-value.
        * ``"step-after"`` : a piecewise constant function (a step function) consisting of
          alternating horizontal and vertical lines. The y-value changes after the x-value.
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
    tension : float
        The tension parameter for the interpolation type of the error band.
    """
    _schema = {'$ref': '#/definitions/ErrorBandConfig'}
    _rootschema = Root._schema

    def __init__(self, band=Undefined, borders=Undefined, extent=Undefined, interpolate=Undefined,
                 tension=Undefined, **kwds):
        super(ErrorBandConfig, self).__init__(band=band, borders=borders, extent=extent,
                                              interpolate=interpolate, tension=tension, **kwds)


class ErrorBandDef(CompositeMarkDef):
    """ErrorBandDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`ErrorBand`
        The mark type. This could a primitive mark type
        (one of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"geoshape"``, ``"rule"``, and ``"text"`` )
        or a composite mark type ( ``"boxplot"``, ``"errorband"``, ``"errorbar"`` ).
    band : anyOf(boolean, :class:`MarkConfig`)

    borders : anyOf(boolean, :class:`MarkConfig`)

    clip : boolean
        Whether a composite mark be clipped to the enclosing group’s width and height.
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    extent : :class:`ErrorBarExtent`
        The extent of the band. Available options include:


        * ``"ci"`` : Extend the band to the confidence interval of the mean.
        * ``"stderr"`` : The size of band are set to the value of standard error, extending
          from the mean.
        * ``"stdev"`` : The size of band are set to the value of standard deviation,
          extending from the mean.
        * ``"iqr"`` : Extend the band to the q1 and q3.

        **Default value:** ``"stderr"``.
    interpolate : :class:`Interpolate`
        The line interpolation method for the error band. One of the following:


        * ``"linear"`` : piecewise linear segments, as in a polyline.
        * ``"linear-closed"`` : close the linear segments to form a polygon.
        * ``"step"`` : a piecewise constant function (a step function) consisting of
          alternating horizontal and vertical lines. The y-value changes at the midpoint of
          each pair of adjacent x-values.
        * ``"step-before"`` : a piecewise constant function (a step function) consisting of
          alternating horizontal and vertical lines. The y-value changes before the x-value.
        * ``"step-after"`` : a piecewise constant function (a step function) consisting of
          alternating horizontal and vertical lines. The y-value changes after the x-value.
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
    opacity : float
        The opacity (value between [0,1]) of the mark.
    orient : :class:`Orientation`
        Orientation of the error band. This is normally automatically determined, but can be
        specified when the orientation is ambiguous and cannot be automatically determined.
    tension : float
        The tension parameter for the interpolation type of the error band.
    """
    _schema = {'$ref': '#/definitions/ErrorBandDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, band=Undefined, borders=Undefined, clip=Undefined,
                 color=Undefined, extent=Undefined, interpolate=Undefined, opacity=Undefined,
                 orient=Undefined, tension=Undefined, **kwds):
        super(ErrorBandDef, self).__init__(type=type, band=band, borders=borders, clip=clip,
                                           color=color, extent=extent, interpolate=interpolate,
                                           opacity=opacity, orient=orient, tension=tension, **kwds)


class ErrorBar(CompositeMark):
    """ErrorBar schema wrapper

    enum('errorbar')
    """
    _schema = {'$ref': '#/definitions/ErrorBar'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ErrorBar, self).__init__(*args)


class ErrorBarConfig(VegaLiteSchema):
    """ErrorBarConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    extent : :class:`ErrorBarExtent`
        The extent of the rule. Available options include:


        * ``"ci"`` : Extend the rule to the confidence interval of the mean.
        * ``"stderr"`` : The size of rule are set to the value of standard error, extending
          from the mean.
        * ``"stdev"`` : The size of rule are set to the value of standard deviation,
          extending from the mean.
        * ``"iqr"`` : Extend the rule to the q1 and q3.

        **Default value:** ``"stderr"``.
    rule : anyOf(boolean, :class:`MarkConfig`)

    ticks : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/ErrorBarConfig'}
    _rootschema = Root._schema

    def __init__(self, extent=Undefined, rule=Undefined, ticks=Undefined, **kwds):
        super(ErrorBarConfig, self).__init__(extent=extent, rule=rule, ticks=ticks, **kwds)


class ErrorBarDef(CompositeMarkDef):
    """ErrorBarDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`ErrorBar`
        The mark type. This could a primitive mark type
        (one of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"geoshape"``, ``"rule"``, and ``"text"`` )
        or a composite mark type ( ``"boxplot"``, ``"errorband"``, ``"errorbar"`` ).
    clip : boolean
        Whether a composite mark be clipped to the enclosing group’s width and height.
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    extent : :class:`ErrorBarExtent`
        The extent of the rule. Available options include:


        * ``"ci"`` : Extend the rule to the confidence interval of the mean.
        * ``"stderr"`` : The size of rule are set to the value of standard error, extending
          from the mean.
        * ``"stdev"`` : The size of rule are set to the value of standard deviation,
          extending from the mean.
        * ``"iqr"`` : Extend the rule to the q1 and q3.

        **Default value:** ``"stderr"``.
    opacity : float
        The opacity (value between [0,1]) of the mark.
    orient : :class:`Orientation`
        Orientation of the error bar. This is normally automatically determined, but can be
        specified when the orientation is ambiguous and cannot be automatically determined.
    rule : anyOf(boolean, :class:`MarkConfig`)

    ticks : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/ErrorBarDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clip=Undefined, color=Undefined, extent=Undefined,
                 opacity=Undefined, orient=Undefined, rule=Undefined, ticks=Undefined, **kwds):
        super(ErrorBarDef, self).__init__(type=type, clip=clip, color=color, extent=extent,
                                          opacity=opacity, orient=orient, rule=rule, ticks=ticks, **kwds)


class ErrorBarExtent(VegaLiteSchema):
    """ErrorBarExtent schema wrapper

    enum('ci', 'iqr', 'stderr', 'stdev')
    """
    _schema = {'$ref': '#/definitions/ErrorBarExtent'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ErrorBarExtent, self).__init__(*args)


class ExcludeMappedValueRefBaseTitle(VegaLiteSchema):
    """ExcludeMappedValueRefBaseTitle schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        Horizontal text alignment for title text. One of ``"left"``, ``"center"``, or
        ``"right"``.
    anchor : :class:`TitleAnchor`
        The anchor position for placing the title and subtitle text. One of ``"start"``,
        ``"middle"``, or ``"end"``. For example, with an orientation of top these anchor
        positions map to a left-, center-, or right-aligned title.
    angle : float
        Angle in degrees of title and subtitle text.
    baseline : :class:`TextBaseline`
        Vertical text baseline for title and subtitle text. One of ``"top"``, ``"middle"``,
        ``"bottom"``, or ``"alphabetic"``.
    color : anyOf(None, :class:`Color`)
        Text color for title text.
    dx : float
        Delta offset for title and subtitle text x-coordinate.
    dy : float
        Delta offset for title and subtitle text y-coordinate.
    font : string
        Font name for title text.
    fontSize : float
        Font size in pixels for title text.
    fontStyle : :class:`FontStyle`
        Font style for title text.
    fontWeight : :class:`FontWeight`
        Font weight for title text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    frame : anyOf(:class:`TitleFrame`, string)
        The reference frame for the anchor position, one of ``"bounds"`` (to anchor relative
        to the full bounding box) or ``"group"`` (to anchor relative to the group width or
        height).
    limit : float
        The maximum allowed length in pixels of title and subtitle text.
    lineHeight : float
        Line height in pixels for multi-line title text.
    offset : float
        The orthogonal offset in pixels by which to displace the title group from its
        position along the edge of the chart.
    orient : :class:`TitleOrient`
        Default title orientation ( ``"top"``, ``"bottom"``, ``"left"``, or ``"right"`` )
    subtitleColor : anyOf(None, :class:`Color`)
        Text color for subtitle text.
    subtitleFont : string
        Font name for subtitle text.
    subtitleFontSize : float
        Font size in pixels for subtitle text.
    subtitleFontStyle : :class:`FontStyle`
        Font style for subtitle text.
    subtitleFontWeight : :class:`FontWeight`
        Font weight for subtitle text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    subtitleLineHeight : float
        Line height in pixels for multi-line subtitle text.
    subtitlePadding : float
        The padding in pixels between title and subtitle text.
    """
    _schema = {'$ref': '#/definitions/ExcludeMappedValueRef<BaseTitle>'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, anchor=Undefined, angle=Undefined, baseline=Undefined,
                 color=Undefined, dx=Undefined, dy=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, frame=Undefined, limit=Undefined,
                 lineHeight=Undefined, offset=Undefined, orient=Undefined, subtitleColor=Undefined,
                 subtitleFont=Undefined, subtitleFontSize=Undefined, subtitleFontStyle=Undefined,
                 subtitleFontWeight=Undefined, subtitleLineHeight=Undefined, subtitlePadding=Undefined,
                 **kwds):
        super(ExcludeMappedValueRefBaseTitle, self).__init__(align=align, anchor=anchor, angle=angle,
                                                             baseline=baseline, color=color, dx=dx,
                                                             dy=dy, font=font, fontSize=fontSize,
                                                             fontStyle=fontStyle, fontWeight=fontWeight,
                                                             frame=frame, limit=limit,
                                                             lineHeight=lineHeight, offset=offset,
                                                             orient=orient, subtitleColor=subtitleColor,
                                                             subtitleFont=subtitleFont,
                                                             subtitleFontSize=subtitleFontSize,
                                                             subtitleFontStyle=subtitleFontStyle,
                                                             subtitleFontWeight=subtitleFontWeight,
                                                             subtitleLineHeight=subtitleLineHeight,
                                                             subtitlePadding=subtitlePadding, **kwds)


class Expr(VegaLiteSchema):
    """Expr schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/Expr'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Expr, self).__init__(*args)


class FacetEncodingFieldDef(VegaLiteSchema):
    """FacetEncodingFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    header : :class:`Header`
        An object defining properties of a facet's header.
    sort : anyOf(:class:`SortArray`, :class:`SortOrder`, :class:`EncodingSortField`, None)
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FacetEncodingFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, align=Undefined, bin=Undefined,
                 bounds=Undefined, center=Undefined, columns=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, spacing=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(FacetEncodingFieldDef, self).__init__(type=type, aggregate=aggregate, align=align,
                                                    bin=bin, bounds=bounds, center=center,
                                                    columns=columns, field=field, header=header,
                                                    sort=sort, spacing=spacing, timeUnit=timeUnit,
                                                    title=title, **kwds)


class FacetFieldDef(VegaLiteSchema):
    """FacetFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    header : :class:`Header`
        An object defining properties of a facet's header.
    sort : anyOf(:class:`SortArray`, :class:`SortOrder`, :class:`EncodingSortField`, None)
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
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

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
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
        A field definition for the horizontal facet of trellis plots.
    row : :class:`FacetFieldDef`
        A field definition for the vertical facet of trellis plots.
    """
    _schema = {'$ref': '#/definitions/FacetMapping'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(FacetMapping, self).__init__(column=column, row=row, **kwds)


class FacetedEncoding(VegaLiteSchema):
    """FacetedEncoding schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : anyOf(:class:`ColorGradientFieldDefWithCondition`,
    :class:`ColorGradientValueDefWithCondition`)
        Color of the marks – either fill or stroke color based on  the ``filled`` property
        of mark definition.
        By default, ``color`` represents fill color for ``"area"``, ``"bar"``, ``"tick"``,
        ``"text"``, ``"trail"``, ``"circle"``, and ``"square"`` / stroke color for
        ``"line"`` and ``"point"``.

        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:*
        1) For fine-grained control over both fill and stroke colors of the marks, please
        use the ``fill`` and ``stroke`` channels. The ``fill`` or ``stroke`` encodings have
        higher precedence than ``color``, thus may override the ``color`` encoding if
        conflicting encodings are specified.
        2) See the scale documentation for more information about customizing `color scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__.
    column : :class:`RowColumnEncodingFieldDef`
        A field definition for the horizontal facet of trellis plots.
    detail : anyOf(:class:`FieldDefWithoutScale`, List(:class:`FieldDefWithoutScale`))
        Additional levels of detail for grouping data in aggregate views and
        in line, trail, and area marks without mapping data to a specific visual channel.
    facet : :class:`FacetEncodingFieldDef`
        A field definition for the (flexible) facet of trellis plots.

        If either ``row`` or ``column`` is specified, this channel will be ignored.
    fill : anyOf(:class:`ColorGradientFieldDefWithCondition`,
    :class:`ColorGradientValueDefWithCondition`)
        Fill color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* The ``fill`` encoding has higher precedence than ``color``, thus may
        override the ``color`` encoding if conflicting encodings are specified.
    fillOpacity : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Fill opacity of the marks.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``fillOpacity``
        property.
    href : anyOf(:class:`StringFieldDefWithCondition`, :class:`StringValueDefWithCondition`)
        A URL to load upon mouse click.
    key : :class:`FieldDefWithoutScale`
        A data field to use as a unique key for data binding. When a visualization’s data is
        updated, the key value will be used to match data elements to existing mark
        instances. Use a key channel to enable object constancy for transitions over dynamic
        data.
    latitude : anyOf(:class:`LatLongFieldDef`, :class:`NumberValueDef`)
        Latitude position of geographically projected marks.
    latitude2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Latitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    longitude : anyOf(:class:`LatLongFieldDef`, :class:`NumberValueDef`)
        Longitude position of geographically projected marks.
    longitude2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Longitude-2 position for geographically projected ranged ``"area"``, ``"bar"``,
        ``"rect"``, and  ``"rule"``.
    opacity : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Opacity of the marks.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``opacity`` property.
    order : anyOf(:class:`OrderFieldDef`, List(:class:`OrderFieldDef`), :class:`NumberValueDef`)
        Order of the marks.


        * For stacked marks, this ``order`` channel encodes `stack order
          <https://vega.github.io/vega-lite/docs/stack.html#order>`__.
        * For line and trail marks, this ``order`` channel encodes order of data points in
          the lines. This can be useful for creating `a connected scatterplot
          <https://vega.github.io/vega-lite/examples/connected_scatterplot.html>`__. Setting
          ``order`` to ``{"value": null}`` makes the line marks use the original order in
          the data sources.
        * Otherwise, this ``order`` channel encodes layer order of the marks.

        **Note** : In aggregate plots, ``order`` field should be ``aggregate`` d to avoid
        creating additional aggregation grouping.
    row : :class:`RowColumnEncodingFieldDef`
        A field definition for the vertical facet of trellis plots.
    shape : anyOf(:class:`ShapeFieldDefWithCondition`, :class:`ShapeValueDefWithCondition`)
        Shape of the mark.


        #.
        For ``point`` marks the supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
        ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
        ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
        <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
        sizing, custom shape paths should be defined within a square bounding box with
        coordinates ranging from -1 to 1 along both the x and y dimensions.)

        #.
        For ``geoshape`` marks it should be a field definition of the geojson data

        **Default value:** If undefined, the default shape depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#point-config>`__ 's ``shape``
        property. ( ``"circle"`` if unset.)
    size : anyOf(:class:`NumericFieldDefWithCondition`, :class:`NumericValueDefWithCondition`)
        Size of the mark.


        * For ``"point"``, ``"square"`` and ``"circle"``, – the symbol size, or pixel area
          of the mark.
        * For ``"bar"`` and ``"tick"`` – the bar and tick's size.
        * For ``"text"`` – the text's font size.
        * Size is unsupported for ``"line"``, ``"area"``, and ``"rect"``. (Use ``"trail"``
          instead of line with varying size)
    stroke : anyOf(:class:`ColorGradientFieldDefWithCondition`,
    :class:`ColorGradientValueDefWithCondition`)
        Stroke color of the marks.
        **Default value:** If undefined, the default color depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``color`` property.

        *Note:* The ``stroke`` encoding has higher precedence than ``color``, thus may
        override the ``color`` encoding if conflicting encodings are specified.
    strokeOpacity : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Stroke opacity of the marks.

        **Default value:** If undefined, the default opacity depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``strokeOpacity``
        property.
    strokeWidth : anyOf(:class:`NumericFieldDefWithCondition`,
    :class:`NumericValueDefWithCondition`)
        Stroke width of the marks.

        **Default value:** If undefined, the default stroke width depends on `mark config
        <https://vega.github.io/vega-lite/docs/config.html#mark>`__ 's ``strokeWidth``
        property.
    text : anyOf(:class:`TextFieldDefWithCondition`, :class:`TextValueDefWithCondition`)
        Text of the ``text`` mark.
    tooltip : anyOf(:class:`StringFieldDefWithCondition`, :class:`StringValueDefWithCondition`,
    List(:class:`StringFieldDef`), None)
        The tooltip text to show upon mouse hover. Specifying ``tooltip`` encoding overrides
        `the tooltip property in the mark definition
        <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip in Vega-Lite.
    url : anyOf(:class:`StringFieldDefWithCondition`, :class:`StringValueDefWithCondition`)
        The URL of an image mark.
    x : anyOf(:class:`PositionFieldDef`, :class:`XValueDef`)
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(:class:`SecondaryFieldDef`, :class:`XValueDef`)
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    xError : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Error value of x coordinates for error specified ``"errorbar"`` and ``"errorband"``.
    xError2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Secondary error value of x coordinates for error specified ``"errorbar"`` and
        ``"errorband"``.
    y : anyOf(:class:`PositionFieldDef`, :class:`YValueDef`)
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(:class:`SecondaryFieldDef`, :class:`YValueDef`)
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    yError : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Error value of y coordinates for error specified ``"errorbar"`` and ``"errorband"``.
    yError2 : anyOf(:class:`SecondaryFieldDef`, :class:`NumberValueDef`)
        Secondary error value of y coordinates for error specified ``"errorbar"`` and
        ``"errorband"``.
    """
    _schema = {'$ref': '#/definitions/FacetedEncoding'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, column=Undefined, detail=Undefined, facet=Undefined,
                 fill=Undefined, fillOpacity=Undefined, href=Undefined, key=Undefined,
                 latitude=Undefined, latitude2=Undefined, longitude=Undefined, longitude2=Undefined,
                 opacity=Undefined, order=Undefined, row=Undefined, shape=Undefined, size=Undefined,
                 stroke=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, text=Undefined,
                 tooltip=Undefined, url=Undefined, x=Undefined, x2=Undefined, xError=Undefined,
                 xError2=Undefined, y=Undefined, y2=Undefined, yError=Undefined, yError2=Undefined,
                 **kwds):
        super(FacetedEncoding, self).__init__(color=color, column=column, detail=detail, facet=facet,
                                              fill=fill, fillOpacity=fillOpacity, href=href, key=key,
                                              latitude=latitude, latitude2=latitude2,
                                              longitude=longitude, longitude2=longitude2,
                                              opacity=opacity, order=order, row=row, shape=shape,
                                              size=size, stroke=stroke, strokeOpacity=strokeOpacity,
                                              strokeWidth=strokeWidth, text=text, tooltip=tooltip,
                                              url=url, x=x, x2=x2, xError=xError, xError2=xError2, y=y,
                                              y2=y2, yError=yError, yError2=yError2, **kwds)


class Field(VegaLiteSchema):
    """Field schema wrapper

    anyOf(:class:`FieldName`, :class:`RepeatRef`)
    """
    _schema = {'$ref': '#/definitions/Field'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Field, self).__init__(*args, **kwds)


class FieldDefWithConditionMarkPropFieldDefGradientstringnull(VegaLiteSchema):
    """FieldDefWithConditionMarkPropFieldDefGradientstringnull schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnull`,
    List(:class:`ConditionalValueDefGradientstringnull`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition<MarkPropFieldDef,(Gradient|string|null)>'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(FieldDefWithConditionMarkPropFieldDefGradientstringnull, self).__init__(type=type,
                                                                                      aggregate=aggregate,
                                                                                      bin=bin,
                                                                                      condition=condition,
                                                                                      field=field,
                                                                                      legend=legend,
                                                                                      scale=scale,
                                                                                      sort=sort,
                                                                                      timeUnit=timeUnit,
                                                                                      title=title,
                                                                                      **kwds)


class FieldDefWithConditionMarkPropFieldDefTypeForShapestringnull(VegaLiteSchema):
    """FieldDefWithConditionMarkPropFieldDefTypeForShapestringnull schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`TypeForShape`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalStringValueDef`,
    List(:class:`ConditionalStringValueDef`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition<MarkPropFieldDef<TypeForShape>,(string|null)>'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(FieldDefWithConditionMarkPropFieldDefTypeForShapestringnull, self).__init__(type=type,
                                                                                          aggregate=aggregate,
                                                                                          bin=bin,
                                                                                          condition=condition,
                                                                                          field=field,
                                                                                          legend=legend,
                                                                                          scale=scale,
                                                                                          sort=sort,
                                                                                          timeUnit=timeUnit,
                                                                                          title=title,
                                                                                          **kwds)


class FieldDefWithConditionMarkPropFieldDefnumber(VegaLiteSchema):
    """FieldDefWithConditionMarkPropFieldDefnumber schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalNumberValueDef`,
    List(:class:`ConditionalNumberValueDef`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition<MarkPropFieldDef,number>'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(FieldDefWithConditionMarkPropFieldDefnumber, self).__init__(type=type,
                                                                          aggregate=aggregate, bin=bin,
                                                                          condition=condition,
                                                                          field=field, legend=legend,
                                                                          scale=scale, sort=sort,
                                                                          timeUnit=timeUnit,
                                                                          title=title, **kwds)


class FieldDefWithConditionStringFieldDefText(VegaLiteSchema):
    """FieldDefWithConditionStringFieldDefText schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefText`, List(:class:`ConditionalValueDefText`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition<StringFieldDef,Text>'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, formatType=Undefined, labelExpr=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(FieldDefWithConditionStringFieldDefText, self).__init__(type=type, aggregate=aggregate,
                                                                      bin=bin, condition=condition,
                                                                      field=field, format=format,
                                                                      formatType=formatType,
                                                                      labelExpr=labelExpr,
                                                                      timeUnit=timeUnit, title=title,
                                                                      **kwds)


class FieldDefWithConditionStringFieldDefstring(VegaLiteSchema):
    """FieldDefWithConditionStringFieldDefstring schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstring`,
    List(:class:`ConditionalValueDefstring`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithCondition<StringFieldDef,string>'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, formatType=Undefined, labelExpr=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(FieldDefWithConditionStringFieldDefstring, self).__init__(type=type, aggregate=aggregate,
                                                                        bin=bin, condition=condition,
                                                                        field=field, format=format,
                                                                        formatType=formatType,
                                                                        labelExpr=labelExpr,
                                                                        timeUnit=timeUnit, title=title,
                                                                        **kwds)


class FieldDefWithoutScale(VegaLiteSchema):
    """FieldDefWithoutScale schema wrapper

    Mapping(required=[type])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/FieldDefWithoutScale'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(FieldDefWithoutScale, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                                   timeUnit=timeUnit, title=title, **kwds)


class FieldName(Field):
    """FieldName schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/FieldName'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FieldName, self).__init__(*args)


class FitType(AutosizeType):
    """FitType schema wrapper

    enum('fit', 'fit-x', 'fit-y')
    """
    _schema = {'$ref': '#/definitions/FitType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FitType, self).__init__(*args)


class FontStyle(VegaLiteSchema):
    """FontStyle schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/FontStyle'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontStyle, self).__init__(*args)


class FontWeight(VegaLiteSchema):
    """FontWeight schema wrapper

    enum('normal', 'bold', 'lighter', 'bolder', 100, 200, 300, 400, 500, 600, 700, 800, 900)
    """
    _schema = {'$ref': '#/definitions/FontWeight'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontWeight, self).__init__(*args)


class Generator(Data):
    """Generator schema wrapper

    anyOf(:class:`SequenceGenerator`, :class:`SphereGenerator`, :class:`GraticuleGenerator`)
    """
    _schema = {'$ref': '#/definitions/Generator'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Generator, self).__init__(*args, **kwds)


class GenericUnitSpecEncodingAnyMark(VegaLiteSchema):
    """GenericUnitSpecEncodingAnyMark schema wrapper

    Mapping(required=[mark])
    Base interface for a unit (single-view) specification.

    Attributes
    ----------

    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A key-value mapping between encoding channels and definition of fields.
    height : anyOf(float, enum('container'), :class:`Step`)
        The height of a visualization.


        * For a plot with a continuous y-field, height should be a number.
        * For a plot with either a discrete y-field or no y-field, height can be either a
          number indicating a fixed height or an object in the form of ``{step: number}``
          defining the height per discrete step. (No y-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on height, it should be set to ``"container"``.

        **Default value:** Based on ``config.view.continuousHeight`` for a plot with a
        continuous y-field and ``config.view.discreteHeight`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view and the ``"container"`` option cannot be used.

        **See also:** `height <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    view : :class:`ViewBackground`
        An object defining the view background's fill and stroke.

        **Default value:** none (transparent)
    width : anyOf(float, enum('container'), :class:`Step`)
        The width of a visualization.


        * For a plot with a continuous x-field, width should be a number.
        * For a plot with either a discrete x-field or no x-field, width can be either a
          number indicating a fixed width or an object in the form of ``{step: number}``
          defining the width per discrete step. (No x-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on width, it should be set to ``"container"``.

        **Default value:**
        Based on ``config.view.continuousWidth`` for a plot with a continuous x-field and
        ``config.view.discreteWidth`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view and the ``"container"`` option cannot be used.

        **See also:** `width <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/GenericUnitSpec<Encoding,AnyMark>'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, selection=Undefined,
                 title=Undefined, transform=Undefined, view=Undefined, width=Undefined, **kwds):
        super(GenericUnitSpecEncodingAnyMark, self).__init__(mark=mark, data=data,
                                                             description=description, encoding=encoding,
                                                             height=height, name=name,
                                                             projection=projection, selection=selection,
                                                             title=title, transform=transform,
                                                             view=view, width=width, **kwds)


class Gradient(VegaLiteSchema):
    """Gradient schema wrapper

    anyOf(:class:`LinearGradient`, :class:`RadialGradient`)
    """
    _schema = {'$ref': '#/definitions/Gradient'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Gradient, self).__init__(*args, **kwds)


class GradientStop(VegaLiteSchema):
    """GradientStop schema wrapper

    Mapping(required=[offset, color])

    Attributes
    ----------

    color : :class:`Color`
        The color value at this point in the gradient.
    offset : float
        The offset fraction for the color stop, indicating its position within the gradient.
    """
    _schema = {'$ref': '#/definitions/GradientStop'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, offset=Undefined, **kwds):
        super(GradientStop, self).__init__(color=color, offset=offset, **kwds)


class GraticuleGenerator(Generator):
    """GraticuleGenerator schema wrapper

    Mapping(required=[graticule])

    Attributes
    ----------

    graticule : anyOf(enum(True), :class:`GraticuleParams`)
        Generate graticule GeoJSON data for geographic reference lines.
    name : string
        Provide a placeholder name and bind data at runtime.
    """
    _schema = {'$ref': '#/definitions/GraticuleGenerator'}
    _rootschema = Root._schema

    def __init__(self, graticule=Undefined, name=Undefined, **kwds):
        super(GraticuleGenerator, self).__init__(graticule=graticule, name=name, **kwds)


class GraticuleParams(VegaLiteSchema):
    """GraticuleParams schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    extent : :class:`Vector2Vector2number`
        Sets both the major and minor extents to the same values.
    extentMajor : :class:`Vector2Vector2number`
        The major extent of the graticule as a two-element array of coordinates.
    extentMinor : :class:`Vector2Vector2number`
        The minor extent of the graticule as a two-element array of coordinates.
    precision : float
        The precision of the graticule in degrees.

        **Default value:** ``2.5``
    step : :class:`Vector2number`
        Sets both the major and minor step angles to the same values.
    stepMajor : :class:`Vector2number`
        The major step angles of the graticule.

        **Default value:** ``[90, 360]``
    stepMinor : :class:`Vector2number`
        The minor step angles of the graticule.

        **Default value:** ``[10, 10]``
    """
    _schema = {'$ref': '#/definitions/GraticuleParams'}
    _rootschema = Root._schema

    def __init__(self, extent=Undefined, extentMajor=Undefined, extentMinor=Undefined,
                 precision=Undefined, step=Undefined, stepMajor=Undefined, stepMinor=Undefined, **kwds):
        super(GraticuleParams, self).__init__(extent=extent, extentMajor=extentMajor,
                                              extentMinor=extentMinor, precision=precision, step=step,
                                              stepMajor=stepMajor, stepMinor=stepMinor, **kwds)


class Header(VegaLiteSchema):
    """Header schema wrapper

    Mapping(required=[])
    Headers of row / column channels for faceted plots.

    Attributes
    ----------

    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelAlign : :class:`Align`
        Horizontal text alignment of header labels. One of ``"left"``, ``"center"``, or
        ``"right"``.
    labelAnchor : :class:`TitleAnchor`
        The anchor position for placing the labels. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with a label orientation of top these anchor positions map
        to a left-, center-, or right-aligned label.
    labelAngle : float
        The rotation angle of the header labels.

        **Default value:** ``0`` for column header, ``-90`` for row header.
    labelColor : :class:`Color`
        The color of the header label, can be in hex color code or regular color name.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the header's backing ``datum`` object.
    labelFont : string
        The font of the header label.
    labelFontSize : float
        The font size of the header label, in pixels.
    labelFontStyle : :class:`FontStyle`
        The font style of the header label.
    labelLimit : float
        The maximum length of the header label in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    labelOrient : :class:`Orient`
        The orientation of the header label. One of ``"top"``, ``"bottom"``, ``"left"`` or
        ``"right"``.
    labelPadding : float
        The padding, in pixel, between facet header's label and the plot.

        **Default value:** ``10``
    labels : boolean
        A boolean flag indicating if labels should be included as part of the header.

        **Default value:** ``true``.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    titleAlign : :class:`Align`
        Horizontal text alignment (to the anchor) of header titles.
    titleAnchor : :class:`TitleAnchor`
        The anchor position for placing the title. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with an orientation of top these anchor positions map to a
        left-, center-, or right-aligned title.
    titleAngle : float
        The rotation angle of the header title.

        **Default value:** ``0``.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for the header title. One of ``"top"``, ``"bottom"``,
        ``"middle"``.

        **Default value:** ``"middle"``
    titleColor : :class:`Color`
        Color of the header title, can be in hex color code or regular color name.
    titleFont : string
        Font of the header title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the header title.
    titleFontStyle : :class:`FontStyle`
        The font style of the header title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the header title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        The maximum length of the header title in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    titleLineHeight : float
        Line height in pixels for multi-line title text.
    titleOrient : :class:`Orient`
        The orientation of the header title. One of ``"top"``, ``"bottom"``, ``"left"`` or
        ``"right"``.
    titlePadding : float
        The padding, in pixel, between facet header's title and the label.

        **Default value:** ``10``
    """
    _schema = {'$ref': '#/definitions/Header'}
    _rootschema = Root._schema

    def __init__(self, format=Undefined, formatType=Undefined, labelAlign=Undefined,
                 labelAnchor=Undefined, labelAngle=Undefined, labelColor=Undefined, labelExpr=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined,
                 labelLimit=Undefined, labelOrient=Undefined, labelPadding=Undefined, labels=Undefined,
                 title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined,
                 titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined,
                 titleLimit=Undefined, titleLineHeight=Undefined, titleOrient=Undefined,
                 titlePadding=Undefined, **kwds):
        super(Header, self).__init__(format=format, formatType=formatType, labelAlign=labelAlign,
                                     labelAnchor=labelAnchor, labelAngle=labelAngle,
                                     labelColor=labelColor, labelExpr=labelExpr, labelFont=labelFont,
                                     labelFontSize=labelFontSize, labelFontStyle=labelFontStyle,
                                     labelLimit=labelLimit, labelOrient=labelOrient,
                                     labelPadding=labelPadding, labels=labels, title=title,
                                     titleAlign=titleAlign, titleAnchor=titleAnchor,
                                     titleAngle=titleAngle, titleBaseline=titleBaseline,
                                     titleColor=titleColor, titleFont=titleFont,
                                     titleFontSize=titleFontSize, titleFontStyle=titleFontStyle,
                                     titleFontWeight=titleFontWeight, titleLimit=titleLimit,
                                     titleLineHeight=titleLineHeight, titleOrient=titleOrient,
                                     titlePadding=titlePadding, **kwds)


class HeaderConfig(VegaLiteSchema):
    """HeaderConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelAlign : :class:`Align`
        Horizontal text alignment of header labels. One of ``"left"``, ``"center"``, or
        ``"right"``.
    labelAnchor : :class:`TitleAnchor`
        The anchor position for placing the labels. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with a label orientation of top these anchor positions map
        to a left-, center-, or right-aligned label.
    labelAngle : float
        The rotation angle of the header labels.

        **Default value:** ``0`` for column header, ``-90`` for row header.
    labelColor : :class:`Color`
        The color of the header label, can be in hex color code or regular color name.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the header's backing ``datum`` object.
    labelFont : string
        The font of the header label.
    labelFontSize : float
        The font size of the header label, in pixels.
    labelFontStyle : :class:`FontStyle`
        The font style of the header label.
    labelLimit : float
        The maximum length of the header label in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    labelOrient : :class:`Orient`
        The orientation of the header label. One of ``"top"``, ``"bottom"``, ``"left"`` or
        ``"right"``.
    labelPadding : float
        The padding, in pixel, between facet header's label and the plot.

        **Default value:** ``10``
    labels : boolean
        A boolean flag indicating if labels should be included as part of the header.

        **Default value:** ``true``.
    title : None
        Set to null to disable title for the axis, legend, or header.
    titleAlign : :class:`Align`
        Horizontal text alignment (to the anchor) of header titles.
    titleAnchor : :class:`TitleAnchor`
        The anchor position for placing the title. One of ``"start"``, ``"middle"``, or
        ``"end"``. For example, with an orientation of top these anchor positions map to a
        left-, center-, or right-aligned title.
    titleAngle : float
        The rotation angle of the header title.

        **Default value:** ``0``.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for the header title. One of ``"top"``, ``"bottom"``,
        ``"middle"``.

        **Default value:** ``"middle"``
    titleColor : :class:`Color`
        Color of the header title, can be in hex color code or regular color name.
    titleFont : string
        Font of the header title. (e.g., ``"Helvetica Neue"`` ).
    titleFontSize : float
        Font size of the header title.
    titleFontStyle : :class:`FontStyle`
        The font style of the header title.
    titleFontWeight : :class:`FontWeight`
        Font weight of the header title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        The maximum length of the header title in pixels. The text value will be
        automatically truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    titleLineHeight : float
        Line height in pixels for multi-line title text.
    titleOrient : :class:`Orient`
        The orientation of the header title. One of ``"top"``, ``"bottom"``, ``"left"`` or
        ``"right"``.
    titlePadding : float
        The padding, in pixel, between facet header's title and the label.

        **Default value:** ``10``
    """
    _schema = {'$ref': '#/definitions/HeaderConfig'}
    _rootschema = Root._schema

    def __init__(self, format=Undefined, formatType=Undefined, labelAlign=Undefined,
                 labelAnchor=Undefined, labelAngle=Undefined, labelColor=Undefined, labelExpr=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined,
                 labelLimit=Undefined, labelOrient=Undefined, labelPadding=Undefined, labels=Undefined,
                 title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined,
                 titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined,
                 titleLimit=Undefined, titleLineHeight=Undefined, titleOrient=Undefined,
                 titlePadding=Undefined, **kwds):
        super(HeaderConfig, self).__init__(format=format, formatType=formatType, labelAlign=labelAlign,
                                           labelAnchor=labelAnchor, labelAngle=labelAngle,
                                           labelColor=labelColor, labelExpr=labelExpr,
                                           labelFont=labelFont, labelFontSize=labelFontSize,
                                           labelFontStyle=labelFontStyle, labelLimit=labelLimit,
                                           labelOrient=labelOrient, labelPadding=labelPadding,
                                           labels=labels, title=title, titleAlign=titleAlign,
                                           titleAnchor=titleAnchor, titleAngle=titleAngle,
                                           titleBaseline=titleBaseline, titleColor=titleColor,
                                           titleFont=titleFont, titleFontSize=titleFontSize,
                                           titleFontStyle=titleFontStyle,
                                           titleFontWeight=titleFontWeight, titleLimit=titleLimit,
                                           titleLineHeight=titleLineHeight, titleOrient=titleOrient,
                                           titlePadding=titlePadding, **kwds)


class HexColor(Color):
    """HexColor schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/HexColor'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(HexColor, self).__init__(*args)


class ImputeMethod(VegaLiteSchema):
    """ImputeMethod schema wrapper

    enum('value', 'median', 'max', 'min', 'mean')
    """
    _schema = {'$ref': '#/definitions/ImputeMethod'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ImputeMethod, self).__init__(*args)


class ImputeParams(VegaLiteSchema):
    """ImputeParams schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    frame : List([anyOf(None, float), anyOf(None, float)])
        A frame specification as a two-element array used to control the window over which
        the specified method is applied. The array entries should either be a number
        indicating the offset from the current data object, or null to indicate unbounded
        rows preceding or following the current data object. For example, the value ``[-5,
        5]`` indicates that the window should include five objects preceding and five
        objects following the current object.

        **Default value:** :  ``[null, null]`` indicating that the window includes all
        objects.
    keyvals : anyOf(List(Any), :class:`ImputeSequence`)
        Defines the key values that should be considered for imputation.
        An array of key values or an object defining a `number sequence
        <https://vega.github.io/vega-lite/docs/impute.html#sequence-def>`__.

        If provided, this will be used in addition to the key values observed within the
        input data. If not provided, the values will be derived from all unique values of
        the ``key`` field. For ``impute`` in ``encoding``, the key field is the x-field if
        the y-field is imputed, or vice versa.

        If there is no impute grouping, this property *must* be specified.
    method : :class:`ImputeMethod`
        The imputation method to use for the field value of imputed data objects.
        One of ``"value"``, ``"mean"``, ``"median"``, ``"max"`` or ``"min"``.

        **Default value:**  ``"value"``
    value : Any
        The field value to use when the imputation ``method`` is ``"value"``.
    """
    _schema = {'$ref': '#/definitions/ImputeParams'}
    _rootschema = Root._schema

    def __init__(self, frame=Undefined, keyvals=Undefined, method=Undefined, value=Undefined, **kwds):
        super(ImputeParams, self).__init__(frame=frame, keyvals=keyvals, method=method, value=value,
                                           **kwds)


class ImputeSequence(VegaLiteSchema):
    """ImputeSequence schema wrapper

    Mapping(required=[stop])

    Attributes
    ----------

    stop : float
        The ending value(exclusive) of the sequence.
    start : float
        The starting value of the sequence.
        **Default value:** ``0``
    step : float
        The step value between sequence entries.
        **Default value:** ``1`` or ``-1`` if ``stop < start``
    """
    _schema = {'$ref': '#/definitions/ImputeSequence'}
    _rootschema = Root._schema

    def __init__(self, stop=Undefined, start=Undefined, step=Undefined, **kwds):
        super(ImputeSequence, self).__init__(stop=stop, start=start, step=step, **kwds)


class InlineData(DataSource):
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


class InputBinding(Binding):
    """InputBinding schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    autocomplete : string

    debounce : float

    element : :class:`Element`

    input : string

    name : string

    placeholder : string

    type : string

    """
    _schema = {'$ref': '#/definitions/InputBinding'}
    _rootschema = Root._schema

    def __init__(self, autocomplete=Undefined, debounce=Undefined, element=Undefined, input=Undefined,
                 name=Undefined, placeholder=Undefined, type=Undefined, **kwds):
        super(InputBinding, self).__init__(autocomplete=autocomplete, debounce=debounce,
                                           element=element, input=input, name=name,
                                           placeholder=placeholder, type=type, **kwds)


class Interpolate(VegaLiteSchema):
    """Interpolate schema wrapper

    enum('basis', 'basis-open', 'basis-closed', 'bundle', 'cardinal', 'cardinal-open',
    'cardinal-closed', 'catmull-rom', 'linear', 'linear-closed', 'monotone', 'natural', 'step',
    'step-before', 'step-after')
    """
    _schema = {'$ref': '#/definitions/Interpolate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Interpolate, self).__init__(*args)


class IntervalSelectionConfig(VegaLiteSchema):
    """IntervalSelectionConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bind : enum('scales')
        Establishes a two-way binding between the interval selection and the scales
        used within the same view. This allows a user to interactively pan and
        zoom the view.

        **See also:** `bind <https://vega.github.io/vega-lite/docs/bind.html>`__
        documentation.
    clear : anyOf(:class:`Stream`, string, boolean)
        Clears the selection, emptying it of all values. Can be a
        `Event Stream <https://vega.github.io/vega/docs/event-streams/>`__ or ``false`` to
        disable.

        **Default value:** ``dblclick``.

        **See also:** `clear <https://vega.github.io/vega-lite/docs/clear.html>`__
        documentation.
    empty : enum('all', 'none')
        By default, ``all`` data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefUnitChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.

        **See also:** `encodings <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    fields : List(:class:`FieldName`)
        An array of field names whose values must match for a data tuple to
        fall within the selection.

        **See also:** `fields <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    init : :class:`SelectionInitIntervalMapping`
        Initialize the selection with a mapping between `projected channels or field names
        <https://vega.github.io/vega-lite/docs/project.html>`__ and arrays of
        initial values.

        **See also:** `init <https://vega.github.io/vega-lite/docs/init.html>`__
        documentation.
    mark : :class:`BrushConfig`
        An interval selection also adds a rectangle mark to depict the
        extents of the interval. The ``mark`` property can be used to customize the
        appearance of the mark.

        **See also:** `mark <https://vega.github.io/vega-lite/docs/selection-mark.html>`__
        documentation.
    on : anyOf(:class:`Stream`, string)
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.

        **See also:** `resolve
        <https://vega.github.io/vega-lite/docs/selection-resolve.html>`__ documentation.
    translate : anyOf(string, boolean)
        When truthy, allows a user to interactively move an interval selection
        back-and-forth. Can be ``true``, ``false`` (to disable panning), or a
        `Vega event stream definition <https://vega.github.io/vega/docs/event-streams/>`__
        which must include a start and end event to trigger continuous panning.

        **Default value:** ``true``, which corresponds to
        ``[mousedown, window:mouseup] > window:mousemove!`` which corresponds to
        clicks and dragging within an interval selection to reposition it.

        **See also:** `translate <https://vega.github.io/vega-lite/docs/translate.html>`__
        documentation.
    zoom : anyOf(string, boolean)
        When truthy, allows a user to interactively resize an interval selection.
        Can be ``true``, ``false`` (to disable zooming), or a `Vega event stream
        definition <https://vega.github.io/vega/docs/event-streams/>`__. Currently,
        only ``wheel`` events are supported.

        **Default value:** ``true``, which corresponds to ``wheel!``.

        **See also:** `zoom <https://vega.github.io/vega-lite/docs/zoom.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/IntervalSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, clear=Undefined, empty=Undefined, encodings=Undefined,
                 fields=Undefined, init=Undefined, mark=Undefined, on=Undefined, resolve=Undefined,
                 translate=Undefined, zoom=Undefined, **kwds):
        super(IntervalSelectionConfig, self).__init__(bind=bind, clear=clear, empty=empty,
                                                      encodings=encodings, fields=fields, init=init,
                                                      mark=mark, on=on, resolve=resolve,
                                                      translate=translate, zoom=zoom, **kwds)


class JoinAggregateFieldDef(VegaLiteSchema):
    """JoinAggregateFieldDef schema wrapper

    Mapping(required=[op, as])

    Attributes
    ----------

    op : :class:`AggregateOp`
        The aggregation operation to apply (e.g., ``"sum"``, ``"average"`` or ``"count"`` ).
        See the list of all supported operations `here
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__.
    field : :class:`FieldName`
        The data field for which to compute the aggregate function. This can be omitted for
        functions that do not operate over a field such as ``"count"``.
    as : :class:`FieldName`
        The output name for the join aggregate operation.
    """
    _schema = {'$ref': '#/definitions/JoinAggregateFieldDef'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, **kwds):
        super(JoinAggregateFieldDef, self).__init__(op=op, field=field, **kwds)


class JsonDataFormat(DataFormat):
    """JsonDataFormat schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    parse : anyOf(:class:`Parse`, None)
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
        For Specific date formats can be provided (e.g., ``{foo: "date:'%m%d%Y'"}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: "utc:'%m%d%Y'"}`` ).
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

        **Default value:**  The default format type is determined by the extension of the
        file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/JsonDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, property=Undefined, type=Undefined, **kwds):
        super(JsonDataFormat, self).__init__(parse=parse, property=property, type=type, **kwds)


class LabelOverlap(VegaLiteSchema):
    """LabelOverlap schema wrapper

    anyOf(boolean, enum('parity'), enum('greedy'))
    """
    _schema = {'$ref': '#/definitions/LabelOverlap'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LabelOverlap, self).__init__(*args, **kwds)


class LatLongFieldDef(VegaLiteSchema):
    """LatLongFieldDef schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : enum('quantitative')
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/LatLongFieldDef'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(LatLongFieldDef, self).__init__(aggregate=aggregate, bin=bin, field=field,
                                              timeUnit=timeUnit, title=title, type=type, **kwds)


class LayoutAlign(VegaLiteSchema):
    """LayoutAlign schema wrapper

    enum('all', 'each', 'none')
    """
    _schema = {'$ref': '#/definitions/LayoutAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LayoutAlign, self).__init__(*args)


class LayoutBounds(VegaLiteSchema):
    """LayoutBounds schema wrapper

    anyOf(enum('full'), enum('flush'), :class:`SignalRef`)
    """
    _schema = {'$ref': '#/definitions/LayoutBounds'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LayoutBounds, self).__init__(*args, **kwds)


class Legend(VegaLiteSchema):
    """Legend schema wrapper

    Mapping(required=[])
    Properties of a legend or boolean flag for determining whether to show it.

    Attributes
    ----------

    clipHeight : float
        The height in pixels to clip symbol legend entries and limit their size.
    columnPadding : float
        The horizontal padding in pixels between symbol legend entries.

        **Default value:** ``10``.
    columns : float
        The number of columns in which to arrange symbol legend entries. A value of ``0`` or
        lower indicates a single row with one column per entry.
    cornerRadius : float
        Corner radius for the full legend.
    direction : :class:`Orientation`
        The direction of the legend, one of ``"vertical"`` or ``"horizontal"``.

        **Default value:**


        * For top-/bottom- ``orient`` ed legends, ``"horizontal"``
        * For left-/right- ``orient`` ed legends, ``"vertical"``
        * For top/bottom-left/right- ``orient`` ed legends, ``"horizontal"`` for gradient
          legends and ``"vertical"`` for symbol legends.
    fillColor : anyOf(None, :class:`Color`)
        Background fill color for the full legend.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    gradientLength : float
        The length in pixels of the primary axis of a color gradient. This value corresponds
        to the height of a vertical gradient or the width of a horizontal gradient.

        **Default value:** ``200``.
    gradientOpacity : float
        Opacity of the color gradient.
    gradientStrokeColor : anyOf(None, :class:`Color`)
        The color of the gradient stroke, can be in hex color code or regular color name.

        **Default value:** ``"lightGray"``.
    gradientStrokeWidth : float
        The width of the gradient stroke, in pixels.

        **Default value:** ``0``.
    gradientThickness : float
        The thickness in pixels of the color gradient. This value corresponds to the width
        of a vertical gradient or the height of a horizontal gradient.

        **Default value:** ``16``.
    gridAlign : :class:`LayoutAlign`
        The alignment to apply to symbol legends rows and columns. The supported string
        values are ``"all"``, ``"each"`` (the default), and ``none``. For more information,
        see the `grid layout documentation <https://vega.github.io/vega/docs/layout>`__.

        **Default value:** ``"each"``.
    labelAlign : :class:`Align`
        The alignment of the legend label, can be left, center, or right.
    labelBaseline : :class:`TextBaseline`
        The position of the baseline of legend label, can be ``"top"``, ``"middle"``,
        ``"bottom"``, or ``"alphabetic"``.

        **Default value:** ``"middle"``.
    labelColor : anyOf(None, :class:`Color`)
        The color of the legend label, can be in hex color code or regular color name.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the legend's backing ``datum`` object.
    labelFont : string
        The font of the legend label.
    labelFontSize : float
        The font size of legend label.

        **Default value:** ``10``.
    labelFontStyle : :class:`FontStyle`
        The font style of legend label.
    labelFontWeight : :class:`FontWeight`
        The font weight of legend label.
    labelLimit : float
        Maximum allowed pixel width of legend tick labels.

        **Default value:** ``160``.
    labelOffset : float
        The offset of the legend label.
    labelOpacity : float
        Opacity of labels.
    labelOverlap : :class:`LabelOverlap`
        The strategy to use for resolving overlap of labels in gradient legends. If
        ``false``, no overlap reduction is attempted. If set to ``true`` (default) or
        ``"parity"``, a strategy of removing every other label is used. If set to
        ``"greedy"``, a linear scan of the labels is performed, removing any label that
        overlaps with the last visible label (this often works better for log-scaled axes).

        **Default value:** ``true``.
    labelPadding : float
        Padding in pixels between the legend and legend labels.
    labelSeparation : float
        The minimum separation that must be between label bounding boxes for them to be
        considered non-overlapping (default ``0`` ). This property is ignored if
        *labelOverlap* resolution is not enabled.
    legendX : float
        Custom x-position for legend with orient "none".
    legendY : float
        Custom y-position for legend with orient "none".
    offset : float
        The offset in pixels by which to displace the legend from the data rectangle and
        axes.

        **Default value:** ``18``.
    orient : :class:`LegendOrient`
        The orientation of the legend, which determines how the legend is positioned within
        the scene. One of ``"left"``, ``"right"``, ``"top"``, ``"bottom"``, ``"top-left"``,
        ``"top-right"``, ``"bottom-left"``, ``"bottom-right"``, ``"none"``.

        **Default value:** ``"right"``
    padding : float
        The padding between the border and content of the legend group.

        **Default value:** ``0``.
    rowPadding : float
        The vertical padding in pixels between symbol legend entries.

        **Default value:** ``2``.
    strokeColor : anyOf(None, :class:`Color`)
        Border stroke color for the full legend.
    symbolDash : List(float)
        An array of alternating [stroke, space] lengths for dashed symbol strokes.
    symbolDashOffset : float
        The pixel offset at which to start drawing with the symbol stroke dash array.
    symbolFillColor : anyOf(None, :class:`Color`)
        The color of the legend symbol,
    symbolLimit : float
        The maximum number of allowed entries for a symbol legend. Additional entries will
        be dropped.
    symbolOffset : float
        Horizontal pixel offset for legend symbols.

        **Default value:** ``0``.
    symbolOpacity : float
        Opacity of the legend symbols.
    symbolSize : float
        The size of the legend symbol, in pixels.

        **Default value:** ``100``.
    symbolStrokeColor : anyOf(None, :class:`Color`)
        Stroke color for legend symbols.
    symbolStrokeWidth : float
        The width of the symbol's stroke.

        **Default value:** ``1.5``.
    symbolType : :class:`SymbolShape`
        The symbol shape. One of the plotting shapes ``circle`` (default), ``square``,
        ``cross``, ``diamond``, ``triangle-up``, ``triangle-down``, ``triangle-right``, or
        ``triangle-left``, the line symbol ``stroke``, or one of the centered directional
        shapes ``arrow``, ``wedge``, or ``triangle``. Alternatively, a custom `SVG path
        string <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ can be
        provided. For correct sizing, custom shape paths should be defined within a square
        bounding box with coordinates ranging from -1 to 1 along both the x and y
        dimensions.

        **Default value:** ``"circle"``.
    tickCount : anyOf(float, :class:`TimeInterval`)
        The desired number of tick values for quantitative legends.
    tickMinStep : float
        The minimum desired step between legend ticks, in terms of scale domain values. For
        example, a value of ``1`` indicates that ticks should not be less than 1 unit apart.
        If ``tickMinStep`` is specified, the ``tickCount`` value will be adjusted, if
        necessary, to enforce the minimum step value.

        **Default value** : ``undefined``
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    titleAlign : :class:`Align`
        Horizontal text alignment for legend titles.

        **Default value:** ``"left"``.
    titleAnchor : :class:`TitleAnchor`
        Text anchor position for placing legend titles.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for legend titles.

        **Default value:** ``"top"``.
    titleColor : anyOf(None, :class:`Color`)
        The color of the legend title, can be in hex color code or regular color name.
    titleFont : string
        The font of the legend title.
    titleFontSize : float
        The font size of the legend title.
    titleFontStyle : :class:`FontStyle`
        The font style of the legend title.
    titleFontWeight : :class:`FontWeight`
        The font weight of the legend title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        Maximum allowed pixel width of legend titles.

        **Default value:** ``180``.
    titleLineHeight : float
        Line height in pixels for multi-line title text.
    titleOpacity : float
        Opacity of the legend title.
    titleOrient : :class:`Orient`
        Orientation of the legend title.
    titlePadding : float
        The padding, in pixels, between title and legend.

        **Default value:** ``5``.
    type : enum('symbol', 'gradient')
        The type of the legend. Use ``"symbol"`` to create a discrete legend and
        ``"gradient"`` for a continuous color gradient.

        **Default value:** ``"gradient"`` for non-binned quantitative fields and temporal
        fields; ``"symbol"`` otherwise.
    values : List(anyOf(float, string, boolean, :class:`DateTime`))
        Explicitly set the visible legend values.
    zindex : float
        A non-negative integer indicating the z-index of the legend.
        If zindex is 0, legend should be drawn behind all chart elements.
        To put them in front, use zindex = 1.
    """
    _schema = {'$ref': '#/definitions/Legend'}
    _rootschema = Root._schema

    def __init__(self, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined,
                 cornerRadius=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined,
                 formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined,
                 gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined,
                 gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined,
                 labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined,
                 labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined,
                 labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined,
                 labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined,
                 orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined,
                 symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined,
                 symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined,
                 symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined,
                 symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined,
                 titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined,
                 titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined,
                 titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined,
                 titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined,
                 titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(Legend, self).__init__(clipHeight=clipHeight, columnPadding=columnPadding,
                                     columns=columns, cornerRadius=cornerRadius, direction=direction,
                                     fillColor=fillColor, format=format, formatType=formatType,
                                     gradientLength=gradientLength, gradientOpacity=gradientOpacity,
                                     gradientStrokeColor=gradientStrokeColor,
                                     gradientStrokeWidth=gradientStrokeWidth,
                                     gradientThickness=gradientThickness, gridAlign=gridAlign,
                                     labelAlign=labelAlign, labelBaseline=labelBaseline,
                                     labelColor=labelColor, labelExpr=labelExpr, labelFont=labelFont,
                                     labelFontSize=labelFontSize, labelFontStyle=labelFontStyle,
                                     labelFontWeight=labelFontWeight, labelLimit=labelLimit,
                                     labelOffset=labelOffset, labelOpacity=labelOpacity,
                                     labelOverlap=labelOverlap, labelPadding=labelPadding,
                                     labelSeparation=labelSeparation, legendX=legendX, legendY=legendY,
                                     offset=offset, orient=orient, padding=padding,
                                     rowPadding=rowPadding, strokeColor=strokeColor,
                                     symbolDash=symbolDash, symbolDashOffset=symbolDashOffset,
                                     symbolFillColor=symbolFillColor, symbolLimit=symbolLimit,
                                     symbolOffset=symbolOffset, symbolOpacity=symbolOpacity,
                                     symbolSize=symbolSize, symbolStrokeColor=symbolStrokeColor,
                                     symbolStrokeWidth=symbolStrokeWidth, symbolType=symbolType,
                                     tickCount=tickCount, tickMinStep=tickMinStep, title=title,
                                     titleAlign=titleAlign, titleAnchor=titleAnchor,
                                     titleBaseline=titleBaseline, titleColor=titleColor,
                                     titleFont=titleFont, titleFontSize=titleFontSize,
                                     titleFontStyle=titleFontStyle, titleFontWeight=titleFontWeight,
                                     titleLimit=titleLimit, titleLineHeight=titleLineHeight,
                                     titleOpacity=titleOpacity, titleOrient=titleOrient,
                                     titlePadding=titlePadding, type=type, values=values, zindex=zindex,
                                     **kwds)


class LegendBinding(VegaLiteSchema):
    """LegendBinding schema wrapper

    anyOf(enum('legend'), :class:`LegendStreamBinding`)
    """
    _schema = {'$ref': '#/definitions/LegendBinding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LegendBinding, self).__init__(*args, **kwds)


class LegendConfig(VegaLiteSchema):
    """LegendConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    clipHeight : float
        The height in pixels to clip symbol legend entries and limit their size.
    columnPadding : float
        The horizontal padding in pixels between symbol legend entries.

        **Default value:** ``10``.
    columns : float
        The number of columns in which to arrange symbol legend entries. A value of ``0`` or
        lower indicates a single row with one column per entry.
    cornerRadius : float
        Corner radius for the full legend.
    fillColor : anyOf(None, :class:`Color`)
        Background fill color for the full legend.
    gradientDirection : :class:`Orientation`
        The default direction ( ``"horizontal"`` or ``"vertical"`` ) for gradient legends.

        **Default value:** ``"vertical"``.
    gradientHorizontalMaxLength : float
        Max legend length for a horizontal gradient when ``config.legend.gradientLength`` is
        undefined.

        **Default value:** ``200``
    gradientHorizontalMinLength : float
        Min legend length for a horizontal gradient when ``config.legend.gradientLength`` is
        undefined.

        **Default value:** ``100``
    gradientLabelLimit : float
        The maximum allowed length in pixels of color ramp gradient labels.
    gradientLabelOffset : float
        Vertical offset in pixels for color ramp gradient labels.

        **Default value:** ``2``.
    gradientLength : float
        The length in pixels of the primary axis of a color gradient. This value corresponds
        to the height of a vertical gradient or the width of a horizontal gradient.

        **Default value:** ``200``.
    gradientOpacity : float
        Opacity of the color gradient.
    gradientStrokeColor : anyOf(None, :class:`Color`)
        The color of the gradient stroke, can be in hex color code or regular color name.

        **Default value:** ``"lightGray"``.
    gradientStrokeWidth : float
        The width of the gradient stroke, in pixels.

        **Default value:** ``0``.
    gradientThickness : float
        The thickness in pixels of the color gradient. This value corresponds to the width
        of a vertical gradient or the height of a horizontal gradient.

        **Default value:** ``16``.
    gradientVerticalMaxLength : float
        Max legend length for a vertical gradient when ``config.legend.gradientLength`` is
        undefined.

        **Default value:** ``200``
    gradientVerticalMinLength : float
        Min legend length for a vertical gradient when ``config.legend.gradientLength`` is
        undefined.

        **Default value:** ``100``
    gridAlign : :class:`LayoutAlign`
        The alignment to apply to symbol legends rows and columns. The supported string
        values are ``"all"``, ``"each"`` (the default), and ``none``. For more information,
        see the `grid layout documentation <https://vega.github.io/vega/docs/layout>`__.

        **Default value:** ``"each"``.
    labelAlign : :class:`Align`
        The alignment of the legend label, can be left, center, or right.
    labelBaseline : :class:`TextBaseline`
        The position of the baseline of legend label, can be ``"top"``, ``"middle"``,
        ``"bottom"``, or ``"alphabetic"``.

        **Default value:** ``"middle"``.
    labelColor : anyOf(None, :class:`Color`)
        The color of the legend label, can be in hex color code or regular color name.
    labelFont : string
        The font of the legend label.
    labelFontSize : float
        The font size of legend label.

        **Default value:** ``10``.
    labelFontStyle : :class:`FontStyle`
        The font style of legend label.
    labelFontWeight : :class:`FontWeight`
        The font weight of legend label.
    labelLimit : float
        Maximum allowed pixel width of legend tick labels.

        **Default value:** ``160``.
    labelOffset : float
        The offset of the legend label.
    labelOpacity : float
        Opacity of labels.
    labelOverlap : :class:`LabelOverlap`
        The strategy to use for resolving overlap of labels in gradient legends. If
        ``false``, no overlap reduction is attempted. If set to ``true`` or ``"parity"``, a
        strategy of removing every other label is used. If set to ``"greedy"``, a linear
        scan of the labels is performed, removing any label that overlaps with the last
        visible label (this often works better for log-scaled axes).

        **Default value:** ``"greedy"`` for ``log scales otherwise`` true`.
    labelPadding : float
        Padding in pixels between the legend and legend labels.
    labelSeparation : float
        The minimum separation that must be between label bounding boxes for them to be
        considered non-overlapping (default ``0`` ). This property is ignored if
        *labelOverlap* resolution is not enabled.
    layout : :class:`LegendLayout`
        Legend orient group layout parameters.
    legendX : float
        Custom x-position for legend with orient "none".
    legendY : float
        Custom y-position for legend with orient "none".
    offset : float
        The offset in pixels by which to displace the legend from the data rectangle and
        axes.

        **Default value:** ``18``.
    orient : :class:`LegendOrient`
        The orientation of the legend, which determines how the legend is positioned within
        the scene. One of "left", "right", "top-left", "top-right", "bottom-left",
        "bottom-right", "none".

        **Default value:** ``"right"``
    padding : float
        The padding between the border and content of the legend group.

        **Default value:** ``0``.
    rowPadding : float
        The vertical padding in pixels between symbol legend entries.

        **Default value:** ``2``.
    strokeColor : anyOf(None, :class:`Color`)
        Border stroke color for the full legend.
    strokeDash : List(float)
        Border stroke dash pattern for the full legend.
    strokeWidth : float
        Border stroke width for the full legend.
    symbolBaseFillColor : anyOf(None, :class:`Color`)
        Default fill color for legend symbols. Only applied if there is no ``"fill"`` scale
        color encoding for the legend.

        **Default value:** ``"transparent"``.
    symbolBaseStrokeColor : anyOf(None, :class:`Color`)
        Default stroke color for legend symbols. Only applied if there is no ``"fill"``
        scale color encoding for the legend.

        **Default value:** ``"gray"``.
    symbolDash : List(float)
        An array of alternating [stroke, space] lengths for dashed symbol strokes.
    symbolDashOffset : float
        The pixel offset at which to start drawing with the symbol stroke dash array.
    symbolDirection : :class:`Orientation`
        The default direction ( ``"horizontal"`` or ``"vertical"`` ) for symbol legends.

        **Default value:** ``"vertical"``.
    symbolFillColor : anyOf(None, :class:`Color`)
        The color of the legend symbol,
    symbolLimit : float
        The maximum number of allowed entries for a symbol legend. Additional entries will
        be dropped.
    symbolOffset : float
        Horizontal pixel offset for legend symbols.

        **Default value:** ``0``.
    symbolOpacity : float
        Opacity of the legend symbols.
    symbolSize : float
        The size of the legend symbol, in pixels.

        **Default value:** ``100``.
    symbolStrokeColor : anyOf(None, :class:`Color`)
        Stroke color for legend symbols.
    symbolStrokeWidth : float
        The width of the symbol's stroke.

        **Default value:** ``1.5``.
    symbolType : :class:`SymbolShape`
        The symbol shape. One of the plotting shapes ``circle`` (default), ``square``,
        ``cross``, ``diamond``, ``triangle-up``, ``triangle-down``, ``triangle-right``, or
        ``triangle-left``, the line symbol ``stroke``, or one of the centered directional
        shapes ``arrow``, ``wedge``, or ``triangle``. Alternatively, a custom `SVG path
        string <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ can be
        provided. For correct sizing, custom shape paths should be defined within a square
        bounding box with coordinates ranging from -1 to 1 along both the x and y
        dimensions.

        **Default value:** ``"circle"``.
    tickCount : anyOf(float, :class:`TimeInterval`)
        The desired number of tick values for quantitative legends.
    title : None
        Set to null to disable title for the axis, legend, or header.
    titleAlign : :class:`Align`
        Horizontal text alignment for legend titles.

        **Default value:** ``"left"``.
    titleAnchor : :class:`TitleAnchor`
        Text anchor position for placing legend titles.
    titleBaseline : :class:`TextBaseline`
        Vertical text baseline for legend titles.

        **Default value:** ``"top"``.
    titleColor : anyOf(None, :class:`Color`)
        The color of the legend title, can be in hex color code or regular color name.
    titleFont : string
        The font of the legend title.
    titleFontSize : float
        The font size of the legend title.
    titleFontStyle : :class:`FontStyle`
        The font style of the legend title.
    titleFontWeight : :class:`FontWeight`
        The font weight of the legend title.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    titleLimit : float
        Maximum allowed pixel width of legend titles.

        **Default value:** ``180``.
    titleLineHeight : float
        Line height in pixels for multi-line title text.
    titleOpacity : float
        Opacity of the legend title.
    titleOrient : :class:`Orient`
        Orientation of the legend title.
    titlePadding : float
        The padding, in pixels, between title and legend.

        **Default value:** ``5``.
    unselectedOpacity : float
        The opacity of unselected legend entries.

        **Default value:** 0.35.
    """
    _schema = {'$ref': '#/definitions/LegendConfig'}
    _rootschema = Root._schema

    def __init__(self, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined,
                 cornerRadius=Undefined, fillColor=Undefined, gradientDirection=Undefined,
                 gradientHorizontalMaxLength=Undefined, gradientHorizontalMinLength=Undefined,
                 gradientLabelLimit=Undefined, gradientLabelOffset=Undefined, gradientLength=Undefined,
                 gradientOpacity=Undefined, gradientStrokeColor=Undefined,
                 gradientStrokeWidth=Undefined, gradientThickness=Undefined,
                 gradientVerticalMaxLength=Undefined, gradientVerticalMinLength=Undefined,
                 gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined,
                 labelColor=Undefined, labelFont=Undefined, labelFontSize=Undefined,
                 labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined,
                 labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined,
                 labelPadding=Undefined, labelSeparation=Undefined, layout=Undefined, legendX=Undefined,
                 legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined,
                 rowPadding=Undefined, strokeColor=Undefined, strokeDash=Undefined,
                 strokeWidth=Undefined, symbolBaseFillColor=Undefined, symbolBaseStrokeColor=Undefined,
                 symbolDash=Undefined, symbolDashOffset=Undefined, symbolDirection=Undefined,
                 symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined,
                 symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined,
                 symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined,
                 title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined,
                 titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined,
                 titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined,
                 titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined,
                 titlePadding=Undefined, unselectedOpacity=Undefined, **kwds):
        super(LegendConfig, self).__init__(clipHeight=clipHeight, columnPadding=columnPadding,
                                           columns=columns, cornerRadius=cornerRadius,
                                           fillColor=fillColor, gradientDirection=gradientDirection,
                                           gradientHorizontalMaxLength=gradientHorizontalMaxLength,
                                           gradientHorizontalMinLength=gradientHorizontalMinLength,
                                           gradientLabelLimit=gradientLabelLimit,
                                           gradientLabelOffset=gradientLabelOffset,
                                           gradientLength=gradientLength,
                                           gradientOpacity=gradientOpacity,
                                           gradientStrokeColor=gradientStrokeColor,
                                           gradientStrokeWidth=gradientStrokeWidth,
                                           gradientThickness=gradientThickness,
                                           gradientVerticalMaxLength=gradientVerticalMaxLength,
                                           gradientVerticalMinLength=gradientVerticalMinLength,
                                           gridAlign=gridAlign, labelAlign=labelAlign,
                                           labelBaseline=labelBaseline, labelColor=labelColor,
                                           labelFont=labelFont, labelFontSize=labelFontSize,
                                           labelFontStyle=labelFontStyle,
                                           labelFontWeight=labelFontWeight, labelLimit=labelLimit,
                                           labelOffset=labelOffset, labelOpacity=labelOpacity,
                                           labelOverlap=labelOverlap, labelPadding=labelPadding,
                                           labelSeparation=labelSeparation, layout=layout,
                                           legendX=legendX, legendY=legendY, offset=offset,
                                           orient=orient, padding=padding, rowPadding=rowPadding,
                                           strokeColor=strokeColor, strokeDash=strokeDash,
                                           strokeWidth=strokeWidth,
                                           symbolBaseFillColor=symbolBaseFillColor,
                                           symbolBaseStrokeColor=symbolBaseStrokeColor,
                                           symbolDash=symbolDash, symbolDashOffset=symbolDashOffset,
                                           symbolDirection=symbolDirection,
                                           symbolFillColor=symbolFillColor, symbolLimit=symbolLimit,
                                           symbolOffset=symbolOffset, symbolOpacity=symbolOpacity,
                                           symbolSize=symbolSize, symbolStrokeColor=symbolStrokeColor,
                                           symbolStrokeWidth=symbolStrokeWidth, symbolType=symbolType,
                                           tickCount=tickCount, title=title, titleAlign=titleAlign,
                                           titleAnchor=titleAnchor, titleBaseline=titleBaseline,
                                           titleColor=titleColor, titleFont=titleFont,
                                           titleFontSize=titleFontSize, titleFontStyle=titleFontStyle,
                                           titleFontWeight=titleFontWeight, titleLimit=titleLimit,
                                           titleLineHeight=titleLineHeight, titleOpacity=titleOpacity,
                                           titleOrient=titleOrient, titlePadding=titlePadding,
                                           unselectedOpacity=unselectedOpacity, **kwds)


class LegendLayout(VegaLiteSchema):
    """LegendLayout schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    anchor : anyOf(:class:`TitleAnchor`, :class:`SignalRef`)
        The anchor point for legend orient group layout.
    bottom : :class:`BaseLegendLayout`

    bounds : :class:`LayoutBounds`
        The bounds calculation to use for legend orient group layout.
    center : anyOf(boolean, :class:`SignalRef`)
        A flag to center legends within a shared orient group.
    direction : anyOf(:class:`Orientation`, :class:`SignalRef`)
        The layout direction for legend orient group layout.
    left : :class:`BaseLegendLayout`

    margin : anyOf(float, :class:`SignalRef`)
        The pixel margin between legends within a orient group.
    offset : anyOf(float, :class:`SignalRef`)
        The pixel offset from the chart body for a legend orient group.
    right : :class:`BaseLegendLayout`

    top : :class:`BaseLegendLayout`

    bottom-left : :class:`BaseLegendLayout`

    bottom-right : :class:`BaseLegendLayout`

    top-left : :class:`BaseLegendLayout`

    top-right : :class:`BaseLegendLayout`

    """
    _schema = {'$ref': '#/definitions/LegendLayout'}
    _rootschema = Root._schema

    def __init__(self, anchor=Undefined, bottom=Undefined, bounds=Undefined, center=Undefined,
                 direction=Undefined, left=Undefined, margin=Undefined, offset=Undefined,
                 right=Undefined, top=Undefined, **kwds):
        super(LegendLayout, self).__init__(anchor=anchor, bottom=bottom, bounds=bounds, center=center,
                                           direction=direction, left=left, margin=margin, offset=offset,
                                           right=right, top=top, **kwds)


class LegendOrient(VegaLiteSchema):
    """LegendOrient schema wrapper

    enum('none', 'left', 'right', 'top', 'bottom', 'top-left', 'top-right', 'bottom-left',
    'bottom-right')
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

    fillOpacity : :class:`ResolveMode`

    opacity : :class:`ResolveMode`

    shape : :class:`ResolveMode`

    size : :class:`ResolveMode`

    stroke : :class:`ResolveMode`

    strokeOpacity : :class:`ResolveMode`

    strokeWidth : :class:`ResolveMode`

    """
    _schema = {'$ref': '#/definitions/LegendResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, fill=Undefined, fillOpacity=Undefined, opacity=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, **kwds):
        super(LegendResolveMap, self).__init__(color=color, fill=fill, fillOpacity=fillOpacity,
                                               opacity=opacity, shape=shape, size=size, stroke=stroke,
                                               strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                               **kwds)


class LegendStreamBinding(LegendBinding):
    """LegendStreamBinding schema wrapper

    Mapping(required=[legend])

    Attributes
    ----------

    legend : anyOf(string, :class:`Stream`)

    """
    _schema = {'$ref': '#/definitions/LegendStreamBinding'}
    _rootschema = Root._schema

    def __init__(self, legend=Undefined, **kwds):
        super(LegendStreamBinding, self).__init__(legend=legend, **kwds)


class LineConfig(VegaLiteSchema):
    """LineConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    """
    _schema = {'$ref': '#/definitions/LineConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, baseline=Undefined,
                 color=Undefined, cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, height=Undefined, href=Undefined, interpolate=Undefined,
                 invalid=Undefined, limit=Undefined, lineBreak=Undefined, lineHeight=Undefined,
                 opacity=Undefined, order=Undefined, orient=Undefined, point=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 timeUnitBand=Undefined, timeUnitBandPosition=Undefined, tooltip=Undefined,
                 width=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(LineConfig, self).__init__(align=align, angle=angle, aspect=aspect, baseline=baseline,
                                         color=color, cornerRadius=cornerRadius,
                                         cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                         cornerRadiusBottomRight=cornerRadiusBottomRight,
                                         cornerRadiusTopLeft=cornerRadiusTopLeft,
                                         cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                         dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         height=height, href=href, interpolate=interpolate,
                                         invalid=invalid, limit=limit, lineBreak=lineBreak,
                                         lineHeight=lineHeight, opacity=opacity, order=order,
                                         orient=orient, point=point, radius=radius, shape=shape,
                                         size=size, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta,
                                         timeUnitBand=timeUnitBand,
                                         timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                         width=width, x=x, x2=x2, y=y, y2=y2, **kwds)


class LinearGradient(Gradient):
    """LinearGradient schema wrapper

    Mapping(required=[gradient, stops])

    Attributes
    ----------

    gradient : enum('linear')
        The type of gradient. Use ``"linear"`` for a linear gradient.
    stops : List(:class:`GradientStop`)
        An array of gradient stops defining the gradient color sequence.
    id : string

    x1 : float
        The starting x-coordinate, in normalized [0, 1] coordinates, of the linear gradient.

        **Default value:** ``0``
    x2 : float
        The ending x-coordinate, in normalized [0, 1] coordinates, of the linear gradient.

        **Default value:** ``1``
    y1 : float
        The starting y-coordinate, in normalized [0, 1] coordinates, of the linear gradient.

        **Default value:** ``0``
    y2 : float
        The ending y-coordinate, in normalized [0, 1] coordinates, of the linear gradient.

        **Default value:** ``0``
    """
    _schema = {'$ref': '#/definitions/LinearGradient'}
    _rootschema = Root._schema

    def __init__(self, gradient=Undefined, stops=Undefined, id=Undefined, x1=Undefined, x2=Undefined,
                 y1=Undefined, y2=Undefined, **kwds):
        super(LinearGradient, self).__init__(gradient=gradient, stops=stops, id=id, x1=x1, x2=x2, y1=y1,
                                             y2=y2, **kwds)


class LogicalOperandPredicate(VegaLiteSchema):
    """LogicalOperandPredicate schema wrapper

    anyOf(:class:`LogicalNotPredicate`, :class:`LogicalAndPredicate`,
    :class:`LogicalOrPredicate`, :class:`Predicate`)
    """
    _schema = {'$ref': '#/definitions/LogicalOperand<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LogicalOperandPredicate, self).__init__(*args, **kwds)


class LogicalAndPredicate(LogicalOperandPredicate):
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


class LogicalNotPredicate(LogicalOperandPredicate):
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


class LogicalOrPredicate(LogicalOperandPredicate):
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


class LookupData(VegaLiteSchema):
    """LookupData schema wrapper

    Mapping(required=[data, key])

    Attributes
    ----------

    data : :class:`Data`
        Secondary data source to lookup in.
    key : :class:`FieldName`
        Key in data to lookup.
    fields : List(:class:`FieldName`)
        Fields in foreign data or selection to lookup.
        If not specified, the entire object is queried.
    """
    _schema = {'$ref': '#/definitions/LookupData'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, key=Undefined, fields=Undefined, **kwds):
        super(LookupData, self).__init__(data=data, key=key, fields=fields, **kwds)


class LookupSelection(VegaLiteSchema):
    """LookupSelection schema wrapper

    Mapping(required=[key, selection])

    Attributes
    ----------

    key : :class:`FieldName`
        Key in data to lookup.
    selection : string
        Selection name to look up.
    fields : List(:class:`FieldName`)
        Fields in foreign data or selection to lookup.
        If not specified, the entire object is queried.
    """
    _schema = {'$ref': '#/definitions/LookupSelection'}
    _rootschema = Root._schema

    def __init__(self, key=Undefined, selection=Undefined, fields=Undefined, **kwds):
        super(LookupSelection, self).__init__(key=key, selection=selection, fields=fields, **kwds)


class Mark(AnyMark):
    """Mark schema wrapper

    enum('area', 'bar', 'line', 'image', 'trail', 'point', 'text', 'tick', 'rect', 'rule',
    'circle', 'square', 'geoshape')
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

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    """
    _schema = {'$ref': '#/definitions/MarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, baseline=Undefined,
                 color=Undefined, cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, height=Undefined, href=Undefined, interpolate=Undefined,
                 invalid=Undefined, limit=Undefined, lineBreak=Undefined, lineHeight=Undefined,
                 opacity=Undefined, order=Undefined, orient=Undefined, radius=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeCap=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeJoin=Undefined,
                 strokeMiterLimit=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined,
                 tension=Undefined, text=Undefined, theta=Undefined, timeUnitBand=Undefined,
                 timeUnitBandPosition=Undefined, tooltip=Undefined, width=Undefined, x=Undefined,
                 x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(MarkConfig, self).__init__(align=align, angle=angle, aspect=aspect, baseline=baseline,
                                         color=color, cornerRadius=cornerRadius,
                                         cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                         cornerRadiusBottomRight=cornerRadiusBottomRight,
                                         cornerRadiusTopLeft=cornerRadiusTopLeft,
                                         cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                         dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         height=height, href=href, interpolate=interpolate,
                                         invalid=invalid, limit=limit, lineBreak=lineBreak,
                                         lineHeight=lineHeight, opacity=opacity, order=order,
                                         orient=orient, radius=radius, shape=shape, size=size,
                                         stroke=stroke, strokeCap=strokeCap, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                         strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, timeUnitBand=timeUnitBand,
                                         timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                         width=width, x=x, x2=x2, y=y, y2=y2, **kwds)


class MarkDef(AnyMark):
    """MarkDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`Mark`
        The mark type. This could a primitive mark type
        (one of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"geoshape"``, ``"rule"``, and ``"text"`` )
        or a composite mark type ( ``"boxplot"``, ``"errorband"``, ``"errorbar"`` ).
    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    binSpacing : float
        Offset between bars for binned field. The ideal value for this is either 0
        (preferred by statisticians) or 1 (Vega-Lite default, D3 example style).

        **Default value:** ``1``
    clip : boolean
        Whether a mark be clipped to the enclosing group’s width and height.
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
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
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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

        **Default value:** The mark's name. For example, a bar mark will have style
        ``"bar"`` by default.
        **Note:** Any specified style will augment the default style. For example, a bar
        mark with ``"style": "foo"`` will receive from ``config.style.bar`` and
        ``config.style.foo`` (the specified style ``"foo"`` has higher precedence).
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    thickness : float
        Thickness of the tick mark.

        **Default value:**  ``1``
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2Offset : float
        Offset for x2-position.
    xOffset : float
        Offset for x-position.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2Offset : float
        Offset for y2-position.
    yOffset : float
        Offset for y-position.
    """
    _schema = {'$ref': '#/definitions/MarkDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, align=Undefined, angle=Undefined, aspect=Undefined,
                 baseline=Undefined, binSpacing=Undefined, clip=Undefined, color=Undefined,
                 cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined,
                 dy=Undefined, ellipsis=Undefined, fill=Undefined, fillOpacity=Undefined,
                 filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, height=Undefined, href=Undefined, interpolate=Undefined,
                 invalid=Undefined, limit=Undefined, line=Undefined, lineBreak=Undefined,
                 lineHeight=Undefined, opacity=Undefined, order=Undefined, orient=Undefined,
                 point=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, thickness=Undefined, timeUnitBand=Undefined,
                 timeUnitBandPosition=Undefined, tooltip=Undefined, width=Undefined, x=Undefined,
                 x2=Undefined, x2Offset=Undefined, xOffset=Undefined, y=Undefined, y2=Undefined,
                 y2Offset=Undefined, yOffset=Undefined, **kwds):
        super(MarkDef, self).__init__(type=type, align=align, angle=angle, aspect=aspect,
                                      baseline=baseline, binSpacing=binSpacing, clip=clip, color=color,
                                      cornerRadius=cornerRadius,
                                      cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                      cornerRadiusBottomRight=cornerRadiusBottomRight,
                                      cornerRadiusTopLeft=cornerRadiusTopLeft,
                                      cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor, dir=dir,
                                      dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                      fillOpacity=fillOpacity, filled=filled, font=font,
                                      fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                      height=height, href=href, interpolate=interpolate,
                                      invalid=invalid, limit=limit, line=line, lineBreak=lineBreak,
                                      lineHeight=lineHeight, opacity=opacity, order=order,
                                      orient=orient, point=point, radius=radius, shape=shape, size=size,
                                      stroke=stroke, strokeCap=strokeCap, strokeDash=strokeDash,
                                      strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                      strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                      strokeWidth=strokeWidth, style=style, tension=tension, text=text,
                                      theta=theta, thickness=thickness, timeUnitBand=timeUnitBand,
                                      timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                      width=width, x=x, x2=x2, x2Offset=x2Offset, xOffset=xOffset, y=y,
                                      y2=y2, y2Offset=y2Offset, yOffset=yOffset, **kwds)


class MarkType(VegaLiteSchema):
    """MarkType schema wrapper

    enum('arc', 'area', 'image', 'group', 'line', 'path', 'rect', 'rule', 'shape', 'symbol',
    'text', 'trail')
    """
    _schema = {'$ref': '#/definitions/MarkType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(MarkType, self).__init__(*args)


class Month(VegaLiteSchema):
    """Month schema wrapper

    float
    """
    _schema = {'$ref': '#/definitions/Month'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Month, self).__init__(*args)


class MultiSelectionConfig(VegaLiteSchema):
    """MultiSelectionConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bind : :class:`LegendBinding`
        When set, a selection is populated by interacting with the corresponding legend.
        Direct manipulation interaction is disabled by default;
        to re-enable it, set the selection's `on
        <https://vega.github.io/vega-lite/docs/selection.html#common-selection-properties>`__
        property.

        Legend bindings are restricted to selections that only specify a single field or
        encoding.
    clear : anyOf(:class:`Stream`, string, boolean)
        Clears the selection, emptying it of all values. Can be a
        `Event Stream <https://vega.github.io/vega/docs/event-streams/>`__ or ``false`` to
        disable.

        **Default value:** ``dblclick``.

        **See also:** `clear <https://vega.github.io/vega-lite/docs/clear.html>`__
        documentation.
    empty : enum('all', 'none')
        By default, ``all`` data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefUnitChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.

        **See also:** `encodings <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    fields : List(:class:`FieldName`)
        An array of field names whose values must match for a data tuple to
        fall within the selection.

        **See also:** `fields <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    init : List(:class:`SelectionInitMapping`)
        Initialize the selection with a mapping between `projected channels or field names
        <https://vega.github.io/vega-lite/docs/project.html>`__ and an initial
        value (or array of values).

        **See also:** `init <https://vega.github.io/vega-lite/docs/init.html>`__
        documentation.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        **See also:** `nearest <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation.
    on : anyOf(:class:`Stream`, string)
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.

        **See also:** `resolve
        <https://vega.github.io/vega-lite/docs/selection-resolve.html>`__ documentation.
    toggle : anyOf(string, boolean)
        Controls whether data values should be toggled or only ever inserted into
        multi selections. Can be ``true``, ``false`` (for insertion only), or a
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__.

        **Default value:** ``true``, which corresponds to ``event.shiftKey`` (i.e.,
        data values are toggled when a user interacts with the shift-key pressed).

        **See also:** `toggle <https://vega.github.io/vega-lite/docs/toggle.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/MultiSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, clear=Undefined, empty=Undefined, encodings=Undefined,
                 fields=Undefined, init=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined,
                 toggle=Undefined, **kwds):
        super(MultiSelectionConfig, self).__init__(bind=bind, clear=clear, empty=empty,
                                                   encodings=encodings, fields=fields, init=init,
                                                   nearest=nearest, on=on, resolve=resolve,
                                                   toggle=toggle, **kwds)


class NamedData(DataSource):
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


class NonArgAggregateOp(Aggregate):
    """NonArgAggregateOp schema wrapper

    enum('average', 'count', 'distinct', 'max', 'mean', 'median', 'min', 'missing', 'q1', 'q3',
    'ci0', 'ci1', 'stderr', 'stdev', 'stdevp', 'sum', 'valid', 'values', 'variance',
    'variancep')
    """
    _schema = {'$ref': '#/definitions/NonArgAggregateOp'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(NonArgAggregateOp, self).__init__(*args)


class NumberValueDef(VegaLiteSchema):
    """NumberValueDef schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Attributes
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/NumberValueDef'}
    _rootschema = Root._schema

    def __init__(self, value=Undefined, **kwds):
        super(NumberValueDef, self).__init__(value=value, **kwds)


class NumericFieldDefWithCondition(VegaLiteSchema):
    """NumericFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalNumberValueDef`,
    List(:class:`ConditionalNumberValueDef`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/NumericFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(NumericFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                           condition=condition, field=field,
                                                           legend=legend, scale=scale, sort=sort,
                                                           timeUnit=timeUnit, title=title, **kwds)


class NumericValueDefWithCondition(VegaLiteSchema):
    """NumericValueDefWithCondition schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalNumberValueDef`,
    List(:class:`ConditionalNumberValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/NumericValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(NumericValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class OrderFieldDef(VegaLiteSchema):
    """OrderFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    sort : :class:`SortOrder`
        The sort order. One of ``"ascending"`` (default) or ``"descending"``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
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

    enum('left', 'right', 'top', 'bottom')
    """
    _schema = {'$ref': '#/definitions/Orient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Orient, self).__init__(*args)


class Orientation(VegaLiteSchema):
    """Orientation schema wrapper

    enum('horizontal', 'vertical')
    """
    _schema = {'$ref': '#/definitions/Orientation'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Orientation, self).__init__(*args)


class OverlayMarkDef(VegaLiteSchema):
    """OverlayMarkDef schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    clip : boolean
        Whether a mark be clipped to the enclosing group’s width and height.
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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

        **Default value:** The mark's name. For example, a bar mark will have style
        ``"bar"`` by default.
        **Note:** Any specified style will augment the default style. For example, a bar
        mark with ``"style": "foo"`` will receive from ``config.style.bar`` and
        ``config.style.foo`` (the specified style ``"foo"`` has higher precedence).
    tension : float
        Depending on the interpolation type, sets the tension parameter (for line and area
        marks).
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2Offset : float
        Offset for x2-position.
    xOffset : float
        Offset for x-position.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2Offset : float
        Offset for y2-position.
    yOffset : float
        Offset for y-position.
    """
    _schema = {'$ref': '#/definitions/OverlayMarkDef'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, baseline=Undefined,
                 clip=Undefined, color=Undefined, cornerRadius=Undefined,
                 cornerRadiusBottomLeft=Undefined, cornerRadiusBottomRight=Undefined,
                 cornerRadiusTopLeft=Undefined, cornerRadiusTopRight=Undefined, cursor=Undefined,
                 dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                 fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, height=Undefined, href=Undefined,
                 interpolate=Undefined, invalid=Undefined, limit=Undefined, lineBreak=Undefined,
                 lineHeight=Undefined, opacity=Undefined, order=Undefined, orient=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, timeUnitBand=Undefined, timeUnitBandPosition=Undefined,
                 tooltip=Undefined, width=Undefined, x=Undefined, x2=Undefined, x2Offset=Undefined,
                 xOffset=Undefined, y=Undefined, y2=Undefined, y2Offset=Undefined, yOffset=Undefined,
                 **kwds):
        super(OverlayMarkDef, self).__init__(align=align, angle=angle, aspect=aspect, baseline=baseline,
                                             clip=clip, color=color, cornerRadius=cornerRadius,
                                             cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                             cornerRadiusBottomRight=cornerRadiusBottomRight,
                                             cornerRadiusTopLeft=cornerRadiusTopLeft,
                                             cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                             dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                             fillOpacity=fillOpacity, filled=filled, font=font,
                                             fontSize=fontSize, fontStyle=fontStyle,
                                             fontWeight=fontWeight, height=height, href=href,
                                             interpolate=interpolate, invalid=invalid, limit=limit,
                                             lineBreak=lineBreak, lineHeight=lineHeight,
                                             opacity=opacity, order=order, orient=orient, radius=radius,
                                             shape=shape, size=size, stroke=stroke, strokeCap=strokeCap,
                                             strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                             strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                             strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                             style=style, tension=tension, text=text, theta=theta,
                                             timeUnitBand=timeUnitBand,
                                             timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                             width=width, x=x, x2=x2, x2Offset=x2Offset,
                                             xOffset=xOffset, y=y, y2=y2, y2Offset=y2Offset,
                                             yOffset=yOffset, **kwds)


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


class ParseValue(VegaLiteSchema):
    """ParseValue schema wrapper

    anyOf(None, string, enum('string'), enum('boolean'), enum('date'), enum('number'))
    """
    _schema = {'$ref': '#/definitions/ParseValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ParseValue, self).__init__(*args, **kwds)


class PartsMixinsBoxPlotPart(VegaLiteSchema):
    """PartsMixinsBoxPlotPart schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    box : anyOf(boolean, :class:`MarkConfig`)

    median : anyOf(boolean, :class:`MarkConfig`)

    outliers : anyOf(boolean, :class:`MarkConfig`)

    rule : anyOf(boolean, :class:`MarkConfig`)

    ticks : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/PartsMixins<BoxPlotPart>'}
    _rootschema = Root._schema

    def __init__(self, box=Undefined, median=Undefined, outliers=Undefined, rule=Undefined,
                 ticks=Undefined, **kwds):
        super(PartsMixinsBoxPlotPart, self).__init__(box=box, median=median, outliers=outliers,
                                                     rule=rule, ticks=ticks, **kwds)


class PartsMixinsErrorBandPart(VegaLiteSchema):
    """PartsMixinsErrorBandPart schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    band : anyOf(boolean, :class:`MarkConfig`)

    borders : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/PartsMixins<ErrorBandPart>'}
    _rootschema = Root._schema

    def __init__(self, band=Undefined, borders=Undefined, **kwds):
        super(PartsMixinsErrorBandPart, self).__init__(band=band, borders=borders, **kwds)


class PartsMixinsErrorBarPart(VegaLiteSchema):
    """PartsMixinsErrorBarPart schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    rule : anyOf(boolean, :class:`MarkConfig`)

    ticks : anyOf(boolean, :class:`MarkConfig`)

    """
    _schema = {'$ref': '#/definitions/PartsMixins<ErrorBarPart>'}
    _rootschema = Root._schema

    def __init__(self, rule=Undefined, ticks=Undefined, **kwds):
        super(PartsMixinsErrorBarPart, self).__init__(rule=rule, ticks=ticks, **kwds)


class PositionFieldDef(VegaLiteSchema):
    """PositionFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels.
        If ``null``, the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.

        **See also:** `axis <https://vega.github.io/vega-lite/docs/axis.html>`__
        documentation.
    band : float
        For rect-based marks ( ``rect``, ``bar``, and ``image`` ), mark size relative to
        bandwidth of `band scales <https://vega.github.io/vega-lite/docs/scale.html#band>`__
        or time units. If set to ``1``, the mark size is set to the bandwidth or the time
        unit interval. If set to ``0.5``, the mark size is half of the bandwidth or the time
        unit interval.

        For other marks, relative position on a band of a stacked, binned, time unit or band
        scale. If set to ``0``, the marks will be positioned at the beginning of the band.
        If set to ``0.5``, the marks will be positioned in the middle of the band.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    impute : anyOf(:class:`ImputeParams`, None)
        An object defining the properties of the Impute Operation to be applied.
        The field value of the other positional channel is taken as ``key`` of the
        ``Impute`` Operation.
        The field of the ``color`` channel if specified is used as ``groupby`` of the
        ``Impute`` Operation.

        **See also:** `impute <https://vega.github.io/vega-lite/docs/impute.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked.
        ``stack`` is only applicable for ``x`` and ``y`` channels with continuous domains.
        For example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__.
          :raw-html:`<br/>`
        - ``"center"`` - stacking with center baseline (for `streamgraph
        <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar`` or ``area`` ;
        (2) the stacked measure channel (x or y) has a linear scale;
        (3) At least one of non-position channels mapped to an unaggregated field that is
        different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/PositionFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, axis=Undefined, band=Undefined,
                 bin=Undefined, field=Undefined, impute=Undefined, scale=Undefined, sort=Undefined,
                 stack=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(PositionFieldDef, self).__init__(type=type, aggregate=aggregate, axis=axis, band=band,
                                               bin=bin, field=field, impute=impute, scale=scale,
                                               sort=sort, stack=stack, timeUnit=timeUnit, title=title,
                                               **kwds)


class Predicate(LogicalOperandPredicate):
    """Predicate schema wrapper

    anyOf(:class:`FieldEqualPredicate`, :class:`FieldRangePredicate`,
    :class:`FieldOneOfPredicate`, :class:`FieldLTPredicate`, :class:`FieldGTPredicate`,
    :class:`FieldLTEPredicate`, :class:`FieldGTEPredicate`, :class:`FieldValidPredicate`,
    :class:`SelectionPredicate`, string)
    """
    _schema = {'$ref': '#/definitions/Predicate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Predicate, self).__init__(*args, **kwds)


class FieldEqualPredicate(Predicate):
    """FieldEqualPredicate schema wrapper

    Mapping(required=[equal, field])

    Attributes
    ----------

    equal : anyOf(string, float, boolean, :class:`DateTime`)
        The value that the field should be equal to.
    field : :class:`FieldName`
        Field to be filtered.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldEqualPredicate'}
    _rootschema = Root._schema

    def __init__(self, equal=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldEqualPredicate, self).__init__(equal=equal, field=field, timeUnit=timeUnit, **kwds)


class FieldGTEPredicate(Predicate):
    """FieldGTEPredicate schema wrapper

    Mapping(required=[field, gte])

    Attributes
    ----------

    field : :class:`FieldName`
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


class FieldGTPredicate(Predicate):
    """FieldGTPredicate schema wrapper

    Mapping(required=[field, gt])

    Attributes
    ----------

    field : :class:`FieldName`
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


class FieldLTEPredicate(Predicate):
    """FieldLTEPredicate schema wrapper

    Mapping(required=[field, lte])

    Attributes
    ----------

    field : :class:`FieldName`
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


class FieldLTPredicate(Predicate):
    """FieldLTPredicate schema wrapper

    Mapping(required=[field, lt])

    Attributes
    ----------

    field : :class:`FieldName`
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


class FieldOneOfPredicate(Predicate):
    """FieldOneOfPredicate schema wrapper

    Mapping(required=[field, oneOf])

    Attributes
    ----------

    field : :class:`FieldName`
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


class FieldRangePredicate(Predicate):
    """FieldRangePredicate schema wrapper

    Mapping(required=[field, range])

    Attributes
    ----------

    field : :class:`FieldName`
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


class FieldValidPredicate(Predicate):
    """FieldValidPredicate schema wrapper

    Mapping(required=[field, valid])

    Attributes
    ----------

    field : :class:`FieldName`
        Field to be filtered.
    valid : boolean
        If set to true the field's value has to be valid, meaning both not ``null`` and not
        `NaN
        <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN>`__.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/FieldValidPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, valid=Undefined, timeUnit=Undefined, **kwds):
        super(FieldValidPredicate, self).__init__(field=field, valid=valid, timeUnit=timeUnit, **kwds)


class Projection(VegaLiteSchema):
    """Projection schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    center : :class:`Vector2number`
        The projection’s center to the specified center, a two-element array of longitude
        and latitude in degrees.

        **Default value:** ``[0, 0]``
    clipAngle : float
        The projection’s clipping circle radius to the specified angle in degrees. If
        ``null``, switches to `antimeridian <http://bl.ocks.org/mbostock/3788999>`__ cutting
        rather than small-circle clipping.
    clipExtent : :class:`Vector2Vector2number`
        The projection’s viewport clip extent to the specified bounds in pixels. The extent
        bounds are specified as an array ``[[x0, y0], [x1, y1]]``, where ``x0`` is the
        left-side of the viewport, ``y0`` is the top, ``x1`` is the right and ``y1`` is the
        bottom. If ``null``, no viewport clipping is performed.
    coefficient : float

    distance : float

    fraction : float

    lobes : float

    parallel : float

    parallels : List(float)

    precision : float
        The threshold for the projection’s `adaptive resampling
        <http://bl.ocks.org/mbostock/3795544>`__ to the specified value in pixels. This
        value corresponds to the `Douglas–Peucker distance
        <http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm>`__.
        If precision is not specified, returns the projection’s current resampling precision
        which defaults to ``√0.5 ≅ 0.70710…``.
    radius : float

    ratio : float

    reflectX : boolean

    reflectY : boolean

    rotate : anyOf(:class:`Vector2number`, :class:`Vector3number`)
        The projection’s three-axis rotation to the specified angles, which must be a two-
        or three-element array of numbers [ ``lambda``, ``phi``, ``gamma`` ] specifying the
        rotation angles in degrees about each spherical axis. (These correspond to yaw,
        pitch and roll.)

        **Default value:** ``[0, 0, 0]``
    scale : float
        The projection's scale (zoom) value, overriding automatic fitting.
    spacing : float

    tilt : float

    translate : :class:`Vector2number`
        The projection's translation (pan) value, overriding automatic fitting.
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
                 parallel=Undefined, parallels=Undefined, precision=Undefined, radius=Undefined,
                 ratio=Undefined, reflectX=Undefined, reflectY=Undefined, rotate=Undefined,
                 scale=Undefined, spacing=Undefined, tilt=Undefined, translate=Undefined,
                 type=Undefined, **kwds):
        super(Projection, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent,
                                         coefficient=coefficient, distance=distance, fraction=fraction,
                                         lobes=lobes, parallel=parallel, parallels=parallels,
                                         precision=precision, radius=radius, ratio=ratio,
                                         reflectX=reflectX, reflectY=reflectY, rotate=rotate,
                                         scale=scale, spacing=spacing, tilt=tilt, translate=translate,
                                         type=type, **kwds)


class ProjectionConfig(VegaLiteSchema):
    """ProjectionConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    center : :class:`Vector2number`
        The projection’s center to the specified center, a two-element array of longitude
        and latitude in degrees.

        **Default value:** ``[0, 0]``
    clipAngle : float
        The projection’s clipping circle radius to the specified angle in degrees. If
        ``null``, switches to `antimeridian <http://bl.ocks.org/mbostock/3788999>`__ cutting
        rather than small-circle clipping.
    clipExtent : :class:`Vector2Vector2number`
        The projection’s viewport clip extent to the specified bounds in pixels. The extent
        bounds are specified as an array ``[[x0, y0], [x1, y1]]``, where ``x0`` is the
        left-side of the viewport, ``y0`` is the top, ``x1`` is the right and ``y1`` is the
        bottom. If ``null``, no viewport clipping is performed.
    coefficient : float

    distance : float

    fraction : float

    lobes : float

    parallel : float

    parallels : List(float)

    precision : float
        The threshold for the projection’s `adaptive resampling
        <http://bl.ocks.org/mbostock/3795544>`__ to the specified value in pixels. This
        value corresponds to the `Douglas–Peucker distance
        <http://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm>`__.
        If precision is not specified, returns the projection’s current resampling precision
        which defaults to ``√0.5 ≅ 0.70710…``.
    radius : float

    ratio : float

    reflectX : boolean

    reflectY : boolean

    rotate : anyOf(:class:`Vector2number`, :class:`Vector3number`)
        The projection’s three-axis rotation to the specified angles, which must be a two-
        or three-element array of numbers [ ``lambda``, ``phi``, ``gamma`` ] specifying the
        rotation angles in degrees about each spherical axis. (These correspond to yaw,
        pitch and roll.)

        **Default value:** ``[0, 0, 0]``
    scale : float
        The projection's scale (zoom) value, overriding automatic fitting.
    spacing : float

    tilt : float

    translate : :class:`Vector2number`
        The projection's translation (pan) value, overriding automatic fitting.
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
                 parallel=Undefined, parallels=Undefined, precision=Undefined, radius=Undefined,
                 ratio=Undefined, reflectX=Undefined, reflectY=Undefined, rotate=Undefined,
                 scale=Undefined, spacing=Undefined, tilt=Undefined, translate=Undefined,
                 type=Undefined, **kwds):
        super(ProjectionConfig, self).__init__(center=center, clipAngle=clipAngle,
                                               clipExtent=clipExtent, coefficient=coefficient,
                                               distance=distance, fraction=fraction, lobes=lobes,
                                               parallel=parallel, parallels=parallels,
                                               precision=precision, radius=radius, ratio=ratio,
                                               reflectX=reflectX, reflectY=reflectY, rotate=rotate,
                                               scale=scale, spacing=spacing, tilt=tilt,
                                               translate=translate, type=type, **kwds)


class ProjectionType(VegaLiteSchema):
    """ProjectionType schema wrapper

    enum('albers', 'albersUsa', 'azimuthalEqualArea', 'azimuthalEquidistant', 'conicConformal',
    'conicEqualArea', 'conicEquidistant', 'equalEarth', 'equirectangular', 'gnomonic',
    'identity', 'mercator', 'naturalEarth1', 'orthographic', 'stereographic',
    'transverseMercator')
    """
    _schema = {'$ref': '#/definitions/ProjectionType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ProjectionType, self).__init__(*args)


class RadialGradient(Gradient):
    """RadialGradient schema wrapper

    Mapping(required=[gradient, stops])

    Attributes
    ----------

    gradient : enum('radial')
        The type of gradient. Use ``"radial"`` for a radial gradient.
    stops : List(:class:`GradientStop`)
        An array of gradient stops defining the gradient color sequence.
    id : string

    r1 : float
        The radius length, in normalized [0, 1] coordinates, of the inner circle for the
        gradient.

        **Default value:** ``0``
    r2 : float
        The radius length, in normalized [0, 1] coordinates, of the outer circle for the
        gradient.

        **Default value:** ``0.5``
    x1 : float
        The x-coordinate, in normalized [0, 1] coordinates, for the center of the inner
        circle for the gradient.

        **Default value:** ``0.5``
    x2 : float
        The x-coordinate, in normalized [0, 1] coordinates, for the center of the outer
        circle for the gradient.

        **Default value:** ``0.5``
    y1 : float
        The y-coordinate, in normalized [0, 1] coordinates, for the center of the inner
        circle for the gradient.

        **Default value:** ``0.5``
    y2 : float
        The y-coordinate, in normalized [0, 1] coordinates, for the center of the outer
        circle for the gradient.

        **Default value:** ``0.5``
    """
    _schema = {'$ref': '#/definitions/RadialGradient'}
    _rootschema = Root._schema

    def __init__(self, gradient=Undefined, stops=Undefined, id=Undefined, r1=Undefined, r2=Undefined,
                 x1=Undefined, x2=Undefined, y1=Undefined, y2=Undefined, **kwds):
        super(RadialGradient, self).__init__(gradient=gradient, stops=stops, id=id, r1=r1, r2=r2, x1=x1,
                                             x2=x2, y1=y1, y2=y2, **kwds)


class RangeConfig(VegaLiteSchema):
    """RangeConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    category : anyOf(:class:`RangeScheme`, List(string))
        Default `color scheme <https://vega.github.io/vega/docs/schemes/>`__ for categorical
        data.
    diverging : anyOf(:class:`RangeScheme`, List(string))
        Default `color scheme <https://vega.github.io/vega/docs/schemes/>`__ for diverging
        quantitative ramps.
    heatmap : anyOf(:class:`RangeScheme`, List(string))
        Default `color scheme <https://vega.github.io/vega/docs/schemes/>`__ for
        quantitative heatmaps.
    ordinal : anyOf(:class:`RangeScheme`, List(string))
        Default `color scheme <https://vega.github.io/vega/docs/schemes/>`__ for
        rank-ordered data.
    ramp : anyOf(:class:`RangeScheme`, List(string))
        Default `color scheme <https://vega.github.io/vega/docs/schemes/>`__ for sequential
        quantitative ramps.
    symbol : List(:class:`SymbolShape`)
        Array of `symbol <https://vega.github.io/vega/docs/marks/symbol/>`__ names or paths
        for the default shape palette.
    """
    _schema = {'$ref': '#/definitions/RangeConfig'}
    _rootschema = Root._schema

    def __init__(self, category=Undefined, diverging=Undefined, heatmap=Undefined, ordinal=Undefined,
                 ramp=Undefined, symbol=Undefined, **kwds):
        super(RangeConfig, self).__init__(category=category, diverging=diverging, heatmap=heatmap,
                                          ordinal=ordinal, ramp=ramp, symbol=symbol, **kwds)


class RangeRawArray(VegaLiteSchema):
    """RangeRawArray schema wrapper

    List(anyOf(float, :class:`SignalRef`))
    """
    _schema = {'$ref': '#/definitions/RangeRawArray'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(RangeRawArray, self).__init__(*args)


class RangeScheme(VegaLiteSchema):
    """RangeScheme schema wrapper

    anyOf(:class:`RangeEnum`, :class:`RangeRaw`, :class:`SignalRef`, Mapping(required=[scheme]))
    """
    _schema = {'$ref': '#/definitions/RangeScheme'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(RangeScheme, self).__init__(*args, **kwds)


class RangeEnum(RangeScheme):
    """RangeEnum schema wrapper

    enum('width', 'height', 'symbol', 'category', 'ordinal', 'ramp', 'diverging', 'heatmap')
    """
    _schema = {'$ref': '#/definitions/RangeEnum'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(RangeEnum, self).__init__(*args)


class RangeRaw(RangeScheme):
    """RangeRaw schema wrapper

    List(anyOf(None, boolean, string, float, :class:`SignalRef`, :class:`RangeRawArray`))
    """
    _schema = {'$ref': '#/definitions/RangeRaw'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(RangeRaw, self).__init__(*args)


class RectConfig(VegaLiteSchema):
    """RectConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    binSpacing : float
        Offset between bars for binned field. The ideal value for this is either 0
        (preferred by statisticians) or 1 (Vega-Lite default, D3 example style).

        **Default value:** ``1``
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    continuousBandSize : float
        The default size of the bars on continuous scales.

        **Default value:** ``5``
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
        The default size of the bars with discrete dimensions. If unspecified, the default
        size is  ``step-2``, which provides 2 pixel offset between bars.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the *angle* property.
    ellipsis : string
        The ellipsis string for text truncated in response to the limit parameter.

        **Default value:** ``"…"``
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    """
    _schema = {'$ref': '#/definitions/RectConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, baseline=Undefined,
                 binSpacing=Undefined, color=Undefined, continuousBandSize=Undefined,
                 cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, dir=Undefined,
                 discreteBandSize=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined,
                 fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, height=Undefined,
                 href=Undefined, interpolate=Undefined, invalid=Undefined, limit=Undefined,
                 lineBreak=Undefined, lineHeight=Undefined, opacity=Undefined, order=Undefined,
                 orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 timeUnitBand=Undefined, timeUnitBandPosition=Undefined, tooltip=Undefined,
                 width=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(RectConfig, self).__init__(align=align, angle=angle, aspect=aspect, baseline=baseline,
                                         binSpacing=binSpacing, color=color,
                                         continuousBandSize=continuousBandSize,
                                         cornerRadius=cornerRadius,
                                         cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                         cornerRadiusBottomRight=cornerRadiusBottomRight,
                                         cornerRadiusTopLeft=cornerRadiusTopLeft,
                                         cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                         dir=dir, discreteBandSize=discreteBandSize, dx=dx, dy=dy,
                                         ellipsis=ellipsis, fill=fill, fillOpacity=fillOpacity,
                                         filled=filled, font=font, fontSize=fontSize,
                                         fontStyle=fontStyle, fontWeight=fontWeight, height=height,
                                         href=href, interpolate=interpolate, invalid=invalid,
                                         limit=limit, lineBreak=lineBreak, lineHeight=lineHeight,
                                         opacity=opacity, order=order, orient=orient, radius=radius,
                                         shape=shape, size=size, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         tension=tension, text=text, theta=theta,
                                         timeUnitBand=timeUnitBand,
                                         timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                         width=width, x=x, x2=x2, y=y, y2=y2, **kwds)


class RepeatMapping(VegaLiteSchema):
    """RepeatMapping schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : List(string)
        An array of fields to be repeated horizontally.
    row : List(string)
        An array of fields to be repeated vertically.
    """
    _schema = {'$ref': '#/definitions/RepeatMapping'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(RepeatMapping, self).__init__(column=column, row=row, **kwds)


class RepeatRef(Field):
    """RepeatRef schema wrapper

    Mapping(required=[repeat])
    Reference to a repeated value.

    Attributes
    ----------

    repeat : enum('row', 'column', 'repeat')

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
    Scales and guides can be resolved to be ``"independent"`` or ``"shared"``.

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


class RowColLayoutAlign(VegaLiteSchema):
    """RowColLayoutAlign schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : :class:`LayoutAlign`

    row : :class:`LayoutAlign`

    """
    _schema = {'$ref': '#/definitions/RowCol<LayoutAlign>'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(RowColLayoutAlign, self).__init__(column=column, row=row, **kwds)


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


class RowColumnEncodingFieldDef(VegaLiteSchema):
    """RowColumnEncodingFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    align : :class:`LayoutAlign`
        The alignment to apply to row/column facet's subplot.
        The supported string values are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        **Default value:** ``"all"``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    center : boolean
        Boolean flag indicating if facet's subviews should be centered relative to their
        respective rows or columns.

        **Default value:** ``false``
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    header : :class:`Header`
        An object defining properties of a facet's header.
    sort : anyOf(:class:`SortArray`, :class:`SortOrder`, :class:`EncodingSortField`, None)
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    spacing : float
        The spacing in pixels between facet's sub-views.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/RowColumnEncodingFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, align=Undefined, bin=Undefined,
                 center=Undefined, field=Undefined, header=Undefined, sort=Undefined, spacing=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(RowColumnEncodingFieldDef, self).__init__(type=type, aggregate=aggregate, align=align,
                                                        bin=bin, center=center, field=field,
                                                        header=header, sort=sort, spacing=spacing,
                                                        timeUnit=timeUnit, title=title, **kwds)


class Scale(VegaLiteSchema):
    """Scale schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : float
        The alignment of the steps within the scale range.

        This value must lie in the range ``[0,1]``. A value of ``0.5`` indicates that the
        steps should be centered within the range. A value of ``0`` or ``1`` may be used to
        shift the bands to one side, say to position them adjacent to an axis.

        **Default value:** ``0.5``
    base : float
        The logarithm base of the ``log`` scale (default ``10`` ).
    bins : List(float)
        An array of bin boundaries over the scale domain. If provided, axes and legends will
        use the bin boundaries to inform the choice of tick marks and text labels.
    clamp : boolean
        If ``true``, values that exceed the data domain are clamped to either the minimum or
        maximum range value

        **Default value:** derived from the `scale config
        <https://vega.github.io/vega-lite/docs/config.html#scale-config>`__ 's ``clamp`` (
        ``true`` by default).
    constant : float
        A constant determining the slope of the symlog function around zero. Only used for
        ``symlog`` scales.

        **Default value:** ``1``
    domain : anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`),
    enum('unaggregated'), :class:`SelectionExtent`)
        Customized domain values.

        For *quantitative* fields, ``domain`` can take the form of a two-element array with
        minimum and maximum values. `Piecewise scales
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
        numbers, dates, strings and colors (in HCL space) is used. For color ranges, this
        property allows interpolation in alternative color spaces. Legal values include
        ``rgb``, ``hsl``, ``hsl-long``, ``lab``, ``hcl``, ``hcl-long``, ``cubehelix`` and
        ``cubehelix-long`` ('-long' variants use longer paths in polar coordinate spaces).
        If object-valued, this property accepts an object with a string-valued *type*
        property and an optional numeric *gamma* property applicable to rgb and cubehelix
        interpolators. For more, see the `d3-interpolate documentation
        <https://github.com/d3/d3-interpolate>`__.


        * **Default value:** ``hcl``
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
        function as intended. Padding adjustment is performed prior to all other
        adjustments, including the effects of the  ``zero``,  ``nice``,  ``domainMin``, and
        ``domainMax``  properties.

        For * `band <https://vega.github.io/vega-lite/docs/scale.html#band>`__ * scales,
        shortcut for setting ``paddingInner`` and ``paddingOuter`` to the same value.

        For * `point <https://vega.github.io/vega-lite/docs/scale.html#point>`__ * scales,
        alias for ``paddingOuter``.

        **Default value:** For *continuous* scales, derived from the `scale config
        <https://vega.github.io/vega-lite/docs/scale.html#config>`__ 's
        ``continuousPadding``.
        For *band and point* scales, see ``paddingInner`` and ``paddingOuter``. By default,
        Vega-Lite sets padding such that *width/height = number of unique values * step*.
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
        By default, Vega-Lite sets outer padding such that *width/height = number of unique
        values * step*.
    range : anyOf(List(float), List(string), :class:`RangeEnum`)
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

        1) For color scales you can also specify a color `scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__ instead of ``range``.

        2) Any directly specified ``range`` for ``x`` and ``y`` channels will be ignored.
        Range can be customized via the view's corresponding `size
        <https://vega.github.io/vega-lite/docs/size.html>`__ ( ``width`` and ``height`` ).
    round : boolean
        If ``true``, rounds numeric output values to integers. This can be helpful for
        snapping to the pixel grid.

        **Default value:** ``false``.
    scheme : anyOf(string, :class:`SchemeParams`)
        A string indicating a color `scheme
        <https://vega.github.io/vega-lite/docs/scale.html#scheme>`__ name (e.g.,
        ``"category10"`` or ``"blues"`` ) or a `scheme parameter object
        <https://vega.github.io/vega-lite/docs/scale.html#scheme-params>`__.

        Discrete color schemes may be used with `discrete
        <https://vega.github.io/vega-lite/docs/scale.html#discrete>`__ or `discretizing
        <https://vega.github.io/vega-lite/docs/scale.html#discretizing>`__ scales.
        Continuous color schemes are intended for use with color scales.

        For the full list of supported schemes, please refer to the `Vega Scheme
        <https://vega.github.io/vega/docs/schemes/#reference>`__ reference.
    type : :class:`ScaleType`
        The type of scale. Vega-Lite supports the following categories of scale types:

        1) `Continuous Scales
        <https://vega.github.io/vega-lite/docs/scale.html#continuous>`__ -- mapping
        continuous domains to continuous output ranges ( `"linear"
        <https://vega.github.io/vega-lite/docs/scale.html#linear>`__, `"pow"
        <https://vega.github.io/vega-lite/docs/scale.html#pow>`__, `"sqrt"
        <https://vega.github.io/vega-lite/docs/scale.html#sqrt>`__, `"symlog"
        <https://vega.github.io/vega-lite/docs/scale.html#symlog>`__, `"log"
        <https://vega.github.io/vega-lite/docs/scale.html#log>`__, `"time"
        <https://vega.github.io/vega-lite/docs/scale.html#time>`__, `"utc"
        <https://vega.github.io/vega-lite/docs/scale.html#utc>`__.

        2) `Discrete Scales <https://vega.github.io/vega-lite/docs/scale.html#discrete>`__
        -- mapping discrete domains to discrete ( `"ordinal"
        <https://vega.github.io/vega-lite/docs/scale.html#ordinal>`__ ) or continuous (
        `"band" <https://vega.github.io/vega-lite/docs/scale.html#band>`__ and `"point"
        <https://vega.github.io/vega-lite/docs/scale.html#point>`__ ) output ranges.

        3) `Discretizing Scales
        <https://vega.github.io/vega-lite/docs/scale.html#discretizing>`__ -- mapping
        continuous domains to discrete output ranges `"bin-ordinal"
        <https://vega.github.io/vega-lite/docs/scale.html#bin-ordinal>`__, `"quantile"
        <https://vega.github.io/vega-lite/docs/scale.html#quantile>`__, `"quantize"
        <https://vega.github.io/vega-lite/docs/scale.html#quantize>`__ and `"threshold"
        <https://vega.github.io/vega-lite/docs/scale.html#threshold>`__.

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

    def __init__(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined,
                 constant=Undefined, domain=Undefined, exponent=Undefined, interpolate=Undefined,
                 nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined,
                 range=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined,
                 **kwds):
        super(Scale, self).__init__(align=align, base=base, bins=bins, clamp=clamp, constant=constant,
                                    domain=domain, exponent=exponent, interpolate=interpolate,
                                    nice=nice, padding=padding, paddingInner=paddingInner,
                                    paddingOuter=paddingOuter, range=range, round=round, scheme=scheme,
                                    type=type, zero=zero, **kwds)


class ScaleConfig(VegaLiteSchema):
    """ScaleConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bandPaddingInner : float
        Default inner padding for ``x`` and ``y`` band-ordinal scales.

        **Default value:**


        * ``barBandPaddingInner`` for bar marks ( ``0.1`` by default)
        * ``rectBandPaddingInner`` for rect and other marks ( ``0`` by default)
    bandPaddingOuter : float
        Default outer padding for ``x`` and ``y`` band-ordinal scales.

        **Default value:** ``paddingInner/2`` (which makes *width/height = number of unique
        values * step* )
    barBandPaddingInner : float
        Default inner padding for ``x`` and ``y`` band-ordinal scales of ``"bar"`` marks.

        **Default value:** ``0.1``
    clamp : boolean
        If true, values that exceed the data domain are clamped to either the minimum or
        maximum range value
    continuousPadding : float
        Default padding for continuous scales.

        **Default:** ``5`` for continuous x-scale of a vertical bar and continuous y-scale
        of a horizontal bar.; ``0`` otherwise.
    maxBandSize : float
        The default max value for mapping quantitative fields to bar's size/bandSize.

        If undefined (default), we will use the axis's size (width or height) - 1.
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

        **Default value:** ``0.5`` (which makes *width/height = number of unique values *
        step* )
    quantileCount : float
        Default range cardinality for `quantile
        <https://vega.github.io/vega-lite/docs/scale.html#quantile>`__ scale.

        **Default value:** ``4``
    quantizeCount : float
        Default range cardinality for `quantize
        <https://vega.github.io/vega-lite/docs/scale.html#quantize>`__ scale.

        **Default value:** ``4``
    rectBandPaddingInner : float
        Default inner padding for ``x`` and ``y`` band-ordinal scales of ``"rect"`` marks.

        **Default value:** ``0``
    round : boolean
        If true, rounds numeric output values to integers.
        This can be helpful for snapping to the pixel grid.
        (Only available for ``x``, ``y``, and ``size`` scales.)
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

    def __init__(self, bandPaddingInner=Undefined, bandPaddingOuter=Undefined,
                 barBandPaddingInner=Undefined, clamp=Undefined, continuousPadding=Undefined,
                 maxBandSize=Undefined, maxFontSize=Undefined, maxOpacity=Undefined, maxSize=Undefined,
                 maxStrokeWidth=Undefined, minBandSize=Undefined, minFontSize=Undefined,
                 minOpacity=Undefined, minSize=Undefined, minStrokeWidth=Undefined,
                 pointPadding=Undefined, quantileCount=Undefined, quantizeCount=Undefined,
                 rectBandPaddingInner=Undefined, round=Undefined, useUnaggregatedDomain=Undefined,
                 **kwds):
        super(ScaleConfig, self).__init__(bandPaddingInner=bandPaddingInner,
                                          bandPaddingOuter=bandPaddingOuter,
                                          barBandPaddingInner=barBandPaddingInner, clamp=clamp,
                                          continuousPadding=continuousPadding, maxBandSize=maxBandSize,
                                          maxFontSize=maxFontSize, maxOpacity=maxOpacity,
                                          maxSize=maxSize, maxStrokeWidth=maxStrokeWidth,
                                          minBandSize=minBandSize, minFontSize=minFontSize,
                                          minOpacity=minOpacity, minSize=minSize,
                                          minStrokeWidth=minStrokeWidth, pointPadding=pointPadding,
                                          quantileCount=quantileCount, quantizeCount=quantizeCount,
                                          rectBandPaddingInner=rectBandPaddingInner, round=round,
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

    fillOpacity : :class:`ResolveMode`

    opacity : :class:`ResolveMode`

    shape : :class:`ResolveMode`

    size : :class:`ResolveMode`

    stroke : :class:`ResolveMode`

    strokeOpacity : :class:`ResolveMode`

    strokeWidth : :class:`ResolveMode`

    x : :class:`ResolveMode`

    y : :class:`ResolveMode`

    """
    _schema = {'$ref': '#/definitions/ScaleResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, fill=Undefined, fillOpacity=Undefined, opacity=Undefined,
                 shape=Undefined, size=Undefined, stroke=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, x=Undefined, y=Undefined, **kwds):
        super(ScaleResolveMap, self).__init__(color=color, fill=fill, fillOpacity=fillOpacity,
                                              opacity=opacity, shape=shape, size=size, stroke=stroke,
                                              strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, x=x,
                                              y=y, **kwds)


class ScaleType(VegaLiteSchema):
    """ScaleType schema wrapper

    enum('linear', 'log', 'pow', 'sqrt', 'symlog', 'time', 'utc', 'quantile', 'quantize',
    'threshold', 'bin-ordinal', 'ordinal', 'point', 'band')
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
        A color scheme name for ordinal scales (e.g., ``"category10"`` or ``"blues"`` ).

        For the full list of supported schemes, please refer to the `Vega Scheme
        <https://vega.github.io/vega/docs/schemes/#reference>`__ reference.
    count : float
        The number of colors to use in the scheme. This can be useful for scale types such
        as ``"quantize"``, which use the length of the scale range to determine the number
        of discrete bins for the scale domain.
    extent : List(float)
        The extent of the color range to use. For example ``[0.2, 1]`` will rescale the
        color scheme such that color values in the range *[0, 0.2)* are excluded from the
        scheme.
    """
    _schema = {'$ref': '#/definitions/SchemeParams'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, count=Undefined, extent=Undefined, **kwds):
        super(SchemeParams, self).__init__(name=name, count=count, extent=extent, **kwds)


class SecondaryFieldDef(VegaLiteSchema):
    """SecondaryFieldDef schema wrapper

    Mapping(required=[])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Attributes
    ----------

    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/SecondaryFieldDef'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(SecondaryFieldDef, self).__init__(aggregate=aggregate, bin=bin, field=field,
                                                timeUnit=timeUnit, title=title, **kwds)


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


class IntervalSelection(SelectionDef):
    """IntervalSelection schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('interval')
        Determines the default event processing and data query for the selection. Vega-Lite
        currently supports three selection types:


        * ``"single"`` -- to select a single discrete data value on ``click``.
        * ``"multi"`` -- to select multiple discrete data value; the first value is selected
          on ``click`` and additional values toggled on shift- ``click``.
        * ``"interval"`` -- to select a continuous range of data values on ``drag``.
    bind : enum('scales')
        Establishes a two-way binding between the interval selection and the scales
        used within the same view. This allows a user to interactively pan and
        zoom the view.

        **See also:** `bind <https://vega.github.io/vega-lite/docs/bind.html>`__
        documentation.
    clear : anyOf(:class:`Stream`, string, boolean)
        Clears the selection, emptying it of all values. Can be a
        `Event Stream <https://vega.github.io/vega/docs/event-streams/>`__ or ``false`` to
        disable.

        **Default value:** ``dblclick``.

        **See also:** `clear <https://vega.github.io/vega-lite/docs/clear.html>`__
        documentation.
    empty : enum('all', 'none')
        By default, ``all`` data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefUnitChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.

        **See also:** `encodings <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    fields : List(:class:`FieldName`)
        An array of field names whose values must match for a data tuple to
        fall within the selection.

        **See also:** `fields <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    init : :class:`SelectionInitIntervalMapping`
        Initialize the selection with a mapping between `projected channels or field names
        <https://vega.github.io/vega-lite/docs/project.html>`__ and arrays of
        initial values.

        **See also:** `init <https://vega.github.io/vega-lite/docs/init.html>`__
        documentation.
    mark : :class:`BrushConfig`
        An interval selection also adds a rectangle mark to depict the
        extents of the interval. The ``mark`` property can be used to customize the
        appearance of the mark.

        **See also:** `mark <https://vega.github.io/vega-lite/docs/selection-mark.html>`__
        documentation.
    on : anyOf(:class:`Stream`, string)
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.

        **See also:** `resolve
        <https://vega.github.io/vega-lite/docs/selection-resolve.html>`__ documentation.
    translate : anyOf(string, boolean)
        When truthy, allows a user to interactively move an interval selection
        back-and-forth. Can be ``true``, ``false`` (to disable panning), or a
        `Vega event stream definition <https://vega.github.io/vega/docs/event-streams/>`__
        which must include a start and end event to trigger continuous panning.

        **Default value:** ``true``, which corresponds to
        ``[mousedown, window:mouseup] > window:mousemove!`` which corresponds to
        clicks and dragging within an interval selection to reposition it.

        **See also:** `translate <https://vega.github.io/vega-lite/docs/translate.html>`__
        documentation.
    zoom : anyOf(string, boolean)
        When truthy, allows a user to interactively resize an interval selection.
        Can be ``true``, ``false`` (to disable zooming), or a `Vega event stream
        definition <https://vega.github.io/vega/docs/event-streams/>`__. Currently,
        only ``wheel`` events are supported.

        **Default value:** ``true``, which corresponds to ``wheel!``.

        **See also:** `zoom <https://vega.github.io/vega-lite/docs/zoom.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/IntervalSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, clear=Undefined, empty=Undefined,
                 encodings=Undefined, fields=Undefined, init=Undefined, mark=Undefined, on=Undefined,
                 resolve=Undefined, translate=Undefined, zoom=Undefined, **kwds):
        super(IntervalSelection, self).__init__(type=type, bind=bind, clear=clear, empty=empty,
                                                encodings=encodings, fields=fields, init=init,
                                                mark=mark, on=on, resolve=resolve, translate=translate,
                                                zoom=zoom, **kwds)


class MultiSelection(SelectionDef):
    """MultiSelection schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('multi')
        Determines the default event processing and data query for the selection. Vega-Lite
        currently supports three selection types:


        * ``"single"`` -- to select a single discrete data value on ``click``.
        * ``"multi"`` -- to select multiple discrete data value; the first value is selected
          on ``click`` and additional values toggled on shift- ``click``.
        * ``"interval"`` -- to select a continuous range of data values on ``drag``.
    bind : :class:`LegendBinding`
        When set, a selection is populated by interacting with the corresponding legend.
        Direct manipulation interaction is disabled by default;
        to re-enable it, set the selection's `on
        <https://vega.github.io/vega-lite/docs/selection.html#common-selection-properties>`__
        property.

        Legend bindings are restricted to selections that only specify a single field or
        encoding.
    clear : anyOf(:class:`Stream`, string, boolean)
        Clears the selection, emptying it of all values. Can be a
        `Event Stream <https://vega.github.io/vega/docs/event-streams/>`__ or ``false`` to
        disable.

        **Default value:** ``dblclick``.

        **See also:** `clear <https://vega.github.io/vega-lite/docs/clear.html>`__
        documentation.
    empty : enum('all', 'none')
        By default, ``all`` data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefUnitChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.

        **See also:** `encodings <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    fields : List(:class:`FieldName`)
        An array of field names whose values must match for a data tuple to
        fall within the selection.

        **See also:** `fields <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    init : List(:class:`SelectionInitMapping`)
        Initialize the selection with a mapping between `projected channels or field names
        <https://vega.github.io/vega-lite/docs/project.html>`__ and an initial
        value (or array of values).

        **See also:** `init <https://vega.github.io/vega-lite/docs/init.html>`__
        documentation.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        **See also:** `nearest <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation.
    on : anyOf(:class:`Stream`, string)
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.

        **See also:** `resolve
        <https://vega.github.io/vega-lite/docs/selection-resolve.html>`__ documentation.
    toggle : anyOf(string, boolean)
        Controls whether data values should be toggled or only ever inserted into
        multi selections. Can be ``true``, ``false`` (for insertion only), or a
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__.

        **Default value:** ``true``, which corresponds to ``event.shiftKey`` (i.e.,
        data values are toggled when a user interacts with the shift-key pressed).

        **See also:** `toggle <https://vega.github.io/vega-lite/docs/toggle.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/MultiSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, clear=Undefined, empty=Undefined,
                 encodings=Undefined, fields=Undefined, init=Undefined, nearest=Undefined, on=Undefined,
                 resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelection, self).__init__(type=type, bind=bind, clear=clear, empty=empty,
                                             encodings=encodings, fields=fields, init=init,
                                             nearest=nearest, on=on, resolve=resolve, toggle=toggle,
                                             **kwds)


class SelectionExtent(BinExtent):
    """SelectionExtent schema wrapper

    anyOf(Mapping(required=[selection]), Mapping(required=[selection]))
    """
    _schema = {'$ref': '#/definitions/SelectionExtent'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionExtent, self).__init__(*args, **kwds)


class SelectionInit(VegaLiteSchema):
    """SelectionInit schema wrapper

    anyOf(:class:`Value`, :class:`DateTime`)
    """
    _schema = {'$ref': '#/definitions/SelectionInit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionInit, self).__init__(*args, **kwds)


class DateTime(SelectionInit):
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
        Value representing the day of a week. This can be one of:
        (1) integer value -- ``1`` represents Monday;
        (2) case-insensitive day name (e.g., ``"Monday"`` );
        (3) case-insensitive, 3-character short day name (e.g., ``"Mon"`` ).

        **Warning:** A DateTime definition object with ``day`` ** should not be combined
        with ``year``, ``quarter``, ``month``, or ``date``.
    hours : float
        Integer value representing the hour of a day from 0-23.
    milliseconds : float
        Integer value representing the millisecond segment of time.
    minutes : float
        Integer value representing the minute segment of time from 0-59.
    month : anyOf(:class:`Month`, string)
        One of:
        (1) integer value representing the month from ``1`` - ``12``. ``1`` represents
        January;
        (2) case-insensitive month name (e.g., ``"January"`` );
        (3) case-insensitive, 3-character short month name (e.g., ``"Jan"`` ).
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


class SelectionInitInterval(VegaLiteSchema):
    """SelectionInitInterval schema wrapper

    anyOf(:class:`Vector2boolean`, :class:`Vector2number`, :class:`Vector2string`,
    :class:`Vector2DateTime`)
    """
    _schema = {'$ref': '#/definitions/SelectionInitInterval'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionInitInterval, self).__init__(*args, **kwds)


class SelectionInitIntervalMapping(VegaLiteSchema):
    """SelectionInitIntervalMapping schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/SelectionInitIntervalMapping'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionInitIntervalMapping, self).__init__(**kwds)


class SelectionInitMapping(VegaLiteSchema):
    """SelectionInitMapping schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/SelectionInitMapping'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionInitMapping, self).__init__(**kwds)


class SelectionOperand(VegaLiteSchema):
    """SelectionOperand schema wrapper

    anyOf(:class:`SelectionNot`, :class:`SelectionAnd`, :class:`SelectionOr`, string)
    """
    _schema = {'$ref': '#/definitions/SelectionOperand'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionOperand, self).__init__(*args, **kwds)


class SelectionAnd(SelectionOperand):
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


class SelectionNot(SelectionOperand):
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


class SelectionOr(SelectionOperand):
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


class SelectionPredicate(Predicate):
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


class SequenceGenerator(Generator):
    """SequenceGenerator schema wrapper

    Mapping(required=[sequence])

    Attributes
    ----------

    sequence : :class:`SequenceParams`
        Generate a sequence of numbers.
    name : string
        Provide a placeholder name and bind data at runtime.
    """
    _schema = {'$ref': '#/definitions/SequenceGenerator'}
    _rootschema = Root._schema

    def __init__(self, sequence=Undefined, name=Undefined, **kwds):
        super(SequenceGenerator, self).__init__(sequence=sequence, name=name, **kwds)


class SequenceParams(VegaLiteSchema):
    """SequenceParams schema wrapper

    Mapping(required=[start, stop])

    Attributes
    ----------

    start : float
        The starting value of the sequence (inclusive).
    stop : float
        The ending value of the sequence (exclusive).
    step : float
        The step value between sequence entries.

        **Default value:** ``1``
    as : :class:`FieldName`
        The name of the generated sequence field.

        **Default value:** ``"data"``
    """
    _schema = {'$ref': '#/definitions/SequenceParams'}
    _rootschema = Root._schema

    def __init__(self, start=Undefined, stop=Undefined, step=Undefined, **kwds):
        super(SequenceParams, self).__init__(start=start, stop=stop, step=step, **kwds)


class SequentialMultiHue(ColorScheme):
    """SequentialMultiHue schema wrapper

    enum('viridis', 'inferno', 'magma', 'plasma', 'bluegreen', 'bluegreen-3', 'bluegreen-4',
    'bluegreen-5', 'bluegreen-6', 'bluegreen-7', 'bluegreen-8', 'bluegreen-9', 'bluepurple',
    'bluepurple-3', 'bluepurple-4', 'bluepurple-5', 'bluepurple-6', 'bluepurple-7',
    'bluepurple-8', 'bluepurple-9', 'greenblue', 'greenblue-3', 'greenblue-4', 'greenblue-5',
    'greenblue-6', 'greenblue-7', 'greenblue-8', 'greenblue-9', 'orangered', 'orangered-3',
    'orangered-4', 'orangered-5', 'orangered-6', 'orangered-7', 'orangered-8', 'orangered-9',
    'purplebluegreen', 'purplebluegreen-3', 'purplebluegreen-4', 'purplebluegreen-5',
    'purplebluegreen-6', 'purplebluegreen-7', 'purplebluegreen-8', 'purplebluegreen-9',
    'purpleblue', 'purpleblue-3', 'purpleblue-4', 'purpleblue-5', 'purpleblue-6',
    'purpleblue-7', 'purpleblue-8', 'purpleblue-9', 'purplered', 'purplered-3', 'purplered-4',
    'purplered-5', 'purplered-6', 'purplered-7', 'purplered-8', 'purplered-9', 'redpurple',
    'redpurple-3', 'redpurple-4', 'redpurple-5', 'redpurple-6', 'redpurple-7', 'redpurple-8',
    'redpurple-9', 'yellowgreenblue', 'yellowgreenblue-3', 'yellowgreenblue-4',
    'yellowgreenblue-5', 'yellowgreenblue-6', 'yellowgreenblue-7', 'yellowgreenblue-8',
    'yellowgreenblue-9', 'yellowgreen', 'yellowgreen-3', 'yellowgreen-4', 'yellowgreen-5',
    'yellowgreen-6', 'yellowgreen-7', 'yellowgreen-8', 'yellowgreen-9', 'yelloworangebrown',
    'yelloworangebrown-3', 'yelloworangebrown-4', 'yelloworangebrown-5', 'yelloworangebrown-6',
    'yelloworangebrown-7', 'yelloworangebrown-8', 'yelloworangebrown-9', 'yelloworangered',
    'yelloworangered-3', 'yelloworangered-4', 'yelloworangered-5', 'yelloworangered-6',
    'yelloworangered-7', 'yelloworangered-8', 'yelloworangered-9')
    """
    _schema = {'$ref': '#/definitions/SequentialMultiHue'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SequentialMultiHue, self).__init__(*args)


class SequentialSingleHue(ColorScheme):
    """SequentialSingleHue schema wrapper

    enum('blues', 'greens', 'greys', 'purples', 'reds', 'oranges')
    """
    _schema = {'$ref': '#/definitions/SequentialSingleHue'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SequentialSingleHue, self).__init__(*args)


class ShapeFieldDefWithCondition(VegaLiteSchema):
    """ShapeFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`TypeForShape`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalStringValueDef`,
    List(:class:`ConditionalStringValueDef`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/ShapeFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(ShapeFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                         condition=condition, field=field,
                                                         legend=legend, scale=scale, sort=sort,
                                                         timeUnit=timeUnit, title=title, **kwds)


class ShapeValueDefWithCondition(VegaLiteSchema):
    """ShapeValueDefWithCondition schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDefTypeForShape`,
    :class:`ConditionalStringValueDef`, List(:class:`ConditionalStringValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ShapeValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ShapeValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class SignalRef(LayoutBounds, RangeScheme):
    """SignalRef schema wrapper

    Mapping(required=[signal])

    Attributes
    ----------

    signal : string

    """
    _schema = {'$ref': '#/definitions/SignalRef'}
    _rootschema = Root._schema

    def __init__(self, signal=Undefined, **kwds):
        super(SignalRef, self).__init__(signal=signal, **kwds)


class SingleDefUnitChannel(VegaLiteSchema):
    """SingleDefUnitChannel schema wrapper

    enum('x', 'y', 'x2', 'y2', 'longitude', 'latitude', 'longitude2', 'latitude2', 'color',
    'fill', 'stroke', 'opacity', 'fillOpacity', 'strokeOpacity', 'strokeWidth', 'size', 'shape',
    'key', 'text', 'href', 'url')
    """
    _schema = {'$ref': '#/definitions/SingleDefUnitChannel'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SingleDefUnitChannel, self).__init__(*args)


class SingleSelection(SelectionDef):
    """SingleSelection schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('single')
        Determines the default event processing and data query for the selection. Vega-Lite
        currently supports three selection types:


        * ``"single"`` -- to select a single discrete data value on ``click``.
        * ``"multi"`` -- to select multiple discrete data value; the first value is selected
          on ``click`` and additional values toggled on shift- ``click``.
        * ``"interval"`` -- to select a continuous range of data values on ``drag``.
    bind : anyOf(:class:`Binding`, Mapping(required=[]), :class:`LegendBinding`)
        When set, a selection is populated by input elements (also known as dynamic query
        widgets)
        or by interacting with the corresponding legend. Direct manipulation interaction is
        disabled by default;
        to re-enable it, set the selection's `on
        <https://vega.github.io/vega-lite/docs/selection.html#common-selection-properties>`__
        property.

        Legend bindings are restricted to selections that only specify a single field or
        encoding.

        Query widget binding takes the form of Vega's `input element binding definition
        <https://vega.github.io/vega/docs/signals/#bind>`__
        or can be a mapping between projected field/encodings and binding definitions.

        **See also:** `bind <https://vega.github.io/vega-lite/docs/bind.html>`__
        documentation.
    clear : anyOf(:class:`Stream`, string, boolean)
        Clears the selection, emptying it of all values. Can be a
        `Event Stream <https://vega.github.io/vega/docs/event-streams/>`__ or ``false`` to
        disable.

        **Default value:** ``dblclick``.

        **See also:** `clear <https://vega.github.io/vega-lite/docs/clear.html>`__
        documentation.
    empty : enum('all', 'none')
        By default, ``all`` data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefUnitChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.

        **See also:** `encodings <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    fields : List(:class:`FieldName`)
        An array of field names whose values must match for a data tuple to
        fall within the selection.

        **See also:** `fields <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    init : :class:`SelectionInitMapping`
        Initialize the selection with a mapping between `projected channels or field names
        <https://vega.github.io/vega-lite/docs/project.html>`__ and initial values.

        **See also:** `init <https://vega.github.io/vega-lite/docs/init.html>`__
        documentation.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        **See also:** `nearest <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation.
    on : anyOf(:class:`Stream`, string)
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.

        **See also:** `resolve
        <https://vega.github.io/vega-lite/docs/selection-resolve.html>`__ documentation.
    """
    _schema = {'$ref': '#/definitions/SingleSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, clear=Undefined, empty=Undefined,
                 encodings=Undefined, fields=Undefined, init=Undefined, nearest=Undefined, on=Undefined,
                 resolve=Undefined, **kwds):
        super(SingleSelection, self).__init__(type=type, bind=bind, clear=clear, empty=empty,
                                              encodings=encodings, fields=fields, init=init,
                                              nearest=nearest, on=on, resolve=resolve, **kwds)


class SingleSelectionConfig(VegaLiteSchema):
    """SingleSelectionConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bind : anyOf(:class:`Binding`, Mapping(required=[]), :class:`LegendBinding`)
        When set, a selection is populated by input elements (also known as dynamic query
        widgets)
        or by interacting with the corresponding legend. Direct manipulation interaction is
        disabled by default;
        to re-enable it, set the selection's `on
        <https://vega.github.io/vega-lite/docs/selection.html#common-selection-properties>`__
        property.

        Legend bindings are restricted to selections that only specify a single field or
        encoding.

        Query widget binding takes the form of Vega's `input element binding definition
        <https://vega.github.io/vega/docs/signals/#bind>`__
        or can be a mapping between projected field/encodings and binding definitions.

        **See also:** `bind <https://vega.github.io/vega-lite/docs/bind.html>`__
        documentation.
    clear : anyOf(:class:`Stream`, string, boolean)
        Clears the selection, emptying it of all values. Can be a
        `Event Stream <https://vega.github.io/vega/docs/event-streams/>`__ or ``false`` to
        disable.

        **Default value:** ``dblclick``.

        **See also:** `clear <https://vega.github.io/vega-lite/docs/clear.html>`__
        documentation.
    empty : enum('all', 'none')
        By default, ``all`` data values are considered to lie within an empty selection.
        When set to ``none``, empty selections contain no data values.
    encodings : List(:class:`SingleDefUnitChannel`)
        An array of encoding channels. The corresponding data field values
        must match for a data tuple to fall within the selection.

        **See also:** `encodings <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    fields : List(:class:`FieldName`)
        An array of field names whose values must match for a data tuple to
        fall within the selection.

        **See also:** `fields <https://vega.github.io/vega-lite/docs/project.html>`__
        documentation.
    init : :class:`SelectionInitMapping`
        Initialize the selection with a mapping between `projected channels or field names
        <https://vega.github.io/vega-lite/docs/project.html>`__ and initial values.

        **See also:** `init <https://vega.github.io/vega-lite/docs/init.html>`__
        documentation.
    nearest : boolean
        When true, an invisible voronoi diagram is computed to accelerate discrete
        selection. The data value *nearest* the mouse cursor is added to the selection.

        **See also:** `nearest <https://vega.github.io/vega-lite/docs/nearest.html>`__
        documentation.
    on : anyOf(:class:`Stream`, string)
        A `Vega event stream <https://vega.github.io/vega/docs/event-streams/>`__ (object or
        selector) that triggers the selection.
        For interval selections, the event stream must specify a `start and end
        <https://vega.github.io/vega/docs/event-streams/#between-filters>`__.
    resolve : :class:`SelectionResolution`
        With layered and multi-view displays, a strategy that determines how
        selections' data queries are resolved when applied in a filter transform,
        conditional encoding rule, or scale domain.

        **See also:** `resolve
        <https://vega.github.io/vega-lite/docs/selection-resolve.html>`__ documentation.
    """
    _schema = {'$ref': '#/definitions/SingleSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, clear=Undefined, empty=Undefined, encodings=Undefined,
                 fields=Undefined, init=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined,
                 **kwds):
        super(SingleSelectionConfig, self).__init__(bind=bind, clear=clear, empty=empty,
                                                    encodings=encodings, fields=fields, init=init,
                                                    nearest=nearest, on=on, resolve=resolve, **kwds)


class Sort(VegaLiteSchema):
    """Sort schema wrapper

    anyOf(:class:`SortArray`, :class:`AllSortString`, :class:`EncodingSortField`,
    :class:`SortByEncoding`, None)
    """
    _schema = {'$ref': '#/definitions/Sort'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Sort, self).__init__(*args, **kwds)


class AllSortString(Sort):
    """AllSortString schema wrapper

    anyOf(:class:`SortOrder`, :class:`SortByChannel`, :class:`SortByChannelDesc`)
    """
    _schema = {'$ref': '#/definitions/AllSortString'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(AllSortString, self).__init__(*args, **kwds)


class EncodingSortField(Sort):
    """EncodingSortField schema wrapper

    Mapping(required=[])
    A sort definition for sorting a discrete scale in an encoding field definition.

    Attributes
    ----------

    field : :class:`Field`
        The data `field <https://vega.github.io/vega-lite/docs/field.html>`__ to sort by.

        **Default value:** If unspecified, defaults to the field specified in the outer data
        reference.
    op : :class:`NonArgAggregateOp`
        An `aggregate operation
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__ to perform on the
        field prior to sorting (e.g., ``"count"``, ``"mean"`` and ``"median"`` ).
        An aggregation is required when there are multiple values of the sort field for each
        encoded data field.
        The input data objects will be aggregated, grouped by the encoded data field.

        For a full list of operations, please see the documentation for `aggregate
        <https://vega.github.io/vega-lite/docs/aggregate.html#ops>`__.

        **Default value:** ``"sum"`` for stacked plots. Otherwise, ``"mean"``.
    order : anyOf(:class:`SortOrder`, None)
        The sort order. One of ``"ascending"`` (default), ``"descending"``, or ``null`` (no
        not sort).
    """
    _schema = {'$ref': '#/definitions/EncodingSortField'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, op=Undefined, order=Undefined, **kwds):
        super(EncodingSortField, self).__init__(field=field, op=op, order=order, **kwds)


class SortArray(Sort):
    """SortArray schema wrapper

    anyOf(List(float), List(string), List(boolean), List(:class:`DateTime`))
    """
    _schema = {'$ref': '#/definitions/SortArray'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SortArray, self).__init__(*args, **kwds)


class SortByChannel(AllSortString):
    """SortByChannel schema wrapper

    enum('x', 'y', 'color', 'fill', 'stroke', 'strokeWidth', 'size', 'shape', 'fillOpacity',
    'strokeOpacity', 'opacity', 'text')
    """
    _schema = {'$ref': '#/definitions/SortByChannel'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SortByChannel, self).__init__(*args)


class SortByChannelDesc(AllSortString):
    """SortByChannelDesc schema wrapper

    enum('-x', '-y', '-color', '-fill', '-stroke', '-strokeWidth', '-size', '-shape',
    '-fillOpacity', '-strokeOpacity', '-opacity', '-text')
    """
    _schema = {'$ref': '#/definitions/SortByChannelDesc'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SortByChannelDesc, self).__init__(*args)


class SortByEncoding(Sort):
    """SortByEncoding schema wrapper

    Mapping(required=[encoding])

    Attributes
    ----------

    encoding : :class:`SortByChannel`
        The `encoding channel
        <https://vega.github.io/vega-lite/docs/encoding.html#channels>`__ to sort by (e.g.,
        ``"x"``, ``"y"`` )
    order : anyOf(:class:`SortOrder`, None)
        The sort order. One of ``"ascending"`` (default), ``"descending"``, or ``null`` (no
        not sort).
    """
    _schema = {'$ref': '#/definitions/SortByEncoding'}
    _rootschema = Root._schema

    def __init__(self, encoding=Undefined, order=Undefined, **kwds):
        super(SortByEncoding, self).__init__(encoding=encoding, order=order, **kwds)


class SortField(VegaLiteSchema):
    """SortField schema wrapper

    Mapping(required=[field])
    A sort definition for transform

    Attributes
    ----------

    field : :class:`FieldName`
        The name of the field to sort.
    order : anyOf(:class:`SortOrder`, None)
        Whether to sort the field in ascending or descending order. One of ``"ascending"``
        (default), ``"descending"``, or ``null`` (no not sort).
    """
    _schema = {'$ref': '#/definitions/SortField'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, order=Undefined, **kwds):
        super(SortField, self).__init__(field=field, order=order, **kwds)


class SortOrder(AllSortString):
    """SortOrder schema wrapper

    enum('ascending', 'descending')
    """
    _schema = {'$ref': '#/definitions/SortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SortOrder, self).__init__(*args)


class Spec(VegaLiteSchema):
    """Spec schema wrapper

    anyOf(:class:`FacetedUnitSpec`, :class:`LayerSpec`, :class:`FacetSpec`, :class:`RepeatSpec`,
    :class:`ConcatSpec`, :class:`VConcatSpec`, :class:`HConcatSpec`)
    Any specification in Vega-Lite.
    """
    _schema = {'$ref': '#/definitions/Spec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Spec, self).__init__(*args, **kwds)


class ConcatSpec(Spec):
    """ConcatSpec schema wrapper

    Mapping(required=[concat])
    Base interface for a generalized concatenation specification.

    Attributes
    ----------

    concat : List(:class:`Spec`)
        A list of views to be concatenated.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/ConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, concat=Undefined, align=Undefined, bounds=Undefined, center=Undefined,
                 columns=Undefined, data=Undefined, description=Undefined, name=Undefined,
                 resolve=Undefined, spacing=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(ConcatSpec, self).__init__(concat=concat, align=align, bounds=bounds, center=center,
                                         columns=columns, data=data, description=description, name=name,
                                         resolve=resolve, spacing=spacing, title=title,
                                         transform=transform, **kwds)


class FacetSpec(Spec):
    """FacetSpec schema wrapper

    Mapping(required=[facet, spec])
    Base interface for a facet specification.

    Attributes
    ----------

    facet : anyOf(:class:`FacetFieldDef`, :class:`FacetMapping`)
        Definition for how to facet the data. One of:
        1) `a field definition for faceting the plot by one field
        <https://vega.github.io/vega-lite/docs/facet.html#field-def>`__
        2) `An object that maps row and column channels to their field definitions
        <https://vega.github.io/vega-lite/docs/facet.html#mapping>`__
    spec : anyOf(:class:`LayerSpec`, :class:`FacetedUnitSpec`)
        A specification of the view that gets faceted.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/FacetSpec'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, spec=Undefined, align=Undefined, bounds=Undefined,
                 center=Undefined, columns=Undefined, data=Undefined, description=Undefined,
                 name=Undefined, resolve=Undefined, spacing=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, align=align, bounds=bounds,
                                        center=center, columns=columns, data=data,
                                        description=description, name=name, resolve=resolve,
                                        spacing=spacing, title=title, transform=transform, **kwds)


class FacetedUnitSpec(Spec):
    """FacetedUnitSpec schema wrapper

    Mapping(required=[mark])
    Unit spec that can have a composite mark and row or column channels (shorthand for a facet
    spec).

    Attributes
    ----------

    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`FacetedEncoding`
        A key-value mapping between encoding channels and definition of fields.
    height : anyOf(float, enum('container'), :class:`Step`)
        The height of a visualization.


        * For a plot with a continuous y-field, height should be a number.
        * For a plot with either a discrete y-field or no y-field, height can be either a
          number indicating a fixed height or an object in the form of ``{step: number}``
          defining the height per discrete step. (No y-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on height, it should be set to ``"container"``.

        **Default value:** Based on ``config.view.continuousHeight`` for a plot with a
        continuous y-field and ``config.view.discreteHeight`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view and the ``"container"`` option cannot be used.

        **See also:** `height <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    view : :class:`ViewBackground`
        An object defining the view background's fill and stroke.

        **Default value:** none (transparent)
    width : anyOf(float, enum('container'), :class:`Step`)
        The width of a visualization.


        * For a plot with a continuous x-field, width should be a number.
        * For a plot with either a discrete x-field or no x-field, width can be either a
          number indicating a fixed width or an object in the form of ``{step: number}``
          defining the width per discrete step. (No x-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on width, it should be set to ``"container"``.

        **Default value:**
        Based on ``config.view.continuousWidth`` for a plot with a continuous x-field and
        ``config.view.discreteWidth`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view and the ``"container"`` option cannot be used.

        **See also:** `width <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/FacetedUnitSpec'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, bounds=Undefined, data=Undefined, description=Undefined,
                 encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined,
                 resolve=Undefined, selection=Undefined, title=Undefined, transform=Undefined,
                 view=Undefined, width=Undefined, **kwds):
        super(FacetedUnitSpec, self).__init__(mark=mark, bounds=bounds, data=data,
                                              description=description, encoding=encoding, height=height,
                                              name=name, projection=projection, resolve=resolve,
                                              selection=selection, title=title, transform=transform,
                                              view=view, width=width, **kwds)


class HConcatSpec(Spec):
    """HConcatSpec schema wrapper

    Mapping(required=[hconcat])
    Base interface for a horizontal concatenation specification.

    Attributes
    ----------

    hconcat : List(:class:`Spec`)
        A list of views to be concatenated and put into a row.
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
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(:class:`Text`, :class:`TitleParams`)
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


class LayerSpec(Spec):
    """LayerSpec schema wrapper

    Mapping(required=[layer])
    A full layered plot specification, which may contains ``encoding`` and ``projection``
    properties that will be applied to underlying unit (single-view) specifications.

    Attributes
    ----------

    layer : List(anyOf(:class:`LayerSpec`, :class:`UnitSpec`))
        Layer or single view specifications to be layered.

        **Note** : Specifications inside ``layer`` cannot use ``row`` and ``column``
        channels as layering facet specifications is not allowed. Instead, use the `facet
        operator <https://vega.github.io/vega-lite/docs/facet.html>`__ and place a layer
        inside a facet.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A shared key-value mapping between encoding channels and definition of fields in the
        underlying layers.
    height : anyOf(float, enum('container'), :class:`Step`)
        The height of a visualization.


        * For a plot with a continuous y-field, height should be a number.
        * For a plot with either a discrete y-field or no y-field, height can be either a
          number indicating a fixed height or an object in the form of ``{step: number}``
          defining the height per discrete step. (No y-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on height, it should be set to ``"container"``.

        **Default value:** Based on ``config.view.continuousHeight`` for a plot with a
        continuous y-field and ``config.view.discreteHeight`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view and the ``"container"`` option cannot be used.

        **See also:** `height <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of the geographic projection shared by underlying
        layers.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    view : :class:`ViewBackground`
        An object defining the view background's fill and stroke.

        **Default value:** none (transparent)
    width : anyOf(float, enum('container'), :class:`Step`)
        The width of a visualization.


        * For a plot with a continuous x-field, width should be a number.
        * For a plot with either a discrete x-field or no x-field, width can be either a
          number indicating a fixed width or an object in the form of ``{step: number}``
          defining the width per discrete step. (No x-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on width, it should be set to ``"container"``.

        **Default value:**
        Based on ``config.view.continuousWidth`` for a plot with a continuous x-field and
        ``config.view.discreteWidth`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view and the ``"container"`` option cannot be used.

        **See also:** `width <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/LayerSpec'}
    _rootschema = Root._schema

    def __init__(self, layer=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, resolve=Undefined,
                 title=Undefined, transform=Undefined, view=Undefined, width=Undefined, **kwds):
        super(LayerSpec, self).__init__(layer=layer, data=data, description=description,
                                        encoding=encoding, height=height, name=name,
                                        projection=projection, resolve=resolve, title=title,
                                        transform=transform, view=view, width=width, **kwds)


class RepeatSpec(Spec):
    """RepeatSpec schema wrapper

    Mapping(required=[repeat, spec])
    Base interface for a repeat specification.

    Attributes
    ----------

    repeat : anyOf(List(string), :class:`RepeatMapping`)
        Definition for fields to be repeated. One of:
        1) An array of fields to be repeated. If ``"repeat"`` is an array, the field can be
        referred using ``{"repeat": "repeat"}``
        2) An object that mapped ``"row"`` and/or ``"column"`` to the listed of fields to be
        repeated along the particular orientations. The objects ``{"repeat": "row"}`` and
        ``{"repeat": "column"}`` can be used to refer to the repeated field respectively.
    spec : :class:`Spec`
        A specification of the view that gets repeated.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/RepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, align=Undefined, bounds=Undefined,
                 center=Undefined, columns=Undefined, data=Undefined, description=Undefined,
                 name=Undefined, resolve=Undefined, spacing=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(RepeatSpec, self).__init__(repeat=repeat, spec=spec, align=align, bounds=bounds,
                                         center=center, columns=columns, data=data,
                                         description=description, name=name, resolve=resolve,
                                         spacing=spacing, title=title, transform=transform, **kwds)


class SphereGenerator(Generator):
    """SphereGenerator schema wrapper

    Mapping(required=[sphere])

    Attributes
    ----------

    sphere : anyOf(enum(True), Mapping(required=[]))
        Generate sphere GeoJSON data for the full globe.
    name : string
        Provide a placeholder name and bind data at runtime.
    """
    _schema = {'$ref': '#/definitions/SphereGenerator'}
    _rootschema = Root._schema

    def __init__(self, sphere=Undefined, name=Undefined, **kwds):
        super(SphereGenerator, self).__init__(sphere=sphere, name=name, **kwds)


class StackOffset(VegaLiteSchema):
    """StackOffset schema wrapper

    enum('zero', 'center', 'normalize')
    """
    _schema = {'$ref': '#/definitions/StackOffset'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)


class StandardType(VegaLiteSchema):
    """StandardType schema wrapper

    enum('quantitative', 'ordinal', 'temporal', 'nominal')
    """
    _schema = {'$ref': '#/definitions/StandardType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StandardType, self).__init__(*args)


class Step(VegaLiteSchema):
    """Step schema wrapper

    Mapping(required=[step])

    Attributes
    ----------

    step : float
        The size (width/height) per discrete step.
    """
    _schema = {'$ref': '#/definitions/Step'}
    _rootschema = Root._schema

    def __init__(self, step=Undefined, **kwds):
        super(Step, self).__init__(step=step, **kwds)


class Stream(VegaLiteSchema):
    """Stream schema wrapper

    anyOf(:class:`EventStream`, :class:`DerivedStream`, :class:`MergedStream`)
    """
    _schema = {'$ref': '#/definitions/Stream'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Stream, self).__init__(*args, **kwds)


class DerivedStream(Stream):
    """DerivedStream schema wrapper

    Mapping(required=[stream])

    Attributes
    ----------

    stream : :class:`Stream`

    between : List(:class:`Stream`)

    consume : boolean

    debounce : float

    filter : anyOf(:class:`Expr`, List(:class:`Expr`))

    markname : string

    marktype : :class:`MarkType`

    throttle : float

    """
    _schema = {'$ref': '#/definitions/DerivedStream'}
    _rootschema = Root._schema

    def __init__(self, stream=Undefined, between=Undefined, consume=Undefined, debounce=Undefined,
                 filter=Undefined, markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(DerivedStream, self).__init__(stream=stream, between=between, consume=consume,
                                            debounce=debounce, filter=filter, markname=markname,
                                            marktype=marktype, throttle=throttle, **kwds)


class EventStream(Stream):
    """EventStream schema wrapper

    anyOf(Mapping(required=[type]), Mapping(required=[source, type]))
    """
    _schema = {'$ref': '#/definitions/EventStream'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(EventStream, self).__init__(*args, **kwds)


class MergedStream(Stream):
    """MergedStream schema wrapper

    Mapping(required=[merge])

    Attributes
    ----------

    merge : List(:class:`Stream`)

    between : List(:class:`Stream`)

    consume : boolean

    debounce : float

    filter : anyOf(:class:`Expr`, List(:class:`Expr`))

    markname : string

    marktype : :class:`MarkType`

    throttle : float

    """
    _schema = {'$ref': '#/definitions/MergedStream'}
    _rootschema = Root._schema

    def __init__(self, merge=Undefined, between=Undefined, consume=Undefined, debounce=Undefined,
                 filter=Undefined, markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(MergedStream, self).__init__(merge=merge, between=between, consume=consume,
                                           debounce=debounce, filter=filter, markname=markname,
                                           marktype=marktype, throttle=throttle, **kwds)


class StringFieldDef(VegaLiteSchema):
    """StringFieldDef schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/StringFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 format=Undefined, formatType=Undefined, labelExpr=Undefined, timeUnit=Undefined,
                 title=Undefined, **kwds):
        super(StringFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                             format=format, formatType=formatType, labelExpr=labelExpr,
                                             timeUnit=timeUnit, title=title, **kwds)


class StringFieldDefWithCondition(VegaLiteSchema):
    """StringFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstring`,
    List(:class:`ConditionalValueDefstring`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/StringFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, formatType=Undefined, labelExpr=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(StringFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                          condition=condition, field=field,
                                                          format=format, formatType=formatType,
                                                          labelExpr=labelExpr, timeUnit=timeUnit,
                                                          title=title, **kwds)


class StringValueDefWithCondition(VegaLiteSchema):
    """StringValueDefWithCondition schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalStringValueDef`,
    List(:class:`ConditionalStringValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/StringValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(StringValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class StringValueDefWithConditionTypeForShape(VegaLiteSchema):
    """StringValueDefWithConditionTypeForShape schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDefTypeForShape`,
    :class:`ConditionalStringValueDef`, List(:class:`ConditionalStringValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/StringValueDefWithCondition<TypeForShape>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(StringValueDefWithConditionTypeForShape, self).__init__(condition=condition, value=value,
                                                                      **kwds)


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


class SymbolShape(VegaLiteSchema):
    """SymbolShape schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/SymbolShape'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SymbolShape, self).__init__(*args)


class Text(VegaLiteSchema):
    """Text schema wrapper

    anyOf(string, List(string))
    """
    _schema = {'$ref': '#/definitions/Text'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Text, self).__init__(*args, **kwds)


class TextBaseline(VegaLiteSchema):
    """TextBaseline schema wrapper

    anyOf(enum('alphabetic'), :class:`Baseline`)
    """
    _schema = {'$ref': '#/definitions/TextBaseline'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TextBaseline, self).__init__(*args, **kwds)


class Baseline(TextBaseline):
    """Baseline schema wrapper

    enum('top', 'middle', 'bottom')
    """
    _schema = {'$ref': '#/definitions/Baseline'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Baseline, self).__init__(*args)


class TextFieldDefWithCondition(VegaLiteSchema):
    """TextFieldDefWithCondition schema wrapper

    Mapping(required=[type])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefText`, List(:class:`ConditionalValueDefText`))
        One or more value definition(s) with `a selection or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The text formatting pattern for labels of guides (axes, legends, headers) and text
        marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : enum('number', 'time')
        The format type for labels ( ``"number"`` or ``"time"`` ).

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nomimal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nomimal fields without
          ``timeUnit``.
    labelExpr : string
        `Vega expression <https://vega.github.io/vega/docs/expressions/>`__ for customizing
        labels text.

        **Note:** The label text and value can be assessed via the ``label`` and ``value``
        properties of the axis's backing ``datum`` object.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/TextFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, formatType=Undefined, labelExpr=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(TextFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin,
                                                        condition=condition, field=field, format=format,
                                                        formatType=formatType, labelExpr=labelExpr,
                                                        timeUnit=timeUnit, title=title, **kwds)


class TextValueDefWithCondition(VegaLiteSchema):
    """TextValueDefWithCondition schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalStringFieldDef`, :class:`ConditionalValueDefText`,
    List(:class:`ConditionalValueDefText`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : :class:`Text`
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/TextValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(TextValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)


class TickConfig(VegaLiteSchema):
    """TickConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        The horizontal alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"left"``, ``"right"``, ``"center"``.
    angle : float
        The rotation angle of the text, in degrees.
    aspect : boolean
        Whether to keep aspect ratio of image marks.
    bandSize : float
        The width of the ticks.

        **Default value:**  3/4 of step (width step for horizontal ticks and height step for
        vertical ticks).
    baseline : :class:`TextBaseline`
        The vertical alignment of the text or ranged marks (area, bar, image, rect, rule).
        One of ``"top"``, ``"middle"``, ``"bottom"``.

        **Default value:** ``"middle"``
    color : anyOf(:class:`Color`, :class:`Gradient`)
        Default color.

        **Default value:** :raw-html:`<span style="color: #4682b4;">&#9632;</span>`
        ``"#4682b4"``

        **Note:**


        * This property cannot be used in a `style config
          <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__.
        * The ``fill`` and ``stroke`` properties have higher precedence than ``color`` and
          will override ``color``.
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    cornerRadiusBottomLeft : float
        The radius in pixels of rounded rectangle bottom left corner.

        **Default value:** ``0``
    cornerRadiusBottomRight : float
        The radius in pixels of rounded rectangle bottom right corner.

        **Default value:** ``0``
    cornerRadiusTopLeft : float
        The radius in pixels of rounded rectangle top right corner.

        **Default value:** ``0``
    cornerRadiusTopRight : float
        The radius in pixels of rounded rectangle top left corner.

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
    fill : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Fill Color. This has higher precedence than ``config.color``.

        **Default value:** (None)
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    filled : boolean
        Whether the mark's color should be used as fill color instead of stroke color.

        **Default value:** ``false`` for all ``point``, ``line``, and ``rule`` marks as well
        as ``geoshape`` marks for `graticule
        <https://vega.github.io/vega-lite/docs/data.html#graticule>`__ data sources;
        otherwise, ``true``.

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
    height : float
        Height of the marks.
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
    invalid : enum('filter', None)
        Defines how Vega-Lite should handle marks for invalid values ( ``null`` and ``NaN``
        ).


        * If set to ``"filter"`` (default), all data items with null values will be skipped
          (for line, trail, and area marks) or filtered (for other marks).
        * If ``null``, all data items are included. In this case, invalid values will be
          interpreted as zeroes.
    limit : float
        The maximum length of the text mark in pixels. The text value will be automatically
        truncated if the rendered size exceeds the limit.

        **Default value:** ``0``, indicating no limit
    lineBreak : string
        A delimiter, such as a newline character, upon which to break text strings into
        multiple lines. This property will be ignored if the text property is array-valued.
    lineHeight : float
        The height, in pixels, of each line of text in a multi-line text mark.
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    order : anyOf(None, boolean)
        For line and trail marks, this ``order`` property can be set to ``null`` or
        ``false`` to make the lines use the original order in the data sources.
    orient : :class:`Orientation`
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
        Shape of the point marks. Supported values include:


        * plotting shapes: ``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``,
          ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, or
          ``"triangle-left"``.
        * the line symbol ``"stroke"``
        * centered directional shapes ``"arrow"``, ``"wedge"``, or ``"triangle"``
        * a custom `SVG path string
          <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>`__ (For correct
          sizing, custom shape paths should be defined within a square bounding box with
          coordinates ranging from -1 to 1 along both the x and y dimensions.)

        **Default value:** ``"circle"``
    size : float
        Default size for marks.


        * For ``point`` / ``circle`` / ``square``, this represents the pixel area of the
          marks. For example: in the case of circles, the radius is determined in part by
          the square root of the size value.
        * For ``bar``, this represents the band size of the bar, in pixels.
        * For ``text``, this represents the font size, in pixels.

        **Default value:**


        * ``30`` for point, circle, square marks; width/height's ``step``
        * ``2`` for bar marks with discrete dimensions;
        * ``5`` for bar marks with continuous dimensions;
        * ``11`` for text marks.
    stroke : anyOf(:class:`Color`, :class:`Gradient`, None)
        Default Stroke Color. This has higher precedence than ``config.color``.

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
    text : :class:`Text`
        Placeholder text if the ``text`` channel is not specified
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the ``x`` and ``y`` properties. Values for ``theta`` follow the same convention of
        ``arc`` mark ``startAngle`` and ``endAngle`` properties: angles are measured in
        radians, with ``0`` indicating "north".
    thickness : float
        Thickness of the tick mark.

        **Default value:**  ``1``
    timeUnitBand : float
        Default relative band size for a time unit. If set to ``1``, the bandwidth of the
        marks will be equal to the time unit band step.
        If set to ``0.5``, bandwidth of the marks will be half of the time unit band step.
    timeUnitBandPosition : float
        Default relative band position for a time unit. If set to ``0``, the marks will be
        positioned at the beginning of the time unit band step.
        If set to ``0.5``, the marks will be positioned in the middle of the time unit band
        step.
    tooltip : anyOf(:class:`Value`, :class:`TooltipContent`, None)
        The tooltip text string to show upon mouse hover or an object defining which fields
        should the tooltip be derived from.


        * If ``tooltip`` is ``true`` or ``{"content": "encoding"}``, then all fields from
          ``encoding`` will be used.
        * If ``tooltip`` is ``{"content": "data"}``, then all fields that appear in the
          highlighted data point will be used.
        * If set to ``null`` or ``false``, then no tooltip will be used.

        See the `tooltip <https://vega.github.io/vega-lite/docs/tooltip.html>`__
        documentation for a detailed discussion about tooltip  in Vega-Lite.

        **Default value:** ``null``
    width : float
        Width of the marks.
    x : anyOf(float, enum('width'))
        X coordinates of the marks, or width of horizontal ``"bar"`` and ``"area"`` without
        specified ``x2`` or ``width``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    x2 : anyOf(float, enum('width'))
        X2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"width"`` for the width
        of the plot.
    y : anyOf(float, enum('height'))
        Y coordinates of the marks, or height of vertical ``"bar"`` and ``"area"`` without
        specified ``y2`` or ``height``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    y2 : anyOf(float, enum('height'))
        Y2 coordinates for ranged ``"area"``, ``"bar"``, ``"rect"``, and  ``"rule"``.

        The ``value`` of this channel can be a number or a string ``"height"`` for the
        height of the plot.
    """
    _schema = {'$ref': '#/definitions/TickConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, aspect=Undefined, bandSize=Undefined,
                 baseline=Undefined, color=Undefined, cornerRadius=Undefined,
                 cornerRadiusBottomLeft=Undefined, cornerRadiusBottomRight=Undefined,
                 cornerRadiusTopLeft=Undefined, cornerRadiusTopRight=Undefined, cursor=Undefined,
                 dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, fill=Undefined,
                 fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, height=Undefined, href=Undefined,
                 interpolate=Undefined, invalid=Undefined, limit=Undefined, lineBreak=Undefined,
                 lineHeight=Undefined, opacity=Undefined, order=Undefined, orient=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined,
                 strokeCap=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeJoin=Undefined, strokeMiterLimit=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 thickness=Undefined, timeUnitBand=Undefined, timeUnitBandPosition=Undefined,
                 tooltip=Undefined, width=Undefined, x=Undefined, x2=Undefined, y=Undefined,
                 y2=Undefined, **kwds):
        super(TickConfig, self).__init__(align=align, angle=angle, aspect=aspect, bandSize=bandSize,
                                         baseline=baseline, color=color, cornerRadius=cornerRadius,
                                         cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                         cornerRadiusBottomRight=cornerRadiusBottomRight,
                                         cornerRadiusTopLeft=cornerRadiusTopLeft,
                                         cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                         dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, fill=fill,
                                         fillOpacity=fillOpacity, filled=filled, font=font,
                                         fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                         height=height, href=href, interpolate=interpolate,
                                         invalid=invalid, limit=limit, lineBreak=lineBreak,
                                         lineHeight=lineHeight, opacity=opacity, order=order,
                                         orient=orient, radius=radius, shape=shape, size=size,
                                         stroke=stroke, strokeCap=strokeCap, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                         strokeMiterLimit=strokeMiterLimit, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, thickness=thickness, timeUnitBand=timeUnitBand,
                                         timeUnitBandPosition=timeUnitBandPosition, tooltip=tooltip,
                                         width=width, x=x, x2=x2, y=y, y2=y2, **kwds)


class TimeInterval(VegaLiteSchema):
    """TimeInterval schema wrapper

    enum('millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'year')
    """
    _schema = {'$ref': '#/definitions/TimeInterval'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TimeInterval, self).__init__(*args)


class TimeUnit(VegaLiteSchema):
    """TimeUnit schema wrapper

    anyOf(:class:`SingleTimeUnit`, :class:`MultiTimeUnit`)
    """
    _schema = {'$ref': '#/definitions/TimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TimeUnit, self).__init__(*args, **kwds)


class MultiTimeUnit(TimeUnit):
    """MultiTimeUnit schema wrapper

    anyOf(:class:`LocalMultiTimeUnit`, :class:`UtcMultiTimeUnit`)
    """
    _schema = {'$ref': '#/definitions/MultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(MultiTimeUnit, self).__init__(*args, **kwds)


class LocalMultiTimeUnit(MultiTimeUnit):
    """LocalMultiTimeUnit schema wrapper

    enum('yearquarter', 'yearquartermonth', 'yearmonth', 'yearmonthdate', 'yearmonthdatehours',
    'yearmonthdatehoursminutes', 'yearmonthdatehoursminutesseconds', 'quartermonth',
    'monthdate', 'monthdatehours', 'hoursminutes', 'hoursminutesseconds', 'minutesseconds',
    'secondsmilliseconds')
    """
    _schema = {'$ref': '#/definitions/LocalMultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LocalMultiTimeUnit, self).__init__(*args)


class SingleTimeUnit(TimeUnit):
    """SingleTimeUnit schema wrapper

    anyOf(:class:`LocalSingleTimeUnit`, :class:`UtcSingleTimeUnit`)
    """
    _schema = {'$ref': '#/definitions/SingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SingleTimeUnit, self).__init__(*args, **kwds)


class LocalSingleTimeUnit(SingleTimeUnit):
    """LocalSingleTimeUnit schema wrapper

    enum('year', 'quarter', 'month', 'day', 'date', 'hours', 'minutes', 'seconds',
    'milliseconds')
    """
    _schema = {'$ref': '#/definitions/LocalSingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LocalSingleTimeUnit, self).__init__(*args)


class TitleAnchor(VegaLiteSchema):
    """TitleAnchor schema wrapper

    enum(None, 'start', 'middle', 'end')
    """
    _schema = {'$ref': '#/definitions/TitleAnchor'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TitleAnchor, self).__init__(*args)


class TitleConfig(VegaLiteSchema):
    """TitleConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`Align`
        Horizontal text alignment for title text. One of ``"left"``, ``"center"``, or
        ``"right"``.
    anchor : :class:`TitleAnchor`
        The anchor position for placing the title and subtitle text. One of ``"start"``,
        ``"middle"``, or ``"end"``. For example, with an orientation of top these anchor
        positions map to a left-, center-, or right-aligned title.
    angle : float
        Angle in degrees of title and subtitle text.
    baseline : :class:`TextBaseline`
        Vertical text baseline for title and subtitle text. One of ``"top"``, ``"middle"``,
        ``"bottom"``, or ``"alphabetic"``.
    color : anyOf(None, :class:`Color`)
        Text color for title text.
    dx : float
        Delta offset for title and subtitle text x-coordinate.
    dy : float
        Delta offset for title and subtitle text y-coordinate.
    font : string
        Font name for title text.
    fontSize : float
        Font size in pixels for title text.
    fontStyle : :class:`FontStyle`
        Font style for title text.
    fontWeight : :class:`FontWeight`
        Font weight for title text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    frame : anyOf(:class:`TitleFrame`, string)
        The reference frame for the anchor position, one of ``"bounds"`` (to anchor relative
        to the full bounding box) or ``"group"`` (to anchor relative to the group width or
        height).
    limit : float
        The maximum allowed length in pixels of title and subtitle text.
    lineHeight : float
        Line height in pixels for multi-line title text.
    offset : float
        The orthogonal offset in pixels by which to displace the title group from its
        position along the edge of the chart.
    orient : :class:`TitleOrient`
        Default title orientation ( ``"top"``, ``"bottom"``, ``"left"``, or ``"right"`` )
    subtitleColor : anyOf(None, :class:`Color`)
        Text color for subtitle text.
    subtitleFont : string
        Font name for subtitle text.
    subtitleFontSize : float
        Font size in pixels for subtitle text.
    subtitleFontStyle : :class:`FontStyle`
        Font style for subtitle text.
    subtitleFontWeight : :class:`FontWeight`
        Font weight for subtitle text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    subtitleLineHeight : float
        Line height in pixels for multi-line subtitle text.
    subtitlePadding : float
        The padding in pixels between title and subtitle text.
    """
    _schema = {'$ref': '#/definitions/TitleConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, anchor=Undefined, angle=Undefined, baseline=Undefined,
                 color=Undefined, dx=Undefined, dy=Undefined, font=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, frame=Undefined, limit=Undefined,
                 lineHeight=Undefined, offset=Undefined, orient=Undefined, subtitleColor=Undefined,
                 subtitleFont=Undefined, subtitleFontSize=Undefined, subtitleFontStyle=Undefined,
                 subtitleFontWeight=Undefined, subtitleLineHeight=Undefined, subtitlePadding=Undefined,
                 **kwds):
        super(TitleConfig, self).__init__(align=align, anchor=anchor, angle=angle, baseline=baseline,
                                          color=color, dx=dx, dy=dy, font=font, fontSize=fontSize,
                                          fontStyle=fontStyle, fontWeight=fontWeight, frame=frame,
                                          limit=limit, lineHeight=lineHeight, offset=offset,
                                          orient=orient, subtitleColor=subtitleColor,
                                          subtitleFont=subtitleFont, subtitleFontSize=subtitleFontSize,
                                          subtitleFontStyle=subtitleFontStyle,
                                          subtitleFontWeight=subtitleFontWeight,
                                          subtitleLineHeight=subtitleLineHeight,
                                          subtitlePadding=subtitlePadding, **kwds)


class TitleFrame(VegaLiteSchema):
    """TitleFrame schema wrapper

    enum('bounds', 'group')
    """
    _schema = {'$ref': '#/definitions/TitleFrame'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TitleFrame, self).__init__(*args)


class TitleOrient(VegaLiteSchema):
    """TitleOrient schema wrapper

    enum('none', 'left', 'right', 'top', 'bottom')
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

    text : :class:`Text`
        The title text.
    align : :class:`Align`
        Horizontal text alignment for title text. One of ``"left"``, ``"center"``, or
        ``"right"``.
    anchor : :class:`TitleAnchor`
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
        <https://vega.github.io/vega-lite/docs/layer.html>`__ views. For other composite
        views, ``anchor`` is always ``"start"``.
    angle : float
        Angle in degrees of title and subtitle text.
    baseline : :class:`TextBaseline`
        Vertical text baseline for title and subtitle text. One of ``"top"``, ``"middle"``,
        ``"bottom"``, or ``"alphabetic"``.
    color : anyOf(None, :class:`Color`)
        Text color for title text.
    dx : float
        Delta offset for title and subtitle text x-coordinate.
    dy : float
        Delta offset for title and subtitle text y-coordinate.
    font : string
        Font name for title text.
    fontSize : float
        Font size in pixels for title text.
    fontStyle : :class:`FontStyle`
        Font style for title text.
    fontWeight : :class:`FontWeight`
        Font weight for title text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    frame : anyOf(:class:`TitleFrame`, string)
        The reference frame for the anchor position, one of ``"bounds"`` (to anchor relative
        to the full bounding box) or ``"group"`` (to anchor relative to the group width or
        height).
    limit : float
        The maximum allowed length in pixels of title and subtitle text.
    lineHeight : float
        Line height in pixels for multi-line title text.
    offset : float
        The orthogonal offset in pixels by which to displace the title group from its
        position along the edge of the chart.
    orient : :class:`TitleOrient`
        Default title orientation ( ``"top"``, ``"bottom"``, ``"left"``, or ``"right"`` )
    style : anyOf(string, List(string))
        A `mark style property <https://vega.github.io/vega-lite/docs/config.html#style>`__
        to apply to the title text mark.

        **Default value:** ``"group-title"``.
    subtitle : :class:`Text`
        The subtitle Text.
    subtitleColor : anyOf(None, :class:`Color`)
        Text color for subtitle text.
    subtitleFont : string
        Font name for subtitle text.
    subtitleFontSize : float
        Font size in pixels for subtitle text.
    subtitleFontStyle : :class:`FontStyle`
        Font style for subtitle text.
    subtitleFontWeight : :class:`FontWeight`
        Font weight for subtitle text.
        This can be either a string (e.g ``"bold"``, ``"normal"`` ) or a number ( ``100``,
        ``200``, ``300``, ..., ``900`` where ``"normal"`` = ``400`` and ``"bold"`` = ``700``
        ).
    subtitleLineHeight : float
        Line height in pixels for multi-line subtitle text.
    subtitlePadding : float
        The padding in pixels between title and subtitle text.
    zindex : float
        The integer z-index indicating the layering of the title group relative to other
        axis, mark and legend groups.

        **Default value:** ``0``.
    """
    _schema = {'$ref': '#/definitions/TitleParams'}
    _rootschema = Root._schema

    def __init__(self, text=Undefined, align=Undefined, anchor=Undefined, angle=Undefined,
                 baseline=Undefined, color=Undefined, dx=Undefined, dy=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, frame=Undefined,
                 limit=Undefined, lineHeight=Undefined, offset=Undefined, orient=Undefined,
                 style=Undefined, subtitle=Undefined, subtitleColor=Undefined, subtitleFont=Undefined,
                 subtitleFontSize=Undefined, subtitleFontStyle=Undefined, subtitleFontWeight=Undefined,
                 subtitleLineHeight=Undefined, subtitlePadding=Undefined, zindex=Undefined, **kwds):
        super(TitleParams, self).__init__(text=text, align=align, anchor=anchor, angle=angle,
                                          baseline=baseline, color=color, dx=dx, dy=dy, font=font,
                                          fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight,
                                          frame=frame, limit=limit, lineHeight=lineHeight,
                                          offset=offset, orient=orient, style=style, subtitle=subtitle,
                                          subtitleColor=subtitleColor, subtitleFont=subtitleFont,
                                          subtitleFontSize=subtitleFontSize,
                                          subtitleFontStyle=subtitleFontStyle,
                                          subtitleFontWeight=subtitleFontWeight,
                                          subtitleLineHeight=subtitleLineHeight,
                                          subtitlePadding=subtitlePadding, zindex=zindex, **kwds)


class TooltipContent(VegaLiteSchema):
    """TooltipContent schema wrapper

    Mapping(required=[content])

    Attributes
    ----------

    content : enum('encoding', 'data')

    """
    _schema = {'$ref': '#/definitions/TooltipContent'}
    _rootschema = Root._schema

    def __init__(self, content=Undefined, **kwds):
        super(TooltipContent, self).__init__(content=content, **kwds)


class TopLevelSpec(VegaLiteSchema):
    """TopLevelSpec schema wrapper

    anyOf(:class:`TopLevelUnitSpec`, :class:`TopLevelFacetSpec`, :class:`TopLevelLayerSpec`,
    :class:`TopLevelRepeatSpec`, :class:`TopLevelConcatSpec`, :class:`TopLevelVConcatSpec`,
    :class:`TopLevelHConcatSpec`)
    A Vega-Lite top-level specification.
    This is the root class for all Vega-Lite specifications.
    (The json schema is generated from this type.)
    """
    _schema = {'$ref': '#/definitions/TopLevelSpec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TopLevelSpec, self).__init__(*args, **kwds)


class TopLevelConcatSpec(TopLevelSpec):
    """TopLevelConcatSpec schema wrapper

    Mapping(required=[concat])

    Attributes
    ----------

    concat : List(:class:`Spec`)
        A list of views to be concatenated.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    config : :class:`Config`
        Vega-Lite configuration object. This property can only be defined at the top-level
        of a specification.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
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
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, concat=Undefined, align=Undefined, autosize=Undefined, background=Undefined,
                 bounds=Undefined, center=Undefined, columns=Undefined, config=Undefined,
                 data=Undefined, datasets=Undefined, description=Undefined, name=Undefined,
                 padding=Undefined, resolve=Undefined, spacing=Undefined, title=Undefined,
                 transform=Undefined, usermeta=Undefined, **kwds):
        super(TopLevelConcatSpec, self).__init__(concat=concat, align=align, autosize=autosize,
                                                 background=background, bounds=bounds, center=center,
                                                 columns=columns, config=config, data=data,
                                                 datasets=datasets, description=description, name=name,
                                                 padding=padding, resolve=resolve, spacing=spacing,
                                                 title=title, transform=transform, usermeta=usermeta,
                                                 **kwds)


class TopLevelFacetSpec(TopLevelSpec):
    """TopLevelFacetSpec schema wrapper

    Mapping(required=[data, facet, spec])

    Attributes
    ----------

    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    facet : anyOf(:class:`FacetFieldDef`, :class:`FacetMapping`)
        Definition for how to facet the data. One of:
        1) `a field definition for faceting the plot by one field
        <https://vega.github.io/vega-lite/docs/facet.html#field-def>`__
        2) `An object that maps row and column channels to their field definitions
        <https://vega.github.io/vega-lite/docs/facet.html#mapping>`__
    spec : anyOf(:class:`LayerSpec`, :class:`FacetedUnitSpec`)
        A specification of the view that gets faceted.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    config : :class:`Config`
        Vega-Lite configuration object. This property can only be defined at the top-level
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
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelFacetSpec'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, facet=Undefined, spec=Undefined, align=Undefined,
                 autosize=Undefined, background=Undefined, bounds=Undefined, center=Undefined,
                 columns=Undefined, config=Undefined, datasets=Undefined, description=Undefined,
                 name=Undefined, padding=Undefined, resolve=Undefined, spacing=Undefined,
                 title=Undefined, transform=Undefined, usermeta=Undefined, **kwds):
        super(TopLevelFacetSpec, self).__init__(data=data, facet=facet, spec=spec, align=align,
                                                autosize=autosize, background=background, bounds=bounds,
                                                center=center, columns=columns, config=config,
                                                datasets=datasets, description=description, name=name,
                                                padding=padding, resolve=resolve, spacing=spacing,
                                                title=title, transform=transform, usermeta=usermeta,
                                                **kwds)


class TopLevelHConcatSpec(TopLevelSpec):
    """TopLevelHConcatSpec schema wrapper

    Mapping(required=[hconcat])

    Attributes
    ----------

    hconcat : List(:class:`Spec`)
        A list of views to be concatenated and put into a row.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
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
        Vega-Lite configuration object. This property can only be defined at the top-level
        of a specification.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
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
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelHConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, autosize=Undefined, background=Undefined, bounds=Undefined,
                 center=Undefined, config=Undefined, data=Undefined, datasets=Undefined,
                 description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined,
                 spacing=Undefined, title=Undefined, transform=Undefined, usermeta=Undefined, **kwds):
        super(TopLevelHConcatSpec, self).__init__(hconcat=hconcat, autosize=autosize,
                                                  background=background, bounds=bounds, center=center,
                                                  config=config, data=data, datasets=datasets,
                                                  description=description, name=name, padding=padding,
                                                  resolve=resolve, spacing=spacing, title=title,
                                                  transform=transform, usermeta=usermeta, **kwds)


class TopLevelLayerSpec(TopLevelSpec):
    """TopLevelLayerSpec schema wrapper

    Mapping(required=[layer])

    Attributes
    ----------

    layer : List(anyOf(:class:`LayerSpec`, :class:`UnitSpec`))
        Layer or single view specifications to be layered.

        **Note** : Specifications inside ``layer`` cannot use ``row`` and ``column``
        channels as layering facet specifications is not allowed. Instead, use the `facet
        operator <https://vega.github.io/vega-lite/docs/facet.html>`__ and place a layer
        inside a facet.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
    config : :class:`Config`
        Vega-Lite configuration object. This property can only be defined at the top-level
        of a specification.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
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
    height : anyOf(float, enum('container'), :class:`Step`)
        The height of a visualization.


        * For a plot with a continuous y-field, height should be a number.
        * For a plot with either a discrete y-field or no y-field, height can be either a
          number indicating a fixed height or an object in the form of ``{step: number}``
          defining the height per discrete step. (No y-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on height, it should be set to ``"container"``.

        **Default value:** Based on ``config.view.continuousHeight`` for a plot with a
        continuous y-field and ``config.view.discreteHeight`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view and the ``"container"`` option cannot be used.

        **See also:** `height <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    projection : :class:`Projection`
        An object defining properties of the geographic projection shared by underlying
        layers.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    view : :class:`ViewBackground`
        An object defining the view background's fill and stroke.

        **Default value:** none (transparent)
    width : anyOf(float, enum('container'), :class:`Step`)
        The width of a visualization.


        * For a plot with a continuous x-field, width should be a number.
        * For a plot with either a discrete x-field or no x-field, width can be either a
          number indicating a fixed width or an object in the form of ``{step: number}``
          defining the width per discrete step. (No x-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on width, it should be set to ``"container"``.

        **Default value:**
        Based on ``config.view.continuousWidth`` for a plot with a continuous x-field and
        ``config.view.discreteWidth`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view and the ``"container"`` option cannot be used.

        **See also:** `width <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelLayerSpec'}
    _rootschema = Root._schema

    def __init__(self, layer=Undefined, autosize=Undefined, background=Undefined, config=Undefined,
                 data=Undefined, datasets=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, padding=Undefined, projection=Undefined,
                 resolve=Undefined, title=Undefined, transform=Undefined, usermeta=Undefined,
                 view=Undefined, width=Undefined, **kwds):
        super(TopLevelLayerSpec, self).__init__(layer=layer, autosize=autosize, background=background,
                                                config=config, data=data, datasets=datasets,
                                                description=description, encoding=encoding,
                                                height=height, name=name, padding=padding,
                                                projection=projection, resolve=resolve, title=title,
                                                transform=transform, usermeta=usermeta, view=view,
                                                width=width, **kwds)


class TopLevelRepeatSpec(TopLevelSpec):
    """TopLevelRepeatSpec schema wrapper

    Mapping(required=[repeat, spec])

    Attributes
    ----------

    repeat : anyOf(List(string), :class:`RepeatMapping`)
        Definition for fields to be repeated. One of:
        1) An array of fields to be repeated. If ``"repeat"`` is an array, the field can be
        referred using ``{"repeat": "repeat"}``
        2) An object that mapped ``"row"`` and/or ``"column"`` to the listed of fields to be
        repeated along the particular orientations. The objects ``{"repeat": "row"}`` and
        ``{"repeat": "column"}`` can be used to refer to the repeated field respectively.
    spec : :class:`Spec`
        A specification of the view that gets repeated.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
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
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
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
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to
        ``hconcat`` (for ``concat`` ) and to using the ``column`` channel (for ``facet`` and
        ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    config : :class:`Config`
        Vega-Lite configuration object. This property can only be defined at the top-level
        of a specification.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
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
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator.
        An object of the form ``{"row": number, "column": number}`` can be used to set
        different spacing values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelRepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, align=Undefined, autosize=Undefined,
                 background=Undefined, bounds=Undefined, center=Undefined, columns=Undefined,
                 config=Undefined, data=Undefined, datasets=Undefined, description=Undefined,
                 name=Undefined, padding=Undefined, resolve=Undefined, spacing=Undefined,
                 title=Undefined, transform=Undefined, usermeta=Undefined, **kwds):
        super(TopLevelRepeatSpec, self).__init__(repeat=repeat, spec=spec, align=align,
                                                 autosize=autosize, background=background,
                                                 bounds=bounds, center=center, columns=columns,
                                                 config=config, data=data, datasets=datasets,
                                                 description=description, name=name, padding=padding,
                                                 resolve=resolve, spacing=spacing, title=title,
                                                 transform=transform, usermeta=usermeta, **kwds)


class TopLevelUnitSpec(TopLevelSpec):
    """TopLevelUnitSpec schema wrapper

    Mapping(required=[data, mark])

    Attributes
    ----------

    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    config : :class:`Config`
        Vega-Lite configuration object. This property can only be defined at the top-level
        of a specification.
    datasets : :class:`Datasets`
        A global data store for named datasets. This is a mapping from names to inline
        datasets.
        This can be an array of objects or primitive values or a string. Arrays of primitive
        values are ingested as objects with a ``data`` property.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`FacetedEncoding`
        A key-value mapping between encoding channels and definition of fields.
    height : anyOf(float, enum('container'), :class:`Step`)
        The height of a visualization.


        * For a plot with a continuous y-field, height should be a number.
        * For a plot with either a discrete y-field or no y-field, height can be either a
          number indicating a fixed height or an object in the form of ``{step: number}``
          defining the height per discrete step. (No y-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on height, it should be set to ``"container"``.

        **Default value:** Based on ``config.view.continuousHeight`` for a plot with a
        continuous y-field and ``config.view.discreteHeight`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view and the ``"container"`` option cannot be used.

        **See also:** `height <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    name : string
        Name of the visualization for later reference.
    padding : :class:`Padding`
        The default visualization padding, in pixels, from the edge of the visualization
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    view : :class:`ViewBackground`
        An object defining the view background's fill and stroke.

        **Default value:** none (transparent)
    width : anyOf(float, enum('container'), :class:`Step`)
        The width of a visualization.


        * For a plot with a continuous x-field, width should be a number.
        * For a plot with either a discrete x-field or no x-field, width can be either a
          number indicating a fixed width or an object in the form of ``{step: number}``
          defining the width per discrete step. (No x-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on width, it should be set to ``"container"``.

        **Default value:**
        Based on ``config.view.continuousWidth`` for a plot with a continuous x-field and
        ``config.view.discreteWidth`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view and the ``"container"`` option cannot be used.

        **See also:** `width <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelUnitSpec'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, mark=Undefined, autosize=Undefined, background=Undefined,
                 bounds=Undefined, config=Undefined, datasets=Undefined, description=Undefined,
                 encoding=Undefined, height=Undefined, name=Undefined, padding=Undefined,
                 projection=Undefined, resolve=Undefined, selection=Undefined, title=Undefined,
                 transform=Undefined, usermeta=Undefined, view=Undefined, width=Undefined, **kwds):
        super(TopLevelUnitSpec, self).__init__(data=data, mark=mark, autosize=autosize,
                                               background=background, bounds=bounds, config=config,
                                               datasets=datasets, description=description,
                                               encoding=encoding, height=height, name=name,
                                               padding=padding, projection=projection, resolve=resolve,
                                               selection=selection, title=title, transform=transform,
                                               usermeta=usermeta, view=view, width=width, **kwds)


class TopLevelVConcatSpec(TopLevelSpec):
    """TopLevelVConcatSpec schema wrapper

    Mapping(required=[vconcat])

    Attributes
    ----------

    vconcat : List(:class:`Spec`)
        A list of views to be concatenated and put into a column.
    autosize : anyOf(:class:`AutosizeType`, :class:`AutoSizeParams`)
        How the visualization size should be determined. If a string, should be one of
        ``"pad"``, ``"fit"`` or ``"none"``.
        Object values can additionally specify parameters for content sizing and automatic
        resizing.

        **Default value** : ``pad``
    background : :class:`Color`
        CSS color property to use as the background of the entire view.

        **Default value:** ``"white"``
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
        Vega-Lite configuration object. This property can only be defined at the top-level
        of a specification.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
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
        canvas to the data rectangle. If a number, specifies padding for all sides.
        If an object, the value should have the format ``{"left": 5, "top": 5, "right": 5,
        "bottom": 5}`` to specify padding for each side of the visualization.

        **Default value** : ``5``
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    usermeta : Mapping(required=[])
        Optional metadata that will be passed to Vega.
        This object is completely ignored by Vega and Vega-Lite and can be used for custom
        metadata.
    $schema : string
        URL to `JSON schema <http://json-schema.org/>`__ for a Vega-Lite specification.
        Unless you have a reason to change this, use
        ``https://vega.github.io/schema/vega-lite/v4.json``. Setting the ``$schema``
        property allows automatic validation and autocomplete in editors that support JSON
        schema.
    """
    _schema = {'$ref': '#/definitions/TopLevelVConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, autosize=Undefined, background=Undefined, bounds=Undefined,
                 center=Undefined, config=Undefined, data=Undefined, datasets=Undefined,
                 description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined,
                 spacing=Undefined, title=Undefined, transform=Undefined, usermeta=Undefined, **kwds):
        super(TopLevelVConcatSpec, self).__init__(vconcat=vconcat, autosize=autosize,
                                                  background=background, bounds=bounds, center=center,
                                                  config=config, data=data, datasets=datasets,
                                                  description=description, name=name, padding=padding,
                                                  resolve=resolve, spacing=spacing, title=title,
                                                  transform=transform, usermeta=usermeta, **kwds)


class TopoDataFormat(DataFormat):
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
    parse : anyOf(:class:`Parse`, None)
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
        For Specific date formats can be provided (e.g., ``{foo: "date:'%m%d%Y'"}`` ), using
        the `d3-time-format syntax <https://github.com/d3/d3-time-format#locale_format>`__.
        UTC date format parsing is supported similarly (e.g., ``{foo: "utc:'%m%d%Y'"}`` ).
        See more about `UTC time
        <https://vega.github.io/vega-lite/docs/timeunit.html#utc>`__
    type : enum('topojson')
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``, ``"dsv"``.

        **Default value:**  The default format type is determined by the extension of the
        file URL.
        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/TopoDataFormat'}
    _rootschema = Root._schema

    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(TopoDataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, type=type, **kwds)


class Transform(VegaLiteSchema):
    """Transform schema wrapper

    anyOf(:class:`AggregateTransform`, :class:`BinTransform`, :class:`CalculateTransform`,
    :class:`DensityTransform`, :class:`FilterTransform`, :class:`FlattenTransform`,
    :class:`FoldTransform`, :class:`ImputeTransform`, :class:`JoinAggregateTransform`,
    :class:`LoessTransform`, :class:`LookupTransform`, :class:`QuantileTransform`,
    :class:`RegressionTransform`, :class:`TimeUnitTransform`, :class:`SampleTransform`,
    :class:`StackTransform`, :class:`WindowTransform`, :class:`PivotTransform`)
    """
    _schema = {'$ref': '#/definitions/Transform'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Transform, self).__init__(*args, **kwds)


class AggregateTransform(Transform):
    """AggregateTransform schema wrapper

    Mapping(required=[aggregate])

    Attributes
    ----------

    aggregate : List(:class:`AggregatedFieldDef`)
        Array of objects that define fields to aggregate.
    groupby : List(:class:`FieldName`)
        The data fields to group by. If not specified, a single group containing all data
        objects will be used.
    """
    _schema = {'$ref': '#/definitions/AggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, groupby=Undefined, **kwds):
        super(AggregateTransform, self).__init__(aggregate=aggregate, groupby=groupby, **kwds)


class BinTransform(Transform):
    """BinTransform schema wrapper

    Mapping(required=[bin, field, as])

    Attributes
    ----------

    bin : anyOf(enum(True), :class:`BinParams`)
        An object indicating bin properties, or simply ``true`` for using default bin
        parameters.
    field : :class:`FieldName`
        The data field to bin.
    as : anyOf(:class:`FieldName`, List(:class:`FieldName`))
        The output fields at which to write the start and end bin values.
    """
    _schema = {'$ref': '#/definitions/BinTransform'}
    _rootschema = Root._schema

    def __init__(self, bin=Undefined, field=Undefined, **kwds):
        super(BinTransform, self).__init__(bin=bin, field=field, **kwds)


class CalculateTransform(Transform):
    """CalculateTransform schema wrapper

    Mapping(required=[calculate, as])

    Attributes
    ----------

    calculate : string
        A `expression <https://vega.github.io/vega-lite/docs/types.html#expression>`__
        string. Use the variable ``datum`` to refer to the current data object.
    as : :class:`FieldName`
        The field for storing the computed formula value.
    """
    _schema = {'$ref': '#/definitions/CalculateTransform'}
    _rootschema = Root._schema

    def __init__(self, calculate=Undefined, **kwds):
        super(CalculateTransform, self).__init__(calculate=calculate, **kwds)


class DensityTransform(Transform):
    """DensityTransform schema wrapper

    Mapping(required=[density])

    Attributes
    ----------

    density : :class:`FieldName`
        The data field for which to perform density estimation.
    bandwidth : float
        The bandwidth (standard deviation) of the Gaussian kernel. If unspecified or set to
        zero, the bandwidth value is automatically estimated from the input data using
        Scott’s rule.
    counts : boolean
        A boolean flag indicating if the output values should be probability estimates
        (false) or smoothed counts (true).

        **Default value:** ``false``
    cumulative : boolean
        A boolean flag indicating whether to produce density estimates (false) or cumulative
        density estimates (true).

        **Default value:** ``false``
    extent : List([float, float])
        A [min, max] domain from which to sample the distribution. If unspecified, the
        extent will be determined by the observed minimum and maximum values of the density
        value field.
    groupby : List(:class:`FieldName`)
        The data fields to group by. If not specified, a single group containing all data
        objects will be used.
    maxsteps : float
        The maximum number of samples to take along the extent domain for plotting the
        density.

        **Default value:** ``200``
    minsteps : float
        The minimum number of samples to take along the extent domain for plotting the
        density.

        **Default value:** ``25``
    steps : float
        The exact number of samples to take along the extent domain for plotting the
        density. If specified, overrides both minsteps and maxsteps to set an exact number
        of uniform samples. Potentially useful in conjunction with a fixed extent to ensure
        consistent sample points for stacked densities.
    as : List([:class:`FieldName`, :class:`FieldName`])
        The output fields for the sample value and corresponding density estimate.

        **Default value:** ``["value", "density"]``
    """
    _schema = {'$ref': '#/definitions/DensityTransform'}
    _rootschema = Root._schema

    def __init__(self, density=Undefined, bandwidth=Undefined, counts=Undefined, cumulative=Undefined,
                 extent=Undefined, groupby=Undefined, maxsteps=Undefined, minsteps=Undefined,
                 steps=Undefined, **kwds):
        super(DensityTransform, self).__init__(density=density, bandwidth=bandwidth, counts=counts,
                                               cumulative=cumulative, extent=extent, groupby=groupby,
                                               maxsteps=maxsteps, minsteps=minsteps, steps=steps, **kwds)


class FilterTransform(Transform):
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
        `oneOf <https://vega.github.io/vega-lite/docs/filter.html#one-of-predicate>`__,
        or `valid <https://vega.github.io/vega-lite/docs/filter.html#valid-predicate>`__,

        3) a `selection predicate
        <https://vega.github.io/vega-lite/docs/filter.html#selection-predicate>`__

        4) a logical operand that combines (1), (2), or (3).
    """
    _schema = {'$ref': '#/definitions/FilterTransform'}
    _rootschema = Root._schema

    def __init__(self, filter=Undefined, **kwds):
        super(FilterTransform, self).__init__(filter=filter, **kwds)


class FlattenTransform(Transform):
    """FlattenTransform schema wrapper

    Mapping(required=[flatten])

    Attributes
    ----------

    flatten : List(:class:`FieldName`)
        An array of one or more data fields containing arrays to flatten.
        If multiple fields are specified, their array values should have a parallel
        structure, ideally with the same length.
        If the lengths of parallel arrays do not match,
        the longest array will be used with ``null`` values added for missing entries.
    as : List(:class:`FieldName`)
        The output field names for extracted array values.

        **Default value:** The field name of the corresponding array field
    """
    _schema = {'$ref': '#/definitions/FlattenTransform'}
    _rootschema = Root._schema

    def __init__(self, flatten=Undefined, **kwds):
        super(FlattenTransform, self).__init__(flatten=flatten, **kwds)


class FoldTransform(Transform):
    """FoldTransform schema wrapper

    Mapping(required=[fold])

    Attributes
    ----------

    fold : List(:class:`FieldName`)
        An array of data fields indicating the properties to fold.
    as : List([:class:`FieldName`, :class:`FieldName`])
        The output field names for the key and value properties produced by the fold
        transform.
        **Default value:** ``["key", "value"]``
    """
    _schema = {'$ref': '#/definitions/FoldTransform'}
    _rootschema = Root._schema

    def __init__(self, fold=Undefined, **kwds):
        super(FoldTransform, self).__init__(fold=fold, **kwds)


class ImputeTransform(Transform):
    """ImputeTransform schema wrapper

    Mapping(required=[impute, key])

    Attributes
    ----------

    impute : :class:`FieldName`
        The data field for which the missing values should be imputed.
    key : :class:`FieldName`
        A key field that uniquely identifies data objects within a group.
        Missing key values (those occurring in the data but not in the current group) will
        be imputed.
    frame : List([anyOf(None, float), anyOf(None, float)])
        A frame specification as a two-element array used to control the window over which
        the specified method is applied. The array entries should either be a number
        indicating the offset from the current data object, or null to indicate unbounded
        rows preceding or following the current data object. For example, the value ``[-5,
        5]`` indicates that the window should include five objects preceding and five
        objects following the current object.

        **Default value:** :  ``[null, null]`` indicating that the window includes all
        objects.
    groupby : List(:class:`FieldName`)
        An optional array of fields by which to group the values.
        Imputation will then be performed on a per-group basis.
    keyvals : anyOf(List(Any), :class:`ImputeSequence`)
        Defines the key values that should be considered for imputation.
        An array of key values or an object defining a `number sequence
        <https://vega.github.io/vega-lite/docs/impute.html#sequence-def>`__.

        If provided, this will be used in addition to the key values observed within the
        input data. If not provided, the values will be derived from all unique values of
        the ``key`` field. For ``impute`` in ``encoding``, the key field is the x-field if
        the y-field is imputed, or vice versa.

        If there is no impute grouping, this property *must* be specified.
    method : :class:`ImputeMethod`
        The imputation method to use for the field value of imputed data objects.
        One of ``"value"``, ``"mean"``, ``"median"``, ``"max"`` or ``"min"``.

        **Default value:**  ``"value"``
    value : Any
        The field value to use when the imputation ``method`` is ``"value"``.
    """
    _schema = {'$ref': '#/definitions/ImputeTransform'}
    _rootschema = Root._schema

    def __init__(self, impute=Undefined, key=Undefined, frame=Undefined, groupby=Undefined,
                 keyvals=Undefined, method=Undefined, value=Undefined, **kwds):
        super(ImputeTransform, self).__init__(impute=impute, key=key, frame=frame, groupby=groupby,
                                              keyvals=keyvals, method=method, value=value, **kwds)


class JoinAggregateTransform(Transform):
    """JoinAggregateTransform schema wrapper

    Mapping(required=[joinaggregate])

    Attributes
    ----------

    joinaggregate : List(:class:`JoinAggregateFieldDef`)
        The definition of the fields in the join aggregate, and what calculations to use.
    groupby : List(:class:`FieldName`)
        The data fields for partitioning the data objects into separate groups. If
        unspecified, all data points will be in a single group.
    """
    _schema = {'$ref': '#/definitions/JoinAggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, joinaggregate=Undefined, groupby=Undefined, **kwds):
        super(JoinAggregateTransform, self).__init__(joinaggregate=joinaggregate, groupby=groupby,
                                                     **kwds)


class LoessTransform(Transform):
    """LoessTransform schema wrapper

    Mapping(required=[loess, on])

    Attributes
    ----------

    loess : :class:`FieldName`
        The data field of the dependent variable to smooth.
    on : :class:`FieldName`
        The data field of the independent variable to use a predictor.
    bandwidth : float
        A bandwidth parameter in the range ``[0, 1]`` that determines the amount of
        smoothing.

        **Default value:** ``0.3``
    groupby : List(:class:`FieldName`)
        The data fields to group by. If not specified, a single group containing all data
        objects will be used.
    as : List([:class:`FieldName`, :class:`FieldName`])
        The output field names for the smoothed points generated by the loess transform.

        **Default value:** The field names of the input x and y values.
    """
    _schema = {'$ref': '#/definitions/LoessTransform'}
    _rootschema = Root._schema

    def __init__(self, loess=Undefined, on=Undefined, bandwidth=Undefined, groupby=Undefined, **kwds):
        super(LoessTransform, self).__init__(loess=loess, on=on, bandwidth=bandwidth, groupby=groupby,
                                             **kwds)


class LookupTransform(Transform):
    """LookupTransform schema wrapper

    Mapping(required=[lookup, from])

    Attributes
    ----------

    lookup : string
        Key in primary data source.
    default : string
        The default value to use if lookup fails.

        **Default value:** ``null``
    as : anyOf(:class:`FieldName`, List(:class:`FieldName`))
        The output fields on which to store the looked up data values.

        For data lookups, this property may be left blank if ``from.fields``
        has been specified (those field names will be used); if ``from.fields``
        has not been specified, ``as`` must be a string.

        For selection lookups, this property is optional: if unspecified,
        looked up values will be stored under a property named for the selection;
        and if specified, it must correspond to ``from.fields``.
    from : anyOf(:class:`LookupData`, :class:`LookupSelection`)
        Data source or selection for secondary data reference.
    """
    _schema = {'$ref': '#/definitions/LookupTransform'}
    _rootschema = Root._schema

    def __init__(self, lookup=Undefined, default=Undefined, **kwds):
        super(LookupTransform, self).__init__(lookup=lookup, default=default, **kwds)


class PivotTransform(Transform):
    """PivotTransform schema wrapper

    Mapping(required=[pivot, value])

    Attributes
    ----------

    pivot : :class:`FieldName`
        The data field to pivot on. The unique values of this field become new field names
        in the output stream.
    value : :class:`FieldName`
        The data field to populate pivoted fields. The aggregate values of this field become
        the values of the new pivoted fields.
    groupby : List(:class:`FieldName`)
        The optional data fields to group by. If not specified, a single group containing
        all data objects will be used.
    limit : float
        An optional parameter indicating the maximum number of pivoted fields to generate.
        The default ( ``0`` ) applies no limit. The pivoted ``pivot`` names are sorted in
        ascending order prior to enforcing the limit.
        **Default value:** ``0``
    op : string
        The aggregation operation to apply to grouped ``value`` field values.
        **Default value:** ``sum``
    """
    _schema = {'$ref': '#/definitions/PivotTransform'}
    _rootschema = Root._schema

    def __init__(self, pivot=Undefined, value=Undefined, groupby=Undefined, limit=Undefined,
                 op=Undefined, **kwds):
        super(PivotTransform, self).__init__(pivot=pivot, value=value, groupby=groupby, limit=limit,
                                             op=op, **kwds)


class QuantileTransform(Transform):
    """QuantileTransform schema wrapper

    Mapping(required=[quantile])

    Attributes
    ----------

    quantile : :class:`FieldName`
        The data field for which to perform quantile estimation.
    groupby : List(:class:`FieldName`)
        The data fields to group by. If not specified, a single group containing all data
        objects will be used.
    probs : List(float)
        An array of probabilities in the range (0, 1) for which to compute quantile values.
        If not specified, the *step* parameter will be used.
    step : float
        A probability step size (default 0.01) for sampling quantile values. All values from
        one-half the step size up to 1 (exclusive) will be sampled. This parameter is only
        used if the *probs* parameter is not provided.
    as : List([:class:`FieldName`, :class:`FieldName`])
        The output field names for the probability and quantile values.

        **Default value:** ``["prob", "value"]``
    """
    _schema = {'$ref': '#/definitions/QuantileTransform'}
    _rootschema = Root._schema

    def __init__(self, quantile=Undefined, groupby=Undefined, probs=Undefined, step=Undefined, **kwds):
        super(QuantileTransform, self).__init__(quantile=quantile, groupby=groupby, probs=probs,
                                                step=step, **kwds)


class RegressionTransform(Transform):
    """RegressionTransform schema wrapper

    Mapping(required=[regression, on])

    Attributes
    ----------

    on : :class:`FieldName`
        The data field of the independent variable to use a predictor.
    regression : :class:`FieldName`
        The data field of the dependent variable to predict.
    extent : List([float, float])
        A [min, max] domain over the independent (x) field for the starting and ending
        points of the generated trend line.
    groupby : List(:class:`FieldName`)
        The data fields to group by. If not specified, a single group containing all data
        objects will be used.
    method : enum('linear', 'log', 'exp', 'pow', 'quad', 'poly')
        The functional form of the regression model. One of ``"linear"``, ``"log"``,
        ``"exp"``, ``"pow"``, ``"quad"``, or ``"poly"``.

        **Default value:** ``"linear"``
    order : float
        The polynomial order (number of coefficients) for the 'poly' method.

        **Default value:** ``3``
    params : boolean
        A boolean flag indicating if the transform should return the regression model
        parameters (one object per group), rather than trend line points.
        The resulting objects include a ``coef`` array of fitted coefficient values
        (starting with the intercept term and then including terms of increasing order)
        and an ``rSquared`` value (indicating the total variance explained by the model).

        **Default value:** ``false``
    as : List([:class:`FieldName`, :class:`FieldName`])
        The output field names for the smoothed points generated by the regression
        transform.

        **Default value:** The field names of the input x and y values.
    """
    _schema = {'$ref': '#/definitions/RegressionTransform'}
    _rootschema = Root._schema

    def __init__(self, on=Undefined, regression=Undefined, extent=Undefined, groupby=Undefined,
                 method=Undefined, order=Undefined, params=Undefined, **kwds):
        super(RegressionTransform, self).__init__(on=on, regression=regression, extent=extent,
                                                  groupby=groupby, method=method, order=order,
                                                  params=params, **kwds)


class SampleTransform(Transform):
    """SampleTransform schema wrapper

    Mapping(required=[sample])

    Attributes
    ----------

    sample : float
        The maximum number of data objects to include in the sample.

        **Default value:** ``1000``
    """
    _schema = {'$ref': '#/definitions/SampleTransform'}
    _rootschema = Root._schema

    def __init__(self, sample=Undefined, **kwds):
        super(SampleTransform, self).__init__(sample=sample, **kwds)


class StackTransform(Transform):
    """StackTransform schema wrapper

    Mapping(required=[stack, groupby, as])

    Attributes
    ----------

    groupby : List(:class:`FieldName`)
        The data fields to group by.
    stack : :class:`FieldName`
        The field which is stacked.
    offset : enum('zero', 'center', 'normalize')
        Mode for stacking marks. One of ``"zero"`` (default), ``"center"``, or
        ``"normalize"``.
        The ``"zero"`` offset will stack starting at ``0``. The ``"center"`` offset will
        center the stacks. The ``"normalize"`` offset will compute percentage values for
        each stack point, with output values in the range ``[0,1]``.

        **Default value:** ``"zero"``
    sort : List(:class:`SortField`)
        Field that determines the order of leaves in the stacked charts.
    as : anyOf(:class:`FieldName`, List([:class:`FieldName`, :class:`FieldName`]))
        Output field names. This can be either a string or an array of strings with two
        elements denoting the name for the fields for stack start and stack end
        respectively.
        If a single string(e.g., ``"val"`` ) is provided, the end field will be
        ``"val_end"``.
    """
    _schema = {'$ref': '#/definitions/StackTransform'}
    _rootschema = Root._schema

    def __init__(self, groupby=Undefined, stack=Undefined, offset=Undefined, sort=Undefined, **kwds):
        super(StackTransform, self).__init__(groupby=groupby, stack=stack, offset=offset, sort=sort,
                                             **kwds)


class TimeUnitTransform(Transform):
    """TimeUnitTransform schema wrapper

    Mapping(required=[timeUnit, field, as])

    Attributes
    ----------

    field : :class:`FieldName`
        The data field to apply time unit.
    timeUnit : :class:`TimeUnit`
        The timeUnit.
    as : :class:`FieldName`
        The output field to write the timeUnit value.
    """
    _schema = {'$ref': '#/definitions/TimeUnitTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, timeUnit=Undefined, **kwds):
        super(TimeUnitTransform, self).__init__(field=field, timeUnit=timeUnit, **kwds)


class TypeForShape(VegaLiteSchema):
    """TypeForShape schema wrapper

    enum('nominal', 'ordinal', 'geojson')
    """
    _schema = {'$ref': '#/definitions/TypeForShape'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TypeForShape, self).__init__(*args)


class TypedFieldDef(VegaLiteSchema):
    """TypedFieldDef schema wrapper

    Mapping(required=[type])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    type : :class:`StandardType`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        **Note:**


        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (for using a temporal scale) or `"ordinal" (for using
          an ordinal scale) <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat", "type": "quantitative"}``. The ``"type"`` of the aggregate output
          is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``"mean"``, ``"sum"``, ``"median"``, ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bin : anyOf(boolean, :class:`BinParams`, enum('binned'), None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#params>`__, or indicating that the
        data for ``x`` or ``y`` channel are binned before they are imported into Vega-Lite (
        ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:**
        1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access nested
        objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.
        2) ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _schema = {'$ref': '#/definitions/TypedFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, **kwds):
        super(TypedFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field,
                                            timeUnit=timeUnit, title=title, **kwds)


class UnitSpec(VegaLiteSchema):
    """UnitSpec schema wrapper

    Mapping(required=[mark])
    Base interface for a unit (single-view) specification.

    Attributes
    ----------

    mark : :class:`AnyMark`
        A string describing the mark type (one of ``"bar"``, ``"circle"``, ``"square"``,
        ``"tick"``, ``"line"``,
        ``"area"``, ``"point"``, ``"rule"``, ``"geoshape"``, and ``"text"`` ) or a `mark
        definition object <https://vega.github.io/vega-lite/docs/mark.html#mark-def>`__.
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    encoding : :class:`Encoding`
        A key-value mapping between encoding channels and definition of fields.
    height : anyOf(float, enum('container'), :class:`Step`)
        The height of a visualization.


        * For a plot with a continuous y-field, height should be a number.
        * For a plot with either a discrete y-field or no y-field, height can be either a
          number indicating a fixed height or an object in the form of ``{step: number}``
          defining the height per discrete step. (No y-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on height, it should be set to ``"container"``.

        **Default value:** Based on ``config.view.continuousHeight`` for a plot with a
        continuous y-field and ``config.view.discreteHeight`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        height of a single view and the ``"container"`` option cannot be used.

        **See also:** `height <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    name : string
        Name of the visualization for later reference.
    projection : :class:`Projection`
        An object defining properties of geographic projection, which will be applied to
        ``shape`` path for ``"geoshape"`` marks
        and to ``latitude`` and ``"longitude"`` channels for other marks.
    selection : Mapping(required=[])
        A key-value mapping between selection names and definitions.
    title : anyOf(:class:`Text`, :class:`TitleParams`)
        Title for the plot.
    transform : List(:class:`Transform`)
        An array of data transformations such as filter and new field calculation.
    view : :class:`ViewBackground`
        An object defining the view background's fill and stroke.

        **Default value:** none (transparent)
    width : anyOf(float, enum('container'), :class:`Step`)
        The width of a visualization.


        * For a plot with a continuous x-field, width should be a number.
        * For a plot with either a discrete x-field or no x-field, width can be either a
          number indicating a fixed width or an object in the form of ``{step: number}``
          defining the width per discrete step. (No x-field is equivalent to having one
          discrete step.)
        * To enable responsive sizing on width, it should be set to ``"container"``.

        **Default value:**
        Based on ``config.view.continuousWidth`` for a plot with a continuous x-field and
        ``config.view.discreteWidth`` otherwise.

        **Note:** For plots with `row and column channels
        <https://vega.github.io/vega-lite/docs/encoding.html#facet>`__, this represents the
        width of a single view and the ``"container"`` option cannot be used.

        **See also:** `width <https://vega.github.io/vega-lite/docs/size.html>`__
        documentation.
    """
    _schema = {'$ref': '#/definitions/UnitSpec'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined,
                 height=Undefined, name=Undefined, projection=Undefined, selection=Undefined,
                 title=Undefined, transform=Undefined, view=Undefined, width=Undefined, **kwds):
        super(UnitSpec, self).__init__(mark=mark, data=data, description=description, encoding=encoding,
                                       height=height, name=name, projection=projection,
                                       selection=selection, title=title, transform=transform, view=view,
                                       width=width, **kwds)


class UrlData(DataSource):
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


class UtcMultiTimeUnit(MultiTimeUnit):
    """UtcMultiTimeUnit schema wrapper

    enum('utcyearquarter', 'utcyearquartermonth', 'utcyearmonth', 'utcyearmonthdate',
    'utcyearmonthdatehours', 'utcyearmonthdatehoursminutes',
    'utcyearmonthdatehoursminutesseconds', 'utcquartermonth', 'utcmonthdate',
    'utcmonthdatehours', 'utchoursminutes', 'utchoursminutesseconds', 'utcminutesseconds',
    'utcsecondsmilliseconds')
    """
    _schema = {'$ref': '#/definitions/UtcMultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(UtcMultiTimeUnit, self).__init__(*args)


class UtcSingleTimeUnit(SingleTimeUnit):
    """UtcSingleTimeUnit schema wrapper

    enum('utcyear', 'utcquarter', 'utcmonth', 'utcday', 'utcdate', 'utchours', 'utcminutes',
    'utcseconds', 'utcmilliseconds')
    """
    _schema = {'$ref': '#/definitions/UtcSingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(UtcSingleTimeUnit, self).__init__(*args)


class VConcatSpec(Spec):
    """VConcatSpec schema wrapper

    Mapping(required=[vconcat])
    Base interface for a vertical concatenation specification.

    Attributes
    ----------

    vconcat : List(:class:`Spec`)
        A list of views to be concatenated and put into a column.
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
    data : anyOf(:class:`Data`, None)
        An object describing the data source. Set to ``null`` to ignore the parent's data
        source. If no data is set, it is derived from the parent.
    description : string
        Description of this mark for commenting purpose.
    name : string
        Name of the visualization for later reference.
    resolve : :class:`Resolve`
        Scale, axis, and legend resolutions for view composition specifications.
    spacing : float
        The spacing in pixels between sub-views of the concat operator.

        **Default value** : ``10``
    title : anyOf(:class:`Text`, :class:`TitleParams`)
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


class Value(SelectionInit):
    """Value schema wrapper

    anyOf(float, string, boolean, None)
    """
    _schema = {'$ref': '#/definitions/Value'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Value, self).__init__(*args)


class ValueDefWithConditionMarkPropFieldDefGradientstringnull(VegaLiteSchema):
    """ValueDefWithConditionMarkPropFieldDefGradientstringnull schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`,
    :class:`ConditionalValueDefGradientstringnull`,
    List(:class:`ConditionalValueDefGradientstringnull`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(:class:`Gradient`, string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDefWithCondition<MarkPropFieldDef,(Gradient|string|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithConditionMarkPropFieldDefGradientstringnull, self).__init__(condition=condition,
                                                                                      value=value,
                                                                                      **kwds)


class ValueDefWithConditionMarkPropFieldDefTypeForShapestringnull(VegaLiteSchema):
    """ValueDefWithConditionMarkPropFieldDefTypeForShapestringnull schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDefTypeForShape`,
    :class:`ConditionalStringValueDef`, List(:class:`ConditionalStringValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDefWithCondition<MarkPropFieldDef<TypeForShape>,(string|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithConditionMarkPropFieldDefTypeForShapestringnull, self).__init__(condition=condition,
                                                                                          value=value,
                                                                                          **kwds)


class ValueDefWithConditionMarkPropFieldDefnumber(VegaLiteSchema):
    """ValueDefWithConditionMarkPropFieldDefnumber schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalNumberValueDef`,
    List(:class:`ConditionalNumberValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDefWithCondition<MarkPropFieldDef,number>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithConditionMarkPropFieldDefnumber, self).__init__(condition=condition,
                                                                          value=value, **kwds)


class ValueDefWithConditionMarkPropFieldDefstringnull(VegaLiteSchema):
    """ValueDefWithConditionMarkPropFieldDefstringnull schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalStringValueDef`,
    List(:class:`ConditionalStringValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(string, None)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDefWithCondition<MarkPropFieldDef,(string|null)>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithConditionMarkPropFieldDefstringnull, self).__init__(condition=condition,
                                                                              value=value, **kwds)


class ValueDefWithConditionStringFieldDefText(VegaLiteSchema):
    """ValueDefWithConditionStringFieldDefText schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalStringFieldDef`, :class:`ConditionalValueDefText`,
    List(:class:`ConditionalValueDefText`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : :class:`Text`
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/ValueDefWithCondition<StringFieldDef,Text>'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithConditionStringFieldDefText, self).__init__(condition=condition, value=value,
                                                                      **kwds)


class Vector2DateTime(SelectionInitInterval):
    """Vector2DateTime schema wrapper

    List([:class:`DateTime`, :class:`DateTime`])
    """
    _schema = {'$ref': '#/definitions/Vector2<DateTime>'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Vector2DateTime, self).__init__(*args)


class Vector2Vector2number(VegaLiteSchema):
    """Vector2Vector2number schema wrapper

    List([:class:`Vector2number`, :class:`Vector2number`])
    """
    _schema = {'$ref': '#/definitions/Vector2<Vector2<number>>'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Vector2Vector2number, self).__init__(*args)


class Vector2boolean(SelectionInitInterval):
    """Vector2boolean schema wrapper

    List([boolean, boolean])
    """
    _schema = {'$ref': '#/definitions/Vector2<boolean>'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Vector2boolean, self).__init__(*args)


class Vector2number(SelectionInitInterval):
    """Vector2number schema wrapper

    List([float, float])
    """
    _schema = {'$ref': '#/definitions/Vector2<number>'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Vector2number, self).__init__(*args)


class Vector2string(SelectionInitInterval):
    """Vector2string schema wrapper

    List([string, string])
    """
    _schema = {'$ref': '#/definitions/Vector2<string>'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Vector2string, self).__init__(*args)


class Vector3number(VegaLiteSchema):
    """Vector3number schema wrapper

    List([float, float, float])
    """
    _schema = {'$ref': '#/definitions/Vector3<number>'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Vector3number, self).__init__(*args)


class ViewBackground(VegaLiteSchema):
    """ViewBackground schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    fill : anyOf(:class:`Color`, None)
        The fill color.

        **Default value:** ``undefined``
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    stroke : anyOf(:class:`Color`, None)
        The stroke color.

        **Default value:** ``"#ddd"``
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
        view background. A style is a named collection of mark property defaults defined
        within the `style configuration
        <https://vega.github.io/vega-lite/docs/mark.html#style-config>`__. If style is an
        array, later styles will override earlier styles.

        **Default value:** ``"cell"``
        **Note:** Any specified view background properties will augment the default style.
    """
    _schema = {'$ref': '#/definitions/ViewBackground'}
    _rootschema = Root._schema

    def __init__(self, cornerRadius=Undefined, fill=Undefined, fillOpacity=Undefined, opacity=Undefined,
                 stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, **kwds):
        super(ViewBackground, self).__init__(cornerRadius=cornerRadius, fill=fill,
                                             fillOpacity=fillOpacity, opacity=opacity, stroke=stroke,
                                             strokeCap=strokeCap, strokeDash=strokeDash,
                                             strokeDashOffset=strokeDashOffset, strokeJoin=strokeJoin,
                                             strokeMiterLimit=strokeMiterLimit,
                                             strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                             style=style, **kwds)


class ViewConfig(VegaLiteSchema):
    """ViewConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    clip : boolean
        Whether the view should be clipped.
    continuousHeight : float
        The default height when the plot has a continuous y-field.

        **Default value:** ``200``
    continuousWidth : float
        The default width when the plot has a continuous x-field.

        **Default value:** ``200``
    cornerRadius : float
        The radius in pixels of rounded rectangle corners.

        **Default value:** ``0``
    discreteHeight : anyOf(float, Mapping(required=[step]))
        The default height when the plot has either a discrete y-field or no y-field.

        **Default value:** a step size based on ``config.view.step``.
    discreteWidth : anyOf(float, Mapping(required=[step]))
        The default width when the plot has either a discrete x-field or no x-field.

        **Default value:** a step size based on ``config.view.step``.
    fill : anyOf(:class:`Color`, None)
        The fill color.

        **Default value:** ``undefined``
    fillOpacity : float
        The fill opacity (value between [0,1]).

        **Default value:** ``1``
    height : float
        Default height
    opacity : float
        The overall opacity (value between [0,1]).

        **Default value:** ``0.7`` for non-aggregate plots with ``point``, ``tick``,
        ``circle``, or ``square`` marks or layered ``bar`` charts and ``1`` otherwise.
    step : float
        Default step size for x-/y- discrete fields.
    stroke : anyOf(:class:`Color`, None)
        The stroke color.

        **Default value:** ``"#ddd"``
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
    width : float
        Default width
    """
    _schema = {'$ref': '#/definitions/ViewConfig'}
    _rootschema = Root._schema

    def __init__(self, clip=Undefined, continuousHeight=Undefined, continuousWidth=Undefined,
                 cornerRadius=Undefined, discreteHeight=Undefined, discreteWidth=Undefined,
                 fill=Undefined, fillOpacity=Undefined, height=Undefined, opacity=Undefined,
                 step=Undefined, stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeJoin=Undefined, strokeMiterLimit=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, width=Undefined, **kwds):
        super(ViewConfig, self).__init__(clip=clip, continuousHeight=continuousHeight,
                                         continuousWidth=continuousWidth, cornerRadius=cornerRadius,
                                         discreteHeight=discreteHeight, discreteWidth=discreteWidth,
                                         fill=fill, fillOpacity=fillOpacity, height=height,
                                         opacity=opacity, step=step, stroke=stroke, strokeCap=strokeCap,
                                         strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                         strokeJoin=strokeJoin, strokeMiterLimit=strokeMiterLimit,
                                         strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                         width=width, **kwds)


class WindowEventType(VegaLiteSchema):
    """WindowEventType schema wrapper

    anyOf(:class:`EventType`, string)
    """
    _schema = {'$ref': '#/definitions/WindowEventType'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(WindowEventType, self).__init__(*args, **kwds)


class EventType(WindowEventType):
    """EventType schema wrapper

    enum('click', 'dblclick', 'dragenter', 'dragleave', 'dragover', 'keydown', 'keypress',
    'keyup', 'mousedown', 'mousemove', 'mouseout', 'mouseover', 'mouseup', 'mousewheel',
    'timer', 'touchend', 'touchmove', 'touchstart', 'wheel')
    """
    _schema = {'$ref': '#/definitions/EventType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(EventType, self).__init__(*args)


class WindowFieldDef(VegaLiteSchema):
    """WindowFieldDef schema wrapper

    Mapping(required=[op, as])

    Attributes
    ----------

    op : anyOf(:class:`AggregateOp`, :class:`WindowOnlyOp`)
        The window or aggregation operation to apply within a window (e.g., ``"rank"``,
        ``"lead"``, ``"sum"``, ``"average"`` or ``"count"`` ). See the list of all supported
        operations `here <https://vega.github.io/vega-lite/docs/window.html#ops>`__.
    field : :class:`FieldName`
        The data field for which to compute the aggregate or window function. This can be
        omitted for window functions that do not operate over a field such as ``"count"``,
        ``"rank"``, ``"dense_rank"``.
    param : float
        Parameter values for the window functions. Parameter values can be omitted for
        operations that do not accept a parameter.

        See the list of all supported operations and their parameters `here
        <https://vega.github.io/vega-lite/docs/transforms/window.html>`__.
    as : :class:`FieldName`
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


class WindowTransform(Transform):
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
        that the window frame should always include all data objects. If you this frame and
        want to assign the same value to add objects, you can use the simpler `join
        aggregate transform <https://vega.github.io/vega-lite/docs/joinaggregate.html>`__.
        The only operators affected are the aggregation operations and the ``first_value``,
        ``last_value``, and ``nth_value`` window operations. The other window operations are
        not affected by this.

        **Default value:** :  ``[null, 0]`` (includes the current object and all preceding
        objects)
    groupby : List(:class:`FieldName`)
        The data fields for partitioning the data objects into separate windows. If
        unspecified, all data points will be in a single window.
    ignorePeers : boolean
        Indicates if the sliding window frame should ignore peer values (data that are
        considered identical by the sort criteria). The default is false, causing the window
        frame to expand to include all peer values. If set to true, the window frame will be
        defined by offset values only. This setting only affects those operations that
        depend on the window frame, namely aggregation operations and the first_value,
        last_value, and nth_value window operations.

        **Default value:** ``false``
    sort : List(:class:`SortField`)
        A sort field definition for sorting data objects within a window. If two data
        objects are considered equal by the comparator, they are considered "peer" values of
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


class XValueDef(VegaLiteSchema):
    """XValueDef schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Attributes
    ----------

    value : anyOf(float, enum('width'))
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/XValueDef'}
    _rootschema = Root._schema

    def __init__(self, value=Undefined, **kwds):
        super(XValueDef, self).__init__(value=value, **kwds)


class YValueDef(VegaLiteSchema):
    """YValueDef schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Attributes
    ----------

    value : anyOf(float, enum('height'))
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _schema = {'$ref': '#/definitions/YValueDef'}
    _rootschema = Root._schema

    def __init__(self, value=Undefined, **kwds):
        super(YValueDef, self).__init__(value=value, **kwds)

