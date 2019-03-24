from .core import FunctionExpression


FUNCTION_LISTING = {
  "utcyear": "returns the year for a given date input, in UTC time",
  "indexof": "returns the first index of an element (for array inputs) or substring (for string inputs) e.g., `indexof(\"visualization\", \"i\") == 1",
  "upper": "transforms a string to upper-case",
  "asin": "trigonometric arcsine (alias to `Math.asin`)",
  "length": "returns the length of an array or string",
  "isFinite": "checks if a value is a finite number (same as JavaScript `isFinite`)",
  "open": "opens a hyperlink (alias to `window.open`). This function is only valid when running in the browser. It should not be invoked within a server-side (e.g., node.js) environment.",
  "cos": "trigonometric cosine (alias to `Math.cos`)",
  "lastindexof": "returns the last index of an element (for array inputs) or substring (for string inputs)  e.g., `lastindexof(\"visualization\", \"i\") == 10",
  "if": "if the first argument evaluates true then the second argument is returned, otherwise the third argument is returned (`if(a, b, c)` is equivalent to `a ? b : c`)",
  "timeFormat": "formats a string as a local datetime; the first argument must be a valid [d3-time-format specifier](https://github.com/d3/d3-time-format/) (e.g., `timeFormat(\"%A\", datum.timestamp)`)",
  "timezoneoffset": "returns the timezone offset from the local timezone to UTC for a given date input",
  "utcmilliseconds": "returns the hours component for a given date input, in UTC time",
  "test": "evaluates a regular expression against a string, returning true if the string matches the pattern, false otherwise. _Example_: `test(/\\d{3}/, \"32-21-9483\") -> true",
  "utcmonth": "returns the (zero-based) month for a given date input, in UTC time",
  "eventGroup": "returns the scenegraph group mark item within which the current event has occurred. If no arguments are provided, the immediate parent group is returned. If a group name is provided, the matching ancestor group item is returned.",
  "minutes": "returns the minutes component for a given date input, in local time",
  "tan": "trigonometric tangent (alias to `Math.tan`)",
  "milliseconds": "returns the milliseconds component for a given date input, in local time",
  "atan": "trigonometric arctangent (alias to `Math.atan`)",
  "parseInt": "parses a string to an integer value (same as JavaScript `parseInt`)",
  "year": "returns the year for a given date input, in local time",
  "utcseconds": "returns the hours component for a given date input, in UTC time",
  "seconds": "returns the seconds component for a given date input, in local time",
  "pow": "exponentiates the first argument by the second argument (alias to `Math.pow`)",
  "abs": "absolute value (alias to `Math.abs`)",
  "utc": "returns a timestamp for a UTC date _(year, month[, day, hour, min, sec])",
  "date": "returns the day of the month for a given date input, in local time",
  "day": "return the day of the week for a given date input, in local time",
  "acos": "trigonometric arccosine (alias to `Math.acos`)",
  "time": "returns the epoch-based timestamp for a given date input",
  "indata": "tests if a specified datasource contains a tuple with a given value for a specific field (i.e., `indata(\"table\", val, \"price\")`)",
  "clamp": "restricts a value between a specified min and max (e.g. `clamp(value, min, max)`)",
  "lower": "transforms a string to lower-case",
  "log": "natural logarithm function (alias to `Math.log`)",
  "atan2": "returns the arctangent of the quotient of its arguments (alias to `Math.atan2`)",
  "eventX": "returns the x-coordinate for the current event. If no arguments are provided, the top-level coordinate space of the visualization is used. If a group name is provided, the coordinate-space of the matching ancestor group item is used.",
  "month": "returns the (zero-based) month for a given date input, in local time",
  "sin": "trigonometric sine (alias to `Math.sin`)",
  "datetime": "returns a new `Date` instance _(year, month[, day, hour, min, sec, millisec])_  Note that, just like Javascript, `month` is 0-based. For example, `1` represents February.",
  "scale": "applies a named scale transform to a specified value; by default, looks for the scale at the top-level of the specification, but an optional signal can also be supplied corresponding to the group which contains the scale (i.e., `scale(\"x\", val, group)`). *Note:* This function is only legal within signal stream handlers and mark [production rules](https://github.com/vega/vega/wiki/Marks#production-rules). Invoking this function elsewhere (e.g., with filter or formula transforms) will result in an error.",
  "random": "generates a pseudo-random number in the range [0,1) (alias to `Math.random`)",
  "sqrt": "square root function (alias to `Math.sqrt`)",
  "round": "rounds to the nearest integer (alias to `Math.round`)",
  "min": "returns the minimum argument value (alias to `Math.min`)",
  "utcday": "returns the day of the week for a given date input, in UTC time",
  "max": "return the maximum argument (alias to `Math.max`)",
  "replace": "replace a pattern with a given string (alias to `String.replace`)",
  "utcminutes": "returns the hours component for a given date input, in UTC time",
  "regexp": "creates a regular expression instance from input strings (same as JavaScript `RegExp`)",
  "utchours": "returns the hours component for a given date input, in UTC time",
  "isNaN": "checks if a value is not-a-number (same as JavaScript `isNaN`)",
  "eventItem": "a zero-argument function that returns the current scenegraph item that is the subject of the event.",
  "utcdate": "returns the day of the month for a given date input, in UTC time",
  "ceil": "rounds to the nearest integer of greater value (alias to `Math.ceil`)",
  "utcFormat": "formats a string as a [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) datetime; the first argument must be a valid [d3-time-format specifier](https://github.com/mbostock/d3/wiki/Time-Formatting) (e.g., `utcFormat(\"%\", datum.timestamp)`).",
  "substring": "extracts a substring from a string (alias to `String.substring`)",
  "hours": "returns the hours component for a given date input, in local time",
  "format": "formats a string as a numeric value; the first argument must be a valid [d3-format specifier](https://github.com/d3/d3-format/) (e.g., `format(\",.2f\", datum.value)`)",
  "exp": "raises _e_ to the provided exponent (alias to `Math.exp`)",
  "parseFloat": "parses a string to a floating-point value (same as JavaScript `parseFloat`)",
  "iscale": "applies an inverse scale transform to a specified value; by default, looks for the scale at the top-level of the specification, but an optional signal can also be supplied corresponding to the group which contains the scale (i.e., `iscale(\"x\", val, group)`). *Note:* This function is only legal within signal stream handlers and mark [production rules](https://github.com/vega/vega/wiki/Marks#production-rules). Invoking this function elsewhere (e.g., with filter or formula transforms) will result in an error.",
  "now": "returns the timestamp for the current time",
  "slice": "slices a string into a substring (alias to `String.slice`)",
  "floor": "rounds to the nearest integer of lower value (alias to `Math.floor`)",
  "inrange": "tests whether a value falls within a specified inclusive extent; an optional flag uses an exclusive extent instead (i.e., `inrange(value, a, b, exclusive?) `).",
  "eventY": "returns the y-coordinate for the current event. If no arguments are provided, the top-level coordinate space of the visualization is used. If a group name is provided, the coordinate-space of the matching ancestor group item is used."
}


# This maps vega expression function names to the Python name
NAME_MAP = {'if': 'if_'}


class ExprFunc(object):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc
        self.__doc__ = """{}(*args)\n    {}""".format(name, doc)

    def __call__(self, *args):
        return FunctionExpression(self.name, args)

    def __repr__(self):
        return "<function expr.{}(*args)>".format(self.name)


def _populate_namespace():
    globals_ = globals()
    for name, doc in FUNCTION_LISTING.items():
        py_name = NAME_MAP.get(name, name)
        globals_[py_name] = ExprFunc(name, doc)
        yield py_name


__all__ = list(_populate_namespace())
