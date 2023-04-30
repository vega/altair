# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.

import sys
from . import core
import pandas as pd
from altair.utils.schemapi import Undefined, with_property_setters
from altair.utils import parse_shorthand
from typing import overload, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


class FieldChannelMixin:
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        shorthand = self._get('shorthand')
        field = self._get('field')

        if shorthand is not Undefined and field is not Undefined:
            raise ValueError("{} specifies both shorthand={} and field={}. "
                             "".format(self.__class__.__name__, shorthand, field))

        if isinstance(shorthand, (tuple, list)):
            # If given a list of shorthands, then transform it to a list of classes
            kwds = self._kwds.copy()
            kwds.pop('shorthand')
            return [self.__class__(sh, **kwds).to_dict(validate=validate, ignore=ignore, context=context)
                    for sh in shorthand]

        if shorthand is Undefined:
            parsed = {}
        elif isinstance(shorthand, str):
            parsed = parse_shorthand(shorthand, data=context.get('data', None))
            type_required = 'type' in self._kwds
            type_in_shorthand = 'type' in parsed
            type_defined_explicitly = self._get('type') is not Undefined
            if not type_required:
                # Secondary field names don't require a type argument in VegaLite 3+.
                # We still parse it out of the shorthand, but drop it here.
                parsed.pop('type', None)
            elif not (type_in_shorthand or type_defined_explicitly):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError(
                        'Unable to determine data type for the field "{}";'
                        " verify that the field name is not misspelled."
                        " If you are referencing a field from a transform,"
                        " also confirm that the data type is specified correctly.".format(shorthand)
                    )
                else:
                    raise ValueError("{} encoding field is specified without a type; "
                                     "the type cannot be automatically inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(shorthand))
        else:
            # Shorthand is not a string; we pass the definition to field,
            # and do not do any parsing.
            parsed = {'field': shorthand}
        context["parsed_shorthand"] = parsed

        return super(FieldChannelMixin, self).to_dict(
            validate=validate,
            ignore=ignore,
            context=context
        )


class ValueChannelMixin:
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        condition = self._get('condition', Undefined)
        copy = self  # don't copy unless we need to
        if condition is not Undefined:
            if isinstance(condition, core.SchemaBase):
                pass
            elif 'field' in condition and 'type' not in condition:
                kwds = parse_shorthand(condition['field'], context.get('data', None))
                copy = self.copy(deep=['condition'])
                copy['condition'].update(kwds)
        return super(ValueChannelMixin, copy).to_dict(validate=validate,
                                                      ignore=ignore,
                                                      context=context)


class DatumChannelMixin:
    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {}
        datum = self._get('datum', Undefined)
        copy = self  # don't copy unless we need to
        if datum is not Undefined:
            if isinstance(datum, core.SchemaBase):
                pass
        return super(DatumChannelMixin, copy).to_dict(validate=validate,
                                                      ignore=ignore,
                                                      context=context)


@with_property_setters
class Angle(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumber):
    """Angle schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "angle"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Angle':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Angle':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Angle':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Angle':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Angle, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                    bin=bin, condition=condition, field=field, legend=legend,
                                    scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type,
                                    **kwds)


@with_property_setters
class AngleDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumber):
    """AngleDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "angle"

    def bandPosition(self, _: float, **kwds) -> 'AngleDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'AngleDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'AngleDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'AngleDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'AngleDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'AngleDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'AngleDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'AngleDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(AngleDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                         title=title, type=type, **kwds)


@with_property_setters
class AngleValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumber):
    """AngleValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "angle"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'AngleValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'AngleValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'AngleValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'AngleValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'AngleValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'AngleValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'AngleValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(AngleValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Color(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefGradientstringnull):
    """Color schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "color"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Color':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Color':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Color':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Color':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Color, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                    bin=bin, condition=condition, field=field, legend=legend,
                                    scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type,
                                    **kwds)


@with_property_setters
class ColorDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefGradientstringnull):
    """ColorDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "color"

    def bandPosition(self, _: float, **kwds) -> 'ColorDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'ColorDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'ColorDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'ColorDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'ColorDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'ColorDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'ColorDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'ColorDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(ColorDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                         title=title, type=type, **kwds)


@with_property_setters
class ColorValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefGradientstringnull):
    """ColorValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(:class:`Gradient`, string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "color"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ColorValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ColorValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ColorValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ColorValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'ColorValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'ColorValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'ColorValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(ColorValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Column(FieldChannelMixin, core.RowColumnEncodingFieldDef):
    """Column schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    align : :class:`LayoutAlign`
        The alignment to apply to row/column facet's subplot. The supported string values
        are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        **Default value:** ``"all"``.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    center : boolean
        Boolean flag indicating if facet's subviews should be centered relative to their
        respective rows or columns.

        **Default value:** ``false``
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    header : anyOf(:class:`Header`, None)
        An object defining properties of a facet's header.
    sort : anyOf(:class:`SortArray`, :class:`SortOrder`, :class:`EncodingSortField`, None)
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    spacing : float
        The spacing in pixels between facet's sub-views.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "column"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Column':
        ...

    def align(self, _: Literal["all", "each", "none"], **kwds) -> 'Column':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Column':
        ...

    def center(self, _: bool, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def header(self, format=Undefined, formatType=Undefined, labelAlign=Undefined, labelAnchor=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOrient=Undefined, labelPadding=Undefined, labels=Undefined, orient=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOrient=Undefined, titlePadding=Undefined, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def header(self, _: None, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Column':
        ...

    def spacing(self, _: float, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Column':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Column':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Column':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, align=Undefined,
                 bandPosition=Undefined, bin=Undefined, center=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, spacing=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Column, self).__init__(shorthand=shorthand, aggregate=aggregate, align=align,
                                     bandPosition=bandPosition, bin=bin, center=center, field=field,
                                     header=header, sort=sort, spacing=spacing, timeUnit=timeUnit,
                                     title=title, type=type, **kwds)


@with_property_setters
class Description(FieldChannelMixin, core.StringFieldDefWithCondition):
    """Description schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstringExprRef`, List(:class:`ConditionalValueDefstringExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    format : anyOf(string, :class:`Dict`)
        When used with the default ``"number"`` and ``"time"`` format type, the text
        formatting pattern for labels of guides (axes, legends, headers) and text marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        When used with a `custom formatType
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__, this
        value will be passed as ``format`` alongside ``datum.value`` to the registered
        function.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : string
        The format type for labels. One of ``"number"``, ``"time"``, or a `registered custom
        format type
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__.

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nominal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nominal fields without
          ``timeUnit``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "description"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Description':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringExprRef], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: str, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: dict, **kwds) -> 'Description':
        ...

    def formatType(self, _: str, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Description':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Description':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Description':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, format=Undefined, formatType=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Description, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                          bandPosition=bandPosition, bin=bin, condition=condition,
                                          field=field, format=format, formatType=formatType,
                                          timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class DescriptionValue(ValueChannelMixin, core.StringValueDefWithCondition):
    """DescriptionValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "description"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'DescriptionValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'DescriptionValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'DescriptionValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'DescriptionValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'DescriptionValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'DescriptionValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'DescriptionValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(DescriptionValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Detail(FieldChannelMixin, core.FieldDefWithoutScale):
    """Detail schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "detail"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Detail':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Detail':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Detail':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Detail':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Detail, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                     bandPosition=bandPosition, bin=bin, field=field, timeUnit=timeUnit,
                                     title=title, type=type, **kwds)


@with_property_setters
class Facet(FieldChannelMixin, core.FacetEncodingFieldDef):
    """Facet schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    align : anyOf(:class:`LayoutAlign`, :class:`RowColLayoutAlign`)
        The alignment to apply to grid rows and columns. The supported string values are
        ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        Alternatively, an object value of the form ``{"row": string, "column": string}`` can
        be used to supply different alignments for rows and columns.

        **Default value:** ``"all"``.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    bounds : enum('full', 'flush')
        The bounds calculation method to use for determining the extent of a sub-plot. One
        of ``full`` (the default) or ``flush``.


        * If set to ``full``, the entire calculated bounds (including axes, title, and
          legend) will be used.
        * If set to ``flush``, only the specified width and height values for the sub-view
          will be used. The ``flush`` setting can be useful when attempting to place
          sub-plots without axes or legends into a uniform grid structure.

        **Default value:** ``"full"``
    center : anyOf(boolean, :class:`RowColboolean`)
        Boolean flag indicating if subviews should be centered relative to their respective
        rows or columns.

        An object value of the form ``{"row": boolean, "column": boolean}`` can be used to
        supply different centering values for rows and columns.

        **Default value:** ``false``
    columns : float
        The number of columns to include in the view composition layout.

        **Default value** : ``undefined`` -- An infinite number of columns (a single row)
        will be assumed. This is equivalent to ``hconcat`` (for ``concat`` ) and to using
        the ``column`` channel (for ``facet`` and ``repeat`` ).

        **Note** :

        1) This property is only for:


        * the general (wrappable) ``concat`` operator (not ``hconcat`` / ``vconcat`` )
        * the ``facet`` and ``repeat`` operator with one field/repetition definition
          (without row/column nesting)

        2) Setting the ``columns`` to ``1`` is equivalent to ``vconcat`` (for ``concat`` )
        and to using the ``row`` channel (for ``facet`` and ``repeat`` ).
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    header : anyOf(:class:`Header`, None)
        An object defining properties of a facet's header.
    sort : anyOf(:class:`SortArray`, :class:`SortOrder`, :class:`EncodingSortField`, None)
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    spacing : anyOf(float, :class:`RowColnumber`)
        The spacing in pixels between sub-views of the composition operator. An object of
        the form ``{"row": number, "column": number}`` can be used to set different spacing
        values for rows and columns.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "facet"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def align(self, _: Literal["all", "each", "none"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def align(self, column=Undefined, row=Undefined, **kwds) -> 'Facet':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Facet':
        ...

    def bounds(self, _: Literal["full", "flush"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def center(self, _: bool, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def center(self, column=Undefined, row=Undefined, **kwds) -> 'Facet':
        ...

    def columns(self, _: float, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def header(self, format=Undefined, formatType=Undefined, labelAlign=Undefined, labelAnchor=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOrient=Undefined, labelPadding=Undefined, labels=Undefined, orient=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOrient=Undefined, titlePadding=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def header(self, _: None, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def spacing(self, _: float, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def spacing(self, column=Undefined, row=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Facet':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Facet':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Facet':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, align=Undefined,
                 bandPosition=Undefined, bin=Undefined, bounds=Undefined, center=Undefined,
                 columns=Undefined, field=Undefined, header=Undefined, sort=Undefined,
                 spacing=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Facet, self).__init__(shorthand=shorthand, aggregate=aggregate, align=align,
                                    bandPosition=bandPosition, bin=bin, bounds=bounds, center=center,
                                    columns=columns, field=field, header=header, sort=sort,
                                    spacing=spacing, timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class Fill(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefGradientstringnull):
    """Fill schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "fill"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Fill':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Fill':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Fill':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Fill':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Fill, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                   bin=bin, condition=condition, field=field, legend=legend,
                                   scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type,
                                   **kwds)


