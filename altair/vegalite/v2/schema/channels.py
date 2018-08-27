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


class Color(FieldChannelMixin, core.MarkPropFieldDefWithCondition):
    """Color schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Color, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                    condition=condition, field=field, legend=legend, scale=scale,
                                    sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class ColorValue(ValueChannelMixin, core.MarkPropValueDefWithCondition):
    """ColorValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(ColorValue, self).__init__(value=value, condition=condition, **kwds)


class Column(FieldChannelMixin, core.FacetFieldDef):
    """Column schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    header : :class:`Header`
        An object defining properties of a facet's header.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(Column, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                     header=header, sort=sort, timeUnit=timeUnit, title=title,
                                     type=type, **kwds)


class Detail(FieldChannelMixin, core.FieldDef):
    """Detail schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Detail, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                     timeUnit=timeUnit, title=title, type=type, **kwds)


class Fill(FieldChannelMixin, core.MarkPropFieldDefWithCondition):
    """Fill schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Fill, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                   condition=condition, field=field, legend=legend, scale=scale,
                                   sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class FillValue(ValueChannelMixin, core.MarkPropValueDefWithCondition):
    """FillValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(FillValue, self).__init__(value=value, condition=condition, **kwds)


class Href(FieldChannelMixin, core.FieldDefWithCondition):
    """Href schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Href, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                   condition=condition, field=field, timeUnit=timeUnit, title=title,
                                   type=type, **kwds)


class HrefValue(ValueChannelMixin, core.ValueDefWithCondition):
    """HrefValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(HrefValue, self).__init__(value=value, condition=condition, **kwds)


class Key(FieldChannelMixin, core.FieldDef):
    """Key schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Key, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                  timeUnit=timeUnit, title=title, type=type, **kwds)


class Latitude(FieldChannelMixin, core.FieldDef):
    """Latitude schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Latitude, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                       timeUnit=timeUnit, title=title, type=type, **kwds)


class Latitude2(FieldChannelMixin, core.FieldDef):
    """Latitude2 schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Latitude2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                        timeUnit=timeUnit, title=title, type=type, **kwds)


class Longitude(FieldChannelMixin, core.FieldDef):
    """Longitude schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Longitude, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                        timeUnit=timeUnit, title=title, type=type, **kwds)


class Longitude2(FieldChannelMixin, core.FieldDef):
    """Longitude2 schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Longitude2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                         timeUnit=timeUnit, title=title, type=type, **kwds)


class Opacity(FieldChannelMixin, core.MarkPropFieldDefWithCondition):
    """Opacity schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Opacity, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                      condition=condition, field=field, legend=legend, scale=scale,
                                      sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class OpacityValue(ValueChannelMixin, core.MarkPropValueDefWithCondition):
    """OpacityValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(OpacityValue, self).__init__(value=value, condition=condition, **kwds)


class Order(FieldChannelMixin, core.OrderFieldDef):
    """Order schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    sort : :class:`SortOrder`
        The sort order. One of ``"ascending"`` (default) or ``"descending"``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Order, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                    sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class OrderValue(ValueChannelMixin, core.ValueDef):
    """OrderValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value of an encoding channel.

    Attributes
    ----------

    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, **kwds):
        super(OrderValue, self).__init__(value=value, **kwds)


class Row(FieldChannelMixin, core.FacetFieldDef):
    """Row schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    header : :class:`Header`
        An object defining properties of a facet's header.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(Row, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                  header=header, sort=sort, timeUnit=timeUnit, title=title, type=type,
                                  **kwds)


class Shape(FieldChannelMixin, core.MarkPropFieldDefWithCondition):
    """Shape schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Shape, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                    condition=condition, field=field, legend=legend, scale=scale,
                                    sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class ShapeValue(ValueChannelMixin, core.MarkPropValueDefWithCondition):
    """ShapeValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(ShapeValue, self).__init__(value=value, condition=condition, **kwds)


class Size(FieldChannelMixin, core.MarkPropFieldDefWithCondition):
    """Size schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Size, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                   condition=condition, field=field, legend=legend, scale=scale,
                                   sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class SizeValue(ValueChannelMixin, core.MarkPropValueDefWithCondition):
    """SizeValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(SizeValue, self).__init__(value=value, condition=condition, **kwds)


class Stroke(FieldChannelMixin, core.MarkPropFieldDefWithCondition):
    """Stroke schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend.
        If ``null``, the legend for the encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Stroke, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                     condition=condition, field=field, legend=legend, scale=scale,
                                     sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


class StrokeValue(ValueChannelMixin, core.MarkPropValueDefWithCondition):
    """StrokeValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(StrokeValue, self).__init__(value=value, condition=condition, **kwds)


class Text(FieldChannelMixin, core.TextFieldDefWithCondition):
    """Text schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The `formatting pattern <https://vega.github.io/vega-lite/docs/format.html>`__ for a
        text field. If not defined, this will be determined automatically.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(Text, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                   condition=condition, field=field, format=format, timeUnit=timeUnit,
                                   title=title, type=type, **kwds)


class TextValue(ValueChannelMixin, core.TextValueDefWithCondition):
    """TextValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalTextFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(TextValue, self).__init__(value=value, condition=condition, **kwds)


