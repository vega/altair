# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# 2018-02-23 20:22

from altair.utils.schemapi import SchemaBase, Undefined

import os
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, '..', 'vega-schema.json')) as f:
        return json.load(f)


class Root(SchemaBase):
    """Root schema wrapper"""
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, autosize=Undefined, axes=Undefined, background=Undefined, config=Undefined, data=Undefined, description=Undefined, encode=Undefined, height=Undefined, layout=Undefined, legends=Undefined, marks=Undefined, padding=Undefined, projections=Undefined, scales=Undefined, signals=Undefined, title=Undefined, usermeta=Undefined, width=Undefined, **kwds):
        super(Root, self).__init__(autosize=autosize, axes=axes, background=background, config=config, data=data, description=description, encode=encode, height=height, layout=layout, legends=legends, marks=marks, padding=padding, projections=projections, scales=scales, signals=signals, title=title, usermeta=usermeta, width=width, **kwds)
    


class autosize(SchemaBase):
    """autosize schema wrapper"""
    _schema = {'$ref': '#/defs/autosize'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(autosize, self).__init__(*args, **kwds)
    


class axis(SchemaBase):
    """axis schema wrapper
    
    Attributes
    ----------
    orient : any
        
    scale : string
        
    title : stringOrSignal
        
    zindex : float
        
    ticks : boolean
        
    labels : boolean
        
    domain : boolean
        
    grid : boolean
        
    gridScale : string
        
    tickSize : float
        
    labelPadding : float
        
    labelFlush : oneOf(boolean, float)
        
    labelFlushOffset : float
        
    labelOverlap : oneOf(boolean, string)
        
    labelBound : oneOf(boolean, float)
        
    tickCount : tickCount
        
    format : stringOrSignal
        
    values : oneOf(list, signal)
        
    offset : oneOf(float, numberValue)
        
    position : oneOf(float, numberValue)
        
    titlePadding : oneOf(float, numberValue)
        
    minExtent : oneOf(float, numberValue)
        
    maxExtent : oneOf(float, numberValue)
        
    encode : mapping
        
    """
    _schema = {'$ref': '#/defs/axis'}
    _rootschema = Root._schema

    def __init__(self, orient=Undefined, scale=Undefined, domain=Undefined, encode=Undefined, format=Undefined, grid=Undefined, gridScale=Undefined, labelBound=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, position=Undefined, tickCount=Undefined, tickSize=Undefined, ticks=Undefined, title=Undefined, titlePadding=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(axis, self).__init__(orient=orient, scale=scale, domain=domain, encode=encode, format=format, grid=grid, gridScale=gridScale, labelBound=labelBound, labelFlush=labelFlush, labelFlushOffset=labelFlushOffset, labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels, maxExtent=maxExtent, minExtent=minExtent, offset=offset, position=position, tickCount=tickCount, tickSize=tickSize, ticks=ticks, title=title, titlePadding=titlePadding, values=values, zindex=zindex, **kwds)
    


class background(SchemaBase):
    """background schema wrapper"""
    _schema = {'$ref': '#/defs/background'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(background, self).__init__(*args)
    


class bind(SchemaBase):
    """bind schema wrapper"""
    _schema = {'$ref': '#/defs/bind'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(bind, self).__init__(*args, **kwds)
    


class data(SchemaBase):
    """data schema wrapper"""
    _schema = {'$ref': '#/defs/data'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, format=Undefined, on=Undefined, transform=Undefined, **kwds):
        super(data, self).__init__(name=name, format=format, on=on, transform=transform, **kwds)
    


class rule(SchemaBase):
    """rule schema wrapper
    
    Attributes
    ----------
    test : string
        
    """
    _schema = {'$ref': '#/defs/rule'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, **kwds):
        super(rule, self).__init__(test=test, **kwds)
    


class encodeEntry(SchemaBase):
    """encodeEntry schema wrapper
    
    Attributes
    ----------
    x : numberValue
        
    x2 : numberValue
        
    xc : numberValue
        
    width : numberValue
        
    y : numberValue
        
    y2 : numberValue
        
    yc : numberValue
        
    height : numberValue
        
    opacity : numberValue
        
    fill : colorValue
        
    fillOpacity : numberValue
        
    stroke : colorValue
        
    strokeWidth : numberValue
        
    strokeOpacity : numberValue
        
    strokeDash : arrayValue
        
    strokeDashOffset : numberValue
        
    cursor : stringValue
        
    clip : booleanValue
        
    size : numberValue
        
    shape : anyOf(string, stringValue)
        
    path : stringValue
        
    innerRadius : numberValue
        
    outerRadius : numberValue
        
    startAngle : numberValue
        
    endAngle : numberValue
        
    interpolate : stringValue
        
    tension : numberValue
        
    orient : oneOf(list, allOf(stringModifiers, anyOf(oneOf(signal, any, any, any), any, any, any)))
        
    url : stringValue
        
    align : oneOf(list, allOf(stringModifiers, anyOf(oneOf(signal, any, any, any), any, any, any)))
        
    baseline : oneOf(list, allOf(stringModifiers, anyOf(oneOf(signal, any, any, any), any, any, any)))
        
    text : stringValue
        
    dir : stringValue
        
    ellipsis : stringValue
        
    limit : numberValue
        
    dx : numberValue
        
    dy : numberValue
        
    radius : numberValue
        
    theta : numberValue
        
    angle : numberValue
        
    font : stringValue
        
    fontSize : numberValue
        
    fontWeight : nullableStringValue
        
    fontStyle : stringValue
        
    """
    _schema = {'$ref': '#/defs/encodeEntry'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined, cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined, endAngle=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, height=Undefined, innerRadius=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined, orient=Undefined, outerRadius=Undefined, path=Undefined, radius=Undefined, shape=Undefined, size=Undefined, startAngle=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, url=Undefined, width=Undefined, x=Undefined, x2=Undefined, xc=Undefined, y=Undefined, y2=Undefined, yc=Undefined, **kwds):
        super(encodeEntry, self).__init__(align=align, angle=angle, baseline=baseline, clip=clip, cursor=cursor, dir=dir, dx=dx, dy=dy, ellipsis=ellipsis, endAngle=endAngle, fill=fill, fillOpacity=fillOpacity, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, height=height, innerRadius=innerRadius, interpolate=interpolate, limit=limit, opacity=opacity, orient=orient, outerRadius=outerRadius, path=path, radius=radius, shape=shape, size=size, startAngle=startAngle, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, url=url, width=width, x=x, x2=x2, xc=xc, y=y, y2=y2, yc=yc, **kwds)
    


class encode(SchemaBase):
    """encode schema wrapper"""
    _schema = {'$ref': '#/defs/encode'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(encode, self).__init__(**kwds)
    


class layout(SchemaBase):
    """layout schema wrapper"""
    _schema = {'$ref': '#/defs/layout'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(layout, self).__init__(*args, **kwds)
    


class guideEncode(SchemaBase):
    """guideEncode schema wrapper
    
    Attributes
    ----------
    name : string
        
    interactive : boolean
        
    style : style
        
    """
    _schema = {'$ref': '#/defs/guideEncode'}
    _rootschema = Root._schema

    def __init__(self, interactive=Undefined, name=Undefined, style=Undefined, **kwds):
        super(guideEncode, self).__init__(interactive=interactive, name=name, style=style, **kwds)
    


class legend(SchemaBase):
    """legend schema wrapper
    
    Attributes
    ----------
    size : string
        
    shape : string
        
    fill : string
        
    stroke : string
        
    opacity : string
        
    strokeDash : string
        
    type : any
        
    orient : any
        
    title : stringOrSignal
        
    zindex : float
        
    offset : oneOf(float, numberValue)
        
    padding : oneOf(float, numberValue)
        
    titlePadding : oneOf(float, numberValue)
        
    entryPadding : oneOf(float, numberValue)
        
    tickCount : tickCount
        
    format : stringOrSignal
        
    values : oneOf(list, signal)
        
    encode : mapping
        
    """
    _schema = {'$ref': '#/defs/legend'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(legend, self).__init__(*args, **kwds)
    


class mark(SchemaBase):
    """mark schema wrapper
    
    Attributes
    ----------
    type : marktype
        
    role : string
        
    name : string
        
    style : style
        
    key : string
        
    clip : boolean
        
    sort : compare
        
    interactive : boolean
        
    encode : encode
        
    transform : list
        
    on : onMarkTrigger
        
    """
    _schema = {'$ref': '#/defs/mark'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clip=Undefined, encode=Undefined, interactive=Undefined, key=Undefined, name=Undefined, on=Undefined, role=Undefined, sort=Undefined, style=Undefined, transform=Undefined, **kwds):
        super(mark, self).__init__(type=type, clip=clip, encode=encode, interactive=interactive, key=key, name=name, on=on, role=role, sort=sort, style=style, transform=transform, **kwds)
    


class markGroup(SchemaBase):
    """markGroup schema wrapper"""
    _schema = {'$ref': '#/defs/markGroup'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, axes=Undefined, clip=Undefined, data=Undefined, encode=Undefined, interactive=Undefined, key=Undefined, layout=Undefined, legends=Undefined, marks=Undefined, name=Undefined, on=Undefined, projections=Undefined, role=Undefined, scales=Undefined, signals=Undefined, sort=Undefined, style=Undefined, title=Undefined, transform=Undefined, **kwds):
        super(markGroup, self).__init__(type=type, axes=axes, clip=clip, data=data, encode=encode, interactive=interactive, key=key, layout=layout, legends=legends, marks=marks, name=name, on=on, projections=projections, role=role, scales=scales, signals=signals, sort=sort, style=style, title=title, transform=transform, **kwds)
    


class markVisual(SchemaBase):
    """markVisual schema wrapper"""
    _schema = {'$ref': '#/defs/markVisual'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clip=Undefined, encode=Undefined, interactive=Undefined, key=Undefined, name=Undefined, on=Undefined, role=Undefined, sort=Undefined, style=Undefined, transform=Undefined, **kwds):
        super(markVisual, self).__init__(type=type, clip=clip, encode=encode, interactive=interactive, key=key, name=name, on=on, role=role, sort=sort, style=style, transform=transform, **kwds)
    


class listener(SchemaBase):
    """listener schema wrapper"""
    _schema = {'$ref': '#/defs/listener'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(listener, self).__init__(*args, **kwds)
    


class onEvents(SchemaBase):
    """onEvents schema wrapper"""
    _schema = {'$ref': '#/defs/onEvents'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(onEvents, self).__init__(*args)
    


class onTrigger(SchemaBase):
    """onTrigger schema wrapper"""
    _schema = {'$ref': '#/defs/onTrigger'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(onTrigger, self).__init__(*args)
    


class onMarkTrigger(SchemaBase):
    """onMarkTrigger schema wrapper"""
    _schema = {'$ref': '#/defs/onMarkTrigger'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(onMarkTrigger, self).__init__(*args)
    


class padding(SchemaBase):
    """padding schema wrapper"""
    _schema = {'$ref': '#/defs/padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(padding, self).__init__(*args, **kwds)
    


class projection(SchemaBase):
    """projection schema wrapper
    
    Attributes
    ----------
    name : string
        
    type : stringOrSignal
        
    clipAngle : numberOrSignal
        
    clipExtent : oneOf(signal, list)
        
    scale : numberOrSignal
        
    translate : oneOf(signal, list)
        
    center : oneOf(signal, list)
        
    rotate : oneOf(signal, list)
        
    parallels : oneOf(signal, list)
        
    precision : numberOrSignal
        
    pointRadius : numberOrSignal
        
    fit : oneOf(mapping, list)
        
    extent : oneOf(signal, list)
        
    size : oneOf(signal, list)
        
    """
    _schema = {'$ref': '#/defs/projection'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, type=Undefined, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, extent=Undefined, fit=Undefined, parallels=Undefined, pointRadius=Undefined, precision=Undefined, rotate=Undefined, scale=Undefined, size=Undefined, translate=Undefined, **kwds):
        super(projection, self).__init__(name=name, type=type, center=center, clipAngle=clipAngle, clipExtent=clipExtent, extent=extent, fit=fit, parallels=parallels, pointRadius=pointRadius, precision=precision, rotate=rotate, scale=scale, size=size, translate=translate, **kwds)
    


class scale(SchemaBase):
    """scale schema wrapper"""
    _schema = {'$ref': '#/defs/scale'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, domainRaw=Undefined, reverse=Undefined, round=Undefined, type=Undefined, **kwds):
        super(scale, self).__init__(name=name, domain=domain, domainMax=domainMax, domainMid=domainMid, domainMin=domainMin, domainRaw=domainRaw, reverse=reverse, round=round, type=type, **kwds)
    


class scope(SchemaBase):
    """scope schema wrapper
    
    Attributes
    ----------
    encode : encode
        
    layout : layout
        
    signals : list
        
    data : list
        
    scales : list
        
    projections : list
        
    axes : list
        
    legends : list
        
    title : title
        
    marks : list
        
    """
    _schema = {'$ref': '#/defs/scope'}
    _rootschema = Root._schema

    def __init__(self, axes=Undefined, data=Undefined, encode=Undefined, layout=Undefined, legends=Undefined, marks=Undefined, projections=Undefined, scales=Undefined, signals=Undefined, title=Undefined, **kwds):
        super(scope, self).__init__(axes=axes, data=data, encode=encode, layout=layout, legends=legends, marks=marks, projections=projections, scales=scales, signals=signals, title=title, **kwds)
    


class signal(SchemaBase):
    """signal schema wrapper"""
    _schema = {'$ref': '#/defs/signal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(signal, self).__init__(*args, **kwds)
    


class signalName(SchemaBase):
    """signalName schema wrapper"""
    _schema = {'$ref': '#/defs/signalName'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(signalName, self).__init__(*args)
    


class signalNew(SchemaBase):
    """signalNew schema wrapper
    
    Attributes
    ----------
    name : signalName
        
    description : string
        
    value : any
        
    react : boolean
        
    update : exprString
        
    on : onEvents
        
    bind : bind
        
    """
    _schema = {'$ref': '#/defs/signalNew'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, bind=Undefined, description=Undefined, on=Undefined, react=Undefined, update=Undefined, value=Undefined, **kwds):
        super(signalNew, self).__init__(name=name, bind=bind, description=description, on=on, react=react, update=update, value=value, **kwds)
    


class signalPush(SchemaBase):
    """signalPush schema wrapper
    
    Attributes
    ----------
    name : signalName
        
    push : any
        
    description : string
        
    on : onEvents
        
    """
    _schema = {'$ref': '#/defs/signalPush'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, push=Undefined, description=Undefined, on=Undefined, **kwds):
        super(signalPush, self).__init__(name=name, push=push, description=description, on=on, **kwds)
    


class streamParams(SchemaBase):
    """streamParams schema wrapper
    
    Attributes
    ----------
    between : list
        
    marktype : string
        
    markname : string
        
    filter : oneOf(exprString, list)
        
    throttle : float
        
    debounce : float
        
    consume : boolean
        
    """
    _schema = {'$ref': '#/defs/streamParams'}
    _rootschema = Root._schema

    def __init__(self, between=Undefined, consume=Undefined, debounce=Undefined, filter=Undefined, markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(streamParams, self).__init__(between=between, consume=consume, debounce=debounce, filter=filter, markname=markname, marktype=marktype, throttle=throttle, **kwds)
    


class streamEvents(SchemaBase):
    """streamEvents schema wrapper
    
    Attributes
    ----------
    source : string
        
    type : string
        
    """
    _schema = {'$ref': '#/defs/streamEvents'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, source=Undefined, **kwds):
        super(streamEvents, self).__init__(type=type, source=source, **kwds)
    


class stream(SchemaBase):
    """stream schema wrapper"""
    _schema = {'$ref': '#/defs/stream'}
    _rootschema = Root._schema

    def __init__(self, between=Undefined, consume=Undefined, debounce=Undefined, filter=Undefined, markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(stream, self).__init__(between=between, consume=consume, debounce=debounce, filter=filter, markname=markname, marktype=marktype, throttle=throttle, **kwds)
    


class titleEncode(SchemaBase):
    """titleEncode schema wrapper"""
    _schema = {'$ref': '#/defs/titleEncode'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(titleEncode, self).__init__(**kwds)
    


class title(SchemaBase):
    """title schema wrapper"""
    _schema = {'$ref': '#/defs/title'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(title, self).__init__(*args, **kwds)
    


class transform(SchemaBase):
    """transform schema wrapper"""
    _schema = {'$ref': '#/defs/transform'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(transform, self).__init__(*args, **kwds)
    


class transformMark(SchemaBase):
    """transformMark schema wrapper"""
    _schema = {'$ref': '#/defs/transformMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(transformMark, self).__init__(*args, **kwds)
    


class aggregateTransform(SchemaBase):
    """aggregateTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    groupby : oneOf(list, signal)
        
    ops : oneOf(list, signal)
        
    fields : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    drop : anyOf(boolean, signal)
        
    cross : anyOf(boolean, signal)
        
    key : oneOf(scaleField, paramField, expr)
        
    """
    _schema = {'$ref': '#/defs/aggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, cross=Undefined, drop=Undefined, fields=Undefined, groupby=Undefined, key=Undefined, ops=Undefined, signal=Undefined, **kwds):
        super(aggregateTransform, self).__init__(type=type, cross=cross, drop=drop, fields=fields, groupby=groupby, key=key, ops=ops, signal=signal, **kwds)
    


class binTransform(SchemaBase):
    """binTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    anchor : anyOf(float, signal)
        
    maxbins : anyOf(float, signal)
        
    base : anyOf(float, signal)
        
    divide : oneOf(list, signal)
        
    extent : oneOf(list, signal)
        
    step : anyOf(float, signal)
        
    steps : oneOf(list, signal)
        
    minstep : anyOf(float, signal)
        
    nice : anyOf(boolean, signal)
        
    name : anyOf(string, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/binTransform'}
    _rootschema = Root._schema

    def __init__(self, extent=Undefined, field=Undefined, type=Undefined, anchor=Undefined, base=Undefined, divide=Undefined, maxbins=Undefined, minstep=Undefined, name=Undefined, nice=Undefined, signal=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(binTransform, self).__init__(extent=extent, field=field, type=type, anchor=anchor, base=base, divide=divide, maxbins=maxbins, minstep=minstep, name=name, nice=nice, signal=signal, step=step, steps=steps, **kwds)
    


class collectTransform(SchemaBase):
    """collectTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    sort : compare
        
    """
    _schema = {'$ref': '#/defs/collectTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, signal=Undefined, sort=Undefined, **kwds):
        super(collectTransform, self).__init__(type=type, signal=signal, sort=sort, **kwds)
    


class countpatternTransform(SchemaBase):
    """countpatternTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    case : anyOf(any, signal)
        
    pattern : anyOf(string, signal)
        
    stopwords : anyOf(string, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/countpatternTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, type=Undefined, case=Undefined, pattern=Undefined, signal=Undefined, stopwords=Undefined, **kwds):
        super(countpatternTransform, self).__init__(field=field, type=type, case=case, pattern=pattern, signal=signal, stopwords=stopwords, **kwds)
    


class crossTransform(SchemaBase):
    """crossTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    filter : exprString
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/crossTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, filter=Undefined, signal=Undefined, **kwds):
        super(crossTransform, self).__init__(type=type, filter=filter, signal=signal, **kwds)
    


class densityTransform(SchemaBase):
    """densityTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    extent : oneOf(list, signal)
        
    steps : anyOf(float, signal)
        
    method : anyOf(string, signal)
        
    distribution : oneOf(mapping, mapping, mapping, mapping)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/densityTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, distribution=Undefined, extent=Undefined, method=Undefined, signal=Undefined, steps=Undefined, **kwds):
        super(densityTransform, self).__init__(type=type, distribution=distribution, extent=extent, method=method, signal=signal, steps=steps, **kwds)
    


class extentTransform(SchemaBase):
    """extentTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    """
    _schema = {'$ref': '#/defs/extentTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(extentTransform, self).__init__(field=field, type=type, signal=signal, **kwds)
    


class filterTransform(SchemaBase):
    """filterTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    expr : exprString
        
    """
    _schema = {'$ref': '#/defs/filterTransform'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(filterTransform, self).__init__(expr=expr, type=type, signal=signal, **kwds)
    


class foldTransform(SchemaBase):
    """foldTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    fields : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/foldTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(foldTransform, self).__init__(fields=fields, type=type, signal=signal, **kwds)
    


class formulaTransform(SchemaBase):
    """formulaTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    expr : exprString
        
    as : anyOf(string, signal)
        
    initonly : anyOf(boolean, signal)
        
    """
    _schema = {'$ref': '#/defs/formulaTransform'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, type=Undefined, initonly=Undefined, signal=Undefined, **kwds):
        super(formulaTransform, self).__init__(expr=expr, type=type, initonly=initonly, signal=signal, **kwds)
    


class imputeTransform(SchemaBase):
    """imputeTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    key : oneOf(scaleField, paramField, expr)
        
    keyvals : oneOf(list, signal)
        
    groupby : oneOf(list, signal)
        
    method : anyOf(any, signal)
        
    value : any
        
    """
    _schema = {'$ref': '#/defs/imputeTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, key=Undefined, type=Undefined, groupby=Undefined, keyvals=Undefined, method=Undefined, signal=Undefined, value=Undefined, **kwds):
        super(imputeTransform, self).__init__(field=field, key=key, type=type, groupby=groupby, keyvals=keyvals, method=method, signal=signal, value=value, **kwds)
    


class joinaggregateTransform(SchemaBase):
    """joinaggregateTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    groupby : oneOf(list, signal)
        
    fields : oneOf(list, signal)
        
    ops : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    key : oneOf(scaleField, paramField, expr)
        
    """
    _schema = {'$ref': '#/defs/joinaggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, fields=Undefined, groupby=Undefined, key=Undefined, ops=Undefined, signal=Undefined, **kwds):
        super(joinaggregateTransform, self).__init__(type=type, fields=fields, groupby=groupby, key=key, ops=ops, signal=signal, **kwds)
    


class lookupTransform(SchemaBase):
    """lookupTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    from : string
        
    key : oneOf(scaleField, paramField, expr)
        
    values : oneOf(list, signal)
        
    fields : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    default : any
        
    """
    _schema = {'$ref': '#/defs/lookupTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, key=Undefined, type=Undefined, default=Undefined, signal=Undefined, values=Undefined, **kwds):
        super(lookupTransform, self).__init__(fields=fields, key=key, type=type, default=default, signal=signal, values=values, **kwds)
    


class projectTransform(SchemaBase):
    """projectTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    fields : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/projectTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, fields=Undefined, signal=Undefined, **kwds):
        super(projectTransform, self).__init__(type=type, fields=fields, signal=signal, **kwds)
    


class sampleTransform(SchemaBase):
    """sampleTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    size : anyOf(float, signal)
        
    """
    _schema = {'$ref': '#/defs/sampleTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, signal=Undefined, size=Undefined, **kwds):
        super(sampleTransform, self).__init__(type=type, signal=signal, size=size, **kwds)
    


class sequenceTransform(SchemaBase):
    """sequenceTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    start : anyOf(float, signal)
        
    stop : anyOf(float, signal)
        
    step : anyOf(float, signal)
        
    """
    _schema = {'$ref': '#/defs/sequenceTransform'}
    _rootschema = Root._schema

    def __init__(self, start=Undefined, stop=Undefined, type=Undefined, signal=Undefined, step=Undefined, **kwds):
        super(sequenceTransform, self).__init__(start=start, stop=stop, type=type, signal=signal, step=step, **kwds)
    


class windowTransform(SchemaBase):
    """windowTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    sort : compare
        
    groupby : oneOf(list, signal)
        
    ops : oneOf(list, signal)
        
    params : oneOf(list, signal)
        
    fields : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    frame : oneOf(list, signal)
        
    ignorePeers : anyOf(boolean, signal)
        
    """
    _schema = {'$ref': '#/defs/windowTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, fields=Undefined, frame=Undefined, groupby=Undefined, ignorePeers=Undefined, ops=Undefined, params=Undefined, signal=Undefined, sort=Undefined, **kwds):
        super(windowTransform, self).__init__(type=type, fields=fields, frame=frame, groupby=groupby, ignorePeers=ignorePeers, ops=ops, params=params, signal=signal, sort=sort, **kwds)
    


class identifierTransform(SchemaBase):
    """identifierTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    as : anyOf(string, signal)
        
    """
    _schema = {'$ref': '#/defs/identifierTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, signal=Undefined, **kwds):
        super(identifierTransform, self).__init__(type=type, signal=signal, **kwds)
    


class linkpathTransform(SchemaBase):
    """linkpathTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    sourceX : oneOf(scaleField, paramField, expr)
        
    sourceY : oneOf(scaleField, paramField, expr)
        
    targetX : oneOf(scaleField, paramField, expr)
        
    targetY : oneOf(scaleField, paramField, expr)
        
    orient : anyOf(any, signal)
        
    shape : anyOf(any, signal)
        
    as : anyOf(string, signal)
        
    """
    _schema = {'$ref': '#/defs/linkpathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, orient=Undefined, shape=Undefined, signal=Undefined, sourceX=Undefined, sourceY=Undefined, targetX=Undefined, targetY=Undefined, **kwds):
        super(linkpathTransform, self).__init__(type=type, orient=orient, shape=shape, signal=signal, sourceX=sourceX, sourceY=sourceY, targetX=targetX, targetY=targetY, **kwds)
    


class pieTransform(SchemaBase):
    """pieTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    startAngle : anyOf(float, signal)
        
    endAngle : anyOf(float, signal)
        
    sort : anyOf(boolean, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/pieTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, endAngle=Undefined, field=Undefined, signal=Undefined, sort=Undefined, startAngle=Undefined, **kwds):
        super(pieTransform, self).__init__(type=type, endAngle=endAngle, field=field, signal=signal, sort=sort, startAngle=startAngle, **kwds)
    


class stackTransform(SchemaBase):
    """stackTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    groupby : oneOf(list, signal)
        
    sort : compare
        
    offset : anyOf(any, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/stackTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, groupby=Undefined, offset=Undefined, signal=Undefined, sort=Undefined, **kwds):
        super(stackTransform, self).__init__(type=type, field=field, groupby=groupby, offset=offset, signal=signal, sort=sort, **kwds)
    


class contourTransform(SchemaBase):
    """contourTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    size : oneOf(list, signal)
        
    values : oneOf(list, signal)
        
    x : oneOf(scaleField, paramField, expr)
        
    y : oneOf(scaleField, paramField, expr)
        
    cellSize : anyOf(float, signal)
        
    bandwidth : anyOf(float, signal)
        
    count : anyOf(float, signal)
        
    nice : anyOf(float, signal)
        
    thresholds : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/contourTransform'}
    _rootschema = Root._schema

    def __init__(self, size=Undefined, type=Undefined, bandwidth=Undefined, cellSize=Undefined, count=Undefined, nice=Undefined, signal=Undefined, thresholds=Undefined, values=Undefined, x=Undefined, y=Undefined, **kwds):
        super(contourTransform, self).__init__(size=size, type=type, bandwidth=bandwidth, cellSize=cellSize, count=count, nice=nice, signal=signal, thresholds=thresholds, values=values, x=x, y=y, **kwds)
    


class geojsonTransform(SchemaBase):
    """geojsonTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    fields : oneOf(list, signal)
        
    geojson : oneOf(scaleField, paramField, expr)
        
    """
    _schema = {'$ref': '#/defs/geojsonTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, fields=Undefined, geojson=Undefined, signal=Undefined, **kwds):
        super(geojsonTransform, self).__init__(type=type, fields=fields, geojson=geojson, signal=signal, **kwds)
    


class geopathTransform(SchemaBase):
    """geopathTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    projection : string
        
    field : oneOf(scaleField, paramField, expr)
        
    as : anyOf(string, signal)
        
    """
    _schema = {'$ref': '#/defs/geopathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, projection=Undefined, signal=Undefined, **kwds):
        super(geopathTransform, self).__init__(type=type, field=field, projection=projection, signal=signal, **kwds)
    


class geopointTransform(SchemaBase):
    """geopointTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    projection : string
        
    fields : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/geopointTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, projection=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(geopointTransform, self).__init__(fields=fields, projection=projection, type=type, signal=signal, **kwds)
    


class geoshapeTransform(SchemaBase):
    """geoshapeTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    projection : string
        
    field : oneOf(scaleField, paramField, expr)
        
    as : anyOf(string, signal)
        
    """
    _schema = {'$ref': '#/defs/geoshapeTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, projection=Undefined, signal=Undefined, **kwds):
        super(geoshapeTransform, self).__init__(type=type, field=field, projection=projection, signal=signal, **kwds)
    


class graticuleTransform(SchemaBase):
    """graticuleTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    extent : oneOf(list, signal)
        
    extentMajor : oneOf(list, signal)
        
    extentMinor : oneOf(list, signal)
        
    step : oneOf(list, signal)
        
    stepMajor : oneOf(list, signal)
        
    stepMinor : oneOf(list, signal)
        
    precision : anyOf(float, signal)
        
    """
    _schema = {'$ref': '#/defs/graticuleTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, extent=Undefined, extentMajor=Undefined, extentMinor=Undefined, precision=Undefined, signal=Undefined, step=Undefined, stepMajor=Undefined, stepMinor=Undefined, **kwds):
        super(graticuleTransform, self).__init__(type=type, extent=extent, extentMajor=extentMajor, extentMinor=extentMinor, precision=precision, signal=signal, step=step, stepMajor=stepMajor, stepMinor=stepMinor, **kwds)
    


class forceTransform(SchemaBase):
    """forceTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    static : anyOf(boolean, signal)
        
    restart : anyOf(boolean, signal)
        
    iterations : anyOf(float, signal)
        
    alpha : anyOf(float, signal)
        
    alphaMin : anyOf(float, signal)
        
    alphaTarget : anyOf(float, signal)
        
    velocityDecay : anyOf(float, signal)
        
    forces : list
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/forceTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, alpha=Undefined, alphaMin=Undefined, alphaTarget=Undefined, forces=Undefined, iterations=Undefined, restart=Undefined, signal=Undefined, static=Undefined, velocityDecay=Undefined, **kwds):
        super(forceTransform, self).__init__(type=type, alpha=alpha, alphaMin=alphaMin, alphaTarget=alphaTarget, forces=forces, iterations=iterations, restart=restart, signal=signal, static=static, velocityDecay=velocityDecay, **kwds)
    


class nestTransform(SchemaBase):
    """nestTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    keys : oneOf(list, signal)
        
    key : oneOf(scaleField, paramField, expr)
        
    generate : anyOf(boolean, signal)
        
    """
    _schema = {'$ref': '#/defs/nestTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, generate=Undefined, key=Undefined, keys=Undefined, signal=Undefined, **kwds):
        super(nestTransform, self).__init__(type=type, generate=generate, key=key, keys=keys, signal=signal, **kwds)
    


class packTransform(SchemaBase):
    """packTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    sort : compare
        
    padding : anyOf(float, signal)
        
    radius : oneOf(scaleField, paramField, expr)
        
    size : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/packTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, padding=Undefined, radius=Undefined, signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(packTransform, self).__init__(type=type, field=field, padding=padding, radius=radius, signal=signal, size=size, sort=sort, **kwds)
    


class partitionTransform(SchemaBase):
    """partitionTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    sort : compare
        
    padding : anyOf(float, signal)
        
    round : anyOf(boolean, signal)
        
    size : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/partitionTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, padding=Undefined, round=Undefined, signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(partitionTransform, self).__init__(type=type, field=field, padding=padding, round=round, signal=signal, size=size, sort=sort, **kwds)
    


class stratifyTransform(SchemaBase):
    """stratifyTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    key : oneOf(scaleField, paramField, expr)
        
    parentKey : oneOf(scaleField, paramField, expr)
        
    """
    _schema = {'$ref': '#/defs/stratifyTransform'}
    _rootschema = Root._schema

    def __init__(self, key=Undefined, parentKey=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(stratifyTransform, self).__init__(key=key, parentKey=parentKey, type=type, signal=signal, **kwds)
    


class treeTransform(SchemaBase):
    """treeTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    sort : compare
        
    method : anyOf(any, signal)
        
    size : oneOf(list, signal)
        
    nodeSize : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/treeTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, method=Undefined, nodeSize=Undefined, signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(treeTransform, self).__init__(type=type, field=field, method=method, nodeSize=nodeSize, signal=signal, size=size, sort=sort, **kwds)
    


class treelinksTransform(SchemaBase):
    """treelinksTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    key : oneOf(scaleField, paramField, expr)
        
    """
    _schema = {'$ref': '#/defs/treelinksTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, key=Undefined, signal=Undefined, **kwds):
        super(treelinksTransform, self).__init__(type=type, key=key, signal=signal, **kwds)
    


class treemapTransform(SchemaBase):
    """treemapTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    field : oneOf(scaleField, paramField, expr)
        
    sort : compare
        
    method : anyOf(any, signal)
        
    padding : anyOf(float, signal)
        
    paddingInner : anyOf(float, signal)
        
    paddingOuter : anyOf(float, signal)
        
    paddingTop : anyOf(float, signal)
        
    paddingRight : anyOf(float, signal)
        
    paddingBottom : anyOf(float, signal)
        
    paddingLeft : anyOf(float, signal)
        
    ratio : anyOf(float, signal)
        
    round : anyOf(boolean, signal)
        
    size : oneOf(list, signal)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/treemapTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, method=Undefined, padding=Undefined, paddingBottom=Undefined, paddingInner=Undefined, paddingLeft=Undefined, paddingOuter=Undefined, paddingRight=Undefined, paddingTop=Undefined, ratio=Undefined, round=Undefined, signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(treemapTransform, self).__init__(type=type, field=field, method=method, padding=padding, paddingBottom=paddingBottom, paddingInner=paddingInner, paddingLeft=paddingLeft, paddingOuter=paddingOuter, paddingRight=paddingRight, paddingTop=paddingTop, ratio=ratio, round=round, signal=signal, size=size, sort=sort, **kwds)
    


class voronoiTransform(SchemaBase):
    """voronoiTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    x : oneOf(scaleField, paramField, expr)
        
    y : oneOf(scaleField, paramField, expr)
        
    size : oneOf(list, signal)
        
    extent : oneOf(list, signal)
        
    as : anyOf(string, signal)
        
    """
    _schema = {'$ref': '#/defs/voronoiTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, x=Undefined, y=Undefined, extent=Undefined, signal=Undefined, size=Undefined, **kwds):
        super(voronoiTransform, self).__init__(type=type, x=x, y=y, extent=extent, signal=signal, size=size, **kwds)
    


class wordcloudTransform(SchemaBase):
    """wordcloudTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    size : oneOf(list, signal)
        
    font : anyOf(string, signal, expr, paramField)
        
    fontStyle : anyOf(string, signal, expr, paramField)
        
    fontWeight : anyOf(string, signal, expr, paramField)
        
    fontSize : anyOf(float, signal, expr, paramField)
        
    fontSizeRange : oneOf(list, signal, None)
        
    rotate : anyOf(float, signal, expr, paramField)
        
    text : oneOf(scaleField, paramField, expr)
        
    spiral : anyOf(string, signal)
        
    padding : anyOf(float, signal, expr, paramField)
        
    as : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/wordcloudTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, font=Undefined, fontSize=Undefined, fontSizeRange=Undefined, fontStyle=Undefined, fontWeight=Undefined, padding=Undefined, rotate=Undefined, signal=Undefined, size=Undefined, spiral=Undefined, text=Undefined, **kwds):
        super(wordcloudTransform, self).__init__(type=type, font=font, fontSize=fontSize, fontSizeRange=fontSizeRange, fontStyle=fontStyle, fontWeight=fontWeight, padding=padding, rotate=rotate, signal=signal, size=size, spiral=spiral, text=text, **kwds)
    


class crossfilterTransform(SchemaBase):
    """crossfilterTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    fields : oneOf(list, signal)
        
    query : oneOf(list, signal)
        
    """
    _schema = {'$ref': '#/defs/crossfilterTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, query=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(crossfilterTransform, self).__init__(fields=fields, query=query, type=type, signal=signal, **kwds)
    


class resolvefilterTransform(SchemaBase):
    """resolvefilterTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    signal : string
        
    ignore : anyOf(float, signal)
        
    filter : any
        
    """
    _schema = {'$ref': '#/defs/resolvefilterTransform'}
    _rootschema = Root._schema

    def __init__(self, filter=Undefined, ignore=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(resolvefilterTransform, self).__init__(filter=filter, ignore=ignore, type=type, signal=signal, **kwds)
    


class tickCount(SchemaBase):
    """tickCount schema wrapper"""
    _schema = {'$ref': '#/refs/tickCount'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(tickCount, self).__init__(*args, **kwds)
    


class element(SchemaBase):
    """element schema wrapper"""
    _schema = {'$ref': '#/refs/element'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(element, self).__init__(*args)
    


class paramField(SchemaBase):
    """paramField schema wrapper
    
    Attributes
    ----------
    field : string
        
    """
    _schema = {'$ref': '#/refs/paramField'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, **kwds):
        super(paramField, self).__init__(field=field, **kwds)
    


class field(SchemaBase):
    """field schema wrapper"""
    _schema = {'$ref': '#/refs/field'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(field, self).__init__(*args, **kwds)
    


class scale(SchemaBase):
    """scale schema wrapper"""
    _schema = {'$ref': '#/refs/scale'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scale, self).__init__(*args, **kwds)
    


class stringModifiers(SchemaBase):
    """stringModifiers schema wrapper
    
    Attributes
    ----------
    scale : scale
        
    """
    _schema = {'$ref': '#/refs/stringModifiers'}
    _rootschema = Root._schema

    def __init__(self, scale=Undefined, **kwds):
        super(stringModifiers, self).__init__(scale=scale, **kwds)
    


class numberModifiers(SchemaBase):
    """numberModifiers schema wrapper
    
    Attributes
    ----------
    exponent : oneOf(float, numberValue)
        
    mult : oneOf(float, numberValue)
        
    offset : oneOf(float, numberValue)
        
    round : boolean
        
    scale : scale
        
    band : anyOf(float, boolean)
        
    extra : boolean
        
    """
    _schema = {'$ref': '#/refs/numberModifiers'}
    _rootschema = Root._schema

    def __init__(self, band=Undefined, exponent=Undefined, extra=Undefined, mult=Undefined, offset=Undefined, round=Undefined, scale=Undefined, **kwds):
        super(numberModifiers, self).__init__(band=band, exponent=exponent, extra=extra, mult=mult, offset=offset, round=round, scale=scale, **kwds)
    


class value(SchemaBase):
    """value schema wrapper"""
    _schema = {'$ref': '#/refs/value'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(value, self).__init__(*args, **kwds)
    


class numberValue(SchemaBase):
    """numberValue schema wrapper"""
    _schema = {'$ref': '#/refs/numberValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(numberValue, self).__init__(*args, **kwds)
    


class stringValue(SchemaBase):
    """stringValue schema wrapper"""
    _schema = {'$ref': '#/refs/stringValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(stringValue, self).__init__(*args, **kwds)
    


class booleanValue(SchemaBase):
    """booleanValue schema wrapper"""
    _schema = {'$ref': '#/refs/booleanValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(booleanValue, self).__init__(*args, **kwds)
    


class arrayValue(SchemaBase):
    """arrayValue schema wrapper"""
    _schema = {'$ref': '#/refs/arrayValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(arrayValue, self).__init__(*args, **kwds)
    


class nullableStringValue(SchemaBase):
    """nullableStringValue schema wrapper"""
    _schema = {'$ref': '#/refs/nullableStringValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(nullableStringValue, self).__init__(*args, **kwds)
    


class colorRGB(SchemaBase):
    """colorRGB schema wrapper
    
    Attributes
    ----------
    r : numberValue
        
    g : numberValue
        
    b : numberValue
        
    """
    _schema = {'$ref': '#/refs/colorRGB'}
    _rootschema = Root._schema

    def __init__(self, b=Undefined, g=Undefined, r=Undefined, **kwds):
        super(colorRGB, self).__init__(b=b, g=g, r=r, **kwds)
    


class colorHSL(SchemaBase):
    """colorHSL schema wrapper
    
    Attributes
    ----------
    h : numberValue
        
    s : numberValue
        
    l : numberValue
        
    """
    _schema = {'$ref': '#/refs/colorHSL'}
    _rootschema = Root._schema

    def __init__(self, h=Undefined, l=Undefined, s=Undefined, **kwds):
        super(colorHSL, self).__init__(h=h, l=l, s=s, **kwds)
    


class colorLAB(SchemaBase):
    """colorLAB schema wrapper
    
    Attributes
    ----------
    l : numberValue
        
    a : numberValue
        
    b : numberValue
        
    """
    _schema = {'$ref': '#/refs/colorLAB'}
    _rootschema = Root._schema

    def __init__(self, a=Undefined, b=Undefined, l=Undefined, **kwds):
        super(colorLAB, self).__init__(a=a, b=b, l=l, **kwds)
    


class colorHCL(SchemaBase):
    """colorHCL schema wrapper
    
    Attributes
    ----------
    h : numberValue
        
    c : numberValue
        
    l : numberValue
        
    """
    _schema = {'$ref': '#/refs/colorHCL'}
    _rootschema = Root._schema

    def __init__(self, c=Undefined, h=Undefined, l=Undefined, **kwds):
        super(colorHCL, self).__init__(c=c, h=h, l=l, **kwds)
    


class colorValue(SchemaBase):
    """colorValue schema wrapper"""
    _schema = {'$ref': '#/refs/colorValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(colorValue, self).__init__(*args, **kwds)
    


class expr(SchemaBase):
    """expr schema wrapper
    
    Attributes
    ----------
    expr : string
        
    """
    _schema = {'$ref': '#/refs/expr'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, **kwds):
        super(expr, self).__init__(expr=expr, **kwds)
    


class exprString(SchemaBase):
    """exprString schema wrapper"""
    _schema = {'$ref': '#/refs/exprString'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(exprString, self).__init__(*args)
    


class compare(SchemaBase):
    """compare schema wrapper"""
    _schema = {'$ref': '#/refs/compare'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(compare, self).__init__(*args, **kwds)
    


class from_(SchemaBase):
    """from_ schema wrapper
    
    Attributes
    ----------
    data : string
        
    """
    _schema = {'$ref': '#/refs/from'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, **kwds):
        super(from_, self).__init__(data=data, **kwds)
    


class facet(SchemaBase):
    """facet schema wrapper
    
    Attributes
    ----------
    data : string
        
    facet : oneOf(mapping, mapping)
        
    """
    _schema = {'$ref': '#/refs/facet'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, data=Undefined, **kwds):
        super(facet, self).__init__(facet=facet, data=data, **kwds)
    


class style(SchemaBase):
    """style schema wrapper"""
    _schema = {'$ref': '#/refs/style'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(style, self).__init__(*args, **kwds)
    


class marktype(SchemaBase):
    """marktype schema wrapper"""
    _schema = {'$ref': '#/refs/marktype'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(marktype, self).__init__(*args)
    


class sortOrder(SchemaBase):
    """sortOrder schema wrapper"""
    _schema = {'$ref': '#/refs/sortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(sortOrder, self).__init__(*args, **kwds)
    


class scaleField(SchemaBase):
    """scaleField schema wrapper"""
    _schema = {'$ref': '#/refs/scaleField'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scaleField, self).__init__(*args, **kwds)
    


class scaleInterpolate(SchemaBase):
    """scaleInterpolate schema wrapper"""
    _schema = {'$ref': '#/refs/scaleInterpolate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scaleInterpolate, self).__init__(*args, **kwds)
    


class scaleData(SchemaBase):
    """scaleData schema wrapper"""
    _schema = {'$ref': '#/refs/scaleData'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scaleData, self).__init__(*args, **kwds)
    


class selector(SchemaBase):
    """selector schema wrapper"""
    _schema = {'$ref': '#/refs/selector'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(selector, self).__init__(*args)
    


class signal(SchemaBase):
    """signal schema wrapper
    
    Attributes
    ----------
    signal : string
        
    """
    _schema = {'$ref': '#/refs/signal'}
    _rootschema = Root._schema

    def __init__(self, signal=Undefined, **kwds):
        super(signal, self).__init__(signal=signal, **kwds)
    


class booleanOrSignal(SchemaBase):
    """booleanOrSignal schema wrapper"""
    _schema = {'$ref': '#/refs/booleanOrSignal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(booleanOrSignal, self).__init__(*args, **kwds)
    


class numberOrSignal(SchemaBase):
    """numberOrSignal schema wrapper"""
    _schema = {'$ref': '#/refs/numberOrSignal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(numberOrSignal, self).__init__(*args, **kwds)
    


class stringOrSignal(SchemaBase):
    """stringOrSignal schema wrapper"""
    _schema = {'$ref': '#/refs/stringOrSignal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(stringOrSignal, self).__init__(*args, **kwds)
    