@with_property_setters
class FillDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefGradientstringnull):
    """FillDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "fill"

    def bandPosition(self, _: float, **kwds) -> 'FillDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'FillDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'FillDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'FillDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'FillDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'FillDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'FillDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'FillDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(FillDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                        title=title, type=type, **kwds)


@with_property_setters
class FillValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefGradientstringnull):
    """FillValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(:class:`Gradient`, string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "fill"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'FillValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'FillValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'FillValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(FillValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class FillOpacity(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumber):
    """FillOpacity schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "fillOpacity"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'FillOpacity':
        ...

    def bandPosition(self, _: float, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'FillOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'FillOpacity':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'FillOpacity':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(FillOpacity, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                          bandPosition=bandPosition, bin=bin, condition=condition,
                                          field=field, legend=legend, scale=scale, sort=sort,
                                          timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class FillOpacityDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumber):
    """FillOpacityDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "fillOpacity"

    def bandPosition(self, _: float, **kwds) -> 'FillOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'FillOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'FillOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'FillOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'FillOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'FillOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'FillOpacityDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'FillOpacityDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(FillOpacityDatum, self).__init__(datum=datum, bandPosition=bandPosition,
                                               condition=condition, title=title, type=type, **kwds)


@with_property_setters
class FillOpacityValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumber):
    """FillOpacityValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "fillOpacity"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'FillOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'FillOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'FillOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'FillOpacityValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(FillOpacityValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Href(FieldChannelMixin, core.StringFieldDefWithCondition):
    """Href schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstringExprRef`, List(:class:`ConditionalValueDefstringExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    format : anyOf(string, :class:`Dict`)
        When used with the default ``"number"`` and ``"time"`` format type, the text
        formatting pattern for labels of guides (axes, legends, headers) and text marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        When used with a `custom formatType
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__, this
        value will be passed as ``format`` alongside ``datum.value`` to the registered
        function.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : string
        The format type for labels. One of ``"number"``, ``"time"``, or a `registered custom
        format type
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__.

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nominal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nominal fields without
          ``timeUnit``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "href"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Href':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringExprRef], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: str, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: dict, **kwds) -> 'Href':
        ...

    def formatType(self, _: str, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Href':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Href':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Href':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, format=Undefined, formatType=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Href, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                   bin=bin, condition=condition, field=field, format=format,
                                   formatType=formatType, timeUnit=timeUnit, title=title, type=type,
                                   **kwds)


@with_property_setters
class HrefValue(ValueChannelMixin, core.StringValueDefWithCondition):
    """HrefValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "href"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'HrefValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'HrefValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'HrefValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'HrefValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'HrefValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'HrefValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'HrefValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(HrefValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Key(FieldChannelMixin, core.FieldDefWithoutScale):
    """Key schema wrapper

    Mapping(required=[shorthand])
    Definition object for a data field, its type and transformation of an encoding channel.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "key"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Key':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Key':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Key':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Key':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Key, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                  bin=bin, field=field, timeUnit=timeUnit, title=title, type=type,
                                  **kwds)


@with_property_setters
class Latitude(FieldChannelMixin, core.LatLongFieldDef):
    """Latitude schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : string
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "latitude"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Latitude':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Latitude':
        ...

    def bin(self, _: None, **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Latitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Latitude':
        ...

    def type(self, _: str, **kwds) -> 'Latitude':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Latitude, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                       bandPosition=bandPosition, bin=bin, field=field,
                                       timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class LatitudeDatum(DatumChannelMixin, core.DatumDef):
    """LatitudeDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "latitude"

    def bandPosition(self, _: float, **kwds) -> 'LatitudeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'LatitudeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'LatitudeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'LatitudeDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'LatitudeDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(LatitudeDatum, self).__init__(datum=datum, bandPosition=bandPosition, title=title,
                                            type=type, **kwds)


@with_property_setters
class Latitude2(FieldChannelMixin, core.SecondaryFieldDef):
    """Latitude2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "latitude2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Latitude2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Latitude2':
        ...

    def bin(self, _: None, **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Latitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Latitude2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(Latitude2, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                        bandPosition=bandPosition, bin=bin, field=field,
                                        timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class Latitude2Datum(DatumChannelMixin, core.DatumDef):
    """Latitude2Datum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "latitude2"

    def bandPosition(self, _: float, **kwds) -> 'Latitude2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Latitude2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Latitude2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Latitude2Datum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'Latitude2Datum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Latitude2Datum, self).__init__(datum=datum, bandPosition=bandPosition, title=title,
                                             type=type, **kwds)


@with_property_setters
class Latitude2Value(ValueChannelMixin, core.PositionValueDef):
    """Latitude2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "latitude2"

    

    def __init__(self, value, **kwds):
        super(Latitude2Value, self).__init__(value=value, **kwds)


@with_property_setters
class Longitude(FieldChannelMixin, core.LatLongFieldDef):
    """Longitude schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : string
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "longitude"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Longitude':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Longitude':
        ...

    def bin(self, _: None, **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Longitude':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Longitude':
        ...

    def type(self, _: str, **kwds) -> 'Longitude':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Longitude, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                        bandPosition=bandPosition, bin=bin, field=field,
                                        timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class LongitudeDatum(DatumChannelMixin, core.DatumDef):
    """LongitudeDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "longitude"

    def bandPosition(self, _: float, **kwds) -> 'LongitudeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'LongitudeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'LongitudeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'LongitudeDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'LongitudeDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(LongitudeDatum, self).__init__(datum=datum, bandPosition=bandPosition, title=title,
                                             type=type, **kwds)


@with_property_setters
class Longitude2(FieldChannelMixin, core.SecondaryFieldDef):
    """Longitude2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "longitude2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Longitude2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Longitude2':
        ...

    def bin(self, _: None, **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Longitude2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Longitude2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(Longitude2, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                         bandPosition=bandPosition, bin=bin, field=field,
                                         timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class Longitude2Datum(DatumChannelMixin, core.DatumDef):
    """Longitude2Datum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "longitude2"

    def bandPosition(self, _: float, **kwds) -> 'Longitude2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Longitude2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Longitude2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Longitude2Datum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'Longitude2Datum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Longitude2Datum, self).__init__(datum=datum, bandPosition=bandPosition, title=title,
                                              type=type, **kwds)


@with_property_setters
class Longitude2Value(ValueChannelMixin, core.PositionValueDef):
    """Longitude2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "longitude2"

    

    def __init__(self, value, **kwds):
        super(Longitude2Value, self).__init__(value=value, **kwds)


@with_property_setters
class Opacity(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumber):
    """Opacity schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "opacity"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Opacity':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Opacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Opacity':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Opacity':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Opacity, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, condition=condition,
                                      field=field, legend=legend, scale=scale, sort=sort,
                                      timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class OpacityDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumber):
    """OpacityDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "opacity"

    def bandPosition(self, _: float, **kwds) -> 'OpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'OpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'OpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'OpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'OpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'OpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'OpacityDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'OpacityDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(OpacityDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                           title=title, type=type, **kwds)


@with_property_setters
class OpacityValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumber):
    """OpacityValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "opacity"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'OpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'OpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'OpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'OpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'OpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'OpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'OpacityValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(OpacityValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Order(FieldChannelMixin, core.OrderFieldDef):
    """Order schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    sort : :class:`SortOrder`
        The sort order. One of ``"ascending"`` (default) or ``"descending"``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "order"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Order':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Order':
        ...

    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Order':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Order':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Order':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(Order, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                    bin=bin, field=field, sort=sort, timeUnit=timeUnit, title=title,
                                    type=type, **kwds)


@with_property_setters
class OrderValue(ValueChannelMixin, core.OrderValueDef):
    """OrderValue schema wrapper

    Mapping(required=[value])

    Parameters
    ----------

    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    condition : anyOf(:class:`ConditionalValueDefnumber`, List(:class:`ConditionalValueDefnumber`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "order"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'OrderValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'OrderValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumber], **kwds) -> 'OrderValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(OrderValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Radius(FieldChannelMixin, core.PositionFieldDefBase):
    """Radius schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "radius"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Radius':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Radius':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Radius':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Radius':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Radius, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                     bandPosition=bandPosition, bin=bin, field=field, scale=scale,
                                     sort=sort, stack=stack, timeUnit=timeUnit, title=title, type=type,
                                     **kwds)


