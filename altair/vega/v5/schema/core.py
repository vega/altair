# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import SchemaBase, Undefined, _subclasses

import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, 'vega-schema.json').decode('utf-8'))


class VegaSchema(SchemaBase):
    _rootschema = load_schema()
    @classmethod
    def _default_wrapper_classes(cls):
        return _subclasses(VegaSchema)


class Root(VegaSchema):
    """Root schema wrapper

    allOf(:class:`scope`, Mapping(required=[]))
    """
    _schema = VegaSchema._rootschema

    def __init__(self, autosize=Undefined, axes=Undefined, background=Undefined, config=Undefined,
                 data=Undefined, description=Undefined, encode=Undefined, height=Undefined,
                 layout=Undefined, legends=Undefined, marks=Undefined, padding=Undefined,
                 projections=Undefined, scales=Undefined, signals=Undefined, style=Undefined,
                 title=Undefined, usermeta=Undefined, width=Undefined, **kwds):
        super(Root, self).__init__(autosize=autosize, axes=axes, background=background, config=config,
                                   data=data, description=description, encode=encode, height=height,
                                   layout=layout, legends=legends, marks=marks, padding=padding,
                                   projections=projections, scales=scales, signals=signals, style=style,
                                   title=title, usermeta=usermeta, width=width, **kwds)


