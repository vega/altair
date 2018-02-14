# The contents of this file are automatically generated
# at time 2018-02-14 13:13:41

from altair.utils.schemapi import SchemaBase, Undefined

import os
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, '..', 'vega-lite-schema.json')) as f:
        return json.load(f)


class Root(SchemaBase):
    """Root schema wrapper"""
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)
    


class Aggregate(SchemaBase):
    """Aggregate schema wrapper"""
    _schema = {'$ref': '#/definitions/Aggregate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Aggregate, self).__init__(*args)
    


class AggregateOp(SchemaBase):
    """AggregateOp schema wrapper"""
    _schema = {'$ref': '#/definitions/AggregateOp'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AggregateOp, self).__init__(*args)
    


class AggregateTransform(SchemaBase):
    """AggregateTransform schema wrapper"""
    _schema = {'$ref': '#/definitions/AggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, groupby=Undefined, **kwds):
        super(AggregateTransform, self).__init__(aggregate=aggregate, groupby=groupby, **kwds)
    


class AggregatedFieldDef(SchemaBase):
    """AggregatedFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/AggregatedFieldDef'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, op=Undefined, **kwds):
        super(AggregatedFieldDef, self).__init__(field=field, op=op, **kwds)
    


class Anchor(SchemaBase):
    """Anchor schema wrapper"""
    _schema = {'$ref': '#/definitions/Anchor'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Anchor, self).__init__(*args)
    


class AnyMark(SchemaBase):
    """AnyMark schema wrapper"""
    _schema = {'$ref': '#/definitions/AnyMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(AnyMark, self).__init__(*args, **kwds)
    


class AutoSizeParams(SchemaBase):
    """AutoSizeParams schema wrapper"""
    _schema = {'$ref': '#/definitions/AutoSizeParams'}
    _rootschema = Root._schema

    def __init__(self, contains=Undefined, resize=Undefined, type=Undefined, **kwds):
        super(AutoSizeParams, self).__init__(contains=contains, resize=resize, type=type, **kwds)
    


class AutosizeType(SchemaBase):
    """AutosizeType schema wrapper"""
    _schema = {'$ref': '#/definitions/AutosizeType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AutosizeType, self).__init__(*args)
    


class Axis(SchemaBase):
    """Axis schema wrapper"""
    _schema = {'$ref': '#/definitions/Axis'}
    _rootschema = Root._schema

    def __init__(self, domain=Undefined, format=Undefined, grid=Undefined, labelAngle=Undefined, labelBound=Undefined, labelFlush=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, tickCount=Undefined, tickSize=Undefined, ticks=Undefined, title=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(Axis, self).__init__(domain=domain, format=format, grid=grid, labelAngle=labelAngle, labelBound=labelBound, labelFlush=labelFlush, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, offset=offset, orient=orient, position=position, tickCount=tickCount, tickSize=tickSize, ticks=ticks, title=title, titleMaxLength=titleMaxLength, titlePadding=titlePadding, values=values, zindex=zindex, **kwds)
    


class AxisConfig(SchemaBase):
    """AxisConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/AxisConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined, domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, shortTimeLabels=Undefined, tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, **kwds):
        super(AxisConfig, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor, domainWidth=domainWidth, grid=grid, gridColor=gridColor, gridDash=gridDash, gridOpacity=gridOpacity, gridWidth=gridWidth, labelAngle=labelAngle, labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, shortTimeLabels=shortTimeLabels, tickColor=tickColor, tickRound=tickRound, tickSize=tickSize, tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign, titleAngle=titleAngle, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titleMaxLength=titleMaxLength, titlePadding=titlePadding, titleX=titleX, titleY=titleY, **kwds)
    


class AxisOrient(SchemaBase):
    """AxisOrient schema wrapper"""
    _schema = {'$ref': '#/definitions/AxisOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AxisOrient, self).__init__(*args)
    


class AxisResolveMap(SchemaBase):
    """AxisResolveMap schema wrapper"""
    _schema = {'$ref': '#/definitions/AxisResolveMap'}
    _rootschema = Root._schema

    def __init__(self, x=Undefined, y=Undefined, **kwds):
        super(AxisResolveMap, self).__init__(x=x, y=y, **kwds)
    


class BarConfig(SchemaBase):
    """BarConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/BarConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, binSpacing=Undefined, color=Undefined, continuousBandSize=Undefined, cursor=Undefined, discreteBandSize=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(BarConfig, self).__init__(align=align, angle=angle, baseline=baseline, binSpacing=binSpacing, color=color, continuousBandSize=continuousBandSize, cursor=cursor, discreteBandSize=discreteBandSize, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class BasicType(SchemaBase):
    """BasicType schema wrapper"""
    _schema = {'$ref': '#/definitions/BasicType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(BasicType, self).__init__(*args)
    


class BinParams(SchemaBase):
    """BinParams schema wrapper"""
    _schema = {'$ref': '#/definitions/BinParams'}
    _rootschema = Root._schema

    def __init__(self, base=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(BinParams, self).__init__(base=base, divide=divide, extent=extent, maxbins=maxbins, minstep=minstep, nice=nice, step=step, steps=steps, **kwds)
    


class BinTransform(SchemaBase):
    """BinTransform schema wrapper"""
    _schema = {'$ref': '#/definitions/BinTransform'}
    _rootschema = Root._schema

    def __init__(self, bin=Undefined, field=Undefined, **kwds):
        super(BinTransform, self).__init__(bin=bin, field=field, **kwds)
    


class BrushConfig(SchemaBase):
    """BrushConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/BrushConfig'}
    _rootschema = Root._schema

    def __init__(self, fill=Undefined, fillOpacity=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, **kwds):
        super(BrushConfig, self).__init__(fill=fill, fillOpacity=fillOpacity, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, **kwds)
    


class CalculateTransform(SchemaBase):
    """CalculateTransform schema wrapper"""
    _schema = {'$ref': '#/definitions/CalculateTransform'}
    _rootschema = Root._schema

    def __init__(self, calculate=Undefined, **kwds):
        super(CalculateTransform, self).__init__(calculate=calculate, **kwds)
    


class CompositeUnitSpec(SchemaBase):
    """CompositeUnitSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/CompositeUnitSpec'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(CompositeUnitSpec, self).__init__(mark=mark, data=data, description=description, encoding=encoding, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class ConditionalFieldDef(SchemaBase):
    """ConditionalFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/Conditional<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalFieldDef, self).__init__(*args, **kwds)
    


class ConditionalMarkPropFieldDef(SchemaBase):
    """ConditionalMarkPropFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/Conditional<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalMarkPropFieldDef, self).__init__(*args, **kwds)
    


class ConditionalTextFieldDef(SchemaBase):
    """ConditionalTextFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/Conditional<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalTextFieldDef, self).__init__(*args, **kwds)
    


