# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-31-g9016ca4
# - date: 2017-07-19 08:59:00

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
        
    field : string
        Name of the field from which to pull a data value.
    title : string
        Title for axis or legend.
    legend : object
        
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    scale : object
        
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', sort=jst.undefined, field=jst.undefined, title=jst.undefined, legend=jst.undefined, type=jst.undefined, scale=jst.undefined, bin=jst.undefined, aggregate=jst.undefined, value=jst.undefined, timeUnit=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(sort=sort, field=field, title=title, legend=legend, type=type, scale=scale, bin=bin, aggregate=aggregate, value=value, timeUnit=timeUnit)
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
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    field : string
        Name of the field from which to pull a data value.
    title : string
        Title for axis or legend.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', timeUnit=jst.undefined, type=jst.undefined, value=jst.undefined, bin=jst.undefined, aggregate=jst.undefined, field=jst.undefined, title=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(timeUnit=timeUnit, type=type, value=value, bin=bin, aggregate=aggregate, field=field, title=title)
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
        
    field : string
        Name of the field from which to pull a data value.
    title : string
        Title for axis or legend.
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', sort=jst.undefined, field=jst.undefined, title=jst.undefined, type=jst.undefined, bin=jst.undefined, aggregate=jst.undefined, value=jst.undefined, timeUnit=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(sort=sort, field=field, title=title, type=type, bin=bin, aggregate=aggregate, value=value, timeUnit=timeUnit)
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
        
    field : string
        Name of the field from which to pull a data value.
    title : string
        Title for axis or legend.
    type : object
        The encoded field's type of measurement. This can be either a
        full type
        name (`"quantitative"`, `"temporal"`, `"ordinal"`,  and
        `"nominal"`)
        or an initial character of the type name (`"Q"`, `"T"`, `"O"`,
        `"N"`).
        This property is case insensitive.
    scale : object
        
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    axis : object
        
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', sort=jst.undefined, field=jst.undefined, title=jst.undefined, type=jst.undefined, scale=jst.undefined, bin=jst.undefined, aggregate=jst.undefined, value=jst.undefined, axis=jst.undefined, timeUnit=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(sort=sort, field=field, title=title, type=type, scale=scale, bin=bin, aggregate=aggregate, value=value, axis=axis, timeUnit=timeUnit)
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


