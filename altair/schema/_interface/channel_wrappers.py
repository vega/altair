# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-70-g6173dc1
# - date: 2017-07-21 10:12:17

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
    sort : object
        
    field : string
        Name of the field from which to pull a data value.
    legend : object
        
    title : string
        Title for axis or legend.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    scale : object
        
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', timeUnit=jst.undefined, type=jst.undefined, sort=jst.undefined, field=jst.undefined, legend=jst.undefined, title=jst.undefined, value=jst.undefined, bin=jst.undefined, aggregate=jst.undefined, scale=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(timeUnit=timeUnit, type=type, sort=sort, field=field, legend=legend, title=title, value=value, bin=bin, aggregate=aggregate, scale=scale)
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
    title : string
        Title for axis or legend.
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    field : string
        Name of the field from which to pull a data value.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', timeUnit=jst.undefined, type=jst.undefined, value=jst.undefined, title=jst.undefined, bin=jst.undefined, aggregate=jst.undefined, field=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(timeUnit=timeUnit, type=type, value=value, title=title, bin=bin, aggregate=aggregate, field=field)
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
    sort : object
        
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    title : string
        Title for axis or legend.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    field : string
        Name of the field from which to pull a data value.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', timeUnit=jst.undefined, type=jst.undefined, sort=jst.undefined, bin=jst.undefined, value=jst.undefined, title=jst.undefined, aggregate=jst.undefined, field=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(timeUnit=timeUnit, type=type, sort=sort, bin=bin, value=value, title=title, aggregate=aggregate, field=field)
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
    field : string
        Name of the field from which to pull a data value.
    sort : object
        
    axis : object
        
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    title : string
        Title for axis or legend.
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    scale : object
        
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', timeUnit=jst.undefined, type=jst.undefined, field=jst.undefined, sort=jst.undefined, axis=jst.undefined, bin=jst.undefined, value=jst.undefined, title=jst.undefined, aggregate=jst.undefined, scale=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(timeUnit=timeUnit, type=type, field=field, sort=sort, axis=axis, bin=bin, value=value, title=title, aggregate=aggregate, scale=scale)
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


