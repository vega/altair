import types
from packaging.version import Version
from importlib.metadata import version as importlib_version

import numpy as np
import pandas as pd
import pytest

import altair as alt
from altair.utils.core import parse_shorthand, update_nested, infer_encoding_types
from altair.utils.core import infer_dtype

json_schema_specification = alt.load_schema()["$schema"]
json_schema_dict_str = f'{{"$schema": "{json_schema_specification}"}}'

try:
    import pyarrow as pa
except ImportError:
    pa = None

PANDAS_VERSION = Version(importlib_version("pandas"))


FAKE_CHANNELS_MODULE = f'''
"""Fake channels module for utility tests."""

from altair.utils import schemapi


class FieldChannel:
    def __init__(self, shorthand, **kwargs):
        kwargs['shorthand'] = shorthand
        return super(FieldChannel, self).__init__(**kwargs)


class ValueChannel:
    def __init__(self, value, **kwargs):
        kwargs['value'] = value
        return super(ValueChannel, self).__init__(**kwargs)


class X(FieldChannel, schemapi.SchemaBase):
    _schema = {json_schema_dict_str}
    _encoding_name = "x"


class XValue(ValueChannel, schemapi.SchemaBase):
    _schema = {json_schema_dict_str}
    _encoding_name = "x"


class Y(FieldChannel, schemapi.SchemaBase):
    _schema = {json_schema_dict_str}
    _encoding_name = "y"


class YValue(ValueChannel, schemapi.SchemaBase):
    _schema = {json_schema_dict_str}
    _encoding_name = "y"


class StrokeWidth(FieldChannel, schemapi.SchemaBase):
    _schema = {json_schema_dict_str}
    _encoding_name = "strokeWidth"


class StrokeWidthValue(ValueChannel, schemapi.SchemaBase):
    _schema = {json_schema_dict_str}
    _encoding_name = "strokeWidth"
'''


@pytest.mark.parametrize(
    ("value", "expected_type"),
    [
        ([1, 2, 3], "integer"),
        ([1.0, 2.0, 3.0], "floating"),
        ([1, 2.0, 3], "mixed-integer-float"),
        (["a", "b", "c"], "string"),
        (["a", "b", np.nan], "mixed"),
    ],
)
def test_infer_dtype(value, expected_type):
    assert infer_dtype(value, skipna=False) == expected_type


def test_parse_shorthand():
    def check(s, **kwargs):
        assert parse_shorthand(s) == kwargs

    check("")

    # Fields alone
    check("foobar", field="foobar")
    check(r"blah\:(fd ", field=r"blah\:(fd ")

    # Fields with type
    check("foobar:quantitative", type="quantitative", field="foobar")
    check("foobar:nominal", type="nominal", field="foobar")
    check("foobar:ordinal", type="ordinal", field="foobar")
    check("foobar:temporal", type="temporal", field="foobar")
    check("foobar:geojson", type="geojson", field="foobar")

    check("foobar:Q", type="quantitative", field="foobar")
    check("foobar:N", type="nominal", field="foobar")
    check("foobar:O", type="ordinal", field="foobar")
    check("foobar:T", type="temporal", field="foobar")
    check("foobar:G", type="geojson", field="foobar")

    # Fields with aggregate and/or type
    check("average(foobar)", field="foobar", aggregate="average")
    check("min(foobar):temporal", type="temporal", field="foobar", aggregate="min")
    check("sum(foobar):Q", type="quantitative", field="foobar", aggregate="sum")

    # check that invalid arguments are not split-out
    check("invalid(blah)", field="invalid(blah)")
    check(r"blah\:invalid", field=r"blah\:invalid")
    check(r"invalid(blah)\:invalid", field=r"invalid(blah)\:invalid")

    # check parsing in presence of strange characters
    check(
        r"average(a b\:(c\nd):Q",
        aggregate="average",
        field=r"a b\:(c\nd",
        type="quantitative",
    )

    # special case: count doesn't need an argument
    check("count()", aggregate="count", type="quantitative")
    check("count():O", aggregate="count", type="ordinal")

    # time units:
    check("month(x)", field="x", timeUnit="month", type="temporal")
    check("year(foo):O", field="foo", timeUnit="year", type="ordinal")
    check("date(date):quantitative", field="date", timeUnit="date", type="quantitative")
    check(
        "yearmonthdate(field)", field="field", timeUnit="yearmonthdate", type="temporal"
    )


@pytest.mark.parametrize("object_dtype", [False, True])
def test_parse_shorthand_with_data(object_dtype):
    def check(s, data, **kwargs):
        assert parse_shorthand(s, data) == kwargs

    data = pd.DataFrame(
        {
            "x": [1, 2, 3, 4, 5],
            "y": ["A", "B", "C", "D", "E"],
            "z": pd.date_range("2018-01-01", periods=5, freq="D"),
            "t": pd.date_range("2018-01-01", periods=5, freq="D").tz_localize("UTC"),
        }
    )

    if object_dtype:
        data = data.astype("object")

    check("x", data, field="x", type="quantitative")
    check("y", data, field="y", type="nominal")
    check("z", data, field="z", type="temporal")
    check("t", data, field="t", type="temporal")
    check("count(x)", data, field="x", aggregate="count", type="quantitative")
    check("count()", data, aggregate="count", type="quantitative")
    check("month(z)", data, timeUnit="month", field="z", type="temporal")
    check("month(t)", data, timeUnit="month", field="t", type="temporal")

    if Version("1.0.0") <= PANDAS_VERSION:
        data["b"] = pd.Series([True, False, True, False, None], dtype="boolean")
        check("b", data, field="b", type="nominal")


