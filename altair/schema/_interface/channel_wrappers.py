# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-68-g3ada237
# - date: 2017-07-19 11:12:59

import pandas as pd

from . import jstraitlets as jst
from . import schema
from ...utils import parse_shorthand, infer_vegalite_type


class ChannelWithLegend(schema.ChannelDefWithLegend):
    """Wrapper for Vega-Lite ChannelDefWithLegend definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    sort : object
        
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    legend : object
        
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    scale : object
        
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    title : string
        Title for axis or legend.
    field : string
        Name of the field from which to pull a data value.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', sort=jst.undefined, type=jst.undefined, legend=jst.undefined, timeUnit=jst.undefined, scale=jst.undefined, aggregate=jst.undefined, value=jst.undefined, title=jst.undefined, field=jst.undefined, bin=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(sort=sort, type=type, legend=legend, timeUnit=timeUnit, scale=scale, aggregate=aggregate, value=value, title=title, field=field, bin=bin)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(ChannelWithLegend, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(ChannelWithLegend, self)._finalize(**kwargs)


class Field(schema.FieldDef):
    """Wrapper for Vega-Lite FieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    title : string
        Title for axis or legend.
    field : string
        Name of the field from which to pull a data value.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', type=jst.undefined, timeUnit=jst.undefined, aggregate=jst.undefined, bin=jst.undefined, title=jst.undefined, field=jst.undefined, value=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(type=type, timeUnit=timeUnit, aggregate=aggregate, bin=bin, title=title, field=field, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(Field, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(Field, self)._finalize(**kwargs)


class OrderChannel(schema.OrderChannelDef):
    """Wrapper for Vega-Lite OrderChannelDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    sort : object
        
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    title : string
        Title for axis or legend.
    field : string
        Name of the field from which to pull a data value.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', sort=jst.undefined, type=jst.undefined, timeUnit=jst.undefined, aggregate=jst.undefined, value=jst.undefined, title=jst.undefined, field=jst.undefined, bin=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(sort=sort, type=type, timeUnit=timeUnit, aggregate=aggregate, value=value, title=title, field=field, bin=bin)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(OrderChannel, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(OrderChannel, self)._finalize(**kwargs)


class PositionChannel(schema.PositionChannelDef):
    """Wrapper for Vega-Lite PositionChannelDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    sort : object
        
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    axis : object
        
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    scale : object
        
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    title : string
        Title for axis or legend.
    field : string
        Name of the field from which to pull a data value.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', sort=jst.undefined, type=jst.undefined, axis=jst.undefined, timeUnit=jst.undefined, scale=jst.undefined, aggregate=jst.undefined, value=jst.undefined, title=jst.undefined, field=jst.undefined, bin=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(sort=sort, type=type, axis=axis, timeUnit=timeUnit, scale=scale, aggregate=aggregate, value=value, title=title, field=field, bin=bin)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(PositionChannel, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(PositionChannel, self)._finalize(**kwargs)


