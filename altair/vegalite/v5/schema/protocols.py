# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import Undefined
from typing import Any, Protocol

class AllSortStringCallable(Protocol):
    def __call__(self, **kwds):
        return None

class ArgmaxDefCallable(Protocol):
    def __call__(self, argmax=Undefined, **kwds):
        return None

class ArgminDefCallable(Protocol):
    def __call__(self, argmin=Undefined, **kwds):
        return None

class AxisCallable(Protocol):
    def __call__(self, aria=Undefined, bandPosition=Undefined, description=Undefined, domain=Undefined, domainCap=Undefined, domainColor=Undefined, domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined, domainWidth=Undefined, format=Undefined, formatType=Undefined, grid=Undefined, gridCap=Undefined, gridColor=Undefined, gridDash=Undefined, gridDashOffset=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, style=Undefined, tickBand=Undefined, tickCap=Undefined, tickColor=Undefined, tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined, tickExtra=Undefined, tickMinStep=Undefined, tickOffset=Undefined, tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, translate=Undefined, values=Undefined, zindex=Undefined, **kwds):
        return None

class BinParamsCallable(Protocol):
    def __call__(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds):
        return None

class BooleanCallable(Protocol):
    def __call__(self, arg: bool):
        return None

class ConditionalMarkPropFieldOrDatumDefCallable(Protocol):
    def __call__(self, **kwds):
        return None

class ConditionalMarkPropFieldOrDatumDefTypeForShapeCallable(Protocol):
    def __call__(self, **kwds):
        return None

class ConditionalStringFieldDefCallable(Protocol):
    def __call__(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, format=Undefined, formatType=Undefined, param=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        return None

class ConditionalValueDefGradientstringnullExprRefCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class ConditionalValueDefTextExprRefCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class ConditionalValueDefnumberArrayExprRefCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class ConditionalValueDefnumberCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class ConditionalValueDefnumberExprRefCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class ConditionalValueDefstringExprRefCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class ConditionalValueDefstringnullExprRefCallable(Protocol):
    def __call__(self, empty=Undefined, param=Undefined, test=Undefined, value=Undefined, **kwds):
        return None

class DictCallable(Protocol):
    def __call__(self, arg: dict):
        return None

class EncodingSortFieldCallable(Protocol):
    def __call__(self, field=Undefined, op=Undefined, order=Undefined, **kwds):
        return None

class FieldNameCallable(Protocol):
    def __call__(self, arg: str):
        return None

class FloatCallable(Protocol):
    def __call__(self, arg: float):
        return None

class HeaderCallable(Protocol):
    def __call__(self, format=Undefined, formatType=Undefined, labelAlign=Undefined, labelAnchor=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOrient=Undefined, labelPadding=Undefined, labels=Undefined, orient=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOrient=Undefined, titlePadding=Undefined, **kwds):
        return None

class ImputeParamsCallable(Protocol):
    def __call__(self, frame=Undefined, keyvals=Undefined, method=Undefined, value=Undefined, **kwds):
        return None

class LayoutAlignCallable(Protocol):
    def __call__(self, arg: str):
        return None

class LegendCallable(Protocol):
    def __call__(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds):
        return None

class ListCallable(Protocol):
    def __call__(self, arg: list):
        return None

class NonArgAggregateOpCallable(Protocol):
    def __call__(self, arg: str):
        return None

class NoneCallable(Protocol):
    def __call__(self, arg: type(None)):
        return None

class RepeatRefCallable(Protocol):
    def __call__(self, repeat=Undefined, **kwds):
        return None

class RowColLayoutAlignCallable(Protocol):
    def __call__(self, column=Undefined, row=Undefined, **kwds):
        return None

class RowColbooleanCallable(Protocol):
    def __call__(self, column=Undefined, row=Undefined, **kwds):
        return None

class RowColnumberCallable(Protocol):
    def __call__(self, column=Undefined, row=Undefined, **kwds):
        return None

class ScaleCallable(Protocol):
    def __call__(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds):
        return None

class SortArrayCallable(Protocol):
    def __call__(self, **kwds):
        return None

class SortByEncodingCallable(Protocol):
    def __call__(self, encoding=Undefined, order=Undefined, **kwds):
        return None

class SortOrderCallable(Protocol):
    def __call__(self, arg: str):
        return None

class StackOffsetCallable(Protocol):
    def __call__(self, arg: str):
        return None

class StandardTypeCallable(Protocol):
    def __call__(self, arg: str):
        return None

class StringCallable(Protocol):
    def __call__(self, arg: str):
        return None

class TextCallable(Protocol):
    def __call__(self, **kwds):
        return None

class TimeUnitCallable(Protocol):
    def __call__(self, **kwds):
        return None

class TimeUnitParamsCallable(Protocol):
    def __call__(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds):
        return None

class TypeCallable(Protocol):
    def __call__(self, arg: str):
        return None

class TypeForShapeCallable(Protocol):
    def __call__(self, arg: str):
        return None
