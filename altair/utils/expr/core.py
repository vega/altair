__all__ = ['DataFrame']


import warnings
from collections import OrderedDict


# List of functions which should become methods of the dataframe wrapper.
# Note that numpy ufuncs will point to the appropriately named method
METHOD_MAP = {
    '__abs__': 'abs',
    #'isfinite': 'isFinite',
    #'isnan': 'isNaN',
    'cos': 'cos',
    'sin': 'sin',
    'tan': 'tan',
    'arccos': 'acos',
    'arcsin': 'asin',
    'arctan': 'atan',
    'log': 'log',
    'sqrt': 'sqrt',
    'round': 'round',
    'ceil': 'ceil',
    'floor': 'floor',
    'exp': 'exp',
    # binary ufuncs seem not to work
    #'arctan2': 'atan2',
    #'minimum': 'min',
    #'maximum': 'max',
    #'power': 'pow',
}


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

    def __neq__(self, other):
        return BinaryExpression("!=", self, other)

    def __gt__(self, other):
        return BinaryExpression(">", self, other)

    def __lt__(self, other):
        return BinaryExpression("<", self, other)

    def __ge__(self, other):
        return BinaryExpression(">=", self, other)

    def __le__(self, other):
        return BinaryExpression("<=", self, other)

    # TODO: how to handle assignment? Overwriting would be an issue...

    # Logical Operators
    # TODO: how to handle bitwise/logical distinction here?
    # should make the semantics match Pandas.

    # def __and__(self, other):
    #     return BinaryExpression('&&', self, other)
    #
    # def __or__(self, other):
    #     return BinaryExpression('||', self, other)
    #
    # def __invert__(self):
    #     return UnaryExpression('!', self)



# Add methods to enable ufunc support.
# Should we do something like this instead?
#
# for npfunc in _ufuncs_with_fixed_point_at_zero:
#     name = npfunc.__name__
#
#     def _create_method(op):
#         def method(self):
#             result = op(self.data)
#             x = self._with_data(result, copy=True)
#             return x
#
#         method.__doc__ = ("Element-wise %s.\n\n"
#                           "See numpy.%s for more information." % (name, name))
#         method.__name__ = name
#
#         return method
#
#     setattr(_data_matrix, name, _create_method(npfunc))
#


for (pymethod, jsfunc) in METHOD_MAP.items():
    func = """def {pymethod}(self, *args):
    if any(args):
        raise ValueError("additional ufunc args not valid")
    return FunctionExpression('{jsfunc}', self)
    """.format(pymethod=pymethod, jsfunc=jsfunc)
    exec(func)
    setattr(BaseExpression, pymethod, locals()[pymethod])


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
    df : DataFrame or dict or iterable
        Object specifying the valid column names in the dataframe. Names can
        be DataFrame columns, dict keys, or items returned by an iterable.
    """
    def __init__(self, cols=None):
        self._cols = cols
        self._calculated_columns = OrderedDict({})

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