class autosize(VegaSchema):
    """autosize schema wrapper

    oneOf(enum('pad', 'fit', 'fit-x', 'fit-y', 'none'), Mapping(required=[type]),
    :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/autosize'}

    def __init__(self, *args, **kwds):
        super(autosize, self).__init__(*args, **kwds)


class axis(VegaSchema):
    """axis schema wrapper

    Mapping(required=[orient, scale])

    Attributes
    ----------

    orient : oneOf(enum('top', 'bottom', 'left', 'right'), :class:`signalRef`)

    scale : string

    aria : boolean

    bandPosition : oneOf(float, :class:`numberValue`)

    description : string

    domain : boolean

    domainCap : oneOf(string, :class:`stringValue`)

    domainColor : oneOf(None, string, :class:`colorValue`)

    domainDash : oneOf(List(float), :class:`arrayValue`)

    domainDashOffset : oneOf(float, :class:`numberValue`)

    domainOpacity : oneOf(float, :class:`numberValue`)

    domainWidth : oneOf(float, :class:`numberValue`)

    encode : Mapping(required=[])

    format : oneOf(string, Mapping(required=[]), :class:`signalRef`)

    formatType : oneOf(enum('number', 'time', 'utc'), :class:`signalRef`)

    grid : boolean

    gridCap : oneOf(string, :class:`stringValue`)

    gridColor : oneOf(None, string, :class:`colorValue`)

    gridDash : oneOf(List(float), :class:`arrayValue`)

    gridDashOffset : oneOf(float, :class:`numberValue`)

    gridOpacity : oneOf(float, :class:`numberValue`)

    gridScale : string

    gridWidth : oneOf(float, :class:`numberValue`)

    labelAlign : oneOf(enum('left', 'right', 'center'), :class:`alignValue`)

    labelAngle : oneOf(float, :class:`numberValue`)

    labelBaseline : oneOf(enum('top', 'middle', 'bottom', 'alphabetic', 'line-top',
    'line-bottom'), :class:`baselineValue`)

    labelBound : oneOf(boolean, float, :class:`signalRef`)

    labelColor : oneOf(None, string, :class:`colorValue`)

    labelFlush : oneOf(boolean, float, :class:`signalRef`)

    labelFlushOffset : :class:`numberOrSignal`

    labelFont : oneOf(string, :class:`stringValue`)

    labelFontSize : oneOf(float, :class:`numberValue`)

    labelFontStyle : oneOf(string, :class:`stringValue`)

    labelFontWeight : oneOf(enum(None, 'normal', 'bold', 'lighter', 'bolder', '100', '200',
    '300', '400', '500', '600', '700', '800', '900', 100, 200, 300, 400, 500, 600, 700, 800,
    900), :class:`fontWeightValue`)

    labelLimit : oneOf(float, :class:`numberValue`)

    labelLineHeight : oneOf(float, :class:`numberValue`)

    labelOffset : oneOf(float, :class:`numberValue`)

    labelOpacity : oneOf(float, :class:`numberValue`)

    labelOverlap : :class:`labelOverlap`

    labelPadding : oneOf(float, :class:`numberValue`)

    labelSeparation : :class:`numberOrSignal`

    labels : boolean

    maxExtent : oneOf(float, :class:`numberValue`)

    minExtent : oneOf(float, :class:`numberValue`)

    offset : oneOf(float, :class:`numberValue`)

    position : oneOf(float, :class:`numberValue`)

    tickBand : :class:`tickBand`

    tickCap : oneOf(string, :class:`stringValue`)

    tickColor : oneOf(None, string, :class:`colorValue`)

    tickCount : :class:`tickCount`

    tickDash : oneOf(List(float), :class:`arrayValue`)

    tickDashOffset : oneOf(float, :class:`numberValue`)

    tickExtra : :class:`booleanOrSignal`

    tickMinStep : :class:`numberOrSignal`

    tickOffset : oneOf(float, :class:`numberValue`)

    tickOpacity : oneOf(float, :class:`numberValue`)

    tickRound : oneOf(boolean, :class:`booleanValue`)

    tickSize : oneOf(float, :class:`numberValue`)

    tickWidth : oneOf(float, :class:`numberValue`)

    ticks : boolean

    title : :class:`textOrSignal`

    titleAlign : oneOf(enum('left', 'right', 'center'), :class:`alignValue`)

    titleAnchor : oneOf(enum(None, 'start', 'middle', 'end'), :class:`anchorValue`)

    titleAngle : oneOf(float, :class:`numberValue`)

    titleBaseline : oneOf(enum('top', 'middle', 'bottom', 'alphabetic', 'line-top',
    'line-bottom'), :class:`baselineValue`)

    titleColor : oneOf(None, string, :class:`colorValue`)

    titleFont : oneOf(string, :class:`stringValue`)

    titleFontSize : oneOf(float, :class:`numberValue`)

    titleFontStyle : oneOf(string, :class:`stringValue`)

    titleFontWeight : oneOf(enum(None, 'normal', 'bold', 'lighter', 'bolder', '100', '200',
    '300', '400', '500', '600', '700', '800', '900', 100, 200, 300, 400, 500, 600, 700, 800,
    900), :class:`fontWeightValue`)

    titleLimit : oneOf(float, :class:`numberValue`)

    titleLineHeight : oneOf(float, :class:`numberValue`)

    titleOpacity : oneOf(float, :class:`numberValue`)

    titlePadding : oneOf(float, :class:`numberValue`)

    titleX : oneOf(float, :class:`numberValue`)

    titleY : oneOf(float, :class:`numberValue`)

    translate : oneOf(float, :class:`numberValue`)

    values : :class:`arrayOrSignal`

    zindex : float

    """
    _schema = {'$ref': '#/definitions/axis'}

    def __init__(self, orient=Undefined, scale=Undefined, aria=Undefined, bandPosition=Undefined,
                 description=Undefined, domain=Undefined, domainCap=Undefined, domainColor=Undefined,
                 domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined,
                 domainWidth=Undefined, encode=Undefined, format=Undefined, formatType=Undefined,
                 grid=Undefined, gridCap=Undefined, gridColor=Undefined, gridDash=Undefined,
                 gridDashOffset=Undefined, gridOpacity=Undefined, gridScale=Undefined,
                 gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined,
                 labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined,
                 labelFlush=Undefined, labelFlushOffset=Undefined, labelFont=Undefined,
                 labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined,
                 labelLimit=Undefined, labelLineHeight=Undefined, labelOffset=Undefined,
                 labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined,
                 labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined,
                 offset=Undefined, position=Undefined, tickBand=Undefined, tickCap=Undefined,
                 tickColor=Undefined, tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined,
                 tickExtra=Undefined, tickMinStep=Undefined, tickOffset=Undefined,
                 tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined,
                 ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined,
                 titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined,
                 titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined,
                 titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined,
                 titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined,
                 translate=Undefined, values=Undefined, zindex=Undefined, **kwds):
        super(axis, self).__init__(orient=orient, scale=scale, aria=aria, bandPosition=bandPosition,
                                   description=description, domain=domain, domainCap=domainCap,
                                   domainColor=domainColor, domainDash=domainDash,
                                   domainDashOffset=domainDashOffset, domainOpacity=domainOpacity,
                                   domainWidth=domainWidth, encode=encode, format=format,
                                   formatType=formatType, grid=grid, gridCap=gridCap,
                                   gridColor=gridColor, gridDash=gridDash,
                                   gridDashOffset=gridDashOffset, gridOpacity=gridOpacity,
                                   gridScale=gridScale, gridWidth=gridWidth, labelAlign=labelAlign,
                                   labelAngle=labelAngle, labelBaseline=labelBaseline,
                                   labelBound=labelBound, labelColor=labelColor, labelFlush=labelFlush,
                                   labelFlushOffset=labelFlushOffset, labelFont=labelFont,
                                   labelFontSize=labelFontSize, labelFontStyle=labelFontStyle,
                                   labelFontWeight=labelFontWeight, labelLimit=labelLimit,
                                   labelLineHeight=labelLineHeight, labelOffset=labelOffset,
                                   labelOpacity=labelOpacity, labelOverlap=labelOverlap,
                                   labelPadding=labelPadding, labelSeparation=labelSeparation,
                                   labels=labels, maxExtent=maxExtent, minExtent=minExtent,
                                   offset=offset, position=position, tickBand=tickBand, tickCap=tickCap,
                                   tickColor=tickColor, tickCount=tickCount, tickDash=tickDash,
                                   tickDashOffset=tickDashOffset, tickExtra=tickExtra,
                                   tickMinStep=tickMinStep, tickOffset=tickOffset,
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


class labelOverlap(VegaSchema):
    """labelOverlap schema wrapper

    oneOf(boolean, enum('parity', 'greedy'), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/labelOverlap'}

    def __init__(self, *args, **kwds):
        super(labelOverlap, self).__init__(*args, **kwds)


class tickBand(VegaSchema):
    """tickBand schema wrapper

    oneOf(enum('center', 'extent'), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/tickBand'}

    def __init__(self, *args, **kwds):
        super(tickBand, self).__init__(*args, **kwds)


class tickCount(VegaSchema):
    """tickCount schema wrapper

    oneOf(float, enum('millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month',
    'year'), Mapping(required=[interval]), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/tickCount'}

    def __init__(self, *args, **kwds):
        super(tickCount, self).__init__(*args, **kwds)


class background(VegaSchema):
    """background schema wrapper

    oneOf(string, :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/background'}

    def __init__(self, *args, **kwds):
        super(background, self).__init__(*args, **kwds)


class bind(VegaSchema):
    """bind schema wrapper

    oneOf(Mapping(required=[input]), Mapping(required=[input, options]),
    Mapping(required=[input]), Mapping(required=[input]), Mapping(required=[element]))
    """
    _schema = {'$ref': '#/definitions/bind'}

    def __init__(self, *args, **kwds):
        super(bind, self).__init__(*args, **kwds)


class element(VegaSchema):
    """element schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/element'}

    def __init__(self, *args):
        super(element, self).__init__(*args)


class data(VegaSchema):
    """data schema wrapper

    oneOf(Mapping(required=[name]), Mapping(required=[source, name]), Mapping(required=[url,
    name]), Mapping(required=[values, name]))
    """
    _schema = {'$ref': '#/definitions/data'}

    def __init__(self, *args, **kwds):
        super(data, self).__init__(*args, **kwds)


class paramField(VegaSchema):
    """paramField schema wrapper

    Mapping(required=[field])

    Attributes
    ----------

    field : string

    as : string

    """
    _schema = {'$ref': '#/definitions/paramField'}

    def __init__(self, field=Undefined, **kwds):
        super(paramField, self).__init__(field=field, **kwds)


class rule(VegaSchema):
    """rule schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    test : string

    """
    _schema = {'$ref': '#/definitions/rule'}

    def __init__(self, test=Undefined, **kwds):
        super(rule, self).__init__(test=test, **kwds)


class encodeEntry(VegaSchema):
    """encodeEntry schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`alignValue`

    angle : :class:`numberValue`

    aria : :class:`booleanValue`

    ariaRole : :class:`stringValue`

    ariaRoleDescription : :class:`stringValue`

    aspect : :class:`booleanValue`

    baseline : :class:`baselineValue`

    blend : :class:`blendValue`

    clip : :class:`booleanValue`

    cornerRadius : :class:`numberValue`

    cornerRadiusBottomLeft : :class:`numberValue`

    cornerRadiusBottomRight : :class:`numberValue`

    cornerRadiusTopLeft : :class:`numberValue`

    cornerRadiusTopRight : :class:`numberValue`

    cursor : :class:`stringValue`

    defined : :class:`booleanValue`

    description : :class:`stringValue`

    dir : :class:`stringValue`

    dx : :class:`numberValue`

    dy : :class:`numberValue`

    ellipsis : :class:`stringValue`

    endAngle : :class:`numberValue`

    fill : :class:`colorValue`

    fillOpacity : :class:`numberValue`

    font : :class:`stringValue`

    fontSize : :class:`numberValue`

    fontStyle : :class:`stringValue`

    fontWeight : :class:`fontWeightValue`

    height : :class:`numberValue`

    innerRadius : :class:`numberValue`

    interpolate : :class:`stringValue`

    limit : :class:`numberValue`

    lineBreak : :class:`stringValue`

    lineHeight : :class:`numberValue`

    opacity : :class:`numberValue`

    orient : :class:`directionValue`

    outerRadius : :class:`numberValue`

    padAngle : :class:`numberValue`

    path : :class:`stringValue`

    radius : :class:`numberValue`

    scaleX : :class:`numberValue`

    scaleY : :class:`numberValue`

    shape : :class:`stringValue`

    size : :class:`numberValue`

    smooth : :class:`booleanValue`

    startAngle : :class:`numberValue`

    stroke : :class:`colorValue`

    strokeCap : :class:`strokeCapValue`

    strokeDash : :class:`arrayValue`

    strokeDashOffset : :class:`numberValue`

    strokeForeground : :class:`booleanValue`

    strokeJoin : :class:`strokeJoinValue`

    strokeMiterLimit : :class:`numberValue`

    strokeOffset : :class:`numberValue`

    strokeOpacity : :class:`numberValue`

    strokeWidth : :class:`numberValue`

    tension : :class:`numberValue`

    text : :class:`textValue`

    theta : :class:`numberValue`

    tooltip : :class:`anyValue`

    url : :class:`stringValue`

    width : :class:`numberValue`

    x : :class:`numberValue`

    x2 : :class:`numberValue`

    xc : :class:`numberValue`

    y : :class:`numberValue`

    y2 : :class:`numberValue`

    yc : :class:`numberValue`

    zindex : :class:`numberValue`

    """
    _schema = {'$ref': '#/definitions/encodeEntry'}

    def __init__(self, align=Undefined, angle=Undefined, aria=Undefined, ariaRole=Undefined,
                 ariaRoleDescription=Undefined, aspect=Undefined, baseline=Undefined, blend=Undefined,
                 clip=Undefined, cornerRadius=Undefined, cornerRadiusBottomLeft=Undefined,
                 cornerRadiusBottomRight=Undefined, cornerRadiusTopLeft=Undefined,
                 cornerRadiusTopRight=Undefined, cursor=Undefined, defined=Undefined,
                 description=Undefined, dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined,
                 endAngle=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, height=Undefined,
                 innerRadius=Undefined, interpolate=Undefined, limit=Undefined, lineBreak=Undefined,
                 lineHeight=Undefined, opacity=Undefined, orient=Undefined, outerRadius=Undefined,
                 padAngle=Undefined, path=Undefined, radius=Undefined, scaleX=Undefined,
                 scaleY=Undefined, shape=Undefined, size=Undefined, smooth=Undefined,
                 startAngle=Undefined, stroke=Undefined, strokeCap=Undefined, strokeDash=Undefined,
                 strokeDashOffset=Undefined, strokeForeground=Undefined, strokeJoin=Undefined,
                 strokeMiterLimit=Undefined, strokeOffset=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 tooltip=Undefined, url=Undefined, width=Undefined, x=Undefined, x2=Undefined,
                 xc=Undefined, y=Undefined, y2=Undefined, yc=Undefined, zindex=Undefined, **kwds):
        super(encodeEntry, self).__init__(align=align, angle=angle, aria=aria, ariaRole=ariaRole,
                                          ariaRoleDescription=ariaRoleDescription, aspect=aspect,
                                          baseline=baseline, blend=blend, clip=clip,
                                          cornerRadius=cornerRadius,
                                          cornerRadiusBottomLeft=cornerRadiusBottomLeft,
                                          cornerRadiusBottomRight=cornerRadiusBottomRight,
                                          cornerRadiusTopLeft=cornerRadiusTopLeft,
                                          cornerRadiusTopRight=cornerRadiusTopRight, cursor=cursor,
                                          defined=defined, description=description, dir=dir, dx=dx,
                                          dy=dy, ellipsis=ellipsis, endAngle=endAngle, fill=fill,
                                          fillOpacity=fillOpacity, font=font, fontSize=fontSize,
                                          fontStyle=fontStyle, fontWeight=fontWeight, height=height,
                                          innerRadius=innerRadius, interpolate=interpolate, limit=limit,
                                          lineBreak=lineBreak, lineHeight=lineHeight, opacity=opacity,
                                          orient=orient, outerRadius=outerRadius, padAngle=padAngle,
                                          path=path, radius=radius, scaleX=scaleX, scaleY=scaleY,
                                          shape=shape, size=size, smooth=smooth, startAngle=startAngle,
                                          stroke=stroke, strokeCap=strokeCap, strokeDash=strokeDash,
                                          strokeDashOffset=strokeDashOffset,
                                          strokeForeground=strokeForeground, strokeJoin=strokeJoin,
                                          strokeMiterLimit=strokeMiterLimit, strokeOffset=strokeOffset,
                                          strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                          tension=tension, text=text, theta=theta, tooltip=tooltip,
                                          url=url, width=width, x=x, x2=x2, xc=xc, y=y, y2=y2, yc=yc,
                                          zindex=zindex, **kwds)


class encode(VegaSchema):
    """encode schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/definitions/encode'}

    def __init__(self, **kwds):
        super(encode, self).__init__(**kwds)


class field(VegaSchema):
    """field schema wrapper

    oneOf(string, :class:`signalRef`, Mapping(required=[datum]), Mapping(required=[group]),
    Mapping(required=[parent]))
    """
    _schema = {'$ref': '#/definitions/field'}

    def __init__(self, *args, **kwds):
        super(field, self).__init__(*args, **kwds)


class stringModifiers(VegaSchema):
    """stringModifiers schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    scale : :class:`field`

    """
    _schema = {'$ref': '#/definitions/stringModifiers'}

    def __init__(self, scale=Undefined, **kwds):
        super(stringModifiers, self).__init__(scale=scale, **kwds)


class numberModifiers(VegaSchema):
    """numberModifiers schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    band : oneOf(float, boolean)

    exponent : oneOf(float, :class:`numberValue`)

    extra : boolean

    mult : oneOf(float, :class:`numberValue`)

    offset : oneOf(float, :class:`numberValue`)

    round : boolean

    scale : :class:`field`

    """
    _schema = {'$ref': '#/definitions/numberModifiers'}

    def __init__(self, band=Undefined, exponent=Undefined, extra=Undefined, mult=Undefined,
                 offset=Undefined, round=Undefined, scale=Undefined, **kwds):
        super(numberModifiers, self).__init__(band=band, exponent=exponent, extra=extra, mult=mult,
                                              offset=offset, round=round, scale=scale, **kwds)


class anyValue(VegaSchema):
    """anyValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/anyValue'}

    def __init__(self, *args, **kwds):
        super(anyValue, self).__init__(*args, **kwds)


class blendValue(VegaSchema):
    """blendValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/blendValue'}

    def __init__(self, *args, **kwds):
        super(blendValue, self).__init__(*args, **kwds)


class numberValue(VegaSchema):
    """numberValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`numberModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`numberModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/numberValue'}

    def __init__(self, *args, **kwds):
        super(numberValue, self).__init__(*args, **kwds)


class stringValue(VegaSchema):
    """stringValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/stringValue'}

    def __init__(self, *args, **kwds):
        super(stringValue, self).__init__(*args, **kwds)


class textValue(VegaSchema):
    """textValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/textValue'}

    def __init__(self, *args, **kwds):
        super(textValue, self).__init__(*args, **kwds)


class booleanValue(VegaSchema):
    """booleanValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/booleanValue'}

    def __init__(self, *args, **kwds):
        super(booleanValue, self).__init__(*args, **kwds)


class arrayValue(VegaSchema):
    """arrayValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/arrayValue'}

    def __init__(self, *args, **kwds):
        super(arrayValue, self).__init__(*args, **kwds)


class fontWeightValue(VegaSchema):
    """fontWeightValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/fontWeightValue'}

    def __init__(self, *args, **kwds):
        super(fontWeightValue, self).__init__(*args, **kwds)


class anchorValue(VegaSchema):
    """anchorValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/anchorValue'}

    def __init__(self, *args, **kwds):
        super(anchorValue, self).__init__(*args, **kwds)


class alignValue(VegaSchema):
    """alignValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/alignValue'}

    def __init__(self, *args, **kwds):
        super(alignValue, self).__init__(*args, **kwds)


class baselineValue(VegaSchema):
    """baselineValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/baselineValue'}

    def __init__(self, *args, **kwds):
        super(baselineValue, self).__init__(*args, **kwds)


class directionValue(VegaSchema):
    """directionValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/directionValue'}

    def __init__(self, *args, **kwds):
        super(directionValue, self).__init__(*args, **kwds)


class orientValue(VegaSchema):
    """orientValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/orientValue'}

    def __init__(self, *args, **kwds):
        super(orientValue, self).__init__(*args, **kwds)


class strokeCapValue(VegaSchema):
    """strokeCapValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/strokeCapValue'}

    def __init__(self, *args, **kwds):
        super(strokeCapValue, self).__init__(*args, **kwds)


class strokeJoinValue(VegaSchema):
    """strokeJoinValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signalRef`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/definitions/strokeJoinValue'}

    def __init__(self, *args, **kwds):
        super(strokeJoinValue, self).__init__(*args, **kwds)


class baseColorValue(VegaSchema):
    """baseColorValue schema wrapper

    oneOf(allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signalRef`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))), Mapping(required=[value]), Mapping(required=[value]),
    Mapping(required=[gradient]), Mapping(required=[color]))
    """
    _schema = {'$ref': '#/definitions/baseColorValue'}

    def __init__(self, *args, **kwds):
        super(baseColorValue, self).__init__(*args, **kwds)


class colorRGB(VegaSchema):
    """colorRGB schema wrapper

    Mapping(required=[r, g, b])

    Attributes
    ----------

    b : :class:`numberValue`

    g : :class:`numberValue`

    r : :class:`numberValue`

    """
    _schema = {'$ref': '#/definitions/colorRGB'}

    def __init__(self, b=Undefined, g=Undefined, r=Undefined, **kwds):
        super(colorRGB, self).__init__(b=b, g=g, r=r, **kwds)


class colorHSL(VegaSchema):
    """colorHSL schema wrapper

    Mapping(required=[h, s, l])

    Attributes
    ----------

    h : :class:`numberValue`

    l : :class:`numberValue`

    s : :class:`numberValue`

    """
    _schema = {'$ref': '#/definitions/colorHSL'}

    def __init__(self, h=Undefined, l=Undefined, s=Undefined, **kwds):
        super(colorHSL, self).__init__(h=h, l=l, s=s, **kwds)


class colorLAB(VegaSchema):
    """colorLAB schema wrapper

    Mapping(required=[l, a, b])

    Attributes
    ----------

    a : :class:`numberValue`

    b : :class:`numberValue`

    l : :class:`numberValue`

    """
    _schema = {'$ref': '#/definitions/colorLAB'}

    def __init__(self, a=Undefined, b=Undefined, l=Undefined, **kwds):
        super(colorLAB, self).__init__(a=a, b=b, l=l, **kwds)


class colorHCL(VegaSchema):
    """colorHCL schema wrapper

    Mapping(required=[h, c, l])

    Attributes
    ----------

    c : :class:`numberValue`

    h : :class:`numberValue`

    l : :class:`numberValue`

    """
    _schema = {'$ref': '#/definitions/colorHCL'}

    def __init__(self, c=Undefined, h=Undefined, l=Undefined, **kwds):
        super(colorHCL, self).__init__(c=c, h=h, l=l, **kwds)


class colorValue(VegaSchema):
    """colorValue schema wrapper

    oneOf(List(allOf(:class:`rule`, :class:`baseColorValue`)), :class:`baseColorValue`)
    """
    _schema = {'$ref': '#/definitions/colorValue'}

    def __init__(self, *args, **kwds):
        super(colorValue, self).__init__(*args, **kwds)


class gradientStops(VegaSchema):
    """gradientStops schema wrapper

    List(Mapping(required=[offset, color]))
    """
    _schema = {'$ref': '#/definitions/gradientStops'}

    def __init__(self, *args):
        super(gradientStops, self).__init__(*args)


class linearGradient(VegaSchema):
    """linearGradient schema wrapper

    Mapping(required=[gradient, stops])

    Attributes
    ----------

    gradient : enum('linear')

    stops : :class:`gradientStops`

    id : string

    x1 : float

    x2 : float

    y1 : float

    y2 : float

    """
    _schema = {'$ref': '#/definitions/linearGradient'}

    def __init__(self, gradient=Undefined, stops=Undefined, id=Undefined, x1=Undefined, x2=Undefined,
                 y1=Undefined, y2=Undefined, **kwds):
        super(linearGradient, self).__init__(gradient=gradient, stops=stops, id=id, x1=x1, x2=x2, y1=y1,
                                             y2=y2, **kwds)


class radialGradient(VegaSchema):
    """radialGradient schema wrapper

    Mapping(required=[gradient, stops])

    Attributes
    ----------

    gradient : enum('radial')

    stops : :class:`gradientStops`

    id : string

    r1 : float

    r2 : float

    x1 : float

    x2 : float

    y1 : float

    y2 : float

    """
    _schema = {'$ref': '#/definitions/radialGradient'}

    def __init__(self, gradient=Undefined, stops=Undefined, id=Undefined, r1=Undefined, r2=Undefined,
                 x1=Undefined, x2=Undefined, y1=Undefined, y2=Undefined, **kwds):
        super(radialGradient, self).__init__(gradient=gradient, stops=stops, id=id, r1=r1, r2=r2, x1=x1,
                                             x2=x2, y1=y1, y2=y2, **kwds)


class expr(VegaSchema):
    """expr schema wrapper

    Mapping(required=[expr])

    Attributes
    ----------

    expr : string

    as : string

    """
    _schema = {'$ref': '#/definitions/expr'}

    def __init__(self, expr=Undefined, **kwds):
        super(expr, self).__init__(expr=expr, **kwds)


class exprString(VegaSchema):
    """exprString schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/exprString'}

    def __init__(self, *args):
        super(exprString, self).__init__(*args)


