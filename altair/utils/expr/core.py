__all__ = ['DataFrame']


import warnings
from collections import OrderedDict
from .._py3k_compat import string_types

import pandas as pd


class BaseExpression(object):
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

    # Logical Operators
    # TODO: how to handle bitwise/logical distinction here?
    # should make the semantics match Pandas & reflect accurately in JS

    # def __and__(self, other):
    #     return BinaryExpression('&&', self, other)
    #
    # def __or__(self, other):
    #     return BinaryExpression('||', self, other)
    #
    # def __invert__(self):
    #     return UnaryExpression('!', self)


class UnaryExpression(BaseExpression):
    def __init__(self, op, val):
        self.op = op
        self.val = val

    def __repr__(self):
        return "({op}{val})".format(op=self.op, val=repr(self.val))


class BinaryExpression(BaseExpression):
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return "({lhs}{op}{rhs})".format(op=self.op,
                                         lhs=repr(self.lhs),
                                         rhs=repr(self.rhs))


class FunctionExpression(BaseExpression):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __repr__(self):
        args = ','.join(repr(arg) for arg in self.args)
        return "{name}({args})".format(name=self.name, args=args)


class ConstExpression(BaseExpression):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc
        self.__doc__ = """{0}: {1}""".format(name, doc)

    def __repr__(self):
        return str(self.name)


class Series(BaseExpression):
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
            return self.parent._calculated_columns.get(self.name, None)


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
            self._calculated_columns = data._calculated_columns.copy()
        else:
            self._data = data
            self._cols = self._get_cols(self._data, cols)
            self._calculated_columns = OrderedDict({})

    @classmethod
    def _get_cols(cls, data, cols=None):
        from ... import Data as altair_Data
        if cols is not None:
            return cols
        elif isinstance(data, string_types):
            return None
        elif isinstance(data, pd.DataFrame):
            return list(data.columns)
        elif isinstance(data, altair_Data):
            if hasattr(data, 'values'):
                return list(data.values[0].keys())
            else:
                return None
        else:
            raise ValueError("Unrecognized data type")

    @property
    def _columns(self):
        # return dataframe columns or dict keys or list of names
        if self._cols is None:
            return []
        else:
            return list(iter(self._cols))

    # TODO: add drop() method to remove columns, returning a new object

    def __dir__(self):
        return list(self._columns) + list(self._calculated_columns.keys())

    def __getattr__(self, attr):
        if attr in self._columns or attr in self._calculated_columns:
            return Series(attr, self)
        else:
            raise AttributeError("No attribute {0}".format(attr))

    def __getitem__(self, attr):
        # TODO: add support for attr=list of columns, returning a new object
        if attr in self._columns or attr in self._calculated_columns:
            return Series(attr, self)
        else:
            raise KeyError("No column {0}".format(attr))

    def __setitem__(self, attr, obj):
        if attr in self._columns or attr in self._calculated_columns:
            raise ValueError("Cannot overwrite column '{0}'".format(attr))
        self._calculated_columns[attr] = obj
