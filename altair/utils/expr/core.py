__all__ = ['DataFrame']


import warnings
from collections import OrderedDict
from .._py3k_compat import string_types

import pandas as pd


class Expression(object):
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
        FunctionExpression('pow', (self, other))

    def __rpow__(self, other):
        # "**" Javascript operator is not supported in all browsers
        FunctionExpression('pow', (other, self))

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
        return "({op}{val})".format(op=self.op, val=repr(self.val))


class BinaryExpression(Expression):
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return "({lhs}{op}{rhs})".format(op=self.op,
                                         lhs=repr(self.lhs),
                                         rhs=repr(self.rhs))


class FunctionExpression(Expression):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __repr__(self):
        args = ','.join(repr(arg) for arg in self.args)
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
    """Wrapper for pandas dataframe

    Parameters
    ----------
    data : string, pd.DataFrame, or altair.Data object
        The data to wrap and do operations on
    cols : list (optional)
        The column names
    df : DataFrame or dict or iterable
        Object specifying the valid column names in the dataframe. Names can
        be DataFrame columns, dict keys, or items returned by an iterable.
    """
    def __init__(self, data, cols=None):
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

    def copy(self):
        return self.__class__(self)

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
        # TODO: add support for attr=list of columns, returning a new object
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
            # Return a subset array
            raise NotImplementedError("list of columns")
        else:
            raise KeyError("attribute {0} not recognized".format(attr))

    def __setitem__(self, attr, obj):
        if (self._cols is not None and attr in self._cols) or attr in self._calculated_cols:
            raise ValueError("Cannot overwrite column '{0}'".format(attr))
        self._calculated_cols[attr] = obj
