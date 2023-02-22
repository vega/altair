"""Tools for creating transform & filter expressions with a python syntax"""
# flake8: noqa
from .core import datum, Expression
from .funcs import *
from .consts import *
from ..vegalite.v5.schema.core import ExprRef as _ExprRef


class _ExprType:
    def __init__(self, expr):
        vars(self).update(expr)

    def __call__(self, expr, **kwargs):
        return _ExprRef(expr, **kwargs)


expr = _ExprType(globals())
