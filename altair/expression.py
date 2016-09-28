"""Tools for building Vega-Lite Expressions"""

__all__ = ['vg']

import json


class _Expression(object):
    """Vega expression generator.

    This object provides a Python interface to generating vega expressions,
    which are used in the :class:`Transform`. :class:`Formula`,
    and :class:`Filter` objects.

    For example, instead of a formula like this::

        expr = "if(datum.gender == 0, 'M', 'F')"

    You can compose a formula like this:

        from altair.expression import vg
        expr = vg.if_(vg.d.gender == 0, 'M', 'F')

    This expression can be used in place of the above string in a
    :class:`Formula` object.
    """
    def __init__(self, df=None):
        self.d = _Datum(df)

    def __getattr__(self, name):
        if name in _exp_consts:
            return _VgConst(name, doc=_exp_consts[name])
        elif name in _exp_funcs:
            return _VgFunc(name, doc=_exp_funcs[name])
        else:
            raise AttributeError('No atttribute {0}'.format(name))

    def __dir__(self):
        return ['d', 'with_df'] + list(_exp_consts.keys()) + list(_exp_funcs.keys())

    def with_df(self, df):
        return _Expression(df)


# The following dicts are populated from the vega Expression documentation at
# https://github.com/vega/vega/wiki/Expressions

_exp_vars = ['datum', 'parent', 'event', 'signals']

# List of available constants
_exp_consts = {
    'NaN': 'not a number (same as JavaScript literal NaN)',
    'E': 'the transcendental number e (alias to Math.E)',
    'LN2': 'the natural log of 2 (alias to Math.LN2)',
    'LN10': 'the natural log of 10 (alias to Math.LN10)',
    'LOG2E': 'the base 2 logarithm of e (alias to Math.LOG2E)',
    'LOG10E': 'the base 10 logarithm e (alias to Math.LOG10E)',
    'PI': 'the transcendental number pi (alias to Math.PI)',
    'SQRT1_2': 'the square root of 0.5 (alias to Math.SQRT1_2)',
    'SQRT2': 'the square root of 2 (alias to Math.SQRT1_2)',
}