class ConditionalValueDef(SchemaBase):
    """ConditionalValueDef schema wrapper"""
    _schema = {'$ref': '#/definitions/Conditional<ValueDef>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(ConditionalValueDef, self).__init__(*args, **kwds)
    


class ConditionalPredicateFieldDef(SchemaBase):
    """ConditionalPredicateFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalPredicate<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, **kwds)
    


class ConditionalPredicateMarkPropFieldDef(SchemaBase):
    """ConditionalPredicateMarkPropFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalPredicate<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateMarkPropFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, **kwds)
    


class ConditionalPredicateTextFieldDef(SchemaBase):
    """ConditionalPredicateTextFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalPredicate<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalPredicateTextFieldDef, self).__init__(test=test, type=type, aggregate=aggregate, bin=bin, field=field, format=format, timeUnit=timeUnit, **kwds)
    


class ConditionalPredicateValueDef(SchemaBase):
    """ConditionalPredicateValueDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalPredicate<ValueDef>'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, value=Undefined, **kwds):
        super(ConditionalPredicateValueDef, self).__init__(test=test, value=value, **kwds)
    


class ConditionalSelectionFieldDef(SchemaBase):
    """ConditionalSelectionFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalSelection<FieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, **kwds)
    


class ConditionalSelectionMarkPropFieldDef(SchemaBase):
    """ConditionalSelectionMarkPropFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalSelection<MarkPropFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionMarkPropFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, **kwds)
    


class ConditionalSelectionTextFieldDef(SchemaBase):
    """ConditionalSelectionTextFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalSelection<TextFieldDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(ConditionalSelectionTextFieldDef, self).__init__(selection=selection, type=type, aggregate=aggregate, bin=bin, field=field, format=format, timeUnit=timeUnit, **kwds)
    


class ConditionalSelectionValueDef(SchemaBase):
    """ConditionalSelectionValueDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ConditionalSelection<ValueDef>'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, value=Undefined, **kwds):
        super(ConditionalSelectionValueDef, self).__init__(selection=selection, value=value, **kwds)
    


class Config(SchemaBase):
    """Config schema wrapper"""
    _schema = {'$ref': '#/definitions/Config'}
    _rootschema = Root._schema

    def __init__(self, area=Undefined, autosize=Undefined, axis=Undefined, axisBand=Undefined, axisBottom=Undefined, axisLeft=Undefined, axisRight=Undefined, axisTop=Undefined, axisX=Undefined, axisY=Undefined, background=Undefined, bar=Undefined, circle=Undefined, countTitle=Undefined, fieldTitle=Undefined, geoshape=Undefined, invalidValues=Undefined, legend=Undefined, line=Undefined, mark=Undefined, numberFormat=Undefined, padding=Undefined, point=Undefined, projection=Undefined, range=Undefined, rect=Undefined, rule=Undefined, scale=Undefined, selection=Undefined, square=Undefined, stack=Undefined, style=Undefined, text=Undefined, tick=Undefined, timeFormat=Undefined, title=Undefined, view=Undefined, **kwds):
        super(Config, self).__init__(area=area, autosize=autosize, axis=axis, axisBand=axisBand, axisBottom=axisBottom, axisLeft=axisLeft, axisRight=axisRight, axisTop=axisTop, axisX=axisX, axisY=axisY, background=background, bar=bar, circle=circle, countTitle=countTitle, fieldTitle=fieldTitle, geoshape=geoshape, invalidValues=invalidValues, legend=legend, line=line, mark=mark, numberFormat=numberFormat, padding=padding, point=point, projection=projection, range=range, rect=rect, rule=rule, scale=scale, selection=selection, square=square, stack=stack, style=style, text=text, tick=tick, timeFormat=timeFormat, title=title, view=view, **kwds)
    


