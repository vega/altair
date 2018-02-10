__all__ = ['DataFrame']


import warnings
from collections import OrderedDict
from ..utils._py3k_compat import string_types

import pandas as pd


def js_repr(val):
    """Return a javascript-safe string representation of val"""
    if val is True:
        return 'true'
    elif val is False:
        return 'false'
    elif val is None:
        return 'null'
    else:
        return repr(val)


class Expression(object):
    """Expression

    This is an object to enable the build-up of Javascript expressions using
    a Python syntax. Calling ``repr(obj)`` will return a Javascript
    representation of the object and/or the operations it encodes.
    """
    # TODO: Javascript's add is does things like string concatenation...
    # should we attempt to translate Python's semantics appropriately?
    def __add__(self, other):
        return BinaryExpression("+", self, other)

    def __radd__(self, other):
        return BinaryExpression("+", other, self)

    def __sub__(self, other):
        return BinaryExpression("-", self, other)

    def __rsub__(self, other):
        return BinaryExpression("-", other, self)

    def __mul__(self, other):
        return BinaryExpression("*", self, other)

    def __rmul__(self, other):
        return BinaryExpression("*", other, self)

    def __floordiv__(self, other):
        return BinaryExpression("/", self, other)

    def __rfloordiv__(self, other):
        return BinaryExpression("/", other, self)

    def __truediv__(self, other):
        warnings.warn("Javascript uses floor division; use '//' to silence this warning")
        return self.__floordiv__(other)

    def __rtruediv__(self, other):
        warnings.warn("Javascript uses floor division; use '//' to silence this warning")
        return self.__rfloordiv(other)

    __div__ = __floordiv__

    __rdiv__ = __rfloordiv__

    def __mod__(self, other):
        return BinaryExpression('%', self, other)

    def __rmod__(self, other):
        return BinaryExpression('%', other, self)

    def __pow__(self, other):
        # "**" Javascript operator is not supported in all browsers
        return FunctionExpression('pow', self, other)

    def __rpow__(self, other):
        # "**" Javascript operator is not supported in all browsers
        return FunctionExpression('pow', other, self)

    def __neg__(self):
        return UnaryExpression('-', self)

    def __pos__(self):
        return UnaryExpression('+', self)

    # comparison operators

    def __eq__(self, other):
        return BinaryExpression("==", self, other)

    def __ne__(self, other):
        return BinaryExpression("!=", self, other)

    def __gt__(self, other):
        return BinaryExpression(">", self, other)

    def __lt__(self, other):
        return BinaryExpression("<", self, other)

    def __ge__(self, other):
        return BinaryExpression(">=", self, other)

    def __le__(self, other):
        return BinaryExpression("<=", self, other)

    def __abs__(self):
        return FunctionExpression('abs', self)

    # TODO: how to handle assignment? Overwriting would be an issue...

    # logical operators
    def __and__(self, other):
        return BinaryExpression('&&', self, other)

    def __rand__(self, other):
        return BinaryExpression('&&', other, self)

    def __or__(self, other):
        return BinaryExpression('||', self, other)

    def __ror__(self, other):
        return BinaryExpression('||', other, self)

    def __invert__(self):
        return UnaryExpression('!', self)


class UnaryExpression(Expression):
    def __init__(self, op, val):
        self.op = op
        self.val = val

    def __repr__(self):
        return "({op}{val})".format(op=self.op, val=js_repr(self.val))


class BinaryExpression(Expression):
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return "({lhs}{op}{rhs})".format(op=self.op,
                                         lhs=js_repr(self.lhs),
                                         rhs=js_repr(self.rhs))


class FunctionExpression(Expression):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __repr__(self):
        args = ','.join(js_repr(arg) for arg in self.args)
        return "{name}({args})".format(name=self.name, args=args)


class ConstExpression(Expression):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc
        self.__doc__ = """{0}: {1}""".format(name, doc)

    def __repr__(self):
        return str(self.name)


class Series(Expression):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return "datum.{name}".format(name=self.name)

    @property
    def contents(self):
        if self.parent is None:
            return None
        else:
            return self.parent._calculated_cols.get(self.name, None)


