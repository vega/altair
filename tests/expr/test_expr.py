from __future__ import annotations

import operator
import sys
from inspect import classify_class_attrs, getmembers, signature
from typing import TYPE_CHECKING, Any, Iterator, cast

import pytest
from jsonschema.exceptions import ValidationError

from altair import datum, expr, ExprRef
from altair.expr import _ConstExpressionType
from altair.expr import dummy as dummy
from altair.expr.core import GetAttrExpression

if TYPE_CHECKING:
    from inspect import Signature
    from typing import Callable, Container

    from altair.expr.core import Expression


# This maps vega expression function names to the Python name
VEGA_REMAP = {"if_": "if"}


def _is_property(obj: Any, /) -> bool:
    return isinstance(obj, property)


def _get_classmethod_names(tp: type[Any], /) -> Iterator[str]:
    for m in classify_class_attrs(tp):
        if m.kind == "class method" and m.defining_class is tp:
            yield m.name


def _remap_classmethod_names(tp: type[Any], /) -> Iterator[tuple[str, str]]:
    for name in _get_classmethod_names(tp):
        yield VEGA_REMAP.get(name, name), name


def _get_property_names(tp: type[Any], /) -> Iterator[str]:
    for nm, _ in getmembers(tp, _is_property):
        yield nm


def signature_n_params(
    sig: Signature, /, *, exclude: Container[str] = frozenset(("cls", "self"))
) -> int:
    return len([p for p in sig.parameters.values() if p.name not in exclude])


def _get_classmethod_members(
    tp: type[Any], /
) -> Iterator[tuple[str, Callable[..., Any]]]:
    for m in classify_class_attrs(tp):
        if m.kind == "class method" and m.defining_class is tp:
            yield m.name, cast("classmethod[Any, Any, Any]", m.object).__func__


def _get_classmethod_signatures(
    tp: type[Any], /
) -> Iterator[tuple[str, Callable[..., Expression], int]]:
    for name, fn in _get_classmethod_members(tp):
        yield (
            VEGA_REMAP.get(name, name),
            fn.__get__(tp),
            signature_n_params(signature(fn)),
        )


@pytest.mark.parametrize(
    ("veganame", "fn", "n_params"), _get_classmethod_signatures(dummy.expr)
)
def test_dummy_expr_funcs(
    veganame: str, fn: Callable[..., Expression], n_params: int
) -> None:
    datum_names = [f"col_{n}" for n in range(n_params)]
    datum_args = ",".join(f"datum.{nm}" for nm in datum_names)

    fn_call = fn(*(GetAttrExpression("datum", nm) for nm in datum_names))
    assert repr(fn_call) == f"{veganame}({datum_args})"


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


@pytest.mark.parametrize(("veganame", "methodname"), _remap_classmethod_names(expr))
def test_expr_funcs(veganame: str, methodname: str):
    """
    Test all functions defined in expr.funcs.

    # FIXME: These tests are no longer suitable
    They only work for functions with a **single** argument:

        TypeError: expr.if_() missing 2 required positional arguments: 'thenValue' and 'elseValue'.
    """
    func = getattr(expr, methodname)
    z = func(datum.xxx)
    assert repr(z) == f"{veganame}(datum.xxx)"


@pytest.mark.parametrize("constname", _get_property_names(_ConstExpressionType))
def test_expr_consts(constname: str):
    """Test all constants defined in expr.consts."""
    const = getattr(expr, constname)
    z = const * datum.xxx
    assert repr(z) == f"({constname} * datum.xxx)"


@pytest.mark.parametrize("constname", _get_property_names(_ConstExpressionType))
def test_expr_consts_immutable(constname: str):
    """Ensure e.g `alt.expr.PI = 2` is prevented."""
    if sys.version_info >= (3, 11):
        pattern = f"property {constname!r}.+has no setter"
    elif sys.version_info >= (3, 10):
        pattern = f"can't set attribute {constname!r}"
    else:
        pattern = "can't set attribute"
    with pytest.raises(AttributeError, match=pattern):
        setattr(expr, constname, 2)


def test_json_reprs():
    """Test JSON representations of special values."""
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
        expr(2 * 2)  # pyright: ignore

    with pytest.raises(ValidationError):
        expr(["foo", "bah"])  # pyright: ignore