class CsvDataFormat(SchemaBase):
    """CsvDataFormat schema wrapper"""
    _schema = {'$ref': '#/definitions/CsvDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, type=Undefined, **kwds):
        super(CsvDataFormat, self).__init__(parse=parse, type=type, **kwds)
    


class Data(SchemaBase):
    """Data schema wrapper"""
    _schema = {'$ref': '#/definitions/Data'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Data, self).__init__(*args, **kwds)
    


class DataFormat(SchemaBase):
    """DataFormat schema wrapper"""
    _schema = {'$ref': '#/definitions/DataFormat'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(DataFormat, self).__init__(*args, **kwds)
    


class DateTime(SchemaBase):
    """DateTime schema wrapper"""
    _schema = {'$ref': '#/definitions/DateTime'}
    _rootschema = Root._schema

    def __init__(self, date=Undefined, day=Undefined, hours=Undefined, milliseconds=Undefined, minutes=Undefined, month=Undefined, quarter=Undefined, seconds=Undefined, utc=Undefined, year=Undefined, **kwds):
        super(DateTime, self).__init__(date=date, day=day, hours=hours, milliseconds=milliseconds, minutes=minutes, month=month, quarter=quarter, seconds=seconds, utc=utc, year=year, **kwds)
    


class Day(SchemaBase):
    """Day schema wrapper"""
    _schema = {'$ref': '#/definitions/Day'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Day, self).__init__(*args)
    


class Encoding(SchemaBase):
    """Encoding schema wrapper"""
    _schema = {'$ref': '#/definitions/Encoding'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, detail=Undefined, href=Undefined, opacity=Undefined, order=Undefined, shape=Undefined, size=Undefined, text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(Encoding, self).__init__(color=color, detail=detail, href=href, opacity=opacity, order=order, shape=shape, size=size, text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2, **kwds)
    


class EncodingWithFacet(SchemaBase):
    """EncodingWithFacet schema wrapper"""
    _schema = {'$ref': '#/definitions/EncodingWithFacet'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, column=Undefined, detail=Undefined, href=Undefined, opacity=Undefined, order=Undefined, row=Undefined, shape=Undefined, size=Undefined, text=Undefined, tooltip=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(EncodingWithFacet, self).__init__(color=color, column=column, detail=detail, href=href, opacity=opacity, order=order, row=row, shape=shape, size=size, text=text, tooltip=tooltip, x=x, x2=x2, y=y, y2=y2, **kwds)
    


class FacetFieldDef(SchemaBase):
    """FacetFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/FacetFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, header=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(FacetFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, header=header, sort=sort, timeUnit=timeUnit, **kwds)
    


class FacetMapping(SchemaBase):
    """FacetMapping schema wrapper"""
    _schema = {'$ref': '#/definitions/FacetMapping'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(FacetMapping, self).__init__(column=column, row=row, **kwds)
    


class FieldDef(SchemaBase):
    """FieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/FieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, **kwds)
    


class FieldDefWithCondition(SchemaBase):
    """FieldDefWithCondition schema wrapper"""
    _schema = {'$ref': '#/definitions/FieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, timeUnit=timeUnit, **kwds)
    


class MarkPropFieldDefWithCondition(SchemaBase):
    """MarkPropFieldDefWithCondition schema wrapper"""
    _schema = {'$ref': '#/definitions/MarkPropFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(MarkPropFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, **kwds)
    


class TextFieldDefWithCondition(SchemaBase):
    """TextFieldDefWithCondition schema wrapper"""
    _schema = {'$ref': '#/definitions/TextFieldDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined, field=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(TextFieldDefWithCondition, self).__init__(type=type, aggregate=aggregate, bin=bin, condition=condition, field=field, format=format, timeUnit=timeUnit, **kwds)
    


class FieldEqualPredicate(SchemaBase):
    """FieldEqualPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/FieldEqualPredicate'}
    _rootschema = Root._schema

    def __init__(self, equal=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(FieldEqualPredicate, self).__init__(equal=equal, field=field, timeUnit=timeUnit, **kwds)
    


class FieldOneOfPredicate(SchemaBase):
    """FieldOneOfPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/FieldOneOfPredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, oneOf=Undefined, timeUnit=Undefined, **kwds):
        super(FieldOneOfPredicate, self).__init__(field=field, oneOf=oneOf, timeUnit=timeUnit, **kwds)
    


class FieldRangePredicate(SchemaBase):
    """FieldRangePredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/FieldRangePredicate'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, range=Undefined, timeUnit=Undefined, **kwds):
        super(FieldRangePredicate, self).__init__(field=field, range=range, timeUnit=timeUnit, **kwds)
    


class FilterTransform(SchemaBase):
    """FilterTransform schema wrapper"""
    _schema = {'$ref': '#/definitions/FilterTransform'}
    _rootschema = Root._schema

    def __init__(self, filter=Undefined, **kwds):
        super(FilterTransform, self).__init__(filter=filter, **kwds)
    


class FontStyle(SchemaBase):
    """FontStyle schema wrapper"""
    _schema = {'$ref': '#/definitions/FontStyle'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontStyle, self).__init__(*args)
    


class FontWeight(SchemaBase):
    """FontWeight schema wrapper"""
    _schema = {'$ref': '#/definitions/FontWeight'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontWeight, self).__init__(*args)
    


class FontWeightNumber(SchemaBase):
    """FontWeightNumber schema wrapper"""
    _schema = {'$ref': '#/definitions/FontWeightNumber'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontWeightNumber, self).__init__(*args)
    


class FacetSpec(SchemaBase):
    """FacetSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/FacetSpec'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, spec=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class HConcatSpec(SchemaBase):
    """HConcatSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/HConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(HConcatSpec, self).__init__(hconcat=hconcat, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class LayerSpec(SchemaBase):
    """LayerSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/LayerSpec'}
    _rootschema = Root._schema

    def __init__(self, layer=Undefined, data=Undefined, description=Undefined, height=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(LayerSpec, self).__init__(layer=layer, data=data, description=description, height=height, name=name, resolve=resolve, title=title, transform=transform, width=width, **kwds)
    


class RepeatSpec(SchemaBase):
    """RepeatSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/RepeatSpec'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(RepeatSpec, self).__init__(repeat=repeat, spec=spec, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class Spec(SchemaBase):
    """Spec schema wrapper"""
    _schema = {'$ref': '#/definitions/Spec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Spec, self).__init__(*args, **kwds)
    


class CompositeUnitSpecAlias(SchemaBase):
    """CompositeUnitSpecAlias schema wrapper"""
    _schema = {'$ref': '#/definitions/CompositeUnitSpecAlias'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(CompositeUnitSpecAlias, self).__init__(mark=mark, data=data, description=description, encoding=encoding, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class FacetedCompositeUnitSpecAlias(SchemaBase):
    """FacetedCompositeUnitSpecAlias schema wrapper"""
    _schema = {'$ref': '#/definitions/FacetedCompositeUnitSpecAlias'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(FacetedCompositeUnitSpecAlias, self).__init__(mark=mark, data=data, description=description, encoding=encoding, height=height, name=name, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class VConcatSpec(SchemaBase):
    """VConcatSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/VConcatSpec'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, data=Undefined, description=Undefined, name=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(VConcatSpec, self).__init__(vconcat=vconcat, data=data, description=description, name=name, resolve=resolve, title=title, transform=transform, **kwds)
    


class GeoType(SchemaBase):
    """GeoType schema wrapper"""
    _schema = {'$ref': '#/definitions/GeoType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(GeoType, self).__init__(*args)
    


class Header(SchemaBase):
    """Header schema wrapper"""
    _schema = {'$ref': '#/definitions/Header'}
    _rootschema = Root._schema

    def __init__(self, format=Undefined, labelAngle=Undefined, title=Undefined, **kwds):
        super(Header, self).__init__(format=format, labelAngle=labelAngle, title=title, **kwds)
    


class HorizontalAlign(SchemaBase):
    """HorizontalAlign schema wrapper"""
    _schema = {'$ref': '#/definitions/HorizontalAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(HorizontalAlign, self).__init__(*args)
    


class InlineData(SchemaBase):
    """InlineData schema wrapper"""
    _schema = {'$ref': '#/definitions/InlineData'}
    _rootschema = Root._schema

    def __init__(self, values=Undefined, format=Undefined, **kwds):
        super(InlineData, self).__init__(values=values, format=format, **kwds)
    


class Interpolate(SchemaBase):
    """Interpolate schema wrapper"""
    _schema = {'$ref': '#/definitions/Interpolate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Interpolate, self).__init__(*args)
    


class IntervalSelection(SchemaBase):
    """IntervalSelection schema wrapper"""
    _schema = {'$ref': '#/definitions/IntervalSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined, **kwds):
        super(IntervalSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings, fields=fields, mark=mark, on=on, resolve=resolve, translate=translate, zoom=zoom, **kwds)
    


class IntervalSelectionConfig(SchemaBase):
    """IntervalSelectionConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/IntervalSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, mark=Undefined, on=Undefined, resolve=Undefined, translate=Undefined, zoom=Undefined, **kwds):
        super(IntervalSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings, fields=fields, mark=mark, on=on, resolve=resolve, translate=translate, zoom=zoom, **kwds)
    


class JsonDataFormat(SchemaBase):
    """JsonDataFormat schema wrapper"""
    _schema = {'$ref': '#/definitions/JsonDataFormat'}
    _rootschema = Root._schema

    def __init__(self, parse=Undefined, property=Undefined, type=Undefined, **kwds):
        super(JsonDataFormat, self).__init__(parse=parse, property=property, type=type, **kwds)
    


class Legend(SchemaBase):
    """Legend schema wrapper"""
    _schema = {'$ref': '#/definitions/Legend'}
    _rootschema = Root._schema

    def __init__(self, entryPadding=Undefined, format=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, tickCount=Undefined, title=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(Legend, self).__init__(entryPadding=entryPadding, format=format, offset=offset, orient=orient, padding=padding, tickCount=tickCount, title=title, type=type, values=values, zindex=zindex, **kwds)
    


class LegendConfig(SchemaBase):
    """LegendConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/LegendConfig'}
    _rootschema = Root._schema

    def __init__(self, cornerRadius=Undefined, entryPadding=Undefined, fillColor=Undefined, gradientHeight=Undefined, gradientLabelBaseline=Undefined, gradientLabelLimit=Undefined, gradientLabelOffset=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientWidth=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOffset=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, shortTimeLabels=Undefined, strokeColor=Undefined, strokeDash=Undefined, strokeWidth=Undefined, symbolColor=Undefined, symbolSize=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, titleAlign=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titlePadding=Undefined, **kwds):
        super(LegendConfig, self).__init__(cornerRadius=cornerRadius, entryPadding=entryPadding, fillColor=fillColor, gradientHeight=gradientHeight, gradientLabelBaseline=gradientLabelBaseline, gradientLabelLimit=gradientLabelLimit, gradientLabelOffset=gradientLabelOffset, gradientStrokeColor=gradientStrokeColor, gradientStrokeWidth=gradientStrokeWidth, gradientWidth=gradientWidth, labelAlign=labelAlign, labelBaseline=labelBaseline, labelColor=labelColor, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOffset=labelOffset, offset=offset, orient=orient, padding=padding, shortTimeLabels=shortTimeLabels, strokeColor=strokeColor, strokeDash=strokeDash, strokeWidth=strokeWidth, symbolColor=symbolColor, symbolSize=symbolSize, symbolStrokeWidth=symbolStrokeWidth, symbolType=symbolType, titleAlign=titleAlign, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titlePadding=titlePadding, **kwds)
    


class LegendOrient(SchemaBase):
    """LegendOrient schema wrapper"""
    _schema = {'$ref': '#/definitions/LegendOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LegendOrient, self).__init__(*args)
    


class LegendResolveMap(SchemaBase):
    """LegendResolveMap schema wrapper"""
    _schema = {'$ref': '#/definitions/LegendResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, opacity=Undefined, shape=Undefined, size=Undefined, **kwds):
        super(LegendResolveMap, self).__init__(color=color, opacity=opacity, shape=shape, size=size, **kwds)
    


class LocalMultiTimeUnit(SchemaBase):
    """LocalMultiTimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/LocalMultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LocalMultiTimeUnit, self).__init__(*args)
    


class LocalSingleTimeUnit(SchemaBase):
    """LocalSingleTimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/LocalSingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(LocalSingleTimeUnit, self).__init__(*args)
    


class LogicalAndPredicate(SchemaBase):
    """LogicalAndPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/LogicalAnd<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(LogicalAndPredicate, self).__init__(**kwds)
    


class SelectionAnd(SchemaBase):
    """SelectionAnd schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionAnd'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionAnd, self).__init__(**kwds)
    


class LogicalNotPredicate(SchemaBase):
    """LogicalNotPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/LogicalNot<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(LogicalNotPredicate, self).__init__(**kwds)
    


class SelectionNot(SchemaBase):
    """SelectionNot schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionNot'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionNot, self).__init__(**kwds)
    


class LogicalOperandPredicate(SchemaBase):
    """LogicalOperandPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/LogicalOperand<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(LogicalOperandPredicate, self).__init__(*args, **kwds)
    


class SelectionOperand(SchemaBase):
    """SelectionOperand schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionOperand'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionOperand, self).__init__(*args, **kwds)
    


class LogicalOrPredicate(SchemaBase):
    """LogicalOrPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/LogicalOr<Predicate>'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(LogicalOrPredicate, self).__init__(**kwds)
    


class SelectionOr(SchemaBase):
    """SelectionOr schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionOr'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(SelectionOr, self).__init__(**kwds)
    


class LookupData(SchemaBase):
    """LookupData schema wrapper"""
    _schema = {'$ref': '#/definitions/LookupData'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, key=Undefined, fields=Undefined, **kwds):
        super(LookupData, self).__init__(data=data, key=key, fields=fields, **kwds)
    


class LookupTransform(SchemaBase):
    """LookupTransform schema wrapper"""
    _schema = {'$ref': '#/definitions/LookupTransform'}
    _rootschema = Root._schema

    def __init__(self, lookup=Undefined, default=Undefined, **kwds):
        super(LookupTransform, self).__init__(lookup=lookup, default=default, **kwds)
    


class Mark(SchemaBase):
    """Mark schema wrapper"""
    _schema = {'$ref': '#/definitions/Mark'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Mark, self).__init__(*args)
    


class MarkConfig(SchemaBase):
    """MarkConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/MarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(MarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class MarkDef(SchemaBase):
    """MarkDef schema wrapper"""
    _schema = {'$ref': '#/definitions/MarkDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, style=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(MarkDef, self).__init__(type=type, align=align, angle=angle, baseline=baseline, clip=clip, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, style=style, tension=tension, text=text, theta=theta, **kwds)
    


class Month(SchemaBase):
    """Month schema wrapper"""
    _schema = {'$ref': '#/definitions/Month'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Month, self).__init__(*args)
    


class MultiSelection(SchemaBase):
    """MultiSelection schema wrapper"""
    _schema = {'$ref': '#/definitions/MultiSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelection, self).__init__(type=type, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, toggle=toggle, **kwds)
    


class MultiSelectionConfig(SchemaBase):
    """MultiSelectionConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/MultiSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, toggle=Undefined, **kwds):
        super(MultiSelectionConfig, self).__init__(empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, toggle=toggle, **kwds)
    


class MultiTimeUnit(SchemaBase):
    """MultiTimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/MultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(MultiTimeUnit, self).__init__(*args, **kwds)
    


class NamedData(SchemaBase):
    """NamedData schema wrapper"""
    _schema = {'$ref': '#/definitions/NamedData'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, format=Undefined, **kwds):
        super(NamedData, self).__init__(name=name, format=format, **kwds)
    


class NiceTime(SchemaBase):
    """NiceTime schema wrapper"""
    _schema = {'$ref': '#/definitions/NiceTime'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(NiceTime, self).__init__(*args)
    


class OrderFieldDef(SchemaBase):
    """OrderFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/OrderFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(OrderFieldDef, self).__init__(type=type, aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit, **kwds)
    


class Orient(SchemaBase):
    """Orient schema wrapper"""
    _schema = {'$ref': '#/definitions/Orient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Orient, self).__init__(*args)
    


class Padding(SchemaBase):
    """Padding schema wrapper"""
    _schema = {'$ref': '#/definitions/Padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Padding, self).__init__(*args, **kwds)
    


class PositionFieldDef(SchemaBase):
    """PositionFieldDef schema wrapper"""
    _schema = {'$ref': '#/definitions/PositionFieldDef'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined, field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined, **kwds):
        super(PositionFieldDef, self).__init__(type=type, aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, stack=stack, timeUnit=timeUnit, **kwds)
    


class Predicate(SchemaBase):
    """Predicate schema wrapper"""
    _schema = {'$ref': '#/definitions/Predicate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Predicate, self).__init__(*args, **kwds)
    


class Projection(SchemaBase):
    """Projection schema wrapper"""
    _schema = {'$ref': '#/definitions/Projection'}
    _rootschema = Root._schema

    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined, parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined, rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined, **kwds):
        super(Projection, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent, coefficient=coefficient, distance=distance, fraction=fraction, lobes=lobes, parallel=parallel, precision=precision, radius=radius, ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt, type=type, **kwds)
    


class ProjectionConfig(SchemaBase):
    """ProjectionConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/ProjectionConfig'}
    _rootschema = Root._schema

    def __init__(self, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, coefficient=Undefined, distance=Undefined, fraction=Undefined, lobes=Undefined, parallel=Undefined, precision=Undefined, radius=Undefined, ratio=Undefined, rotate=Undefined, spacing=Undefined, tilt=Undefined, type=Undefined, **kwds):
        super(ProjectionConfig, self).__init__(center=center, clipAngle=clipAngle, clipExtent=clipExtent, coefficient=coefficient, distance=distance, fraction=fraction, lobes=lobes, parallel=parallel, precision=precision, radius=radius, ratio=ratio, rotate=rotate, spacing=spacing, tilt=tilt, type=type, **kwds)
    


class ProjectionType(SchemaBase):
    """ProjectionType schema wrapper"""
    _schema = {'$ref': '#/definitions/ProjectionType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ProjectionType, self).__init__(*args)
    


class RangeConfig(SchemaBase):
    """RangeConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/RangeConfig'}
    _rootschema = Root._schema

    def __init__(self, category=Undefined, diverging=Undefined, heatmap=Undefined, ordinal=Undefined, ramp=Undefined, symbol=Undefined, **kwds):
        super(RangeConfig, self).__init__(category=category, diverging=diverging, heatmap=heatmap, ordinal=ordinal, ramp=ramp, symbol=symbol, **kwds)
    


class RangeConfigValue(SchemaBase):
    """RangeConfigValue schema wrapper"""
    _schema = {'$ref': '#/definitions/RangeConfigValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(RangeConfigValue, self).__init__(*args, **kwds)
    


class Repeat(SchemaBase):
    """Repeat schema wrapper"""
    _schema = {'$ref': '#/definitions/Repeat'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(Repeat, self).__init__(column=column, row=row, **kwds)
    


class RepeatRef(SchemaBase):
    """RepeatRef schema wrapper"""
    _schema = {'$ref': '#/definitions/RepeatRef'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, **kwds):
        super(RepeatRef, self).__init__(repeat=repeat, **kwds)
    


class Resolve(SchemaBase):
    """Resolve schema wrapper"""
    _schema = {'$ref': '#/definitions/Resolve'}
    _rootschema = Root._schema

    def __init__(self, axis=Undefined, legend=Undefined, scale=Undefined, **kwds):
        super(Resolve, self).__init__(axis=axis, legend=legend, scale=scale, **kwds)
    


class ResolveMode(SchemaBase):
    """ResolveMode schema wrapper"""
    _schema = {'$ref': '#/definitions/ResolveMode'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ResolveMode, self).__init__(*args)
    


class Scale(SchemaBase):
    """Scale schema wrapper"""
    _schema = {'$ref': '#/definitions/Scale'}
    _rootschema = Root._schema

    def __init__(self, base=Undefined, clamp=Undefined, domain=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeStep=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds):
        super(Scale, self).__init__(base=base, clamp=clamp, domain=domain, exponent=exponent, interpolate=interpolate, nice=nice, padding=padding, paddingInner=paddingInner, paddingOuter=paddingOuter, range=range, rangeStep=rangeStep, round=round, scheme=scheme, type=type, zero=zero, **kwds)
    


class ScaleConfig(SchemaBase):
    """ScaleConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/ScaleConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPaddingInner=Undefined, bandPaddingOuter=Undefined, clamp=Undefined, continuousPadding=Undefined, maxBandSize=Undefined, maxFontSize=Undefined, maxOpacity=Undefined, maxSize=Undefined, maxStrokeWidth=Undefined, minBandSize=Undefined, minFontSize=Undefined, minOpacity=Undefined, minSize=Undefined, minStrokeWidth=Undefined, pointPadding=Undefined, rangeStep=Undefined, round=Undefined, textXRangeStep=Undefined, useUnaggregatedDomain=Undefined, **kwds):
        super(ScaleConfig, self).__init__(bandPaddingInner=bandPaddingInner, bandPaddingOuter=bandPaddingOuter, clamp=clamp, continuousPadding=continuousPadding, maxBandSize=maxBandSize, maxFontSize=maxFontSize, maxOpacity=maxOpacity, maxSize=maxSize, maxStrokeWidth=maxStrokeWidth, minBandSize=minBandSize, minFontSize=minFontSize, minOpacity=minOpacity, minSize=minSize, minStrokeWidth=minStrokeWidth, pointPadding=pointPadding, rangeStep=rangeStep, round=round, textXRangeStep=textXRangeStep, useUnaggregatedDomain=useUnaggregatedDomain, **kwds)
    


class ScaleInterpolate(SchemaBase):
    """ScaleInterpolate schema wrapper"""
    _schema = {'$ref': '#/definitions/ScaleInterpolate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ScaleInterpolate, self).__init__(*args)
    


class ScaleInterpolateParams(SchemaBase):
    """ScaleInterpolateParams schema wrapper"""
    _schema = {'$ref': '#/definitions/ScaleInterpolateParams'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, gamma=Undefined, **kwds):
        super(ScaleInterpolateParams, self).__init__(type=type, gamma=gamma, **kwds)
    


class ScaleResolveMap(SchemaBase):
    """ScaleResolveMap schema wrapper"""
    _schema = {'$ref': '#/definitions/ScaleResolveMap'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, opacity=Undefined, shape=Undefined, size=Undefined, x=Undefined, y=Undefined, **kwds):
        super(ScaleResolveMap, self).__init__(color=color, opacity=opacity, shape=shape, size=size, x=x, y=y, **kwds)
    


class ScaleType(SchemaBase):
    """ScaleType schema wrapper"""
    _schema = {'$ref': '#/definitions/ScaleType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ScaleType, self).__init__(*args)
    


class SchemeParams(SchemaBase):
    """SchemeParams schema wrapper"""
    _schema = {'$ref': '#/definitions/SchemeParams'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, extent=Undefined, **kwds):
        super(SchemeParams, self).__init__(name=name, extent=extent, **kwds)
    


class SelectionConfig(SchemaBase):
    """SelectionConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, interval=Undefined, multi=Undefined, single=Undefined, **kwds):
        super(SelectionConfig, self).__init__(interval=interval, multi=multi, single=single, **kwds)
    


class SelectionDef(SchemaBase):
    """SelectionDef schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionDef'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionDef, self).__init__(*args, **kwds)
    


class SelectionDomain(SchemaBase):
    """SelectionDomain schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionDomain'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SelectionDomain, self).__init__(*args, **kwds)
    


class SelectionPredicate(SchemaBase):
    """SelectionPredicate schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionPredicate'}
    _rootschema = Root._schema

    def __init__(self, selection=Undefined, **kwds):
        super(SelectionPredicate, self).__init__(selection=selection, **kwds)
    


class SelectionResolution(SchemaBase):
    """SelectionResolution schema wrapper"""
    _schema = {'$ref': '#/definitions/SelectionResolution'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SelectionResolution, self).__init__(*args)
    


class SingleDefChannel(SchemaBase):
    """SingleDefChannel schema wrapper"""
    _schema = {'$ref': '#/definitions/SingleDefChannel'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SingleDefChannel, self).__init__(*args)
    


class SingleSelection(SchemaBase):
    """SingleSelection schema wrapper"""
    _schema = {'$ref': '#/definitions/SingleSelection'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, **kwds):
        super(SingleSelection, self).__init__(type=type, bind=bind, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, **kwds)
    


class SingleSelectionConfig(SchemaBase):
    """SingleSelectionConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/SingleSelectionConfig'}
    _rootschema = Root._schema

    def __init__(self, bind=Undefined, empty=Undefined, encodings=Undefined, fields=Undefined, nearest=Undefined, on=Undefined, resolve=Undefined, **kwds):
        super(SingleSelectionConfig, self).__init__(bind=bind, empty=empty, encodings=encodings, fields=fields, nearest=nearest, on=on, resolve=resolve, **kwds)
    


class SingleTimeUnit(SchemaBase):
    """SingleTimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/SingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(SingleTimeUnit, self).__init__(*args, **kwds)
    


class SortField(SchemaBase):
    """SortField schema wrapper"""
    _schema = {'$ref': '#/definitions/SortField'}
    _rootschema = Root._schema

    def __init__(self, op=Undefined, field=Undefined, order=Undefined, **kwds):
        super(SortField, self).__init__(op=op, field=field, order=order, **kwds)
    


class SortOrder(SchemaBase):
    """SortOrder schema wrapper"""
    _schema = {'$ref': '#/definitions/SortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SortOrder, self).__init__(*args)
    


class StackOffset(SchemaBase):
    """StackOffset schema wrapper"""
    _schema = {'$ref': '#/definitions/StackOffset'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)
    


class StyleConfigIndex(SchemaBase):
    """StyleConfigIndex schema wrapper"""
    _schema = {'$ref': '#/definitions/StyleConfigIndex'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(StyleConfigIndex, self).__init__(**kwds)
    


class TextConfig(SchemaBase):
    """TextConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/TextConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, shortTimeLabels=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(TextConfig, self).__init__(align=align, angle=angle, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, shortTimeLabels=shortTimeLabels, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class TickConfig(SchemaBase):
    """TickConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/TickConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, bandSize=Undefined, baseline=Undefined, color=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, thickness=Undefined, **kwds):
        super(TickConfig, self).__init__(align=align, angle=angle, bandSize=bandSize, baseline=baseline, color=color, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, thickness=thickness, **kwds)
    


class TimeUnit(SchemaBase):
    """TimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/TimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TimeUnit, self).__init__(*args, **kwds)
    


class TimeUnitTransform(SchemaBase):
    """TimeUnitTransform schema wrapper"""
    _schema = {'$ref': '#/definitions/TimeUnitTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, timeUnit=Undefined, **kwds):
        super(TimeUnitTransform, self).__init__(field=field, timeUnit=timeUnit, **kwds)
    


class TitleOrient(SchemaBase):
    """TitleOrient schema wrapper"""
    _schema = {'$ref': '#/definitions/TitleOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TitleOrient, self).__init__(*args)
    


class TitleParams(SchemaBase):
    """TitleParams schema wrapper"""
    _schema = {'$ref': '#/definitions/TitleParams'}
    _rootschema = Root._schema

    def __init__(self, text=Undefined, anchor=Undefined, offset=Undefined, orient=Undefined, style=Undefined, **kwds):
        super(TitleParams, self).__init__(text=text, anchor=anchor, offset=offset, orient=orient, style=style, **kwds)
    


class TopLevelFacetedUnitSpec(SchemaBase):
    """TopLevelFacetedUnitSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevel<FacetedUnitSpec>'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, encoding=Undefined, height=Undefined, name=Undefined, padding=Undefined, projection=Undefined, selection=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(TopLevelFacetedUnitSpec, self).__init__(mark=mark, autosize=autosize, background=background, config=config, data=data, description=description, encoding=encoding, height=height, name=name, padding=padding, projection=projection, selection=selection, title=title, transform=transform, width=width, **kwds)
    


class TopLevelFacetSpec(SchemaBase):
    """TopLevelFacetSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevel<FacetSpec>'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, spec=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelFacetSpec, self).__init__(facet=facet, spec=spec, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelHConcatSpec(SchemaBase):
    """TopLevelHConcatSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevel<HConcatSpec>'}
    _rootschema = Root._schema

    def __init__(self, hconcat=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelHConcatSpec, self).__init__(hconcat=hconcat, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelLayerSpec(SchemaBase):
    """TopLevelLayerSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevel<LayerSpec>'}
    _rootschema = Root._schema

    def __init__(self, layer=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, height=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(TopLevelLayerSpec, self).__init__(layer=layer, autosize=autosize, background=background, config=config, data=data, description=description, height=height, name=name, padding=padding, resolve=resolve, title=title, transform=transform, width=width, **kwds)
    


class TopLevelRepeatSpec(SchemaBase):
    """TopLevelRepeatSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevel<RepeatSpec>'}
    _rootschema = Root._schema

    def __init__(self, repeat=Undefined, spec=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelRepeatSpec, self).__init__(repeat=repeat, spec=spec, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelVConcatSpec(SchemaBase):
    """TopLevelVConcatSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevel<VConcatSpec>'}
    _rootschema = Root._schema

    def __init__(self, vconcat=Undefined, autosize=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, name=Undefined, padding=Undefined, resolve=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(TopLevelVConcatSpec, self).__init__(vconcat=vconcat, autosize=autosize, background=background, config=config, data=data, description=description, name=name, padding=padding, resolve=resolve, title=title, transform=transform, **kwds)
    


class TopLevelExtendedSpec(SchemaBase):
    """TopLevelExtendedSpec schema wrapper"""
    _schema = {'$ref': '#/definitions/TopLevelExtendedSpec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(TopLevelExtendedSpec, self).__init__(*args, **kwds)
    


class TopoDataFormat(SchemaBase):
    """TopoDataFormat schema wrapper"""
    _schema = {'$ref': '#/definitions/TopoDataFormat'}
    _rootschema = Root._schema

    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, type=Undefined, **kwds):
        super(TopoDataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, type=type, **kwds)
    


class Transform(SchemaBase):
    """Transform schema wrapper"""
    _schema = {'$ref': '#/definitions/Transform'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Transform, self).__init__(*args, **kwds)
    


class Type(SchemaBase):
    """Type schema wrapper"""
    _schema = {'$ref': '#/definitions/Type'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Type, self).__init__(*args, **kwds)
    


class UrlData(SchemaBase):
    """UrlData schema wrapper"""
    _schema = {'$ref': '#/definitions/UrlData'}
    _rootschema = Root._schema

    def __init__(self, url=Undefined, format=Undefined, **kwds):
        super(UrlData, self).__init__(url=url, format=format, **kwds)
    


class UtcMultiTimeUnit(SchemaBase):
    """UtcMultiTimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/UtcMultiTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(UtcMultiTimeUnit, self).__init__(*args)
    


class UtcSingleTimeUnit(SchemaBase):
    """UtcSingleTimeUnit schema wrapper"""
    _schema = {'$ref': '#/definitions/UtcSingleTimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(UtcSingleTimeUnit, self).__init__(*args)
    


class ValueDef(SchemaBase):
    """ValueDef schema wrapper"""
    _schema = {'$ref': '#/definitions/ValueDef'}
    _rootschema = Root._schema

    def __init__(self, value=Undefined, **kwds):
        super(ValueDef, self).__init__(value=value, **kwds)
    


class ValueDefWithCondition(SchemaBase):
    """ValueDefWithCondition schema wrapper"""
    _schema = {'$ref': '#/definitions/ValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(ValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)
    


class MarkPropValueDefWithCondition(SchemaBase):
    """MarkPropValueDefWithCondition schema wrapper"""
    _schema = {'$ref': '#/definitions/MarkPropValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(MarkPropValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)
    


class TextValueDefWithCondition(SchemaBase):
    """TextValueDefWithCondition schema wrapper"""
    _schema = {'$ref': '#/definitions/TextValueDefWithCondition'}
    _rootschema = Root._schema

    def __init__(self, condition=Undefined, value=Undefined, **kwds):
        super(TextValueDefWithCondition, self).__init__(condition=condition, value=value, **kwds)
    


class VerticalAlign(SchemaBase):
    """VerticalAlign schema wrapper"""
    _schema = {'$ref': '#/definitions/VerticalAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VerticalAlign, self).__init__(*args)
    


class VgAxisConfig(SchemaBase):
    """VgAxisConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/VgAxisConfig'}
    _rootschema = Root._schema

    def __init__(self, bandPosition=Undefined, domain=Undefined, domainColor=Undefined, domainWidth=Undefined, grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAngle=Undefined, labelBound=Undefined, labelColor=Undefined, labelFlush=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelLimit=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, tickColor=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, titleAlign=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleMaxLength=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, **kwds):
        super(VgAxisConfig, self).__init__(bandPosition=bandPosition, domain=domain, domainColor=domainColor, domainWidth=domainWidth, grid=grid, gridColor=gridColor, gridDash=gridDash, gridOpacity=gridOpacity, gridWidth=gridWidth, labelAngle=labelAngle, labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush, labelFont=labelFont, labelFontSize=labelFontSize, labelLimit=labelLimit, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, tickColor=tickColor, tickRound=tickRound, tickSize=tickSize, tickWidth=tickWidth, ticks=ticks, titleAlign=titleAlign, titleAngle=titleAngle, titleBaseline=titleBaseline, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight, titleLimit=titleLimit, titleMaxLength=titleMaxLength, titlePadding=titlePadding, titleX=titleX, titleY=titleY, **kwds)
    


class VgBinding(SchemaBase):
    """VgBinding schema wrapper"""
    _schema = {'$ref': '#/definitions/VgBinding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(VgBinding, self).__init__(*args, **kwds)
    


class VgCheckboxBinding(SchemaBase):
    """VgCheckboxBinding schema wrapper"""
    _schema = {'$ref': '#/definitions/VgCheckboxBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, element=Undefined, **kwds):
        super(VgCheckboxBinding, self).__init__(input=input, element=element, **kwds)
    


class VgEventStream(SchemaBase):
    """VgEventStream schema wrapper"""
    _schema = {'$ref': '#/definitions/VgEventStream'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(VgEventStream, self).__init__(**kwds)
    


class VgGenericBinding(SchemaBase):
    """VgGenericBinding schema wrapper"""
    _schema = {'$ref': '#/definitions/VgGenericBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, element=Undefined, **kwds):
        super(VgGenericBinding, self).__init__(input=input, element=element, **kwds)
    


class VgMarkConfig(SchemaBase):
    """VgMarkConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/VgMarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, href=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, radius=Undefined, shape=Undefined, size=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, **kwds):
        super(VgMarkConfig, self).__init__(align=align, angle=angle, baseline=baseline, cursor=cursor, dx=dx, dy=dy, fill=fill, fillOpacity=fillOpacity, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, href=href, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, radius=radius, shape=shape, size=size, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, **kwds)
    


class VgProjectionType(SchemaBase):
    """VgProjectionType schema wrapper"""
    _schema = {'$ref': '#/definitions/VgProjectionType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VgProjectionType, self).__init__(*args)
    


class VgRadioBinding(SchemaBase):
    """VgRadioBinding schema wrapper"""
    _schema = {'$ref': '#/definitions/VgRadioBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, options=Undefined, element=Undefined, **kwds):
        super(VgRadioBinding, self).__init__(input=input, options=options, element=element, **kwds)
    


class VgRangeBinding(SchemaBase):
    """VgRangeBinding schema wrapper"""
    _schema = {'$ref': '#/definitions/VgRangeBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, element=Undefined, max=Undefined, min=Undefined, step=Undefined, **kwds):
        super(VgRangeBinding, self).__init__(input=input, element=element, max=max, min=min, step=step, **kwds)
    


class VgScheme(SchemaBase):
    """VgScheme schema wrapper"""
    _schema = {'$ref': '#/definitions/VgScheme'}
    _rootschema = Root._schema

    def __init__(self, scheme=Undefined, count=Undefined, extent=Undefined, **kwds):
        super(VgScheme, self).__init__(scheme=scheme, count=count, extent=extent, **kwds)
    


class VgSelectBinding(SchemaBase):
    """VgSelectBinding schema wrapper"""
    _schema = {'$ref': '#/definitions/VgSelectBinding'}
    _rootschema = Root._schema

    def __init__(self, input=Undefined, options=Undefined, element=Undefined, **kwds):
        super(VgSelectBinding, self).__init__(input=input, options=options, element=element, **kwds)
    


class VgTitleConfig(SchemaBase):
    """VgTitleConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/VgTitleConfig'}
    _rootschema = Root._schema

    def __init__(self, anchor=Undefined, angle=Undefined, baseline=Undefined, color=Undefined, font=Undefined, fontSize=Undefined, fontWeight=Undefined, limit=Undefined, offset=Undefined, orient=Undefined, **kwds):
        super(VgTitleConfig, self).__init__(anchor=anchor, angle=angle, baseline=baseline, color=color, font=font, fontSize=fontSize, fontWeight=fontWeight, limit=limit, offset=offset, orient=orient, **kwds)
    


class ViewConfig(SchemaBase):
    """ViewConfig schema wrapper"""
    _schema = {'$ref': '#/definitions/ViewConfig'}
    _rootschema = Root._schema

    def __init__(self, clip=Undefined, fill=Undefined, fillOpacity=Undefined, height=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, width=Undefined, **kwds):
        super(ViewConfig, self).__init__(clip=clip, fill=fill, fillOpacity=fillOpacity, height=height, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, width=width, **kwds)
    

