# Auto-generated file: do not modify directly
# - altair version info: v1.2.0-69-ga13043b
# - date: 2017-07-19 14:16:39

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
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
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
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    field : string
        Name of the field from which to pull a data value.
    legend : object
        
    scale : object
        
    sort : object
        
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, title=jst.undefined, type=jst.undefined, timeUnit=jst.undefined, value=jst.undefined, field=jst.undefined, legend=jst.undefined, scale=jst.undefined, sort=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, title=title, type=type, timeUnit=timeUnit, value=value, field=field, legend=legend, scale=scale, sort=sort)
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
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
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
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    field : string
        Name of the field from which to pull a data value.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, title=jst.undefined, type=jst.undefined, timeUnit=jst.undefined, value=jst.undefined, field=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, title=title, type=type, timeUnit=timeUnit, value=value, field=field)
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
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
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
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    sort : object
        
    field : string
        Name of the field from which to pull a data value.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, title=jst.undefined, type=jst.undefined, timeUnit=jst.undefined, value=jst.undefined, sort=jst.undefined, field=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, title=title, type=type, timeUnit=timeUnit, value=value, sort=sort, field=field)
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
    aggregate : object
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
    bin : object
        Flag for binning a `quantitative` field, or a bin property
        object
        for binning parameters.
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
    timeUnit : object
        Time unit for a `temporal` field  (e.g., `year`, `yearmonth`,
        `month`, `hour`).
    value : ['number', 'string', 'boolean']
        A constant value in visual domain.
    scale : object
        
    sort : object
        
    axis : object
        
    field : string
        Name of the field from which to pull a data value.
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, title=jst.undefined, type=jst.undefined, timeUnit=jst.undefined, value=jst.undefined, scale=jst.undefined, sort=jst.undefined, axis=jst.undefined, field=jst.undefined, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, title=title, type=type, timeUnit=timeUnit, value=value, scale=scale, sort=sort, axis=axis, field=field)
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


