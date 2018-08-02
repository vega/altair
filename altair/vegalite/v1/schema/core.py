# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

from altair.utils.schemapi import SchemaBase, Undefined

import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, 'vega-lite-schema.json').decode('utf-8'))


class VegaLiteSchema(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return VegaLiteSchema.__subclasses__()


class Root(VegaLiteSchema):
    """Root schema wrapper

    anyOf(:class:`ExtendedUnitSpec`, :class:`FacetSpec`, :class:`LayerSpec`)
    """
    _schema = load_schema()
    _rootschema = _schema

    def __init__(self, *args, **kwds):
        super(Root, self).__init__(*args, **kwds)


class ExtendedUnitSpec(VegaLiteSchema):
    """ExtendedUnitSpec schema wrapper

    Mapping(required=[mark])
    Schema for a unit Vega-Lite specification, with the syntactic sugar extensions:


      ``row`` and ``column`` are included in the encoding.

      (Future) label, box plot

    Note: the spec could contain facet.

    Attributes
    ----------

    mark : :class:`Mark`
        The mark type.

        One of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,

        ``"area"``, ``"point"``, ``"rule"``, and ``"text"``.
    config : :class:`Config`
        Configuration object
    data : :class:`Data`
        An object describing the data source
    description : string
        An optional description of this mark for commenting purpose.

        This property has no effect on the output visualization.
    encoding : :class:`Encoding`
        A key-value mapping between encoding channels and definition of fields.
    height : float

    name : string
        Name of the visualization for later reference.
    transform : :class:`Transform`
        An object describing filter and new field calculation.
    width : float

    """
    _schema = {'$ref': '#/definitions/ExtendedUnitSpec'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, config=Undefined, data=Undefined, description=Undefined,
                 encoding=Undefined, height=Undefined, name=Undefined, transform=Undefined,
                 width=Undefined, **kwds):
        super(ExtendedUnitSpec, self).__init__(mark=mark, config=config, data=data,
                                               description=description, encoding=encoding,
                                               height=height, name=name, transform=transform,
                                               width=width, **kwds)


class Mark(VegaLiteSchema):
    """Mark schema wrapper

    enum('area', 'bar', 'line', 'point', 'text', 'tick', 'rule', 'circle', 'square', 'errorBar')
    """
    _schema = {'$ref': '#/definitions/Mark'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Mark, self).__init__(*args)


class Encoding(VegaLiteSchema):
    """Encoding schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : :class:`ChannelDefWithLegend`
        Color of the marks – either fill or stroke color based on mark type.

        (By default, fill color for ``area``, ``bar``, ``tick``, ``text``, ``circle``, and
        ``square`` /

        stroke color for ``line`` and ``point``.)
    column : :class:`PositionChannelDef`
        Horizontal facets for trellis plots.
    detail : anyOf(:class:`FieldDef`, List(:class:`FieldDef`))
        Additional levels of detail for grouping data in aggregate views and

        in line and area marks without mapping data to a specific visual channel.
    label : :class:`FieldDef`

    opacity : :class:`ChannelDefWithLegend`
        Opacity of the marks – either can be a value or in a range.
    order : anyOf(:class:`OrderChannelDef`, List(:class:`OrderChannelDef`))
        Layer order for non-stacked marks, or stack order for stacked marks.
    path : anyOf(:class:`OrderChannelDef`, List(:class:`OrderChannelDef`))
        Order of data points in line marks.
    row : :class:`PositionChannelDef`
        Vertical facets for trellis plots.
    shape : :class:`ChannelDefWithLegend`
        The symbol's shape (only for ``point`` marks). The supported values are

        ``"circle"`` (default), ``"square"``, ``"cross"``, ``"diamond"``, ``"triangle-up"``,

        or ``"triangle-down"``, or else a custom SVG path string.
    size : :class:`ChannelDefWithLegend`
        Size of the mark.


        * For ``point``, ``square`` and ``circle``

        – the symbol size, or pixel area of the mark.


        For ``bar`` and ``tick`` – the bar and tick's size.

        For ``text`` – the text's font size.

        Size is currently unsupported for ``line`` and ``area``.
    text : :class:`FieldDef`
        Text of the ``text`` mark.
    x : :class:`PositionChannelDef`
        X coordinates for ``point``, ``circle``, ``square``,

        ``line``, ``rule``, ``text``, and ``tick``

        (or to width and height for ``bar`` and ``area`` marks).
    x2 : :class:`FieldDef`
        X2 coordinates for ranged ``bar``, ``rule``, ``area``
    y : :class:`PositionChannelDef`
        Y coordinates for ``point``, ``circle``, ``square``,

        ``line``, ``rule``, ``text``, and ``tick``

        (or to width and height for ``bar`` and ``area`` marks).
    y2 : :class:`FieldDef`
        Y2 coordinates for ranged ``bar``, ``rule``, ``area``
    """
    _schema = {'$ref': '#/definitions/Encoding'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, column=Undefined, detail=Undefined, label=Undefined,
                 opacity=Undefined, order=Undefined, path=Undefined, row=Undefined, shape=Undefined,
                 size=Undefined, text=Undefined, x=Undefined, x2=Undefined, y=Undefined, y2=Undefined,
                 **kwds):
        super(Encoding, self).__init__(color=color, column=column, detail=detail, label=label,
                                       opacity=opacity, order=order, path=path, row=row, shape=shape,
                                       size=size, text=text, x=x, x2=x2, y=y, y2=y2, **kwds)


class PositionChannelDef(VegaLiteSchema):
    """PositionChannelDef schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    aggregate : :class:`AggregateOp`
        Aggregation function for the field

        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).
    axis : :class:`Axis`

    bin : anyOf(:class:`Bin`, boolean)
        Flag for binning a ``quantitative`` field, or a bin property object

        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    scale : :class:`Scale`

    sort : anyOf(:class:`SortOrder`, :class:`SortField`)

    timeUnit : :class:`TimeUnit`
        Time unit for a ``temporal`` field  (e.g., ``year``, ``yearmonth``, ``month``,
        ``hour`` ).
    title : string
        Title for axis or legend.
    type : :class:`Type`
        The encoded field's type of measurement. This can be either a full type

        name ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``,  and ``"nominal"`` )

        or an initial character of the type name ( ``"Q"``, ``"T"``, ``"O"``, ``"N"`` ).

        This property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/PositionChannelDef'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, axis=Undefined, bin=Undefined, field=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(PositionChannelDef, self).__init__(aggregate=aggregate, axis=axis, bin=bin, field=field,
                                                 scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                                 type=type, value=value, **kwds)


class Axis(VegaLiteSchema):
    """Axis schema wrapper

    anyOf(Mapping(required=[]), None)
    """
    _schema = {'$ref': '#/definitions/Axis'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Axis, self).__init__(*args, **kwds)


class AxisOrient(VegaLiteSchema):
    """AxisOrient schema wrapper

    enum('top', 'right', 'left', 'bottom')
    """
    _schema = {'$ref': '#/definitions/AxisOrient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AxisOrient, self).__init__(*args)


class DateTime(VegaLiteSchema):
    """DateTime schema wrapper

    Mapping(required=[])
    Object for defining datetime in Vega-Lite Filter.

    If both month and quarter are provided, month has higher precedence.

    ``day`` cannot be combined with other date.

    We accept string for month and day names.

    Attributes
    ----------

    date : float
        Integer value representing the date from 1-31.
    day : anyOf(string, float)
        Value representing the day of week.  This can be one of: (1) integer value -- ``1``
        represents Monday; (2) case-insensitive day name (e.g., ``"Monday"`` );  (3)
        case-insensitive, 3-character short day name (e.g., ``"Mon"`` ).   :raw-html:`<br/>`
        **Warning:** A DateTime definition object with ``day`` ** should not be combined
        with ``year``, ``quarter``, ``month``, or ``date``.
    hours : float
        Integer value representing the hour of day from 0-23.
    milliseconds : float
        Integer value representing millisecond segment of a time.
    minutes : float
        Integer value representing minute segment of a time from 0-59.
    month : anyOf(string, float)
        One of: (1) integer value representing the month from ``1`` - ``12``. ``1``
        represents January;  (2) case-insensitive month name (e.g., ``"January"`` );  (3)
        case-insensitive, 3-character short month name (e.g., ``"Jan"`` ).
    quarter : float
        Integer value representing the quarter of the year (from 1-4).
    seconds : float
        Integer value representing second segment of a time from 0-59.
    year : float
        Integer value representing the year.
    """
    _schema = {'$ref': '#/definitions/DateTime'}
    _rootschema = Root._schema

    def __init__(self, date=Undefined, day=Undefined, hours=Undefined, milliseconds=Undefined,
                 minutes=Undefined, month=Undefined, quarter=Undefined, seconds=Undefined,
                 year=Undefined, **kwds):
        super(DateTime, self).__init__(date=date, day=day, hours=hours, milliseconds=milliseconds,
                                       minutes=minutes, month=month, quarter=quarter, seconds=seconds,
                                       year=year, **kwds)


class Scale(VegaLiteSchema):
    """Scale schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bandSize : anyOf(:class:`BandSize`, float)

    clamp : boolean
        If true, values that exceed the data domain are clamped to either the minimum or
        maximum range value
    domain : anyOf(List(string), List(float), List(:class:`DateTime`))
        The domain of the scale, representing the set of data values. For quantitative data,
        this can take the form of a two-element array with minimum and maximum values. For
        ordinal/categorical data, this may be an array of valid input values.
    exponent : float
        Sets the exponent of the scale transformation. For pow scale types only, otherwise
        ignored.
    nice : anyOf(:class:`NiceTime`, boolean)
        If specified, modifies the scale domain to use a more human-friendly value range. If
        specified as a true boolean, modifies the scale domain to use a more human-friendly
        number range (e.g., 7 instead of 6.96). If specified as a string, modifies the scale
        domain to use a more human-friendly value range. For time and utc scale types only,
        the nice value should be a string indicating the desired time interval.
    padding : float
        Applies spacing among ordinal elements in the scale range. The actual effect depends
        on how the scale is configured. If the **points** parameter is ``true``, the padding
        value is interpreted as a multiple of the spacing between points. A reasonable value
        is 1.0, such that the first and last point will be offset from the minimum and
        maximum value by half the distance between points. Otherwise, padding is typically
        in the range [0, 1] and corresponds to the fraction of space in the range interval
        to allocate to padding. A value of 0.5 means that the range band width will be equal
        to the padding width. For more, see the `D3 ordinal scale documentation
        <https://github.com/mbostock/d3/wiki/Ordinal-Scales>`__.
    range : anyOf(List(string), List(float), string)
        The range of the scale, representing the set of visual values. For numeric values,
        the range can take the form of a two-element array with minimum and maximum values.
        For ordinal or quantized data, the range may by an array of desired output values,
        which are mapped to elements in the specified domain. For ordinal scales only, the
        range can be defined using a DataRef: the range values are then drawn dynamically
        from a backing data set.
    round : boolean
        If true, rounds numeric output values to integers. This can be helpful for snapping
        to the pixel grid.
    type : :class:`ScaleType`

    useRawDomain : boolean
        Uses the source data range as scale domain instead of aggregated data for aggregate
        axis.

        This property only works with aggregate functions that produce values within the raw
        data domain ( ``"mean"``, ``"average"``, ``"stdev"``, ``"stdevp"``, ``"median"``,
        ``"q1"``, ``"q3"``, ``"min"``, ``"max"`` ). For other aggregations that produce
        values outside of the raw data domain (e.g. ``"count"``, ``"sum"`` ), this property
        is ignored.
    zero : boolean
        If ``true``, ensures that a zero baseline value is included in the scale domain.

        Default value: ``true`` for ``x`` and ``y`` channel if the quantitative field is not
        binned

        and no custom ``domain`` is provided; ``false`` otherwise.
    """
    _schema = {'$ref': '#/definitions/Scale'}
    _rootschema = Root._schema

    def __init__(self, bandSize=Undefined, clamp=Undefined, domain=Undefined, exponent=Undefined,
                 nice=Undefined, padding=Undefined, range=Undefined, round=Undefined, type=Undefined,
                 useRawDomain=Undefined, zero=Undefined, **kwds):
        super(Scale, self).__init__(bandSize=bandSize, clamp=clamp, domain=domain, exponent=exponent,
                                    nice=nice, padding=padding, range=range, round=round, type=type,
                                    useRawDomain=useRawDomain, zero=zero, **kwds)


class ScaleType(VegaLiteSchema):
    """ScaleType schema wrapper

    enum('linear', 'log', 'pow', 'sqrt', 'quantile', 'quantize', 'ordinal', 'time', 'utc')
    """
    _schema = {'$ref': '#/definitions/ScaleType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(ScaleType, self).__init__(*args)


class BandSize(VegaLiteSchema):
    """BandSize schema wrapper

    enum('fit')
    """
    _schema = {'$ref': '#/definitions/BandSize'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(BandSize, self).__init__(*args)


class NiceTime(VegaLiteSchema):
    """NiceTime schema wrapper

    enum('second', 'minute', 'hour', 'day', 'week', 'month', 'year')
    """
    _schema = {'$ref': '#/definitions/NiceTime'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(NiceTime, self).__init__(*args)


class SortOrder(VegaLiteSchema):
    """SortOrder schema wrapper

    enum('ascending', 'descending', 'none')
    """
    _schema = {'$ref': '#/definitions/SortOrder'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(SortOrder, self).__init__(*args)


class SortField(VegaLiteSchema):
    """SortField schema wrapper

    Mapping(required=[field, op])

    Attributes
    ----------

    field : string
        The field name to aggregate over.
    op : :class:`AggregateOp`
        The sort aggregation operator
    order : :class:`SortOrder`

    """
    _schema = {'$ref': '#/definitions/SortField'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, op=Undefined, order=Undefined, **kwds):
        super(SortField, self).__init__(field=field, op=op, order=order, **kwds)


class AggregateOp(VegaLiteSchema):
    """AggregateOp schema wrapper

    enum('values', 'count', 'valid', 'missing', 'distinct', 'sum', 'mean', 'average',
    'variance', 'variancep', 'stdev', 'stdevp', 'median', 'q1', 'q3', 'modeskew', 'min', 'max',
    'argmin', 'argmax')
    """
    _schema = {'$ref': '#/definitions/AggregateOp'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AggregateOp, self).__init__(*args)


class Type(VegaLiteSchema):
    """Type schema wrapper

    enum('quantitative', 'ordinal', 'temporal', 'nominal')
    """
    _schema = {'$ref': '#/definitions/Type'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Type, self).__init__(*args)


class TimeUnit(VegaLiteSchema):
    """TimeUnit schema wrapper

    enum('year', 'month', 'day', 'date', 'hours', 'minutes', 'seconds', 'milliseconds',
    'yearmonth', 'yearmonthdate', 'yearmonthdatehours', 'yearmonthdatehoursminutes',
    'yearmonthdatehoursminutesseconds', 'monthdate', 'hoursminutes', 'hoursminutesseconds',
    'minutesseconds', 'secondsmilliseconds', 'quarter', 'yearquarter', 'quartermonth',
    'yearquartermonth')
    """
    _schema = {'$ref': '#/definitions/TimeUnit'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(TimeUnit, self).__init__(*args)


class Bin(VegaLiteSchema):
    """Bin schema wrapper

    Mapping(required=[])
    Binning properties or boolean flag for determining whether to bin data or not.

    Attributes
    ----------

    base : float
        The number base to use for automatic bin determination (default is base 10).
    div : List(float)
        Scale factors indicating allowable subdivisions. The default value is [5, 2], which
        indicates that for base 10 numbers (the default base), the method may consider
        dividing bin sizes by 5 and/or 2. For example, for an initial step size of 10, the
        method can check if bin sizes of 2 (= 10/5), 5 (= 10/2), or 1 (= 10/(5*2)) might
        also satisfy the given constraints.
    max : float
        The maximum bin value to consider. If unspecified, the maximum value of the
        specified field is used.
    maxbins : float
        Maximum number of bins.
    min : float
        The minimum bin value to consider. If unspecified, the minimum value of the
        specified field is used.
    minstep : float
        A minimum allowable step size (particularly useful for integer values).
    step : float
        An exact step size to use between bins. If provided, options such as maxbins will be
        ignored.
    steps : List(float)
        An array of allowable step sizes to choose from.
    """
    _schema = {'$ref': '#/definitions/Bin'}
    _rootschema = Root._schema

    def __init__(self, base=Undefined, div=Undefined, max=Undefined, maxbins=Undefined, min=Undefined,
                 minstep=Undefined, step=Undefined, steps=Undefined, **kwds):
        super(Bin, self).__init__(base=base, div=div, max=max, maxbins=maxbins, min=min,
                                  minstep=minstep, step=step, steps=steps, **kwds)


class FieldDef(VegaLiteSchema):
    """FieldDef schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    aggregate : :class:`AggregateOp`
        Aggregation function for the field

        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).
    bin : anyOf(:class:`Bin`, boolean)
        Flag for binning a ``quantitative`` field, or a bin property object

        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : :class:`TimeUnit`
        Time unit for a ``temporal`` field  (e.g., ``year``, ``yearmonth``, ``month``,
        ``hour`` ).
    title : string
        Title for axis or legend.
    type : :class:`Type`
        The encoded field's type of measurement. This can be either a full type

        name ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``,  and ``"nominal"`` )

        or an initial character of the type name ( ``"Q"``, ``"T"``, ``"O"``, ``"N"`` ).

        This property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/FieldDef'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, bin=Undefined, field=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(FieldDef, self).__init__(aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit,
                                       title=title, type=type, value=value, **kwds)