@with_property_setters
class RadiusDatum(DatumChannelMixin, core.PositionDatumDefBase):
    """RadiusDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "radius"

    def bandPosition(self, _: float, **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'RadiusDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'RadiusDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'RadiusDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, scale=Undefined, stack=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(RadiusDatum, self).__init__(datum=datum, bandPosition=bandPosition, scale=scale,
                                          stack=stack, title=title, type=type, **kwds)


@with_property_setters
class RadiusValue(ValueChannelMixin, core.PositionValueDef):
    """RadiusValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "radius"

    

    def __init__(self, value, **kwds):
        super(RadiusValue, self).__init__(value=value, **kwds)


@with_property_setters
class Radius2(FieldChannelMixin, core.SecondaryFieldDef):
    """Radius2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "radius2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Radius2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Radius2':
        ...

    def bin(self, _: None, **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Radius2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Radius2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(Radius2, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, field=field,
                                      timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class Radius2Datum(DatumChannelMixin, core.DatumDef):
    """Radius2Datum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "radius2"

    def bandPosition(self, _: float, **kwds) -> 'Radius2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Radius2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Radius2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Radius2Datum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'Radius2Datum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Radius2Datum, self).__init__(datum=datum, bandPosition=bandPosition, title=title,
                                           type=type, **kwds)


@with_property_setters
class Radius2Value(ValueChannelMixin, core.PositionValueDef):
    """Radius2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "radius2"

    

    def __init__(self, value, **kwds):
        super(Radius2Value, self).__init__(value=value, **kwds)


@with_property_setters
class Row(FieldChannelMixin, core.RowColumnEncodingFieldDef):
    """Row schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    align : :class:`LayoutAlign`
        The alignment to apply to row/column facet's subplot. The supported string values
        are ``"all"``, ``"each"``, and ``"none"``.


        * For ``"none"``, a flow layout will be used, in which adjacent subviews are simply
          placed one after the other.
        * For ``"each"``, subviews will be aligned into a clean grid structure, but each row
          or column may be of variable size.
        * For ``"all"``, subviews will be aligned and each row or column will be sized
          identically based on the maximum observed size. String values for this property
          will be applied to both grid rows and columns.

        **Default value:** ``"all"``.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    center : boolean
        Boolean flag indicating if facet's subviews should be centered relative to their
        respective rows or columns.

        **Default value:** ``false``
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    header : anyOf(:class:`Header`, None)
        An object defining properties of a facet's header.
    sort : anyOf(:class:`SortArray`, :class:`SortOrder`, :class:`EncodingSortField`, None)
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` is not supported for ``row`` and ``column``.
    spacing : float
        The spacing in pixels between facet's sub-views.

        **Default value** : Depends on ``"spacing"`` property of `the view composition
        configuration <https://vega.github.io/vega-lite/docs/config.html#view-config>`__ (
        ``20`` by default)
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "row"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Row':
        ...

    def align(self, _: Literal["all", "each", "none"], **kwds) -> 'Row':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Row':
        ...

    def center(self, _: bool, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def header(self, format=Undefined, formatType=Undefined, labelAlign=Undefined, labelAnchor=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOrient=Undefined, labelPadding=Undefined, labels=Undefined, orient=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOrient=Undefined, titlePadding=Undefined, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def header(self, _: None, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Row':
        ...

    def spacing(self, _: float, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Row':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Row':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Row':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, align=Undefined,
                 bandPosition=Undefined, bin=Undefined, center=Undefined, field=Undefined,
                 header=Undefined, sort=Undefined, spacing=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Row, self).__init__(shorthand=shorthand, aggregate=aggregate, align=align,
                                  bandPosition=bandPosition, bin=bin, center=center, field=field,
                                  header=header, sort=sort, spacing=spacing, timeUnit=timeUnit,
                                  title=title, type=type, **kwds)


@with_property_setters
class Shape(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefTypeForShapestringnull):
    """Shape schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`TypeForShape`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "shape"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Shape':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Shape':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Shape':
        ...

    def type(self, _: Literal["nominal", "ordinal", "geojson"], **kwds) -> 'Shape':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Shape, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                    bin=bin, condition=condition, field=field, legend=legend,
                                    scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type,
                                    **kwds)


@with_property_setters
class ShapeDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefstringnull):
    """ShapeDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "shape"

    def bandPosition(self, _: float, **kwds) -> 'ShapeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'ShapeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'ShapeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'ShapeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'ShapeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'ShapeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'ShapeDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'ShapeDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(ShapeDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                         title=title, type=type, **kwds)


@with_property_setters
class ShapeValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefTypeForShapestringnull):
    """ShapeValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDefTypeForShape`, :class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "shape"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ShapeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ShapeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ShapeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'ShapeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'ShapeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'ShapeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'ShapeValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(ShapeValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Size(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumber):
    """Size schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "size"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Size':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Size':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Size':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Size':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Size, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                   bin=bin, condition=condition, field=field, legend=legend,
                                   scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type,
                                   **kwds)


@with_property_setters
class SizeDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumber):
    """SizeDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "size"

    def bandPosition(self, _: float, **kwds) -> 'SizeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'SizeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'SizeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'SizeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'SizeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'SizeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'SizeDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'SizeDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(SizeDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                        title=title, type=type, **kwds)


@with_property_setters
class SizeValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumber):
    """SizeValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "size"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'SizeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'SizeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'SizeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'SizeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'SizeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'SizeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'SizeValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(SizeValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Stroke(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefGradientstringnull):
    """Stroke schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "stroke"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Stroke':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Stroke':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Stroke':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Stroke':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Stroke, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                     bandPosition=bandPosition, bin=bin, condition=condition,
                                     field=field, legend=legend, scale=scale, sort=sort,
                                     timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class StrokeDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefGradientstringnull):
    """StrokeDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "stroke"

    def bandPosition(self, _: float, **kwds) -> 'StrokeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'StrokeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'StrokeDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(StrokeDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                          title=title, type=type, **kwds)


@with_property_setters
class StrokeValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefGradientstringnull):
    """StrokeValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefGradientstringnullExprRef`, List(:class:`ConditionalValueDefGradientstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(:class:`Gradient`, string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "stroke"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefGradientstringnullExprRef], **kwds) -> 'StrokeValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(StrokeValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class StrokeDash(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumberArray):
    """StrokeDash schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberArrayExprRef`, List(:class:`ConditionalValueDefnumberArrayExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeDash"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'StrokeDash':
        ...

    def bandPosition(self, _: float, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberArrayExprRef], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeDash':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeDash':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'StrokeDash':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(StrokeDash, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                         bandPosition=bandPosition, bin=bin, condition=condition,
                                         field=field, legend=legend, scale=scale, sort=sort,
                                         timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class StrokeDashDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumberArray):
    """StrokeDashDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberArrayExprRef`, List(:class:`ConditionalValueDefnumberArrayExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeDash"

    def bandPosition(self, _: float, **kwds) -> 'StrokeDashDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeDashDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeDashDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberArrayExprRef], **kwds) -> 'StrokeDashDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeDashDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeDashDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeDashDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'StrokeDashDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(StrokeDashDatum, self).__init__(datum=datum, bandPosition=bandPosition,
                                              condition=condition, title=title, type=type, **kwds)


@with_property_setters
class StrokeDashValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumberArray):
    """StrokeDashValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberArrayExprRef`, List(:class:`ConditionalValueDefnumberArrayExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(List(float), :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeDash"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeDashValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeDashValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeDashValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeDashValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeDashValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeDashValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberArrayExprRef], **kwds) -> 'StrokeDashValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(StrokeDashValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class StrokeOpacity(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumber):
    """StrokeOpacity schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeOpacity"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    def bandPosition(self, _: float, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeOpacity':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeOpacity':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'StrokeOpacity':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(StrokeOpacity, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                            bandPosition=bandPosition, bin=bin, condition=condition,
                                            field=field, legend=legend, scale=scale, sort=sort,
                                            timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class StrokeOpacityDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumber):
    """StrokeOpacityDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeOpacity"

    def bandPosition(self, _: float, **kwds) -> 'StrokeOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'StrokeOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeOpacityDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeOpacityDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'StrokeOpacityDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(StrokeOpacityDatum, self).__init__(datum=datum, bandPosition=bandPosition,
                                                 condition=condition, title=title, type=type, **kwds)


