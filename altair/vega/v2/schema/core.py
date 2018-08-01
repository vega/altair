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

    allOf(:class:`container`, Mapping(required=[]))
    """
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, axes=Undefined, background=Undefined, data=Undefined, height=Undefined,
                 legends=Undefined, marks=Undefined, padding=Undefined, predicates=Undefined,
                 scales=Undefined, scene=Undefined, signals=Undefined, viewport=Undefined,
                 width=Undefined, **kwds):
        super(Root, self).__init__(axes=axes, background=background, data=data, height=height,
                                   legends=legends, marks=marks, padding=padding, predicates=predicates,
                                   scales=scales, scene=scene, signals=signals, viewport=viewport,
                                   width=width, **kwds)


class axis(VegaSchema):
    """axis schema wrapper

    Mapping(required=[type, scale])

    Attributes
    ----------

    scale : string

    type : enum('x', 'y')

    format : string

    formatType : enum('time', 'utc', 'string', 'number')

    grid : boolean

    layer : enum('front', 'back')

    offset : oneOf(float, Mapping(required=[scale, value]))

    orient : enum('top', 'bottom', 'left', 'right')

    properties : Mapping(required=[])

    subdivide : float

    tickPadding : float

    tickSize : float

    tickSizeEnd : float

    tickSizeMajor : float

    tickSizeMinor : float

    ticks : float

    title : string

    titleOffset : float

    values : List(anyOf(string, float))

    """
    _schema = {'$ref': '#/defs/axis'}
    _rootschema = Root._schema

    def __init__(self, scale=Undefined, type=Undefined, format=Undefined, formatType=Undefined,
                 grid=Undefined, layer=Undefined, offset=Undefined, orient=Undefined,
                 properties=Undefined, subdivide=Undefined, tickPadding=Undefined, tickSize=Undefined,
                 tickSizeEnd=Undefined, tickSizeMajor=Undefined, tickSizeMinor=Undefined,
                 ticks=Undefined, title=Undefined, titleOffset=Undefined, values=Undefined, **kwds):
        super(axis, self).__init__(scale=scale, type=type, format=format, formatType=formatType,
                                   grid=grid, layer=layer, offset=offset, orient=orient,
                                   properties=properties, subdivide=subdivide, tickPadding=tickPadding,
                                   tickSize=tickSize, tickSizeEnd=tickSizeEnd,
                                   tickSizeMajor=tickSizeMajor, tickSizeMinor=tickSizeMinor,
                                   ticks=ticks, title=title, titleOffset=titleOffset, values=values,
                                   **kwds)


class background(VegaSchema):
    """background schema wrapper

    string
    """
    _schema = {'$ref': '#/defs/background'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(background, self).__init__(*args)


class data(VegaSchema):
    """data schema wrapper

    allOf(Mapping(required=[name]), anyOf(Mapping(required=[name, modify]),
    oneOf(Mapping(required=[source]), Mapping(required=[values]), Mapping(required=[url]))))
    """
    _schema = {'$ref': '#/defs/data'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, format=Undefined, modify=Undefined, transform=Undefined, **kwds):
        super(data, self).__init__(name=name, format=format, modify=modify, transform=transform, **kwds)


class legend(VegaSchema):
    """legend schema wrapper

    anyOf(Mapping(required=[size]), Mapping(required=[shape]), Mapping(required=[fill]),
    Mapping(required=[stroke]), Mapping(required=[opacity]))

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

    type : enum('rect', 'symbol', 'path', 'arc', 'area', 'line', 'rule', 'image', 'text',
    'group')

    delay : :class:`numberValue`

    ease : enum('linear-in', 'linear-out', 'linear-in-out', 'linear-out-in', 'quad-in',
    'quad-out', 'quad-in-out', 'quad-out-in', 'cubic-in', 'cubic-out', 'cubic-in-out',
    'cubic-out-in', 'sin-in', 'sin-out', 'sin-in-out', 'sin-out-in', 'exp-in', 'exp-out',
    'exp-in-out', 'exp-out-in', 'circle-in', 'circle-out', 'circle-in-out', 'circle-out-in',
    'bounce-in', 'bounce-out', 'bounce-in-out', 'bounce-out-in')

    interactive : boolean

    key : string

    name : string

    properties : anyOf(Mapping(required=[enter]), Mapping(required=[update]))

    from : Mapping(required=[])

    """
    _schema = {'$ref': '#/defs/mark'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, delay=Undefined, ease=Undefined, interactive=Undefined,
                 key=Undefined, name=Undefined, properties=Undefined, **kwds):
        super(mark, self).__init__(type=type, delay=delay, ease=ease, interactive=interactive, key=key,
                                   name=name, properties=properties, **kwds)


class container(VegaSchema):
    """container schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    axes : List(:class:`axis`)

    legends : List(:class:`legend`)

    marks : List(oneOf(:class:`groupMark`, :class:`visualMark`))

    scales : List(:class:`scale`)

    scene : Mapping(required=[])

    """
    _schema = {'$ref': '#/defs/container'}
    _rootschema = Root._schema

    def __init__(self, axes=Undefined, legends=Undefined, marks=Undefined, scales=Undefined,
                 scene=Undefined, **kwds):
        super(container, self).__init__(axes=axes, legends=legends, marks=marks, scales=scales,
                                        scene=scene, **kwds)


class groupMark(VegaSchema):
    """groupMark schema wrapper

    allOf(Mapping(required=[type]), :class:`mark`, :class:`container`)
    """
    _schema = {'$ref': '#/defs/groupMark'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, axes=Undefined, delay=Undefined, ease=Undefined,
                 interactive=Undefined, key=Undefined, legends=Undefined, marks=Undefined,
                 name=Undefined, properties=Undefined, scales=Undefined, scene=Undefined, **kwds):
        super(groupMark, self).__init__(type=type, axes=axes, delay=delay, ease=ease,
                                        interactive=interactive, key=key, legends=legends, marks=marks,
                                        name=name, properties=properties, scales=scales, scene=scene,
                                        **kwds)


class visualMark(VegaSchema):
    """visualMark schema wrapper

    allOf(not Mapping(required=[]), :class:`mark`)
    """
    _schema = {'$ref': '#/defs/visualMark'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, delay=Undefined, ease=Undefined, interactive=Undefined,
                 key=Undefined, name=Undefined, properties=Undefined, **kwds):
        super(visualMark, self).__init__(type=type, delay=delay, ease=ease, interactive=interactive,
                                         key=key, name=name, properties=properties, **kwds)


class modify(VegaSchema):
    """modify schema wrapper

    List(oneOf(Mapping(required=[type, signal]), Mapping(required=[type, predicate]),
    Mapping(required=[type, test])))
    """
    _schema = {'$ref': '#/defs/modify'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(modify, self).__init__(*args)


class padding(VegaSchema):
    """padding schema wrapper

    oneOf(enum('strict', 'auto'), float, Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(padding, self).__init__(*args, **kwds)


class predicate(VegaSchema):
    """predicate schema wrapper

    oneOf(Mapping(required=[name, type, operands]), Mapping(required=[name, type, operands]),
    oneOf(Mapping(required=[range]), Mapping(required=[data, field])))
    """
    _schema = {'$ref': '#/defs/predicate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(predicate, self).__init__(*args, **kwds)


class rule(VegaSchema):
    """rule schema wrapper

    anyOf(Mapping(required=[]), Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/rule'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(rule, self).__init__(*args, **kwds)


class propset(VegaSchema):
    """propset schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`,
    allOf(:class:`stringModifiers`, oneOf(:class:`signal`, Mapping(required=[value]),
    Mapping(required=[field]), Mapping(required=[band]))))), allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))

    angle : :class:`numberValue`

    baseline : oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`,
    allOf(:class:`stringModifiers`, oneOf(:class:`signal`, Mapping(required=[value]),
    Mapping(required=[field]), Mapping(required=[band]))))), allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))

    clip : :class:`booleanValue`

    cursor : :class:`stringValue`

    dx : :class:`numberValue`

    dy : :class:`numberValue`

    endAngle : :class:`numberValue`

    fill : :class:`colorValue`

    fillOpacity : :class:`numberValue`

    font : :class:`stringValue`

    fontSize : :class:`numberValue`

    fontStyle : :class:`stringValue`

    fontWeight : :class:`stringValue`

    height : :class:`numberValue`

    innerRadius : :class:`numberValue`

    interpolate : oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`,
    allOf(:class:`stringModifiers`, oneOf(:class:`signal`, Mapping(required=[value]),
    Mapping(required=[field]), Mapping(required=[band]))))), allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))

    opacity : :class:`numberValue`

    orient : oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`,
    allOf(:class:`stringModifiers`, oneOf(:class:`signal`, Mapping(required=[value]),
    Mapping(required=[field]), Mapping(required=[band]))))), allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))

    outerRadius : :class:`numberValue`

    path : :class:`stringValue`

    radius : :class:`numberValue`

    shape : anyOf(oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`,
    allOf(:class:`stringModifiers`, oneOf(:class:`signal`, Mapping(required=[value]),
    Mapping(required=[field]), Mapping(required=[band]))))), allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band])))), :class:`stringValue`)

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
    _schema = {'$ref': '#/defs/propset'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined,
                 cursor=Undefined, dx=Undefined, dy=Undefined, endAngle=Undefined, fill=Undefined,
                 fillOpacity=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined,
                 fontWeight=Undefined, height=Undefined, innerRadius=Undefined, interpolate=Undefined,
                 opacity=Undefined, orient=Undefined, outerRadius=Undefined, path=Undefined,
                 radius=Undefined, shape=Undefined, size=Undefined, startAngle=Undefined,
                 stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined,
                 theta=Undefined, url=Undefined, width=Undefined, x=Undefined, x2=Undefined,
                 xc=Undefined, y=Undefined, y2=Undefined, yc=Undefined, **kwds):
        super(propset, self).__init__(align=align, angle=angle, baseline=baseline, clip=clip,
                                      cursor=cursor, dx=dx, dy=dy, endAngle=endAngle, fill=fill,
                                      fillOpacity=fillOpacity, font=font, fontSize=fontSize,
                                      fontStyle=fontStyle, fontWeight=fontWeight, height=height,
                                      innerRadius=innerRadius, interpolate=interpolate, opacity=opacity,
                                      orient=orient, outerRadius=outerRadius, path=path, radius=radius,
                                      shape=shape, size=size, startAngle=startAngle, stroke=stroke,
                                      strokeDash=strokeDash, strokeDashOffset=strokeDashOffset,
                                      strokeOpacity=strokeOpacity, strokeWidth=strokeWidth,
                                      tension=tension, text=text, theta=theta, url=url, width=width,
                                      x=x, x2=x2, xc=xc, y=y, y2=y2, yc=yc, **kwds)


class signal(VegaSchema):
    """signal schema wrapper

    Mapping(required=[name])

    Attributes
    ----------

    name : not Mapping(required=[])

    expr : string

    init : Mapping(required=[])

    scale : :class:`scopedScale`

    streams : :class:`streams`

    verbose : boolean

    """
    _schema = {'$ref': '#/defs/signal'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, expr=Undefined, init=Undefined, scale=Undefined,
                 streams=Undefined, verbose=Undefined, **kwds):
        super(signal, self).__init__(name=name, expr=expr, init=init, scale=scale, streams=streams,
                                     verbose=verbose, **kwds)


class spec(VegaSchema):
    """spec schema wrapper

    allOf(:class:`container`, Mapping(required=[]))
    """
    _schema = {'$ref': '#/defs/spec'}
    _rootschema = Root._schema

    def __init__(self, axes=Undefined, background=Undefined, data=Undefined, height=Undefined,
                 legends=Undefined, marks=Undefined, padding=Undefined, predicates=Undefined,
                 scales=Undefined, scene=Undefined, signals=Undefined, viewport=Undefined,
                 width=Undefined, **kwds):
        super(spec, self).__init__(axes=axes, background=background, data=data, height=height,
                                   legends=legends, marks=marks, padding=padding, predicates=predicates,
                                   scales=scales, scene=scene, signals=signals, viewport=viewport,
                                   width=width, **kwds)


class streams(VegaSchema):
    """streams schema wrapper

    List(Mapping(required=[type, expr]))
    """
    _schema = {'$ref': '#/defs/streams'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(streams, self).__init__(*args)


class aggregateTransform(VegaSchema):
    """aggregateTransform schema wrapper

    Mapping(required=[type])
    Compute summary aggregate statistics

    Attributes
    ----------

    type : enum('aggregate')

    groupby : List(oneOf(string, :class:`signal`))
        A list of fields to split the data into groups.
    summarize : oneOf(Mapping(required=[]), List(Mapping(required=[field, ops])))

    """
    _schema = {'$ref': '#/defs/aggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, groupby=Undefined, summarize=Undefined, **kwds):
        super(aggregateTransform, self).__init__(type=type, groupby=groupby, summarize=summarize, **kwds)


class binTransform(VegaSchema):
    """binTransform schema wrapper

    Mapping(required=[type, field])
    Bins values into quantitative bins (e.g., for a histogram).

    Attributes
    ----------

    field : oneOf(string, :class:`signal`)
        The name of the field to bin values from.
    type : enum('bin')

    base : oneOf(float, :class:`signal`)
        The number base to use for automatic bin determination.
    div : oneOf(List(float), :class:`signal`)
        An array of scale factors indicating allowable subdivisions.
    max : oneOf(float, :class:`signal`)
        The maximum bin value to consider.
    maxbins : oneOf(float, :class:`signal`)
        The maximum number of allowable bins.
    min : oneOf(float, :class:`signal`)
        The minimum bin value to consider.
    minstep : oneOf(float, :class:`signal`)
        A minimum allowable step size (particularly useful for integer values).
    output : Mapping(required=[])
        Rename the output data fields
    step : oneOf(float, :class:`signal`)
        An exact step size to use between bins. If provided, options such as maxbins will be
        ignored.
    steps : oneOf(List(float), :class:`signal`)
        An array of allowable step sizes to choose from.
    """
    _schema = {'$ref': '#/defs/binTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, type=Undefined, base=Undefined, div=Undefined, max=Undefined,
                 maxbins=Undefined, min=Undefined, minstep=Undefined, output=Undefined, step=Undefined,
                 steps=Undefined, **kwds):
        super(binTransform, self).__init__(field=field, type=type, base=base, div=div, max=max,
                                           maxbins=maxbins, min=min, minstep=minstep, output=output,
                                           step=step, steps=steps, **kwds)


class crossTransform(VegaSchema):
    """crossTransform schema wrapper

    Mapping(required=[type])
    Compute the cross-product of two data sets.

    Attributes
    ----------

    type : enum('cross')

    diagonal : oneOf(boolean, :class:`signal`)
        If false, items along the "diagonal" of the cross-product (those elements with the
        same index in their respective array) will not be included in the output.
    filter : string
        A string containing an expression (in JavaScript syntax) to filter the resulting
        data elements.
    output : Mapping(required=[])
        Rename the output data fields
    with : string
        The name of the secondary data set to cross with the primary data. If unspecified,
        the primary data is crossed with itself.
    """
    _schema = {'$ref': '#/defs/crossTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, diagonal=Undefined, filter=Undefined, output=Undefined, **kwds):
        super(crossTransform, self).__init__(type=type, diagonal=diagonal, filter=filter, output=output,
                                             **kwds)


class countpatternTransform(VegaSchema):
    """countpatternTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('countpattern')

    case : oneOf(enum('lower', 'upper', 'none'), :class:`signal`)
        Text case transformation to apply.
    field : oneOf(string, :class:`signal`)
        The field containing the text to analyze.
    output : Mapping(required=[])
        Rename the output data fields
    pattern : oneOf(string, :class:`signal`)
        A regexp pattern for matching words in text.
    stopwords : oneOf(string, :class:`signal`)
        A regexp pattern for matching stopwords to omit.
    """
    _schema = {'$ref': '#/defs/countpatternTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, case=Undefined, field=Undefined, output=Undefined,
                 pattern=Undefined, stopwords=Undefined, **kwds):
        super(countpatternTransform, self).__init__(type=type, case=case, field=field, output=output,
                                                    pattern=pattern, stopwords=stopwords, **kwds)


class linkpathTransform(VegaSchema):
    """linkpathTransform schema wrapper

    Mapping(required=[type])
    Computes a path definition for connecting nodes within a node-link network or tree diagram.

    Attributes
    ----------

    type : enum('linkpath')

    output : Mapping(required=[])
        Rename the output data fields
    shape : oneOf(enum('line', 'curve', 'cornerX', 'cornerY', 'cornerR', 'diagonalX',
    'diagonalY', 'diagonalR'), :class:`signal`)
        The path shape to use
    sourceX : oneOf(string, :class:`signal`)
        The data field that references the source x-coordinate for this link.
    sourceY : oneOf(string, :class:`signal`)
        The data field that references the source y-coordinate for this link.
    targetX : oneOf(string, :class:`signal`)
        The data field that references the target x-coordinate for this link.
    targetY : oneOf(string, :class:`signal`)
        The data field that references the target y-coordinate for this link.
    tension : oneOf(float, :class:`signal`)
        A tension parameter for the "tightness" of "curve"-shaped links.
    """
    _schema = {'$ref': '#/defs/linkpathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, output=Undefined, shape=Undefined, sourceX=Undefined,
                 sourceY=Undefined, targetX=Undefined, targetY=Undefined, tension=Undefined, **kwds):
        super(linkpathTransform, self).__init__(type=type, output=output, shape=shape, sourceX=sourceX,
                                                sourceY=sourceY, targetX=targetX, targetY=targetY,
                                                tension=tension, **kwds)


class facetTransform(VegaSchema):
    """facetTransform schema wrapper

    Mapping(required=[type])
    A special aggregate transform that organizes a data set into groups or "facets".

    Attributes
    ----------

    type : enum('facet')

    groupby : List(oneOf(string, :class:`signal`))
        A list of fields to split the data into groups.
    summarize : oneOf(Mapping(required=[]), List(Mapping(required=[field, ops])))

    transform : :class:`transform`

    """
    _schema = {'$ref': '#/defs/facetTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, groupby=Undefined, summarize=Undefined, transform=Undefined,
                 **kwds):
        super(facetTransform, self).__init__(type=type, groupby=groupby, summarize=summarize,
                                             transform=transform, **kwds)


class filterTransform(VegaSchema):
    """filterTransform schema wrapper

    Mapping(required=[type, test])
    Filters elements from a data set to remove unwanted items.

    Attributes
    ----------

    test : string
        A string containing an expression (in JavaScript syntax) for the filter predicate.
    type : enum('filter')

    """
    _schema = {'$ref': '#/defs/filterTransform'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, **kwds):
        super(filterTransform, self).__init__(test=test, type=type, **kwds)


class foldTransform(VegaSchema):
    """foldTransform schema wrapper

    Mapping(required=[type, fields])
    Collapse ("fold") one or more data properties into two properties.

    Attributes
    ----------

    fields : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)

    type : enum('fold')

    output : Mapping(required=[])
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/foldTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, type=Undefined, output=Undefined, **kwds):
        super(foldTransform, self).__init__(fields=fields, type=type, output=output, **kwds)


class forceTransform(VegaSchema):
    """forceTransform schema wrapper

    Mapping(required=[type, links])
    Performs force-directed layout for network data.

    Attributes
    ----------

    links : string
        The name of the link (edge) data set.
    type : enum('force')

    active : :class:`signal`
        A signal representing the active node.
    alpha : oneOf(float, :class:`signal`)
        A "temperature" parameter that determines how much node positions are adjusted at
        each step.
    charge : oneOf(float, string, :class:`signal`)
        The strength of the charge each node exerts.
    chargeDistance : oneOf(float, :class:`signal`)
        The maximum distance over which charge forces are applied.
    fixed : string
        The name of a datasource containing the IDs of nodes with fixed positions.
    friction : oneOf(float, :class:`signal`)
        The strength of the friction force used to stabilize the layout.
    gravity : oneOf(float, :class:`signal`)
        The strength of the pseudo-gravity force that pulls nodes towards the center of the
        layout area.
    interactive : oneOf(boolean, :class:`signal`)
        Enables an interactive force-directed layout.
    iterations : oneOf(float, :class:`signal`)
        The number of iterations to run the force directed layout.
    linkDistance : oneOf(float, string, :class:`signal`)
        Determines the length of edges, in pixels.
    linkStrength : oneOf(float, string, :class:`signal`)
        Determines the tension of edges (the spring constant).
    output : Mapping(required=[])
        Rename the output data fields
    size : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The dimensions [width, height] of this force layout.
    theta : oneOf(float, :class:`signal`)
        The theta parameter for the Barnes-Hut algorithm, which is used to compute charge
        forces between nodes.
    """
    _schema = {'$ref': '#/defs/forceTransform'}
    _rootschema = Root._schema

    def __init__(self, links=Undefined, type=Undefined, active=Undefined, alpha=Undefined,
                 charge=Undefined, chargeDistance=Undefined, fixed=Undefined, friction=Undefined,
                 gravity=Undefined, interactive=Undefined, iterations=Undefined, linkDistance=Undefined,
                 linkStrength=Undefined, output=Undefined, size=Undefined, theta=Undefined, **kwds):
        super(forceTransform, self).__init__(links=links, type=type, active=active, alpha=alpha,
                                             charge=charge, chargeDistance=chargeDistance, fixed=fixed,
                                             friction=friction, gravity=gravity,
                                             interactive=interactive, iterations=iterations,
                                             linkDistance=linkDistance, linkStrength=linkStrength,
                                             output=output, size=size, theta=theta, **kwds)


class formulaTransform(VegaSchema):
    """formulaTransform schema wrapper

    Mapping(required=[type, field, expr])
    Extends data elements with new values according to a calculation formula.

    Attributes
    ----------

    expr : string
        A string containing an expression (in JavaScript syntax) for the formula.
    field : string
        The property name in which to store the computed formula value.
    type : enum('formula')

    """
    _schema = {'$ref': '#/defs/formulaTransform'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, field=Undefined, type=Undefined, **kwds):
        super(formulaTransform, self).__init__(expr=expr, field=field, type=type, **kwds)


class geoTransform(VegaSchema):
    """geoTransform schema wrapper

    Mapping(required=[type, lon, lat])
    Performs a cartographic projection. Given longitude and latitude values, sets corresponding
    x and y properties for a mark.

    Attributes
    ----------

    lat : oneOf(string, :class:`signal`)
        The input latitude values.
    lon : oneOf(string, :class:`signal`)
        The input longitude values.
    type : enum('geo')

    center : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The center of the projection.
    clipAngle : oneOf(float, :class:`signal`)
        The clip angle of the projection.
    clipExtent : oneOf(float, :class:`signal`)
        The clip extent of the projection.
    output : Mapping(required=[])
        Rename the output data fields
    precision : oneOf(float, :class:`signal`)
        The desired precision of the projection.
    projection : oneOf(string, :class:`signal`)
        The type of cartographic projection to use.
    rotate : oneOf(float, :class:`signal`)
        The rotation of the projection.
    scale : oneOf(float, :class:`signal`)
        The scale of the projection.
    translate : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The translation of the projection.
    """
    _schema = {'$ref': '#/defs/geoTransform'}
    _rootschema = Root._schema

    def __init__(self, lat=Undefined, lon=Undefined, type=Undefined, center=Undefined,
                 clipAngle=Undefined, clipExtent=Undefined, output=Undefined, precision=Undefined,
                 projection=Undefined, rotate=Undefined, scale=Undefined, translate=Undefined, **kwds):
        super(geoTransform, self).__init__(lat=lat, lon=lon, type=type, center=center,
                                           clipAngle=clipAngle, clipExtent=clipExtent, output=output,
                                           precision=precision, projection=projection, rotate=rotate,
                                           scale=scale, translate=translate, **kwds)


class geopathTransform(VegaSchema):
    """geopathTransform schema wrapper

    Mapping(required=[type])
    Creates paths for geographic regions, such as countries, states and counties.

    Attributes
    ----------

    type : enum('geopath')

    center : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The center of the projection.
    clipAngle : oneOf(float, :class:`signal`)
        The clip angle of the projection.
    clipExtent : oneOf(float, :class:`signal`)
        The clip extent of the projection.
    field : oneOf(string, :class:`signal`)
        The data field containing GeoJSON Feature data.
    output : Mapping(required=[])
        Rename the output data fields
    precision : oneOf(float, :class:`signal`)
        The desired precision of the projection.
    projection : oneOf(string, :class:`signal`)
        The type of cartographic projection to use.
    rotate : oneOf(float, :class:`signal`)
        The rotation of the projection.
    scale : oneOf(float, :class:`signal`)
        The scale of the projection.
    translate : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The translation of the projection.
    """
    _schema = {'$ref': '#/defs/geopathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, center=Undefined, clipAngle=Undefined, clipExtent=Undefined,
                 field=Undefined, output=Undefined, precision=Undefined, projection=Undefined,
                 rotate=Undefined, scale=Undefined, translate=Undefined, **kwds):
        super(geopathTransform, self).__init__(type=type, center=center, clipAngle=clipAngle,
                                               clipExtent=clipExtent, field=field, output=output,
                                               precision=precision, projection=projection,
                                               rotate=rotate, scale=scale, translate=translate, **kwds)


class hierarchyTransform(VegaSchema):
    """hierarchyTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('hierarchy')

    children : oneOf(string, :class:`signal`)
        The data field for the children node array
    field : oneOf(string, :class:`signal`)
        The value for the area of each leaf-level node for partition layouts.
    mode : oneOf(enum('tidy', 'cluster', 'partition'), :class:`signal`)
        The layout algorithm mode to use.
    nodesize : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        Sets a fixed x,y size for each node (overrides the size parameter)
    orient : oneOf(enum('cartesian', 'radial'), :class:`signal`)
        The layout orientation to use.
    output : Mapping(required=[])
        Rename the output data fields
    parent : oneOf(string, :class:`signal`)
        The data field for the parent node
    size : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The dimensions of the tree layout
    sort : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        A list of fields to use as sort criteria for sibling nodes.
    """
    _schema = {'$ref': '#/defs/hierarchyTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, children=Undefined, field=Undefined, mode=Undefined,
                 nodesize=Undefined, orient=Undefined, output=Undefined, parent=Undefined,
                 size=Undefined, sort=Undefined, **kwds):
        super(hierarchyTransform, self).__init__(type=type, children=children, field=field, mode=mode,
                                                 nodesize=nodesize, orient=orient, output=output,
                                                 parent=parent, size=size, sort=sort, **kwds)


class imputeTransform(VegaSchema):
    """imputeTransform schema wrapper

    Mapping(required=[type, groupby, orderby, field])
    Performs imputation of missing values.

    Attributes
    ----------

    field : oneOf(string, :class:`signal`)
        The data field to impute.
    groupby : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        A list of fields to group the data into series.
    orderby : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        A list of fields to determine ordering within series.
    type : enum('impute')

    method : oneOf(enum('value', 'mean', 'median', 'min', 'max'), :class:`signal`)
        The imputation method to use.
    value : oneOf(float, string, boolean, None, :class:`signal`)
        The value to use for missing data if the method is 'value'.
    """
    _schema = {'$ref': '#/defs/imputeTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, groupby=Undefined, orderby=Undefined, type=Undefined,
                 method=Undefined, value=Undefined, **kwds):
        super(imputeTransform, self).__init__(field=field, groupby=groupby, orderby=orderby, type=type,
                                              method=method, value=value, **kwds)


class lookupTransform(VegaSchema):
    """lookupTransform schema wrapper

    Mapping(required=[type, on, as, keys])
    Extends a data set by looking up values in another data set.

    Attributes
    ----------

    keys : List(oneOf(string, :class:`signal`))
        One or more fields in the primary data set to match against the secondary data set.
    on : string
        The name of the secondary data set on which to lookup values.
    type : enum('lookup')

    default : Mapping(required=[])
        The default value to use if a lookup match fails.
    onKey : oneOf(string, :class:`signal`)
        The key field to lookup, or null for index-based lookup.
    as : List(string)
        The names of the fields in which to store looked-up values.
    """
    _schema = {'$ref': '#/defs/lookupTransform'}
    _rootschema = Root._schema

    def __init__(self, keys=Undefined, on=Undefined, type=Undefined, default=Undefined, onKey=Undefined,
                 **kwds):
        super(lookupTransform, self).__init__(keys=keys, on=on, type=type, default=default, onKey=onKey,
                                              **kwds)


class pieTransform(VegaSchema):
    """pieTransform schema wrapper

    Mapping(required=[type])
    Computes a pie chart layout.

    Attributes
    ----------

    type : enum('pie')

    endAngle : oneOf(float, :class:`signal`)

    field : oneOf(string, :class:`signal`)
        The data values to encode as angular spans. If this property is omitted, all pie
        slices will have equal spans.
    output : Mapping(required=[])
        Rename the output data fields
    sort : oneOf(boolean, :class:`signal`)
        If true, will sort the data prior to computing angles.
    startAngle : oneOf(float, :class:`signal`)

    """
    _schema = {'$ref': '#/defs/pieTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, endAngle=Undefined, field=Undefined, output=Undefined,
                 sort=Undefined, startAngle=Undefined, **kwds):
        super(pieTransform, self).__init__(type=type, endAngle=endAngle, field=field, output=output,
                                           sort=sort, startAngle=startAngle, **kwds)


class rankTransform(VegaSchema):
    """rankTransform schema wrapper

    Mapping(required=[type])
    Computes ascending rank scores for data tuples.

    Attributes
    ----------

    type : enum('rank')

    field : oneOf(string, :class:`signal`)
        A key field to used to rank tuples. If undefined, tuples will be ranked in their
        observed order.
    normalize : oneOf(boolean, :class:`signal`)
        If true, values of the output field will lie in the range [0, 1].
    output : Mapping(required=[])
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/rankTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, normalize=Undefined, output=Undefined, **kwds):
        super(rankTransform, self).__init__(type=type, field=field, normalize=normalize, output=output,
                                            **kwds)


class sortTransform(VegaSchema):
    """sortTransform schema wrapper

    Mapping(required=[type, by])
    Sorts the values of a data set.

    Attributes
    ----------

    by : oneOf(string, List(string))
        A list of fields to use as sort criteria.
    type : enum('sort')

    """
    _schema = {'$ref': '#/defs/sortTransform'}
    _rootschema = Root._schema

    def __init__(self, by=Undefined, type=Undefined, **kwds):
        super(sortTransform, self).__init__(by=by, type=type, **kwds)


class stackTransform(VegaSchema):
    """stackTransform schema wrapper

    Mapping(required=[type, groupby, field])
    Computes layout values for stacked graphs, as in stacked bar charts or stream graphs.

    Attributes
    ----------

    field : oneOf(string, :class:`signal`)
        The data field that determines the thickness/height of stacks.
    groupby : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        A list of fields to split the data into groups (stacks).
    type : enum('stack')

    offset : oneOf(enum('zero', 'center', 'normalize'), :class:`signal`)
        The baseline offset
    output : Mapping(required=[])
        Rename the output data fields
    sortby : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        A list of fields to determine the sort order of stacks.
    """
    _schema = {'$ref': '#/defs/stackTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, groupby=Undefined, type=Undefined, offset=Undefined,
                 output=Undefined, sortby=Undefined, **kwds):
        super(stackTransform, self).__init__(field=field, groupby=groupby, type=type, offset=offset,
                                             output=output, sortby=sortby, **kwds)


class treeifyTransform(VegaSchema):
    """treeifyTransform schema wrapper

    Mapping(required=[type, groupby])

    Attributes
    ----------

    groupby : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        An ordered list of fields by which to group tuples into a tree.
    type : enum('treeify')

    output : Mapping(required=[])
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/treeifyTransform'}
    _rootschema = Root._schema

    def __init__(self, groupby=Undefined, type=Undefined, output=Undefined, **kwds):
        super(treeifyTransform, self).__init__(groupby=groupby, type=type, output=output, **kwds)


class treemapTransform(VegaSchema):
    """treemapTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('treemap')

    children : oneOf(string, :class:`signal`)
        The data field for the children node array
    field : oneOf(string, :class:`signal`)
        The values to use to determine the area of each leaf-level treemap cell.
    mode : oneOf(enum('squarify', 'slice', 'dice', 'slice-dice'), :class:`signal`)
        The treemap layout algorithm to use.
    output : Mapping(required=[])
        Rename the output data fields
    padding : oneOf(float, List(oneOf(float, :class:`signal`)), :class:`signal`)
        he padding (in pixels) to provide around internal nodes in the treemap.
    parent : oneOf(string, :class:`signal`)
        The data field for the parent node
    ratio : oneOf(float, :class:`signal`)
        The target aspect ratio for the layout to optimize.
    round : oneOf(boolean, :class:`signal`)
        If true, treemap cell dimensions will be rounded to integer pixels.
    size : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The dimensions of the treemap layout
    sort : oneOf(List(oneOf(string, :class:`signal`)), :class:`signal`)
        A list of fields to use as sort criteria for sibling nodes.
    sticky : oneOf(boolean, :class:`signal`)
        If true, repeated runs of the treemap will use cached partition boundaries.
    """
    _schema = {'$ref': '#/defs/treemapTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, children=Undefined, field=Undefined, mode=Undefined,
                 output=Undefined, padding=Undefined, parent=Undefined, ratio=Undefined,
                 round=Undefined, size=Undefined, sort=Undefined, sticky=Undefined, **kwds):
        super(treemapTransform, self).__init__(type=type, children=children, field=field, mode=mode,
                                               output=output, padding=padding, parent=parent,
                                               ratio=ratio, round=round, size=size, sort=sort,
                                               sticky=sticky, **kwds)


class voronoiTransform(VegaSchema):
    """voronoiTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('voronoi')

    clipExtent : oneOf(List(oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)),
    :class:`signal`)
        The min and max points at which to clip the voronoi diagram.
    output : Mapping(required=[])
        Rename the output data fields
    x : oneOf(string, :class:`signal`)
        The input x coordinates.
    y : oneOf(string, :class:`signal`)
        The input y coordinates.
    """
    _schema = {'$ref': '#/defs/voronoiTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clipExtent=Undefined, output=Undefined, x=Undefined, y=Undefined,
                 **kwds):
        super(voronoiTransform, self).__init__(type=type, clipExtent=clipExtent, output=output, x=x,
                                               y=y, **kwds)


class wordcloudTransform(VegaSchema):
    """wordcloudTransform schema wrapper

    Mapping(required=[type])

    Attributes
    ----------

    type : enum('wordcloud')

    font : oneOf(string, oneOf(Mapping(required=[field]), Mapping(required=[value])),
    :class:`signal`)
        The font face to use for a word.
    fontScale : oneOf(None, List(oneOf(float, :class:`signal`)))
        The minimum and maximum scaled font sizes, or null to prevent scaling.
    fontSize : oneOf(float, oneOf(Mapping(required=[field]), Mapping(required=[value])), string,
    :class:`signal`)
        The font size to use for a word.
    fontStyle : oneOf(string, oneOf(Mapping(required=[field]), Mapping(required=[value])),
    :class:`signal`)
        The font style to use for a word.
    fontWeight : oneOf(string, oneOf(Mapping(required=[field]), Mapping(required=[value])),
    :class:`signal`)
        The font weight to use for a word.
    output : Mapping(required=[])
        Rename the output data fields
    padding : oneOf(float, oneOf(Mapping(required=[field]), Mapping(required=[value])),
    :class:`signal`)
        The padding around each word.
    rotate : oneOf(float, string, oneOf(Mapping(required=[field]), Mapping(required=[value])),
    :class:`signal`)
        The field or number to set the roration angle (in degrees).
    size : oneOf(List(oneOf(float, :class:`signal`)), :class:`signal`)
        The dimensions of the wordcloud layout
    spiral : oneOf(enum('archimedean', 'rectangular'), oneOf(Mapping(required=[field]),
    Mapping(required=[value])), :class:`signal`)
        The type of spiral used for positioning words, either 'archimedean' or
        'rectangular'.
    text : oneOf(string, oneOf(Mapping(required=[field]), Mapping(required=[value])),
    :class:`signal`)
        The field containing the text to use for each word.
    """
    _schema = {'$ref': '#/defs/wordcloudTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, font=Undefined, fontScale=Undefined, fontSize=Undefined,
                 fontStyle=Undefined, fontWeight=Undefined, output=Undefined, padding=Undefined,
                 rotate=Undefined, size=Undefined, spiral=Undefined, text=Undefined, **kwds):
        super(wordcloudTransform, self).__init__(type=type, font=font, fontScale=fontScale,
                                                 fontSize=fontSize, fontStyle=fontStyle,
                                                 fontWeight=fontWeight, output=output, padding=padding,
                                                 rotate=rotate, size=size, spiral=spiral, text=text,
                                                 **kwds)


class transform(VegaSchema):
    """transform schema wrapper

    List(oneOf(:class:`aggregateTransform`, :class:`binTransform`, :class:`crossTransform`,
    :class:`countpatternTransform`, :class:`linkpathTransform`, :class:`facetTransform`,
    :class:`filterTransform`, :class:`foldTransform`, :class:`forceTransform`,
    :class:`formulaTransform`, :class:`geoTransform`, :class:`geopathTransform`,
    :class:`hierarchyTransform`, :class:`imputeTransform`, :class:`lookupTransform`,
    :class:`pieTransform`, :class:`rankTransform`, :class:`sortTransform`,
    :class:`stackTransform`, :class:`treeifyTransform`, :class:`treemapTransform`,
    :class:`voronoiTransform`, :class:`wordcloudTransform`))
    """
    _schema = {'$ref': '#/defs/transform'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(transform, self).__init__(*args)


class scale(VegaSchema):
    """scale schema wrapper

    allOf(Mapping(required=[name]), oneOf(Mapping(required=[type]), Mapping(required=[type]),
    anyOf(Mapping(required=[]), Mapping(required=[type]))))
    """
    _schema = {'$ref': '#/defs/scale'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, domain=Undefined, domainMax=Undefined, domainMin=Undefined,
                 rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined,
                 type=Undefined, **kwds):
        super(scale, self).__init__(name=name, domain=domain, domainMax=domainMax, domainMin=domainMin,
                                    rangeMax=rangeMax, rangeMin=rangeMin, reverse=reverse, round=round,
                                    type=type, **kwds)


class operand(VegaSchema):
    """operand schema wrapper

    oneOf(Mapping(required=[value]), Mapping(required=[arg]), :class:`signal`,
    Mapping(required=[predicate]))
    """
    _schema = {'$ref': '#/refs/operand'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(operand, self).__init__(*args, **kwds)


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

    oneOf(:class:`field`, Mapping(required=[name]))
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

    mult : float

    offset : float

    scale : :class:`scale`

    """
    _schema = {'$ref': '#/refs/numberModifiers'}
    _rootschema = Root._schema

    def __init__(self, mult=Undefined, offset=Undefined, scale=Undefined, **kwds):
        super(numberModifiers, self).__init__(mult=mult, offset=offset, scale=scale, **kwds)


class value(VegaSchema):
    """value schema wrapper

    oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))), allOf(:class:`stringModifiers`, oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[band]))))
    """
    _schema = {'$ref': '#/refs/value'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(value, self).__init__(*args, **kwds)


class numberValue(VegaSchema):
    """numberValue schema wrapper

    oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`, allOf(:class:`numberModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))), allOf(:class:`numberModifiers`, oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[band]))))
    """
    _schema = {'$ref': '#/refs/numberValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(numberValue, self).__init__(*args, **kwds)


class stringValue(VegaSchema):
    """stringValue schema wrapper

    oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]), Mapping(required=[template]))))), allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]), Mapping(required=[template]))))
    """
    _schema = {'$ref': '#/refs/stringValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(stringValue, self).__init__(*args, **kwds)


class booleanValue(VegaSchema):
    """booleanValue schema wrapper

    oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))), allOf(:class:`stringModifiers`, oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[band]))))
    """
    _schema = {'$ref': '#/refs/booleanValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(booleanValue, self).__init__(*args, **kwds)


class arrayValue(VegaSchema):
    """arrayValue schema wrapper

    oneOf(Mapping(required=[rule]), List(allOf(:class:`rule`, allOf(:class:`stringModifiers`,
    oneOf(:class:`signal`, Mapping(required=[value]), Mapping(required=[field]),
    Mapping(required=[band]))))), allOf(:class:`stringModifiers`, oneOf(:class:`signal`,
    Mapping(required=[value]), Mapping(required=[field]), Mapping(required=[band]))))
    """
    _schema = {'$ref': '#/refs/arrayValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(arrayValue, self).__init__(*args, **kwds)


class colorValue(VegaSchema):
    """colorValue schema wrapper

    oneOf(:class:`stringValue`, Mapping(required=[r, g, b]), Mapping(required=[h, s, l]),
    Mapping(required=[l, a, b]), Mapping(required=[h, c, l]))
    """
    _schema = {'$ref': '#/refs/colorValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(colorValue, self).__init__(*args, **kwds)


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


class scopedScale(VegaSchema):
    """scopedScale schema wrapper

    oneOf(string, Mapping(required=[name]))
    """
    _schema = {'$ref': '#/refs/scopedScale'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scopedScale, self).__init__(*args, **kwds)


class data(VegaSchema):
    """data schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    data : oneOf(string, Mapping(required=[fields]))

    field : oneOf(string, List(string), Mapping(required=[parent]),
    List(Mapping(required=[parent])))

    sort : oneOf(boolean, Mapping(required=[]))

    """
    _schema = {'$ref': '#/refs/data'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, field=Undefined, sort=Undefined, **kwds):
        super(data, self).__init__(data=data, field=field, sort=sort, **kwds)

