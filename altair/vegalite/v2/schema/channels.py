# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# 2018-02-24 22:43

from . import core
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand, parse_shorthand_plus_data


class Color(core.MarkPropFieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the
        encoding channel will be removed.  __Default value:__ If undefined, default
        [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are
        applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function
        that transforms values in the data domain (numbers, dates, strings, etc) to
        visual values (pixels, colors, sizes) of the encoding channels.  __Default
        value:__ If undefined, default [scale
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include
        `"ascending"`, `"descending"` and `null` (no sorting). For fields with
        discrete domains, `sort` can also be a [sort field definition
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).
        __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, **kwds):
        super(Color, self).__init__(field=field, type=type, aggregate=aggregate,
                                    bin=bin, condition=condition, legend=legend,
                                    scale=scale, sort=sort, timeUnit=timeUnit,
                                    **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Color, self).to_dict(validate=validate, ignore=ignore, context=context)


class ColorValue(core.MarkPropValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<MarkPropFieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(ColorValue, self).__init__(value=value, condition=condition, **kwds)


class Column(core.FacetFieldDef):
    """Column schema wrapper
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    header : Header
        An object defining properties of a facet's header.
    sort : SortOrder
        Sort order for a facet field. This can be `"ascending"`, `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 header=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(Column, self).__init__(field=field, type=type, aggregate=aggregate,
                                     bin=bin, header=header, sort=sort,
                                     timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Column, self).to_dict(validate=validate, ignore=ignore, context=context)


class Detail(core.FieldDef):
    """
    Definition object for a data field, its type and transformation of an encoding 
    channel.
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, **kwds):
        super(Detail, self).__init__(field=field, type=type, aggregate=aggregate,
                                     bin=bin, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Detail, self).to_dict(validate=validate, ignore=ignore, context=context)


class Href(core.FieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, timeUnit=Undefined, **kwds):
        super(Href, self).__init__(field=field, type=type, aggregate=aggregate,
                                   bin=bin, condition=condition, timeUnit=timeUnit,
                                   **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Href, self).to_dict(validate=validate, ignore=ignore, context=context)


class HrefValue(core.ValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<FieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(HrefValue, self).__init__(value=value, condition=condition, **kwds)


class Opacity(core.MarkPropFieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the
        encoding channel will be removed.  __Default value:__ If undefined, default
        [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are
        applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function
        that transforms values in the data domain (numbers, dates, strings, etc) to
        visual values (pixels, colors, sizes) of the encoding channels.  __Default
        value:__ If undefined, default [scale
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include
        `"ascending"`, `"descending"` and `null` (no sorting). For fields with
        discrete domains, `sort` can also be a [sort field definition
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).
        __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, **kwds):
        super(Opacity, self).__init__(field=field, type=type, aggregate=aggregate,
                                      bin=bin, condition=condition, legend=legend,
                                      scale=scale, sort=sort, timeUnit=timeUnit,
                                      **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Opacity, self).to_dict(validate=validate, ignore=ignore, context=context)


class OpacityValue(core.MarkPropValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<MarkPropFieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(OpacityValue, self).__init__(value=value, condition=condition, **kwds)


class Order(core.OrderFieldDef):
    """Order schema wrapper
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    sort : SortOrder
        The sort order. One of `"ascending"` (default) or `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 sort=Undefined, timeUnit=Undefined, **kwds):
        super(Order, self).__init__(field=field, type=type, aggregate=aggregate,
                                    bin=bin, sort=sort, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Order, self).to_dict(validate=validate, ignore=ignore, context=context)


class Row(core.FacetFieldDef):
    """Row schema wrapper
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    header : Header
        An object defining properties of a facet's header.
    sort : SortOrder
        Sort order for a facet field. This can be `"ascending"`, `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 header=Undefined, sort=Undefined, timeUnit=Undefined, **kwds):
        super(Row, self).__init__(field=field, type=type, aggregate=aggregate,
                                  bin=bin, header=header, sort=sort,
                                  timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Row, self).to_dict(validate=validate, ignore=ignore, context=context)


class Shape(core.MarkPropFieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the
        encoding channel will be removed.  __Default value:__ If undefined, default
        [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are
        applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function
        that transforms values in the data domain (numbers, dates, strings, etc) to
        visual values (pixels, colors, sizes) of the encoding channels.  __Default
        value:__ If undefined, default [scale
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include
        `"ascending"`, `"descending"` and `null` (no sorting). For fields with
        discrete domains, `sort` can also be a [sort field definition
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).
        __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, **kwds):
        super(Shape, self).__init__(field=field, type=type, aggregate=aggregate,
                                    bin=bin, condition=condition, legend=legend,
                                    scale=scale, sort=sort, timeUnit=timeUnit,
                                    **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Shape, self).to_dict(validate=validate, ignore=ignore, context=context)


class ShapeValue(core.MarkPropValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<MarkPropFieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(ShapeValue, self).__init__(value=value, condition=condition, **kwds)


class Size(core.MarkPropFieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the
        encoding channel will be removed.  __Default value:__ If undefined, default
        [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are
        applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function
        that transforms values in the data domain (numbers, dates, strings, etc) to
        visual values (pixels, colors, sizes) of the encoding channels.  __Default
        value:__ If undefined, default [scale
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include
        `"ascending"`, `"descending"` and `null` (no sorting). For fields with
        discrete domains, `sort` can also be a [sort field definition
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).
        __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, **kwds):
        super(Size, self).__init__(field=field, type=type, aggregate=aggregate,
                                   bin=bin, condition=condition, legend=legend,
                                   scale=scale, sort=sort, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Size, self).to_dict(validate=validate, ignore=ignore, context=context)


class SizeValue(core.MarkPropValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<MarkPropFieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(SizeValue, self).__init__(value=value, condition=condition, **kwds)


class Text(core.TextFieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html)
        for a text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(Text, self).__init__(field=field, type=type, aggregate=aggregate,
                                   bin=bin, condition=condition, format=format,
                                   timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Text, self).to_dict(validate=validate, ignore=ignore, context=context)


class TextValue(core.TextValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<TextFieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(TextValue, self).__init__(value=value, condition=condition, **kwds)


class Tooltip(core.TextFieldDefWithCondition):
    """
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    condition : anyOf(Conditional<ValueDef>, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A
        field definition's `condition` property can only contain [value
        definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def)
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html)
        for a text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 condition=Undefined, format=Undefined, timeUnit=Undefined, **kwds):
        super(Tooltip, self).__init__(field=field, type=type, aggregate=aggregate,
                                      bin=bin, condition=condition, format=format,
                                      timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Tooltip, self).to_dict(validate=validate, ignore=ignore, context=context)


class TooltipValue(core.TextValueDefWithCondition):
    """
    A ValueDef with Condition<ValueDef | FieldDef>
    {
       condition: {field: ...} | {value: ...},
       value: ...,
    }
    
    Attributes
    ----------
    condition : anyOf(Conditional<TextFieldDef>, Conditional<ValueDef>, list)
        A field definition or one or more value definition(s) with a selection
        predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, condition=Undefined, **kwds):
        super(TooltipValue, self).__init__(value=value, condition=condition, **kwds)


class X(core.PositionFieldDef):
    """X schema wrapper
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    axis : anyOf(Axis, None)
        An object defining properties of axis's gridlines, ticks and labels. If
        `null`, the axis for the encoding channel will be removed.  __Default
        value:__ If undefined, default [axis
        properties](https://vega.github.io/vega-lite/docs/axis.html) are applied.
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    scale : Scale
        An object defining properties of the channel's scale, which is the function
        that transforms values in the data domain (numbers, dates, strings, etc) to
        visual values (pixels, colors, sizes) of the encoding channels.  __Default
        value:__ If undefined, default [scale
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include
        `"ascending"`, `"descending"` and `null` (no sorting). For fields with
        discrete domains, `sort` can also be a [sort field definition
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).
        __Default value:__ `"ascending"`
    stack : anyOf(StackOffset, None)
        Type of stacking offset if the field should be stacked. `stack` is only
        applicable for `x` and `y` channels with continuous domains. For example,
        `stack` of `y` can be used to customize stacking for a vertical bar chart.
        `stack` can be one of the following values: - `"zero"`: stacking with
        baseline offset at zero value of the scale (for creating typical stacked
        [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and
        [area](https://vega.github.io/vega-lite/docs/stack.html#area) chart). -
        `"normalize"` - stacking with normalized domain (for creating [normalized
        stacked bar and area
        charts](https://vega.github.io/vega-lite/docs/stack.html#normalized). <br/>
        -`"center"` - stacking with center baseline (for
        [streamgraph](https://vega.github.io/vega-lite/docs/stack.html#streamgraph)).
        - `null` - No-stacking. This will produce layered
        [bar](https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart)
        and area chart.  __Default value:__ `zero` for plots with all of the
        following conditions are true: (1) the mark is `bar` or `area`; (2) the
        stacked measure channel (x or y) has a linear scale; (3) At least one of
        non-position channels mapped to an unaggregated field that is different from
        x and y.  Otherwise, `null` by default.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, axis=Undefined,
                 bin=Undefined, scale=Undefined, sort=Undefined, stack=Undefined,
                 timeUnit=Undefined, **kwds):
        super(X, self).__init__(field=field, type=type, aggregate=aggregate,
                                axis=axis, bin=bin, scale=scale, sort=sort,
                                stack=stack, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X, self).to_dict(validate=validate, ignore=ignore, context=context)


class XValue(core.ValueDef):
    """
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color,
        values between `0` to `1` for opacity).
    """
    def __init__(self, value, **kwds):
        super(XValue, self).__init__(value=value, **kwds)


class X2(core.FieldDef):
    """
    Definition object for a data field, its type and transformation of an encoding 
    channel.
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, **kwds):
        super(X2, self).__init__(field=field, type=type, aggregate=aggregate,
                                 bin=bin, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X2, self).to_dict(validate=validate, ignore=ignore, context=context)


class X2Value(core.ValueDef):
    """
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color,
        values between `0` to `1` for opacity).
    """
    def __init__(self, value, **kwds):
        super(X2Value, self).__init__(value=value, **kwds)


class Y(core.PositionFieldDef):
    """Y schema wrapper
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    axis : anyOf(Axis, None)
        An object defining properties of axis's gridlines, ticks and labels. If
        `null`, the axis for the encoding channel will be removed.  __Default
        value:__ If undefined, default [axis
        properties](https://vega.github.io/vega-lite/docs/axis.html) are applied.
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    scale : Scale
        An object defining properties of the channel's scale, which is the function
        that transforms values in the data domain (numbers, dates, strings, etc) to
        visual values (pixels, colors, sizes) of the encoding channels.  __Default
        value:__ If undefined, default [scale
        properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include
        `"ascending"`, `"descending"` and `null` (no sorting). For fields with
        discrete domains, `sort` can also be a [sort field definition
        object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).
        __Default value:__ `"ascending"`
    stack : anyOf(StackOffset, None)
        Type of stacking offset if the field should be stacked. `stack` is only
        applicable for `x` and `y` channels with continuous domains. For example,
        `stack` of `y` can be used to customize stacking for a vertical bar chart.
        `stack` can be one of the following values: - `"zero"`: stacking with
        baseline offset at zero value of the scale (for creating typical stacked
        [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and
        [area](https://vega.github.io/vega-lite/docs/stack.html#area) chart). -
        `"normalize"` - stacking with normalized domain (for creating [normalized
        stacked bar and area
        charts](https://vega.github.io/vega-lite/docs/stack.html#normalized). <br/>
        -`"center"` - stacking with center baseline (for
        [streamgraph](https://vega.github.io/vega-lite/docs/stack.html#streamgraph)).
        - `null` - No-stacking. This will produce layered
        [bar](https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart)
        and area chart.  __Default value:__ `zero` for plots with all of the
        following conditions are true: (1) the mark is `bar` or `area`; (2) the
        stacked measure channel (x or y) has a linear scale; (3) At least one of
        non-position channels mapped to an unaggregated field that is different from
        x and y.  Otherwise, `null` by default.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, axis=Undefined,
                 bin=Undefined, scale=Undefined, sort=Undefined, stack=Undefined,
                 timeUnit=Undefined, **kwds):
        super(Y, self).__init__(field=field, type=type, aggregate=aggregate,
                                axis=axis, bin=bin, scale=scale, sort=sort,
                                stack=stack, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y, self).to_dict(validate=validate, ignore=ignore, context=context)


class YValue(core.ValueDef):
    """
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color,
        values between `0` to `1` for opacity).
    """
    def __init__(self, value, **kwds):
        super(YValue, self).__init__(value=value, **kwds)


class Y2(core.FieldDef):
    """
    Definition object for a data field, its type and transformation of an encoding 
    channel.
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`,
        `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If
        `true`, default [binning
        parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.
        __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a
        data value or an object defining iterated values from the
        [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested
        objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field
        names contain dots or brackets but are not nested, you can use `\\` to
        escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more
        details about escaping in the [field
        documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__
        `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal
        field. or [a temporal field that gets casted as
        ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default
        value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`,
        `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`,
        `"longitude"`, and `"geojson"`) when a [geographic
        projection](https://vega.github.io/vega-lite/docs/projection.html) is
        applied.
    """
    def __init__(self, field, type=Undefined, aggregate=Undefined, bin=Undefined,
                 timeUnit=Undefined, **kwds):
        super(Y2, self).__init__(field=field, type=type, aggregate=aggregate,
                                 bin=bin, timeUnit=timeUnit, **kwds)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y2, self).to_dict(validate=validate, ignore=ignore, context=context)


class Y2Value(core.ValueDef):
    """
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color,
        values between `0` to `1` for opacity).
    """
    def __init__(self, value, **kwds):
        super(Y2Value, self).__init__(value=value, **kwds)
