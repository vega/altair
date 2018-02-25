# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# 2018-02-24 22:32

from . import core
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand, parse_shorthand_plus_data


class Row(core.PositionChannelDef):
    """Row schema wrapper
    
    Attributes
    ----------
    axis : Axis
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Row, self).__init__(field=field, aggregate=aggregate, axis=axis,
                                  bin=bin, scale=scale, sort=sort,
                                  timeUnit=timeUnit, title=title, type=type,
                                  value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Row, self).to_dict(validate=validate, ignore=ignore, context=context)


class Column(core.PositionChannelDef):
    """Column schema wrapper
    
    Attributes
    ----------
    axis : Axis
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Column, self).__init__(field=field, aggregate=aggregate, axis=axis,
                                     bin=bin, scale=scale, sort=sort,
                                     timeUnit=timeUnit, title=title, type=type,
                                     value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Column, self).to_dict(validate=validate, ignore=ignore, context=context)


class X(core.PositionChannelDef):
    """X schema wrapper
    
    Attributes
    ----------
    axis : Axis
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(X, self).__init__(field=field, aggregate=aggregate, axis=axis,
                                bin=bin, scale=scale, sort=sort, timeUnit=timeUnit,
                                title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X, self).to_dict(validate=validate, ignore=ignore, context=context)


class Y(core.PositionChannelDef):
    """Y schema wrapper
    
    Attributes
    ----------
    axis : Axis
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Y, self).__init__(field=field, aggregate=aggregate, axis=axis,
                                bin=bin, scale=scale, sort=sort, timeUnit=timeUnit,
                                title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y, self).to_dict(validate=validate, ignore=ignore, context=context)


class X2(core.FieldDef):
    """X2 schema wrapper
    
    Attributes
    ----------
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(X2, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                 timeUnit=timeUnit, title=title, type=type,
                                 value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X2, self).to_dict(validate=validate, ignore=ignore, context=context)


class Y2(core.FieldDef):
    """Y2 schema wrapper
    
    Attributes
    ----------
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(Y2, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                 timeUnit=timeUnit, title=title, type=type,
                                 value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y2, self).to_dict(validate=validate, ignore=ignore, context=context)


class Color(core.ChannelDefWithLegend):
    """Color schema wrapper
    
    Attributes
    ----------
    legend : Legend
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined, legend=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Color, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                    legend=legend, scale=scale, sort=sort,
                                    timeUnit=timeUnit, title=title, type=type,
                                    value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Color, self).to_dict(validate=validate, ignore=ignore, context=context)


class Opacity(core.ChannelDefWithLegend):
    """Opacity schema wrapper
    
    Attributes
    ----------
    legend : Legend
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined, legend=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Opacity, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                      legend=legend, scale=scale, sort=sort,
                                      timeUnit=timeUnit, title=title, type=type,
                                      value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Opacity, self).to_dict(validate=validate, ignore=ignore, context=context)


class Size(core.ChannelDefWithLegend):
    """Size schema wrapper
    
    Attributes
    ----------
    legend : Legend
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined, legend=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Size, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                   legend=legend, scale=scale, sort=sort,
                                   timeUnit=timeUnit, title=title, type=type,
                                   value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Size, self).to_dict(validate=validate, ignore=ignore, context=context)


class Shape(core.ChannelDefWithLegend):
    """Shape schema wrapper
    
    Attributes
    ----------
    legend : Legend
    scale : Scale
    sort : anyOf(SortOrder, SortField)
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined, legend=Undefined,
                 scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Shape, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                    legend=legend, scale=scale, sort=sort,
                                    timeUnit=timeUnit, title=title, type=type,
                                    value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Shape, self).to_dict(validate=validate, ignore=ignore, context=context)


class Detail(core.FieldDef):
    """Detail schema wrapper
    
    Attributes
    ----------
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(Detail, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                     timeUnit=timeUnit, title=title, type=type,
                                     value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Detail, self).to_dict(validate=validate, ignore=ignore, context=context)


class Text(core.FieldDef):
    """Text schema wrapper
    
    Attributes
    ----------
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(Text, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                   timeUnit=timeUnit, title=title, type=type,
                                   value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Text, self).to_dict(validate=validate, ignore=ignore, context=context)


class Label(core.FieldDef):
    """Label schema wrapper
    
    Attributes
    ----------
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(Label, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                    timeUnit=timeUnit, title=title, type=type,
                                    value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Label, self).to_dict(validate=validate, ignore=ignore, context=context)


class Path(core.OrderChannelDef):
    """Path schema wrapper
    
    Attributes
    ----------
    sort : SortOrder
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined, sort=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(Path, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                   sort=sort, timeUnit=timeUnit, title=title,
                                   type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Path, self).to_dict(validate=validate, ignore=ignore, context=context)


class Order(core.OrderChannelDef):
    """Order schema wrapper
    
    Attributes
    ----------
    sort : SortOrder
    field : string
        Name of the field from which to pull a data value.
    type : Type
        The encoded field's type of measurement. This can be either a full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an
        initial character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This
        property is case insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`,
        `hour`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for
        binning parameters.
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).
    title : string
        Title for axis or legend.
    """
    def __init__(self, field, aggregate=Undefined, bin=Undefined, sort=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined,
                 value=Undefined, **kwds):
        super(Order, self).__init__(field=field, aggregate=aggregate, bin=bin,
                                    sort=sort, timeUnit=timeUnit, title=title,
                                    type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Order, self).to_dict(validate=validate, ignore=ignore, context=context)