class layout(VegaSchema):
    """layout schema wrapper

    oneOf(Mapping(required=[]), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/layout'}

    def __init__(self, *args, **kwds):
        super(layout, self).__init__(*args, **kwds)


class guideEncode(VegaSchema):
    """guideEncode schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    interactive : boolean

    name : string

    style : :class:`style`

    """
    _schema = {'$ref': '#/definitions/guideEncode'}

    def __init__(self, interactive=Undefined, name=Undefined, style=Undefined, **kwds):
        super(guideEncode, self).__init__(interactive=interactive, name=name, style=style, **kwds)


class legend(VegaSchema):
    """legend schema wrapper

    allOf(Mapping(required=[]), anyOf(Mapping(required=[size]), Mapping(required=[shape]),
    Mapping(required=[fill]), Mapping(required=[stroke]), Mapping(required=[opacity]),
    Mapping(required=[strokeDash]), Mapping(required=[strokeWidth])))
    """
    _schema = {'$ref': '#/definitions/legend'}

    def __init__(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined,
                 cornerRadius=Undefined, description=Undefined, direction=Undefined, encode=Undefined,
                 fill=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined,
                 gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined,
                 gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined,
                 labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined,
                 labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined,
                 labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined,
                 labelOpacity=Undefined, labelOverlap=Undefined, labelSeparation=Undefined,
                 legendX=Undefined, legendY=Undefined, offset=Undefined, opacity=Undefined,
                 orient=Undefined, padding=Undefined, rowPadding=Undefined, shape=Undefined,
                 size=Undefined, stroke=Undefined, strokeColor=Undefined, strokeDash=Undefined,
                 strokeWidth=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined,
                 symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined,
                 symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined,
                 symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined,
                 tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined,
                 titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined,
                 titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined,
                 titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined,
                 zindex=Undefined, **kwds):
        super(legend, self).__init__(aria=aria, clipHeight=clipHeight, columnPadding=columnPadding,
                                     columns=columns, cornerRadius=cornerRadius,
                                     description=description, direction=direction, encode=encode,
                                     fill=fill, fillColor=fillColor, format=format,
                                     formatType=formatType, gradientLength=gradientLength,
                                     gradientOpacity=gradientOpacity,
                                     gradientStrokeColor=gradientStrokeColor,
                                     gradientStrokeWidth=gradientStrokeWidth,
                                     gradientThickness=gradientThickness, gridAlign=gridAlign,
                                     labelAlign=labelAlign, labelBaseline=labelBaseline,
                                     labelColor=labelColor, labelFont=labelFont,
                                     labelFontSize=labelFontSize, labelFontStyle=labelFontStyle,
                                     labelFontWeight=labelFontWeight, labelLimit=labelLimit,
                                     labelOffset=labelOffset, labelOpacity=labelOpacity,
                                     labelOverlap=labelOverlap, labelSeparation=labelSeparation,
                                     legendX=legendX, legendY=legendY, offset=offset, opacity=opacity,
                                     orient=orient, padding=padding, rowPadding=rowPadding, shape=shape,
                                     size=size, stroke=stroke, strokeColor=strokeColor,
                                     strokeDash=strokeDash, strokeWidth=strokeWidth,
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


class compare(VegaSchema):
    """compare schema wrapper

    oneOf(Mapping(required=[]), Mapping(required=[]))
    """
    _schema = {'$ref': '#/definitions/compare'}

    def __init__(self, *args, **kwds):
        super(compare, self).__init__(*args, **kwds)


class from_(VegaSchema):
    """from_ schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    data : string

    """
    _schema = {'$ref': '#/definitions/from'}

    def __init__(self, data=Undefined, **kwds):
        super(from_, self).__init__(data=data, **kwds)


class facet(VegaSchema):
    """facet schema wrapper

    Mapping(required=[facet])

    Attributes
    ----------

    facet : oneOf(Mapping(required=[name, data, field]), Mapping(required=[name, data,
    groupby]))

    data : string

    """
    _schema = {'$ref': '#/definitions/facet'}

    def __init__(self, facet=Undefined, data=Undefined, **kwds):
        super(facet, self).__init__(facet=facet, data=data, **kwds)


class mark(VegaSchema):
    """mark schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`marktype`

    aria : boolean

    clip : :class:`markclip`

    description : string

    encode : :class:`encode`

    interactive : :class:`booleanOrSignal`

    key : string

    name : string

    on : :class:`onMarkTrigger`

    role : string

    sort : :class:`compare`

    style : :class:`style`

    transform : List(:class:`transformMark`)

    """
    _schema = {'$ref': '#/definitions/mark'}

    def __init__(self, type=Undefined, aria=Undefined, clip=Undefined, description=Undefined,
                 encode=Undefined, interactive=Undefined, key=Undefined, name=Undefined, on=Undefined,
                 role=Undefined, sort=Undefined, style=Undefined, transform=Undefined, **kwds):
        super(mark, self).__init__(type=type, aria=aria, clip=clip, description=description,
                                   encode=encode, interactive=interactive, key=key, name=name, on=on,
                                   role=role, sort=sort, style=style, transform=transform, **kwds)


class markclip(VegaSchema):
    """markclip schema wrapper

    oneOf(:class:`booleanOrSignal`, Mapping(required=[path]), Mapping(required=[sphere]))
    """
    _schema = {'$ref': '#/definitions/markclip'}

    def __init__(self, *args, **kwds):
        super(markclip, self).__init__(*args, **kwds)


class markGroup(VegaSchema):
    """markGroup schema wrapper

    allOf(Mapping(required=[type]), :class:`mark`, :class:`scope`)
    """
    _schema = {'$ref': '#/definitions/markGroup'}

    def __init__(self, type=Undefined, aria=Undefined, axes=Undefined, clip=Undefined, data=Undefined,
                 description=Undefined, encode=Undefined, interactive=Undefined, key=Undefined,
                 layout=Undefined, legends=Undefined, marks=Undefined, name=Undefined, on=Undefined,
                 projections=Undefined, role=Undefined, scales=Undefined, signals=Undefined,
                 sort=Undefined, style=Undefined, title=Undefined, transform=Undefined,
                 usermeta=Undefined, **kwds):
        super(markGroup, self).__init__(type=type, aria=aria, axes=axes, clip=clip, data=data,
                                        description=description, encode=encode, interactive=interactive,
                                        key=key, layout=layout, legends=legends, marks=marks, name=name,
                                        on=on, projections=projections, role=role, scales=scales,
                                        signals=signals, sort=sort, style=style, title=title,
                                        transform=transform, usermeta=usermeta, **kwds)


class markVisual(VegaSchema):
    """markVisual schema wrapper

    allOf(Mapping(required=[]), :class:`mark`)
    """
    _schema = {'$ref': '#/definitions/markVisual'}

    def __init__(self, type=Undefined, aria=Undefined, clip=Undefined, description=Undefined,
                 encode=Undefined, interactive=Undefined, key=Undefined, name=Undefined, on=Undefined,
                 role=Undefined, sort=Undefined, style=Undefined, transform=Undefined, **kwds):
        super(markVisual, self).__init__(type=type, aria=aria, clip=clip, description=description,
                                         encode=encode, interactive=interactive, key=key, name=name,
                                         on=on, role=role, sort=sort, style=style, transform=transform,
                                         **kwds)


class style(VegaSchema):
    """style schema wrapper

    oneOf(string, List(string))
    """
    _schema = {'$ref': '#/definitions/style'}

    def __init__(self, *args, **kwds):
        super(style, self).__init__(*args, **kwds)


class marktype(VegaSchema):
    """marktype schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/marktype'}

    def __init__(self, *args):
        super(marktype, self).__init__(*args)


