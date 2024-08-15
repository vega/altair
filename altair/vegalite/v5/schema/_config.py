# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, Sequence, TypedDict

if TYPE_CHECKING:
    # ruff: noqa: F405
    from ._typing import *  # noqa: F403
    from .core import *  # noqa: F403


class RectConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: TextBaseline_T
    binSpacing: float
    blend: Blend_T
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    continuousBandSize: float
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    discreteBandSize: float
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    lineBreak: str
    lineHeight: float
    minBandSize: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    y: float | Literal["height"]
    y2: float | Literal["height"]


class AreaConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: TextBaseline_T
    blend: Blend_T
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    line: bool | OverlayMarkDefKwds
    lineBreak: str
    lineHeight: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    point: bool | OverlayMarkDefKwds | Literal["transparent"]
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    y: float | Literal["height"]
    y2: float | Literal["height"]


class AxisConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    aria: bool
    bandPosition: float
    description: str
    disable: bool
    domain: bool
    domainCap: StrokeCap_T
    domainColor: None | ColorHex | ColorName_T
    domainDash: Sequence[float]
    domainDashOffset: float
    domainOpacity: float
    domainWidth: float
    format: str
    formatType: str
    grid: bool
    gridCap: StrokeCap_T
    gridColor: None | ColorHex | ColorName_T
    gridDash: Sequence[float]
    gridDashOffset: float
    gridOpacity: float
    gridWidth: float
    labelAlign: Align_T
    labelAngle: float
    labelBaseline: TextBaseline_T
    labelBound: bool | float
    labelColor: None | ColorHex | ColorName_T
    labelExpr: str
    labelFlush: bool | float
    labelFlushOffset: float
    labelFont: str
    labelFontSize: float
    labelFontStyle: str
    labelFontWeight: FontWeight_T
    labelLimit: float
    labelLineHeight: float
    labelOffset: float
    labelOpacity: float
    labelOverlap: bool | Literal["greedy", "parity"]
    labelPadding: float
    labelSeparation: float
    labels: bool
    maxExtent: float
    minExtent: float
    offset: float
    orient: AxisOrient_T
    position: float
    style: str | Sequence[str]
    tickBand: Literal["center", "extent"]
    tickCap: StrokeCap_T
    tickColor: None | ColorHex | ColorName_T
    tickCount: float | TimeIntervalStepKwds | TimeInterval_T
    tickDash: Sequence[float]
    tickDashOffset: float
    tickExtra: bool
    tickMinStep: float
    tickOffset: float
    tickOpacity: float
    tickRound: bool
    tickSize: float
    tickWidth: float
    ticks: bool
    title: str | None | Sequence[str]
    titleAlign: Align_T
    titleAnchor: TitleAnchor_T
    titleAngle: float
    titleBaseline: TextBaseline_T
    titleColor: None | ColorHex | ColorName_T
    titleFont: str
    titleFontSize: float
    titleFontStyle: str
    titleFontWeight: FontWeight_T
    titleLimit: float
    titleLineHeight: float
    titleOpacity: float
    titlePadding: float
    titleX: float
    titleY: float
    translate: float
    values: Sequence[str] | Sequence[bool] | Sequence[float] | Sequence[DateTimeKwds]
    zindex: float


class BarConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: TextBaseline_T
    binSpacing: float
    blend: Blend_T
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    continuousBandSize: float
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusEnd: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    discreteBandSize: float
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    lineBreak: str
    lineHeight: float
    minBandSize: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    y: float | Literal["height"]
    y2: float | Literal["height"]


class BoxPlotConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    box: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    extent: float | Literal["min-max"]
    median: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    outliers: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    rule: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    size: float
    ticks: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )


class MarkConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: TextBaseline_T
    blend: Blend_T
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    lineBreak: str
    lineHeight: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    y: float | Literal["height"]
    y2: float | Literal["height"]


class CompositionConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    columns: float
    spacing: float


class ErrorBandConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    band: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    borders: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    extent: ErrorBarExtent_T
    interpolate: Interpolate_T
    tension: float


class ErrorBarConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    extent: ErrorBarExtent_T
    rule: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )
    size: float
    thickness: float
    ticks: (
        bool
        | BarConfigKwds
        | AreaConfigKwds
        | LineConfigKwds
        | MarkConfigKwds
        | RectConfigKwds
        | TickConfigKwds
    )


class HeaderConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    format: str
    formatType: str
    labelAlign: Align_T
    labelAnchor: TitleAnchor_T
    labelAngle: float
    labelBaseline: TextBaseline_T
    labelColor: ColorHex | ColorName_T
    labelExpr: str
    labelFont: str
    labelFontSize: float
    labelFontStyle: str
    labelFontWeight: FontWeight_T
    labelLimit: float
    labelLineHeight: float
    labelOrient: Orient_T
    labelPadding: float
    labels: bool
    orient: Orient_T
    title: None
    titleAlign: Align_T
    titleAnchor: TitleAnchor_T
    titleAngle: float
    titleBaseline: TextBaseline_T
    titleColor: ColorHex | ColorName_T
    titleFont: str
    titleFontSize: float
    titleFontStyle: str
    titleFontWeight: FontWeight_T
    titleLimit: float
    titleLineHeight: float
    titleOrient: Orient_T
    titlePadding: float


class LegendConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    aria: bool
    clipHeight: float
    columnPadding: float
    columns: float
    cornerRadius: float
    description: str
    direction: Orientation_T
    disable: bool
    fillColor: None | ColorHex | ColorName_T
    gradientDirection: Orientation_T
    gradientHorizontalMaxLength: float
    gradientHorizontalMinLength: float
    gradientLabelLimit: float
    gradientLabelOffset: float
    gradientLength: float
    gradientOpacity: float
    gradientStrokeColor: None | ColorHex | ColorName_T
    gradientStrokeWidth: float
    gradientThickness: float
    gradientVerticalMaxLength: float
    gradientVerticalMinLength: float
    gridAlign: LayoutAlign_T
    labelAlign: Align_T
    labelBaseline: TextBaseline_T
    labelColor: None | ColorHex | ColorName_T
    labelFont: str
    labelFontSize: float
    labelFontStyle: str
    labelFontWeight: FontWeight_T
    labelLimit: float
    labelOffset: float
    labelOpacity: float
    labelOverlap: bool | Literal["greedy", "parity"]
    labelPadding: float
    labelSeparation: float
    layout: Map
    legendX: float
    legendY: float
    offset: float
    orient: LegendOrient_T
    padding: float
    rowPadding: float
    strokeColor: None | ColorHex | ColorName_T
    strokeDash: Sequence[float]
    strokeWidth: float
    symbolBaseFillColor: None | ColorHex | ColorName_T
    symbolBaseStrokeColor: None | ColorHex | ColorName_T
    symbolDash: Sequence[float]
    symbolDashOffset: float
    symbolDirection: Orientation_T
    symbolFillColor: None | ColorHex | ColorName_T
    symbolLimit: float
    symbolOffset: float
    symbolOpacity: float
    symbolSize: float
    symbolStrokeColor: None | ColorHex | ColorName_T
    symbolStrokeWidth: float
    symbolType: str
    tickCount: float | TimeIntervalStepKwds | TimeInterval_T
    title: None
    titleAlign: Align_T
    titleAnchor: TitleAnchor_T
    titleBaseline: TextBaseline_T
    titleColor: None | ColorHex | ColorName_T
    titleFont: str
    titleFontSize: float
    titleFontStyle: str
    titleFontWeight: FontWeight_T
    titleLimit: float
    titleLineHeight: float
    titleOpacity: float
    titleOrient: Orient_T
    titlePadding: float
    unselectedOpacity: float
    zindex: float


class LineConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: TextBaseline_T
    blend: Blend_T
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    lineBreak: str
    lineHeight: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    point: bool | OverlayMarkDefKwds | Literal["transparent"]
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    y: float | Literal["height"]
    y2: float | Literal["height"]


class ProjectionConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    center: Sequence[float]
    clipAngle: float
    clipExtent: Sequence[Sequence[float]]
    coefficient: float
    distance: float
    extent: Sequence[Sequence[float]]
    fit: (
        GeoJsonFeatureKwds
        | GeoJsonFeatureCollectionKwds
        | Sequence[GeoJsonFeatureKwds]
        | Sequence[
            GeoJsonFeatureKwds
            | GeoJsonFeatureCollectionKwds
            | Sequence[GeoJsonFeatureKwds]
        ]
    )
    fraction: float
    lobes: float
    parallel: float
    parallels: Sequence[float]
    pointRadius: float
    precision: float
    radius: float
    ratio: float
    reflectX: bool
    reflectY: bool
    rotate: Sequence[float]
    scale: float
    size: Sequence[float]
    spacing: float
    tilt: float
    translate: Sequence[float]
    type: ProjectionType_T


class RangeConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    category: (
        Sequence[ColorHex | ColorName_T]
        | Sequence[str | bool | None | float | Sequence[float]]
        | RangeEnum_T
    )
    diverging: (
        Sequence[ColorHex | ColorName_T]
        | Sequence[str | bool | None | float | Sequence[float]]
        | RangeEnum_T
    )
    heatmap: (
        Sequence[ColorHex | ColorName_T]
        | Sequence[str | bool | None | float | Sequence[float]]
        | RangeEnum_T
    )
    ordinal: (
        Sequence[ColorHex | ColorName_T]
        | Sequence[str | bool | None | float | Sequence[float]]
        | RangeEnum_T
    )
    ramp: (
        Sequence[ColorHex | ColorName_T]
        | Sequence[str | bool | None | float | Sequence[float]]
        | RangeEnum_T
    )
    symbol: Sequence[str]


class ScaleConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    bandPaddingInner: float
    bandPaddingOuter: float
    bandWithNestedOffsetPaddingInner: float
    bandWithNestedOffsetPaddingOuter: float
    barBandPaddingInner: float
    clamp: bool
    continuousPadding: float
    invalid: ScaleInvalidDataConfigKwds
    maxBandSize: float
    maxFontSize: float
    maxOpacity: float
    maxSize: float
    maxStrokeWidth: float
    minBandSize: float
    minFontSize: float
    minOpacity: float
    minSize: float
    minStrokeWidth: float
    offsetBandPaddingInner: float
    offsetBandPaddingOuter: float
    pointPadding: float
    quantileCount: float
    quantizeCount: float
    rectBandPaddingInner: float
    round: bool
    tickBandPaddingInner: float
    useUnaggregatedDomain: bool
    xReverse: bool
    zero: bool


class SelectionConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    interval: IntervalSelectionConfigWithoutTypeKwds
    point: PointSelectionConfigWithoutTypeKwds


class TickConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    bandSize: float
    baseline: TextBaseline_T
    blend: Blend_T
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    lineBreak: str
    lineHeight: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    thickness: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    y: float | Literal["height"]
    y2: float | Literal["height"]


class TitleConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    anchor: TitleAnchor_T
    angle: float
    aria: bool
    baseline: TextBaseline_T
    color: None | ColorHex | ColorName_T
    dx: float
    dy: float
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    frame: str | TitleFrame_T
    limit: float
    lineHeight: float
    offset: float
    orient: TitleOrient_T
    subtitleColor: None | ColorHex | ColorName_T
    subtitleFont: str
    subtitleFontSize: float
    subtitleFontStyle: str
    subtitleFontWeight: FontWeight_T
    subtitleLineHeight: float
    subtitlePadding: float
    zindex: float


class FormatConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    normalizedNumberFormat: str
    normalizedNumberFormatType: str
    numberFormat: str
    numberFormatType: str
    timeFormat: str
    timeFormatType: str


class ViewConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    clip: bool
    continuousHeight: float
    continuousWidth: float
    cornerRadius: float
    cursor: Cursor_T
    discreteHeight: float
    discreteWidth: float
    fill: None | ColorHex | ColorName_T
    fillOpacity: float
    opacity: float
    step: float
    stroke: None | ColorHex | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOpacity: float
    strokeWidth: float


class ScaleInvalidDataConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    angle: Value[float] | Literal["zero-or-min"]
    color: (
        Literal["zero-or-min"]
        | Value[ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T]
    )
    fill: (
        Literal["zero-or-min"]
        | Value[None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T]
    )
    fillOpacity: Value[float] | Literal["zero-or-min"]
    opacity: Value[float] | Literal["zero-or-min"]
    radius: Value[float] | Literal["zero-or-min"]
    shape: Value[str] | Literal["zero-or-min"]
    size: Value[float] | Literal["zero-or-min"]
    stroke: (
        Literal["zero-or-min"]
        | Value[None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T]
    )
    strokeDash: Literal["zero-or-min"] | Value[Sequence[float]]
    strokeOpacity: Value[float] | Literal["zero-or-min"]
    strokeWidth: Value[float] | Literal["zero-or-min"]
    theta: Value[float] | Literal["zero-or-min"]
    x: Literal["zero-or-min"] | Value[float | Literal["width"]]
    xOffset: Value[float] | Literal["zero-or-min"]
    y: Literal["zero-or-min"] | Value[float | Literal["height"]]
    yOffset: Value[float] | Literal["zero-or-min"]


class OverlayMarkDefKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: TextBaseline_T
    blend: Blend_T
    clip: bool
    color: ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    cornerRadius: float
    cornerRadiusBottomLeft: float
    cornerRadiusBottomRight: float
    cornerRadiusTopLeft: float
    cornerRadiusTopRight: float
    cursor: Cursor_T
    description: str
    dir: TextDirection_T
    dx: float
    dy: float
    ellipsis: str
    endAngle: float
    fill: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    fillOpacity: float
    filled: bool
    font: str
    fontSize: float
    fontStyle: str
    fontWeight: FontWeight_T
    height: float
    href: str
    innerRadius: float
    interpolate: Interpolate_T
    invalid: None | MarkInvalidDataMode_T
    limit: float
    lineBreak: str
    lineHeight: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    radius: float
    radius2: float
    radius2Offset: float
    radiusOffset: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradientKwds | RadialGradientKwds | ColorName_T
    strokeCap: StrokeCap_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeJoin: StrokeJoin_T
    strokeMiterLimit: float
    strokeOffset: float
    strokeOpacity: float
    strokeWidth: float
    style: str | Sequence[str]
    tension: float
    text: str | Sequence[str]
    theta: float
    theta2: float
    theta2Offset: float
    thetaOffset: float
    timeUnitBandPosition: float
    timeUnitBandSize: float
    tooltip: str | bool | None | float | TooltipContentKwds
    url: str
    width: float
    x: float | Literal["width"]
    x2: float | Literal["width"]
    x2Offset: float
    xOffset: float
    y: float | Literal["height"]
    y2: float | Literal["height"]
    y2Offset: float
    yOffset: float


class LinearGradientKwds(TypedDict, total=False):
    """Placeholder doc."""

    gradient: Literal["linear"]
    stops: Sequence[GradientStopKwds]
    id: str
    x1: float
    x2: float
    y1: float
    y2: float


class RadialGradientKwds(TypedDict, total=False):
    """Placeholder doc."""

    gradient: Literal["radial"]
    stops: Sequence[GradientStopKwds]
    id: str
    r1: float
    r2: float
    x1: float
    x2: float
    y1: float
    y2: float


class GradientStopKwds(TypedDict, total=False):
    """Placeholder doc."""

    color: ColorHex | ColorName_T
    offset: float


class TooltipContentKwds(TypedDict, total=False):
    """Placeholder doc."""

    content: Literal["encoding", "data"]


