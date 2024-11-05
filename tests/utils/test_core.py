from __future__ import annotations

import types
from importlib.metadata import version as importlib_version
from typing import Any

import numpy as np
import pandas as pd
import pytest
from packaging.version import Version
from pandas.api.types import infer_dtype

import altair as alt
from altair.utils import core
from altair.utils.core import infer_encoding_types, parse_shorthand, update_nested
from tests import skip_requires_pyarrow

json_schema_specification = alt.load_schema()["$schema"]
json_schema_dict_str = f'{{"$schema": "{json_schema_specification}"}}'


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


@pytest.fixture(params=[False, True])
def pd_data(request) -> pd.DataFrame:
    data = pd.DataFrame(
        {
            "x": [1, 2, 3, 4, 5],
            "y": ["A", "B", "C", "D", "E"],
            "z": pd.date_range("2018-01-01", periods=5, freq="D"),
            "t": pd.date_range("2018-01-01", periods=5, freq="D").tz_localize("UTC"),
        }
    )
    object_dtype = request.param
    if object_dtype:
        data = data.astype("object")
    return data


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


# ruff: noqa: C408


@pytest.mark.parametrize(
    ("shorthand", "expected"),
    [
        ("", {}),
        # Fields alone
        ("foobar", dict(field="foobar")),
        (r"blah\:(fd ", dict(field=r"blah\:(fd ")),
        # Fields with type
        ("foobar:quantitative", dict(type="quantitative", field="foobar")),
        ("foobar:nominal", dict(type="nominal", field="foobar")),
        ("foobar:ordinal", dict(type="ordinal", field="foobar")),
        ("foobar:temporal", dict(type="temporal", field="foobar")),
        ("foobar:geojson", dict(type="geojson", field="foobar")),
        ("foobar:Q", dict(type="quantitative", field="foobar")),
        ("foobar:N", dict(type="nominal", field="foobar")),
        ("foobar:O", dict(type="ordinal", field="foobar")),
        ("foobar:T", dict(type="temporal", field="foobar")),
        ("foobar:G", dict(type="geojson", field="foobar")),
        # Fields with aggregate and/or type
        ("average(foobar)", dict(field="foobar", aggregate="average")),
        (
            "min(foobar):temporal",
            dict(type="temporal", field="foobar", aggregate="min"),
        ),
        ("sum(foobar):Q", dict(type="quantitative", field="foobar", aggregate="sum")),
        # check that invalid arguments are not split-out
        ("invalid(blah)", dict(field="invalid(blah)")),
        (r"blah\:invalid", dict(field=r"blah\:invalid")),
        (r"invalid(blah)\:invalid", dict(field=r"invalid(blah)\:invalid")),
        # check parsing in presence of strange characters
        (
            r"average(a b\:(c\nd):Q",
            dict(aggregate="average", field=r"a b\:(c\nd", type="quantitative"),
        ),
        # special case: count doesn't need an argument
        ("count()", dict(aggregate="count", type="quantitative")),
        ("count():O", dict(aggregate="count", type="ordinal")),
        # time units:
        ("month(x)", dict(field="x", timeUnit="month", type="temporal")),
        ("year(foo):O", dict(field="foo", timeUnit="year", type="ordinal")),
        (
            "date(date):quantitative",
            dict(field="date", timeUnit="date", type="quantitative"),
        ),
        (
            "yearmonthdate(field)",
            dict(field="field", timeUnit="yearmonthdate", type="temporal"),
        ),
    ],
)
def test_parse_shorthand(shorthand: str, expected: dict[str, Any]) -> None:
    assert parse_shorthand(shorthand) == expected


@pytest.mark.parametrize(
    ("shorthand", "expected"),
    [
        ("x", dict(field="x", type="quantitative")),
        ("y", dict(field="y", type="nominal")),
        ("z", dict(field="z", type="temporal")),
        ("t", dict(field="t", type="temporal")),
        ("count(x)", dict(field="x", aggregate="count", type="quantitative")),
        ("count()", dict(aggregate="count", type="quantitative")),
        ("month(z)", dict(timeUnit="month", field="z", type="temporal")),
        ("month(t)", dict(timeUnit="month", field="t", type="temporal")),
    ],
)
def test_parse_shorthand_with_data(
    pd_data, shorthand: str, expected: dict[str, Any]
) -> None:
    assert parse_shorthand(shorthand, pd_data) == expected


@pytest.mark.skipif(Version("1.0.0") > PANDAS_VERSION, reason="dtype unavailable")
def test_parse_shorthand_with_data_pandas_v1(pd_data) -> None:
    pd_data["b"] = pd.Series([True, False, True, False, None], dtype="boolean")
    shorthand = "b"
    expected = dict(field="b", type="nominal")
    assert parse_shorthand(shorthand, pd_data) == expected


@skip_requires_pyarrow
def test_parse_shorthand_for_arrow_timestamp():
    import pyarrow as pa

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
def channels() -> types.ModuleType:
    channels = types.ModuleType("channels")
    exec(FAKE_CHANNELS_MODULE, channels.__dict__)
    return channels


@pytest.fixture
def channels_cached(channels) -> core._ChannelCache:
    """Previously ``_ChannelCache.from_channels``."""
    cached = core._ChannelCache.__new__(core._ChannelCache)
    cached.channel_to_name = {
        c: c._encoding_name  # pyright: ignore[reportAttributeAccessIssue]
        for c in channels.__dict__.values()
        if isinstance(c, type)
        and issubclass(c, alt.SchemaBase)
        and hasattr(c, "_encoding_name")
    }
    cached.name_to_channel = core._invert_group_channels(cached.channel_to_name)
    return cached


def _getargs(*args, **kwargs):
    return args, kwargs


def test_infer_encoding_types(
    monkeypatch: pytest.MonkeyPatch, channels, channels_cached
):
    # Indirectly initialize `_CHANNEL_CACHE`
    infer_encoding_types((), {})
    # Replace with contents of `FAKE_CHANNELS_MODULE`
    # Scoped to only this test
    monkeypatch.setattr(core, "_CHANNEL_CACHE", channels_cached)

    expected = {
        "x": channels.X("xval"),
        "y": channels.YValue("yval"),
        "strokeWidth": channels.StrokeWidthValue(value=4),
    }

    # All positional args
    args, kwds = _getargs(
        channels.X("xval"), channels.YValue("yval"), channels.StrokeWidthValue(4)
    )
    assert infer_encoding_types(args, kwds) == expected

    # All keyword args
    args, kwds = _getargs(x="xval", y=alt.value("yval"), strokeWidth=alt.value(4))
    assert infer_encoding_types(args, kwds) == expected

    # Mixed positional & keyword
    args, kwds = _getargs(
        channels.X("xval"), channels.YValue("yval"), strokeWidth=alt.value(4)
    )
    assert infer_encoding_types(args, kwds) == expected


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
            field=alt.FieldName("cfield"),
            type=alt.StandardType("nominal"),
            condition=alt.ConditionalPredicateValueDefGradientstringnullExprRef(
                value="red",
                test=alt.Predicate("pred2"),
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
