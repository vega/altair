__all__ = ['DataFrame']


from collections import OrderedDict


class BaseExpression(object):
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

    def __truediv__(self, other):
        return BinaryExpression("/", self, other)

    def __rtruediv__(self, other):
        return BinaryExpression("/", other, self)

    __div__ = __truediv__

    __rdiv__ = __rtruediv__

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



class UnaryExpression(BaseExpression):
    def __init__(self, op, val):
        self.op = op
        self.val = val

    def __repr__(self):
        return "{op}{val}".format(op=self.op, val=repr(self.val))


class BinaryExpression(BaseExpression):
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return "{lhs}{op}{rhs}".format(op=self.op,
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
    def __init__(self, df=None):
        self._df = df
        self._calculated_columns = OrderedDict({})

    @property
    def _dfcols(self):
        if self._df is None:
            return []
        else:
            return self._df.columns

    def __dir__(self):
        return list(self._dfcols) + list(self._calculated_columns.keys())

    def __getattr__(self, attr):
        if attr in self._dfcols or attr in self._calculated_columns:
            return Series(attr, self)
        else:
            raise AttributeError("No attribute {0}".format(attr))

    def __getitem__(self, attr):
        if attr in self._dfcols or attr in self._calculated_columns:
            return Series(attr, self)
        else:
            raise KeyError("No column {0}".format(attr))

    def __setitem__(self, attr, obj):
        self._calculated_columns[attr] = obj
