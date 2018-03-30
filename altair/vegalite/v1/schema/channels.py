# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

import six
from . import core
import pandas as pd
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand


class Row(core.PositionChannelDef):
    """Row schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    axis : Axis
    
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Row, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                  field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                  type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Row, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Column(core.PositionChannelDef):
    """Column schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    axis : Axis
    
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Column, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                     field=field, scale=scale, sort=sort, timeUnit=timeUnit,
                                     title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Column, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class X(core.PositionChannelDef):
    """X schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    axis : Axis
    
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(X, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(X, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Y(core.PositionChannelDef):
    """Y schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    axis : Axis
    
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Y, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Y, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class X2(core.FieldDef):
    """X2 schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(X2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                 timeUnit=timeUnit, title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(X2, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Y2(core.FieldDef):
    """Y2 schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Y2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                 timeUnit=timeUnit, title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Y2, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Color(core.ChannelDefWithLegend):
    """Color schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    legend : Legend
    
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Color, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                    title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Color, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Opacity(core.ChannelDefWithLegend):
    """Opacity schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    legend : Legend
    
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Opacity, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                      legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                      title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Opacity, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Size(core.ChannelDefWithLegend):
    """Size schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    legend : Legend
    
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Size, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                   legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                   title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Size, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Shape(core.ChannelDefWithLegend):
    """Shape schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    legend : Legend
    
    scale : Scale
    
    sort : anyOf(SortOrder, SortField)
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Shape, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                    title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Shape, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Detail(core.FieldDef):
    """Detail schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Detail, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                     timeUnit=timeUnit, title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Detail, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Text(core.FieldDef):
    """Text schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Text, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                   timeUnit=timeUnit, title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Text, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Label(core.FieldDef):
    """Label schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Label, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    timeUnit=timeUnit, title=title, type=type, value=value, **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Label, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Path(core.OrderChannelDef):
    """Path schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    sort : SortOrder
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined,
                 **kwds):
        super(Path, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                   sort=sort, timeUnit=timeUnit, title=title, type=type, value=value,
                                   **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Path, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)


class Order(core.OrderChannelDef):
    """Order schema wrapper
    
    Mapping(required=[shorthand])
    
    Attributes
    ----------
    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : AggregateOp
        Aggregation function for the field  (e.g., `mean`, `sum`, `median`, `min`, `max`, 
        `count`).
    bin : anyOf(Bin, boolean)
        Flag for binning a `quantitative` field, or a bin property object  for binning 
        parameters.
    field : string
        Name of the field from which to pull a data value.
    sort : SortOrder
    
    timeUnit : TimeUnit
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`, `month`, `hour`).
    title : string
        Title for axis or legend.
    type : Type
        The encoded field's type of measurement. This can be either a full type  name 
        (`"quantitative"`, `"temporal"`, `"ordinal"`,  and `"nominal"`)  or an initial 
        character of the type name (`"Q"`, `"T"`, `"O"`, `"N"`).  This property is case 
        insensitive.
    value : anyOf(string, float, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined,
                 **kwds):
        super(Order, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    sort=sort, timeUnit=timeUnit, title=title, type=type, value=value,
                                    **kwds)

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{0} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {0}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(Order, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)