class Tooltip(FieldChannelMixin, core.TextFieldDefWithCondition):
    """Tooltip schema wrapper

    Mapping(required=[shorthand])
    A FieldDef with Condition :raw-html:`<ValueDef>`

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    condition : anyOf(:class:`ConditionalValueDef`, List(:class:`ConditionalValueDef`))
        One or more value definition(s) with a selection predicate.

        **Note:** A field definition's ``condition`` property can only contain `value
        definitions <https://vega.github.io/vega-lite/docs/encoding.html#value-def>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    format : string
        The `formatting pattern <https://vega.github.io/vega-lite/docs/format.html>`__ for a
        text field. If not defined, this will be determined automatically.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, condition=Undefined,
                 field=Undefined, format=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(Tooltip, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin,
                                      condition=condition, field=field, format=format,
                                      timeUnit=timeUnit, title=title, type=type, **kwds)


class TooltipValue(ValueChannelMixin, core.TextValueDefWithCondition):
    """TooltipValue schema wrapper

    Mapping(required=[])
    A ValueDef with Condition<ValueDef | FieldDef>

    Attributes
    ----------

    condition : anyOf(:class:`ConditionalTextFieldDef`, :class:`ConditionalValueDef`,
    List(:class:`ConditionalValueDef`))
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, condition=Undefined, **kwds):
        super(TooltipValue, self).__init__(value=value, condition=condition, **kwds)


class X(FieldChannelMixin, core.PositionFieldDef):
    """X schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels.
        If ``null``, the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    stack : anyOf(:class:`StackOffset`, None)
        Type of stacking offset if the field should be stacked.
        ``stack`` is only applicable for ``x`` and ``y`` channels with continuous domains.
        For example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * `"zero"`: stacking with baseline offset at zero value of the scale (for creating
          typical stacked [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and
          `area <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__.
          :raw-html:`<br/>`
        - ``"center"`` - stacking with center baseline (for `streamgraph
        <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar`` or ``area`` ;
        (2) the stacked measure channel (x or y) has a linear scale;
        (3) At least one of non-position channels mapped to an unaggregated field that is
        different from x and y.  Otherwise, ``null`` by default.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(X, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                field=field, scale=scale, sort=sort, stack=stack, timeUnit=timeUnit,
                                title=title, type=type, **kwds)


class XValue(ValueChannelMixin, core.ValueDef):
    """XValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value of an encoding channel.

    Attributes
    ----------

    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, **kwds):
        super(XValue, self).__init__(value=value, **kwds)


class X2(FieldChannelMixin, core.FieldDef):
    """X2 schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(X2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                 timeUnit=timeUnit, title=title, type=type, **kwds)


class X2Value(ValueChannelMixin, core.ValueDef):
    """X2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value of an encoding channel.

    Attributes
    ----------

    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, **kwds):
        super(X2Value, self).__init__(value=value, **kwds)


class Y(FieldChannelMixin, core.PositionFieldDef):
    """Y schema wrapper

    Mapping(required=[shorthand])

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels.
        If ``null``, the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          Javascript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order.  For discrete time field, values in the sort array can be
          `date-time definition objects <types#datetime>`__. In addition, for time units
          ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    stack : anyOf(:class:`StackOffset`, None)
        Type of stacking offset if the field should be stacked.
        ``stack`` is only applicable for ``x`` and ``y`` channels with continuous domains.
        For example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * `"zero"`: stacking with baseline offset at zero value of the scale (for creating
          typical stacked [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and
          `area <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__.
          :raw-html:`<br/>`
        - ``"center"`` - stacking with center baseline (for `streamgraph
        <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar`` or ``area`` ;
        (2) the stacked measure channel (x or y) has a linear scale;
        (3) At least one of non-position channels mapped to an unaggregated field that is
        different from x and y.  Otherwise, ``null`` by default.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Y, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis, bin=bin,
                                field=field, scale=scale, sort=sort, stack=stack, timeUnit=timeUnit,
                                title=title, type=type, **kwds)


class YValue(ValueChannelMixin, core.ValueDef):
    """YValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value of an encoding channel.

    Attributes
    ----------

    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, **kwds):
        super(YValue, self).__init__(value=value, **kwds)


class Y2(FieldChannelMixin, core.FieldDef):
    """Y2 schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Attributes
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field
        (e.g., ``mean``, ``sum``, ``median``, ``min``, ``max``, ``count`` ).

        **Default value:** ``undefined`` (None)
    bin : anyOf(boolean, :class:`BinParams`)
        A flag for binning a ``quantitative`` field, or `an object defining binning
        parameters <https://vega.github.io/vega-lite/docs/bin.html#params>`__.
        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html>`__ will be applied.

        **Default value:** ``false``
    field : anyOf(string, :class:`RepeatRef`)
        **Required.** A string defining the name of the field from which to pull a data
        value
        or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **Note:** Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ).
        If field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ).
        See more details about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__.

        **Note:** ``field`` is not required if ``aggregate`` is ``count``.
    timeUnit : :class:`TimeUnit`
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field.
        or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)
    title : anyOf(string, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ).  If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the [fieldTitle
        property in the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or
        `fieldTitle function via the compile function's options
        <https://vega.github.io/vega-lite/docs/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The encoded field's type of measurement ( ``"quantitative"``, ``"temporal"``,
        ``"ordinal"``, or ``"nominal"`` ).
        It can also be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, shorthand=Undefined, aggregate=Undefined, bin=Undefined, field=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Y2, self).__init__(shorthand=shorthand, aggregate=aggregate, bin=bin, field=field,
                                 timeUnit=timeUnit, title=title, type=type, **kwds)


class Y2Value(ValueChannelMixin, core.ValueDef):
    """Y2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value of an encoding channel.

    Attributes
    ----------

    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., ``"red"`` / "#0099ff" for color, values
        between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False

    def __init__(self, value, **kwds):
        super(Y2Value, self).__init__(value=value, **kwds)
