from __future__ import division

import operator

import pytest

import numpy as np

from ... import expr


@pytest.fixture
def data():
    return ['xxx', 'yyy', 'zzz']


def test_dataframe_namespace(data):
    df = expr.DataFrame(data)
    assert set(dir(df)) == set(iter(data))


def test_dataframe_newcols(data):
    df = expr.DataFrame(data)
    df['sum'] = df.xxx + df.yyy + df.zzz
    df['prod'] = df.xxx * df.yyy * df.zzz
    assert set(dir(df)) == set.union({'sum', 'prod'}, set(iter(data)))
    assert repr(df.sum.contents) == '((datum.xxx+datum.yyy)+datum.zzz)'
    assert repr(df.prod.contents) == '((datum.xxx*datum.yyy)*datum.zzz)'


def test_unary_operations(data):
    df = expr.DataFrame(data)
    OP_MAP = {'-': operator.neg, '+': operator.pos}
    for op, func in OP_MAP.items():
        z = func(df.xxx)
        assert repr(z) == '({0}datum.xxx)'.format(op)


def test_binary_operations(data):
    df = expr.DataFrame(data)
    OP_MAP = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv,
              '%': operator.mod, '==': operator.eq,
              '<': operator.lt, '<=': operator.le,
              '>': operator.gt, '>=': operator.ge,
              '!=': operator.ne}
    # When these are on the RHS, the opposite is evaluated instead.
    INEQ_REVERSE = {'>':'<', '<': '>',
                    '<=':'>=', '>=':'<=',
                    '==':'==', '!=':'!='}
    for op, func in OP_MAP.items():
        z1 = func(df.xxx, 2)
        assert repr(z1) == '(datum.xxx{0}2)'.format(op)

        z2 = func(2, df.xxx)
        if op in INEQ_REVERSE:
            assert repr(z2) == '(datum.xxx{0}2)'.format(INEQ_REVERSE[op])
        else:
            assert repr(z2) == '(2{0}datum.xxx)'.format(op)

        z3 = func(df.xxx, df.yyy)
        assert repr(z3) == '(datum.xxx{0}datum.yyy)'.format(op)


def test_expr_ufuncs(data):
    """test numpy ufuncs"""
    df = expr.DataFrame(data)
    from ..core import METHOD_MAP
    for pyfunc, jsfunc in METHOD_MAP.items():
        if pyfunc == '__abs__':
            pyfunc = 'abs'
        func = getattr(np, pyfunc)
        z = func(df.xxx)
        assert repr(z) == '{0}(datum.xxx)'.format(jsfunc)


def test_expr_funcs(data):
    """test all functions defined in expr.funcs"""
    df = expr.DataFrame(data)
    for funcname in expr.funcs.__all__:
        func = getattr(expr, funcname)
        z = func(df.xxx)
        assert repr(z) == '{0}(datum.xxx)'.format(funcname)


def test_expr_consts(data):
    """Test all constants defined in expr.consts"""
    df = expr.DataFrame(data)
    for constname in expr.consts.__all__:
        const = getattr(expr, constname)
        z = const * df.xxx
        assert repr(z) == '({0}*datum.xxx)'.format(constname)
