# The contents of this file are automatically generated
# at time 2018-02-12 13:38:47

from altair.utils.schemapi import SchemaBase, Undefined

import os
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, 'vega-lite-schema.json')) as f:
        return json.load(f)


class Root(SchemaBase):
    """Root schema wrapper"""
    __schema = load_schema()

    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)
    


class Aggregate(SchemaBase):
    """Aggregate schema wrapper"""
    __schema = {'$ref': '#/definitions/Aggregate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Aggregate, self).__init__(*args)
    


class AggregateOp(SchemaBase):
    """AggregateOp schema wrapper"""
    __schema = {'$ref': '#/definitions/AggregateOp', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(AggregateOp, self).__init__(*args)
    


class AggregateTransform(SchemaBase):
    """AggregateTransform schema wrapper"""
    __schema = {'$ref': '#/definitions/AggregateTransform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, aggregate=Undefined, groupby=Undefined, **kwds):
        super(AggregateTransform, self).__init__(aggregate=aggregate, groupby=groupby, **kwds)
    


class AggregatedFieldDef(SchemaBase):
    """AggregatedFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/AggregatedFieldDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, field=Undefined, op=Undefined, **kwds):
        super(AggregatedFieldDef, self).__init__(field=field, op=op, **kwds)
    


class Anchor(SchemaBase):
    """Anchor schema wrapper"""
    __schema = {'$ref': '#/definitions/Anchor', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Anchor, self).__init__(*args)
    


class AnyMark(SchemaBase):
    """AnyMark schema wrapper"""
    __schema = {'$ref': '#/definitions/AnyMark', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(AnyMark, self).__init__(*args, **kwds)
    


class AutoSizeParams(SchemaBase):
    """AutoSizeParams schema wrapper"""
    __schema = {'$ref': '#/definitions/AutoSizeParams', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, contains=Undefined, resize=Undefined, type=Undefined, **kwds):
        super(AutoSizeParams, self).__init__(contains=contains, resize=resize, type=type, **kwds)
    


class AutosizeType(SchemaBase):
    """AutosizeType schema wrapper"""
    __schema = {'$ref': '#/definitions/AutosizeType', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(AutosizeType, self).__init__(*args)
    


class Axis(SchemaBase):
    """Axis schema wrapper"""
    __schema = {'$ref': '#/definitions/Axis', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, domain=Undefined, format=Undefined, grid=Undefined, labelAngle=Undefined, labelBound=Undefined, labelFlush=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, tickCount=Undefined, tickSize=Undefined, ticks=Undefined, title=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(Axis, self).__init__(domain=domain, format=format, grid=grid, labelAngle=labelAngle, labelBound=labelBound, labelFlush=labelFlush, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, offset=offset, orient=orient, position=position, tickCount=tickCount, tickSize=tickSize, ticks=ticks, title=title, titleMaxLength=titleMaxLength, titlePadding=titlePadding, values=values, zindex=zindex, **kwds)
    


class AxisConfig(SchemaBase):
    """AxisConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/AxisConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined, domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, shortTimeLabels=Undefined, tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, **kwds):
        super(AxisConfig, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor, domainWidth=domainWidth, grid=grid, gridColor=gridColor, gridDash=gridDash, gridOpacity=gridOpacity, gridWidth=gridWidth, labelAngle=labelAngle, labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, shortTimeLabels=shortTimeLabels, tickColor=tickColor, tickRound=tickRound, tickSize=tickSize, tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign, titleAngle=titleAngle, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titleMaxLength=titleMaxLength, titlePadding=titlePadding, titleX=titleX, titleY=titleY, **kwds)
    


class AxisOrient(SchemaBase):
    """AxisOrient schema wrapper"""
    __schema = {'$ref': '#/definitions/AxisOrient', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(AxisOrient, self).__init__(*args)
    


class AxisResolveMap(SchemaBase):
    """AxisResolveMap schema wrapper"""
    __schema = {'$ref': '#/definitions/AxisResolveMap', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, x=Undefined, y=Undefined, **kwds):
        super(AxisResolveMap, self).__init__(x=x, y=y, **kwds)
    


class BarConfig(SchemaBase):
    """BarConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/BarConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined, color=Undefined, continuousBandSize=Undefined, cursor=Undefined, discreteBandSize=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(BarConfig, self).__init__(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, color=color, continuousBandSize=continuousBandSize, cursor=cursor, discreteBandSize=discreteBandSize, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class BasicType(SchemaBase):
    """BasicType schema wrapper"""
    __schema = {'$ref': '#/definitions/BasicType', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(BasicType, self).__init__(*args)
    


class BinParams(SchemaBase):
    """BinParams schema wrapper"""
    __schema = {'$ref': '#/definitions/BinParams', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, base=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(BinParams, self).__init__(base=base, divide=divide, extent=extent, maxbins=maxbins, minstep=minstep, nice=nice, step=step, steps=steps, **kwds)
    


class BinTransform(SchemaBase):
    """BinTransform schema wrapper"""
    __schema = {'$ref': '#/definitions/BinTransform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, bin=Undefined, field=Undefined, **kwds):
        super(BinTransform, self).__init__(bin=bin, field=field, **kwds)
    


class BrushConfig(SchemaBase):
    """BrushConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/BrushConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, fill=Undefined, fillOpacity=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, **kwds):
        super(BrushConfig, self).__init__(fill=fill, fillOpacity=fillOpacity, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, **kwds)
    


class CalculateTransform(SchemaBase):
    """CalculateTransform schema wrapper"""
    __schema = {'$ref': '#/definitions/CalculateTransform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, calculate=Undefined, **kwds):
        super(CalculateTransform, self).__init__(calculate=calculate, **kwds)
    


class CompositeUnitSpec(SchemaBase):
    """CompositeUnitSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/CompositeUnitSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(CompositeUnitSpec, self).__init__(mark=mark, data=data, description=description, encoding=encoding, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class ConditionalFieldDef(SchemaBase):
    """ConditionalFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/Conditional<FieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(ConditionalFieldDef, self).__init__(*args, **kwds)
    


class ConditionalMarkPropFieldDef(SchemaBase):
    """ConditionalMarkPropFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/Conditional<MarkPropFieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDef, self).__init__(*args, **kwds)
    


class ConditionalTextFieldDef(SchemaBase):
    """ConditionalTextFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/Conditional<TextFieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(ConditionalTextFieldDef, self).__init__(*args, **kwds)
    


class ConditionalValueDef(SchemaBase):
    """ConditionalValueDef schema wrapper"""
    __schema = {'$ref': '#/definitions/Conditional<ValueDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(ConditionalValueDef, self).__init__(*args, **kwds)
    


class ConditionalPredicateFieldDef(SchemaBase):
    """ConditionalPredicateFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalPredicate<FieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, **kwds)
    


class ConditionalPredicateMarkPropFieldDef(SchemaBase):
    """ConditionalPredicateMarkPropFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateMarkPropFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, **kwds)
    


class ConditionalPredicateTextFieldDef(SchemaBase):
    """ConditionalPredicateTextFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalPredicate<TextFieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateTextFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, format=format, timeUnit=timeUnit, **kwds)
    


class ConditionalPredicateValueDef(SchemaBase):
    """ConditionalPredicateValueDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDef, self).__init__(test=test, value=value, **kwds)
    


class ConditionalSelectionFieldDef(SchemaBase):
    """ConditionalSelectionFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalSelection<FieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, **kwds)
    


class ConditionalSelectionMarkPropFieldDef(SchemaBase):
    """ConditionalSelectionMarkPropFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionMarkPropFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, **kwds)
    


class ConditionalSelectionTextFieldDef(SchemaBase):
    """ConditionalSelectionTextFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalSelection<TextFieldDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionTextFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, format=format, timeUnit=timeUnit, **kwds)
    


class ConditionalSelectionValueDef(SchemaBase):
    """ConditionalSelectionValueDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionValueDef, self).__init__(selection=selection, value=value, **kwds)
    


