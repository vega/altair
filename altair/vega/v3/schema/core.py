# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import SchemaBase, Undefined

import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, 'vega-schema.json').decode('utf-8'))


class VegaSchema(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return VegaSchema.__subclasses__()


class Root(VegaSchema):
    """Root schema wrapper

    allOf(:class:`scope`, Mapping(required=[]))
    """
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, autosize=Undefined, axes=Undefined, background=Undefined, config=Undefined,
                 data=Undefined, description=Undefined, encode=Undefined, height=Undefined,
                 layout=Undefined, legends=Undefined, marks=Undefined, padding=Undefined,
                 projections=Undefined, scales=Undefined, signals=Undefined, title=Undefined,
                 usermeta=Undefined, width=Undefined, **kwds):
        super(Root, self).__init__(autosize=autosize, axes=axes, background=background, config=config,
                                   data=data, description=description, encode=encode, height=height,
                                   layout=layout, legends=legends, marks=marks, padding=padding,
                                   projections=projections, scales=scales, signals=signals, title=title,
                                   usermeta=usermeta, width=width, **kwds)


class autosize(VegaSchema):
    """autosize schema wrapper

    oneOf(enum('pad', 'fit', 'fit-x', 'fit-y', 'none'), Mapping(required=[type]))
    """
    _schema = {'$ref': '#/defs/autosize'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(autosize, self).__init__(*args, **kwds)


class axis(VegaSchema):
    """axis schema wrapper

    Mapping(required=[orient, scale])

    Attributes
    ----------

    orient : enum('top', 'bottom', 'left', 'right')

    scale : string

    domain : boolean

    encode : Mapping(required=[])

    format : :class:`stringOrSignal`

    grid : boolean

    gridScale : string

    labelBound : oneOf(boolean, float)

    labelFlush : oneOf(boolean, float)

    labelFlushOffset : float

    labelOverlap : oneOf(boolean, enum('parity', 'greedy'))

    labelPadding : float

    labels : boolean

    maxExtent : oneOf(float, :class:`numberValue`)

    minExtent : oneOf(float, :class:`numberValue`)

    offset : oneOf(float, :class:`numberValue`)

    position : oneOf(float, :class:`numberValue`)

    tickCount : :class:`tickCount`

    tickSize : float

    ticks : boolean

    title : :class:`stringOrSignal`

    titlePadding : oneOf(float, :class:`numberValue`)

    values : oneOf(List(Mapping(required=[])), :class:`signal`)

    zindex : float

    """
    _schema = {'$ref': '#/defs/axis'}
    _rootschema = Root._schema

    def __init__(self, orient=Undefined, scale=Undefined, domain=Undefined, encode=Undefined,
                 format=Undefined, grid=Undefined, gridScale=Undefined, labelBound=Undefined,
                 labelFlush=Undefined, labelFlushOffset=Undefined, labelOverlap=Undefined,
                 labelPadding=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined,
                 offset=Undefined, position=Undefined, tickCount=Undefined, tickSize=Undefined,
                 ticks=Undefined, title=Undefined, titlePadding=Undefined, values=Undefined,
                 zindex=Undefined, **kwds):
        super(axis, self).__init__(orient=orient, scale=scale, domain=domain, encode=encode,
                                   format=format, grid=grid, gridScale=gridScale, labelBound=labelBound,
                                   labelFlush=labelFlush, labelFlushOffset=labelFlushOffset,
                                   labelOverlap=labelOverlap, labelPadding=labelPadding, labels=labels,
                                   maxExtent=maxExtent, minExtent=minExtent, offset=offset,
                                   position=position, tickCount=tickCount, tickSize=tickSize,
                                   ticks=ticks, title=title, titlePadding=titlePadding, values=values,
                                   zindex=zindex, **kwds)


class background(VegaSchema):
    """background schema wrapper

    string
    """
    _schema = {'$ref': '#/defs/background'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(background, self).__init__(*args)


class bind(VegaSchema):
    """bind schema wrapper

    oneOf(Mapping(required=[input]), Mapping(required=[input, options]),
    Mapping(required=[input]), Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/bind'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(bind, self).__init__(*args, **kwds)


class dataFormat(VegaSchema):
    """dataFormat schema wrapper

    anyOf(Mapping(required=[]), Mapping(required=[]), Mapping(required=[]),
    oneOf(Mapping(required=[]), Mapping(required=[])))
    """
    _schema = {'$ref': '#/defs/dataFormat'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(dataFormat, self).__init__(*args, **kwds)


class data(VegaSchema):
    """data schema wrapper

    allOf(Mapping(required=[name]), anyOf(Mapping(required=[name]),
    oneOf(Mapping(required=[source]), Mapping(required=[values]), Mapping(required=[url]))))
    """
    _schema = {'$ref': '#/defs/data'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, on=Undefined, transform=Undefined, **kwds):
        super(data, self).__init__(name=name, on=on, transform=transform, **kwds)


class rule(VegaSchema):
    """rule schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    test : string

    """
    _schema = {'$ref': '#/defs/rule'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, **kwds):
        super(rule, self).__init__(test=test, **kwds)


class encodeEntry(VegaSchema):
    """encodeEntry schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))

    angle : :class:`numberValue`

    baseline : oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))

    clip : :class:`booleanValue`

    cursor : :class:`stringValue`

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

    opacity : :class:`numberValue`

    orient : oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))), allOf(:class:`stringModifiers`,
    anyOf(oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[range])), Mapping(required=[scale, value]), Mapping(required=[scale,
    band]), Mapping(required=[offset]))))

    outerRadius : :class:`numberValue`

    path : :class:`stringValue`

    radius : :class:`numberValue`

    shape : anyOf(string, :class:`stringValue`)

    size : :class:`numberValue`

    startAngle : :class:`numberValue`

    stroke : :class:`colorValue`

    strokeDash : :class:`arrayValue`

    strokeDashOffset : :class:`numberValue`

    strokeOpacity : :class:`numberValue`

    strokeWidth : :class:`numberValue`

    tension : :class:`numberValue`

    text : :class:`stringValue`

    theta : :class:`numberValue`

    url : :class:`stringValue`

    width : :class:`numberValue`

    x : :class:`numberValue`

    x2 : :class:`numberValue`

    xc : :class:`numberValue`

    y : :class:`numberValue`

    y2 : :class:`numberValue`

    yc : :class:`numberValue`

    """
    _schema = {'$ref': '#/defs/encodeEntry'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined,
                 cursor=Undefined, dir=Undefined, dx=Undefined, dy=Undefined, ellipsis=Undefined,
                 endAngle=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined,
                 fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, height=Undefined,
                 innerRadius=Undefined, interpolate=Undefined, limit=Undefined, opacity=Undefined,
                 orient=Undefined, outerRadius=Undefined, path=Undefined, radius=Undefined,
                 shape=Undefined, size=Undefined, startAngle=Undefined, stroke=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 url=Undefined, width=Undefined, x=Undefined, x2=Undefined, xc=Undefined, y=Undefined,
                 y2=Undefined, yc=Undefined, **kwds):
        super(encodeEntry, self).__init__(align=align, angle=angle, baseline=baseline, clip=clip,
                                          cursor=cursor, dir=dir, dx=dx, dy=dy, ellipsis=ellipsis,
                                          endAngle=endAngle, fill=fill, fillOpacity=fillOpacity,
                                          font=font, fontSize=fontSize, fontStyle=fontStyle,
                                          fontWeight=fontWeight, height=height, innerRadius=innerRadius,
                                          interpolate=interpolate, limit=limit, opacity=opacity,
                                          orient=orient, outerRadius=outerRadius, path=path,
                                          radius=radius, shape=shape, size=size, startAngle=startAngle,
                                          stroke=stroke, strokeDash=strokeDash,
                                          strokeDashOffset=strokeDashOffset,
                                          strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                          tension=tension, text=text, theta=theta, url=url, width=width,
                                          x=x, x2=x2, xc=xc, y=y, y2=y2, yc=yc, **kwds)


class encode(VegaSchema):
    """encode schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/defs/encode'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(encode, self).__init__(**kwds)


