from __future__ import division

import operator

import pytest

import pandas as pd

from ... import expr


@pytest.fixture
def data():
    return pd.DataFrame({'xxx': [1, 2, 3],
                         'yyy': [4, 5, 6],
                         'zzz': [7, 8, 9]})

def test_dataframe_namespace(data):
    df = expr.DataFrame(data)
    assert set(dir(df)) == set(iter(data))

    df = expr.DataFrame(data, cols=['x'])
    assert set(dir(df)) == {'x'}

    df = expr.DataFrame('http://url.com/path/to/data.json')
    assert dir(df) == []

    df = expr.DataFrame('http://url.com/path/to/data.json',
                        cols=['a', 'b', 'c'])
    assert set(dir(df)) == {'a', 'b', 'c'}


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
              '!=': operator.ne, '&&': operator.and_,
              '||': operator.or_}
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


def test_abs(data):
    df = expr.DataFrame(data)
    z = abs(df.xxx)
    assert repr(z) == 'abs(datum.xxx)'


def test_expr_funcs(data):
    """test all functions defined in expr.funcs"""
    df = expr.DataFrame(data)
    name_map = {val:key for key, val in expr.funcs.NAME_MAP.items()}
    for funcname in expr.funcs.__all__:
        func = getattr(expr, funcname)
        z = func(df.xxx)
        assert repr(z) == '{0}(datum.xxx)'.format(name_map.get(funcname,
                                                               funcname))


def test_expr_consts(data):
    """Test all constants defined in expr.consts"""
    df = expr.DataFrame(data)
    name_map = {val:key for key, val in expr.consts.NAME_MAP.items()}
    for constname in expr.consts.__all__:
        const = getattr(expr, constname)
        z = const * df.xxx
        assert repr(z) == '({0}*datum.xxx)'.format(name_map.get(constname,
                                                                constname))


def test_getitem_list(data):
    """Test getting a sub-dataframe"""
    df = expr.DataFrame(data)
    df['calculated'] = df.xxx + df.yyy + df.zzz

    # df2 should have a subset of df's values
    df2 = df[['xxx', 'yyy', 'calculated']]
    assert set(dir(df2)) == {'xxx', 'yyy', 'calculated'}

    # changing df2 shouldn't affect df1
    df2['qqq'] = df2.xxx // df2.yyy
    assert set(dir(df2)) == {'xxx', 'yyy', 'calculated', 'qqq'}
    assert set(dir(df)) == {'xxx', 'yyy', 'zzz', 'calculated'}


def test_json_reprs(data):
    df = expr.DataFrame(data)

    assert repr(df.xxx == None) == '(datum.xxx==null)'
    assert repr(df.xxx == False) == '(datum.xxx==false)'
    assert repr(df.xxx == True) == '(datum.xxx==true)'