class Config(SchemaBase):
    """Config schema wrapper"""
    __schema = {'$ref': '#/definitions/Config', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, area=Undefined, autosize=Undefined, axis=Undefined, axisBand=Undefined, axisBottom=Undefined, axisLeft=Undefined, axisRight=Undefined, axisTop=Undefined, axisX=Undefined, axisY=Undefined, background=Undefined, bar=Undefined, circle=Undefined, countTitle=Undefined, fieldTitle=Undefined, geoshape=Undefined, invalidValues=Undefined, legend=Undefined, line=Undefined, mark=Undefined, numberFormat=Undefined, padding=Undefined, point=Undefined, projection=Undefined, range=Undefined, rect=Undefined, rule=Undefined, scale=Undefined, selection=Undefined, square=Undefined, stack=Undefined, style=Undefined, text=Undefined, tick=Undefined, timeFormat=Undefined, title=Undefined, view=Undefined, **kwds):
        super(Config, self).__init__(area=area, autosize=autosize, axis=axis, axisBand=axisBand, axisBottom=axisBottom, axisLeft=axisLeft, axisRight=axisRight, axisTop=axisTop, axisX=axisX, axisY=axisY, background=background, bar=bar, circle=circle, countTitle=countTitle, fieldTitle=fieldTitle, geoshape=geoshape, invalidValues=invalidValues, legend=legend, line=line, mark=mark, numberFormat=numberFormat, padding=padding, point=point, projection=projection, range=range, rect=rect, rule=rule, scale=scale, selection=selection, square=square, stack=stack, style=style, text=text, tick=tick, timeFormat=timeFormat, title=title, view=view, **kwds)
    


class CsvDataFormat(SchemaBase):
    """CsvDataFormat schema wrapper"""
    __schema = {'$ref': '#/definitions/CsvDataFormat', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, parse=Undefined, type=Undefined, **kwds):
        super(CsvDataFormat, self).__init__(parse=parse, type=type, **kwds)
    


