# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, Sequence, TypedDict

# ruff: noqa: F405
if TYPE_CHECKING:
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
    baseline: str | Baseline_T
    binSpacing: float
    blend: Blend_T
    color: ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    fill: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    stroke: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    tooltip: str | bool | None | float | TooltipContent
    url: str
    width: float
    x: str | float
    x2: str | float
    y: str | float
    y2: str | float


class AreaConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: str | Baseline_T
    blend: Blend_T
    color: ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    fill: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    line: bool | OverlayMarkDef
    lineBreak: str
    lineHeight: float
    opacity: float
    order: bool | None
    orient: Orientation_T
    outerRadius: float
    padAngle: float
    point: str | bool | OverlayMarkDef
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    tooltip: str | bool | None | float | TooltipContent
    url: str
    width: float
    x: str | float
    x2: str | float
    y: str | float
    y2: str | float


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
    labelBaseline: str | Baseline_T
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
    labelOverlap: str | bool
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
    tickCount: float | TimeIntervalStep | TimeInterval_T
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
    titleBaseline: str | Baseline_T
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
    values: Sequence[str] | Sequence[bool] | Sequence[float] | Sequence[DateTime]
    zindex: float


class BarConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    baseline: str | Baseline_T
    binSpacing: float
    blend: Blend_T
    color: ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    fill: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    stroke: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    tooltip: str | bool | None | float | TooltipContent
    url: str
    width: float
    x: str | float
    x2: str | float
    y: str | float
    y2: str | float


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
    extent: str | float
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
    baseline: str | Baseline_T
    blend: Blend_T
    color: ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    fill: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    stroke: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    tooltip: str | bool | None | float | TooltipContent
    url: str
    width: float
    x: str | float
    x2: str | float
    y: str | float
    y2: str | float


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
    labelBaseline: str | Baseline_T
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
    titleBaseline: str | Baseline_T
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
    labelBaseline: str | Baseline_T
    labelColor: None | ColorHex | ColorName_T
    labelFont: str
    labelFontSize: float
    labelFontStyle: str
    labelFontWeight: FontWeight_T
    labelLimit: float
    labelOffset: float
    labelOpacity: float
    labelOverlap: str | bool
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
    tickCount: float | TimeIntervalStep | TimeInterval_T
    title: None
    titleAlign: Align_T
    titleAnchor: TitleAnchor_T
    titleBaseline: str | Baseline_T
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
    baseline: str | Baseline_T
    blend: Blend_T
    color: ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    fill: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    point: str | bool | OverlayMarkDef
    radius: float
    radius2: float
    shape: str
    size: float
    smooth: bool
    startAngle: float
    stroke: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    tooltip: str | bool | None | float | TooltipContent
    url: str
    width: float
    x: str | float
    x2: str | float
    y: str | float
    y2: str | float


class ProjectionConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    center: Sequence[float]
    clipAngle: float
    clipExtent: Sequence[Sequence[float]]
    coefficient: float
    distance: float
    extent: Sequence[Sequence[float]]
    fit: (
        GeoJsonFeature
        | GeoJsonFeatureCollection
        | Sequence[GeoJsonFeature]
        | Sequence[GeoJsonFeature | GeoJsonFeatureCollection | Sequence[GeoJsonFeature]]
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

    interval: IntervalSelectionConfigWithoutType
    point: PointSelectionConfigWithoutType


class TickConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    angle: float
    aria: bool
    ariaRole: str
    ariaRoleDescription: str
    aspect: bool
    bandSize: float
    baseline: str | Baseline_T
    blend: Blend_T
    color: ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    fill: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    stroke: None | ColorHex | LinearGradient | RadialGradient | ColorName_T
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
    tooltip: str | bool | None | float | TooltipContent
    url: str
    width: float
    x: str | float
    x2: str | float
    y: str | float
    y2: str | float


class TitleConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    align: Align_T
    anchor: TitleAnchor_T
    angle: float
    aria: bool
    baseline: str | Baseline_T
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


# TODO: Non-`TypedDict` arg


class ScaleInvalidDataConfigKwds(TypedDict, total=False):
    """Placeholder doc."""

    angle: str | Value[float]
    color: str | Value[ColorHex | LinearGradient | RadialGradient | ColorName_T]
    fill: str | Value[None | ColorHex | LinearGradient | RadialGradient | ColorName_T]
    fillOpacity: str | Value[float]
    opacity: str | Value[float]
    radius: str | Value[float]
    shape: str | Value[str]
    size: str | Value[float]
    stroke: str | Value[None | ColorHex | LinearGradient | RadialGradient | ColorName_T]
    strokeDash: str | Value[Sequence[float]]
    strokeOpacity: str | Value[float]
    strokeWidth: str | Value[float]
    theta: str | Value[float]
    x: str | Value[str | float]
    xOffset: str | Value[float]
    y: str | Value[str | float]
    yOffset: str | Value[float]


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
