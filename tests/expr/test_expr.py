from __future__ import annotations

import datetime as dt
import operator
import sys
from inspect import classify_class_attrs, getmembers, signature
from typing import TYPE_CHECKING, Any, TypeVar, cast

import numpy as np
import pytest
from jsonschema.exceptions import ValidationError

from altair import datum, expr, ExprRef
from altair.expr import _ExprMeta
from altair.expr.core import Expression, GetAttrExpression

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator
    from inspect import _IntrospectableCallable

T = TypeVar("T")

# This maps vega expression function names to the Python name
VEGA_REMAP = {"if_": "if"}


def _is_property(obj: Any, /) -> bool:
    return isinstance(obj, property)


def _get_property_names(tp: type[Any], /) -> Iterator[str]:
    for nm, _ in getmembers(tp, _is_property):
        yield nm


def signature_n_params(
    obj: _IntrospectableCallable,
    /,
    *,
    exclude: Iterable[str] = frozenset(("cls", "self")),
) -> int:
    sig = signature(obj)
    return len(set(sig.parameters).difference(exclude))


def _iter_classmethod_specs(
    tp: type[T], /
) -> Iterator[tuple[str, Callable[..., Expression], int]]:
    for m in classify_class_attrs(tp):
        if m.kind == "class method" and m.defining_class is tp:
            name = m.name
            fn = cast("classmethod[T, ..., Expression]", m.object).__func__
            yield (VEGA_REMAP.get(name, name), fn.__get__(tp), signature_n_params(fn))


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


@pytest.mark.parametrize(("veganame", "fn", "n_params"), _iter_classmethod_specs(expr))
def test_expr_methods(
    veganame: str, fn: Callable[..., Expression], n_params: int
) -> None:
    datum_names = [f"col_{n}" for n in range(n_params)]
    datum_args = ",".join(f"datum.{nm}" for nm in datum_names)

    fn_call = fn(*(GetAttrExpression("datum", nm) for nm in datum_names))
    assert repr(fn_call) == f"{veganame}({datum_args})"


@pytest.mark.parametrize("constname", _get_property_names(_ExprMeta))
def test_expr_consts(constname: str):
    """Test all constants defined in expr.consts."""
    const = getattr(expr, constname)
    z = const * datum.xxx
    assert repr(z) == f"({constname} * datum.xxx)"


@pytest.mark.parametrize("constname", _get_property_names(_ExprMeta))
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
    assert repr(datum.xxx == np.int64(0)) == "(datum.xxx === 0)"


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


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (dt.date(2000, 1, 1), "datetime(2000,0,1)"),
        (dt.datetime(2000, 1, 1), "datetime(2000,0,1,0,0,0,0)"),
        (dt.datetime(2001, 1, 1, 9, 30, 0, 2999), "datetime(2001,0,1,9,30,0,2)"),
        (
            dt.datetime(2003, 5, 1, 1, 30, tzinfo=dt.timezone.utc),
            "utc(2003,4,1,1,30,0,0)",
        ),
    ],
    ids=["date", "datetime (no time)", "datetime (microseconds)", "datetime (UTC)"],
)
def test_expr_datetime(value: Any, expected: str) -> None:
    r_datum = datum.date >= value
    assert isinstance(r_datum, Expression)
    assert repr(r_datum) == f"(datum.date >= {expected})"


@pytest.mark.parametrize(
    "tzinfo",
    [
        dt.timezone(dt.timedelta(hours=2), "UTC+2"),
        dt.timezone(dt.timedelta(hours=1), "BST"),
        dt.timezone(dt.timedelta(hours=-7), "pdt"),
        dt.timezone(dt.timedelta(hours=-3), "BRT"),
        dt.timezone(dt.timedelta(hours=9), "UTC"),
        dt.timezone(dt.timedelta(minutes=60), "utc"),
    ],
)
def test_expr_datetime_unsupported_timezone(tzinfo: dt.timezone) -> None:
    datetime = dt.datetime(2003, 5, 1, 1, 30)

    result = datum.date == datetime
    assert repr(result) == "(datum.date === datetime(2003,4,1,1,30,0,0))"

    with pytest.raises(TypeError, match=r"Unsupported timezone.+\n.+UTC.+local"):
        datum.date == datetime.replace(tzinfo=tzinfo)  # noqa: B015