class listener(VegaSchema):
    """listener schema wrapper

    oneOf(:class:`signalRef`, Mapping(required=[scale]), :class:`stream`)
    """
    _schema = {'$ref': '#/definitions/listener'}

    def __init__(self, *args, **kwds):
        super(listener, self).__init__(*args, **kwds)


class onEvents(VegaSchema):
    """onEvents schema wrapper

    List(allOf(Mapping(required=[events]), oneOf(Mapping(required=[encode]),
    Mapping(required=[update]))))
    """
    _schema = {'$ref': '#/definitions/onEvents'}

    def __init__(self, *args):
        super(onEvents, self).__init__(*args)


class onTrigger(VegaSchema):
    """onTrigger schema wrapper

    List(Mapping(required=[trigger]))
    """
    _schema = {'$ref': '#/definitions/onTrigger'}

    def __init__(self, *args):
        super(onTrigger, self).__init__(*args)


class onMarkTrigger(VegaSchema):
    """onMarkTrigger schema wrapper

    List(Mapping(required=[trigger]))
    """
    _schema = {'$ref': '#/definitions/onMarkTrigger'}

    def __init__(self, *args):
        super(onMarkTrigger, self).__init__(*args)


class padding(VegaSchema):
    """padding schema wrapper

    oneOf(float, Mapping(required=[]), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/padding'}

    def __init__(self, *args, **kwds):
        super(padding, self).__init__(*args, **kwds)


class projection(VegaSchema):
    """projection schema wrapper

    Mapping(required=[name])

    Attributes
    ----------

    name : string

    center : oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)

    clipAngle : :class:`numberOrSignal`

    clipExtent : oneOf(List(oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)),
    :class:`signalRef`)

    extent : oneOf(List(oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)),
    :class:`signalRef`)

    fit : oneOf(Mapping(required=[]), List(Any))

    parallels : oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)

    pointRadius : :class:`numberOrSignal`

    precision : :class:`numberOrSignal`

    rotate : oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)

    scale : :class:`numberOrSignal`

    size : oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)

    translate : oneOf(List(:class:`numberOrSignal`), :class:`signalRef`)

    type : :class:`stringOrSignal`

    """
    _schema = {'$ref': '#/definitions/projection'}

    def __init__(self, name=Undefined, center=Undefined, clipAngle=Undefined, clipExtent=Undefined,
                 extent=Undefined, fit=Undefined, parallels=Undefined, pointRadius=Undefined,
                 precision=Undefined, rotate=Undefined, scale=Undefined, size=Undefined,
                 translate=Undefined, type=Undefined, **kwds):
        super(projection, self).__init__(name=name, center=center, clipAngle=clipAngle,
                                         clipExtent=clipExtent, extent=extent, fit=fit,
                                         parallels=parallels, pointRadius=pointRadius,
                                         precision=precision, rotate=rotate, scale=scale, size=size,
                                         translate=translate, type=type, **kwds)


class scale(VegaSchema):
    """scale schema wrapper

    oneOf(Mapping(required=[type, name]), Mapping(required=[type, name]),
    Mapping(required=[type, name]), Mapping(required=[type, name]), Mapping(required=[type,
    name]), Mapping(required=[type, name]), Mapping(required=[type, name]),
    Mapping(required=[type, name]), Mapping(required=[name]), Mapping(required=[type, name]),
    Mapping(required=[type, name]), Mapping(required=[type, name]))
    """
    _schema = {'$ref': '#/definitions/scale'}

    def __init__(self, *args, **kwds):
        super(scale, self).__init__(*args, **kwds)


class scaleField(VegaSchema):
    """scaleField schema wrapper

    oneOf(string, :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/scaleField'}

    def __init__(self, *args, **kwds):
        super(scaleField, self).__init__(*args, **kwds)


class sortOrder(VegaSchema):
    """sortOrder schema wrapper

    oneOf(enum('ascending', 'descending'), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/sortOrder'}

    def __init__(self, *args, **kwds):
        super(sortOrder, self).__init__(*args, **kwds)


class scaleBins(VegaSchema):
    """scaleBins schema wrapper

    oneOf(List(:class:`numberOrSignal`), Mapping(required=[step]), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/scaleBins'}

    def __init__(self, *args, **kwds):
        super(scaleBins, self).__init__(*args, **kwds)


class scaleInterpolate(VegaSchema):
    """scaleInterpolate schema wrapper

    oneOf(string, :class:`signalRef`, Mapping(required=[type]))
    """
    _schema = {'$ref': '#/definitions/scaleInterpolate'}

    def __init__(self, *args, **kwds):
        super(scaleInterpolate, self).__init__(*args, **kwds)


class scaleData(VegaSchema):
    """scaleData schema wrapper

    oneOf(Mapping(required=[data, field]), Mapping(required=[data, fields]),
    Mapping(required=[fields]))
    """
    _schema = {'$ref': '#/definitions/scaleData'}

    def __init__(self, *args, **kwds):
        super(scaleData, self).__init__(*args, **kwds)


class scope(VegaSchema):
    """scope schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    axes : List(:class:`axis`)

    data : List(:class:`data`)

    encode : :class:`encode`

    layout : :class:`layout`

    legends : List(:class:`legend`)

    marks : List(oneOf(:class:`markGroup`, :class:`markVisual`))

    projections : List(:class:`projection`)

    scales : List(:class:`scale`)

    signals : List(:class:`signal`)

    title : :class:`title`

    usermeta : Mapping(required=[])

    """
    _schema = {'$ref': '#/definitions/scope'}

    def __init__(self, axes=Undefined, data=Undefined, encode=Undefined, layout=Undefined,
                 legends=Undefined, marks=Undefined, projections=Undefined, scales=Undefined,
                 signals=Undefined, title=Undefined, usermeta=Undefined, **kwds):
        super(scope, self).__init__(axes=axes, data=data, encode=encode, layout=layout, legends=legends,
                                    marks=marks, projections=projections, scales=scales,
                                    signals=signals, title=title, usermeta=usermeta, **kwds)


class selector(VegaSchema):
    """selector schema wrapper

    string
    """
    _schema = {'$ref': '#/definitions/selector'}

    def __init__(self, *args):
        super(selector, self).__init__(*args)


class signal(VegaSchema):
    """signal schema wrapper

    oneOf(Mapping(required=[name, push]), Mapping(required=[name]), Mapping(required=[name,
    init]))
    """
    _schema = {'$ref': '#/definitions/signal'}

    def __init__(self, *args, **kwds):
        super(signal, self).__init__(*args, **kwds)


class signalName(VegaSchema):
    """signalName schema wrapper

    not enum('parent', 'datum', 'event', 'item')
    """
    _schema = {'$ref': '#/definitions/signalName'}

    def __init__(self, *args):
        super(signalName, self).__init__(*args)


class signalRef(VegaSchema):
    """signalRef schema wrapper

    Mapping(required=[signal])

    Attributes
    ----------

    signal : string

    """
    _schema = {'$ref': '#/definitions/signalRef'}

    def __init__(self, signal=Undefined, **kwds):
        super(signalRef, self).__init__(signal=signal, **kwds)


class arrayOrSignal(VegaSchema):
    """arrayOrSignal schema wrapper

    oneOf(List(Any), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/arrayOrSignal'}

    def __init__(self, *args, **kwds):
        super(arrayOrSignal, self).__init__(*args, **kwds)


class booleanOrSignal(VegaSchema):
    """booleanOrSignal schema wrapper

    oneOf(boolean, :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/booleanOrSignal'}

    def __init__(self, *args, **kwds):
        super(booleanOrSignal, self).__init__(*args, **kwds)


class numberOrSignal(VegaSchema):
    """numberOrSignal schema wrapper

    oneOf(float, :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/numberOrSignal'}

    def __init__(self, *args, **kwds):
        super(numberOrSignal, self).__init__(*args, **kwds)


class stringOrSignal(VegaSchema):
    """stringOrSignal schema wrapper

    oneOf(string, :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/stringOrSignal'}

    def __init__(self, *args, **kwds):
        super(stringOrSignal, self).__init__(*args, **kwds)


class textOrSignal(VegaSchema):
    """textOrSignal schema wrapper

    oneOf(oneOf(string, List(string)), :class:`signalRef`)
    """
    _schema = {'$ref': '#/definitions/textOrSignal'}

    def __init__(self, *args, **kwds):
        super(textOrSignal, self).__init__(*args, **kwds)


class stream(VegaSchema):
    """stream schema wrapper

    allOf(Mapping(required=[]), oneOf(Mapping(required=[type]), Mapping(required=[stream]),
    Mapping(required=[merge])))
    """
    _schema = {'$ref': '#/definitions/stream'}

    def __init__(self, between=Undefined, consume=Undefined, debounce=Undefined, filter=Undefined,
                 markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(stream, self).__init__(between=between, consume=consume, debounce=debounce, filter=filter,
                                     markname=markname, marktype=marktype, throttle=throttle, **kwds)


class title(VegaSchema):
    """title schema wrapper

    oneOf(string, Mapping(required=[]))
    """
    _schema = {'$ref': '#/definitions/title'}

    def __init__(self, *args, **kwds):
        super(title, self).__init__(*args, **kwds)


class transform(VegaSchema):
    """transform schema wrapper

    oneOf(:class:`crossfilterTransform`, :class:`resolvefilterTransform`,
    :class:`linkpathTransform`, :class:`pieTransform`, :class:`stackTransform`,
    :class:`forceTransform`, :class:`contourTransform`, :class:`geojsonTransform`,
    :class:`geopathTransform`, :class:`geopointTransform`, :class:`geoshapeTransform`,
    :class:`graticuleTransform`, :class:`heatmapTransform`, :class:`isocontourTransform`,
    :class:`kde2dTransform`, :class:`nestTransform`, :class:`packTransform`,
    :class:`partitionTransform`, :class:`stratifyTransform`, :class:`treeTransform`,
    :class:`treelinksTransform`, :class:`treemapTransform`, :class:`labelTransform`,
    :class:`loessTransform`, :class:`regressionTransform`, :class:`aggregateTransform`,
    :class:`binTransform`, :class:`collectTransform`, :class:`countpatternTransform`,
    :class:`crossTransform`, :class:`densityTransform`, :class:`dotbinTransform`,
    :class:`extentTransform`, :class:`filterTransform`, :class:`flattenTransform`,
    :class:`foldTransform`, :class:`formulaTransform`, :class:`imputeTransform`,
    :class:`joinaggregateTransform`, :class:`kdeTransform`, :class:`lookupTransform`,
    :class:`pivotTransform`, :class:`projectTransform`, :class:`quantileTransform`,
    :class:`sampleTransform`, :class:`sequenceTransform`, :class:`timeunitTransform`,
    :class:`windowTransform`, :class:`identifierTransform`, :class:`voronoiTransform`,
    :class:`wordcloudTransform`)
    """
    _schema = {'$ref': '#/definitions/transform'}

    def __init__(self, *args, **kwds):
        super(transform, self).__init__(*args, **kwds)


class transformMark(VegaSchema):
    """transformMark schema wrapper

    oneOf(:class:`crossfilterTransform`, :class:`resolvefilterTransform`,
    :class:`linkpathTransform`, :class:`pieTransform`, :class:`stackTransform`,
    :class:`forceTransform`, :class:`geojsonTransform`, :class:`geopathTransform`,
    :class:`geopointTransform`, :class:`geoshapeTransform`, :class:`heatmapTransform`,
    :class:`packTransform`, :class:`partitionTransform`, :class:`stratifyTransform`,
    :class:`treeTransform`, :class:`treemapTransform`, :class:`labelTransform`,
    :class:`binTransform`, :class:`collectTransform`, :class:`dotbinTransform`,
    :class:`extentTransform`, :class:`formulaTransform`, :class:`joinaggregateTransform`,
    :class:`lookupTransform`, :class:`sampleTransform`, :class:`timeunitTransform`,
    :class:`windowTransform`, :class:`identifierTransform`, :class:`voronoiTransform`,
    :class:`wordcloudTransform`)
    """
    _schema = {'$ref': '#/definitions/transformMark'}

    def __init__(self, *args, **kwds):
        super(transformMark, self).__init__(*args, **kwds)


class crossfilterTransform(VegaSchema):
    """crossfilterTransform schema wrapper

    Mapping(required=[type, fields, query])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    query : oneOf(List(Any), :class:`signalRef`)

    type : enum('crossfilter')

    signal : string

    """
    _schema = {'$ref': '#/definitions/crossfilterTransform'}

    def __init__(self, fields=Undefined, query=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(crossfilterTransform, self).__init__(fields=fields, query=query, type=type, signal=signal,
                                                   **kwds)


class resolvefilterTransform(VegaSchema):
    """resolvefilterTransform schema wrapper

    Mapping(required=[type, ignore, filter])

    Attributes
    ----------

    filter : Any

    ignore : anyOf(float, :class:`signalRef`)

    type : enum('resolvefilter')

    signal : string

    """
    _schema = {'$ref': '#/definitions/resolvefilterTransform'}

    def __init__(self, filter=Undefined, ignore=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(resolvefilterTransform, self).__init__(filter=filter, ignore=ignore, type=type,
                                                     signal=signal, **kwds)


class linkpathTransform(VegaSchema):
    """linkpathTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('linkpath')

    orient : anyOf(enum('horizontal', 'vertical', 'radial'), :class:`signalRef`)

    require : :class:`signalRef`

    shape : anyOf(enum('line', 'arc', 'curve', 'diagonal', 'orthogonal'), :class:`signalRef`)

    signal : string

    sourceX : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    sourceY : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    targetX : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    targetY : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/linkpathTransform'}

    def __init__(self, type=Undefined, orient=Undefined, require=Undefined, shape=Undefined,
                 signal=Undefined, sourceX=Undefined, sourceY=Undefined, targetX=Undefined,
                 targetY=Undefined, **kwds):
        super(linkpathTransform, self).__init__(type=type, orient=orient, require=require, shape=shape,
                                                signal=signal, sourceX=sourceX, sourceY=sourceY,
                                                targetX=targetX, targetY=targetY, **kwds)


class pieTransform(VegaSchema):
    """pieTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('pie')

    endAngle : anyOf(float, :class:`signalRef`)

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    sort : anyOf(boolean, :class:`signalRef`)

    startAngle : anyOf(float, :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/pieTransform'}

    def __init__(self, type=Undefined, endAngle=Undefined, field=Undefined, signal=Undefined,
                 sort=Undefined, startAngle=Undefined, **kwds):
        super(pieTransform, self).__init__(type=type, endAngle=endAngle, field=field, signal=signal,
                                           sort=sort, startAngle=startAngle, **kwds)


class stackTransform(VegaSchema):
    """stackTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('stack')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    offset : anyOf(enum('zero', 'center', 'normalize'), :class:`signalRef`)

    signal : string

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/stackTransform'}

    def __init__(self, type=Undefined, field=Undefined, groupby=Undefined, offset=Undefined,
                 signal=Undefined, sort=Undefined, **kwds):
        super(stackTransform, self).__init__(type=type, field=field, groupby=groupby, offset=offset,
                                             signal=signal, sort=sort, **kwds)


class forceTransform(VegaSchema):
    """forceTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('force')

    alpha : anyOf(float, :class:`signalRef`)

    alphaMin : anyOf(float, :class:`signalRef`)

    alphaTarget : anyOf(float, :class:`signalRef`)

    forces : List(oneOf(Mapping(required=[force]), Mapping(required=[force]),
    Mapping(required=[force]), Mapping(required=[force]), Mapping(required=[force]),
    Mapping(required=[force])))

    iterations : anyOf(float, :class:`signalRef`)

    restart : anyOf(boolean, :class:`signalRef`)

    signal : string

    static : anyOf(boolean, :class:`signalRef`)

    velocityDecay : anyOf(float, :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/forceTransform'}

    def __init__(self, type=Undefined, alpha=Undefined, alphaMin=Undefined, alphaTarget=Undefined,
                 forces=Undefined, iterations=Undefined, restart=Undefined, signal=Undefined,
                 static=Undefined, velocityDecay=Undefined, **kwds):
        super(forceTransform, self).__init__(type=type, alpha=alpha, alphaMin=alphaMin,
                                             alphaTarget=alphaTarget, forces=forces,
                                             iterations=iterations, restart=restart, signal=signal,
                                             static=static, velocityDecay=velocityDecay, **kwds)


class contourTransform(VegaSchema):
    """contourTransform schema wrapper

    Mapping(required=[type, size])

    Attributes
    ----------

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    type : enum('contour')

    bandwidth : anyOf(float, :class:`signalRef`)

    cellSize : anyOf(float, :class:`signalRef`)

    count : anyOf(float, :class:`signalRef`)

    nice : anyOf(boolean, :class:`signalRef`)

    signal : string

    smooth : anyOf(boolean, :class:`signalRef`)

    thresholds : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    values : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    weight : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    """
    _schema = {'$ref': '#/definitions/contourTransform'}

    def __init__(self, size=Undefined, type=Undefined, bandwidth=Undefined, cellSize=Undefined,
                 count=Undefined, nice=Undefined, signal=Undefined, smooth=Undefined,
                 thresholds=Undefined, values=Undefined, weight=Undefined, x=Undefined, y=Undefined,
                 **kwds):
        super(contourTransform, self).__init__(size=size, type=type, bandwidth=bandwidth,
                                               cellSize=cellSize, count=count, nice=nice, signal=signal,
                                               smooth=smooth, thresholds=thresholds, values=values,
                                               weight=weight, x=x, y=y, **kwds)


class geojsonTransform(VegaSchema):
    """geojsonTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('geojson')

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    geojson : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    """
    _schema = {'$ref': '#/definitions/geojsonTransform'}

    def __init__(self, type=Undefined, fields=Undefined, geojson=Undefined, signal=Undefined, **kwds):
        super(geojsonTransform, self).__init__(type=type, fields=fields, geojson=geojson, signal=signal,
                                               **kwds)


class geopathTransform(VegaSchema):
    """geopathTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('geopath')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    pointRadius : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    projection : string

    signal : string

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/geopathTransform'}

    def __init__(self, type=Undefined, field=Undefined, pointRadius=Undefined, projection=Undefined,
                 signal=Undefined, **kwds):
        super(geopathTransform, self).__init__(type=type, field=field, pointRadius=pointRadius,
                                               projection=projection, signal=signal, **kwds)


class geopointTransform(VegaSchema):
    """geopointTransform schema wrapper

    Mapping(required=[type, projection, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    projection : string

    type : enum('geopoint')

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/geopointTransform'}

    def __init__(self, fields=Undefined, projection=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(geopointTransform, self).__init__(fields=fields, projection=projection, type=type,
                                                signal=signal, **kwds)


class geoshapeTransform(VegaSchema):
    """geoshapeTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('geoshape')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    pointRadius : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    projection : string

    signal : string

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/geoshapeTransform'}

    def __init__(self, type=Undefined, field=Undefined, pointRadius=Undefined, projection=Undefined,
                 signal=Undefined, **kwds):
        super(geoshapeTransform, self).__init__(type=type, field=field, pointRadius=pointRadius,
                                                projection=projection, signal=signal, **kwds)


class graticuleTransform(VegaSchema):
    """graticuleTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('graticule')

    extent : oneOf(List(Any), :class:`signalRef`)

    extentMajor : oneOf(List(Any), :class:`signalRef`)

    extentMinor : oneOf(List(Any), :class:`signalRef`)

    precision : anyOf(float, :class:`signalRef`)

    signal : string

    step : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    stepMajor : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    stepMinor : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/graticuleTransform'}

    def __init__(self, type=Undefined, extent=Undefined, extentMajor=Undefined, extentMinor=Undefined,
                 precision=Undefined, signal=Undefined, step=Undefined, stepMajor=Undefined,
                 stepMinor=Undefined, **kwds):
        super(graticuleTransform, self).__init__(type=type, extent=extent, extentMajor=extentMajor,
                                                 extentMinor=extentMinor, precision=precision,
                                                 signal=signal, step=step, stepMajor=stepMajor,
                                                 stepMinor=stepMinor, **kwds)


class heatmapTransform(VegaSchema):
    """heatmapTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('heatmap')

    color : anyOf(string, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    opacity : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    resolve : anyOf(enum('shared', 'independent'), :class:`signalRef`)

    signal : string

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/heatmapTransform'}

    def __init__(self, type=Undefined, color=Undefined, field=Undefined, opacity=Undefined,
                 resolve=Undefined, signal=Undefined, **kwds):
        super(heatmapTransform, self).__init__(type=type, color=color, field=field, opacity=opacity,
                                               resolve=resolve, signal=signal, **kwds)


class isocontourTransform(VegaSchema):
    """isocontourTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('isocontour')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    levels : anyOf(float, :class:`signalRef`)

    nice : anyOf(boolean, :class:`signalRef`)

    resolve : anyOf(enum('shared', 'independent'), :class:`signalRef`)

    scale : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    signal : string

    smooth : anyOf(boolean, :class:`signalRef`)

    thresholds : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    translate : oneOf(List(anyOf(float, :class:`signalRef`, :class:`expr`,
    :class:`paramField`)), :class:`signalRef`)

    zero : anyOf(boolean, :class:`signalRef`)

    as : anyOf(string, :class:`signalRef`, None)

    """
    _schema = {'$ref': '#/definitions/isocontourTransform'}

    def __init__(self, type=Undefined, field=Undefined, levels=Undefined, nice=Undefined,
                 resolve=Undefined, scale=Undefined, signal=Undefined, smooth=Undefined,
                 thresholds=Undefined, translate=Undefined, zero=Undefined, **kwds):
        super(isocontourTransform, self).__init__(type=type, field=field, levels=levels, nice=nice,
                                                  resolve=resolve, scale=scale, signal=signal,
                                                  smooth=smooth, thresholds=thresholds,
                                                  translate=translate, zero=zero, **kwds)


class kde2dTransform(VegaSchema):
    """kde2dTransform schema wrapper

    Mapping(required=[type, size, x, y])

    Attributes
    ----------

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    type : enum('kde2d')

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    bandwidth : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    cellSize : anyOf(float, :class:`signalRef`)

    counts : anyOf(boolean, :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    signal : string

    weight : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/kde2dTransform'}

    def __init__(self, size=Undefined, type=Undefined, x=Undefined, y=Undefined, bandwidth=Undefined,
                 cellSize=Undefined, counts=Undefined, groupby=Undefined, signal=Undefined,
                 weight=Undefined, **kwds):
        super(kde2dTransform, self).__init__(size=size, type=type, x=x, y=y, bandwidth=bandwidth,
                                             cellSize=cellSize, counts=counts, groupby=groupby,
                                             signal=signal, weight=weight, **kwds)


class nestTransform(VegaSchema):
    """nestTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('nest')

    generate : anyOf(boolean, :class:`signalRef`)

    keys : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    signal : string

    """
    _schema = {'$ref': '#/definitions/nestTransform'}

    def __init__(self, type=Undefined, generate=Undefined, keys=Undefined, signal=Undefined, **kwds):
        super(nestTransform, self).__init__(type=type, generate=generate, keys=keys, signal=signal,
                                            **kwds)


class packTransform(VegaSchema):
    """packTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('pack')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    padding : anyOf(float, :class:`signalRef`)

    radius : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/packTransform'}

    def __init__(self, type=Undefined, field=Undefined, padding=Undefined, radius=Undefined,
                 signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(packTransform, self).__init__(type=type, field=field, padding=padding, radius=radius,
                                            signal=signal, size=size, sort=sort, **kwds)


class partitionTransform(VegaSchema):
    """partitionTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('partition')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    padding : anyOf(float, :class:`signalRef`)

    round : anyOf(boolean, :class:`signalRef`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/partitionTransform'}

    def __init__(self, type=Undefined, field=Undefined, padding=Undefined, round=Undefined,
                 signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(partitionTransform, self).__init__(type=type, field=field, padding=padding, round=round,
                                                 signal=signal, size=size, sort=sort, **kwds)


class stratifyTransform(VegaSchema):
    """stratifyTransform schema wrapper

    Mapping(required=[type, key, parentKey])

    Attributes
    ----------

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    parentKey : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('stratify')

    signal : string

    """
    _schema = {'$ref': '#/definitions/stratifyTransform'}

    def __init__(self, key=Undefined, parentKey=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(stratifyTransform, self).__init__(key=key, parentKey=parentKey, type=type, signal=signal,
                                                **kwds)


class treeTransform(VegaSchema):
    """treeTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('tree')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    method : anyOf(enum('tidy', 'cluster'), :class:`signalRef`)

    nodeSize : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    separation : anyOf(boolean, :class:`signalRef`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/treeTransform'}

    def __init__(self, type=Undefined, field=Undefined, method=Undefined, nodeSize=Undefined,
                 separation=Undefined, signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(treeTransform, self).__init__(type=type, field=field, method=method, nodeSize=nodeSize,
                                            separation=separation, signal=signal, size=size, sort=sort,
                                            **kwds)


class treelinksTransform(VegaSchema):
    """treelinksTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('treelinks')

    signal : string

    """
    _schema = {'$ref': '#/definitions/treelinksTransform'}

    def __init__(self, type=Undefined, signal=Undefined, **kwds):
        super(treelinksTransform, self).__init__(type=type, signal=signal, **kwds)


class treemapTransform(VegaSchema):
    """treemapTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('treemap')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    method : anyOf(enum('squarify', 'resquarify', 'binary', 'dice', 'slice', 'slicedice'),
    :class:`signalRef`)

    padding : anyOf(float, :class:`signalRef`)

    paddingBottom : anyOf(float, :class:`signalRef`)

    paddingInner : anyOf(float, :class:`signalRef`)

    paddingLeft : anyOf(float, :class:`signalRef`)

    paddingOuter : anyOf(float, :class:`signalRef`)

    paddingRight : anyOf(float, :class:`signalRef`)

    paddingTop : anyOf(float, :class:`signalRef`)

    ratio : anyOf(float, :class:`signalRef`)

    round : anyOf(boolean, :class:`signalRef`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/treemapTransform'}

    def __init__(self, type=Undefined, field=Undefined, method=Undefined, padding=Undefined,
                 paddingBottom=Undefined, paddingInner=Undefined, paddingLeft=Undefined,
                 paddingOuter=Undefined, paddingRight=Undefined, paddingTop=Undefined, ratio=Undefined,
                 round=Undefined, signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(treemapTransform, self).__init__(type=type, field=field, method=method, padding=padding,
                                               paddingBottom=paddingBottom, paddingInner=paddingInner,
                                               paddingLeft=paddingLeft, paddingOuter=paddingOuter,
                                               paddingRight=paddingRight, paddingTop=paddingTop,
                                               ratio=ratio, round=round, signal=signal, size=size,
                                               sort=sort, **kwds)


class labelTransform(VegaSchema):
    """labelTransform schema wrapper

    Mapping(required=[type, size])

    Attributes
    ----------

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    type : enum('label')

    anchor : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    avoidBaseMark : anyOf(boolean, :class:`signalRef`)

    avoidMarks : oneOf(List(string), :class:`signalRef`)

    lineAnchor : anyOf(string, :class:`signalRef`)

    markIndex : anyOf(float, :class:`signalRef`)

    method : anyOf(string, :class:`signalRef`)

    offset : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    padding : anyOf(float, :class:`signalRef`, None)

    signal : string

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/labelTransform'}

    def __init__(self, size=Undefined, type=Undefined, anchor=Undefined, avoidBaseMark=Undefined,
                 avoidMarks=Undefined, lineAnchor=Undefined, markIndex=Undefined, method=Undefined,
                 offset=Undefined, padding=Undefined, signal=Undefined, sort=Undefined, **kwds):
        super(labelTransform, self).__init__(size=size, type=type, anchor=anchor,
                                             avoidBaseMark=avoidBaseMark, avoidMarks=avoidMarks,
                                             lineAnchor=lineAnchor, markIndex=markIndex, method=method,
                                             offset=offset, padding=padding, signal=signal, sort=sort,
                                             **kwds)


class loessTransform(VegaSchema):
    """loessTransform schema wrapper

    Mapping(required=[type, x, y])

    Attributes
    ----------

    type : enum('loess')

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    bandwidth : anyOf(float, :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/loessTransform'}

    def __init__(self, type=Undefined, x=Undefined, y=Undefined, bandwidth=Undefined, groupby=Undefined,
                 signal=Undefined, **kwds):
        super(loessTransform, self).__init__(type=type, x=x, y=y, bandwidth=bandwidth, groupby=groupby,
                                             signal=signal, **kwds)


class regressionTransform(VegaSchema):
    """regressionTransform schema wrapper

    Mapping(required=[type, x, y])

    Attributes
    ----------

    type : enum('regression')

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    extent : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    method : anyOf(string, :class:`signalRef`)

    order : anyOf(float, :class:`signalRef`)

    params : anyOf(boolean, :class:`signalRef`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/regressionTransform'}

    def __init__(self, type=Undefined, x=Undefined, y=Undefined, extent=Undefined, groupby=Undefined,
                 method=Undefined, order=Undefined, params=Undefined, signal=Undefined, **kwds):
        super(regressionTransform, self).__init__(type=type, x=x, y=y, extent=extent, groupby=groupby,
                                                  method=method, order=order, params=params,
                                                  signal=signal, **kwds)


class aggregateTransform(VegaSchema):
    """aggregateTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('aggregate')

    cross : anyOf(boolean, :class:`signalRef`)

    drop : anyOf(boolean, :class:`signalRef`)

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`, None)),
    :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    ops : oneOf(List(anyOf(enum('values', 'count', '__count__', 'missing', 'valid', 'sum',
    'product', 'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr',
    'distinct', 'ci0', 'ci1', 'median', 'q1', 'q3', 'min', 'max', 'argmin', 'argmax'),
    :class:`signalRef`)), :class:`signalRef`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`, None)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/aggregateTransform'}

    def __init__(self, type=Undefined, cross=Undefined, drop=Undefined, fields=Undefined,
                 groupby=Undefined, key=Undefined, ops=Undefined, signal=Undefined, **kwds):
        super(aggregateTransform, self).__init__(type=type, cross=cross, drop=drop, fields=fields,
                                                 groupby=groupby, key=key, ops=ops, signal=signal,
                                                 **kwds)


class binTransform(VegaSchema):
    """binTransform schema wrapper

    Mapping(required=[type, field, extent])

    Attributes
    ----------

    extent : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('bin')

    anchor : anyOf(float, :class:`signalRef`)

    base : anyOf(float, :class:`signalRef`)

    divide : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    interval : anyOf(boolean, :class:`signalRef`)

    maxbins : anyOf(float, :class:`signalRef`)

    minstep : anyOf(float, :class:`signalRef`)

    name : anyOf(string, :class:`signalRef`)

    nice : anyOf(boolean, :class:`signalRef`)

    signal : string

    span : anyOf(float, :class:`signalRef`)

    step : anyOf(float, :class:`signalRef`)

    steps : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/binTransform'}

    def __init__(self, extent=Undefined, field=Undefined, type=Undefined, anchor=Undefined,
                 base=Undefined, divide=Undefined, interval=Undefined, maxbins=Undefined,
                 minstep=Undefined, name=Undefined, nice=Undefined, signal=Undefined, span=Undefined,
                 step=Undefined, steps=Undefined, **kwds):
        super(binTransform, self).__init__(extent=extent, field=field, type=type, anchor=anchor,
                                           base=base, divide=divide, interval=interval, maxbins=maxbins,
                                           minstep=minstep, name=name, nice=nice, signal=signal,
                                           span=span, step=step, steps=steps, **kwds)


class collectTransform(VegaSchema):
    """collectTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('collect')

    signal : string

    sort : :class:`compare`

    """
    _schema = {'$ref': '#/definitions/collectTransform'}

    def __init__(self, type=Undefined, signal=Undefined, sort=Undefined, **kwds):
        super(collectTransform, self).__init__(type=type, signal=signal, sort=sort, **kwds)


class countpatternTransform(VegaSchema):
    """countpatternTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('countpattern')

    case : anyOf(enum('upper', 'lower', 'mixed'), :class:`signalRef`)

    pattern : anyOf(string, :class:`signalRef`)

    signal : string

    stopwords : anyOf(string, :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/countpatternTransform'}

    def __init__(self, field=Undefined, type=Undefined, case=Undefined, pattern=Undefined,
                 signal=Undefined, stopwords=Undefined, **kwds):
        super(countpatternTransform, self).__init__(field=field, type=type, case=case, pattern=pattern,
                                                    signal=signal, stopwords=stopwords, **kwds)


class crossTransform(VegaSchema):
    """crossTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('cross')

    filter : :class:`exprString`

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/crossTransform'}

    def __init__(self, type=Undefined, filter=Undefined, signal=Undefined, **kwds):
        super(crossTransform, self).__init__(type=type, filter=filter, signal=signal, **kwds)


class densityTransform(VegaSchema):
    """densityTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('density')

    distribution : oneOf(Mapping(required=[function]), Mapping(required=[function]),
    Mapping(required=[function]), Mapping(required=[function, field]),
    Mapping(required=[function]))

    extent : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    maxsteps : anyOf(float, :class:`signalRef`)

    method : anyOf(string, :class:`signalRef`)

    minsteps : anyOf(float, :class:`signalRef`)

    signal : string

    steps : anyOf(float, :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/densityTransform'}

    def __init__(self, type=Undefined, distribution=Undefined, extent=Undefined, maxsteps=Undefined,
                 method=Undefined, minsteps=Undefined, signal=Undefined, steps=Undefined, **kwds):
        super(densityTransform, self).__init__(type=type, distribution=distribution, extent=extent,
                                               maxsteps=maxsteps, method=method, minsteps=minsteps,
                                               signal=signal, steps=steps, **kwds)


class dotbinTransform(VegaSchema):
    """dotbinTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('dotbin')

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    signal : string

    smooth : anyOf(boolean, :class:`signalRef`)

    step : anyOf(float, :class:`signalRef`)

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/dotbinTransform'}

    def __init__(self, field=Undefined, type=Undefined, groupby=Undefined, signal=Undefined,
                 smooth=Undefined, step=Undefined, **kwds):
        super(dotbinTransform, self).__init__(field=field, type=type, groupby=groupby, signal=signal,
                                              smooth=smooth, step=step, **kwds)


class extentTransform(VegaSchema):
    """extentTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('extent')

    signal : string

    """
    _schema = {'$ref': '#/definitions/extentTransform'}

    def __init__(self, field=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(extentTransform, self).__init__(field=field, type=type, signal=signal, **kwds)


class filterTransform(VegaSchema):
    """filterTransform schema wrapper

    Mapping(required=[type, expr])

    Attributes
    ----------

    expr : :class:`exprString`

    type : enum('filter')

    signal : string

    """
    _schema = {'$ref': '#/definitions/filterTransform'}

    def __init__(self, expr=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(filterTransform, self).__init__(expr=expr, type=type, signal=signal, **kwds)


class flattenTransform(VegaSchema):
    """flattenTransform schema wrapper

    Mapping(required=[type, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    type : enum('flatten')

    index : anyOf(string, :class:`signalRef`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/flattenTransform'}

    def __init__(self, fields=Undefined, type=Undefined, index=Undefined, signal=Undefined, **kwds):
        super(flattenTransform, self).__init__(fields=fields, type=type, index=index, signal=signal,
                                               **kwds)


class foldTransform(VegaSchema):
    """foldTransform schema wrapper

    Mapping(required=[type, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    type : enum('fold')

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/foldTransform'}

    def __init__(self, fields=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(foldTransform, self).__init__(fields=fields, type=type, signal=signal, **kwds)


class formulaTransform(VegaSchema):
    """formulaTransform schema wrapper

    Mapping(required=[type, expr, as])

    Attributes
    ----------

    expr : :class:`exprString`

    type : enum('formula')

    initonly : anyOf(boolean, :class:`signalRef`)

    signal : string

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/formulaTransform'}

    def __init__(self, expr=Undefined, type=Undefined, initonly=Undefined, signal=Undefined, **kwds):
        super(formulaTransform, self).__init__(expr=expr, type=type, initonly=initonly, signal=signal,
                                               **kwds)


class imputeTransform(VegaSchema):
    """imputeTransform schema wrapper

    Mapping(required=[type, field, key])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('impute')

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    keyvals : oneOf(List(Any), :class:`signalRef`)

    method : anyOf(enum('value', 'mean', 'median', 'max', 'min'), :class:`signalRef`)

    signal : string

    value : Any

    """
    _schema = {'$ref': '#/definitions/imputeTransform'}

    def __init__(self, field=Undefined, key=Undefined, type=Undefined, groupby=Undefined,
                 keyvals=Undefined, method=Undefined, signal=Undefined, value=Undefined, **kwds):
        super(imputeTransform, self).__init__(field=field, key=key, type=type, groupby=groupby,
                                              keyvals=keyvals, method=method, signal=signal,
                                              value=value, **kwds)


class joinaggregateTransform(VegaSchema):
    """joinaggregateTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('joinaggregate')

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`, None)),
    :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    ops : oneOf(List(anyOf(enum('values', 'count', '__count__', 'missing', 'valid', 'sum',
    'product', 'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr',
    'distinct', 'ci0', 'ci1', 'median', 'q1', 'q3', 'min', 'max', 'argmin', 'argmax'),
    :class:`signalRef`)), :class:`signalRef`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`, None)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/joinaggregateTransform'}

    def __init__(self, type=Undefined, fields=Undefined, groupby=Undefined, key=Undefined,
                 ops=Undefined, signal=Undefined, **kwds):
        super(joinaggregateTransform, self).__init__(type=type, fields=fields, groupby=groupby, key=key,
                                                     ops=ops, signal=signal, **kwds)


class kdeTransform(VegaSchema):
    """kdeTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('kde')

    bandwidth : anyOf(float, :class:`signalRef`)

    counts : anyOf(boolean, :class:`signalRef`)

    cumulative : anyOf(boolean, :class:`signalRef`)

    extent : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    maxsteps : anyOf(float, :class:`signalRef`)

    minsteps : anyOf(float, :class:`signalRef`)

    resolve : anyOf(enum('shared', 'independent'), :class:`signalRef`)

    signal : string

    steps : anyOf(float, :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/kdeTransform'}

    def __init__(self, field=Undefined, type=Undefined, bandwidth=Undefined, counts=Undefined,
                 cumulative=Undefined, extent=Undefined, groupby=Undefined, maxsteps=Undefined,
                 minsteps=Undefined, resolve=Undefined, signal=Undefined, steps=Undefined, **kwds):
        super(kdeTransform, self).__init__(field=field, type=type, bandwidth=bandwidth, counts=counts,
                                           cumulative=cumulative, extent=extent, groupby=groupby,
                                           maxsteps=maxsteps, minsteps=minsteps, resolve=resolve,
                                           signal=signal, steps=steps, **kwds)


class lookupTransform(VegaSchema):
    """lookupTransform schema wrapper

    Mapping(required=[type, from, key, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('lookup')

    default : Any

    signal : string

    values : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    from : string

    """
    _schema = {'$ref': '#/definitions/lookupTransform'}

    def __init__(self, fields=Undefined, key=Undefined, type=Undefined, default=Undefined,
                 signal=Undefined, values=Undefined, **kwds):
        super(lookupTransform, self).__init__(fields=fields, key=key, type=type, default=default,
                                              signal=signal, values=values, **kwds)


class pivotTransform(VegaSchema):
    """pivotTransform schema wrapper

    Mapping(required=[type, field, value])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('pivot')

    value : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    limit : anyOf(float, :class:`signalRef`)

    op : anyOf(enum('values', 'count', '__count__', 'missing', 'valid', 'sum', 'product',
    'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr', 'distinct', 'ci0',
    'ci1', 'median', 'q1', 'q3', 'min', 'max', 'argmin', 'argmax'), :class:`signalRef`)

    signal : string

    """
    _schema = {'$ref': '#/definitions/pivotTransform'}

    def __init__(self, field=Undefined, type=Undefined, value=Undefined, groupby=Undefined,
                 key=Undefined, limit=Undefined, op=Undefined, signal=Undefined, **kwds):
        super(pivotTransform, self).__init__(field=field, type=type, value=value, groupby=groupby,
                                             key=key, limit=limit, op=op, signal=signal, **kwds)


class projectTransform(VegaSchema):
    """projectTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('project')

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signalRef`, None)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/projectTransform'}

    def __init__(self, type=Undefined, fields=Undefined, signal=Undefined, **kwds):
        super(projectTransform, self).__init__(type=type, fields=fields, signal=signal, **kwds)


class quantileTransform(VegaSchema):
    """quantileTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('quantile')

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    probs : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    signal : string

    step : anyOf(float, :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/quantileTransform'}

    def __init__(self, field=Undefined, type=Undefined, groupby=Undefined, probs=Undefined,
                 signal=Undefined, step=Undefined, **kwds):
        super(quantileTransform, self).__init__(field=field, type=type, groupby=groupby, probs=probs,
                                                signal=signal, step=step, **kwds)


class sampleTransform(VegaSchema):
    """sampleTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('sample')

    signal : string

    size : anyOf(float, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/sampleTransform'}

    def __init__(self, type=Undefined, signal=Undefined, size=Undefined, **kwds):
        super(sampleTransform, self).__init__(type=type, signal=signal, size=size, **kwds)


class sequenceTransform(VegaSchema):
    """sequenceTransform schema wrapper

    Mapping(required=[type, start, stop])

    Attributes
    ----------

    start : anyOf(float, :class:`signalRef`)

    stop : anyOf(float, :class:`signalRef`)

    type : enum('sequence')

    signal : string

    step : anyOf(float, :class:`signalRef`)

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/sequenceTransform'}

    def __init__(self, start=Undefined, stop=Undefined, type=Undefined, signal=Undefined,
                 step=Undefined, **kwds):
        super(sequenceTransform, self).__init__(start=start, stop=stop, type=type, signal=signal,
                                                step=step, **kwds)


class timeunitTransform(VegaSchema):
    """timeunitTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('timeunit')

    extent : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    interval : anyOf(boolean, :class:`signalRef`)

    maxbins : anyOf(float, :class:`signalRef`)

    signal : string

    step : anyOf(float, :class:`signalRef`)

    timezone : anyOf(enum('local', 'utc'), :class:`signalRef`)

    units : oneOf(List(anyOf(enum('year', 'quarter', 'month', 'week', 'date', 'day',
    'dayofyear', 'hours', 'minutes', 'seconds', 'milliseconds'), :class:`signalRef`)),
    :class:`signalRef`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/timeunitTransform'}

    def __init__(self, field=Undefined, type=Undefined, extent=Undefined, interval=Undefined,
                 maxbins=Undefined, signal=Undefined, step=Undefined, timezone=Undefined,
                 units=Undefined, **kwds):
        super(timeunitTransform, self).__init__(field=field, type=type, extent=extent,
                                                interval=interval, maxbins=maxbins, signal=signal,
                                                step=step, timezone=timezone, units=units, **kwds)


class windowTransform(VegaSchema):
    """windowTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('window')

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`, None)),
    :class:`signalRef`)

    frame : oneOf(List(anyOf(float, :class:`signalRef`, None)), :class:`signalRef`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signalRef`)

    ignorePeers : anyOf(boolean, :class:`signalRef`)

    ops : oneOf(List(anyOf(enum('row_number', 'rank', 'dense_rank', 'percent_rank', 'cume_dist',
    'ntile', 'lag', 'lead', 'first_value', 'last_value', 'nth_value', 'prev_value',
    'next_value', 'values', 'count', '__count__', 'missing', 'valid', 'sum', 'product', 'mean',
    'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr', 'distinct', 'ci0', 'ci1',
    'median', 'q1', 'q3', 'min', 'max', 'argmin', 'argmax'), :class:`signalRef`)),
    :class:`signalRef`)

    params : oneOf(List(anyOf(float, :class:`signalRef`, None)), :class:`signalRef`)

    signal : string

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signalRef`, None)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/windowTransform'}

    def __init__(self, type=Undefined, fields=Undefined, frame=Undefined, groupby=Undefined,
                 ignorePeers=Undefined, ops=Undefined, params=Undefined, signal=Undefined,
                 sort=Undefined, **kwds):
        super(windowTransform, self).__init__(type=type, fields=fields, frame=frame, groupby=groupby,
                                              ignorePeers=ignorePeers, ops=ops, params=params,
                                              signal=signal, sort=sort, **kwds)


class identifierTransform(VegaSchema):
    """identifierTransform schema wrapper

    Mapping(required=[type, as])

    Attributes
    ----------

    type : enum('identifier')

    signal : string

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/identifierTransform'}

    def __init__(self, type=Undefined, signal=Undefined, **kwds):
        super(identifierTransform, self).__init__(type=type, signal=signal, **kwds)


class voronoiTransform(VegaSchema):
    """voronoiTransform schema wrapper

    Mapping(required=[type, x, y])

    Attributes
    ----------

    type : enum('voronoi')

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    extent : oneOf(List(Any), :class:`signalRef`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    as : anyOf(string, :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/voronoiTransform'}

    def __init__(self, type=Undefined, x=Undefined, y=Undefined, extent=Undefined, signal=Undefined,
                 size=Undefined, **kwds):
        super(voronoiTransform, self).__init__(type=type, x=x, y=y, extent=extent, signal=signal,
                                               size=size, **kwds)


class wordcloudTransform(VegaSchema):
    """wordcloudTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('wordcloud')

    font : anyOf(string, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    fontSize : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    fontSizeRange : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`, None)

    fontStyle : anyOf(string, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    fontWeight : anyOf(string, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    padding : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    rotate : anyOf(float, :class:`signalRef`, :class:`expr`, :class:`paramField`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signalRef`)), :class:`signalRef`)

    spiral : anyOf(string, :class:`signalRef`)

    text : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    as : oneOf(List(anyOf(string, :class:`signalRef`)), :class:`signalRef`)

    """
    _schema = {'$ref': '#/definitions/wordcloudTransform'}

    def __init__(self, type=Undefined, font=Undefined, fontSize=Undefined, fontSizeRange=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, padding=Undefined, rotate=Undefined,
                 signal=Undefined, size=Undefined, spiral=Undefined, text=Undefined, **kwds):
        super(wordcloudTransform, self).__init__(type=type, font=font, fontSize=fontSize,
                                                 fontSizeRange=fontSizeRange, fontStyle=fontStyle,
                                                 fontWeight=fontWeight, padding=padding, rotate=rotate,
                                                 signal=signal, size=size, spiral=spiral, text=text,
                                                 **kwds)