class Data(SchemaBase):
    """Data schema wrapper"""
    __schema = {'$ref': '#/definitions/Data', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(Data, self).__init__(*args, **kwds)
    


class DataFormat(SchemaBase):
    """DataFormat schema wrapper"""
    __schema = {'$ref': '#/definitions/DataFormat', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(DataFormat, self).__init__(*args, **kwds)
    


class DateTime(SchemaBase):
    """DateTime schema wrapper"""
    __schema = {'$ref': '#/definitions/DateTime', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, date=Undefined, day=Undefined, hours=Undefined, milliseconds=Undefined, minutes=Undefined, month=Undefined, quarter=Undefined, seconds=Undefined, utc=Undefined, year=Undefined, **kwds):
        super(DateTime, self).__init__(date=date, day=day, hours=hours, milliseconds=milliseconds, minutes=minutes, month=month, quarter=quarter, seconds=seconds, utc=utc, year=year, **kwds)
    


class Day(SchemaBase):
    """Day schema wrapper"""
    __schema = {'$ref': '#/definitions/Day', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Day, self).__init__(*args)
    


class Encoding(SchemaBase):
    """Encoding schema wrapper"""
    __schema = {'$ref': '#/definitions/Encoding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, color=Undefined, detail=Undefined, href=Undefined, opacity=Undefined, order=Undefined, shape=Undefined, size=Undefined, text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(Encoding, self).__init__(color=color, detail=detail, href=href, opacity=opacity, order=order, shape=shape, size=size, text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2, **kwds)
    


class EncodingWithFacet(SchemaBase):
    """EncodingWithFacet schema wrapper"""
    __schema = {'$ref': '#/definitions/EncodingWithFacet', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, color=Undefined, column=Undefined, detail=Undefined, href=Undefined, opacity=Undefined, order=Undefined, row=Undefined, shape=Undefined, size=Undefined, text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(EncodingWithFacet, self).__init__(color=color, column=column, detail=detail, href=href, opacity=opacity, order=order, row=row, shape=shape, size=size, text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2, **kwds)
    


class FacetFieldDef(SchemaBase):
    """FacetFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/FacetFieldDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, header=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(FacetFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, header=header, sort=sort, timeUnit=timeUnit, **kwds)
    


class FacetMapping(SchemaBase):
    """FacetMapping schema wrapper"""
    __schema = {'$ref': '#/definitions/FacetMapping', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(FacetMapping, self).__init__(column=column, row=row, **kwds)
    


class FieldDef(SchemaBase):
    """FieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/FieldDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, **kwds)
    


class FieldDefWithCondition(SchemaBase):
    """FieldDefWithCondition schema wrapper"""
    __schema = {'$ref': '#/definitions/FieldDefWithCondition', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, timeUnit=timeUnit, **kwds)
    


class MarkPropFieldDefWithCondition(SchemaBase):
    """MarkPropFieldDefWithCondition schema wrapper"""
    __schema = {'$ref': '#/definitions/MarkPropFieldDefWithCondition', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(MarkPropFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, **kwds)
    


class TextFieldDefWithCondition(SchemaBase):
    """TextFieldDefWithCondition schema wrapper"""
    __schema = {'$ref': '#/definitions/TextFieldDefWithCondition', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(TextFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, format=format, timeUnit=timeUnit, **kwds)
    


class FieldEqualPredicate(SchemaBase):
    """FieldEqualPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/FieldEqualPredicate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, equal=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldEqualPredicate, self).__init__(equal=equal, field=field, timeUnit=timeUnit, **kwds)
    


class FieldOneOfPredicate(SchemaBase):
    """FieldOneOfPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/FieldOneOfPredicate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, field=Undefined, oneOf=Undefined, timeUnit=Undefined, **kwds):
        super(FieldOneOfPredicate, self).__init__(field=field, oneOf=oneOf, timeUnit=timeUnit, **kwds)
    


class FieldRangePredicate(SchemaBase):
    """FieldRangePredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/FieldRangePredicate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, field=Undefined, range=Undefined, timeUnit=Undefined, **kwds):
        super(FieldRangePredicate, self).__init__(field=field, range=range, timeUnit=timeUnit, **kwds)
    


class FilterTransform(SchemaBase):
    """FilterTransform schema wrapper"""
    __schema = {'$ref': '#/definitions/FilterTransform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, filter=Undefined, **kwds):
        super(FilterTransform, self).__init__(filter=filter, **kwds)
    


class FontStyle(SchemaBase):
    """FontStyle schema wrapper"""
    __schema = {'$ref': '#/definitions/FontStyle', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(FontStyle, self).__init__(*args)
    


class FontWeight(SchemaBase):
    """FontWeight schema wrapper"""
    __schema = {'$ref': '#/definitions/FontWeight', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(FontWeight, self).__init__(*args)
    


class FontWeightNumber(SchemaBase):
    """FontWeightNumber schema wrapper"""
    __schema = {'$ref': '#/definitions/FontWeightNumber', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(FontWeightNumber, self).__init__(*args)
    


class FacetSpec(SchemaBase):
    """FacetSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/FacetSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, facet=Undefined, spec=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class HConcatSpec(SchemaBase):
    """HConcatSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/HConcatSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, hconcat=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(HConcatSpec, self).__init__(hconcat=hconcat, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class LayerSpec(SchemaBase):
    """LayerSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/LayerSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, layer=Undefined, data=Undefined, description=Undefined, height=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(LayerSpec, self).__init__(layer=layer, data=data, description=description, height=height, name=name, resolve=resolve, title=title, transform=transform, width=width, **kwds)
    


class RepeatSpec(SchemaBase):
    """RepeatSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/RepeatSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, repeat=Undefined, spec=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(RepeatSpec, self).__init__(repeat=repeat, spec=spec, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class Spec(SchemaBase):
    """Spec schema wrapper"""
    __schema = {'$ref': '#/definitions/Spec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(Spec, self).__init__(*args, **kwds)
    


class CompositeUnitSpecAlias(SchemaBase):
    """CompositeUnitSpecAlias schema wrapper"""
    __schema = {'$ref': '#/definitions/CompositeUnitSpecAlias', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(CompositeUnitSpecAlias, self).__init__(mark=mark, data=data, description=description, encoding=encoding, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class FacetedCompositeUnitSpecAlias(SchemaBase):
    """FacetedCompositeUnitSpecAlias schema wrapper"""
    __schema = {'$ref': '#/definitions/FacetedCompositeUnitSpecAlias', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(FacetedCompositeUnitSpecAlias, self).__init__(mark=mark, data=data, description=description, encoding=encoding, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class VConcatSpec(SchemaBase):
    """VConcatSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/VConcatSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, vconcat=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(VConcatSpec, self).__init__(vconcat=vconcat, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class GeoType(SchemaBase):
    """GeoType schema wrapper"""
    __schema = {'$ref': '#/definitions/GeoType', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(GeoType, self).__init__(*args)
    


class Header(SchemaBase):
    """Header schema wrapper"""
    __schema = {'$ref': '#/definitions/Header', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, format=Undefined, labelAngle=Undefined, title=Undefined, **kwds):
        super(Header, self).__init__(format=format, labelAngle=labelAngle, title=title, **kwds)
    


class HorizontalAlign(SchemaBase):
    """HorizontalAlign schema wrapper"""
    __schema = {'$ref': '#/definitions/HorizontalAlign', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(HorizontalAlign, self).__init__(*args)
    


class InlineData(SchemaBase):
    """InlineData schema wrapper"""
    __schema = {'$ref': '#/definitions/InlineData', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, values=Undefined, format=Undefined, **kwds):
        super(InlineData, self).__init__(values=values, format=format, **kwds)
    


class Interpolate(SchemaBase):
    """Interpolate schema wrapper"""
    __schema = {'$ref': '#/definitions/Interpolate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Interpolate, self).__init__(*args)
    


class IntervalSelection(SchemaBase):
    """IntervalSelection schema wrapper"""
    __schema = {'$ref': '#/definitions/IntervalSelection', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined, **kwds):
        super(IntervalSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings, fields=fields, mark=mark, on=on, resolve=resolve, translate=translate, zoom=zoom, **kwds)
    


class IntervalSelectionConfig(SchemaBase):
    """IntervalSelectionConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/IntervalSelectionConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined, **kwds):
        super(IntervalSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings, fields=fields, mark=mark, on=on, resolve=resolve, translate=translate, zoom=zoom, **kwds)
    


class JsonDataFormat(SchemaBase):
    """JsonDataFormat schema wrapper"""
    __schema = {'$ref': '#/definitions/JsonDataFormat', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, parse=Undefined, property=Undefined, type=Undefined, **kwds):
        super(JsonDataFormat, self).__init__(parse=parse, property=property, type=type, **kwds)
    


class Legend(SchemaBase):
    """Legend schema wrapper"""
    __schema = {'$ref': '#/definitions/Legend', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, entryPadding=Undefined, format=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, tickCount=Undefined, title=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(Legend, self).__init__(entryPadding=entryPadding, format=format, offset=offset, orient=orient, padding=padding, tickCount=tickCount, title=title, type=type, values=values, zindex=zindex, **kwds)
    


class LegendConfig(SchemaBase):
    """LegendConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/LegendConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, cornerRadius=Undefined, entryPadding=Undefined, fillColor=Undefined, gradientHeight=Undefined, gradientLabelBaseline=Undefined, gradientLabelLimit=Undefined, gradientLabelOffset=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientWidth=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOffset=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, shortTimeLabels=Undefined, strokeColor=Undefined, strokeDash=Undefined, strokeWidth=Undefined, symbolColor=Undefined, symbolSize=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, titleAlign=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titlePadding=Undefined, **kwds):
        super(LegendConfig, self).__init__(cornerRadius=cornerRadius, entryPadding=entryPadding, fillColor=fillColor, gradientHeight=gradientHeight, gradientLabelBaseline=gradientLabelBaseline, gradientLabelLimit=gradientLabelLimit, gradientLabelOffset=gradientLabelOffset, gradientStrokeColor=gradientStrokeColor, gradientStrokeWidth=gradientStrokeWidth, gradientWidth=gradientWidth, labelAlign=labelAlign, labelBaseline=labelBaseline, labelColor=labelColor, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOffset=labelOffset, offset=offset, orient=orient, padding=padding, shortTimeLabels=shortTimeLabels, strokeColor=strokeColor, strokeDash=strokeDash, strokeWidth=strokeWidth, symbolColor=symbolColor, symbolSize=symbolSize, symbolStrokeWidth=symbolStrokeWidth, symbolType=symbolType, titleAlign=titleAlign, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titlePadding=titlePadding, **kwds)
    


class LegendOrient(SchemaBase):
    """LegendOrient schema wrapper"""
    __schema = {'$ref': '#/definitions/LegendOrient', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(LegendOrient, self).__init__(*args)
    


class LegendResolveMap(SchemaBase):
    """LegendResolveMap schema wrapper"""
    __schema = {'$ref': '#/definitions/LegendResolveMap', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, color=Undefined, opacity=Undefined, shape=Undefined, size=Undefined, **kwds):
        super(LegendResolveMap, self).__init__(color=color, opacity=opacity, shape=shape, size=size, **kwds)
    


class LocalMultiTimeUnit(SchemaBase):
    """LocalMultiTimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/LocalMultiTimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(LocalMultiTimeUnit, self).__init__(*args)
    


class LocalSingleTimeUnit(SchemaBase):
    """LocalSingleTimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/LocalSingleTimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(LocalSingleTimeUnit, self).__init__(*args)
    


class LogicalAndPredicate(SchemaBase):
    """LogicalAndPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/LogicalAnd<Predicate>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(LogicalAndPredicate, self).__init__(**kwds)
    


class SelectionAnd(SchemaBase):
    """SelectionAnd schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionAnd', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(SelectionAnd, self).__init__(**kwds)
    


class LogicalNotPredicate(SchemaBase):
    """LogicalNotPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/LogicalNot<Predicate>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(LogicalNotPredicate, self).__init__(**kwds)
    


class SelectionNot(SchemaBase):
    """SelectionNot schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionNot', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(SelectionNot, self).__init__(**kwds)
    


class LogicalOperandPredicate(SchemaBase):
    """LogicalOperandPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/LogicalOperand<Predicate>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(LogicalOperandPredicate, self).__init__(*args, **kwds)
    


class SelectionOperand(SchemaBase):
    """SelectionOperand schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionOperand', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(SelectionOperand, self).__init__(*args, **kwds)
    


class LogicalOrPredicate(SchemaBase):
    """LogicalOrPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/LogicalOr<Predicate>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(LogicalOrPredicate, self).__init__(**kwds)
    


class SelectionOr(SchemaBase):
    """SelectionOr schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionOr', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(SelectionOr, self).__init__(**kwds)
    


class LookupData(SchemaBase):
    """LookupData schema wrapper"""
    __schema = {'$ref': '#/definitions/LookupData', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, data=Undefined, key=Undefined, fields=Undefined, **kwds):
        super(LookupData, self).__init__(data=data, key=key, fields=fields, **kwds)
    


class LookupTransform(SchemaBase):
    """LookupTransform schema wrapper"""
    __schema = {'$ref': '#/definitions/LookupTransform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, lookup=Undefined, default=Undefined, **kwds):
        super(LookupTransform, self).__init__(lookup=lookup, default=default, **kwds)
    


class Mark(SchemaBase):
    """Mark schema wrapper"""
    __schema = {'$ref': '#/definitions/Mark', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Mark, self).__init__(*args)
    


class MarkConfig(SchemaBase):
    """MarkConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/MarkConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(MarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class MarkDef(SchemaBase):
    """MarkDef schema wrapper"""
    __schema = {'$ref': '#/definitions/MarkDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(MarkDef, self).__init__(type=type, align=align, angle=angle, baseline=baseline, clip=clip, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension, text=text, theta=theta, **kwds)
    


class Month(SchemaBase):
    """Month schema wrapper"""
    __schema = {'$ref': '#/definitions/Month', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Month, self).__init__(*args)
    


class MultiSelection(SchemaBase):
    """MultiSelection schema wrapper"""
    __schema = {'$ref': '#/definitions/MultiSelection', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelection, self).__init__(type=type, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, toggle=toggle, **kwds)
    


class MultiSelectionConfig(SchemaBase):
    """MultiSelectionConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/MultiSelectionConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelectionConfig, self).__init__(empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, toggle=toggle, **kwds)
    


class MultiTimeUnit(SchemaBase):
    """MultiTimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/MultiTimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(MultiTimeUnit, self).__init__(*args, **kwds)
    


class NamedData(SchemaBase):
    """NamedData schema wrapper"""
    __schema = {'$ref': '#/definitions/NamedData', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, name=Undefined, format=Undefined, **kwds):
        super(NamedData, self).__init__(name=name, format=format, **kwds)
    


class NiceTime(SchemaBase):
    """NiceTime schema wrapper"""
    __schema = {'$ref': '#/definitions/NiceTime', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(NiceTime, self).__init__(*args)
    


class OrderFieldDef(SchemaBase):
    """OrderFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/OrderFieldDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(OrderFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit, **kwds)
    


class Orient(SchemaBase):
    """Orient schema wrapper"""
    __schema = {'$ref': '#/definitions/Orient', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(Orient, self).__init__(*args)
    


class Padding(SchemaBase):
    """Padding schema wrapper"""
    __schema = {'$ref': '#/definitions/Padding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(Padding, self).__init__(*args, **kwds)
    


class PositionFieldDef(SchemaBase):
    """PositionFieldDef schema wrapper"""
    __schema = {'$ref': '#/definitions/PositionFieldDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined, field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined, **kwds):
        super(PositionFieldDef, self).__init__(type=type, aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, stack=stack, timeUnit=timeUnit, **kwds)
    


class Predicate(SchemaBase):
    """Predicate schema wrapper"""
    __schema = {'$ref': '#/definitions/Predicate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(Predicate, self).__init__(*args, **kwds)
    


class Projection(SchemaBase):
    """Projection schema wrapper"""
    __schema = {'$ref': '#/definitions/Projection', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined, parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined, rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined, **kwds):
        super(Projection, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent, coefficient=coefficient, distance=distance, fraction=fraction, lobes=lobes, parallel=parallel, precision=precision, radius=radius, ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt, type=type, **kwds)
    


class ProjectionConfig(SchemaBase):
    """ProjectionConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/ProjectionConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined, parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined, rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined, **kwds):
        super(ProjectionConfig, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent, coefficient=coefficient, distance=distance, fraction=fraction, lobes=lobes, parallel=parallel, precision=precision, radius=radius, ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt, type=type, **kwds)
    


class ProjectionType(SchemaBase):
    """ProjectionType schema wrapper"""
    __schema = {'$ref': '#/definitions/ProjectionType', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(ProjectionType, self).__init__(*args)
    


class RangeConfig(SchemaBase):
    """RangeConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/RangeConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, category=Undefined, diverging=Undefined, heatmap=Undefined, ordinal=Undefined, ramp=Undefined, symbol=Undefined, **kwds):
        super(RangeConfig, self).__init__(category=category, diverging=diverging, heatmap=heatmap, ordinal=ordinal, ramp=ramp, symbol=symbol, **kwds)
    


class RangeConfigValue(SchemaBase):
    """RangeConfigValue schema wrapper"""
    __schema = {'$ref': '#/definitions/RangeConfigValue', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(RangeConfigValue, self).__init__(*args, **kwds)
    


class Repeat(SchemaBase):
    """Repeat schema wrapper"""
    __schema = {'$ref': '#/definitions/Repeat', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(Repeat, self).__init__(column=column, row=row, **kwds)
    


class RepeatRef(SchemaBase):
    """RepeatRef schema wrapper"""
    __schema = {'$ref': '#/definitions/RepeatRef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, repeat=Undefined, **kwds):
        super(RepeatRef, self).__init__(repeat=repeat, **kwds)
    


class Resolve(SchemaBase):
    """Resolve schema wrapper"""
    __schema = {'$ref': '#/definitions/Resolve', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, axis=Undefined, legend=Undefined, scale=Undefined, **kwds):
        super(Resolve, self).__init__(axis=axis, legend=legend, scale=scale, **kwds)
    


class ResolveMode(SchemaBase):
    """ResolveMode schema wrapper"""
    __schema = {'$ref': '#/definitions/ResolveMode', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(ResolveMode, self).__init__(*args)
    


class Scale(SchemaBase):
    """Scale schema wrapper"""
    __schema = {'$ref': '#/definitions/Scale', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, base=Undefined, clamp=Undefined, domain=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeStep=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds):
        super(Scale, self).__init__(base=base, clamp=clamp, domain=domain, exponent=exponent, interpolate=interpolate, nice=nice, padding=padding, paddingInner=paddingInner, paddingOuter=paddingOuter, range=range, rangeStep=rangeStep, round=round, scheme=scheme, type=type, zero=zero, **kwds)
    


class ScaleConfig(SchemaBase):
    """ScaleConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/ScaleConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, bandPaddingInner=Undefined, bandPaddingOuter=Undefined, clamp=Undefined, continuousPadding=Undefined, maxBandSize=Undefined, maxFontSize=Undefined, maxOpacity=Undefined, maxSize=Undefined, maxStrokeWidth=Undefined, minBandSize=Undefined, minFontSize=Undefined, minOpacity=Undefined, minSize=Undefined, minStrokeWidth=Undefined, pointPadding=Undefined, rangeStep=Undefined, round=Undefined, textXRangeStep=Undefined, useUnaggregatedDomain=Undefined, **kwds):
        super(ScaleConfig, self).__init__(bandPaddingInner=bandPaddingInner, bandPaddingOuter=bandPaddingOuter, clamp=clamp, continuousPadding=continuousPadding, maxBandSize=maxBandSize, maxFontSize=maxFontSize, maxOpacity=maxOpacity, maxSize=maxSize, maxStrokeWidth=maxStrokeWidth, minBandSize=minBandSize, minFontSize=minFontSize, minOpacity=minOpacity, minSize=minSize, minStrokeWidth=minStrokeWidth, pointPadding=pointPadding, rangeStep=rangeStep, round=round, textXRangeStep=textXRangeStep, useUnaggregatedDomain=useUnaggregatedDomain, **kwds)
    


class ScaleInterpolate(SchemaBase):
    """ScaleInterpolate schema wrapper"""
    __schema = {'$ref': '#/definitions/ScaleInterpolate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(ScaleInterpolate, self).__init__(*args)
    


class ScaleInterpolateParams(SchemaBase):
    """ScaleInterpolateParams schema wrapper"""
    __schema = {'$ref': '#/definitions/ScaleInterpolateParams', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, gamma=Undefined, **kwds):
        super(ScaleInterpolateParams, self).__init__(type=type, gamma=gamma, **kwds)
    


class ScaleResolveMap(SchemaBase):
    """ScaleResolveMap schema wrapper"""
    __schema = {'$ref': '#/definitions/ScaleResolveMap', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, color=Undefined, opacity=Undefined, shape=Undefined, size=Undefined, x=Undefined, y=Undefined, **kwds):
        super(ScaleResolveMap, self).__init__(color=color, opacity=opacity, shape=shape, size=size, x=x, y=y, **kwds)
    


class ScaleType(SchemaBase):
    """ScaleType schema wrapper"""
    __schema = {'$ref': '#/definitions/ScaleType', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(ScaleType, self).__init__(*args)
    


class SchemeParams(SchemaBase):
    """SchemeParams schema wrapper"""
    __schema = {'$ref': '#/definitions/SchemeParams', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, name=Undefined, extent=Undefined, **kwds):
        super(SchemeParams, self).__init__(name=name, extent=extent, **kwds)
    


class SelectionConfig(SchemaBase):
    """SelectionConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, interval=Undefined, multi=Undefined, single=Undefined, **kwds):
        super(SelectionConfig, self).__init__(interval=interval, multi=multi, single=single, **kwds)
    


class SelectionDef(SchemaBase):
    """SelectionDef schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(SelectionDef, self).__init__(*args, **kwds)
    


class SelectionDomain(SchemaBase):
    """SelectionDomain schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionDomain', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(SelectionDomain, self).__init__(*args, **kwds)
    


class SelectionPredicate(SchemaBase):
    """SelectionPredicate schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionPredicate', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, selection=Undefined, **kwds):
        super(SelectionPredicate, self).__init__(selection=selection, **kwds)
    


class SelectionResolution(SchemaBase):
    """SelectionResolution schema wrapper"""
    __schema = {'$ref': '#/definitions/SelectionResolution', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(SelectionResolution, self).__init__(*args)
    


class SingleDefChannel(SchemaBase):
    """SingleDefChannel schema wrapper"""
    __schema = {'$ref': '#/definitions/SingleDefChannel', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(SingleDefChannel, self).__init__(*args)
    


class SingleSelection(SchemaBase):
    """SingleSelection schema wrapper"""
    __schema = {'$ref': '#/definitions/SingleSelection', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, type=Undefined, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, **kwds):
        super(SingleSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, **kwds)
    


class SingleSelectionConfig(SchemaBase):
    """SingleSelectionConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/SingleSelectionConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, **kwds):
        super(SingleSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, **kwds)
    


class SingleTimeUnit(SchemaBase):
    """SingleTimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/SingleTimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(SingleTimeUnit, self).__init__(*args, **kwds)
    


class SortField(SchemaBase):
    """SortField schema wrapper"""
    __schema = {'$ref': '#/definitions/SortField', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, op=Undefined, field=Undefined, order=Undefined, **kwds):
        super(SortField, self).__init__(op=op, field=field, order=order, **kwds)
    


class SortOrder(SchemaBase):
    """SortOrder schema wrapper"""
    __schema = {'$ref': '#/definitions/SortOrder', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(SortOrder, self).__init__(*args)
    


class StackOffset(SchemaBase):
    """StackOffset schema wrapper"""
    __schema = {'$ref': '#/definitions/StackOffset', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)
    


class StyleConfigIndex(SchemaBase):
    """StyleConfigIndex schema wrapper"""
    __schema = {'$ref': '#/definitions/StyleConfigIndex', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(StyleConfigIndex, self).__init__(**kwds)
    


class TextConfig(SchemaBase):
    """TextConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/TextConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, shortTimeLabels=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(TextConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, shortTimeLabels=shortTimeLabels, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class TickConfig(SchemaBase):
    """TickConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/TickConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, align=Undefined, angle=Undefined, bandSize=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, thickness=Undefined, **kwds):
        super(TickConfig, self).__init__(align=align, angle=angle, bandSize=bandSize, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, thickness=thickness, **kwds)
    


class TimeUnit(SchemaBase):
    """TimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/TimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(TimeUnit, self).__init__(*args, **kwds)
    


class TimeUnitTransform(SchemaBase):
    """TimeUnitTransform schema wrapper"""
    __schema = {'$ref': '#/definitions/TimeUnitTransform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, field=Undefined, timeUnit=Undefined, **kwds):
        super(TimeUnitTransform, self).__init__(field=field, timeUnit=timeUnit, **kwds)
    


class TitleOrient(SchemaBase):
    """TitleOrient schema wrapper"""
    __schema = {'$ref': '#/definitions/TitleOrient', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(TitleOrient, self).__init__(*args)
    


class TitleParams(SchemaBase):
    """TitleParams schema wrapper"""
    __schema = {'$ref': '#/definitions/TitleParams', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, text=Undefined, anchor=Undefined, offset=Undefined, orient=Undefined, style=Undefined, **kwds):
        super(TitleParams, self).__init__(text=text, anchor=anchor, offset=offset, orient=orient, style=style, **kwds)
    


class TopLevelFacetedUnitSpec(SchemaBase):
    """TopLevelFacetedUnitSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevel<FacetedUnitSpec>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, mark=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, padding=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(TopLevelFacetedUnitSpec, self).__init__(mark=mark, autosize=autosize, background=background, config=config, data=data, description=description, encoding=encoding, height=height, name=name, padding=padding, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class TopLevelFacetSpec(SchemaBase):
    """TopLevelFacetSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevel<FacetSpec>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, facet=Undefined, spec=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelFacetSpec, self).__init__(facet=facet, spec=spec, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelHConcatSpec(SchemaBase):
    """TopLevelHConcatSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevel<HConcatSpec>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, hconcat=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelHConcatSpec, self).__init__(hconcat=hconcat, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelLayerSpec(SchemaBase):
    """TopLevelLayerSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevel<LayerSpec>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, layer=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, height=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(TopLevelLayerSpec, self).__init__(layer=layer, autosize=autosize, background=background, config=config, data=data, description=description, height=height, name=name, padding=padding, resolve=resolve, title=title, transform=transform, width=width, **kwds)
    


class TopLevelRepeatSpec(SchemaBase):
    """TopLevelRepeatSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevel<RepeatSpec>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, repeat=Undefined, spec=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelRepeatSpec, self).__init__(repeat=repeat, spec=spec, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelVConcatSpec(SchemaBase):
    """TopLevelVConcatSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevel<VConcatSpec>', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, vconcat=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelVConcatSpec, self).__init__(vconcat=vconcat, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelExtendedSpec(SchemaBase):
    """TopLevelExtendedSpec schema wrapper"""
    __schema = {'$ref': '#/definitions/TopLevelExtendedSpec', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(TopLevelExtendedSpec, self).__init__(*args, **kwds)
    


class TopoDataFormat(SchemaBase):
    """TopoDataFormat schema wrapper"""
    __schema = {'$ref': '#/definitions/TopoDataFormat', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(TopoDataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, type=type, **kwds)
    


class Transform(SchemaBase):
    """Transform schema wrapper"""
    __schema = {'$ref': '#/definitions/Transform', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(Transform, self).__init__(*args, **kwds)
    


class Type(SchemaBase):
    """Type schema wrapper"""
    __schema = {'$ref': '#/definitions/Type', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(Type, self).__init__(*args, **kwds)
    


class UrlData(SchemaBase):
    """UrlData schema wrapper"""
    __schema = {'$ref': '#/definitions/UrlData', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, url=Undefined, format=Undefined, **kwds):
        super(UrlData, self).__init__(url=url, format=format, **kwds)
    


class UtcMultiTimeUnit(SchemaBase):
    """UtcMultiTimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/UtcMultiTimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(UtcMultiTimeUnit, self).__init__(*args)
    


class UtcSingleTimeUnit(SchemaBase):
    """UtcSingleTimeUnit schema wrapper"""
    __schema = {'$ref': '#/definitions/UtcSingleTimeUnit', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(UtcSingleTimeUnit, self).__init__(*args)
    


class ValueDef(SchemaBase):
    """ValueDef schema wrapper"""
    __schema = {'$ref': '#/definitions/ValueDef', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, value=Undefined, **kwds):
        super(ValueDef, self).__init__(value=value, **kwds)
    


class ValueDefWithCondition(SchemaBase):
    """ValueDefWithCondition schema wrapper"""
    __schema = {'$ref': '#/definitions/ValueDefWithCondition', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)
    


class MarkPropValueDefWithCondition(SchemaBase):
    """MarkPropValueDefWithCondition schema wrapper"""
    __schema = {'$ref': '#/definitions/MarkPropValueDefWithCondition', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(MarkPropValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)
    


class TextValueDefWithCondition(SchemaBase):
    """TextValueDefWithCondition schema wrapper"""
    __schema = {'$ref': '#/definitions/TextValueDefWithCondition', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(TextValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)
    


class VerticalAlign(SchemaBase):
    """VerticalAlign schema wrapper"""
    __schema = {'$ref': '#/definitions/VerticalAlign', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(VerticalAlign, self).__init__(*args)
    


class VgAxisConfig(SchemaBase):
    """VgAxisConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/VgAxisConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined, domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, **kwds):
        super(VgAxisConfig, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor, domainWidth=domainWidth, grid=grid, gridColor=gridColor, gridDash=gridDash, gridOpacity=gridOpacity, gridWidth=gridWidth, labelAngle=labelAngle, labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, tickColor=tickColor, tickRound=tickRound, tickSize=tickSize, tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign, titleAngle=titleAngle, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titleMaxLength=titleMaxLength, titlePadding=titlePadding, titleX=titleX, titleY=titleY, **kwds)
    


class VgBinding(SchemaBase):
    """VgBinding schema wrapper"""
    __schema = {'$ref': '#/definitions/VgBinding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args, **kwds):
        super(VgBinding, self).__init__(*args, **kwds)
    


class VgCheckboxBinding(SchemaBase):
    """VgCheckboxBinding schema wrapper"""
    __schema = {'$ref': '#/definitions/VgCheckboxBinding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, input=Undefined, element=Undefined, **kwds):
        super(VgCheckboxBinding, self).__init__(input=input, element=element, **kwds)
    


class VgEventStream(SchemaBase):
    """VgEventStream schema wrapper"""
    __schema = {'$ref': '#/definitions/VgEventStream', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, **kwds):
        super(VgEventStream, self).__init__(**kwds)
    


class VgGenericBinding(SchemaBase):
    """VgGenericBinding schema wrapper"""
    __schema = {'$ref': '#/definitions/VgGenericBinding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, input=Undefined, element=Undefined, **kwds):
        super(VgGenericBinding, self).__init__(input=input, element=element, **kwds)
    


class VgMarkConfig(SchemaBase):
    """VgMarkConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/VgMarkConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(VgMarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class VgProjectionType(SchemaBase):
    """VgProjectionType schema wrapper"""
    __schema = {'$ref': '#/definitions/VgProjectionType', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, *args):
        super(VgProjectionType, self).__init__(*args)
    


class VgRadioBinding(SchemaBase):
    """VgRadioBinding schema wrapper"""
    __schema = {'$ref': '#/definitions/VgRadioBinding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, input=Undefined, options=Undefined, element=Undefined, **kwds):
        super(VgRadioBinding, self).__init__(input=input, options=options, element=element, **kwds)
    


class VgRangeBinding(SchemaBase):
    """VgRangeBinding schema wrapper"""
    __schema = {'$ref': '#/definitions/VgRangeBinding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, input=Undefined, element=Undefined, max=Undefined, min=Undefined, step=Undefined, **kwds):
        super(VgRangeBinding, self).__init__(input=input, element=element, max=max, min=min, step=step, **kwds)
    


class VgScheme(SchemaBase):
    """VgScheme schema wrapper"""
    __schema = {'$ref': '#/definitions/VgScheme', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, scheme=Undefined, count=Undefined, extent=Undefined, **kwds):
        super(VgScheme, self).__init__(scheme=scheme, count=count, extent=extent, **kwds)
    


class VgSelectBinding(SchemaBase):
    """VgSelectBinding schema wrapper"""
    __schema = {'$ref': '#/definitions/VgSelectBinding', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, input=Undefined, options=Undefined, element=Undefined, **kwds):
        super(VgSelectBinding, self).__init__(input=input, options=options, element=element, **kwds)
    


class VgTitleConfig(SchemaBase):
    """VgTitleConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/VgTitleConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, anchor=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, font=Undefined, fontSize=Undefined, fontWeight=Undefined, limit=Undefined, offset=Undefined, orient=Undefined, **kwds):
        super(VgTitleConfig, self).__init__(anchor=anchor, angle=angle, baseline=baseline, color=color, font=font, fontSize=fontSize, fontWeight=fontWeight, limit=limit, offset=offset, orient=orient, **kwds)
    


class ViewConfig(SchemaBase):
    """ViewConfig schema wrapper"""
    __schema = {'$ref': '#/definitions/ViewConfig', 'definitions': Root._Root__schema['definitions']}

    def __init__(self, clip=Undefined, fill=Undefined, fillOpacity=Undefined, height=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, width=Undefined, **kwds):
        super(ViewConfig, self).__init__(clip=clip, fill=fill, fillOpacity=fillOpacity, height=height, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, width=width, **kwds)
    

