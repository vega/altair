import operator

import pytest

from altair import expr
from altair import datum
from altair import ExprRef
from jsonschema.exceptions import ValidationError


def test_unary_operations():
    OP_MAP = {"-": operator.neg, "+": operator.pos}
    for op, func in OP_MAP.items():
        z = func(datum.xxx)
        assert repr(z) == "({}datum.xxx)".format(op)


def test_binary_operations():
    OP_MAP = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "===": operator.eq,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
        "!==": operator.ne,
        "&&": operator.and_,
        "||": operator.or_,
    }
    # When these are on the RHS, the opposite is evaluated instead.
    INEQ_REVERSE = {
        ">": "<",
        "<": ">",
        "<=": ">=",
        ">=": "<=",
        "===": "===",
        "!==": "!==",
    }
    for op, func in OP_MAP.items():
        z1 = func(datum.xxx, 2)
        assert repr(z1) == "(datum.xxx {} 2)".format(op)

        z2 = func(2, datum.xxx)
        if op in INEQ_REVERSE:
            assert repr(z2) == "(datum.xxx {} 2)".format(INEQ_REVERSE[op])
        else:
            assert repr(z2) == "(2 {} datum.xxx)".format(op)

        z3 = func(datum.xxx, datum.yyy)
        assert repr(z3) == "(datum.xxx {} datum.yyy)".format(op)


def test_abs():
    z = abs(datum.xxx)
    assert repr(z) == "abs(datum.xxx)"


def test_expr_funcs():
    """test all functions defined in expr.funcs"""
    from altair.expr.funcs import NAME_MAP
    from altair.expr.funcs import FUNCTION_LISTING

    _map = {vname: (NAME_MAP.get(vname, vname)) for vname in FUNCTION_LISTING}
    for veganame, methodname in _map.items():
        func = getattr(expr, methodname)
        z = func(datum.xxx)
        assert repr(z) == "{}(datum.xxx)".format(veganame)


def test_expr_consts():
    """Test all constants defined in expr.consts"""
    from altair.expr.consts import CONST_LISTING

    for constname in CONST_LISTING:
        const = getattr(expr, constname)
        z = const * datum.xxx
        assert repr(z) == "({} * datum.xxx)".format(constname)


def test_json_reprs():
    """Test JSON representations of special values"""
    assert repr(datum.xxx == None) == "(datum.xxx === null)"  # noqa: E711
    assert repr(datum.xxx == False) == "(datum.xxx === false)"  # noqa: E712
    assert repr(datum.xxx == True) == "(datum.xxx === true)"  # noqa: E712


def test_to_dict():
    ex = datum.xxx * 2 > datum.yyy
    assert ex.to_dict() == repr(ex)


def test_copy():
    ex = datum.xxx * 2 > abs(datum.yyy)
    ex_copy = ex.copy()
    assert ex.to_dict() == ex_copy.to_dict()


def test_datum_getattr():
    x = datum["foo"]
    assert repr(x) == "datum['foo']"

    magic_attr = "__magic__"
    with pytest.raises(AttributeError):
        getattr(datum, magic_attr)


def test_expression_getitem():
    x = datum.foo[0]
    assert repr(x) == "datum.foo[0]"


def test_expression_function_expr():
    # test including a expr.<CONSTANT> should return an ExprRef
    er = expr(expr.PI * 2)
    assert isinstance(er, ExprRef)
    assert repr(er) == "ExprRef({\n  expr: (PI * 2)\n})"


def test_expression_function_string():
    # expr() can only work with str
    er = expr("2 * 2")
    assert isinstance(er, ExprRef)
    assert repr(er) == "ExprRef({\n  expr: '2 * 2'\n})"


def test_expression_function_nostring():
    # expr() can only work with str otherwise
    # should raise a SchemaValidationError
    with pytest.raises(ValidationError):
        expr(2 * 2)

    with pytest.raises(ValidationError):
        expr(["foo", "bah"])