class DateTimeKwds(TypedDict, total=False):
    """Placeholder doc."""

    date: float
    day: str | float
    hours: float
    milliseconds: float
    minutes: float
    month: str | float
    quarter: float
    seconds: float
    utc: bool
    year: float


class TimeIntervalStepKwds(TypedDict, total=False):
    """Placeholder doc."""

    interval: TimeInterval_T
    step: float


class IntervalSelectionConfigWithoutTypeKwds(TypedDict, total=False):
    """Placeholder doc."""

    clear: str | bool | MergedStreamKwds | DerivedStreamKwds
    encodings: Sequence[SingleDefUnitChannel_T]
    fields: Sequence[str]
    mark: BrushConfigKwds
    on: str | MergedStreamKwds | DerivedStreamKwds
    resolve: SelectionResolution_T
    translate: str | bool
    zoom: str | bool


class PointSelectionConfigWithoutTypeKwds(TypedDict, total=False):
    """Placeholder doc."""

    clear: str | bool | MergedStreamKwds | DerivedStreamKwds
    encodings: Sequence[SingleDefUnitChannel_T]
    fields: Sequence[str]
    nearest: bool
    on: str | MergedStreamKwds | DerivedStreamKwds
    resolve: SelectionResolution_T
    toggle: str | bool


class FeatureGeometryGeoJsonPropertiesKwds(TypedDict, total=False):
    """Placeholder doc."""

    geometry: (
        PointKwds
        | PolygonKwds
        | LineStringKwds
        | MultiPointKwds
        | MultiPolygonKwds
        | MultiLineStringKwds
        | GeometryCollectionKwds
    )
    properties: None
    type: Literal["Feature"]
    bbox: Sequence[float]
    id: str | float


class GeoJsonFeatureKwds(TypedDict, total=False):
    """Placeholder doc."""

    geometry: (
        PointKwds
        | PolygonKwds
        | LineStringKwds
        | MultiPointKwds
        | MultiPolygonKwds
        | MultiLineStringKwds
        | GeometryCollectionKwds
    )
    properties: None
    type: Literal["Feature"]
    bbox: Sequence[float]
    id: str | float


class GeoJsonFeatureCollectionKwds(TypedDict, total=False):
    """Placeholder doc."""

    features: Sequence[FeatureGeometryGeoJsonPropertiesKwds]
    type: Literal["FeatureCollection"]
    bbox: Sequence[float]


class GeometryCollectionKwds(TypedDict, total=False):
    """Placeholder doc."""

    geometries: Sequence[
        PointKwds
        | PolygonKwds
        | LineStringKwds
        | MultiPointKwds
        | MultiPolygonKwds
        | MultiLineStringKwds
        | GeometryCollectionKwds
    ]
    type: Literal["GeometryCollection"]
    bbox: Sequence[float]


class PointKwds(TypedDict, total=False):
    """Placeholder doc."""

    coordinates: Sequence[float]
    type: Literal["Point"]
    bbox: Sequence[float]


class PolygonKwds(TypedDict, total=False):
    """Placeholder doc."""

    coordinates: Sequence[Sequence[Sequence[float]]]
    type: Literal["Polygon"]
    bbox: Sequence[float]


class LineStringKwds(TypedDict, total=False):
    """Placeholder doc."""

    coordinates: Sequence[Sequence[float]]
    type: Literal["LineString"]
    bbox: Sequence[float]


class MultiPointKwds(TypedDict, total=False):
    """Placeholder doc."""

    coordinates: Sequence[Sequence[float]]
    type: Literal["MultiPoint"]
    bbox: Sequence[float]


class MultiPolygonKwds(TypedDict, total=False):
    """Placeholder doc."""

    coordinates: Sequence[Sequence[Sequence[Sequence[float]]]]
    type: Literal["MultiPolygon"]
    bbox: Sequence[float]


class MultiLineStringKwds(TypedDict, total=False):
    """Placeholder doc."""

    coordinates: Sequence[Sequence[Sequence[float]]]
    type: Literal["MultiLineString"]
    bbox: Sequence[float]


class BrushConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    cursor: Cursor_T
    fill: ColorHex | ColorName_T
    fillOpacity: float
    stroke: ColorHex | ColorName_T
    strokeDash: Sequence[float]
    strokeDashOffset: float
    strokeOpacity: float
    strokeWidth: float


class MergedStreamKwds(TypedDict, total=False):
    """Placeholder doc."""

    merge: Sequence[MergedStreamKwds | DerivedStreamKwds]
    between: Sequence[MergedStreamKwds | DerivedStreamKwds]
    consume: bool
    debounce: float
    filter: str | Sequence[str]
    markname: str
    marktype: MarkType_T
    throttle: float


class DerivedStreamKwds(TypedDict, total=False):
    """Placeholder doc."""

    stream: MergedStreamKwds | DerivedStreamKwds
    between: Sequence[MergedStreamKwds | DerivedStreamKwds]
    consume: bool
    debounce: float
    filter: str | Sequence[str]
    markname: str
    marktype: MarkType_T
    throttle: float


# TODO: Non-`TypedDict` args


class ThemeConfig(TypedDict, total=False):
    """Placeholder doc."""

    arc: RectConfigKwds
    area: AreaConfigKwds
    aria: Any  # TODO
    autosize: Any  # TODO
    axis: AxisConfigKwds
    axisBand: AxisConfigKwds
    axisBottom: AxisConfigKwds
    axisDiscrete: AxisConfigKwds
    axisLeft: AxisConfigKwds
    axisPoint: AxisConfigKwds
    axisQuantitative: AxisConfigKwds
    axisRight: AxisConfigKwds
    axisTemporal: AxisConfigKwds
    axisTop: AxisConfigKwds
    axisX: AxisConfigKwds
    axisXBand: AxisConfigKwds
    axisXDiscrete: AxisConfigKwds
    axisXPoint: AxisConfigKwds
    axisXQuantitative: AxisConfigKwds
    axisXTemporal: AxisConfigKwds
    axisY: AxisConfigKwds
    axisYBand: AxisConfigKwds
    axisYDiscrete: AxisConfigKwds
    axisYPoint: AxisConfigKwds
    axisYQuantitative: AxisConfigKwds
    axisYTemporal: AxisConfigKwds
    background: Any  # TODO
    bar: BarConfigKwds
    boxplot: BoxPlotConfigKwds
    circle: MarkConfigKwds
    concat: CompositionConfigKwds
    countTitle: Any  # TODO
    customFormatTypes: Any  # TODO
    errorband: ErrorBandConfigKwds
    errorbar: ErrorBarConfigKwds
    facet: CompositionConfigKwds
    fieldTitle: Any  # TODO
    font: Any  # TODO
    geoshape: MarkConfigKwds
    header: HeaderConfigKwds
    headerColumn: HeaderConfigKwds
    headerFacet: HeaderConfigKwds
    headerRow: HeaderConfigKwds
    image: RectConfigKwds
    legend: LegendConfigKwds
    line: LineConfigKwds
    lineBreak: Any  # TODO
    locale: Any  # TODO
    mark: MarkConfigKwds
    normalizedNumberFormat: Any  # TODO
    normalizedNumberFormatType: Any  # TODO
    numberFormat: Any  # TODO
    numberFormatType: Any  # TODO
    padding: Any  # TODO
    params: Any  # TODO
    point: MarkConfigKwds
    projection: ProjectionConfigKwds
    range: RangeConfigKwds
    rect: RectConfigKwds
    rule: MarkConfigKwds
    scale: ScaleConfigKwds
    selection: SelectionConfigKwds
    square: MarkConfigKwds
    style: Any  # TODO
    text: MarkConfigKwds
    tick: TickConfigKwds
    timeFormat: Any  # TODO
    timeFormatType: Any  # TODO
    title: TitleConfigKwds
    tooltipFormat: FormatConfigKwds
    trail: LineConfigKwds
    view: ViewConfigKwds
