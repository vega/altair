# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# 2018-02-22 15:42

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

    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)
    


class axis(SchemaBase):
    """axis schema wrapper
    
    Attributes
    ----------
    type : any
        
    scale : string
        
    orient : any
        
    title : string
        
    titleOffset : float
        
    format : string
        
    formatType : any
        
    ticks : float
        
    values : list
        
    subdivide : float
        
    tickPadding : float
        
    tickSize : float
        
    tickSizeMajor : float
        
    tickSizeMinor : float
        
    tickSizeEnd : float
        
    offset : oneOf(float, mapping)
        
    layer : any
        
    grid : boolean
        
    properties : mapping
        
    """
    _schema = {'$ref': '#/defs/axis'}
    _rootschema = Root._schema

    def __init__(self, scale=Undefined, type=Undefined, format=Undefined, formatType=Undefined, grid=Undefined, layer=Undefined, offset=Undefined, orient=Undefined, properties=Undefined, subdivide=Undefined, tickPadding=Undefined, tickSize=Undefined, tickSizeEnd=Undefined, tickSizeMajor=Undefined, tickSizeMinor=Undefined, ticks=Undefined, title=Undefined, titleOffset=Undefined, values=Undefined, **kwds):
        super(axis, self).__init__(scale=scale, type=type, format=format, formatType=formatType, grid=grid, layer=layer, offset=offset, orient=orient, properties=properties, subdivide=subdivide, tickPadding=tickPadding, tickSize=tickSize, tickSizeEnd=tickSizeEnd, tickSizeMajor=tickSizeMajor, tickSizeMinor=tickSizeMinor, ticks=ticks, title=title, titleOffset=titleOffset, values=values, **kwds)
    