class ChannelDefWithLegend(VegaLiteSchema):
    """ChannelDefWithLegend schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    aggregate : :class:`AggregateOp`
        Aggregation function for the field

        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).
    bin : anyOf(:class:`Bin`, boolean)
        Flag for binning a ``quantitative`` field, or a bin property object

        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    legend : :class:`Legend`

    scale : :class:`Scale`

    sort : anyOf(:class:`SortOrder`, :class:`SortField`)

    timeUnit : :class:`TimeUnit`
        Time unit for a ``temporal`` field  (e.g., ``year``, ``yearmonth``, ``month``,
        ``hour`` ).
    title : string
        Title for axis or legend.
    type : :class:`Type`
        The encoded field's type of measurement. This can be either a full type

        name ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``,  and ``"nominal"`` )

        or an initial character of the type name ( ``"Q"``, ``"T"``, ``"O"``, ``"N"`` ).

        This property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/ChannelDefWithLegend'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, bin=Undefined, field=Undefined, legend=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(ChannelDefWithLegend, self).__init__(aggregate=aggregate, bin=bin, field=field,
                                                   legend=legend, scale=scale, sort=sort,
                                                   timeUnit=timeUnit, title=title, type=type,
                                                   value=value, **kwds)


class Legend(VegaLiteSchema):
    """Legend schema wrapper

    anyOf(Mapping(required=[]), None)
    """
    _schema = {'$ref': '#/definitions/Legend'}
    _rootschema = Root._schema

    def __init__(self, *args, **kwds):
        super(Legend, self).__init__(*args, **kwds)


class OrderChannelDef(VegaLiteSchema):
    """OrderChannelDef schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    aggregate : :class:`AggregateOp`
        Aggregation function for the field

        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).
    bin : anyOf(:class:`Bin`, boolean)
        Flag for binning a ``quantitative`` field, or a bin property object

        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    sort : :class:`SortOrder`

    timeUnit : :class:`TimeUnit`
        Time unit for a ``temporal`` field  (e.g., ``year``, ``yearmonth``, ``month``,
        ``hour`` ).
    title : string
        Title for axis or legend.
    type : :class:`Type`
        The encoded field's type of measurement. This can be either a full type

        name ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``,  and ``"nominal"`` )

        or an initial character of the type name ( ``"Q"``, ``"T"``, ``"O"``, ``"N"`` ).

        This property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _schema = {'$ref': '#/definitions/OrderChannelDef'}
    _rootschema = Root._schema

    def __init__(self, aggregate=Undefined, bin=Undefined, field=Undefined, sort=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(OrderChannelDef, self).__init__(aggregate=aggregate, bin=bin, field=field, sort=sort,
                                              timeUnit=timeUnit, title=title, type=type, value=value,
                                              **kwds)


class Data(VegaLiteSchema):
    """Data schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    format : :class:`DataFormat`
        An object that specifies the format for the data file or values.
    url : string
        A URL from which to load the data set. Use the format.type property

        to ensure the loaded data is correctly parsed.
    values : List(Mapping(required=[]))
        Pass array of objects instead of a url to a file.
    """
    _schema = {'$ref': '#/definitions/Data'}
    _rootschema = Root._schema

    def __init__(self, format=Undefined, url=Undefined, values=Undefined, **kwds):
        super(Data, self).__init__(format=format, url=url, values=values, **kwds)


class DataFormat(VegaLiteSchema):
    """DataFormat schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    feature : string
        The name of the TopoJSON object set to convert to a GeoJSON feature collection.

        For example, in a map of the world, there may be an object set named
        ``"countries"``.

        Using the feature property, we can extract this set and generate a GeoJSON feature
        object for each country.
    mesh : string
        The name of the TopoJSON object set to convert to a mesh.

        Similar to the ``feature`` option, ``mesh`` extracts a named TopoJSON object set.

        Unlike the ``feature`` option, the corresponding geo data is returned as a single,
        unified mesh instance, not as individual GeoJSON features.

        Extracting a mesh is useful for more efficiently drawing borders or other geographic
        elements that you do not need to associate with specific regions such as individual
        countries, states or counties.
    parse : Mapping(required=[])
        A collection of parsing instructions can be used to define the data types of
        string-valued attributes in the JSON file. Each instruction is a name-value pair,
        where the name is the name of the attribute, and the value is the desired data type
        (one of ``"number"``, ``"boolean"`` or ``"date"`` ). For example, ``"parse":
        {"modified_on":"date"}`` ensures that the ``modified_on`` value in each row of the
        input data is parsed as a Date value. (See Datalib's `dl.read.types method
        <https://github.com/vega/datalib/wiki/Import#dl_read_types>`__ for more
        information.)
    property : string
        JSON only) The JSON property containing the desired data.

        This parameter can be used when the loaded JSON file may have surrounding structure
        or meta-data.

        For example ``"property": "values.features"`` is equivalent to retrieving
        ``json.values.features``

        from the loaded JSON object.
    type : :class:`DataFormatType`
        Type of input data: ``"json"``, ``"csv"``, ``"tsv"``.

        The default format type is determined by the extension of the file url.

        If no extension is detected, ``"json"`` will be used by default.
    """
    _schema = {'$ref': '#/definitions/DataFormat'}
    _rootschema = Root._schema

    def __init__(self, feature=Undefined, mesh=Undefined, parse=Undefined, property=Undefined,
                 type=Undefined, **kwds):
        super(DataFormat, self).__init__(feature=feature, mesh=mesh, parse=parse, property=property,
                                         type=type, **kwds)


class DataFormatType(VegaLiteSchema):
    """DataFormatType schema wrapper

    enum('json', 'csv', 'tsv', 'topojson')
    """
    _schema = {'$ref': '#/definitions/DataFormatType'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(DataFormatType, self).__init__(*args)


class Transform(VegaLiteSchema):
    """Transform schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    calculate : List(:class:`Formula`)
        Calculate new field(s) using the provided expresssion(s). Calculation are applied
        before filter.
    filter : anyOf(:class:`EqualFilter`, :class:`RangeFilter`, :class:`OneOfFilter`,
    List(anyOf(:class:`EqualFilter`, :class:`RangeFilter`, :class:`OneOfFilter`, string)),
    string)
        A string containing the filter Vega expression. Use ``datum`` to refer to the
        current data object.
    filterInvalid : boolean
        Whether to filter invalid values ( ``null`` and ``NaN`` ) from the data. By default
        ( ``undefined`` ), only quantitative and temporal fields are filtered. If set to
        ``true``, all data items with null values are filtered. If ``false``, all data items
        are included.
    """
    _schema = {'$ref': '#/definitions/Transform'}
    _rootschema = Root._schema

    def __init__(self, calculate=Undefined, filter=Undefined, filterInvalid=Undefined, **kwds):
        super(Transform, self).__init__(calculate=calculate, filter=filter, filterInvalid=filterInvalid,
                                        **kwds)


class EqualFilter(VegaLiteSchema):
    """EqualFilter schema wrapper

    Mapping(required=[field, equal])

    Attributes
    ----------

    equal : anyOf(:class:`DateTime`, anyOf(string, float, boolean))
        Value that the field should be equal to.
    field : string
        Field to be filtered.
    timeUnit : :class:`TimeUnit`
        Time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/EqualFilter'}
    _rootschema = Root._schema

    def __init__(self, equal=Undefined, field=Undefined, timeUnit=Undefined, **kwds):
        super(EqualFilter, self).__init__(equal=equal, field=field, timeUnit=timeUnit, **kwds)


class RangeFilter(VegaLiteSchema):
    """RangeFilter schema wrapper

    Mapping(required=[field, range])

    Attributes
    ----------

    field : string
        Field to be filtered
    range : List(anyOf(:class:`DateTime`, float))
        Array of inclusive minimum and maximum values

        for a field value of a data item to be included in the filtered data.
    timeUnit : :class:`TimeUnit`
        time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/RangeFilter'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, range=Undefined, timeUnit=Undefined, **kwds):
        super(RangeFilter, self).__init__(field=field, range=range, timeUnit=timeUnit, **kwds)


class OneOfFilter(VegaLiteSchema):
    """OneOfFilter schema wrapper

    Mapping(required=[field, oneOf])

    Attributes
    ----------

    field : string
        Field to be filtered
    oneOf : List(anyOf(:class:`DateTime`, anyOf(string, float, boolean)))
        A set of values that the ``field`` 's value should be a member of,

        for a data item included in the filtered data.
    timeUnit : :class:`TimeUnit`
        time unit for the field to be filtered.
    """
    _schema = {'$ref': '#/definitions/OneOfFilter'}
    _rootschema = Root._schema

    def __init__(self, field=Undefined, oneOf=Undefined, timeUnit=Undefined, **kwds):
        super(OneOfFilter, self).__init__(field=field, oneOf=oneOf, timeUnit=timeUnit, **kwds)


class Formula(VegaLiteSchema):
    """Formula schema wrapper

    Mapping(required=[field, expr])
    Formula object for calculate.

    Attributes
    ----------

    expr : string
        A string containing an expression for the formula. Use the variable ``datum`` to to
        refer to the current data object.
    field : string
        The field in which to store the computed formula value.
    """
    _schema = {'$ref': '#/definitions/Formula'}
    _rootschema = Root._schema

    def __init__(self, expr=Undefined, field=Undefined, **kwds):
        super(Formula, self).__init__(expr=expr, field=field, **kwds)


class Config(VegaLiteSchema):
    """Config schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    axis : :class:`AxisConfig`
        Axis Config
    background : string
        CSS color property to use as background of visualization. Default is
        ``"transparent"``.
    cell : :class:`CellConfig`
        Cell Config
    countTitle : string
        Default axis and legend title for count fields.
    facet : :class:`FacetConfig`
        Facet Config
    legend : :class:`LegendConfig`
        Legend Config
    mark : :class:`MarkConfig`
        Mark Config
    numberFormat : string
        D3 Number format for axis labels and text tables. For example "s" for SI units.
    overlay : :class:`OverlayConfig`
        Mark Overlay Config
    scale : :class:`ScaleConfig`
        Scale Config
    timeFormat : string
        Default datetime format for axis and legend labels. The format can be set directly
        on each axis and legend.
    viewport : float
        The width and height of the on-screen viewport, in pixels. If necessary, clipping
        and scrolling will be applied.
    """
    _schema = {'$ref': '#/definitions/Config'}
    _rootschema = Root._schema

    def __init__(self, axis=Undefined, background=Undefined, cell=Undefined, countTitle=Undefined,
                 facet=Undefined, legend=Undefined, mark=Undefined, numberFormat=Undefined,
                 overlay=Undefined, scale=Undefined, timeFormat=Undefined, viewport=Undefined, **kwds):
        super(Config, self).__init__(axis=axis, background=background, cell=cell, countTitle=countTitle,
                                     facet=facet, legend=legend, mark=mark, numberFormat=numberFormat,
                                     overlay=overlay, scale=scale, timeFormat=timeFormat,
                                     viewport=viewport, **kwds)


class CellConfig(VegaLiteSchema):
    """CellConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    clip : boolean

    fill : string
        The fill color.
    fillOpacity : float
        The fill opacity (value between [0,1]).
    height : float

    stroke : string
        The stroke color.
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float
        The stroke opacity (value between [0,1]).
    strokeWidth : float
        The stroke width, in pixels.
    width : float

    """
    _schema = {'$ref': '#/definitions/CellConfig'}
    _rootschema = Root._schema

    def __init__(self, clip=Undefined, fill=Undefined, fillOpacity=Undefined, height=Undefined,
                 stroke=Undefined, strokeDash=Undefined, strokeDashOffset=Undefined,
                 strokeOpacity=Undefined, strokeWidth=Undefined, width=Undefined, **kwds):
        super(CellConfig, self).__init__(clip=clip, fill=fill, fillOpacity=fillOpacity, height=height,
                                         stroke=stroke, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, width=width, **kwds)


class MarkConfig(VegaLiteSchema):
    """MarkConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    align : :class:`HorizontalAlign`
        The horizontal alignment of the text. One of left, right, center.
    angle : float
        The rotation angle of the text, in degrees.
    applyColorToBackground : boolean
        Apply color field to background color instead of the text.
    barSize : float
        The size of the bars.  If unspecified, the default size is  ``bandSize-1``,

        which provides 1 pixel offset between bars.
    barThinSize : float
        The size of the bars on continuous scales.
    baseline : :class:`VerticalAlign`
        The vertical alignment of the text. One of top, middle, bottom.
    color : string
        Default color.
    dx : float
        The horizontal offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the angle property.
    dy : float
        The vertical offset, in pixels, between the text label and its anchor point. The
        offset is applied after rotation by the angle property.
    fill : string
        Default Fill Color.  This has higher precedence than config.color
    fillOpacity : float

    filled : boolean
        Whether the shape\'s color should be used as fill color instead of stroke color.

        This is only applicable for "bar", "point", and "area".

        All marks except "point" marks are filled by default.

        See Mark Documentation (http://vega.github.io/vega-lite/docs/marks.html)

        for usage example.
    font : string
        The typeface to set the text in (e.g., Helvetica Neue).
    fontSize : float
        The font size, in pixels.
    fontStyle : :class:`FontStyle`
        The font style (e.g., italic).
    fontWeight : :class:`FontWeight`
        The font weight (e.g., bold).
    format : string
        The formatting pattern for text value. If not defined, this will be determined
        automatically.
    interpolate : :class:`Interpolate`
        The line interpolation method to use. One of linear, step-before, step-after, basis,
        basis-open, cardinal, cardinal-open, monotone.
    lineSize : float
        Size of line mark.
    opacity : float

    orient : :class:`Orient`
        The orientation of a non-stacked bar, tick, area, and line charts.

        The value is either horizontal (default) or vertical.


        * For bar, rule and tick, this determines whether the size of the bar and tick

        should be applied to x or y dimension.


        For area, this property determines the orient property of the Vega output.

        For line, this property determines the sort order of the points in the line

        if ``config.sortLineBy`` is not specified.

        For stacked charts, this is always determined by the orientation of the stack;

        therefore explicitly specified value will be ignored.
    radius : float
        Polar coordinate radial offset, in pixels, of the text label from the origin
        determined by the x and y properties.
    ruleSize : float
        Size of rule mark.
    shape : anyOf(:class:`Shape`, string)
        The symbol shape to use. One of circle (default), square, cross, diamond,
        triangle-up, or triangle-down, or a custom SVG path.
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.
    size : float
        The pixel area each the point. For example: in the case of circles, the radius is
        determined in part by the square root of the size value.
    stacked : :class:`StackOffset`

    stroke : string
        Default Stroke Color.  This has higher precedence than config.color
    strokeDash : List(float)
        An array of alternating stroke, space lengths for creating dashed or dotted lines.
    strokeDashOffset : float
        The offset (in pixels) into which to begin drawing with the stroke dash array.
    strokeOpacity : float

    strokeWidth : float

    tension : float
        Depending on the interpolation type, sets the tension parameter.
    text : string
        Placeholder Text
    theta : float
        Polar coordinate angle, in radians, of the text label from the origin determined by
        the x and y properties. Values for theta follow the same convention of arc mark
        startAngle and endAngle properties: angles are measured in radians, with 0
        indicating "north".
    tickSize : float
        The width of the ticks.
    tickThickness : float
        Thickness of the tick mark.
    """
    _schema = {'$ref': '#/definitions/MarkConfig'}
    _rootschema = Root._schema

    def __init__(self, align=Undefined, angle=Undefined, applyColorToBackground=Undefined,
                 barSize=Undefined, barThinSize=Undefined, baseline=Undefined, color=Undefined,
                 dx=Undefined, dy=Undefined, fill=Undefined, fillOpacity=Undefined, filled=Undefined,
                 font=Undefined, fontSize=Undefined, fontStyle=Undefined, fontWeight=Undefined,
                 format=Undefined, interpolate=Undefined, lineSize=Undefined, opacity=Undefined,
                 orient=Undefined, radius=Undefined, ruleSize=Undefined, shape=Undefined,
                 shortTimeLabels=Undefined, size=Undefined, stacked=Undefined, stroke=Undefined,
                 strokeDash=Undefined, strokeDashOffset=Undefined, strokeOpacity=Undefined,
                 strokeWidth=Undefined, tension=Undefined, text=Undefined, theta=Undefined,
                 tickSize=Undefined, tickThickness=Undefined, **kwds):
        super(MarkConfig, self).__init__(align=align, angle=angle,
                                         applyColorToBackground=applyColorToBackground, barSize=barSize,
                                         barThinSize=barThinSize, baseline=baseline, color=color, dx=dx,
                                         dy=dy, fill=fill, fillOpacity=fillOpacity, filled=filled,
                                         font=font, fontSize=fontSize, fontStyle=fontStyle,
                                         fontWeight=fontWeight, format=format, interpolate=interpolate,
                                         lineSize=lineSize, opacity=opacity, orient=orient,
                                         radius=radius, ruleSize=ruleSize, shape=shape,
                                         shortTimeLabels=shortTimeLabels, size=size, stacked=stacked,
                                         stroke=stroke, strokeDash=strokeDash,
                                         strokeDashOffset=strokeDashOffset, strokeOpacity=strokeOpacity,
                                         strokeWidth=strokeWidth, tension=tension, text=text,
                                         theta=theta, tickSize=tickSize, tickThickness=tickThickness,
                                         **kwds)


class StackOffset(VegaLiteSchema):
    """StackOffset schema wrapper

    enum('zero', 'center', 'normalize', 'none')
    """
    _schema = {'$ref': '#/definitions/StackOffset'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(StackOffset, self).__init__(*args)


class Orient(VegaLiteSchema):
    """Orient schema wrapper

    enum('horizontal', 'vertical')
    """
    _schema = {'$ref': '#/definitions/Orient'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Orient, self).__init__(*args)


class Interpolate(VegaLiteSchema):
    """Interpolate schema wrapper

    enum('linear', 'linear-closed', 'step', 'step-before', 'step-after', 'basis', 'basis-open',
    'basis-closed', 'cardinal', 'cardinal-open', 'cardinal-closed', 'bundle', 'monotone')
    """
    _schema = {'$ref': '#/definitions/Interpolate'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Interpolate, self).__init__(*args)


class Shape(VegaLiteSchema):
    """Shape schema wrapper

    enum('circle', 'square', 'cross', 'diamond', 'triangle-up', 'triangle-down')
    """
    _schema = {'$ref': '#/definitions/Shape'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(Shape, self).__init__(*args)


class HorizontalAlign(VegaLiteSchema):
    """HorizontalAlign schema wrapper

    enum('left', 'right', 'center')
    """
    _schema = {'$ref': '#/definitions/HorizontalAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(HorizontalAlign, self).__init__(*args)


class VerticalAlign(VegaLiteSchema):
    """VerticalAlign schema wrapper

    enum('top', 'middle', 'bottom')
    """
    _schema = {'$ref': '#/definitions/VerticalAlign'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(VerticalAlign, self).__init__(*args)


class FontStyle(VegaLiteSchema):
    """FontStyle schema wrapper

    enum('normal', 'italic')
    """
    _schema = {'$ref': '#/definitions/FontStyle'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontStyle, self).__init__(*args)


class FontWeight(VegaLiteSchema):
    """FontWeight schema wrapper

    enum('normal', 'bold')
    """
    _schema = {'$ref': '#/definitions/FontWeight'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(FontWeight, self).__init__(*args)


class OverlayConfig(VegaLiteSchema):
    """OverlayConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    area : :class:`AreaOverlay`
        Type of overlay for area mark (line or linepoint)
    line : boolean
        Whether to overlay line with point.
    lineStyle : :class:`MarkConfig`
        Default style for the overlayed point.
    pointStyle : :class:`MarkConfig`
        Default style for the overlayed point.
    """
    _schema = {'$ref': '#/definitions/OverlayConfig'}
    _rootschema = Root._schema

    def __init__(self, area=Undefined, line=Undefined, lineStyle=Undefined, pointStyle=Undefined, **kwds):
        super(OverlayConfig, self).__init__(area=area, line=line, lineStyle=lineStyle,
                                            pointStyle=pointStyle, **kwds)


class AreaOverlay(VegaLiteSchema):
    """AreaOverlay schema wrapper

    enum('line', 'linepoint', 'none')
    """
    _schema = {'$ref': '#/definitions/AreaOverlay'}
    _rootschema = Root._schema

    def __init__(self, *args):
        super(AreaOverlay, self).__init__(*args)


class ScaleConfig(VegaLiteSchema):
    """ScaleConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    bandSize : anyOf(:class:`BandSize`, float)
        Default band size for (1) ``y`` ordinal scale,

        and (2) ``x`` ordinal scale when the mark is not ``text``.
    barSizeRange : List(float)
        Default range for bar size scale
    fontSizeRange : List(float)
        Default range for font size scale
    nominalColorRange : anyOf(List(string), string)
        Default range for nominal color scale
    opacity : List(float)
        Default range for opacity.
    padding : float
        Default padding for ``x`` and ``y`` ordinal scales.
    pointSizeRange : List(float)
        Default range for bar size scale
    round : boolean
        If true, rounds numeric output values to integers.

        This can be helpful for snapping to the pixel grid.

        (Only available for ``x``, ``y``, ``size``, ``row``, and ``column`` scales.)
    ruleSizeRange : List(float)
        Default range for rule stroke widths
    sequentialColorRange : anyOf(List(string), string)
        Default range for ordinal / continuous color scale
    shapeRange : anyOf(List(string), string)
        Default range for shape
    textBandWidth : float
        Default band width for ``x`` ordinal scale when is mark is ``text``.
    tickSizeRange : List(float)
        Default range for tick spans
    useRawDomain : boolean
        Uses the source data range as scale domain instead of aggregated data for aggregate
        axis.

        This property only works with aggregate functions that produce values within the raw
        data domain ( ``"mean"``, ``"average"``, ``"stdev"``, ``"stdevp"``, ``"median"``,
        ``"q1"``, ``"q3"``, ``"min"``, ``"max"`` ). For other aggregations that produce
        values outside of the raw data domain (e.g. ``"count"``, ``"sum"`` ), this property
        is ignored.
    """
    _schema = {'$ref': '#/definitions/ScaleConfig'}
    _rootschema = Root._schema

    def __init__(self, bandSize=Undefined, barSizeRange=Undefined, fontSizeRange=Undefined,
                 nominalColorRange=Undefined, opacity=Undefined, padding=Undefined,
                 pointSizeRange=Undefined, round=Undefined, ruleSizeRange=Undefined,
                 sequentialColorRange=Undefined, shapeRange=Undefined, textBandWidth=Undefined,
                 tickSizeRange=Undefined, useRawDomain=Undefined, **kwds):
        super(ScaleConfig, self).__init__(bandSize=bandSize, barSizeRange=barSizeRange,
                                          fontSizeRange=fontSizeRange,
                                          nominalColorRange=nominalColorRange, opacity=opacity,
                                          padding=padding, pointSizeRange=pointSizeRange, round=round,
                                          ruleSizeRange=ruleSizeRange,
                                          sequentialColorRange=sequentialColorRange,
                                          shapeRange=shapeRange, textBandWidth=textBandWidth,
                                          tickSizeRange=tickSizeRange, useRawDomain=useRawDomain, **kwds)


class AxisConfig(VegaLiteSchema):
    """AxisConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    axisColor : string
        Color of axis line.
    axisWidth : float
        Width of the axis line
    characterWidth : float
        Character width for automatically determining title max length.
    grid : boolean
        A flag indicate if gridlines should be created in addition to ticks. If ``grid`` is
        unspecified, the default value is ``true`` for ROW and COL. For X and Y, the default
        value is ``true`` for quantitative and time fields and ``false`` otherwise.
    gridColor : string
        Color of gridlines.
    gridDash : List(float)
        The offset (in pixels) into which to begin drawing with the grid dash array.
    gridOpacity : float
        The stroke opacity of grid (value between [0,1])
    gridWidth : float
        The grid width, in pixels.
    labelAlign : string
        Text alignment for the Label.
    labelAngle : float
        The rotation angle of the axis labels.
    labelBaseline : string
        Text baseline for the label.
    labelMaxLength : float
        Truncate labels that are too long.
    labels : boolean
        Enable or disable labels.
    layer : string
        A string indicating if the axis (and any gridlines) should be placed above or below
        the data marks.
    offset : float
        The offset, in pixels, by which to displace the axis from the edge of the enclosing
        group or data rectangle.
    properties : Mapping(required=[])
        Optional mark property definitions for custom axis styling.
    shortTimeLabels : boolean
        Whether month and day names should be abbreviated.
    subdivide : float
        If provided, sets the number of minor ticks between major ticks (the value 9 results
        in decimal subdivision). Only applicable for axes visualizing quantitative scales.
    tickColor : string
        The color of the axis's tick.
    tickLabelColor : string
        The color of the tick label, can be in hex color code or regular color name.
    tickLabelFont : string
        The font of the tick label.
    tickLabelFontSize : float
        The font size of label, in pixels.
    tickPadding : float
        The padding, in pixels, between ticks and text labels.
    tickSize : float
        The size, in pixels, of major, minor and end ticks.
    tickSizeEnd : float
        The size, in pixels, of end ticks.
    tickSizeMajor : float
        The size, in pixels, of major ticks.
    tickSizeMinor : float
        The size, in pixels, of minor ticks.
    tickWidth : float
        The width, in pixels, of ticks.
    ticks : float
        A desired number of ticks, for axes visualizing quantitative scales. The resulting
        number may be different so that values are "nice" (multiples of 2, 5, 10) and lie
        within the underlying scale's range.
    titleColor : string
        Color of the title, can be in hex color code or regular color name.
    titleFont : string
        Font of the title.
    titleFontSize : float
        Size of the title.
    titleFontWeight : string
        Weight of the title.
    titleMaxLength : float
        Max length for axis title if the title is automatically generated from the field's
        description. By default, this is automatically based on cell size and characterWidth
        property.
    titleOffset : float
        A title offset value for the axis.
    """
    _schema = {'$ref': '#/definitions/AxisConfig'}
    _rootschema = Root._schema

    def __init__(self, axisColor=Undefined, axisWidth=Undefined, characterWidth=Undefined,
                 grid=Undefined, gridColor=Undefined, gridDash=Undefined, gridOpacity=Undefined,
                 gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined,
                 labelBaseline=Undefined, labelMaxLength=Undefined, labels=Undefined, layer=Undefined,
                 offset=Undefined, properties=Undefined, shortTimeLabels=Undefined, subdivide=Undefined,
                 tickColor=Undefined, tickLabelColor=Undefined, tickLabelFont=Undefined,
                 tickLabelFontSize=Undefined, tickPadding=Undefined, tickSize=Undefined,
                 tickSizeEnd=Undefined, tickSizeMajor=Undefined, tickSizeMinor=Undefined,
                 tickWidth=Undefined, ticks=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontWeight=Undefined, titleMaxLength=Undefined,
                 titleOffset=Undefined, **kwds):
        super(AxisConfig, self).__init__(axisColor=axisColor, axisWidth=axisWidth,
                                         characterWidth=characterWidth, grid=grid, gridColor=gridColor,
                                         gridDash=gridDash, gridOpacity=gridOpacity,
                                         gridWidth=gridWidth, labelAlign=labelAlign,
                                         labelAngle=labelAngle, labelBaseline=labelBaseline,
                                         labelMaxLength=labelMaxLength, labels=labels, layer=layer,
                                         offset=offset, properties=properties,
                                         shortTimeLabels=shortTimeLabels, subdivide=subdivide,
                                         tickColor=tickColor, tickLabelColor=tickLabelColor,
                                         tickLabelFont=tickLabelFont,
                                         tickLabelFontSize=tickLabelFontSize, tickPadding=tickPadding,
                                         tickSize=tickSize, tickSizeEnd=tickSizeEnd,
                                         tickSizeMajor=tickSizeMajor, tickSizeMinor=tickSizeMinor,
                                         tickWidth=tickWidth, ticks=ticks, titleColor=titleColor,
                                         titleFont=titleFont, titleFontSize=titleFontSize,
                                         titleFontWeight=titleFontWeight, titleMaxLength=titleMaxLength,
                                         titleOffset=titleOffset, **kwds)


class LegendConfig(VegaLiteSchema):
    """LegendConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    gradientHeight : float
        The height of the gradient, in pixels.
    gradientStrokeColor : string
        The color of the gradient stroke, can be in hex color code or regular color name.
    gradientStrokeWidth : float
        The width of the gradient stroke, in pixels.
    gradientWidth : float
        The width of the gradient, in pixels.
    labelAlign : string
        The alignment of the legend label, can be left, middle or right.
    labelBaseline : string
        The position of the baseline of legend label, can be top, middle or bottom.
    labelColor : string
        The color of the legend label, can be in hex color code or regular color name.
    labelFont : string
        The font of the legend label.
    labelFontSize : float
        The font size of legend label.
    labelOffset : float
        The offset of the legend label.
    margin : float
        The margin around the legend, in pixels
    offset : float
        The offset, in pixels, by which to displace the legend from the edge of the
        enclosing group or data rectangle.
    orient : string
        The orientation of the legend. One of "left" or "right". This determines how the
        legend is positioned within the scene. The default is "right".
    padding : float
        The padding, in pixels, between the legend and axis.
    properties : Mapping(required=[])
        Optional mark property definitions for custom legend styling.
    shortTimeLabels : boolean
        Whether month names and weekday names should be abbreviated.
    symbolColor : string
        The color of the legend symbol,
    symbolShape : string
        The shape of the legend symbol, can be the 'circle', 'square', 'cross', 'diamond',

        'triangle-up', 'triangle-down', or else a custom SVG path string.
    symbolSize : float
        The size of the legend symbol, in pixels.
    symbolStrokeWidth : float
        The width of the symbol's stroke.
    titleColor : string
        Optional mark property definitions for custom legend styling.

        The color of the legend title, can be in hex color code or regular color name.
    titleFont : string
        The font of the legend title.
    titleFontSize : float
        The font size of the legend title.
    titleFontWeight : string
        The font weight of the legend title.
    """
    _schema = {'$ref': '#/definitions/LegendConfig'}
    _rootschema = Root._schema

    def __init__(self, gradientHeight=Undefined, gradientStrokeColor=Undefined,
                 gradientStrokeWidth=Undefined, gradientWidth=Undefined, labelAlign=Undefined,
                 labelBaseline=Undefined, labelColor=Undefined, labelFont=Undefined,
                 labelFontSize=Undefined, labelOffset=Undefined, margin=Undefined, offset=Undefined,
                 orient=Undefined, padding=Undefined, properties=Undefined, shortTimeLabels=Undefined,
                 symbolColor=Undefined, symbolShape=Undefined, symbolSize=Undefined,
                 symbolStrokeWidth=Undefined, titleColor=Undefined, titleFont=Undefined,
                 titleFontSize=Undefined, titleFontWeight=Undefined, **kwds):
        super(LegendConfig, self).__init__(gradientHeight=gradientHeight,
                                           gradientStrokeColor=gradientStrokeColor,
                                           gradientStrokeWidth=gradientStrokeWidth,
                                           gradientWidth=gradientWidth, labelAlign=labelAlign,
                                           labelBaseline=labelBaseline, labelColor=labelColor,
                                           labelFont=labelFont, labelFontSize=labelFontSize,
                                           labelOffset=labelOffset, margin=margin, offset=offset,
                                           orient=orient, padding=padding, properties=properties,
                                           shortTimeLabels=shortTimeLabels, symbolColor=symbolColor,
                                           symbolShape=symbolShape, symbolSize=symbolSize,
                                           symbolStrokeWidth=symbolStrokeWidth, titleColor=titleColor,
                                           titleFont=titleFont, titleFontSize=titleFontSize,
                                           titleFontWeight=titleFontWeight, **kwds)


class FacetConfig(VegaLiteSchema):
    """FacetConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    axis : :class:`AxisConfig`
        Facet Axis Config
    cell : :class:`CellConfig`
        Facet Cell Config
    grid : :class:`FacetGridConfig`
        Facet Grid Config
    scale : :class:`FacetScaleConfig`
        Facet Scale Config
    """
    _schema = {'$ref': '#/definitions/FacetConfig'}
    _rootschema = Root._schema

    def __init__(self, axis=Undefined, cell=Undefined, grid=Undefined, scale=Undefined, **kwds):
        super(FacetConfig, self).__init__(axis=axis, cell=cell, grid=grid, scale=scale, **kwds)


class FacetScaleConfig(VegaLiteSchema):
    """FacetScaleConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    padding : float

    round : boolean

    """
    _schema = {'$ref': '#/definitions/FacetScaleConfig'}
    _rootschema = Root._schema

    def __init__(self, padding=Undefined, round=Undefined, **kwds):
        super(FacetScaleConfig, self).__init__(padding=padding, round=round, **kwds)


class FacetGridConfig(VegaLiteSchema):
    """FacetGridConfig schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : string

    offset : float

    opacity : float

    """
    _schema = {'$ref': '#/definitions/FacetGridConfig'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, offset=Undefined, opacity=Undefined, **kwds):
        super(FacetGridConfig, self).__init__(color=color, offset=offset, opacity=opacity, **kwds)


class FacetSpec(VegaLiteSchema):
    """FacetSpec schema wrapper

    Mapping(required=[facet, spec])

    Attributes
    ----------

    facet : :class:`Facet`

    spec : anyOf(:class:`UnitSpec`, :class:`LayerSpec`)

    config : :class:`Config`
        Configuration object
    data : :class:`Data`
        An object describing the data source
    description : string
        An optional description of this mark for commenting purpose.

        This property has no effect on the output visualization.
    name : string
        Name of the visualization for later reference.
    transform : :class:`Transform`
        An object describing filter and new field calculation.
    """
    _schema = {'$ref': '#/definitions/FacetSpec'}
    _rootschema = Root._schema

    def __init__(self, facet=Undefined, spec=Undefined, config=Undefined, data=Undefined,
                 description=Undefined, name=Undefined, transform=Undefined, **kwds):
        super(FacetSpec, self).__init__(facet=facet, spec=spec, config=config, data=data,
                                        description=description, name=name, transform=transform, **kwds)


class Facet(VegaLiteSchema):
    """Facet schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    column : :class:`PositionChannelDef`

    row : :class:`PositionChannelDef`

    """
    _schema = {'$ref': '#/definitions/Facet'}
    _rootschema = Root._schema

    def __init__(self, column=Undefined, row=Undefined, **kwds):
        super(Facet, self).__init__(column=column, row=row, **kwds)


class UnitSpec(VegaLiteSchema):
    """UnitSpec schema wrapper

    Mapping(required=[mark])

    Attributes
    ----------

    mark : :class:`Mark`
        The mark type.

        One of ``"bar"``, ``"circle"``, ``"square"``, ``"tick"``, ``"line"``,

        ``"area"``, ``"point"``, ``"rule"``, and ``"text"``.
    config : :class:`Config`
        Configuration object
    data : :class:`Data`
        An object describing the data source
    description : string
        An optional description of this mark for commenting purpose.

        This property has no effect on the output visualization.
    encoding : :class:`UnitEncoding`
        A key-value mapping between encoding channels and definition of fields.
    height : float

    name : string
        Name of the visualization for later reference.
    transform : :class:`Transform`
        An object describing filter and new field calculation.
    width : float

    """
    _schema = {'$ref': '#/definitions/UnitSpec'}
    _rootschema = Root._schema

    def __init__(self, mark=Undefined, config=Undefined, data=Undefined, description=Undefined,
                 encoding=Undefined, height=Undefined, name=Undefined, transform=Undefined,
                 width=Undefined, **kwds):
        super(UnitSpec, self).__init__(mark=mark, config=config, data=data, description=description,
                                       encoding=encoding, height=height, name=name, transform=transform,
                                       width=width, **kwds)


class UnitEncoding(VegaLiteSchema):
    """UnitEncoding schema wrapper

    Mapping(required=[])

    Attributes
    ----------

    color : :class:`ChannelDefWithLegend`
        Color of the marks – either fill or stroke color based on mark type.

        (By default, fill color for ``area``, ``bar``, ``tick``, ``text``, ``circle``, and
        ``square`` /

        stroke color for ``line`` and ``point``.)
    detail : anyOf(:class:`FieldDef`, List(:class:`FieldDef`))
        Additional levels of detail for grouping data in aggregate views and

        in line and area marks without mapping data to a specific visual channel.
    label : :class:`FieldDef`

    opacity : :class:`ChannelDefWithLegend`
        Opacity of the marks – either can be a value or in a range.
    order : anyOf(:class:`OrderChannelDef`, List(:class:`OrderChannelDef`))
        Layer order for non-stacked marks, or stack order for stacked marks.
    path : anyOf(:class:`OrderChannelDef`, List(:class:`OrderChannelDef`))
        Order of data points in line marks.
    shape : :class:`ChannelDefWithLegend`
        The symbol's shape (only for ``point`` marks). The supported values are

        ``"circle"`` (default), ``"square"``, ``"cross"``, ``"diamond"``, ``"triangle-up"``,

        or ``"triangle-down"``, or else a custom SVG path string.
    size : :class:`ChannelDefWithLegend`
        Size of the mark.


        * For ``point``, ``square`` and ``circle``

        – the symbol size, or pixel area of the mark.


        For ``bar`` and ``tick`` – the bar and tick's size.

        For ``text`` – the text's font size.

        Size is currently unsupported for ``line`` and ``area``.
    text : :class:`FieldDef`
        Text of the ``text`` mark.
    x : :class:`PositionChannelDef`
        X coordinates for ``point``, ``circle``, ``square``,

        ``line``, ``rule``, ``text``, and ``tick``

        (or to width and height for ``bar`` and ``area`` marks).
    x2 : :class:`FieldDef`
        X2 coordinates for ranged ``bar``, ``rule``, ``area``
    y : :class:`PositionChannelDef`
        Y coordinates for ``point``, ``circle``, ``square``,

        ``line``, ``rule``, ``text``, and ``tick``

        (or to width and height for ``bar`` and ``area`` marks).
    y2 : :class:`FieldDef`
        Y2 coordinates for ranged ``bar``, ``rule``, ``area``
    """
    _schema = {'$ref': '#/definitions/UnitEncoding'}
    _rootschema = Root._schema

    def __init__(self, color=Undefined, detail=Undefined, label=Undefined, opacity=Undefined,
                 order=Undefined, path=Undefined, shape=Undefined, size=Undefined, text=Undefined,
                 x=Undefined, x2=Undefined, y=Undefined, y2=Undefined, **kwds):
        super(UnitEncoding, self).__init__(color=color, detail=detail, label=label, opacity=opacity,
                                           order=order, path=path, shape=shape, size=size, text=text,
                                           x=x, x2=x2, y=y, y2=y2, **kwds)


class LayerSpec(VegaLiteSchema):
    """LayerSpec schema wrapper

    Mapping(required=[layers])

    Attributes
    ----------

    layers : List(:class:`UnitSpec`)
        Unit specs that will be layered.
    config : :class:`Config`
        Configuration object
    data : :class:`Data`
        An object describing the data source
    description : string
        An optional description of this mark for commenting purpose.

        This property has no effect on the output visualization.
    height : float

    name : string
        Name of the visualization for later reference.
    transform : :class:`Transform`
        An object describing filter and new field calculation.
    width : float

    """
    _schema = {'$ref': '#/definitions/LayerSpec'}
    _rootschema = Root._schema

    def __init__(self, layers=Undefined, config=Undefined, data=Undefined, description=Undefined,
                 height=Undefined, name=Undefined, transform=Undefined, width=Undefined, **kwds):
        super(LayerSpec, self).__init__(layers=layers, config=config, data=data,
                                        description=description, height=height, name=name,
                                        transform=transform, width=width, **kwds)