# List of available functions
_exp_funcs = {
    'isNaN': 'checks if a value is not-a-number (same as JavaScript `isNaN`)',
    'isFinite': 'checks if a value is a finite number (same as JavaScript `isFinite`)',
    'abs': 'absolute value (alias to `Math.abs`)',
    'acos': 'trigonometric arccosine (alias to `Math.acos`)',
    'asin': 'trigonometric arcsine (alias to `Math.asin`)',
    'atan': 'trigonometric arctangent (alias to `Math.atan`)',
    'atan2': 'returns the arctangent of the quotient of its arguments (alias to `Math.atan2`)',
    'ceil': 'rounds to the nearest integer of greater value (alias to `Math.ceil`)',
    'cos': 'trigonometric cosine (alias to `Math.cos`)',
    'exp': 'raises _e_ to the provided exponent (alias to `Math.exp`)',
    'floor': 'rounds to the nearest integer of lower value (alias to `Math.floor`)',
    'log': 'natural logarithm function (alias to `Math.log`)',
    'max': 'return the maximum argument (alias to `Math.max`)',
    'min': 'returns the minimum argument value (alias to `Math.min`)',
    'pow': 'exponentiates the first argument by the second argument (alias to `Math.pow`)',
    'random': 'generates a pseudo-random number in the range [0,1) (alias to `Math.random`)',
    'round': 'rounds to the nearest integer (alias to `Math.round`)',
    'sin': 'trigonometric sine (alias to `Math.sin`)',
    'sqrt': 'square root function (alias to `Math.sqrt`)',
    'tan': 'trigonometric tangent (alias to `Math.tan`)',
    'clamp': 'restricts a value between a specified min and max (e.g. `clamp(value, min, max)`)',
    'inrange': 'tests whether a value falls within a specified inclusive extent; an optional flag uses an exclusive extent instead (i.e., `inrange(value, a, b, exclusive?) `).',
    'now': 'returns the timestamp for the current time',
    'datetime': 'returns a new `Date` instance _(year, month[, day, hour, min, sec, millisec])_  Note that, just like Javascript, `month` is 0-based. For example, `1` represents February.',
    'date': 'returns the day of the month for a given date input, in local time',
    'day': 'return the day of the week for a given date input, in local time',
    'year': 'returns the year for a given date input, in local time',
    'month': 'returns the (zero-based) month for a given date input, in local time',
    'hours': 'returns the hours component for a given date input, in local time',
    'minutes': 'returns the minutes component for a given date input, in local time',
    'seconds': 'returns the seconds component for a given date input, in local time',
    'milliseconds': 'returns the milliseconds component for a given date input, in local time',
    'time': 'returns the epoch-based timestamp for a given date input',
    'timezoneoffset': 'returns the timezone offset from the local timezone to UTC for a given date input',
    'utc': 'returns a timestamp for a UTC date _(year, month[, day, hour, min, sec])',
    'utcdate': 'returns the day of the month for a given date input, in UTC time',
    'utcday': 'returns the day of the week for a given date input, in UTC time',
    'utcyear': 'returns the year for a given date input, in UTC time',
    'utcmonth': 'returns the (zero-based) month for a given date input, in UTC time',
    'utchours': 'returns the hours component for a given date input, in UTC time',
    'utcminutes': 'returns the hours component for a given date input, in UTC time',
    'utcseconds': 'returns the hours component for a given date input, in UTC time',
    'utcmilliseconds': 'returns the hours component for a given date input, in UTC time',
    'length': 'returns the length of an array or string',
    'indexof': 'returns the first index of an element (for array inputs) or substring (for string inputs) e.g., `indexof("visualization", "i") == 1',
    'lastindexof': 'returns the last index of an element (for array inputs) or substring (for string inputs)  e.g., `lastindexof("visualization", "i") == 10',
    'parseFloat': 'parses a string to a floating-point value (same as JavaScript `parseFloat`)',
    'parseInt': 'parses a string to an integer value (same as JavaScript `parseInt`)',
    'upper': 'transforms a string to upper-case',
    'lower': 'transforms a string to lower-case',
    'replace': 'replace a pattern with a given string (alias to `String.replace`)',
    'slice': 'slices a string into a substring (alias to `String.slice`)',
    'substring': 'extracts a substring from a string (alias to `String.substring`)',
    'format': 'formats a string as a numeric value; the first argument must be a valid [d3-format specifier](https://github.com/d3/d3-format/) (e.g., `format(",.2f", datum.value)`)',
    'timeFormat': 'formats a string as a local datetime; the first argument must be a valid [d3-time-format specifier](https://github.com/d3/d3-time-format/) (e.g., `timeFormat("%A", datum.timestamp)`)',
    'utcFormat': 'formats a string as a [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) datetime; the first argument must be a valid [d3-time-format specifier](https://github.com/mbostock/d3/wiki/Time-Formatting) (e.g., `utcFormat("%", datum.timestamp)`).',
    'regexp': 'creates a regular expression instance from input strings (same as JavaScript `RegExp`)',
    'test': 'evaluates a regular expression against a string, returning true if the string matches the pattern, false otherwise. _Example_: `test(/\\d{3}/, "32-21-9483") -> true',
    'if_': 'if the first argument evaluates true then the second argument is returned, otherwise the third argument is returned (`if(a, b, c)` is equivalent to `a ? b : c`)',
    'open': 'opens a hyperlink (alias to `window.open`). This function is only valid when running in the browser. It should not be invoked within a server-side (e.g., node.js) environment.',
    'eventItem': 'a zero-argument function that returns the current scenegraph item that is the subject of the event.',
    'eventGroup': 'returns the scenegraph group mark item within which the current event has occurred. If no arguments are provided, the immediate parent group is returned. If a group name is provided, the matching ancestor group item is returned.',
    'eventX': 'returns the x-coordinate for the current event. If no arguments are provided, the top-level coordinate space of the visualization is used. If a group name is provided, the coordinate-space of the matching ancestor group item is used.',
    'eventY': 'returns the y-coordinate for the current event. If no arguments are provided, the top-level coordinate space of the visualization is used. If a group name is provided, the coordinate-space of the matching ancestor group item is used.',
    'scale': 'applies a named scale transform to a specified value; by default, looks for the scale at the top-level of the specification, but an optional signal can also be supplied corresponding to the group which contains the scale (i.e., `scale("x", val, group)`). *Note:* This function is only legal within signal stream handlers and mark [production rules](https://github.com/vega/vega/wiki/Marks#production-rules). Invoking this function elsewhere (e.g., with filter or formula transforms) will result in an error.',
    'iscale': 'applies an inverse scale transform to a specified value; by default, looks for the scale at the top-level of the specification, but an optional signal can also be supplied corresponding to the group which contains the scale (i.e., `iscale("x", val, group)`). *Note:* This function is only legal within signal stream handlers and mark [production rules](https://github.com/vega/vega/wiki/Marks#production-rules). Invoking this function elsewhere (e.g., with filter or formula transforms) will result in an error.',
    'indata': 'tests if a specified datasource contains a tuple with a given value for a specific field (i.e., `indata("table", val, "price")`)'
}