@with_property_setters
class StrokeOpacityValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumber):
    """StrokeOpacityValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeOpacity"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeOpacityValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'StrokeOpacityValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(StrokeOpacityValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class StrokeWidth(FieldChannelMixin, core.FieldOrDatumDefWithConditionMarkPropFieldDefnumber):
    """StrokeWidth schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    legend : anyOf(:class:`Legend`, None)
        An object defining properties of the legend. If ``null``, the legend for the
        encoding channel will be removed.

        **Default value:** If undefined, default `legend properties
        <https://vega.github.io/vega-lite/docs/legend.html>`__ are applied.

        **See also:** `legend <https://vega.github.io/vega-lite/docs/legend.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeWidth"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'StrokeWidth':
        ...

    def bandPosition(self, _: float, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, aria=Undefined, clipHeight=Undefined, columnPadding=Undefined, columns=Undefined, cornerRadius=Undefined, description=Undefined, direction=Undefined, fillColor=Undefined, format=Undefined, formatType=Undefined, gradientLength=Undefined, gradientOpacity=Undefined, gradientStrokeColor=Undefined, gradientStrokeWidth=Undefined, gradientThickness=Undefined, gridAlign=Undefined, labelAlign=Undefined, labelBaseline=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, legendX=Undefined, legendY=Undefined, offset=Undefined, orient=Undefined, padding=Undefined, rowPadding=Undefined, strokeColor=Undefined, symbolDash=Undefined, symbolDashOffset=Undefined, symbolFillColor=Undefined, symbolLimit=Undefined, symbolOffset=Undefined, symbolOpacity=Undefined, symbolSize=Undefined, symbolStrokeColor=Undefined, symbolStrokeWidth=Undefined, symbolType=Undefined, tickCount=Undefined, tickMinStep=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titleOrient=Undefined, titlePadding=Undefined, type=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def legend(self, _: None, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeWidth':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeWidth':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'StrokeWidth':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, legend=Undefined, scale=Undefined,
                 sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(StrokeWidth, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                          bandPosition=bandPosition, bin=bin, condition=condition,
                                          field=field, legend=legend, scale=scale, sort=sort,
                                          timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class StrokeWidthDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionDatumDefnumber):
    """StrokeWidthDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeWidth"

    def bandPosition(self, _: float, **kwds) -> 'StrokeWidthDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeWidthDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeWidthDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'StrokeWidthDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'StrokeWidthDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'StrokeWidthDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'StrokeWidthDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'StrokeWidthDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(StrokeWidthDatum, self).__init__(datum=datum, bandPosition=bandPosition,
                                               condition=condition, title=title, type=type, **kwds)


@with_property_setters
class StrokeWidthValue(ValueChannelMixin, core.ValueDefWithConditionMarkPropFieldOrDatumDefnumber):
    """StrokeWidthValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefnumberExprRef`, List(:class:`ConditionalValueDefnumberExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(float, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "strokeWidth"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeWidthValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeWidthValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeWidthValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'StrokeWidthValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'StrokeWidthValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'StrokeWidthValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefnumberExprRef], **kwds) -> 'StrokeWidthValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(StrokeWidthValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Text(FieldChannelMixin, core.FieldOrDatumDefWithConditionStringFieldDefText):
    """Text schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefTextExprRef`, List(:class:`ConditionalValueDefTextExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    format : anyOf(string, :class:`Dict`)
        When used with the default ``"number"`` and ``"time"`` format type, the text
        formatting pattern for labels of guides (axes, legends, headers) and text marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        When used with a `custom formatType
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__, this
        value will be passed as ``format`` alongside ``datum.value`` to the registered
        function.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : string
        The format type for labels. One of ``"number"``, ``"time"``, or a `registered custom
        format type
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__.

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nominal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nominal fields without
          ``timeUnit``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "text"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Text':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefTextExprRef], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: str, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: dict, **kwds) -> 'Text':
        ...

    def formatType(self, _: str, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Text':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Text':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Text':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, format=Undefined, formatType=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Text, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                   bin=bin, condition=condition, field=field, format=format,
                                   formatType=formatType, timeUnit=timeUnit, title=title, type=type,
                                   **kwds)


@with_property_setters
class TextDatum(DatumChannelMixin, core.FieldOrDatumDefWithConditionStringDatumDefText):
    """TextDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    condition : anyOf(:class:`ConditionalValueDefTextExprRef`, List(:class:`ConditionalValueDefTextExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    format : anyOf(string, :class:`Dict`)
        When used with the default ``"number"`` and ``"time"`` format type, the text
        formatting pattern for labels of guides (axes, legends, headers) and text marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        When used with a `custom formatType
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__, this
        value will be passed as ``format`` alongside ``datum.value`` to the registered
        function.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : string
        The format type for labels. One of ``"number"``, ``"time"``, or a `registered custom
        format type
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__.

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nominal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nominal fields without
          ``timeUnit``.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "text"

    def bandPosition(self, _: float, **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefTextExprRef], **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: str, **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: dict, **kwds) -> 'TextDatum':
        ...

    def formatType(self, _: str, **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'TextDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'TextDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'TextDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, condition=Undefined, format=Undefined,
                 formatType=Undefined, title=Undefined, type=Undefined, **kwds):
        super(TextDatum, self).__init__(datum=datum, bandPosition=bandPosition, condition=condition,
                                        format=format, formatType=formatType, title=title, type=type,
                                        **kwds)


@with_property_setters
class TextValue(ValueChannelMixin, core.ValueDefWithConditionStringFieldDefText):
    """TextValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalStringFieldDef`, :class:`ConditionalValueDefTextExprRef`, List(:class:`ConditionalValueDefTextExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(:class:`Text`, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "text"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, format=Undefined, formatType=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'TextValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, format=Undefined, formatType=Undefined, param=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'TextValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'TextValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'TextValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefTextExprRef], **kwds) -> 'TextValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(TextValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Theta(FieldChannelMixin, core.PositionFieldDefBase):
    """Theta schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "theta"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Theta':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Theta':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Theta':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Theta':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, stack=Undefined, timeUnit=Undefined,
                 title=Undefined, type=Undefined, **kwds):
        super(Theta, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                    bin=bin, field=field, scale=scale, sort=sort, stack=stack,
                                    timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class ThetaDatum(DatumChannelMixin, core.PositionDatumDefBase):
    """ThetaDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "theta"

    def bandPosition(self, _: float, **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'ThetaDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'ThetaDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'ThetaDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, scale=Undefined, stack=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(ThetaDatum, self).__init__(datum=datum, bandPosition=bandPosition, scale=scale,
                                         stack=stack, title=title, type=type, **kwds)


@with_property_setters
class ThetaValue(ValueChannelMixin, core.PositionValueDef):
    """ThetaValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "theta"

    

    def __init__(self, value, **kwds):
        super(ThetaValue, self).__init__(value=value, **kwds)


@with_property_setters
class Theta2(FieldChannelMixin, core.SecondaryFieldDef):
    """Theta2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "theta2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Theta2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Theta2':
        ...

    def bin(self, _: None, **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Theta2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Theta2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(Theta2, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                     bandPosition=bandPosition, bin=bin, field=field, timeUnit=timeUnit,
                                     title=title, **kwds)


@with_property_setters
class Theta2Datum(DatumChannelMixin, core.DatumDef):
    """Theta2Datum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "theta2"

    def bandPosition(self, _: float, **kwds) -> 'Theta2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Theta2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Theta2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Theta2Datum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'Theta2Datum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Theta2Datum, self).__init__(datum=datum, bandPosition=bandPosition, title=title,
                                          type=type, **kwds)