class DataFrame(object):
    """Lazy wrapper for altair data source

    This object provides DataFrame-like operations for any data source, which
    are not immediately computed but rather stored for later translation into
    Vega-Lite's data transformation language, which is a subset of javascript.

    If you need an "anonymous" DataFrame object, i.e. one not linked to any
    particular dataset, ``altair.expr.df`` is available.

    Parameters
    ----------
    data : string, pd.DataFrame, or altair.Data object
        The data to wrap and do operations on
    cols : list (optional)
        The column names within the dataset. If not specified, columns will be
        inferred from the data if possible (i.e. if data is a pandas DataFrame).

    Notes
    -----
        When column names (``cols``) are present, they will be available via
        tab-completion in the IPython shell, and attempting to access a column
        which does not appear in the list will result in an error.

    Examples
    --------
    >>> from altair import expr, Chart
    >>> df = expr.DataFrame('url/to/my/data.json')
    >>> df['density'] = df.population // df.area    # add calculated column
    >>> df = df[df.density > 100]                   # filter by value
    >>> df
    <Data Wrapper; columns=[*, density]>

    # Filter and transform operations are realized in the Chart object
    >>> chart = Chart(df)
    >>> print(chart.to_json(indent=2))         # doctest: +NORMALIZE_WHITESPACE
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v1.2.1.json",
      "data": {
        "url": "url/to/my/data.json"
      },
      "mark": "point",
      "transform": {
        "calculate": [
          {
            "expr": "(datum.population/datum.area)",
            "field": "density"
          }
        ],
        "filter": "(datum.density>100)"
      }
    }
    """
    def __init__(self, data, cols=None, read_only=False):
        self.read_only = read_only

        if isinstance(data, self.__class__):
            self._data = data._data
            if cols is None:
                self._cols = self._get_cols(self._data, data._cols)
            else:
                self._cols = self._get_cols(self._data, cols)
            self._calculated_cols = data._calculated_cols.copy()
            self._filters = data._filters[:]
        else:
            self._data = data
            self._cols = self._get_cols(data, cols)
            self._calculated_cols = OrderedDict({})
            self._filters = []

    def copy(self, **kwargs):
        return self.__class__(self, **kwargs)

    def __repr__(self):
        if self._cols is None:
            cols = ['*']
        else:
            cols = list(self._cols)
        cols.extend(list(self._calculated_cols))
        return ("<Data Wrapper; columns=[{0}]>".format(', '.join(cols)))

    @classmethod
    def _get_cols(cls, data, cols=None):
        def is_altair_Data(data):
            # importing here avoids circular imports
            from ... import Data
            return isinstance(data, Data)

        if cols is not None:
            return list(cols)
        elif isinstance(data, string_types):
            return None
        elif isinstance(data, pd.DataFrame):
            return list(data.columns)
        elif is_altair_Data(data):
            if hasattr(data, 'values'):
                return list(data.values[0].keys())
            else:
                return None
        else:
            raise ValueError("Unrecognized data type")

    def __dir__(self):
        return (self._cols or []) + list(self._calculated_cols.keys())

    def __getattr__(self, attr):
        if self._cols is None or attr in self._cols or attr in self._calculated_cols:
            return Series(attr, self)
        else:
            raise AttributeError("No attribute {0}".format(attr))

    def __getitem__(self, attr):
        if isinstance(attr, string_types):
            # Select a column
            if self._cols is None or attr in self._cols or attr in self._calculated_cols:
                return Series(attr, self)
            else:
                raise KeyError("No column {0}".format(attr))
        elif isinstance(attr, Expression):
            # Apply a filter
            result = self.copy()
            result._filters.append(attr)
            return result
        elif isinstance(attr, (list, tuple)):
            return self.copy(cols=attr)
        else:
            raise KeyError("attribute {0} not recognized".format(attr))

    def __setitem__(self, attr, obj):
        if self.read_only:
            raise ValueError("Cannot set a column in a read-only data source")
        if (self._cols is not None and attr in self._cols) or attr in self._calculated_cols:
            raise ValueError("Cannot overwrite column '{0}'".format(attr))
        self._calculated_cols[attr] = obj
