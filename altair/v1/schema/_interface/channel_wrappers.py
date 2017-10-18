# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-157-g91fdb9b
# - date: 2017-10-17 17:01:04

import pandas as pd

from . import jstraitlets as jst
from . import schema
from ...traitlet_utils import parse_shorthand, infer_vegalite_type


class ChannelWithLegend(schema.ChannelDefWithLegend):
    """Wrapper for Vega-Lite ChannelDefWithLegend definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : AnyOf([boolean, Bin])
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    legend : Legend
        
    scale : Scale
        
    sort : AnyOf([SortField, string])
        
    timeUnit : string
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    title : string
        Title for axis or legend.
    type : string
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, field=jst.undefined, legend=jst.undefined, scale=jst.undefined, sort=jst.undefined, timeUnit=jst.undefined, title=jst.undefined, type=jst.undefined, value=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(ChannelWithLegend, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(ChannelWithLegend, self)._finalize(**kwargs)


class Field(schema.FieldDef):
    """Wrapper for Vega-Lite FieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : AnyOf([boolean, Bin])
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    timeUnit : string
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    title : string
        Title for axis or legend.
    type : string
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, field=jst.undefined, timeUnit=jst.undefined, title=jst.undefined, type=jst.undefined, value=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(Field, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(Field, self)._finalize(**kwargs)


class OrderChannel(schema.OrderChannelDef):
    """Wrapper for Vega-Lite OrderChannelDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : AnyOf([boolean, Bin])
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    sort : string
        
    timeUnit : string
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    title : string
        Title for axis or legend.
    type : string
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, field=jst.undefined, sort=jst.undefined, timeUnit=jst.undefined, title=jst.undefined, type=jst.undefined, value=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(OrderChannel, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(OrderChannel, self)._finalize(**kwargs)


class PositionChannel(schema.PositionChannelDef):
    """Wrapper for Vega-Lite PositionChannelDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    axis : AnyOf([boolean, Axis])
        
    bin : AnyOf([boolean, Bin])
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    field : string
        Name of the field from which to pull a data value.
    scale : Scale
        
    sort : AnyOf([SortField, string])
        
    timeUnit : string
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    title : string
        Title for axis or legend.
    type : string
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, axis=jst.undefined, bin=jst.undefined, field=jst.undefined, scale=jst.undefined, sort=jst.undefined, timeUnit=jst.undefined, title=jst.undefined, type=jst.undefined, value=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(PositionChannel, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(PositionChannel, self)._finalize(**kwargs)


