# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

import six
from . import core
import pandas as pd
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand


class FieldChannelMixin(object):
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        if self.shorthand is Undefined:
            kwds = {}
        elif isinstance(self.shorthand, (tuple, list)):
            # If given a list of shorthands, then transform it to a list of classes
            kwds = self._kwds.copy()
            kwds.pop('shorthand')
            return [self.__class__(shorthand, **kwds).to_dict()
                    for shorthand in self.shorthand]
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{} encoding field is specified without a type; "
                                     "the type cannot be automatically inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {'field': self.shorthand}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined})
        return super(FieldChannelMixin, self).to_dict(
            validate=validate,
            ignore=ignore,
            context=context
        )


class ValueChannelMixin(object):
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        condition = getattr(self, 'condition', Undefined)
        copy = self  # don't copy unless we need to
        if condition is not Undefined:
            if isinstance(condition, core.SchemaBase):
                pass
            elif 'field' in condition and 'type' not in condition:
                kwds = parse_shorthand(condition['field'], context.get('data', None))
                copy = self.copy()
                copy.condition.update(kwds)
        return super(ValueChannelMixin, copy).to_dict(validate=validate,
                                                      ignore=ignore,
                                                      context=context)


class Row(FieldChannelMixin, core.PositionChannelDef):
    """Row schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Row, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                  field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                  type=type, value=value, **kwds)


class Column(FieldChannelMixin, core.PositionChannelDef):
    """Column schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Column, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                     field=field, scale=scale, sort=sort, timeUnit=timeUnit,
                                     title=title, type=type, value=value, **kwds)


class X(FieldChannelMixin, core.PositionChannelDef):
    """X schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(X, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                type=type, value=value, **kwds)


class Y(FieldChannelMixin, core.PositionChannelDef):
    """Y schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Y, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title,
                                type=type, value=value, **kwds)


class X2(FieldChannelMixin, core.FieldDef):
    """X2 schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(X2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                 timeUnit=timeUnit, title=title, type=type, value=value, **kwds)


class Y2(FieldChannelMixin, core.FieldDef):
    """Y2 schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Y2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                 timeUnit=timeUnit, title=title, type=type, value=value, **kwds)


class Color(FieldChannelMixin, core.ChannelDefWithLegend):
    """Color schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Color, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                    title=title, type=type, value=value, **kwds)


class Opacity(FieldChannelMixin, core.ChannelDefWithLegend):
    """Opacity schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Opacity, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                      legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                      title=title, type=type, value=value, **kwds)


class Size(FieldChannelMixin, core.ChannelDefWithLegend):
    """Size schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Size, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                   legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                   title=title, type=type, value=value, **kwds)


class Shape(FieldChannelMixin, core.ChannelDefWithLegend):
    """Shape schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, value=Undefined, **kwds):
        super(Shape, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    legend=legend, scale=scale, sort=sort, timeUnit=timeUnit,
                                    title=title, type=type, value=value, **kwds)


class Detail(FieldChannelMixin, core.FieldDef):
    """Detail schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Detail, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                     timeUnit=timeUnit, title=title, type=type, value=value, **kwds)


class Text(FieldChannelMixin, core.FieldDef):
    """Text schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Text, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                   timeUnit=timeUnit, title=title, type=type, value=value, **kwds)


class Label(FieldChannelMixin, core.FieldDef):
    """Label schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined, **kwds):
        super(Label, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    timeUnit=timeUnit, title=title, type=type, value=value, **kwds)


class Path(FieldChannelMixin, core.OrderChannelDef):
    """Path schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined,
                 **kwds):
        super(Path, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                   sort=sort, timeUnit=timeUnit, title=title, type=type, value=value,
                                   **kwds)


class Order(FieldChannelMixin, core.OrderChannelDef):
    """Order schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
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
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, value=Undefined,
                 **kwds):
        super(Order, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    sort=sort, timeUnit=timeUnit, title=title, type=type, value=value,
                                    **kwds)
