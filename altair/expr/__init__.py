"""Tools for creating transform & filter expressions with a python syntax."""

from __future__ import annotations

import sys

from altair.expr.core import ConstExpression, FunctionExpression
from altair.vegalite.v5.schema.core import ExprRef as _ExprRef

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class _ConstExpressionType(type):
    """Metaclass providing read-only class properties for :class:`expr`."""

    @property
    def NaN(cls) -> ConstExpression:
        """Not a number (same as JavaScript literal NaN)."""
        return ConstExpression("NaN")

    @property
    def LN10(cls) -> ConstExpression:
        """The natural log of 10 (alias to Math.LN10)."""
        return ConstExpression("LN10")

    @property
    def E(cls) -> ConstExpression:
        """The transcendental number e (alias to Math.E)."""
        return ConstExpression("E")

    @property
    def LOG10E(cls) -> ConstExpression:
        """The base 10 logarithm e (alias to Math.LOG10E)."""
        return ConstExpression("LOG10E")

    @property
    def LOG2E(cls) -> ConstExpression:
        """The base 2 logarithm of e (alias to Math.LOG2E)."""
        return ConstExpression("LOG2E")

    @property
    def SQRT1_2(cls) -> ConstExpression:
        """The square root of 0.5 (alias to Math.SQRT1_2)."""
        return ConstExpression("SQRT1_2")

    @property
    def LN2(cls) -> ConstExpression:
        """The natural log of 2 (alias to Math.LN2)."""
        return ConstExpression("LN2")

    @property
    def SQRT2(cls) -> ConstExpression:
        """The square root of 2 (alias to Math.SQRT1_2)."""
        return ConstExpression("SQRT2")

    @property
    def PI(cls) -> ConstExpression:
        """The transcendental number pi (alias to Math.PI)."""
        return ConstExpression("PI")