@with_property_setters
class Theta2Value(ValueChannelMixin, core.PositionValueDef):
    """Theta2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "theta2"

    

    def __init__(self, value, **kwds):
        super(Theta2Value, self).__init__(value=value, **kwds)


@with_property_setters
class Tooltip(FieldChannelMixin, core.StringFieldDefWithCondition):
    """Tooltip schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstringExprRef`, List(:class:`ConditionalValueDefstringExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    format : anyOf(string, :class:`Dict`)
        When used with the default ``"number"`` and ``"time"`` format type, the text
        formatting pattern for labels of guides (axes, legends, headers) and text marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        When used with a `custom formatType
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__, this
        value will be passed as ``format`` alongside ``datum.value`` to the registered
        function.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : string
        The format type for labels. One of ``"number"``, ``"time"``, or a `registered custom
        format type
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__.

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nominal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nominal fields without
          ``timeUnit``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "tooltip"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Tooltip':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringExprRef], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: str, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: dict, **kwds) -> 'Tooltip':
        ...

    def formatType(self, _: str, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Tooltip':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Tooltip':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Tooltip':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, format=Undefined, formatType=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Tooltip, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, condition=condition,
                                      field=field, format=format, formatType=formatType,
                                      timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class TooltipValue(ValueChannelMixin, core.StringValueDefWithCondition):
    """TooltipValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "tooltip"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'TooltipValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'TooltipValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'TooltipValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'TooltipValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'TooltipValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'TooltipValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'TooltipValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(TooltipValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class Url(FieldChannelMixin, core.StringFieldDefWithCondition):
    """Url schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    condition : anyOf(:class:`ConditionalValueDefstringExprRef`, List(:class:`ConditionalValueDefstringExprRef`))
        One or more value definition(s) with `a parameter or a test predicate
        <https://vega.github.io/vega-lite/docs/condition.html>`__.

        **Note:** A field definition's ``condition`` property can only contain `conditional
        value definitions <https://vega.github.io/vega-lite/docs/condition.html#value>`__
        since Vega-Lite only allows at most one encoded field per encoding channel.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    format : anyOf(string, :class:`Dict`)
        When used with the default ``"number"`` and ``"time"`` format type, the text
        formatting pattern for labels of guides (axes, legends, headers) and text marks.


        * If the format type is ``"number"`` (e.g., for quantitative fields), this is D3's
          `number format pattern <https://github.com/d3/d3-format#locale_format>`__.
        * If the format type is ``"time"`` (e.g., for temporal fields), this is D3's `time
          format pattern <https://github.com/d3/d3-time-format#locale_format>`__.

        See the `format documentation <https://vega.github.io/vega-lite/docs/format.html>`__
        for more examples.

        When used with a `custom formatType
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__, this
        value will be passed as ``format`` alongside ``datum.value`` to the registered
        function.

        **Default value:**  Derived from `numberFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for number
        format and from `timeFormat
        <https://vega.github.io/vega-lite/docs/config.html#format>`__ config for time
        format.
    formatType : string
        The format type for labels. One of ``"number"``, ``"time"``, or a `registered custom
        format type
        <https://vega.github.io/vega-lite/docs/config.html#custom-format-type>`__.

        **Default value:**


        * ``"time"`` for temporal fields and ordinal and nominal fields with ``timeUnit``.
        * ``"number"`` for quantitative fields as well as ordinal and nominal fields without
          ``timeUnit``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "url"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Url':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringExprRef], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: str, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def format(self, _: dict, **kwds) -> 'Url':
        ...

    def formatType(self, _: str, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Url':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Url':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Url':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 condition=Undefined, field=Undefined, format=Undefined, formatType=Undefined,
                 timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Url, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                  bin=bin, condition=condition, field=field, format=format,
                                  formatType=formatType, timeUnit=timeUnit, title=title, type=type,
                                  **kwds)


@with_property_setters
class UrlValue(ValueChannelMixin, core.StringValueDefWithCondition):
    """UrlValue schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    condition : anyOf(:class:`ConditionalMarkPropFieldOrDatumDef`, :class:`ConditionalValueDefstringnullExprRef`, List(:class:`ConditionalValueDefstringnullExprRef`))
        A field definition or one or more value definition(s) with a parameter predicate.
    value : anyOf(string, None, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "url"

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, field=Undefined, legend=Undefined, scale=Undefined, sort=Undefined, test=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'UrlValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, legend=Undefined, scale=Undefined, test=Undefined, title=Undefined, type=Undefined, **kwds) -> 'UrlValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, aggregate=Undefined, bandPosition=Undefined, bin=Undefined, empty=Undefined, field=Undefined, legend=Undefined, param=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds) -> 'UrlValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, bandPosition=Undefined, datum=Undefined, empty=Undefined, legend=Undefined, param=Undefined, scale=Undefined, title=Undefined, type=Undefined, **kwds) -> 'UrlValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, test=Undefined, value=Undefined, **kwds) -> 'UrlValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, empty=Undefined, param=Undefined, value=Undefined, **kwds) -> 'UrlValue':
        ...

    @overload  # type: ignore[no-overload-impl]
    def condition(self, _: List[core.ConditionalValueDefstringnullExprRef], **kwds) -> 'UrlValue':
        ...


    def __init__(self, value, condition=Undefined, **kwds):
        super(UrlValue, self).__init__(value=value, condition=condition, **kwds)


@with_property_setters
class X(FieldChannelMixin, core.PositionFieldDef):
    """X schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels. If ``null``,
        the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.

        **See also:** `axis <https://vega.github.io/vega-lite/docs/axis.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    impute : anyOf(:class:`ImputeParams`, None)
        An object defining the properties of the Impute Operation to be applied. The field
        value of the other positional channel is taken as ``key`` of the ``Impute``
        Operation. The field of the ``color`` channel if specified is used as ``groupby`` of
        the ``Impute`` Operation.

        **See also:** `impute <https://vega.github.io/vega-lite/docs/impute.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "x"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def axis(self, aria=Undefined, bandPosition=Undefined, description=Undefined, domain=Undefined, domainCap=Undefined, domainColor=Undefined, domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined, domainWidth=Undefined, format=Undefined, formatType=Undefined, grid=Undefined, gridCap=Undefined, gridColor=Undefined, gridDash=Undefined, gridDashOffset=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, style=Undefined, tickBand=Undefined, tickCap=Undefined, tickColor=Undefined, tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined, tickExtra=Undefined, tickMinStep=Undefined, tickOffset=Undefined, tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, translate=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def axis(self, _: None, **kwds) -> 'X':
        ...

    def bandPosition(self, _: float, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, frame=Undefined, keyvals=Undefined, method=Undefined, value=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, _: None, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'X':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'X':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'X':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bandPosition=Undefined,
                 bin=Undefined, field=Undefined, impute=Undefined, scale=Undefined, sort=Undefined,
                 stack=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(X, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis,
                                bandPosition=bandPosition, bin=bin, field=field, impute=impute,
                                scale=scale, sort=sort, stack=stack, timeUnit=timeUnit, title=title,
                                type=type, **kwds)


@with_property_setters
class XDatum(DatumChannelMixin, core.PositionDatumDef):
    """XDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels. If ``null``,
        the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.

        **See also:** `axis <https://vega.github.io/vega-lite/docs/axis.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    impute : anyOf(:class:`ImputeParams`, None)
        An object defining the properties of the Impute Operation to be applied. The field
        value of the other positional channel is taken as ``key`` of the ``Impute``
        Operation. The field of the ``color`` channel if specified is used as ``groupby`` of
        the ``Impute`` Operation.

        **See also:** `impute <https://vega.github.io/vega-lite/docs/impute.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "x"

    @overload  # type: ignore[no-overload-impl]
    def axis(self, aria=Undefined, bandPosition=Undefined, description=Undefined, domain=Undefined, domainCap=Undefined, domainColor=Undefined, domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined, domainWidth=Undefined, format=Undefined, formatType=Undefined, grid=Undefined, gridCap=Undefined, gridColor=Undefined, gridDash=Undefined, gridDashOffset=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, style=Undefined, tickBand=Undefined, tickCap=Undefined, tickColor=Undefined, tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined, tickExtra=Undefined, tickMinStep=Undefined, tickOffset=Undefined, tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, translate=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def axis(self, _: None, **kwds) -> 'XDatum':
        ...

    def bandPosition(self, _: float, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, frame=Undefined, keyvals=Undefined, method=Undefined, value=Undefined, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, _: None, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'XDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'XDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'XDatum':
        ...


    def __init__(self, datum, axis=Undefined, bandPosition=Undefined, impute=Undefined, scale=Undefined,
                 stack=Undefined, title=Undefined, type=Undefined, **kwds):
        super(XDatum, self).__init__(datum=datum, axis=axis, bandPosition=bandPosition, impute=impute,
                                     scale=scale, stack=stack, title=title, type=type, **kwds)


@with_property_setters
class XValue(ValueChannelMixin, core.PositionValueDef):
    """XValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "x"

    

    def __init__(self, value, **kwds):
        super(XValue, self).__init__(value=value, **kwds)


@with_property_setters
class X2(FieldChannelMixin, core.SecondaryFieldDef):
    """X2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "x2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'X2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'X2':
        ...

    def bin(self, _: None, **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'X2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'X2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(X2, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                 bin=bin, field=field, timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class X2Datum(DatumChannelMixin, core.DatumDef):
    """X2Datum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "x2"

    def bandPosition(self, _: float, **kwds) -> 'X2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'X2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'X2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'X2Datum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'X2Datum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(X2Datum, self).__init__(datum=datum, bandPosition=bandPosition, title=title, type=type,
                                      **kwds)


@with_property_setters
class X2Value(ValueChannelMixin, core.PositionValueDef):
    """X2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "x2"

    

    def __init__(self, value, **kwds):
        super(X2Value, self).__init__(value=value, **kwds)


@with_property_setters
class XError(FieldChannelMixin, core.SecondaryFieldDef):
    """XError schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xError"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'XError':
        ...

    def bandPosition(self, _: float, **kwds) -> 'XError':
        ...

    def bin(self, _: None, **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'XError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'XError':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(XError, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                     bandPosition=bandPosition, bin=bin, field=field, timeUnit=timeUnit,
                                     title=title, **kwds)


@with_property_setters
class XErrorValue(ValueChannelMixin, core.ValueDefnumber):
    """XErrorValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xError"

    

    def __init__(self, value, **kwds):
        super(XErrorValue, self).__init__(value=value, **kwds)


@with_property_setters
class XError2(FieldChannelMixin, core.SecondaryFieldDef):
    """XError2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xError2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'XError2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'XError2':
        ...

    def bin(self, _: None, **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'XError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'XError2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(XError2, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, field=field,
                                      timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class XError2Value(ValueChannelMixin, core.ValueDefnumber):
    """XError2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xError2"

    

    def __init__(self, value, **kwds):
        super(XError2Value, self).__init__(value=value, **kwds)


@with_property_setters
class XOffset(FieldChannelMixin, core.ScaleFieldDef):
    """XOffset schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xOffset"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'XOffset':
        ...

    def bandPosition(self, _: float, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'XOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'XOffset':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'XOffset':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(XOffset, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, field=field, scale=scale,
                                      sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class XOffsetDatum(DatumChannelMixin, core.ScaleDatumDef):
    """XOffsetDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xOffset"

    def bandPosition(self, _: float, **kwds) -> 'XOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'XOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'XOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'XOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'XOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'XOffsetDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'XOffsetDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, scale=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(XOffsetDatum, self).__init__(datum=datum, bandPosition=bandPosition, scale=scale,
                                           title=title, type=type, **kwds)


@with_property_setters
class XOffsetValue(ValueChannelMixin, core.ValueDefnumber):
    """XOffsetValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "xOffset"

    

    def __init__(self, value, **kwds):
        super(XOffsetValue, self).__init__(value=value, **kwds)


@with_property_setters
class Y(FieldChannelMixin, core.PositionFieldDef):
    """Y schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels. If ``null``,
        the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.

        **See also:** `axis <https://vega.github.io/vega-lite/docs/axis.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, string, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    impute : anyOf(:class:`ImputeParams`, None)
        An object defining the properties of the Impute Operation to be applied. The field
        value of the other positional channel is taken as ``key`` of the ``Impute``
        Operation. The field of the ``color`` channel if specified is used as ``groupby`` of
        the ``Impute`` Operation.

        **See also:** `impute <https://vega.github.io/vega-lite/docs/impute.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "y"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def axis(self, aria=Undefined, bandPosition=Undefined, description=Undefined, domain=Undefined, domainCap=Undefined, domainColor=Undefined, domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined, domainWidth=Undefined, format=Undefined, formatType=Undefined, grid=Undefined, gridCap=Undefined, gridColor=Undefined, gridDash=Undefined, gridDashOffset=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, style=Undefined, tickBand=Undefined, tickCap=Undefined, tickColor=Undefined, tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined, tickExtra=Undefined, tickMinStep=Undefined, tickOffset=Undefined, tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, translate=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def axis(self, _: None, **kwds) -> 'Y':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: str, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, frame=Undefined, keyvals=Undefined, method=Undefined, value=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, _: None, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Y':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Y':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'Y':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, axis=Undefined, bandPosition=Undefined,
                 bin=Undefined, field=Undefined, impute=Undefined, scale=Undefined, sort=Undefined,
                 stack=Undefined, timeUnit=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Y, self).__init__(shorthand=shorthand, aggregate=aggregate, axis=axis,
                                bandPosition=bandPosition, bin=bin, field=field, impute=impute,
                                scale=scale, sort=sort, stack=stack, timeUnit=timeUnit, title=title,
                                type=type, **kwds)


@with_property_setters
class YDatum(DatumChannelMixin, core.PositionDatumDef):
    """YDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    axis : anyOf(:class:`Axis`, None)
        An object defining properties of axis's gridlines, ticks and labels. If ``null``,
        the axis for the encoding channel will be removed.

        **Default value:** If undefined, default `axis properties
        <https://vega.github.io/vega-lite/docs/axis.html>`__ are applied.

        **See also:** `axis <https://vega.github.io/vega-lite/docs/axis.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    impute : anyOf(:class:`ImputeParams`, None)
        An object defining the properties of the Impute Operation to be applied. The field
        value of the other positional channel is taken as ``key`` of the ``Impute``
        Operation. The field of the ``color`` channel if specified is used as ``groupby`` of
        the ``Impute`` Operation.

        **See also:** `impute <https://vega.github.io/vega-lite/docs/impute.html>`__
        documentation.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    stack : anyOf(:class:`StackOffset`, None, boolean)
        Type of stacking offset if the field should be stacked. ``stack`` is only applicable
        for ``x``, ``y``, ``theta``, and ``radius`` channels with continuous domains. For
        example, ``stack`` of ``y`` can be used to customize stacking for a vertical bar
        chart.

        ``stack`` can be one of the following values:


        * ``"zero"`` or `true`: stacking with baseline offset at zero value of the scale
          (for creating typical stacked
          [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and `area
          <https://vega.github.io/vega-lite/docs/stack.html#area>`__ chart).
        * ``"normalize"`` - stacking with normalized domain (for creating `normalized
          stacked bar and area charts
          <https://vega.github.io/vega-lite/docs/stack.html#normalized>`__ and pie charts
          `with percentage tooltip
          <https://vega.github.io/vega-lite/docs/arc.html#tooltip>`__ ). :raw-html:`<br/>`
        * ``"center"`` - stacking with center baseline (for `streamgraph
          <https://vega.github.io/vega-lite/docs/stack.html#streamgraph>`__ ).
        * ``null`` or ``false`` - No-stacking. This will produce layered `bar
          <https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart>`__ and area
          chart.

        **Default value:** ``zero`` for plots with all of the following conditions are true:
        (1) the mark is ``bar``, ``area``, or ``arc`` ; (2) the stacked measure channel (x
        or y) has a linear scale; (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y. Otherwise, ``null`` by default.

        **See also:** `stack <https://vega.github.io/vega-lite/docs/stack.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "y"

    @overload  # type: ignore[no-overload-impl]
    def axis(self, aria=Undefined, bandPosition=Undefined, description=Undefined, domain=Undefined, domainCap=Undefined, domainColor=Undefined, domainDash=Undefined, domainDashOffset=Undefined, domainOpacity=Undefined, domainWidth=Undefined, format=Undefined, formatType=Undefined, grid=Undefined, gridCap=Undefined, gridColor=Undefined, gridDash=Undefined, gridDashOffset=Undefined, gridOpacity=Undefined, gridWidth=Undefined, labelAlign=Undefined, labelAngle=Undefined, labelBaseline=Undefined, labelBound=Undefined, labelColor=Undefined, labelExpr=Undefined, labelFlush=Undefined, labelFlushOffset=Undefined, labelFont=Undefined, labelFontSize=Undefined, labelFontStyle=Undefined, labelFontWeight=Undefined, labelLimit=Undefined, labelLineHeight=Undefined, labelOffset=Undefined, labelOpacity=Undefined, labelOverlap=Undefined, labelPadding=Undefined, labelSeparation=Undefined, labels=Undefined, maxExtent=Undefined, minExtent=Undefined, offset=Undefined, orient=Undefined, position=Undefined, style=Undefined, tickBand=Undefined, tickCap=Undefined, tickColor=Undefined, tickCount=Undefined, tickDash=Undefined, tickDashOffset=Undefined, tickExtra=Undefined, tickMinStep=Undefined, tickOffset=Undefined, tickOpacity=Undefined, tickRound=Undefined, tickSize=Undefined, tickWidth=Undefined, ticks=Undefined, title=Undefined, titleAlign=Undefined, titleAnchor=Undefined, titleAngle=Undefined, titleBaseline=Undefined, titleColor=Undefined, titleFont=Undefined, titleFontSize=Undefined, titleFontStyle=Undefined, titleFontWeight=Undefined, titleLimit=Undefined, titleLineHeight=Undefined, titleOpacity=Undefined, titlePadding=Undefined, titleX=Undefined, titleY=Undefined, translate=Undefined, values=Undefined, zindex=Undefined, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def axis(self, _: None, **kwds) -> 'YDatum':
        ...

    def bandPosition(self, _: float, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, frame=Undefined, keyvals=Undefined, method=Undefined, value=Undefined, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def impute(self, _: None, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: Literal["zero", "center", "normalize"], **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: None, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def stack(self, _: bool, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'YDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'YDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'YDatum':
        ...


    def __init__(self, datum, axis=Undefined, bandPosition=Undefined, impute=Undefined, scale=Undefined,
                 stack=Undefined, title=Undefined, type=Undefined, **kwds):
        super(YDatum, self).__init__(datum=datum, axis=axis, bandPosition=bandPosition, impute=impute,
                                     scale=scale, stack=stack, title=title, type=type, **kwds)


@with_property_setters
class YValue(ValueChannelMixin, core.PositionValueDef):
    """YValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "y"

    

    def __init__(self, value, **kwds):
        super(YValue, self).__init__(value=value, **kwds)


@with_property_setters
class Y2(FieldChannelMixin, core.SecondaryFieldDef):
    """Y2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "y2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'Y2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'Y2':
        ...

    def bin(self, _: None, **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Y2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Y2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(Y2, self).__init__(shorthand=shorthand, aggregate=aggregate, bandPosition=bandPosition,
                                 bin=bin, field=field, timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class Y2Datum(DatumChannelMixin, core.DatumDef):
    """Y2Datum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "y2"

    def bandPosition(self, _: float, **kwds) -> 'Y2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'Y2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'Y2Datum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'Y2Datum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'Y2Datum':
        ...


    def __init__(self, datum, bandPosition=Undefined, title=Undefined, type=Undefined, **kwds):
        super(Y2Datum, self).__init__(datum=datum, bandPosition=bandPosition, title=title, type=type,
                                      **kwds)


@with_property_setters
class Y2Value(ValueChannelMixin, core.PositionValueDef):
    """Y2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : anyOf(float, string, string, :class:`ExprRef`)
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "y2"

    

    def __init__(self, value, **kwds):
        super(Y2Value, self).__init__(value=value, **kwds)


@with_property_setters
class YError(FieldChannelMixin, core.SecondaryFieldDef):
    """YError schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yError"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'YError':
        ...

    def bandPosition(self, _: float, **kwds) -> 'YError':
        ...

    def bin(self, _: None, **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'YError':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'YError':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(YError, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                     bandPosition=bandPosition, bin=bin, field=field, timeUnit=timeUnit,
                                     title=title, **kwds)


@with_property_setters
class YErrorValue(ValueChannelMixin, core.ValueDefnumber):
    """YErrorValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yError"

    

    def __init__(self, value, **kwds):
        super(YErrorValue, self).__init__(value=value, **kwds)


@with_property_setters
class YError2(FieldChannelMixin, core.SecondaryFieldDef):
    """YError2 schema wrapper

    Mapping(required=[shorthand])
    A field definition of a secondary channel that shares a scale with another primary channel.
    For example, ``x2``, ``xError`` and ``xError2`` share the same scale with ``x``.

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : None
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yError2"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'YError2':
        ...

    def bandPosition(self, _: float, **kwds) -> 'YError2':
        ...

    def bin(self, _: None, **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'YError2':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'YError2':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, timeUnit=Undefined, title=Undefined, **kwds):
        super(YError2, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, field=field,
                                      timeUnit=timeUnit, title=title, **kwds)


@with_property_setters
class YError2Value(ValueChannelMixin, core.ValueDefnumber):
    """YError2Value schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yError2"

    

    def __init__(self, value, **kwds):
        super(YError2Value, self).__init__(value=value, **kwds)


@with_property_setters
class YOffset(FieldChannelMixin, core.ScaleFieldDef):
    """YOffset schema wrapper

    Mapping(required=[shorthand])

    Parameters
    ----------

    shorthand : string
        shorthand for field, aggregate, and type
    aggregate : :class:`Aggregate`
        Aggregation function for the field (e.g., ``"mean"``, ``"sum"``, ``"median"``,
        ``"min"``, ``"max"``, ``"count"`` ).

        **Default value:** ``undefined`` (None)

        **See also:** `aggregate <https://vega.github.io/vega-lite/docs/aggregate.html>`__
        documentation.
    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    bin : anyOf(boolean, :class:`BinParams`, None)
        A flag for binning a ``quantitative`` field, `an object defining binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__, or indicating
        that the data for ``x`` or ``y`` channel are binned before they are imported into
        Vega-Lite ( ``"binned"`` ).


        If ``true``, default `binning parameters
        <https://vega.github.io/vega-lite/docs/bin.html#bin-parameters>`__ will be applied.

        If ``"binned"``, this indicates that the data for the ``x`` (or ``y`` ) channel are
        already binned. You can map the bin-start field to ``x`` (or ``y`` ) and the bin-end
        field to ``x2`` (or ``y2`` ). The scale and axis will be formatted similar to
        binning in Vega-Lite.  To adjust the axis ticks based on the bin step, you can also
        set the axis's `tickMinStep
        <https://vega.github.io/vega-lite/docs/axis.html#ticks>`__ property.

        **Default value:** ``false``

        **See also:** `bin <https://vega.github.io/vega-lite/docs/bin.html>`__
        documentation.
    field : :class:`Field`
        **Required.** A string defining the name of the field from which to pull a data
        value or an object defining iterated values from the `repeat
        <https://vega.github.io/vega-lite/docs/repeat.html>`__ operator.

        **See also:** `field <https://vega.github.io/vega-lite/docs/field.html>`__
        documentation.

        **Notes:** 1)  Dots ( ``.`` ) and brackets ( ``[`` and ``]`` ) can be used to access
        nested objects (e.g., ``"field": "foo.bar"`` and ``"field": "foo['bar']"`` ). If
        field names contain dots or brackets but are not nested, you can use ``\\`` to
        escape dots and brackets (e.g., ``"a\\.b"`` and ``"a\\[0\\]"`` ). See more details
        about escaping in the `field documentation
        <https://vega.github.io/vega-lite/docs/field.html>`__. 2) ``field`` is not required
        if ``aggregate`` is ``count``.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    sort : :class:`Sort`
        Sort order for the encoded field.

        For continuous fields (quantitative or temporal), ``sort`` can be either
        ``"ascending"`` or ``"descending"``.

        For discrete fields, ``sort`` can be one of the following:


        * ``"ascending"`` or ``"descending"`` -- for sorting by the values' natural order in
          JavaScript.
        * `A string indicating an encoding channel name to sort by
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__ (e.g.,
          ``"x"`` or ``"y"`` ) with an optional minus prefix for descending sort (e.g.,
          ``"-x"`` to sort by x-field, descending). This channel string is short-form of `a
          sort-by-encoding definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-by-encoding>`__. For
          example, ``"sort": "-x"`` is equivalent to ``"sort": {"encoding": "x", "order":
          "descending"}``.
        * `A sort field definition
          <https://vega.github.io/vega-lite/docs/sort.html#sort-field>`__ for sorting by
          another field.
        * `An array specifying the field values in preferred order
          <https://vega.github.io/vega-lite/docs/sort.html#sort-array>`__. In this case, the
          sort order will obey the values in the array, followed by any unspecified values
          in their original order. For discrete time field, values in the sort array can be
          `date-time definition objects
          <https://vega.github.io/vega-lite/docs/datetime.html>`__. In addition, for time
          units ``"month"`` and ``"day"``, the values can be the month or day names (case
          insensitive) or their 3-letter initials (e.g., ``"Mon"``, ``"Tue"`` ).
        * ``null`` indicating no sort.

        **Default value:** ``"ascending"``

        **Note:** ``null`` and sorting by another channel is not supported for ``row`` and
        ``column``.

        **See also:** `sort <https://vega.github.io/vega-lite/docs/sort.html>`__
        documentation.
    timeUnit : anyOf(:class:`TimeUnit`, :class:`TimeUnitParams`)
        Time unit (e.g., ``year``, ``yearmonth``, ``month``, ``hours`` ) for a temporal
        field. or `a temporal field that gets casted as ordinal
        <https://vega.github.io/vega-lite/docs/type.html#cast>`__.

        **Default value:** ``undefined`` (None)

        **See also:** `timeUnit <https://vega.github.io/vega-lite/docs/timeunit.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`StandardType`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yOffset"

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, _: Literal["average", "count", "distinct", "max", "mean", "median", "min", "missing", "product", "q1", "q3", "ci0", "ci1", "stderr", "stdev", "stdevp", "sum", "valid", "values", "variance", "variancep"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmax=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def aggregate(self, argmin=Undefined, **kwds) -> 'YOffset':
        ...

    def bandPosition(self, _: float, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: bool, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, anchor=Undefined, base=Undefined, binned=Undefined, divide=Undefined, extent=Undefined, maxbins=Undefined, minstep=Undefined, nice=Undefined, step=Undefined, steps=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def bin(self, _: None, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, _: str, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def field(self, repeat=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[float], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[str], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[bool], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: List[core.DateTime], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["ascending", "descending"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["x", "y", "color", "fill", "stroke", "strokeWidth", "size", "shape", "fillOpacity", "strokeOpacity", "opacity", "text"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: Literal["-x", "-y", "-color", "-fill", "-stroke", "-strokeWidth", "-size", "-shape", "-fillOpacity", "-strokeOpacity", "-opacity", "-text"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, field=Undefined, op=Undefined, order=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, encoding=Undefined, order=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def sort(self, _: None, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["year", "quarter", "month", "week", "day", "dayofyear", "date", "hours", "minutes", "seconds", "milliseconds"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyear", "utcquarter", "utcmonth", "utcweek", "utcday", "utcdayofyear", "utcdate", "utchours", "utcminutes", "utcseconds", "utcmilliseconds"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["yearquarter", "yearquartermonth", "yearmonth", "yearmonthdate", "yearmonthdatehours", "yearmonthdatehoursminutes", "yearmonthdatehoursminutesseconds", "yearweek", "yearweekday", "yearweekdayhours", "yearweekdayhoursminutes", "yearweekdayhoursminutesseconds", "yeardayofyear", "quartermonth", "monthdate", "monthdatehours", "monthdatehoursminutes", "monthdatehoursminutesseconds", "weekday", "weeksdayhours", "weekdayhoursminutes", "weekdayhoursminutesseconds", "dayhours", "dayhoursminutes", "dayhoursminutesseconds", "hoursminutes", "hoursminutesseconds", "minutesseconds", "secondsmilliseconds"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, _: Literal["utcyearquarter", "utcyearquartermonth", "utcyearmonth", "utcyearmonthdate", "utcyearmonthdatehours", "utcyearmonthdatehoursminutes", "utcyearmonthdatehoursminutesseconds", "utcyearweek", "utcyearweekday", "utcyearweekdayhours", "utcyearweekdayhoursminutes", "utcyearweekdayhoursminutesseconds", "utcyeardayofyear", "utcquartermonth", "utcmonthdate", "utcmonthdatehours", "utcmonthdatehoursminutes", "utcmonthdatehoursminutesseconds", "utcweekday", "utcweeksdayhours", "utcweekdayhoursminutes", "utcweekdayhoursminutesseconds", "utcdayhours", "utcdayhoursminutes", "utcdayhoursminutesseconds", "utchoursminutes", "utchoursminutesseconds", "utcminutesseconds", "utcsecondsmilliseconds"], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def timeUnit(self, maxbins=Undefined, step=Undefined, unit=Undefined, utc=Undefined, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'YOffset':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'YOffset':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal"], **kwds) -> 'YOffset':
        ...


    def __init__(self, shorthand=Undefined, aggregate=Undefined, bandPosition=Undefined, bin=Undefined,
                 field=Undefined, scale=Undefined, sort=Undefined, timeUnit=Undefined, title=Undefined,
                 type=Undefined, **kwds):
        super(YOffset, self).__init__(shorthand=shorthand, aggregate=aggregate,
                                      bandPosition=bandPosition, bin=bin, field=field, scale=scale,
                                      sort=sort, timeUnit=timeUnit, title=title, type=type, **kwds)


@with_property_setters
class YOffsetDatum(DatumChannelMixin, core.ScaleDatumDef):
    """YOffsetDatum schema wrapper

    Mapping(required=[])

    Parameters
    ----------

    bandPosition : float
        Relative position on a band of a stacked, binned, time unit, or band scale. For
        example, the marks will be positioned at the beginning of the band if set to ``0``,
        and at the middle of the band if set to ``0.5``.
    datum : anyOf(:class:`PrimitiveValue`, :class:`DateTime`, :class:`ExprRef`, :class:`RepeatRef`)
        A constant value in data domain.
    scale : anyOf(:class:`Scale`, None)
        An object defining properties of the channel's scale, which is the function that
        transforms values in the data domain (numbers, dates, strings, etc) to visual values
        (pixels, colors, sizes) of the encoding channels.

        If ``null``, the scale will be `disabled and the data value will be directly encoded
        <https://vega.github.io/vega-lite/docs/scale.html#disable>`__.

        **Default value:** If undefined, default `scale properties
        <https://vega.github.io/vega-lite/docs/scale.html>`__ are applied.

        **See also:** `scale <https://vega.github.io/vega-lite/docs/scale.html>`__
        documentation.
    title : anyOf(:class:`Text`, None)
        A title for the field. If ``null``, the title will be removed.

        **Default value:**  derived from the field's name and transformation function (
        ``aggregate``, ``bin`` and ``timeUnit`` ). If the field has an aggregate function,
        the function is displayed as part of the title (e.g., ``"Sum of Profit"`` ). If the
        field is binned or has a time unit applied, the applied function is shown in
        parentheses (e.g., ``"Profit (binned)"``, ``"Transaction Date (year-month)"`` ).
        Otherwise, the title is simply the field name.

        **Notes** :

        1) You can customize the default field title format by providing the `fieldTitle
        <https://vega.github.io/vega-lite/docs/config.html#top-level-config>`__ property in
        the `config <https://vega.github.io/vega-lite/docs/config.html>`__ or `fieldTitle
        function via the compile function's options
        <https://vega.github.io/vega-lite/usage/compile.html#field-title>`__.

        2) If both field definition's ``title`` and axis, header, or legend ``title`` are
        defined, axis/header/legend title will be used.
    type : :class:`Type`
        The type of measurement ( ``"quantitative"``, ``"temporal"``, ``"ordinal"``, or
        ``"nominal"`` ) for the encoded field or constant value ( ``datum`` ). It can also
        be a ``"geojson"`` type for encoding `'geoshape'
        <https://vega.github.io/vega-lite/docs/geoshape.html>`__.

        Vega-Lite automatically infers data types in many cases as discussed below. However,
        type is required for a field if: (1) the field is not nominal and the field encoding
        has no specified ``aggregate`` (except ``argmin`` and ``argmax`` ), ``bin``, scale
        type, custom ``sort`` order, nor ``timeUnit`` or (2) if you wish to use an ordinal
        scale for a field with ``bin`` or ``timeUnit``.

        **Default value:**

        1) For a data ``field``, ``"nominal"`` is the default data type unless the field
        encoding has ``aggregate``, ``channel``, ``bin``, scale type, ``sort``, or
        ``timeUnit`` that satisfies the following criteria:


        * ``"quantitative"`` is the default type if (1) the encoded field contains ``bin``
          or ``aggregate`` except ``"argmin"`` and ``"argmax"``, (2) the encoding channel is
          ``latitude`` or ``longitude`` channel or (3) if the specified scale type is `a
          quantitative scale <https://vega.github.io/vega-lite/docs/scale.html#type>`__.
        * ``"temporal"`` is the default type if (1) the encoded field contains ``timeUnit``
          or (2) the specified scale type is a time or utc scale
        * ``"ordinal"`` is the default type if (1) the encoded field contains a `custom sort
          order
          <https://vega.github.io/vega-lite/docs/sort.html#specifying-custom-sort-order>`__,
          (2) the specified scale type is an ordinal/point/band scale, or (3) the encoding
          channel is ``order``.

        2) For a constant value in data domain ( ``datum`` ):


        * ``"quantitative"`` if the datum is a number
        * ``"nominal"`` if the datum is a string
        * ``"temporal"`` if the datum is `a date time object
          <https://vega.github.io/vega-lite/docs/datetime.html>`__

        **Note:**


        * Data ``type`` describes the semantics of the data rather than the primitive data
          types (number, string, etc.). The same primitive data type can have different
          types of measurement. For example, numeric data can represent quantitative,
          ordinal, or nominal data.
        * Data values for a temporal field can be either a date-time string (e.g.,
          ``"2015-03-07 12:32:17"``, ``"17:01"``, ``"2015-03-16"``. ``"2015"`` ) or a
          timestamp number (e.g., ``1552199579097`` ).
        * When using with `bin <https://vega.github.io/vega-lite/docs/bin.html>`__, the
          ``type`` property can be either ``"quantitative"`` (for using a linear bin scale)
          or `"ordinal" (for using an ordinal bin scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `timeUnit
          <https://vega.github.io/vega-lite/docs/timeunit.html>`__, the ``type`` property
          can be either ``"temporal"`` (default, for using a temporal scale) or `"ordinal"
          (for using an ordinal scale)
          <https://vega.github.io/vega-lite/docs/type.html#cast-bin>`__.
        * When using with `aggregate
          <https://vega.github.io/vega-lite/docs/aggregate.html>`__, the ``type`` property
          refers to the post-aggregation data type. For example, we can calculate count
          ``distinct`` of a categorical field ``"cat"`` using ``{"aggregate": "distinct",
          "field": "cat"}``. The ``"type"`` of the aggregate output is ``"quantitative"``.
        * Secondary channels (e.g., ``x2``, ``y2``, ``xError``, ``yError`` ) do not have
          ``type`` as they must have exactly the same type as their primary channels (e.g.,
          ``x``, ``y`` ).

        **See also:** `type <https://vega.github.io/vega-lite/docs/type.html>`__
        documentation.
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yOffset"

    def bandPosition(self, _: float, **kwds) -> 'YOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, align=Undefined, base=Undefined, bins=Undefined, clamp=Undefined, constant=Undefined, domain=Undefined, domainMax=Undefined, domainMid=Undefined, domainMin=Undefined, exponent=Undefined, interpolate=Undefined, nice=Undefined, padding=Undefined, paddingInner=Undefined, paddingOuter=Undefined, range=Undefined, rangeMax=Undefined, rangeMin=Undefined, reverse=Undefined, round=Undefined, scheme=Undefined, type=Undefined, zero=Undefined, **kwds) -> 'YOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def scale(self, _: None, **kwds) -> 'YOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: str, **kwds) -> 'YOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: List[str], **kwds) -> 'YOffsetDatum':
        ...

    @overload  # type: ignore[no-overload-impl]
    def title(self, _: None, **kwds) -> 'YOffsetDatum':
        ...

    def type(self, _: Literal["quantitative", "ordinal", "temporal", "nominal", "geojson"], **kwds) -> 'YOffsetDatum':
        ...


    def __init__(self, datum, bandPosition=Undefined, scale=Undefined, title=Undefined, type=Undefined,
                 **kwds):
        super(YOffsetDatum, self).__init__(datum=datum, bandPosition=bandPosition, scale=scale,
                                           title=title, type=type, **kwds)


@with_property_setters
class YOffsetValue(ValueChannelMixin, core.ValueDefnumber):
    """YOffsetValue schema wrapper

    Mapping(required=[value])
    Definition object for a constant value (primitive value or gradient definition) of an
    encoding channel.

    Parameters
    ----------

    value : float
        A constant value in visual domain (e.g., ``"red"`` / ``"#0099ff"`` / `gradient
        definition <https://vega.github.io/vega-lite/docs/types.html#gradient>`__ for color,
        values between ``0`` to ``1`` for opacity).
    """
    _class_is_valid_at_instantiation = False
    _encoding_name = "yOffset"

    

    def __init__(self, value, **kwds):
        super(YOffsetValue, self).__init__(value=value, **kwds)