@pytest.mark.skipif(pa is None, reason="pyarrow not installed")
def test_parse_shorthand_for_arrow_timestamp():
    data = pd.DataFrame(
        {
            "z": pd.date_range("2018-01-01", periods=5, freq="D"),
            "t": pd.date_range("2018-01-01", periods=5, freq="D").tz_localize("UTC"),
        }
    )
    # Convert to arrow-packed dtypes
    data = pa.Table.from_pandas(data).to_pandas(types_mapper=pd.ArrowDtype)
    assert parse_shorthand("z", data) == {"field": "z", "type": "temporal"}
    assert parse_shorthand("z", data) == {"field": "z", "type": "temporal"}


def test_parse_shorthand_all_aggregates():
    aggregates = alt.Root._schema["definitions"]["AggregateOp"]["enum"]
    for aggregate in aggregates:
        shorthand = f"{aggregate}(field):Q"
        assert parse_shorthand(shorthand) == {
            "aggregate": aggregate,
            "field": "field",
            "type": "quantitative",
        }


def test_parse_shorthand_all_timeunits():
    timeUnits = []
    for loc in ["Local", "Utc"]:
        for typ in ["Single", "Multi"]:
            defn = loc + typ + "TimeUnit"
            timeUnits.extend(alt.Root._schema["definitions"][defn]["enum"])
    for timeUnit in timeUnits:
        shorthand = f"{timeUnit}(field):Q"
        assert parse_shorthand(shorthand) == {
            "timeUnit": timeUnit,
            "field": "field",
            "type": "quantitative",
        }


def test_parse_shorthand_window_count():
    shorthand = "count()"
    dct = parse_shorthand(
        shorthand,
        parse_aggregates=False,
        parse_window_ops=True,
        parse_timeunits=False,
        parse_types=False,
    )
    assert dct == {"op": "count"}


def test_parse_shorthand_all_window_ops():
    window_ops = alt.Root._schema["definitions"]["WindowOnlyOp"]["enum"]
    aggregates = alt.Root._schema["definitions"]["AggregateOp"]["enum"]
    for op in window_ops + aggregates:
        shorthand = f"{op}(field)"
        dct = parse_shorthand(
            shorthand,
            parse_aggregates=False,
            parse_window_ops=True,
            parse_timeunits=False,
            parse_types=False,
        )
        assert dct == {"field": "field", "op": op}


def test_update_nested():
    original = {"x": {"b": {"foo": 2}, "c": 4}}
    update = {"x": {"b": {"foo": 5}, "d": 6}, "y": 40}

    output = update_nested(original, update, copy=True)
    assert output is not original
    assert output == {"x": {"b": {"foo": 5}, "c": 4, "d": 6}, "y": 40}

    output2 = update_nested(original, update)
    assert output2 is original
    assert output == output2


@pytest.fixture
def channels():
    channels = types.ModuleType("channels")
    exec(FAKE_CHANNELS_MODULE, channels.__dict__)
    return channels


def _getargs(*args, **kwargs):
    return args, kwargs


# NOTE: Dependent on a no longer needed implementation detail
def test_infer_encoding_types(channels):
    expected = {
        "x": channels.X("xval"),
        "y": channels.YValue("yval"),
        "strokeWidth": channels.StrokeWidthValue(value=4),
    }

    # All positional args
    args, kwds = _getargs(
        channels.X("xval"), channels.YValue("yval"), channels.StrokeWidthValue(4)
    )
    assert infer_encoding_types(args, kwds, channels) == expected

    # All keyword args
    args, kwds = _getargs(x="xval", y=alt.value("yval"), strokeWidth=alt.value(4))
    assert infer_encoding_types(args, kwds, channels) == expected

    # Mixed positional & keyword
    args, kwds = _getargs(
        channels.X("xval"), channels.YValue("yval"), strokeWidth=alt.value(4)
    )
    assert infer_encoding_types(args, kwds, channels) == expected


def test_infer_encoding_types_with_condition():
    args, kwds = _getargs(
        size=alt.condition("pred1", alt.value(1), alt.value(2)),
        color=alt.condition("pred2", alt.value("red"), "cfield:N"),
        opacity=alt.condition("pred3", "ofield:N", alt.value(0.2)),
    )

    expected = {
        "size": alt.SizeValue(
            2,
            condition=alt.ConditionalPredicateValueDefnumberExprRef(
                value=1, test=alt.Predicate("pred1")
            ),
        ),
        "color": alt.Color(
            "cfield:N",
            condition=alt.ConditionalPredicateValueDefGradientstringnullExprRef(
                value="red", test=alt.Predicate("pred2")
            ),
        ),
        "opacity": alt.OpacityValue(
            0.2,
            condition=alt.ConditionalPredicateMarkPropFieldOrDatumDef(
                field=alt.FieldName("ofield"),
                test=alt.Predicate("pred3"),
                type=alt.StandardType("nominal"),
            ),
        ),
    }
    assert infer_encoding_types(args, kwds) == expected


def test_invalid_data_type():
    with pytest.raises(
        ValueError, match=r'"\(fd " is not one of the valid encoding data types'
    ):
        parse_shorthand(r"blah:(fd ")
