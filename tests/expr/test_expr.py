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
        assert repr(z) == f"({op}datum.xxx)"


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
        assert repr(z1) == f"(datum.xxx {op} 2)"

        z2 = func(2, datum.xxx)
        if op in INEQ_REVERSE:
            assert repr(z2) == f"(datum.xxx {INEQ_REVERSE[op]} 2)"
        else:
            assert repr(z2) == f"(2 {op} datum.xxx)"

        z3 = func(datum.xxx, datum.yyy)
        assert repr(z3) == f"(datum.xxx {op} datum.yyy)"


def test_abs():
    z = abs(datum.xxx)
    assert repr(z) == "abs(datum.xxx)"


def test_expr_funcs():
    """test all functions defined in expr.funcs"""
    name_map = {val: key for key, val in expr.funcs.NAME_MAP.items()}
    for funcname in expr.funcs.__all__:
        func = getattr(expr, funcname)
        z = func(datum.xxx)
        assert repr(z) == f"{name_map.get(funcname, funcname)}(datum.xxx)"


def test_expr_consts():
    """Test all constants defined in expr.consts"""
    name_map = {val: key for key, val in expr.consts.NAME_MAP.items()}
    for constname in expr.consts.__all__:
        const = getattr(expr, constname)
        z = const * datum.xxx
        assert repr(z) == f"({name_map.get(constname, constname)} * datum.xxx)"


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