class expr(_ExprRef, metaclass=_ConstExpressionType):
    r"""
    Utility providing *constants* and *classmethods* to construct expressions.

    `Expressions`_ can be used to write basic formulas that enable custom interactions.

    Alternatively, an `inline expression`_ may be defined via :class:`expr()`.

    Parameters
    ----------
    expr: str
        A `vega expression`_ string.

    Returns
    -------
    ``ExprRef``

    .. _Expressions:
        https://altair-viz.github.io/user_guide/interactions.html#expressions
    .. _inline expression:
       https://altair-viz.github.io/user_guide/interactions.html#inline-expressions
    .. _vega expression:
       https://vega.github.io/vega/docs/expressions/

    Examples
    --------
    >>> import altair as alt

    >>> bind_range = alt.binding_range(min=100, max=300, name="Slider value:  ")
    >>> param_width = alt.param(bind=bind_range, name="param_width")
    >>> param_color = alt.param(
    ...     expr=alt.expr.if_(param_width < 200, "red", "black"),
    ...     name="param_color",
    ... )
    >>> y = alt.Y("yval").axis(titleColor=param_color)

    >>> y
    Y({
      axis: {'titleColor': Parameter('param_color', VariableParameter({
        expr: if((param_width < 200),'red','black'),
        name: 'param_color'
      }))},
      shorthand: 'yval'
    })
    """

    @override
    def __new__(cls: type[_ExprRef], expr: str) -> _ExprRef:  # type: ignore[misc]
        # NOTE: `mypy<=1.10.1` is not consistent with typing spec
        # https://github.com/python/mypy/issues/1020
        # https://docs.python.org/3/reference/datamodel.html#object.__new__
        # https://typing.readthedocs.io/en/latest/spec/constructors.html#new-method
        return _ExprRef(expr=expr)

    @classmethod
    def if_(cls, *args) -> FunctionExpression:
        """
        If *test* is truthy, returns *thenValue*. Otherwise, returns *elseValue*.

        The *if* function is equivalent to the ternary operator `a ? b : c`.
        """
        return FunctionExpression("if", args)

    @classmethod
    def isArray(cls, *args) -> FunctionExpression:
        """Returns true if *value* is an array, false otherwise."""
        return FunctionExpression("isArray", args)

    @classmethod
    def isBoolean(cls, *args) -> FunctionExpression:
        """Returns true if *value* is a boolean (`true` or `false`), false otherwise."""
        return FunctionExpression("isBoolean", args)

    @classmethod
    def isDate(cls, *args) -> FunctionExpression:
        """
        Returns true if *value* is a Date object, false otherwise.

        This method will return false for timestamp numbers or date-formatted strings; it recognizes Date objects only.
        """
        return FunctionExpression("isDate", args)

    @classmethod
    def isDefined(cls, *args) -> FunctionExpression:
        """
        Returns true if *value* is a defined value, false if *value* equals `undefined`.

        This method will return true for `null` and `NaN` values.
        """
        return FunctionExpression("isDefined", args)

    @classmethod
    def isNumber(cls, *args) -> FunctionExpression:
        """
        Returns true if *value* is a number, false otherwise.

        `NaN` and `Infinity` are considered numbers.
        """
        return FunctionExpression("isNumber", args)

    @classmethod
    def isObject(cls, *args) -> FunctionExpression:
        """Returns true if *value* is an object (including arrays and Dates), false otherwise."""
        return FunctionExpression("isObject", args)

    @classmethod
    def isRegExp(cls, *args) -> FunctionExpression:
        """Returns true if *value* is a RegExp (regular expression) object, false otherwise."""
        return FunctionExpression("isRegExp", args)

    @classmethod
    def isString(cls, *args) -> FunctionExpression:
        """Returns true if *value* is a string, false otherwise."""
        return FunctionExpression("isString", args)

    @classmethod
    def isValid(cls, *args) -> FunctionExpression:
        """Returns true if *value* is not `null`, `undefined`, or `NaN`, false otherwise."""
        return FunctionExpression("isValid", args)

    @classmethod
    def toBoolean(cls, *args) -> FunctionExpression:
        """
        Coerces the input *value* to a string.

        Null values and empty strings are mapped to `null`.
        """
        return FunctionExpression("toBoolean", args)

    @classmethod
    def toDate(cls, *args) -> FunctionExpression:
        """
        Coerces the input *value* to a Date instance.

        Null values and empty strings are mapped to `null`.
        If an optional *parser* function is provided, it is used to perform date parsing, otherwise `Date.parse` is used.
        Be aware that `Date.parse` has different implementations across browsers!
        """
        return FunctionExpression("toDate", args)

    @classmethod
    def toNumber(cls, *args) -> FunctionExpression:
        """
        Coerces the input *value* to a number.

        Null values and empty strings are mapped to `null`.
        """
        return FunctionExpression("toNumber", args)

    @classmethod
    def toString(cls, *args) -> FunctionExpression:
        """
        Coerces the input *value* to a string.

        Null values and empty strings are mapped to `null`.
        """
        return FunctionExpression("toString", args)

    @classmethod
    def isNaN(cls, *args) -> FunctionExpression:
        """
        Returns true if *value* is not a number.

        Same as JavaScript's `isNaN`.
        """
        return FunctionExpression("isNaN", args)

    @classmethod
    def isFinite(cls, *args) -> FunctionExpression:
        """
        Returns true if *value* is a finite number.

        Same as JavaScript's `isFinite`.
        """
        return FunctionExpression("isFinite", args)

    @classmethod
    def abs(cls, *args) -> FunctionExpression:
        """
        Returns the absolute value of *value*.

        Same as JavaScript's `Math.abs`.
        """
        return FunctionExpression("abs", args)

    @classmethod
    def acos(cls, *args) -> FunctionExpression:
        """
        Trigonometric arccosine.

        Same as JavaScript's `Math.acos`.
        """
        return FunctionExpression("acos", args)

    @classmethod
    def asin(cls, *args) -> FunctionExpression:
        """
        Trigonometric arcsine.

        Same as JavaScript's `Math.asin`.
        """
        return FunctionExpression("asin", args)

    @classmethod
    def atan(cls, *args) -> FunctionExpression:
        """
        Trigonometric arctangent.

        Same as JavaScript's `Math.atan`.
        """
        return FunctionExpression("atan", args)

    @classmethod
    def atan2(cls, *args) -> FunctionExpression:
        """
        Returns the arctangent of *dy / dx*.

        Same as JavaScript's `Math.atan2`.
        """
        return FunctionExpression("atan2", args)

    @classmethod
    def ceil(cls, *args) -> FunctionExpression:
        """
        Rounds *value* to the nearest integer of equal or greater value.

        Same as JavaScript's `Math.ceil`.
        """
        return FunctionExpression("ceil", args)

    @classmethod
    def clamp(cls, *args) -> FunctionExpression:
        """Restricts *value* to be between the specified *min* and *max*."""
        return FunctionExpression("clamp", args)

    @classmethod
    def cos(cls, *args) -> FunctionExpression:
        """
        Trigonometric cosine.

        Same as JavaScript's `Math.cos`.
        """
        return FunctionExpression("cos", args)

    @classmethod
    def exp(cls, *args) -> FunctionExpression:
        """
        Returns the value of *e* raised to the provided *exponent*.

        Same as JavaScript's `Math.exp`.
        """
        return FunctionExpression("exp", args)

    @classmethod
    def floor(cls, *args) -> FunctionExpression:
        """
        Rounds *value* to the nearest integer of equal or lower value.

        Same as JavaScript's `Math.floor`.
        """
        return FunctionExpression("floor", args)

    @classmethod
    def hypot(cls, *args) -> FunctionExpression:
        """
        Returns the square root of the sum of squares of its arguments.

        Same as JavaScript's `Math.hypot`.
        """
        return FunctionExpression("hypot", args)

    @classmethod
    def log(cls, *args) -> FunctionExpression:
        """
        Returns the natural logarithm of *value*.

        Same as JavaScript's `Math.log`.
        """
        return FunctionExpression("log", args)

    @classmethod
    def max(cls, *args) -> FunctionExpression:
        """
        Returns the maximum argument value.

        Same as JavaScript's `Math.max`.
        """
        return FunctionExpression("max", args)

    @classmethod
    def min(cls, *args) -> FunctionExpression:
        """
        Returns the minimum argument value.

        Same as JavaScript's `Math.min`.
        """
        return FunctionExpression("min", args)

    @classmethod
    def pow(cls, *args) -> FunctionExpression:
        """
        Returns *value* raised to the given *exponent*.

        Same as JavaScript's `Math.pow`.
        """
        return FunctionExpression("pow", args)

    @classmethod
    def random(cls, *args) -> FunctionExpression:
        """
        Returns a pseudo-random number in the range `[0, 1]`.

        Same as JavaScript's `Math.random`.
        """
        return FunctionExpression("random", args)

    @classmethod
    def round(cls, *args) -> FunctionExpression:
        """
        Rounds *value* to the nearest integer.

        Same as JavaScript's `Math.round`.
        """
        return FunctionExpression("round", args)

    @classmethod
    def sin(cls, *args) -> FunctionExpression:
        """
        Trigonometric sine.

        Same as JavaScript's `Math.sin`.
        """
        return FunctionExpression("sin", args)

    @classmethod
    def sqrt(cls, *args) -> FunctionExpression:
        """
        Square root function.

        Same as JavaScript's `Math.sqrt`.
        """
        return FunctionExpression("sqrt", args)

    @classmethod
    def tan(cls, *args) -> FunctionExpression:
        """
        Trigonometric tangent.

        Same as JavaScript's `Math.tan`.
        """
        return FunctionExpression("tan", args)

    @classmethod
    def sampleNormal(cls, *args) -> FunctionExpression:
        """
        Returns a sample from a univariate `normal (Gaussian) probability distribution <https://en.wikipedia.org/wiki/Normal_distribution>`__ with specified *mean* and standard deviation *stdev*.

        If unspecified, the mean defaults to `0` and the standard deviation defaults to `1`.
        """
        return FunctionExpression("sampleNormal", args)

    @classmethod
    def cumulativeNormal(cls, *args) -> FunctionExpression:
        """
        Returns the value of the `cumulative distribution function <https://en.wikipedia.org/wiki/Cumulative_distribution_function>`__ at the given input domain *value* for a normal distribution with specified *mean* and standard deviation *stdev*.

        If unspecified, the mean defaults to `0` and the standard deviation defaults to `1`.
        """
        return FunctionExpression("cumulativeNormal", args)

    @classmethod
    def densityNormal(cls, *args) -> FunctionExpression:
        """
        Returns the value of the `probability density function <https://en.wikipedia.org/wiki/Probability_density_function>`__ at the given input domain *value*, for a normal distribution with specified *mean* and standard deviation *stdev*.

        If unspecified, the mean defaults to `0` and the standard deviation defaults to `1`.
        """
        return FunctionExpression("densityNormal", args)

    @classmethod
    def quantileNormal(cls, *args) -> FunctionExpression:
        """
        Returns the quantile value (the inverse of the `cumulative distribution function <https://en.wikipedia.org/wiki/Cumulative_distribution_function)>`__ for the given input *probability*, for a normal distribution with specified *mean* and standard deviation *stdev*.

        If unspecified, the mean defaults to `0` and the standard deviation defaults to `1`.
        """
        return FunctionExpression("quantileNormal", args)

    @classmethod
    def sampleLogNormal(cls, *args) -> FunctionExpression:
        """
        Returns a sample from a univariate `log-normal probability distribution <https://en.wikipedia.org/wiki/Log-normal_distribution>`__ with specified log *mean* and log standard deviation *stdev*.

        If unspecified, the log mean defaults to `0` and the log standard deviation defaults to `1`.
        """
        return FunctionExpression("sampleLogNormal", args)

    @classmethod
    def cumulativeLogNormal(cls, *args) -> FunctionExpression:
        """
        Returns the value of the `cumulative distribution function <https://en.wikipedia.org/wiki/Cumulative_distribution_function>`__ at the given input domain *value* for a log-normal distribution with specified log *mean* and log standard deviation *stdev*.

        If unspecified, the log mean defaults to `0` and the log standard deviation defaults to `1`.
        """
        return FunctionExpression("cumulativeLogNormal", args)

    @classmethod
    def densityLogNormal(cls, *args) -> FunctionExpression:
        """
        Returns the value of the `probability density function <https://en.wikipedia.org/wiki/Probability_density_function>`__ at the given input domain *value*, for a log-normal distribution with specified log *mean* and log standard deviation *stdev*.

        If unspecified, the log mean defaults to `0` and the log standard deviation defaults to `1`.
        """
        return FunctionExpression("densityLogNormal", args)

    @classmethod
    def quantileLogNormal(cls, *args) -> FunctionExpression:
        """
        Returns the quantile value (the inverse of the `cumulative distribution function <https://en.wikipedia.org/wiki/Cumulative_distribution_function)>`__ for the given input *probability*, for a log-normal distribution with specified log *mean* and log standard deviation *stdev*.

        If unspecified, the log mean defaults to `0` and the log standard deviation defaults to `1`.
        """
        return FunctionExpression("quantileLogNormal", args)

    @classmethod
    def sampleUniform(cls, *args) -> FunctionExpression:
        """
        Returns a sample from a univariate `continuous uniform probability distribution <https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)>`__ over the interval `[min, max]`.

        If unspecified, *min* defaults to `0` and *max* defaults to `1`.
        If only one argument is provided, it is interpreted as the *max* value.
        """
        return FunctionExpression("sampleUniform", args)

    @classmethod
    def cumulativeUniform(cls, *args) -> FunctionExpression:
        """
        Returns the value of the `cumulative distribution function <https://en.wikipedia.org/wiki/Cumulative_distribution_function>`__ at the given input domain *value* for a uniform distribution over the interval `[min, max]`.

        If unspecified, *min* defaults to `0` and *max* defaults to `1`.
        If only one argument is provided, it is interpreted as the *max* value.
        """
        return FunctionExpression("cumulativeUniform", args)

    @classmethod
    def densityUniform(cls, *args) -> FunctionExpression:
        """
        Returns the value of the `probability density function <https://en.wikipedia.org/wiki/Probability_density_function>`__ at the given input domain *value*,  for a uniform distribution over the interval `[min, max]`.

        If unspecified, *min* defaults to `0` and *max* defaults to `1`.
        If only one argument is provided, it is interpreted as the *max* value.
        """
        return FunctionExpression("densityUniform", args)

    @classmethod
    def quantileUniform(cls, *args) -> FunctionExpression:
        """
        Returns the quantile value (the inverse of the `cumulative distribution function <https://en.wikipedia.org/wiki/Cumulative_distribution_function)>`__ for the given input *probability*, for a uniform distribution over the interval `[min, max]`.

        If unspecified, *min* defaults to `0` and *max* defaults to `1`.
        If only one argument is provided, it is interpreted as the *max* value.
        """
        return FunctionExpression("quantileUniform", args)

    @classmethod
    def now(cls, *args) -> FunctionExpression:
        """Returns the timestamp for the current time."""
        return FunctionExpression("now", args)

    @classmethod
    def datetime(cls, *args) -> FunctionExpression:
        """
        Returns a new `Date` instance.

        The *month* is 0-based, such that `1` represents February.
        """
        return FunctionExpression("datetime", args)

    @classmethod
    def date(cls, *args) -> FunctionExpression:
        """Returns the day of the month for the given *datetime* value, in local time."""
        return FunctionExpression("date", args)

    @classmethod
    def day(cls, *args) -> FunctionExpression:
        """Returns the day of the week for the given *datetime* value, in local time."""
        return FunctionExpression("day", args)

    @classmethod
    def dayofyear(cls, *args) -> FunctionExpression:
        """Returns the one-based day of the year for the given *datetime* value, in local time."""
        return FunctionExpression("dayofyear", args)

    @classmethod
    def year(cls, *args) -> FunctionExpression:
        """Returns the year for the given *datetime* value, in local time."""
        return FunctionExpression("year", args)

    @classmethod
    def quarter(cls, *args) -> FunctionExpression:
        """Returns the quarter of the year (0-3) for the given *datetime* value, in local time."""
        return FunctionExpression("quarter", args)

    @classmethod
    def month(cls, *args) -> FunctionExpression:
        """Returns the (zero-based) month for the given *datetime* value, in local time."""
        return FunctionExpression("month", args)

    @classmethod
    def week(cls, *args) -> FunctionExpression:
        """
        Returns the week number of the year for the given *datetime*, in local time.

        This function assumes Sunday-based weeks.
        Days before the first Sunday of the year are considered to be in week 0,
        the first Sunday of the year is the start of week 1,
        the second Sunday week 2, etc.
        """
        return FunctionExpression("week", args)

    @classmethod
    def hours(cls, *args) -> FunctionExpression:
        """Returns the hours component for the given *datetime* value, in local time."""
        return FunctionExpression("hours", args)

    @classmethod
    def minutes(cls, *args) -> FunctionExpression:
        """Returns the minutes component for the given *datetime* value, in local time."""
        return FunctionExpression("minutes", args)

    @classmethod
    def seconds(cls, *args) -> FunctionExpression:
        """Returns the seconds component for the given *datetime* value, in local time."""
        return FunctionExpression("seconds", args)

    @classmethod
    def milliseconds(cls, *args) -> FunctionExpression:
        """Returns the milliseconds component for the given *datetime* value, in local time."""
        return FunctionExpression("milliseconds", args)

    @classmethod
    def time(cls, *args) -> FunctionExpression:
        """Returns the epoch-based timestamp for the given *datetime* value."""
        return FunctionExpression("time", args)

    @classmethod
    def timezoneoffset(cls, *args) -> FunctionExpression:
        """Returns the timezone offset from the local timezone to UTC for the given *datetime* value."""
        return FunctionExpression("timezoneoffset", args)

    @classmethod
    def timeOffset(cls, *args) -> FunctionExpression:
        """
        Returns a new `Date` instance that offsets the given *date* by the specified time `unit <https://vega.github.io/vega/docs/api/time/#time-units>`__ in the local timezone.

        The optional *step* argument indicates the number of time unit steps to offset by (default 1).
        """
        return FunctionExpression("timeOffset", args)

    @classmethod
    def timeSequence(cls, *args) -> FunctionExpression:
        """
        Returns an array of `Date` instances from *start* (inclusive) to *stop* (exclusive), with each entry separated by the given time `unit <https://vega.github.io/vega/docs/api/time/#time-units>`__ in the local timezone.

        The optional *step* argument indicates the number of time unit steps to take between each sequence entry (default 1).
        """
        return FunctionExpression("timeSequence", args)

    @classmethod
    def utc(cls, *args) -> FunctionExpression:
        """Returns a timestamp for the given UTC date. The *month* is 0-based, such that `1` represents February."""
        return FunctionExpression("utc", args)

    @classmethod
    def utcdate(cls, *args) -> FunctionExpression:
        """Returns the day of the month for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcdate", args)

    @classmethod
    def utcday(cls, *args) -> FunctionExpression:
        """Returns the day of the week for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcday", args)

    @classmethod
    def utcdayofyear(cls, *args) -> FunctionExpression:
        """Returns the one-based day of the year for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcdayofyear", args)

    @classmethod
    def utcyear(cls, *args) -> FunctionExpression:
        """Returns the year for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcyear", args)

    @classmethod
    def utcquarter(cls, *args) -> FunctionExpression:
        """Returns the quarter of the year (0-3) for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcquarter", args)

    @classmethod
    def utcmonth(cls, *args) -> FunctionExpression:
        """Returns the (zero-based) month for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcmonth", args)

    @classmethod
    def utcweek(cls, *args) -> FunctionExpression:
        """
        Returns the week number of the year for the given *datetime*, in UTC time.

        This function assumes Sunday-based weeks.
        Days before the first Sunday of the year are considered to be in week 0,
        the first Sunday of the year is the start of week 1,
        the second Sunday week 2, etc.
        """
        return FunctionExpression("utcweek", args)

    @classmethod
    def utchours(cls, *args) -> FunctionExpression:
        """Returns the hours component for the given *datetime* value, in UTC time."""
        return FunctionExpression("utchours", args)

    @classmethod
    def utcminutes(cls, *args) -> FunctionExpression:
        """Returns the minutes component for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcminutes", args)

    @classmethod
    def utcseconds(cls, *args) -> FunctionExpression:
        """Returns the seconds component for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcseconds", args)

    @classmethod
    def utcmilliseconds(cls, *args) -> FunctionExpression:
        """Returns the milliseconds component for the given *datetime* value, in UTC time."""
        return FunctionExpression("utcmilliseconds", args)

    @classmethod
    def utcOffset(cls, *args) -> FunctionExpression:
        """
        Returns a new `Date` instance that offsets the given *date* by the specified time `unit <https://vega.github.io/vega/docs/api/time/#time-units>`__ in UTC time.

        The optional *step* argument indicates the number of time unit steps to offset by (default 1).
        """
        return FunctionExpression("utcOffset", args)

    @classmethod
    def utcSequence(cls, *args) -> FunctionExpression:
        """
        Returns an array of `Date` instances from *start* (inclusive) to *stop* (exclusive), with each entry separated by the given time `unit <https://vega.github.io/vega/docs/api/time/#time-units>`__ in UTC time.

        The optional *step* argument indicates the number of time unit steps to take between each sequence entry (default 1).
        """
        return FunctionExpression("utcSequence", args)

    @classmethod
    def extent(cls, *args) -> FunctionExpression:
        """Returns a new `[min, max]` array with the minimum and maximum values of the input array, ignoring `null`, `undefined`, and `NaN` values."""
        return FunctionExpression("extent", args)

    @classmethod
    def clampRange(cls, *args) -> FunctionExpression:
        """
        Clamps a two-element *range* array in a span-preserving manner.

        If the span of the input *range* is less than `(max - min)` and an endpoint exceeds either the *min* or *max* value,
        the range is translated such that the span is preserved and one endpoint touches the boundary of the `[min, max]` range.
        If the span exceeds `(max - min)`, the range `[min, max]` is returned.
        """
        return FunctionExpression("clampRange", args)

    @classmethod
    def indexof(cls, *args) -> FunctionExpression:
        """Returns the first index of *value* in the input *array*, or the first index of *substring* in the input *string*."""
        return FunctionExpression("indexof", args)

    @classmethod
    def inrange(cls, *args) -> FunctionExpression:
        """Tests whether *value* lies within (or is equal to either) the first and last values of the *range* array."""
        return FunctionExpression("inrange", args)

    @classmethod
    def join(cls, *args) -> FunctionExpression:
        """Returns a new string by concatenating all of the elements of the input *array*, separated by commas or a specified *separator* string."""
        return FunctionExpression("join", args)

    @classmethod
    def lastindexof(cls, *args) -> FunctionExpression:
        """Returns the last index of *value* in the input *array*, or the last index of *substring* in the input *string*."""
        return FunctionExpression("lastindexof", args)

    @classmethod
    def length(cls, *args) -> FunctionExpression:
        """Returns the length of the input *array*, or the length of the input *string*."""
        return FunctionExpression("length", args)

    @classmethod
    def lerp(cls, *args) -> FunctionExpression:
        """
        Returns the linearly interpolated value between the first and last entries in the *array* for the provided interpolation *fraction* (typically between 0 and 1).

        For example, `lerp([0, 50], 0.5)` returns 25.
        """
        return FunctionExpression("lerp", args)

    @classmethod
    def peek(cls, *args) -> FunctionExpression:
        """
        Returns the last element in the input *array*.

        Similar to the built-in `Array.pop` method, except that it does not remove the last element.
        This method is a convenient shorthand for `array[array.length - 1]`.
        """
        return FunctionExpression("peek", args)

    @classmethod
    def pluck(cls, *args) -> FunctionExpression:
        """
        Retrieves the value for the specified *field* from a given *array* of objects.

        The input *field* string may include nested properties (e.g., `foo.bar.bz`).
        """
        return FunctionExpression("pluck", args)

    @classmethod
    def reverse(cls, *args) -> FunctionExpression:
        """
        Returns a new array with elements in a reverse order of the input *array*.

        The first array element becomes the last, and the last array element becomes the first.
        """
        return FunctionExpression("reverse", args)

    @classmethod
    def sequence(cls, *args) -> FunctionExpression:
        r"""
        Returns an array containing an arithmetic sequence of numbers.

        If *step* is omitted, it defaults to 1.
        If *start* is omitted, it defaults to 0.

        The *stop* value is exclusive; it is not included in the result.
        If *step* is positive, the last element is the largest `start + i * step` less than *stop*;
        if *step* is negative, the last element is the smallest `start + i * step` greater than *stop*.

        If the returned array would contain an infinite number of values, an empty range is returned.
        The arguments are not required to be integers.
        """
        return FunctionExpression("sequence", args)

    @classmethod
    def slice(cls, *args) -> FunctionExpression:
        """
        Returns a section of *array* between the *start* and *end* indices.

        If the *end* argument is negative, it is treated as an offset from the end of the array `length(array) + end`.
        """
        return FunctionExpression("slice", args)

    @classmethod
    def span(cls, *args) -> FunctionExpression:
        """
        Returns the span of *array*: the difference between the last and first elements, or `array[array.length-1] - array[0]`.

        Or if input is a string: a section of *string* between the *start* and *end* indices.
        If the *end* argument is negative, it is treated as an offset from the end of the string `length(string) + end`.
        """
        return FunctionExpression("span", args)

    @classmethod
    def lower(cls, *args) -> FunctionExpression:
        """Transforms *string* to lower-case letters."""
        return FunctionExpression("lower", args)

    @classmethod
    def pad(cls, *args) -> FunctionExpression:
        """
        Pads a *string* value with repeated instances of a *character* up to a specified *length*.

        If *character* is not specified, a space (' ') is used.
        By default, padding is added to the end of a string.
        An optional *align* parameter specifies if padding should be added to the `'left'` (beginning), `'center'`, or `'right'` (end) of the input string.
        """
        return FunctionExpression("pad", args)

    @classmethod
    def parseFloat(cls, *args) -> FunctionExpression:
        """
        Parses the input *string* to a floating-point value.

        Same as JavaScript's `parseFloat`.
        """
        return FunctionExpression("parseFloat", args)

    @classmethod
    def parseInt(cls, *args) -> FunctionExpression:
        """
        Parses the input *string* to an integer value.

        Same as JavaScript's `parseInt`.
        """
        return FunctionExpression("parseInt", args)

    @classmethod
    def replace(cls, *args) -> FunctionExpression:
        """
        Returns a new string with some or all matches of *pattern* replaced by a *replacement* string.

        The *pattern* can be a string or a regular expression.
        If *pattern* is a string, only the first instance will be replaced.
        Same as `JavaScript's String.replace <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace>`__.
        """
        return FunctionExpression("replace", args)

    @classmethod
    def split(cls, *args) -> FunctionExpression:
        """
        Returns an array of tokens created by splitting the input *string* according to a provided *separator* pattern.

        The result can optionally be constrained to return at most *limit* tokens.
        """
        return FunctionExpression("split", args)

    @classmethod
    def substring(cls, *args) -> FunctionExpression:
        """Returns a section of *string* between the *start* and *end* indices."""
        return FunctionExpression("substring", args)

    @classmethod
    def trim(cls, *args) -> FunctionExpression:
        """Returns a trimmed string with preceding and trailing whitespace removed."""
        return FunctionExpression("trim", args)

    @classmethod
    def truncate(cls, *args) -> FunctionExpression:
        r"""
        Truncates an input *string* to a target *length*.

        The optional *align* argument indicates what part of the string should be truncated: `'left'` (the beginning), `'center'`, or `'right'` (the end).
        By default, the `'right'` end of the string is truncated.
        The optional *ellipsis* argument indicates the string to use to indicate truncated content;
        by default the ellipsis character `...` (`\\u2026`) is used.
        """
        return FunctionExpression("truncate", args)

    @classmethod
    def upper(cls, *args) -> FunctionExpression:
        """Transforms *string* to upper-case letters."""
        return FunctionExpression("upper", args)

    @classmethod
    def merge(cls, *args) -> FunctionExpression:
        """
        Merges the input objects *object1*, *object2*, etc into a new output object.

        Inputs are visited in sequential order, such that key values from later arguments can overwrite those from earlier arguments.

        Example: `merge({a:1, b:2}, {a:3}) -> {a:3, b:2}`.
        """
        return FunctionExpression("merge", args)

    @classmethod
    def dayFormat(cls, *args) -> FunctionExpression:
        """
        Formats a (0-6) *weekday* number as a full week day name, according to the current locale.

        For example: `dayFormat(0) -> "Sunday"`.
        """
        return FunctionExpression("dayFormat", args)

    @classmethod
    def dayAbbrevFormat(cls, *args) -> FunctionExpression:
        """
        Formats a (0-6) *weekday* number as an abbreviated week day name, according to the current locale.

        For example: `dayAbbrevFormat(0) -> "Sun"`.
        """
        return FunctionExpression("dayAbbrevFormat", args)

    @classmethod
    def format(cls, *args) -> FunctionExpression:
        """
        Formats a numeric *value* as a string.

        The *specifier* must be a valid `d3-format specifier <https://d3js.org/d3-format/>`__ (e.g., `format(value, ',.2f')`.
        """
        return FunctionExpression("format", args)

    @classmethod
    def monthFormat(cls, *args) -> FunctionExpression:
        """
        Formats a (zero-based) *month* number as a full month name, according to the current locale.

        For example: `monthFormat(0) -> "January"`.
        """
        return FunctionExpression("monthFormat", args)

    @classmethod
    def monthAbbrevFormat(cls, *args) -> FunctionExpression:
        """
        Formats a (zero-based) *month* number as an abbreviated month name, according to the current locale.

        For example: `monthAbbrevFormat(0) -> "Jan"`.
        """
        return FunctionExpression("monthAbbrevFormat", args)

    @classmethod
    def timeUnitSpecifier(cls, *args) -> FunctionExpression:
        """
        Returns a time format specifier string for the given time `unit <https://vega.github.io/vega/docs/api/time/#time-units>`__.

        The optional *specifiers* object provides a set of specifier sub-strings for customizing the format;
        for more, see the `timeUnitSpecifier API documentation <https://vega.github.io/vega/docs/api/time/#timeUnitSpecifier>`__.

        The resulting specifier string can then be used as input to the `timeFormat <https://vega.github.io/vega/docs/expressions/#timeFormat>`__ or
        `utcFormat <https://vega.github.io/vega/docs/expressions/#utcFormat>`__ functions, or as the *format* parameter of an axis or legend.

        For example: `timeFormat(date, timeUnitSpecifier('year'))` or `timeFormat(date, timeUnitSpecifier(['hours', 'minutes']))`.
        """
        return FunctionExpression("timeUnitSpecifier", args)

    @classmethod
    def timeFormat(cls, *args) -> FunctionExpression:
        """
        Formats a datetime *value* (either a `Date` object or timestamp) as a string, according to the local time.

        The *specifier* must be a valid `d3-time-format specifier <https://d3js.org/d3-time-format/>`__.
        For example: `timeFormat(timestamp, '%A')`.
        """
        return FunctionExpression("timeFormat", args)

    @classmethod
    def timeParse(cls, *args) -> FunctionExpression:
        """
        Parses a *string* value to a Date object, according to the local time.

        The *specifier* must be a valid `d3-time-format specifier <https://d3js.org/d3-time-format/>`__.
        For example: `timeParse('June 30, 2015', '%B %d, %Y')`.
        """
        return FunctionExpression("timeParse", args)

    @classmethod
    def utcFormat(cls, *args) -> FunctionExpression:
        """
        Formats a datetime *value* (either a `Date` object or timestamp) as a string, according to `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`__ time.

        The *specifier* must be a valid `d3-time-format specifier <https://d3js.org/d3-time-format/>`__.
        For example: `utcFormat(timestamp, '%A')`.
        """
        return FunctionExpression("utcFormat", args)

    @classmethod
    def utcParse(cls, *args) -> FunctionExpression:
        """
        Parses a *string* value to a Date object, according to `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`__ time.

        The *specifier* must be a valid `d3-time-format specifier <https://d3js.org/d3-time-format/>`__.
        For example: `utcParse('June 30, 2015', '%B %d, %Y')`.
        """
        return FunctionExpression("utcParse", args)

    @classmethod
    def regexp(cls, *args) -> FunctionExpression:
        """
        Creates a regular expression instance from an input *pattern* string and optional *flags*.

        Same as `JavaScript's `RegExp` <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp>`__.
        """
        return FunctionExpression("regexp", args)

    @classmethod
    def test(cls, *args) -> FunctionExpression:
        r"""
        Evaluates a regular expression *regexp* against the input *string*, returning `true` if the string matches the pattern, `false` otherwise.

        For example: `test(\d{3}, "32-21-9483") -> true`.
        """
        return FunctionExpression("test", args)

    @classmethod
    def rgb(cls, *args) -> FunctionExpression:
        """
        Constructs a new `RGB <https://en.wikipedia.org/wiki/RGB_color_model>`__ color.

        If *r*, *g* and *b* are specified, these represent the channel values of the returned color; an *opacity* may also be specified.
        If a CSS Color Module Level 3 *specifier* string is specified, it is parsed and then converted to the RGB color space. Uses `d3-color's rgb function <https://d3js.org/d3-color#color_rgb>`__.
        """
        return FunctionExpression("rgb", args)

    @classmethod
    def hsl(cls, *args) -> FunctionExpression:
        """
        Constructs a new `HSL <https://en.wikipedia.org/wiki/HSL_and_HSV>`__ color.

        If *h*, *s* and *l* are specified, these represent the channel values of the returned color; an *opacity* may also be specified.
        If a CSS Color Module Level 3 *specifier* string is specified, it is parsed and then converted to the HSL color space.
        Uses `d3-color's hsl function <https://d3js.org/d3-color#hsl>`__.
        """
        return FunctionExpression("hsl", args)

    @classmethod
    def lab(cls, *args) -> FunctionExpression:
        """
        Constructs a new `CIE LAB <https://en.wikipedia.org/wiki/Lab_color_space#CIELAB>`__ color.

        If *l*, *a* and *b* are specified, these represent the channel values of the returned color; an *opacity* may also be specified.
        If a CSS Color Module Level 3 *specifier* string is specified, it is parsed and then converted to the LAB color space.
        Uses `d3-color's lab function <https://d3js.org/d3-color#lab>`__.
        """
        return FunctionExpression("lab", args)

    @classmethod
    def hcl(cls, *args) -> FunctionExpression:
        """
        Constructs a new `HCL <https://en.wikipedia.org/wiki/Lab_color_space#CIELAB>`__ (hue, chroma, luminance) color.

        If *h*, *c* and *l* are specified, these represent the channel values of the returned color; an *opacity* may also be specified.
        If a CSS Color Module Level 3 *specifier* string is specified, it is parsed and then converted to the HCL color space.
        Uses `d3-color's hcl function <https://d3js.org/d3-color#hcl>`__.
        """
        return FunctionExpression("hcl", args)

    @classmethod
    def luminance(cls, *args) -> FunctionExpression:
        """
        Returns the luminance for the given color *specifier* (compatible with `d3-color's rgb function <https://d3js.org/d3-color#rgb)>`__.

        The luminance is calculated according to the `W3C Web Content Accessibility Guidelines <https://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef>`__.
        """
        return FunctionExpression("luminance", args)

    @classmethod
    def contrast(cls, *args) -> FunctionExpression:
        """
        Returns the contrast ratio between the input color specifiers as a float between 1 and 21.

        The contrast is calculated according to the `W3C Web Content Accessibility Guidelines <https://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef>`__.
        """
        return FunctionExpression("contrast", args)

    @classmethod
    def item(cls, *args) -> FunctionExpression:
        """Returns the current scenegraph item that is the target of the event."""
        return FunctionExpression("item", args)

    @classmethod
    def group(cls, *args) -> FunctionExpression:
        """
        Returns the scenegraph group mark item in which the current event has occurred.

        If no arguments are provided, the immediate parent group is returned.
        If a group name is provided, the matching ancestor group item is returned.
        """
        return FunctionExpression("group", args)

    @classmethod
    def xy(cls, *args) -> FunctionExpression:
        """
        Returns the x- and y-coordinates for the current event as a two-element array.

        If no arguments are provided, the top-level coordinate space of the view is used.
        If a scenegraph *item* (or string group name) is provided, the coordinate space of the group item is used.
        """
        return FunctionExpression("xy", args)

    @classmethod
    def x(cls, *args) -> FunctionExpression:
        """
        Returns the x coordinate for the current event.

        If no arguments are provided, the top-level coordinate space of the view is used.
        If a scenegraph *item* (or string group name) is provided, the coordinate space of the group item is used.
        """
        return FunctionExpression("x", args)

    @classmethod
    def y(cls, *args) -> FunctionExpression:
        """
        Returns the y coordinate for the current event.

        If no arguments are provided, the top-level coordinate space of the view is used.
        If a scenegraph *item* (or string group name) is provided, the coordinate space of the group item is used.
        """
        return FunctionExpression("y", args)

    @classmethod
    def pinchDistance(cls, *args) -> FunctionExpression:
        """Returns the pixel distance between the first two touch points of a multi-touch event."""
        return FunctionExpression("pinchDistance", args)

    @classmethod
    def pinchAngle(cls, *args) -> FunctionExpression:
        """Returns the angle of the line connecting the first two touch points of a multi-touch event."""
        return FunctionExpression("pinchAngle", args)

    @classmethod
    def inScope(cls, *args) -> FunctionExpression:
        """Returns true if the given scenegraph *item* is a descendant of the group mark in which the event handler was defined, false otherwise."""
        return FunctionExpression("inScope", args)

    @classmethod
    def data(cls, *args) -> FunctionExpression:
        """
        Returns the array of data objects for the Vega data set with the given *name*.

        If the data set is not found, returns an empty array.
        """
        return FunctionExpression("data", args)

    @classmethod
    def indata(cls, *args) -> FunctionExpression:
        """
        Tests if the data set with a given *name* contains a datum with a *field* value that matches the input *value*.

        For example: `indata('table', 'category', value)`.
        """
        return FunctionExpression("indata", args)

    @classmethod
    def scale(cls, *args) -> FunctionExpression:
        """
        Applies the named scale transform (or projection) to the specified *value*.

        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the scale or projection.
        """
        return FunctionExpression("scale", args)

    @classmethod
    def invert(cls, *args) -> FunctionExpression:
        """
        Inverts the named scale transform (or projection) for the specified *value*.

        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the scale or projection.
        """
        return FunctionExpression("invert", args)

    @classmethod
    def copy(cls, *args) -> FunctionExpression:  # type: ignore[override]
        """
        Returns a copy (a new cloned instance) of the named scale transform of projection, or `undefined` if no scale or projection is found.

        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the scale or projection.
        """
        # error: Signature of "copy" incompatible with supertype "SchemaBase"  [override]
        # note:      def copy(self, deep: bool | Iterable[Any] = ..., ignore: list[str] | None = ...) -> expr
        # NOTE: Not relevant as `expr() -> ExprRef`
        # this method is only accesible via `expr.copy()`
        return FunctionExpression("copy", args)

    @classmethod
    def domain(cls, *args) -> FunctionExpression:
        """
        Returns the scale domain array for the named scale transform, or an empty array if the scale is not found.

        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the scale.
        """
        return FunctionExpression("domain", args)

    @classmethod
    def range(cls, *args) -> FunctionExpression:
        """
        Returns the scale range array for the named scale transform, or an empty array if the scale is not found.

        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the scale.
        """
        return FunctionExpression("range", args)

    @classmethod
    def bandwidth(cls, *args) -> FunctionExpression:
        """
        Returns the current band width for the named band scale transform, or zero if the scale is not found or is not a band scale.

        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the scale.
        """
        return FunctionExpression("bandwidth", args)

    @classmethod
    def bandspace(cls, *args) -> FunctionExpression:
        """
        Returns the number of steps needed within a band scale, based on the *count* of domain elements and the inner and outer padding values.

        While normally calculated within the scale itself, this function can be helpful for determining the size of a chart's layout.
        """
        return FunctionExpression("bandspace", args)

    @classmethod
    def gradient(cls, *args) -> FunctionExpression:
        """
        Returns a linear color gradient for the *scale* (whose range must be a `continuous color scheme <https://vega.github.io/vega/docs/schemes>`__ and starting and ending points *p0* and *p1*, each an `[x, y]` array.

        The points *p0* and *p1* should be expressed in normalized coordinates in the domain `[0, 1]`, relative to the bounds of the item being colored.

        If unspecified, *p0* defaults to `[0, 0]` and *p1* defaults to `[1, 0]`, for a horizontal gradient that spans the full bounds of an item.
        The optional *count* argument indicates a desired target number of sample points to take from the color scale.
        """
        return FunctionExpression("gradient", args)

    @classmethod
    def panLinear(cls, *args) -> FunctionExpression:
        """
        Given a linear scale *domain* array with numeric or datetime values, returns a new two-element domain array that is the result of panning the domain by a fractional *delta*.

        The *delta* value represents fractional units of the scale range; for example, `0.5` indicates panning the scale domain to the right by half the scale range.
        """
        return FunctionExpression("panLinear", args)

    @classmethod
    def panLog(cls, *args) -> FunctionExpression:
        """
        Given a log scale *domain* array with numeric or datetime values, returns a new two-element domain array that is the result of panning the domain by a fractional *delta*.

        The *delta* value represents fractional units of the scale range; for example, `0.5` indicates panning the scale domain to the right by half the scale range.
        """
        return FunctionExpression("panLog", args)

    @classmethod
    def panPow(cls, *args) -> FunctionExpression:
        """
        Given a power scale *domain* array with numeric or datetime values and the given *exponent*, returns a new two-element domain array that is the result of panning the domain by a fractional *delta*.

        The *delta* value represents fractional units of the scale range; for example, `0.5` indicates panning the scale domain to the right by half the scale range.
        """
        return FunctionExpression("panPow", args)

    @classmethod
    def panSymlog(cls, *args) -> FunctionExpression:
        """
        Given a symmetric log scale *domain* array with numeric or datetime values parameterized by the given *constant*, returns a new two-element domain array that is the result of panning the domain by a fractional *delta*.

        The *delta* value represents fractional units of the scale range; for example, `0.5` indicates panning the scale domain to the right by half the scale range.
        """
        return FunctionExpression("panSymlog", args)

    @classmethod
    def zoomLinear(cls, *args) -> FunctionExpression:
        """
        Given a linear scale *domain* array with numeric or datetime values, returns a new two-element domain array that is the result of zooming the domain by a *scaleFactor*, centered at the provided fractional *anchor*.

        The *anchor* value represents the zoom position in terms of fractional units of the scale range; for example, `0.5` indicates a zoom centered on the mid-point of the scale range.
        """
        return FunctionExpression("zoomLinear", args)

    @classmethod
    def zoomLog(cls, *args) -> FunctionExpression:
        """
        Given a log scale *domain* array with numeric or datetime values, returns a new two-element domain array that is the result of zooming the domain by a *scaleFactor*, centered at the provided fractional *anchor*.

        The *anchor* value represents the zoom position in terms of fractional units of the scale range; for example, `0.5` indicates a zoom centered on the mid-point of the scale range.
        """
        return FunctionExpression("zoomLog", args)

    @classmethod
    def zoomPow(cls, *args) -> FunctionExpression:
        """
        Given a power scale *domain* array with numeric or datetime values and the given *exponent*, returns a new two-element domain array that is the result of zooming the domain by a *scaleFactor*, centered at the provided fractional *anchor*.

        The *anchor* value represents the zoom position in terms of fractional units of the scale range; for example, `0.5` indicates a zoom centered on the mid-point of the scale range.
        """
        return FunctionExpression("zoomPow", args)

    @classmethod
    def zoomSymlog(cls, *args) -> FunctionExpression:
        """
        Given a symmetric log scale *domain* array with numeric or datetime values parameterized by the given *constant*, returns a new two-element domain array that is the result of zooming the domain by a *scaleFactor*, centered at the provided fractional *anchor*.

        The *anchor* value represents the zoom position in terms of fractional units of the scale range; for example, `0.5` indicates a zoom centered on the mid-point of the scale range.
        """
        return FunctionExpression("zoomSymlog", args)

    @classmethod
    def geoArea(cls, *args) -> FunctionExpression:
        """
        Returns the projected planar area (typically in square pixels) of a GeoJSON *feature* according to the named *projection*.

        If the *projection* argument is `null`, computes the spherical area in steradians using unprojected longitude, latitude coordinates.
        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the projection.
        Uses d3-geo's `geoArea <https://d3js.org/d3-geo#geoArea>`__ and `path.area <https://d3js.org/d3-geo#path_area>`__ methods.
        """
        return FunctionExpression("geoArea", args)

    @classmethod
    def geoBounds(cls, *args) -> FunctionExpression:
        """
        Returns the projected planar bounding box (typically in pixels) for the specified GeoJSON *feature*, according to the named *projection*.

        The bounding box is represented by a two-dimensional array: `[[x0, y0], [x1, y1]]`,
        where *x0* is the minimum x-coordinate, *y0* is the minimum y-coordinate,
        *x1* is the maximum x-coordinate, and *y1* is the maximum y-coordinate.

        If the *projection* argument is `null`, computes the spherical bounding box using unprojected longitude, latitude coordinates.
        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the projection.
        Uses d3-geo's `geoBounds <https://d3js.org/d3-geo#geoBounds>`__ and `path.bounds <https://d3js.org/d3-geo#path_bounds>`__ methods.
        """
        return FunctionExpression("geoBounds", args)

    @classmethod
    def geoCentroid(cls, *args) -> FunctionExpression:
        """
        Returns the projected planar centroid (typically in pixels) for the specified GeoJSON *feature*, according to the named *projection*.

        If the *projection* argument is `null`, computes the spherical centroid using unprojected longitude, latitude coordinates.
        The optional *group* argument takes a scenegraph group mark item to indicate the specific scope in which to look up the projection.
        Uses d3-geo's `geoCentroid <https://d3js.org/d3-geo#geoCentroid>`__ and `path.centroid <https://d3js.org/d3-geo#path_centroid>`__ methods.
        """
        return FunctionExpression("geoCentroid", args)

    @classmethod
    def treePath(cls, *args) -> FunctionExpression:
        """
        For the hierarchy data set with the given *name*, returns the shortest path through from the *source* node id to the *target* node id.

        The path starts at the *source* node, ascends to the least common ancestor of the *source* node and the *target* node, and then descends to the *target* node.
        """
        return FunctionExpression("treePath", args)

    @classmethod
    def treeAncestors(cls, *args) -> FunctionExpression:
        """For the hierarchy data set with the given *name*, returns the array of ancestors nodes, starting with the input *node*, then followed by each parent up to the root."""
        return FunctionExpression("treeAncestors", args)

    @classmethod
    def containerSize(cls, *args) -> FunctionExpression:
        """
        Returns the current CSS box size (`[el.clientWidth, el.clientHeight]`) of the parent DOM element that contains the Vega view.

        If there is no container element, returns `[undefined, undefined]`.
        """
        return FunctionExpression("containerSize", args)

    @classmethod
    def screen(cls, *args) -> FunctionExpression:
        """Returns the `window.screen <https://developer.mozilla.org/en-US/docs/Web/API/Window/screen>`__ object, or `{}` if Vega is not running in a browser environment."""
        return FunctionExpression("screen", args)

    @classmethod
    def windowSize(cls, *args) -> FunctionExpression:
        """Returns the current window size (`[window.innerWidth, window.innerHeight]`) or `[undefined, undefined]` if Vega is not running in a browser environment."""
        return FunctionExpression("windowSize", args)

    @classmethod
    def warn(cls, *args) -> FunctionExpression:
        """
        Logs a warning message and returns the last argument.

        For the message to appear in the console, the visualization view must have the appropriate logging level set.
        """
        return FunctionExpression("warn", args)

    @classmethod
    def info(cls, *args) -> FunctionExpression:
        """
        Logs an informative message and returns the last argument.

        For the message to appear in the console, the visualization view must have the appropriate logging level set.
        """
        return FunctionExpression("info", args)

    @classmethod
    def debug(cls, *args) -> FunctionExpression:
        """
        Logs a debugging message and returns the last argument.

        For the message to appear in the console, the visualization view must have the appropriate logging level set.
        """
        return FunctionExpression("debug", args)


_ExprType = expr
# NOTE: Compatibility alias for previous type of `alt.expr`.
# `_ExprType` was not referenced in any internal imports/tests.