class layout(VegaSchema):
    """layout schema wrapper

    oneOf(Mapping(required=[]), :class:`signal`)
    """
    _schema = {'$ref': '#/defs/layout'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/defs/guideEncode'}
    _rootschema = Root._schema

    def __init__(self, interactive=Undefined, name=Undefined, style=Undefined, **kwds):
        super(guideEncode, self).__init__(interactive=interactive, name=name, style=style, **kwds)


class legend(VegaSchema):
    """legend schema wrapper

    anyOf(Mapping(required=[size]), Mapping(required=[shape]), Mapping(required=[fill]),
    Mapping(required=[stroke]), Mapping(required=[opacity]), Mapping(required=[strokeDash]))

    Attributes
    ----------

    """
    _schema = {'$ref': '#/defs/legend'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(legend, self).__init__(*args, **kwds)


class mark(VegaSchema):
    """mark schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : :class:`marktype`

    clip : :class:`markclip`

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
    _schema = {'$ref': '#/defs/mark'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clip=Undefined, encode=Undefined, interactive=Undefined,
                 key=Undefined, name=Undefined, on=Undefined, role=Undefined, sort=Undefined,
                 style=Undefined, transform=Undefined, **kwds):
        super(mark, self).__init__(type=type, clip=clip, encode=encode, interactive=interactive,
                                   key=key, name=name, on=on, role=role, sort=sort, style=style,
                                   transform=transform, **kwds)


class markGroup(VegaSchema):
    """markGroup schema wrapper

    allOf(Mapping(required=[type]), :class:`mark`, :class:`scope`, Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/markGroup'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, axes=Undefined, clip=Undefined, data=Undefined, encode=Undefined,
                 interactive=Undefined, key=Undefined, layout=Undefined, legends=Undefined,
                 marks=Undefined, name=Undefined, on=Undefined, projections=Undefined, role=Undefined,
                 scales=Undefined, signals=Undefined, sort=Undefined, style=Undefined, title=Undefined,
                 transform=Undefined, **kwds):
        super(markGroup, self).__init__(type=type, axes=axes, clip=clip, data=data, encode=encode,
                                        interactive=interactive, key=key, layout=layout,
                                        legends=legends, marks=marks, name=name, on=on,
                                        projections=projections, role=role, scales=scales,
                                        signals=signals, sort=sort, style=style, title=title,
                                        transform=transform, **kwds)


class markVisual(VegaSchema):
    """markVisual schema wrapper

    allOf(not Mapping(required=[]), :class:`mark`, Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/markVisual'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clip=Undefined, encode=Undefined, interactive=Undefined,
                 key=Undefined, name=Undefined, on=Undefined, role=Undefined, sort=Undefined,
                 style=Undefined, transform=Undefined, **kwds):
        super(markVisual, self).__init__(type=type, clip=clip, encode=encode, interactive=interactive,
                                         key=key, name=name, on=on, role=role, sort=sort, style=style,
                                         transform=transform, **kwds)


class listener(VegaSchema):
    """listener schema wrapper

    oneOf(:class:`signal`, Mapping(required=[scale]), :class:`stream`)
    """
    _schema = {'$ref': '#/defs/listener'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(listener, self).__init__(*args, **kwds)


class onEvents(VegaSchema):
    """onEvents schema wrapper

    List(allOf(Mapping(required=[events]), oneOf(Mapping(required=[encode]),
    Mapping(required=[update]))))
    """
    _schema = {'$ref': '#/defs/onEvents'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(onEvents, self).__init__(*args)


class onTrigger(VegaSchema):
    """onTrigger schema wrapper

    List(Mapping(required=[trigger]))
    """
    _schema = {'$ref': '#/defs/onTrigger'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(onTrigger, self).__init__(*args)


class onMarkTrigger(VegaSchema):
    """onMarkTrigger schema wrapper

    List(Mapping(required=[trigger]))
    """
    _schema = {'$ref': '#/defs/onMarkTrigger'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(onMarkTrigger, self).__init__(*args)


class padding(VegaSchema):
    """padding schema wrapper

    oneOf(float, Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(padding, self).__init__(*args, **kwds)


class projection(VegaSchema):
    """projection schema wrapper

    Mapping(required=[name])

    Attributes
    ----------

    name : string

    center : oneOf(:class:`signal`, List(:class:`numberOrSignal`))

    clipAngle : :class:`numberOrSignal`

    clipExtent : oneOf(:class:`signal`, List(oneOf(:class:`signal`,
    List(:class:`numberOrSignal`))))

    extent : oneOf(:class:`signal`, List(oneOf(:class:`signal`, List(:class:`numberOrSignal`))))

    fit : oneOf(Mapping(required=[]), List(Mapping(required=[])))

    parallels : oneOf(:class:`signal`, List(:class:`numberOrSignal`))

    pointRadius : :class:`numberOrSignal`

    precision : :class:`numberOrSignal`

    rotate : oneOf(:class:`signal`, List(:class:`numberOrSignal`))

    scale : :class:`numberOrSignal`

    size : oneOf(:class:`signal`, List(:class:`numberOrSignal`))

    translate : oneOf(:class:`signal`, List(:class:`numberOrSignal`))

    type : :class:`stringOrSignal`

    """
    _schema = {'$ref': '#/defs/projection'}
    _rootschema = Root._schema

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

    allOf(Mapping(required=[name]), oneOf(Mapping(required=[type]), Mapping(required=[type]),
    Mapping(required=[type]), Mapping(required=[type, range]), Mapping(required=[type]),
    Mapping(required=[type]), Mapping(required=[type]), not Mapping(required=[]),
    Mapping(required=[type]), Mapping(required=[type]), Mapping(required=[type])))
    """
    _schema = {'$ref': '#/defs/scale'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined,
                 domainMin=Undefined, domainRaw=Undefined, reverse=Undefined, round=Undefined,
                 type=Undefined, **kwds):
        super(scale, self).__init__(name=name, domain=domain, domainMax=domainMax, domainMid=domainMid,
                                    domainMin=domainMin, domainRaw=domainRaw, reverse=reverse,
                                    round=round, type=type, **kwds)


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

    """
    _schema = {'$ref': '#/defs/scope'}
    _rootschema = Root._schema

    def __init__(self, axes=Undefined, data=Undefined, encode=Undefined, layout=Undefined,
                 legends=Undefined, marks=Undefined, projections=Undefined, scales=Undefined,
                 signals=Undefined, title=Undefined, **kwds):
        super(scope, self).__init__(axes=axes, data=data, encode=encode, layout=layout, legends=legends,
                                    marks=marks, projections=projections, scales=scales,
                                    signals=signals, title=title, **kwds)


class signal(VegaSchema):
    """signal schema wrapper

    oneOf(:class:`signalPush`, :class:`signalNew`)
    """
    _schema = {'$ref': '#/defs/signal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(signal, self).__init__(*args, **kwds)


class signalName(VegaSchema):
    """signalName schema wrapper

    not Mapping(required=[])
    """
    _schema = {'$ref': '#/defs/signalName'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(signalName, self).__init__(*args)


class signalNew(VegaSchema):
    """signalNew schema wrapper

    Mapping(required=[name])

    Attributes
    ----------

    name : :class:`signalName`

    bind : :class:`bind`

    description : string

    on : :class:`onEvents`

    react : boolean

    update : :class:`exprString`

    value : Mapping(required=[])

    """
    _schema = {'$ref': '#/defs/signalNew'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, bind=Undefined, description=Undefined, on=Undefined,
                 react=Undefined, update=Undefined, value=Undefined, **kwds):
        super(signalNew, self).__init__(name=name, bind=bind, description=description, on=on,
                                        react=react, update=update, value=value, **kwds)


class signalPush(VegaSchema):
    """signalPush schema wrapper

    Mapping(required=[name, push])

    Attributes
    ----------

    name : :class:`signalName`

    push : enum('outer')

    description : string

    on : :class:`onEvents`

    """
    _schema = {'$ref': '#/defs/signalPush'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, push=Undefined, description=Undefined, on=Undefined, **kwds):
        super(signalPush, self).__init__(name=name, push=push, description=description, on=on, **kwds)


class streamParams(VegaSchema):
    """streamParams schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    between : List(:class:`stream`)

    consume : boolean

    debounce : float

    filter : oneOf(:class:`exprString`, List(:class:`exprString`))

    markname : string

    marktype : string

    throttle : float

    """
    _schema = {'$ref': '#/defs/streamParams'}
    _rootschema = Root._schema

    def __init__(self, between=Undefined, consume=Undefined, debounce=Undefined, filter=Undefined,
                 markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(streamParams, self).__init__(between=between, consume=consume, debounce=debounce,
                                           filter=filter, markname=markname, marktype=marktype,
                                           throttle=throttle, **kwds)


class streamEvents(VegaSchema):
    """streamEvents schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : string

    source : string

    """
    _schema = {'$ref': '#/defs/streamEvents'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, source=Undefined, **kwds):
        super(streamEvents, self).__init__(type=type, source=source, **kwds)


class stream(VegaSchema):
    """stream schema wrapper

    allOf(:class:`streamParams`, oneOf(:class:`streamEvents`, Mapping(required=[stream]),
    Mapping(required=[merge])))
    """
    _schema = {'$ref': '#/defs/stream'}
    _rootschema = Root._schema

    def __init__(self, between=Undefined, consume=Undefined, debounce=Undefined, filter=Undefined,
                 markname=Undefined, marktype=Undefined, throttle=Undefined, **kwds):
        super(stream, self).__init__(between=between, consume=consume, debounce=debounce, filter=filter,
                                     markname=markname, marktype=marktype, throttle=throttle, **kwds)


class titleEncode(VegaSchema):
    """titleEncode schema wrapper

    Mapping(required=[])
    """
    _schema = {'$ref': '#/defs/titleEncode'}
    _rootschema = Root._schema

    def __init__(self, **kwds):
        super(titleEncode, self).__init__(**kwds)


class title(VegaSchema):
    """title schema wrapper

    oneOf(string, Mapping(required=[text]))
    """
    _schema = {'$ref': '#/defs/title'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(title, self).__init__(*args, **kwds)


class transform(VegaSchema):
    """transform schema wrapper

    oneOf(:class:`aggregateTransform`, :class:`binTransform`, :class:`collectTransform`,
    :class:`countpatternTransform`, :class:`crossTransform`, :class:`densityTransform`,
    :class:`extentTransform`, :class:`filterTransform`, :class:`flattenTransform`,
    :class:`foldTransform`, :class:`formulaTransform`, :class:`imputeTransform`,
    :class:`joinaggregateTransform`, :class:`lookupTransform`, :class:`pivotTransform`,
    :class:`projectTransform`, :class:`sampleTransform`, :class:`sequenceTransform`,
    :class:`windowTransform`, :class:`identifierTransform`, :class:`linkpathTransform`,
    :class:`pieTransform`, :class:`stackTransform`, :class:`contourTransform`,
    :class:`geojsonTransform`, :class:`geopathTransform`, :class:`geopointTransform`,
    :class:`geoshapeTransform`, :class:`graticuleTransform`, :class:`forceTransform`,
    :class:`nestTransform`, :class:`packTransform`, :class:`partitionTransform`,
    :class:`stratifyTransform`, :class:`treeTransform`, :class:`treelinksTransform`,
    :class:`treemapTransform`, :class:`voronoiTransform`, :class:`wordcloudTransform`,
    :class:`crossfilterTransform`, :class:`resolvefilterTransform`)
    """
    _schema = {'$ref': '#/defs/transform'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(transform, self).__init__(*args, **kwds)


class transformMark(VegaSchema):
    """transformMark schema wrapper

    oneOf(:class:`binTransform`, :class:`collectTransform`, :class:`extentTransform`,
    :class:`formulaTransform`, :class:`joinaggregateTransform`, :class:`lookupTransform`,
    :class:`sampleTransform`, :class:`windowTransform`, :class:`identifierTransform`,
    :class:`linkpathTransform`, :class:`pieTransform`, :class:`stackTransform`,
    :class:`geojsonTransform`, :class:`geopathTransform`, :class:`geopointTransform`,
    :class:`geoshapeTransform`, :class:`forceTransform`, :class:`packTransform`,
    :class:`partitionTransform`, :class:`stratifyTransform`, :class:`treeTransform`,
    :class:`treemapTransform`, :class:`voronoiTransform`, :class:`wordcloudTransform`,
    :class:`crossfilterTransform`, :class:`resolvefilterTransform`)
    """
    _schema = {'$ref': '#/defs/transformMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(transformMark, self).__init__(*args, **kwds)


class aggregateTransform(VegaSchema):
    """aggregateTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('aggregate')

    cross : anyOf(boolean, :class:`signal`)

    drop : anyOf(boolean, :class:`signal`)

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`, None)),
    :class:`signal`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    ops : oneOf(List(anyOf(enum('values', 'count', '__count__', 'missing', 'valid', 'sum',
    'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr', 'distinct', 'ci0',
    'ci1', 'median', 'q1', 'q3', 'argmin', 'argmax', 'min', 'max'), :class:`signal`)),
    :class:`signal`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signal`, None)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/aggregateTransform'}
    _rootschema = Root._schema

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

    extent : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('bin')

    anchor : anyOf(float, :class:`signal`)

    base : anyOf(float, :class:`signal`)

    divide : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    maxbins : anyOf(float, :class:`signal`)

    minstep : anyOf(float, :class:`signal`)

    name : anyOf(string, :class:`signal`)

    nice : anyOf(boolean, :class:`signal`)

    signal : string

    step : anyOf(float, :class:`signal`)

    steps : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/binTransform'}
    _rootschema = Root._schema

    def __init__(self, extent=Undefined, field=Undefined, type=Undefined, anchor=Undefined,
                 base=Undefined, divide=Undefined, maxbins=Undefined, minstep=Undefined, name=Undefined,
                 nice=Undefined, signal=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(binTransform, self).__init__(extent=extent, field=field, type=type, anchor=anchor,
                                           base=base, divide=divide, maxbins=maxbins, minstep=minstep,
                                           name=name, nice=nice, signal=signal, step=step, steps=steps,
                                           **kwds)


class collectTransform(VegaSchema):
    """collectTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('collect')

    signal : string

    sort : :class:`compare`

    """
    _schema = {'$ref': '#/defs/collectTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, signal=Undefined, sort=Undefined, **kwds):
        super(collectTransform, self).__init__(type=type, signal=signal, sort=sort, **kwds)


class countpatternTransform(VegaSchema):
    """countpatternTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('countpattern')

    case : anyOf(enum('upper', 'lower', 'mixed'), :class:`signal`)

    pattern : anyOf(string, :class:`signal`)

    signal : string

    stopwords : anyOf(string, :class:`signal`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/countpatternTransform'}
    _rootschema = Root._schema

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

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/crossTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, filter=Undefined, signal=Undefined, **kwds):
        super(crossTransform, self).__init__(type=type, filter=filter, signal=signal, **kwds)


class densityTransform(VegaSchema):
    """densityTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('density')

    distribution : oneOf(Mapping(required=[function]), Mapping(required=[function]),
    Mapping(required=[function, field]), Mapping(required=[function]))

    extent : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    method : anyOf(string, :class:`signal`)

    signal : string

    steps : anyOf(float, :class:`signal`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/densityTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, distribution=Undefined, extent=Undefined, method=Undefined,
                 signal=Undefined, steps=Undefined, **kwds):
        super(densityTransform, self).__init__(type=type, distribution=distribution, extent=extent,
                                               method=method, signal=signal, steps=steps, **kwds)


class extentTransform(VegaSchema):
    """extentTransform schema wrapper

    Mapping(required=[type, field])

    Attributes
    ----------

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('extent')

    signal : string

    """
    _schema = {'$ref': '#/defs/extentTransform'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/defs/filterTransform'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(filterTransform, self).__init__(expr=expr, type=type, signal=signal, **kwds)


class flattenTransform(VegaSchema):
    """flattenTransform schema wrapper

    Mapping(required=[type, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    type : enum('flatten')

    signal : string

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/flattenTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(flattenTransform, self).__init__(fields=fields, type=type, signal=signal, **kwds)


class foldTransform(VegaSchema):
    """foldTransform schema wrapper

    Mapping(required=[type, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    type : enum('fold')

    signal : string

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/foldTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(foldTransform, self).__init__(fields=fields, type=type, signal=signal, **kwds)


class formulaTransform(VegaSchema):
    """formulaTransform schema wrapper

    Mapping(required=[type, expr, as])

    Attributes
    ----------

    expr : :class:`exprString`

    type : enum('formula')

    initonly : anyOf(boolean, :class:`signal`)

    signal : string

    as : anyOf(string, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/formulaTransform'}
    _rootschema = Root._schema

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
    :class:`signal`)

    keyvals : oneOf(List(Mapping(required=[])), :class:`signal`)

    method : anyOf(enum('value', 'mean', 'median', 'max', 'min'), :class:`signal`)

    signal : string

    value : Mapping(required=[])

    """
    _schema = {'$ref': '#/defs/imputeTransform'}
    _rootschema = Root._schema

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
    :class:`signal`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    ops : oneOf(List(anyOf(enum('values', 'count', '__count__', 'missing', 'valid', 'sum',
    'mean', 'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr', 'distinct', 'ci0',
    'ci1', 'median', 'q1', 'q3', 'argmin', 'argmax', 'min', 'max'), :class:`signal`)),
    :class:`signal`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signal`, None)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/joinaggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, fields=Undefined, groupby=Undefined, key=Undefined,
                 ops=Undefined, signal=Undefined, **kwds):
        super(joinaggregateTransform, self).__init__(type=type, fields=fields, groupby=groupby, key=key,
                                                     ops=ops, signal=signal, **kwds)


class lookupTransform(VegaSchema):
    """lookupTransform schema wrapper

    Mapping(required=[type, from, key, fields])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    type : enum('lookup')

    default : Mapping(required=[])

    signal : string

    values : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    from : string

    """
    _schema = {'$ref': '#/defs/lookupTransform'}
    _rootschema = Root._schema

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
    :class:`signal`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    limit : anyOf(float, :class:`signal`)

    op : anyOf(enum('values', 'count', '__count__', 'missing', 'valid', 'sum', 'mean',
    'average', 'variance', 'variancep', 'stdev', 'stdevp', 'stderr', 'distinct', 'ci0', 'ci1',
    'median', 'q1', 'q3', 'argmin', 'argmax', 'min', 'max'), :class:`signal`)

    signal : string

    """
    _schema = {'$ref': '#/defs/pivotTransform'}
    _rootschema = Root._schema

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
    :class:`signal`)

    signal : string

    as : oneOf(List(anyOf(string, :class:`signal`, None)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/projectTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, fields=Undefined, signal=Undefined, **kwds):
        super(projectTransform, self).__init__(type=type, fields=fields, signal=signal, **kwds)


class sampleTransform(VegaSchema):
    """sampleTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('sample')

    signal : string

    size : anyOf(float, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/sampleTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, signal=Undefined, size=Undefined, **kwds):
        super(sampleTransform, self).__init__(type=type, signal=signal, size=size, **kwds)


class sequenceTransform(VegaSchema):
    """sequenceTransform schema wrapper

    Mapping(required=[type, start, stop])

    Attributes
    ----------

    start : anyOf(float, :class:`signal`)

    stop : anyOf(float, :class:`signal`)

    type : enum('sequence')

    signal : string

    step : anyOf(float, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/sequenceTransform'}
    _rootschema = Root._schema

    def __init__(self, start=Undefined, stop=Undefined, type=Undefined, signal=Undefined,
                 step=Undefined, **kwds):
        super(sequenceTransform, self).__init__(start=start, stop=stop, type=type, signal=signal,
                                                step=step, **kwds)


class windowTransform(VegaSchema):
    """windowTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('window')

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`, None)),
    :class:`signal`)

    frame : oneOf(List(anyOf(float, :class:`signal`, None)), :class:`signal`)

    groupby : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    ignorePeers : anyOf(boolean, :class:`signal`)

    ops : oneOf(List(anyOf(enum('row_number', 'rank', 'dense_rank', 'percent_rank', 'cume_dist',
    'ntile', 'lag', 'lead', 'first_value', 'last_value', 'nth_value', 'values', 'count',
    '__count__', 'missing', 'valid', 'sum', 'mean', 'average', 'variance', 'variancep', 'stdev',
    'stdevp', 'stderr', 'distinct', 'ci0', 'ci1', 'median', 'q1', 'q3', 'argmin', 'argmax',
    'min', 'max'), :class:`signal`)), :class:`signal`)

    params : oneOf(List(anyOf(float, :class:`signal`, None)), :class:`signal`)

    signal : string

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signal`, None)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/windowTransform'}
    _rootschema = Root._schema

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

    as : anyOf(string, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/identifierTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, signal=Undefined, **kwds):
        super(identifierTransform, self).__init__(type=type, signal=signal, **kwds)


class linkpathTransform(VegaSchema):
    """linkpathTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('linkpath')

    orient : anyOf(enum('horizontal', 'vertical', 'radial'), :class:`signal`)

    shape : anyOf(enum('line', 'arc', 'curve', 'diagonal', 'orthogonal'), :class:`signal`)

    signal : string

    sourceX : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    sourceY : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    targetX : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    targetY : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    as : anyOf(string, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/linkpathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, orient=Undefined, shape=Undefined, signal=Undefined,
                 sourceX=Undefined, sourceY=Undefined, targetX=Undefined, targetY=Undefined, **kwds):
        super(linkpathTransform, self).__init__(type=type, orient=orient, shape=shape, signal=signal,
                                                sourceX=sourceX, sourceY=sourceY, targetX=targetX,
                                                targetY=targetY, **kwds)


class pieTransform(VegaSchema):
    """pieTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('pie')

    endAngle : anyOf(float, :class:`signal`)

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    sort : anyOf(boolean, :class:`signal`)

    startAngle : anyOf(float, :class:`signal`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/pieTransform'}
    _rootschema = Root._schema

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
    :class:`signal`)

    offset : anyOf(enum('zero', 'center', 'normalize'), :class:`signal`)

    signal : string

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/stackTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, groupby=Undefined, offset=Undefined,
                 signal=Undefined, sort=Undefined, **kwds):
        super(stackTransform, self).__init__(type=type, field=field, groupby=groupby, offset=offset,
                                             signal=signal, sort=sort, **kwds)


class contourTransform(VegaSchema):
    """contourTransform schema wrapper

    Mapping(required=[type, size])

    Attributes
    ----------

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    type : enum('contour')

    bandwidth : anyOf(float, :class:`signal`)

    cellSize : anyOf(float, :class:`signal`)

    count : anyOf(float, :class:`signal`)

    nice : anyOf(boolean, :class:`signal`)

    signal : string

    smooth : anyOf(boolean, :class:`signal`)

    thresholds : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    values : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    """
    _schema = {'$ref': '#/defs/contourTransform'}
    _rootschema = Root._schema

    def __init__(self, size=Undefined, type=Undefined, bandwidth=Undefined, cellSize=Undefined,
                 count=Undefined, nice=Undefined, signal=Undefined, smooth=Undefined,
                 thresholds=Undefined, values=Undefined, x=Undefined, y=Undefined, **kwds):
        super(contourTransform, self).__init__(size=size, type=type, bandwidth=bandwidth,
                                               cellSize=cellSize, count=count, nice=nice, signal=signal,
                                               smooth=smooth, thresholds=thresholds, values=values, x=x,
                                               y=y, **kwds)


class geojsonTransform(VegaSchema):
    """geojsonTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('geojson')

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    geojson : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    """
    _schema = {'$ref': '#/defs/geojsonTransform'}
    _rootschema = Root._schema

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

    pointRadius : anyOf(float, :class:`signal`, :class:`expr`, :class:`paramField`)

    projection : string

    signal : string

    as : anyOf(string, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/geopathTransform'}
    _rootschema = Root._schema

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
    :class:`signal`)

    projection : string

    type : enum('geopoint')

    signal : string

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/geopointTransform'}
    _rootschema = Root._schema

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

    pointRadius : anyOf(float, :class:`signal`, :class:`expr`, :class:`paramField`)

    projection : string

    signal : string

    as : anyOf(string, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/geoshapeTransform'}
    _rootschema = Root._schema

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

    extent : oneOf(List(Mapping(required=[])), :class:`signal`)

    extentMajor : oneOf(List(Mapping(required=[])), :class:`signal`)

    extentMinor : oneOf(List(Mapping(required=[])), :class:`signal`)

    precision : anyOf(float, :class:`signal`)

    signal : string

    step : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    stepMajor : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    stepMinor : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/graticuleTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, extent=Undefined, extentMajor=Undefined, extentMinor=Undefined,
                 precision=Undefined, signal=Undefined, step=Undefined, stepMajor=Undefined,
                 stepMinor=Undefined, **kwds):
        super(graticuleTransform, self).__init__(type=type, extent=extent, extentMajor=extentMajor,
                                                 extentMinor=extentMinor, precision=precision,
                                                 signal=signal, step=step, stepMajor=stepMajor,
                                                 stepMinor=stepMinor, **kwds)


class forceTransform(VegaSchema):
    """forceTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('force')

    alpha : anyOf(float, :class:`signal`)

    alphaMin : anyOf(float, :class:`signal`)

    alphaTarget : anyOf(float, :class:`signal`)

    forces : List(oneOf(Mapping(required=[force]), Mapping(required=[force]),
    Mapping(required=[force]), Mapping(required=[force]), Mapping(required=[force]),
    Mapping(required=[force])))

    iterations : anyOf(float, :class:`signal`)

    restart : anyOf(boolean, :class:`signal`)

    signal : string

    static : anyOf(boolean, :class:`signal`)

    velocityDecay : anyOf(float, :class:`signal`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/forceTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, alpha=Undefined, alphaMin=Undefined, alphaTarget=Undefined,
                 forces=Undefined, iterations=Undefined, restart=Undefined, signal=Undefined,
                 static=Undefined, velocityDecay=Undefined, **kwds):
        super(forceTransform, self).__init__(type=type, alpha=alpha, alphaMin=alphaMin,
                                             alphaTarget=alphaTarget, forces=forces,
                                             iterations=iterations, restart=restart, signal=signal,
                                             static=static, velocityDecay=velocityDecay, **kwds)


class nestTransform(VegaSchema):
    """nestTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('nest')

    generate : anyOf(boolean, :class:`signal`)

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    keys : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    signal : string

    """
    _schema = {'$ref': '#/defs/nestTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, generate=Undefined, key=Undefined, keys=Undefined,
                 signal=Undefined, **kwds):
        super(nestTransform, self).__init__(type=type, generate=generate, key=key, keys=keys,
                                            signal=signal, **kwds)


class packTransform(VegaSchema):
    """packTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('pack')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    padding : anyOf(float, :class:`signal`)

    radius : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/packTransform'}
    _rootschema = Root._schema

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

    padding : anyOf(float, :class:`signal`)

    round : anyOf(boolean, :class:`signal`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/partitionTransform'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/defs/stratifyTransform'}
    _rootschema = Root._schema

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

    method : anyOf(enum('tidy', 'cluster'), :class:`signal`)

    nodeSize : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/treeTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, method=Undefined, nodeSize=Undefined,
                 signal=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(treeTransform, self).__init__(type=type, field=field, method=method, nodeSize=nodeSize,
                                            signal=signal, size=size, sort=sort, **kwds)


class treelinksTransform(VegaSchema):
    """treelinksTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('treelinks')

    key : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    signal : string

    """
    _schema = {'$ref': '#/defs/treelinksTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, key=Undefined, signal=Undefined, **kwds):
        super(treelinksTransform, self).__init__(type=type, key=key, signal=signal, **kwds)


class treemapTransform(VegaSchema):
    """treemapTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('treemap')

    field : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    method : anyOf(enum('squarify', 'resquarify', 'binary', 'dice', 'slice', 'slicedice'),
    :class:`signal`)

    padding : anyOf(float, :class:`signal`)

    paddingBottom : anyOf(float, :class:`signal`)

    paddingInner : anyOf(float, :class:`signal`)

    paddingLeft : anyOf(float, :class:`signal`)

    paddingOuter : anyOf(float, :class:`signal`)

    paddingRight : anyOf(float, :class:`signal`)

    paddingTop : anyOf(float, :class:`signal`)

    ratio : anyOf(float, :class:`signal`)

    round : anyOf(boolean, :class:`signal`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    sort : :class:`compare`

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/treemapTransform'}
    _rootschema = Root._schema

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


class voronoiTransform(VegaSchema):
    """voronoiTransform schema wrapper

    Mapping(required=[type, x, y])

    Attributes
    ----------

    type : enum('voronoi')

    x : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    y : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    extent : oneOf(List(Mapping(required=[])), :class:`signal`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    as : anyOf(string, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/voronoiTransform'}
    _rootschema = Root._schema

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

    font : anyOf(string, :class:`signal`, :class:`expr`, :class:`paramField`)

    fontSize : anyOf(float, :class:`signal`, :class:`expr`, :class:`paramField`)

    fontSizeRange : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`, None)

    fontStyle : anyOf(string, :class:`signal`, :class:`expr`, :class:`paramField`)

    fontWeight : anyOf(string, :class:`signal`, :class:`expr`, :class:`paramField`)

    padding : anyOf(float, :class:`signal`, :class:`expr`, :class:`paramField`)

    rotate : anyOf(float, :class:`signal`, :class:`expr`, :class:`paramField`)

    signal : string

    size : oneOf(List(anyOf(float, :class:`signal`)), :class:`signal`)

    spiral : anyOf(string, :class:`signal`)

    text : oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)

    as : oneOf(List(anyOf(string, :class:`signal`)), :class:`signal`)

    """
    _schema = {'$ref': '#/defs/wordcloudTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, font=Undefined, fontSize=Undefined, fontSizeRange=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, padding=Undefined, rotate=Undefined,
                 signal=Undefined, size=Undefined, spiral=Undefined, text=Undefined, **kwds):
        super(wordcloudTransform, self).__init__(type=type, font=font, fontSize=fontSize,
                                                 fontSizeRange=fontSizeRange, fontStyle=fontStyle,
                                                 fontWeight=fontWeight, padding=padding, rotate=rotate,
                                                 signal=signal, size=size, spiral=spiral, text=text,
                                                 **kwds)


class crossfilterTransform(VegaSchema):
    """crossfilterTransform schema wrapper

    Mapping(required=[type, fields, query])

    Attributes
    ----------

    fields : oneOf(List(oneOf(:class:`scaleField`, :class:`paramField`, :class:`expr`)),
    :class:`signal`)

    query : oneOf(List(Mapping(required=[])), :class:`signal`)

    type : enum('crossfilter')

    signal : string

    """
    _schema = {'$ref': '#/defs/crossfilterTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, query=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(crossfilterTransform, self).__init__(fields=fields, query=query, type=type, signal=signal,
                                                   **kwds)


class resolvefilterTransform(VegaSchema):
    """resolvefilterTransform schema wrapper

    Mapping(required=[type, ignore, filter])

    Attributes
    ----------

    filter : Mapping(required=[])

    ignore : anyOf(float, :class:`signal`)

    type : enum('resolvefilter')

    signal : string

    """
    _schema = {'$ref': '#/defs/resolvefilterTransform'}
    _rootschema = Root._schema

    def __init__(self, filter=Undefined, ignore=Undefined, type=Undefined, signal=Undefined, **kwds):
        super(resolvefilterTransform, self).__init__(filter=filter, ignore=ignore, type=type,
                                                     signal=signal, **kwds)


class tickCount(VegaSchema):
    """tickCount schema wrapper

    oneOf(float, enum('millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month',
    'year'), Mapping(required=[interval]), :class:`signal`)
    """
    _schema = {'$ref': '#/refs/tickCount'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(tickCount, self).__init__(*args, **kwds)


class element(VegaSchema):
    """element schema wrapper

    string
    """
    _schema = {'$ref': '#/refs/element'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(element, self).__init__(*args)


class paramField(VegaSchema):
    """paramField schema wrapper

    Mapping(required=[field])

    Attributes
    ----------

    field : string

    """
    _schema = {'$ref': '#/refs/paramField'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, **kwds):
        super(paramField, self).__init__(field=field, **kwds)


class field(VegaSchema):
    """field schema wrapper

    oneOf(string, oneOf(:class:`signal`, Mapping(required=[datum]), Mapping(required=[group]),
    Mapping(required=[parent])))
    """
    _schema = {'$ref': '#/refs/field'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(field, self).__init__(*args, **kwds)


class scale(VegaSchema):
    """scale schema wrapper

    oneOf(string, oneOf(:class:`signal`, Mapping(required=[datum]), Mapping(required=[group]),
    Mapping(required=[parent])))
    """
    _schema = {'$ref': '#/refs/scale'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scale, self).__init__(*args, **kwds)


class stringModifiers(VegaSchema):
    """stringModifiers schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    scale : :class:`scale`

    """
    _schema = {'$ref': '#/refs/stringModifiers'}
    _rootschema = Root._schema

    def __init__(self, scale=Undefined, **kwds):
        super(stringModifiers, self).__init__(scale=scale, **kwds)


class numberModifiers(VegaSchema):
    """numberModifiers schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    band : anyOf(float, boolean)

    exponent : oneOf(float, :class:`numberValue`)

    extra : boolean

    mult : oneOf(float, :class:`numberValue`)

    offset : oneOf(float, :class:`numberValue`)

    round : boolean

    scale : :class:`scale`

    """
    _schema = {'$ref': '#/refs/numberModifiers'}
    _rootschema = Root._schema

    def __init__(self, band=Undefined, exponent=Undefined, extra=Undefined, mult=Undefined,
                 offset=Undefined, round=Undefined, scale=Undefined, **kwds):
        super(numberModifiers, self).__init__(band=band, exponent=exponent, extra=extra, mult=mult,
                                              offset=offset, round=round, scale=scale, **kwds)


class value(VegaSchema):
    """value schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/value'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(value, self).__init__(*args, **kwds)


class numberValue(VegaSchema):
    """numberValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`numberModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`numberModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/numberValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(numberValue, self).__init__(*args, **kwds)


class stringValue(VegaSchema):
    """stringValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/stringValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(stringValue, self).__init__(*args, **kwds)


class booleanValue(VegaSchema):
    """booleanValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/booleanValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(booleanValue, self).__init__(*args, **kwds)


class arrayValue(VegaSchema):
    """arrayValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/arrayValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(arrayValue, self).__init__(*args, **kwds)


class nullableStringValue(VegaSchema):
    """nullableStringValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/nullableStringValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(nullableStringValue, self).__init__(*args, **kwds)


class fontWeightValue(VegaSchema):
    """fontWeightValue schema wrapper

    oneOf(List(allOf(:class:`rule`, allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))), allOf(:class:`stringModifiers`, anyOf(oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[range])),
    Mapping(required=[scale, value]), Mapping(required=[scale, band]),
    Mapping(required=[offset]))))
    """
    _schema = {'$ref': '#/refs/fontWeightValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(fontWeightValue, self).__init__(*args, **kwds)


class colorRGB(VegaSchema):
    """colorRGB schema wrapper

    Mapping(required=[r, g, b])

    Attributes
    ----------

    b : :class:`numberValue`

    g : :class:`numberValue`

    r : :class:`numberValue`

    """
    _schema = {'$ref': '#/refs/colorRGB'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/refs/colorHSL'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/refs/colorLAB'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/refs/colorHCL'}
    _rootschema = Root._schema

    def __init__(self, c=Undefined, h=Undefined, l=Undefined, **kwds):
        super(colorHCL, self).__init__(c=c, h=h, l=l, **kwds)


class colorValue(VegaSchema):
    """colorValue schema wrapper

    oneOf(:class:`nullableStringValue`, Mapping(required=[gradient]), Mapping(required=[color]))
    """
    _schema = {'$ref': '#/refs/colorValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(colorValue, self).__init__(*args, **kwds)


class expr(VegaSchema):
    """expr schema wrapper

    Mapping(required=[expr])

    Attributes
    ----------

    expr : string

    """
    _schema = {'$ref': '#/refs/expr'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, **kwds):
        super(expr, self).__init__(expr=expr, **kwds)


class exprString(VegaSchema):
    """exprString schema wrapper

    string
    """
    _schema = {'$ref': '#/refs/exprString'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(exprString, self).__init__(*args)


class compare(VegaSchema):
    """compare schema wrapper

    oneOf(Mapping(required=[]), Mapping(required=[]))
    """
    _schema = {'$ref': '#/refs/compare'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(compare, self).__init__(*args, **kwds)


class from_(VegaSchema):
    """from_ schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    data : string

    """
    _schema = {'$ref': '#/refs/from'}
    _rootschema = Root._schema

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
    _schema = {'$ref': '#/refs/facet'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, data=Undefined, **kwds):
        super(facet, self).__init__(facet=facet, data=data, **kwds)


class markclip(VegaSchema):
    """markclip schema wrapper

    oneOf(:class:`booleanOrSignal`, Mapping(required=[path]), Mapping(required=[sphere]))
    """
    _schema = {'$ref': '#/refs/markclip'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(markclip, self).__init__(*args, **kwds)


class style(VegaSchema):
    """style schema wrapper

    oneOf(string, List(string))
    """
    _schema = {'$ref': '#/refs/style'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(style, self).__init__(*args, **kwds)


class marktype(VegaSchema):
    """marktype schema wrapper

    string
    """
    _schema = {'$ref': '#/refs/marktype'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(marktype, self).__init__(*args)


class sortOrder(VegaSchema):
    """sortOrder schema wrapper

    oneOf(enum('ascending', 'descending'), :class:`signal`)
    """
    _schema = {'$ref': '#/refs/sortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(sortOrder, self).__init__(*args, **kwds)


class scaleField(VegaSchema):
    """scaleField schema wrapper

    oneOf(string, :class:`signal`)
    """
    _schema = {'$ref': '#/refs/scaleField'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scaleField, self).__init__(*args, **kwds)


class scaleInterpolate(VegaSchema):
    """scaleInterpolate schema wrapper

    oneOf(string, :class:`signal`, Mapping(required=[type]))
    """
    _schema = {'$ref': '#/refs/scaleInterpolate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scaleInterpolate, self).__init__(*args, **kwds)


class scaleData(VegaSchema):
    """scaleData schema wrapper

    oneOf(Mapping(required=[data, field]), Mapping(required=[data, fields]),
    Mapping(required=[fields]))
    """
    _schema = {'$ref': '#/refs/scaleData'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scaleData, self).__init__(*args, **kwds)


class selector(VegaSchema):
    """selector schema wrapper

    string
    """
    _schema = {'$ref': '#/refs/selector'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(selector, self).__init__(*args)


class signal(VegaSchema):
    """signal schema wrapper

    Mapping(required=[signal])

    Attributes
    ----------

    signal : string

    """
    _schema = {'$ref': '#/refs/signal'}
    _rootschema = Root._schema

    def __init__(self, signal=Undefined, **kwds):
        super(signal, self).__init__(signal=signal, **kwds)


class booleanOrSignal(VegaSchema):
    """booleanOrSignal schema wrapper

    oneOf(boolean, :class:`signal`)
    """
    _schema = {'$ref': '#/refs/booleanOrSignal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(booleanOrSignal, self).__init__(*args, **kwds)


class numberOrSignal(VegaSchema):
    """numberOrSignal schema wrapper

    oneOf(float, :class:`signal`)
    """
    _schema = {'$ref': '#/refs/numberOrSignal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(numberOrSignal, self).__init__(*args, **kwds)


class stringOrSignal(VegaSchema):
    """stringOrSignal schema wrapper

    oneOf(string, :class:`signal`)
    """
    _schema = {'$ref': '#/refs/stringOrSignal'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(stringOrSignal, self).__init__(*args, **kwds)