NAME_MAP = {'if_': 'if'}


class _VgExpr(object):
    """Base class for expressions"""
    def __init__(self, name, doc=None):
        self.name = NAME_MAP.get(name, name)
        if doc:
            self.__doc__ = doc

    @staticmethod
    def _str(obj):
        if isinstance(obj, _VgExpr):
            return obj.eval()
        else:
            return json.dumps(obj)

    def __str__(self):
        return self.eval()

    def __repr__(self):
        return self.eval()

    def __mul__(self, other):
        return _VgConst('({0}*{1})'.format(self._str(self), self._str(other)))

    def __rmul__(self, other):
        return _VgConst('({0}*{1})'.format(self._str(other), self._str(self)))

    def __div__(self, other):
        return _VgConst('({0}/{1})'.format(self._str(self), self._str(other)))

    def __rdiv__(self, other):
        return _VgConst('({0}/{1})'.format(self._str(other), self._str(self)))

    def __truediv__(self, other):
        return _VgConst('({0}/{1})'.format(self._str(self), self._str(other)))

    def __rtruediv__(self, other):
        return _VgConst('({0}/{1})'.format(self._str(other), self._str(self)))

    def __add__(self, other):
        return _VgConst('({0}+{1})'.format(self._str(self), self._str(other)))

    def __radd__(self, other):
        return _VgConst('({0}+{1})'.format(self._str(other), self._str(self)))

    def __sub__(self, other):
        return _VgConst('({0}-{1})'.format(self._str(self), self._str(other)))

    def __rsub__(self, other):
        return _VgConst('({0}-{1})'.format(self._str(other), self._str(self)))

    def __neg__(self):
        return _VgConst('(-{0})'.format(self._str(self)))

    def __lt__(self, other):
        return _VgConst('({0}<{1})'.format(self._str(self), self._str(other)))

    def __le__(self, other):
        return _VgConst('({0}<={1})'.format(self._str(self), self._str(other)))

    def __gt__(self, other):
        return _VgConst('({0}>{1})'.format(self._str(self), self._str(other)))

    def __ge__(self, other):
        return _VgConst('({0}>={1})'.format(self._str(self), self._str(other)))

    def __eq__(self, other):
        return _VgConst('({0}=={1})'.format(self._str(self), self._str(other)))

    def __ne__(self, other):
        return _VgConst('({0}!={1})'.format(self._str(self), self._str(other)))


class _VgConst(_VgExpr):
    def eval(self):
        return self.name


class _VgFunc(_VgExpr):
    def eval(self):
        raise ValueError('{0} function requires arguments'.format(self.name))

    def __call__(self, *args):
        args = ','.join(self._str(arg) for arg in args)
        return _VgConst("{0}({1})".format(self.name, args))


class _Datum(object):
    def __init__(self, df=None):
        self.df = df

    def __dir__(self):
        if self.df is not None:
            return list(self.df.columns)
        else:
            return []

    def __getattr__(self, attr):
        return _VgConst('datum.{0}'.format(attr))

    def __getitem__(self, item):
        return _VgConst('datum.{0}'.format(item))


# This is the object that will be exposed
vg = _Expression()