class background(SchemaBase):
    """background schema wrapper"""
    _schema = {'$ref': '#/defs/background'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(background, self).__init__(*args)
    


class data(SchemaBase):
    """data schema wrapper"""
    _schema = {'$ref': '#/defs/data'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(data, self).__init__(*args, **kwds)
    


class legend(SchemaBase):
    """legend schema wrapper
    
    Attributes
    ----------
    size : string
        
    shape : string
        
    fill : string
        
    stroke : string
        
    opacity : string
        
    orient : any
        
    offset : float
        
    title : string
        
    values : list
        
    format : string
        
    formatType : any
        
    properties : mapping
        
    """
    _schema = {'$ref': '#/defs/legend'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(legend, self).__init__(*args, **kwds)
    


class mark(SchemaBase):
    """mark schema wrapper
    
    Attributes
    ----------
    name : string
        
    key : string
        
    type : any
        
    from : mapping
        
    delay : numberValue
        
    ease : any
        
    interactive : boolean
        
    properties : anyOf(any, any)
        
    """
    _schema = {'$ref': '#/defs/mark'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, delay=Undefined, ease=Undefined, interactive=Undefined, key=Undefined, name=Undefined, properties=Undefined, **kwds):
        super(mark, self).__init__(type=type, delay=delay, ease=ease, interactive=interactive, key=key, name=name, properties=properties, **kwds)
    


class container(SchemaBase):
    """container schema wrapper
    
    Attributes
    ----------
    scene : mapping
        
    scales : list
        
    axes : list
        
    legends : list
        
    marks : list
        
    """
    _schema = {'$ref': '#/defs/container'}
    _rootschema = Root._schema

    def __init__(self, axes=Undefined, legends=Undefined, marks=Undefined, scales=Undefined, scene=Undefined, **kwds):
        super(container, self).__init__(axes=axes, legends=legends, marks=marks, scales=scales, scene=scene, **kwds)
    


class groupMark(SchemaBase):
    """groupMark schema wrapper"""
    _schema = {'$ref': '#/defs/groupMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(groupMark, self).__init__(*args, **kwds)
    


class visualMark(SchemaBase):
    """visualMark schema wrapper"""
    _schema = {'$ref': '#/defs/visualMark'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(visualMark, self).__init__(*args, **kwds)
    


class modify(SchemaBase):
    """modify schema wrapper"""
    _schema = {'$ref': '#/defs/modify'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(modify, self).__init__(*args)
    


class padding(SchemaBase):
    """padding schema wrapper"""
    _schema = {'$ref': '#/defs/padding'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(padding, self).__init__(*args, **kwds)
    


class predicate(SchemaBase):
    """predicate schema wrapper"""
    _schema = {'$ref': '#/defs/predicate'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(predicate, self).__init__(*args, **kwds)
    


class rule(SchemaBase):
    """rule schema wrapper"""
    _schema = {'$ref': '#/defs/rule'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(rule, self).__init__(*args, **kwds)
    


class propset(SchemaBase):
    """propset schema wrapper
    
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
        
    shape : anyOf(oneOf(mapping, list, allOf(stringModifiers, oneOf(signal, any, any, any))), stringValue)
        
    path : stringValue
        
    innerRadius : numberValue
        
    outerRadius : numberValue
        
    startAngle : numberValue
        
    endAngle : numberValue
        
    interpolate : oneOf(mapping, list, allOf(stringModifiers, oneOf(signal, any, any, any)))
        
    tension : numberValue
        
    orient : oneOf(mapping, list, allOf(stringModifiers, oneOf(signal, any, any, any)))
        
    url : stringValue
        
    align : oneOf(mapping, list, allOf(stringModifiers, oneOf(signal, any, any, any)))
        
    baseline : oneOf(mapping, list, allOf(stringModifiers, oneOf(signal, any, any, any)))
        
    text : stringValue
        
    dx : numberValue
        
    dy : numberValue
        
    radius : numberValue
        
    theta : numberValue
        
    angle : numberValue
        
    font : stringValue
        
    fontSize : numberValue
        
    fontWeight : stringValue
        
    fontStyle : stringValue
        
    """
    _schema = {'$ref': '#/defs/propset'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, baseline=Undefined, clip=Undefined, cursor=Undefined, dx=Undefined, dy=Undefined, endAngle=Undefined, fill=Undefined, fillOpacity=Undefined, font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, height=Undefined, innerRadius=Undefined, interpolate=Undefined, opacity=Undefined, orient=Undefined, outerRadius=Undefined, path=Undefined, radius=Undefined, shape=Undefined, size=Undefined, startAngle=Undefined, stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined, strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined, url=Undefined, width=Undefined, x=Undefined, x2=Undefined, xc=Undefined, y=Undefined, y2=Undefined, yc=Undefined, **kwds):
        super(propset, self).__init__(align=align, angle=angle, baseline=baseline, clip=clip, cursor=cursor, dx=dx, dy=dy, endAngle=endAngle, fill=fill, fillOpacity=fillOpacity, font=font, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, height=height, innerRadius=innerRadius, interpolate=interpolate, opacity=opacity, orient=orient, outerRadius=outerRadius, path=path, radius=radius, shape=shape, size=size, startAngle=startAngle, stroke=stroke, strokeDash=strokeDash, strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity, strokeWidth=strokeWidth, tension=tension, text=text, theta=theta, url=url, width=width, x=x, x2=x2, xc=xc, y=y, y2=y2, yc=yc, **kwds)
    


class signal(SchemaBase):
    """signal schema wrapper
    
    Attributes
    ----------
    name : not SchemaInfo({
  
})
        
    init : any
        
    verbose : boolean
        
    expr : string
        
    scale : scopedScale
        
    streams : streams
        
    """
    _schema = {'$ref': '#/defs/signal'}
    _rootschema = Root._schema

    def __init__(self, name=Undefined, expr=Undefined, init=Undefined, scale=Undefined, streams=Undefined, verbose=Undefined, **kwds):
        super(signal, self).__init__(name=name, expr=expr, init=init, scale=scale, streams=streams, verbose=verbose, **kwds)
    


class spec(SchemaBase):
    """spec schema wrapper"""
    _schema = {'$ref': '#/defs/spec'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(spec, self).__init__(*args, **kwds)
    


class streams(SchemaBase):
    """streams schema wrapper"""
    _schema = {'$ref': '#/defs/streams'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(streams, self).__init__(*args)
    


class aggregateTransform(SchemaBase):
    """aggregateTransform schema wrapper
    
    Compute summary aggregate statistics
    
    Attributes
    ----------
    type : any
        
    groupby : list
        A list of fields to split the data into groups.
    summarize : oneOf(mapping, list)
        
    """
    _schema = {'$ref': '#/defs/aggregateTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, groupby=Undefined, summarize=Undefined, **kwds):
        super(aggregateTransform, self).__init__(type=type, groupby=groupby, summarize=summarize, **kwds)
    


class binTransform(SchemaBase):
    """binTransform schema wrapper
    
    Bins values into quantitative bins (e.g., for a histogram).
    
    Attributes
    ----------
    type : any
        
    field : oneOf(string, signal)
        The name of the field to bin values from.
    min : oneOf(float, signal)
        The minimum bin value to consider.
    max : oneOf(float, signal)
        The maximum bin value to consider.
    base : oneOf(float, signal)
        The number base to use for automatic bin determination.
    maxbins : oneOf(float, signal)
        The maximum number of allowable bins.
    step : oneOf(float, signal)
        An exact step size to use between bins. If provided, options such as maxbins will be ignored.
    steps : oneOf(list, signal)
        An array of allowable step sizes to choose from.
    minstep : oneOf(float, signal)
        A minimum allowable step size (particularly useful for integer values).
    div : oneOf(list, signal)
        An array of scale factors indicating allowable subdivisions.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/binTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, type=Undefined, base=Undefined, div=Undefined, max=Undefined, maxbins=Undefined, min=Undefined, minstep=Undefined, output=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(binTransform, self).__init__(field=field, type=type, base=base, div=div, max=max, maxbins=maxbins, min=min, minstep=minstep, output=output, step=step, steps=steps, **kwds)
    


class crossTransform(SchemaBase):
    """crossTransform schema wrapper
    
    Compute the cross-product of two data sets.
    
    Attributes
    ----------
    type : any
        
    with : string
        The name of the secondary data set to cross with the primary data. If unspecified, the primary data is crossed with itself.
    diagonal : oneOf(boolean, signal)
        If false, items along the "diagonal" of the cross-product (those elements with the same index in their respective array) will not be included in the output.
    filter : string
        A string containing an expression (in JavaScript syntax) to filter the resulting data elements.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/crossTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, diagonal=Undefined, filter=Undefined, output=Undefined, **kwds):
        super(crossTransform, self).__init__(type=type, diagonal=diagonal, filter=filter, output=output, **kwds)
    


class countpatternTransform(SchemaBase):
    """countpatternTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    field : oneOf(string, signal)
        The field containing the text to analyze.
    pattern : oneOf(string, signal)
        A regexp pattern for matching words in text.
    case : oneOf(any, signal)
        Text case transformation to apply.
    stopwords : oneOf(string, signal)
        A regexp pattern for matching stopwords to omit.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/countpatternTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, case=Undefined, field=Undefined, output=Undefined, pattern=Undefined, stopwords=Undefined, **kwds):
        super(countpatternTransform, self).__init__(type=type, case=case, field=field, output=output, pattern=pattern, stopwords=stopwords, **kwds)
    


class linkpathTransform(SchemaBase):
    """linkpathTransform schema wrapper
    
    Computes a path definition for connecting nodes within a node-link network or tree diagram.
    
    Attributes
    ----------
    type : any
        
    sourceX : oneOf(string, signal)
        The data field that references the source x-coordinate for this link.
    sourceY : oneOf(string, signal)
        The data field that references the source y-coordinate for this link.
    targetX : oneOf(string, signal)
        The data field that references the target x-coordinate for this link.
    targetY : oneOf(string, signal)
        The data field that references the target y-coordinate for this link.
    tension : oneOf(float, signal)
        A tension parameter for the "tightness" of "curve"-shaped links.
    shape : oneOf(any, signal)
        The path shape to use
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/linkpathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, output=Undefined, shape=Undefined, sourceX=Undefined, sourceY=Undefined, targetX=Undefined, targetY=Undefined, tension=Undefined, **kwds):
        super(linkpathTransform, self).__init__(type=type, output=output, shape=shape, sourceX=sourceX, sourceY=sourceY, targetX=targetX, targetY=targetY, tension=tension, **kwds)
    


class facetTransform(SchemaBase):
    """facetTransform schema wrapper
    
    A special aggregate transform that organizes a data set into groups or "facets".
    
    Attributes
    ----------
    type : any
        
    groupby : list
        A list of fields to split the data into groups.
    summarize : oneOf(mapping, list)
        
    transform : transform
        
    """
    _schema = {'$ref': '#/defs/facetTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, groupby=Undefined, summarize=Undefined, transform=Undefined, **kwds):
        super(facetTransform, self).__init__(type=type, groupby=groupby, summarize=summarize, transform=transform, **kwds)
    


class filterTransform(SchemaBase):
    """filterTransform schema wrapper
    
    Filters elements from a data set to remove unwanted items.
    
    Attributes
    ----------
    type : any
        
    test : string
        A string containing an expression (in JavaScript syntax) for the filter predicate.
    """
    _schema = {'$ref': '#/defs/filterTransform'}
    _rootschema = Root._schema

    def __init__(self, test=Undefined, type=Undefined, **kwds):
        super(filterTransform, self).__init__(test=test, type=type, **kwds)
    


class foldTransform(SchemaBase):
    """foldTransform schema wrapper
    
    Collapse ("fold") one or more data properties into two properties.
    
    Attributes
    ----------
    type : any
        
    fields : oneOf(list, signal)
        
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/foldTransform'}
    _rootschema = Root._schema

    def __init__(self, fields=Undefined, type=Undefined, output=Undefined, **kwds):
        super(foldTransform, self).__init__(fields=fields, type=type, output=output, **kwds)
    


class forceTransform(SchemaBase):
    """forceTransform schema wrapper
    
    Performs force-directed layout for network data.
    
    Attributes
    ----------
    type : any
        
    size : oneOf(list, signal)
        The dimensions [width, height] of this force layout.
    links : string
        The name of the link (edge) data set.
    linkDistance : oneOf(float, string, signal)
        Determines the length of edges, in pixels.
    linkStrength : oneOf(float, string, signal)
        Determines the tension of edges (the spring constant).
    charge : oneOf(float, string, signal)
        The strength of the charge each node exerts.
    chargeDistance : oneOf(float, signal)
        The maximum distance over which charge forces are applied.
    iterations : oneOf(float, signal)
        The number of iterations to run the force directed layout.
    friction : oneOf(float, signal)
        The strength of the friction force used to stabilize the layout.
    theta : oneOf(float, signal)
        The theta parameter for the Barnes-Hut algorithm, which is used to compute charge forces between nodes.
    gravity : oneOf(float, signal)
        The strength of the pseudo-gravity force that pulls nodes towards the center of the layout area.
    alpha : oneOf(float, signal)
        A "temperature" parameter that determines how much node positions are adjusted at each step.
    interactive : oneOf(boolean, signal)
        Enables an interactive force-directed layout.
    active : signal
        A signal representing the active node.
    fixed : string
        The name of a datasource containing the IDs of nodes with fixed positions.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/forceTransform'}
    _rootschema = Root._schema

    def __init__(self, links=Undefined, type=Undefined, active=Undefined, alpha=Undefined, charge=Undefined, chargeDistance=Undefined, fixed=Undefined, friction=Undefined, gravity=Undefined, interactive=Undefined, iterations=Undefined, linkDistance=Undefined, linkStrength=Undefined, output=Undefined, size=Undefined, theta=Undefined, **kwds):
        super(forceTransform, self).__init__(links=links, type=type, active=active, alpha=alpha, charge=charge, chargeDistance=chargeDistance, fixed=fixed, friction=friction, gravity=gravity, interactive=interactive, iterations=iterations, linkDistance=linkDistance, linkStrength=linkStrength, output=output, size=size, theta=theta, **kwds)
    


class formulaTransform(SchemaBase):
    """formulaTransform schema wrapper
    
    Extends data elements with new values according to a calculation formula.
    
    Attributes
    ----------
    type : any
        
    field : string
        The property name in which to store the computed formula value.
    expr : string
        A string containing an expression (in JavaScript syntax) for the formula.
    """
    _schema = {'$ref': '#/defs/formulaTransform'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, field=Undefined, type=Undefined, **kwds):
        super(formulaTransform, self).__init__(expr=expr, field=field, type=type, **kwds)
    


class geoTransform(SchemaBase):
    """geoTransform schema wrapper
    
    Performs a cartographic projection. Given longitude and latitude values, sets corresponding x and y properties for a mark.
    
    Attributes
    ----------
    type : any
        
    lon : oneOf(string, signal)
        The input longitude values.
    lat : oneOf(string, signal)
        The input latitude values.
    output : mapping
        Rename the output data fields
    projection : oneOf(string, signal)
        The type of cartographic projection to use.
    center : oneOf(list, signal)
        The center of the projection.
    translate : oneOf(list, signal)
        The translation of the projection.
    rotate : oneOf(float, signal)
        The rotation of the projection.
    scale : oneOf(float, signal)
        The scale of the projection.
    precision : oneOf(float, signal)
        The desired precision of the projection.
    clipAngle : oneOf(float, signal)
        The clip angle of the projection.
    clipExtent : oneOf(float, signal)
        The clip extent of the projection.
    """
    _schema = {'$ref': '#/defs/geoTransform'}
    _rootschema = Root._schema

    def __init__(self, lat=Undefined, lon=Undefined, type=Undefined, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, output=Undefined, precision=Undefined, projection=Undefined, rotate=Undefined, scale=Undefined, translate=Undefined, **kwds):
        super(geoTransform, self).__init__(lat=lat, lon=lon, type=type, center=center, clipAngle=clipAngle, clipExtent=clipExtent, output=output, precision=precision, projection=projection, rotate=rotate, scale=scale, translate=translate, **kwds)
    


class geopathTransform(SchemaBase):
    """geopathTransform schema wrapper
    
    Creates paths for geographic regions, such as countries, states and counties.
    
    Attributes
    ----------
    type : any
        
    field : oneOf(string, signal)
        The data field containing GeoJSON Feature data.
    output : mapping
        Rename the output data fields
    projection : oneOf(string, signal)
        The type of cartographic projection to use.
    center : oneOf(list, signal)
        The center of the projection.
    translate : oneOf(list, signal)
        The translation of the projection.
    rotate : oneOf(float, signal)
        The rotation of the projection.
    scale : oneOf(float, signal)
        The scale of the projection.
    precision : oneOf(float, signal)
        The desired precision of the projection.
    clipAngle : oneOf(float, signal)
        The clip angle of the projection.
    clipExtent : oneOf(float, signal)
        The clip extent of the projection.
    """
    _schema = {'$ref': '#/defs/geopathTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, center=Undefined, clipAngle=Undefined, clipExtent=Undefined, field=Undefined, output=Undefined, precision=Undefined, projection=Undefined, rotate=Undefined, scale=Undefined, translate=Undefined, **kwds):
        super(geopathTransform, self).__init__(type=type, center=center, clipAngle=clipAngle, clipExtent=clipExtent, field=field, output=output, precision=precision, projection=projection, rotate=rotate, scale=scale, translate=translate, **kwds)
    


class hierarchyTransform(SchemaBase):
    """hierarchyTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    sort : oneOf(list, signal)
        A list of fields to use as sort criteria for sibling nodes.
    children : oneOf(string, signal)
        The data field for the children node array
    parent : oneOf(string, signal)
        The data field for the parent node
    field : oneOf(string, signal)
        The value for the area of each leaf-level node for partition layouts.
    mode : oneOf(any, signal)
        The layout algorithm mode to use.
    orient : oneOf(any, signal)
        The layout orientation to use.
    size : oneOf(list, signal)
        The dimensions of the tree layout
    nodesize : oneOf(list, signal)
        Sets a fixed x,y size for each node (overrides the size parameter)
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/hierarchyTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, children=Undefined, field=Undefined, mode=Undefined, nodesize=Undefined, orient=Undefined, output=Undefined, parent=Undefined, size=Undefined, sort=Undefined, **kwds):
        super(hierarchyTransform, self).__init__(type=type, children=children, field=field, mode=mode, nodesize=nodesize, orient=orient, output=output, parent=parent, size=size, sort=sort, **kwds)
    


class imputeTransform(SchemaBase):
    """imputeTransform schema wrapper
    
    Performs imputation of missing values.
    
    Attributes
    ----------
    type : any
        
    method : oneOf(any, signal)
        The imputation method to use.
    value : oneOf(float, string, boolean, None, signal)
        The value to use for missing data if the method is 'value'.
    field : oneOf(string, signal)
        The data field to impute.
    groupby : oneOf(list, signal)
        A list of fields to group the data into series.
    orderby : oneOf(list, signal)
        A list of fields to determine ordering within series.
    """
    _schema = {'$ref': '#/defs/imputeTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, groupby=Undefined, orderby=Undefined, type=Undefined, method=Undefined, value=Undefined, **kwds):
        super(imputeTransform, self).__init__(field=field, groupby=groupby, orderby=orderby, type=type, method=method, value=value, **kwds)
    


class lookupTransform(SchemaBase):
    """lookupTransform schema wrapper
    
    Extends a data set by looking up values in another data set.
    
    Attributes
    ----------
    type : any
        
    on : string
        The name of the secondary data set on which to lookup values.
    onKey : oneOf(string, signal)
        The key field to lookup, or null for index-based lookup.
    keys : list
        One or more fields in the primary data set to match against the secondary data set.
    as : list
        The names of the fields in which to store looked-up values.
    default : any
        The default value to use if a lookup match fails.
    """
    _schema = {'$ref': '#/defs/lookupTransform'}
    _rootschema = Root._schema

    def __init__(self, keys=Undefined, on=Undefined, type=Undefined, default=Undefined, onKey=Undefined, **kwds):
        super(lookupTransform, self).__init__(keys=keys, on=on, type=type, default=default, onKey=onKey, **kwds)
    


class pieTransform(SchemaBase):
    """pieTransform schema wrapper
    
    Computes a pie chart layout.
    
    Attributes
    ----------
    type : any
        
    field : oneOf(string, signal)
        The data values to encode as angular spans. If this property is omitted, all pie slices will have equal spans.
    startAngle : oneOf(float, signal)
        
    endAngle : oneOf(float, signal)
        
    sort : oneOf(boolean, signal)
         If true, will sort the data prior to computing angles.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/pieTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, endAngle=Undefined, field=Undefined, output=Undefined, sort=Undefined, startAngle=Undefined, **kwds):
        super(pieTransform, self).__init__(type=type, endAngle=endAngle, field=field, output=output, sort=sort, startAngle=startAngle, **kwds)
    


class rankTransform(SchemaBase):
    """rankTransform schema wrapper
    
    Computes ascending rank scores for data tuples.
    
    Attributes
    ----------
    type : any
        
    field : oneOf(string, signal)
        A key field to used to rank tuples. If undefined, tuples will be ranked in their observed order.
    normalize : oneOf(boolean, signal)
        If true, values of the output field will lie in the range [0, 1].
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/rankTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, field=Undefined, normalize=Undefined, output=Undefined, **kwds):
        super(rankTransform, self).__init__(type=type, field=field, normalize=normalize, output=output, **kwds)
    


class sortTransform(SchemaBase):
    """sortTransform schema wrapper
    
    Sorts the values of a data set.
    
    Attributes
    ----------
    type : any
        
    by : oneOf(string, list)
        A list of fields to use as sort criteria.
    """
    _schema = {'$ref': '#/defs/sortTransform'}
    _rootschema = Root._schema

    def __init__(self, by=Undefined, type=Undefined, **kwds):
        super(sortTransform, self).__init__(by=by, type=type, **kwds)
    


class stackTransform(SchemaBase):
    """stackTransform schema wrapper
    
    Computes layout values for stacked graphs, as in stacked bar charts or stream graphs.
    
    Attributes
    ----------
    type : any
        
    groupby : oneOf(list, signal)
        A list of fields to split the data into groups (stacks).
    sortby : oneOf(list, signal)
        A list of fields to determine the sort order of stacks.
    field : oneOf(string, signal)
        The data field that determines the thickness/height of stacks.
    offset : oneOf(any, signal)
        The baseline offset
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/stackTransform'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, groupby=Undefined, type=Undefined, offset=Undefined, output=Undefined, sortby=Undefined, **kwds):
        super(stackTransform, self).__init__(field=field, groupby=groupby, type=type, offset=offset, output=output, sortby=sortby, **kwds)
    


class treeifyTransform(SchemaBase):
    """treeifyTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    groupby : oneOf(list, signal)
        An ordered list of fields by which to group tuples into a tree.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/treeifyTransform'}
    _rootschema = Root._schema

    def __init__(self, groupby=Undefined, type=Undefined, output=Undefined, **kwds):
        super(treeifyTransform, self).__init__(groupby=groupby, type=type, output=output, **kwds)
    


class treemapTransform(SchemaBase):
    """treemapTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    sort : oneOf(list, signal)
        A list of fields to use as sort criteria for sibling nodes.
    children : oneOf(string, signal)
        The data field for the children node array
    parent : oneOf(string, signal)
        The data field for the parent node
    field : oneOf(string, signal)
        The values to use to determine the area of each leaf-level treemap cell.
    mode : oneOf(any, signal)
        The treemap layout algorithm to use.
    size : oneOf(list, signal)
        The dimensions of the treemap layout
    round : oneOf(boolean, signal)
        If true, treemap cell dimensions will be rounded to integer pixels.
    sticky : oneOf(boolean, signal)
        If true, repeated runs of the treemap will use cached partition boundaries.
    ratio : oneOf(float, signal)
        The target aspect ratio for the layout to optimize.
    padding : oneOf(float, list, signal)
        he padding (in pixels) to provide around internal nodes in the treemap.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/treemapTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, children=Undefined, field=Undefined, mode=Undefined, output=Undefined, padding=Undefined, parent=Undefined, ratio=Undefined, round=Undefined, size=Undefined, sort=Undefined, sticky=Undefined, **kwds):
        super(treemapTransform, self).__init__(type=type, children=children, field=field, mode=mode, output=output, padding=padding, parent=parent, ratio=ratio, round=round, size=size, sort=sort, sticky=sticky, **kwds)
    


class voronoiTransform(SchemaBase):
    """voronoiTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    clipExtent : oneOf(list, signal)
        The min and max points at which to clip the voronoi diagram.
    x : oneOf(string, signal)
        The input x coordinates.
    y : oneOf(string, signal)
        The input y coordinates.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/voronoiTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, clipExtent=Undefined, output=Undefined, x=Undefined, y=Undefined, **kwds):
        super(voronoiTransform, self).__init__(type=type, clipExtent=clipExtent, output=output, x=x, y=y, **kwds)
    


class wordcloudTransform(SchemaBase):
    """wordcloudTransform schema wrapper
    
    Attributes
    ----------
    type : any
        
    size : oneOf(list, signal)
        The dimensions of the wordcloud layout
    font : oneOf(string, oneOf(any, any), signal)
        The font face to use for a word.
    fontStyle : oneOf(string, oneOf(any, any), signal)
        The font style to use for a word.
    fontWeight : oneOf(string, oneOf(any, any), signal)
        The font weight to use for a word.
    fontSize : oneOf(float, oneOf(any, any), string, signal)
        The font size to use for a word.
    fontScale : oneOf(None, list)
        The minimum and maximum scaled font sizes, or null to prevent scaling.
    rotate : oneOf(float, string, oneOf(any, any), signal)
        The field or number to set the roration angle (in degrees).
    text : oneOf(string, oneOf(any, any), signal)
        The field containing the text to use for each word.
    spiral : oneOf(any, oneOf(any, any), signal)
        The type of spiral used for positioning words, either 'archimedean' or 'rectangular'.
    padding : oneOf(float, oneOf(any, any), signal)
        The padding around each word.
    output : mapping
        Rename the output data fields
    """
    _schema = {'$ref': '#/defs/wordcloudTransform'}
    _rootschema = Root._schema

    def __init__(self, type=Undefined, font=Undefined, fontScale=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined, output=Undefined, padding=Undefined, rotate=Undefined, size=Undefined, spiral=Undefined, text=Undefined, **kwds):
        super(wordcloudTransform, self).__init__(type=type, font=font, fontScale=fontScale, fontSize=fontSize, fontStyle=fontStyle, fontWeight=fontWeight, output=output, padding=padding, rotate=rotate, size=size, spiral=spiral, text=text, **kwds)
    


class transform(SchemaBase):
    """transform schema wrapper"""
    _schema = {'$ref': '#/defs/transform'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(transform, self).__init__(*args)
    


class scale(SchemaBase):
    """scale schema wrapper"""
    _schema = {'$ref': '#/defs/scale'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scale, self).__init__(*args, **kwds)
    


class operand(SchemaBase):
    """operand schema wrapper"""
    _schema = {'$ref': '#/refs/operand'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(operand, self).__init__(*args, **kwds)
    


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
    mult : float
        
    offset : float
        
    scale : scale
        
    """
    _schema = {'$ref': '#/refs/numberModifiers'}
    _rootschema = Root._schema

    def __init__(self, mult=Undefined, offset=Undefined, scale=Undefined, **kwds):
        super(numberModifiers, self).__init__(mult=mult, offset=offset, scale=scale, **kwds)
    


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
    


class colorValue(SchemaBase):
    """colorValue schema wrapper"""
    _schema = {'$ref': '#/refs/colorValue'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(colorValue, self).__init__(*args, **kwds)
    


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
    


class scopedScale(SchemaBase):
    """scopedScale schema wrapper"""
    _schema = {'$ref': '#/refs/scopedScale'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(scopedScale, self).__init__(*args, **kwds)
    


class data(SchemaBase):
    """data schema wrapper
    
    Attributes
    ----------
    data : oneOf(string, mapping)
        
    field : oneOf(string, list, mapping, list)
        
    sort : oneOf(boolean, mapping)
        
    """
    _schema = {'$ref': '#/refs/data'}
    _rootschema = Root._schema

    def __init__(self, data=Undefined, field=Undefined, sort=Undefined, **kwds):
        super(data, self).__init__(data=data, field=field, sort=sort, **kwds)
    

