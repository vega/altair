# ruff: noqa: W291
from __future__ import annotations

import copy
import datetime as dt
import inspect
import io
import json
import pickle
import re
import types
import warnings
from collections import deque
from functools import partial
from typing import TYPE_CHECKING, Any

import jsonschema
import jsonschema.exceptions
import numpy as np
import pandas as pd
import polars as pl
import pytest

import altair as alt
from altair import load_schema
from altair.utils.schemapi import (
    _DEFAULT_JSON_SCHEMA_DRAFT_URL,
    SchemaBase,
    SchemaValidationError,
    Undefined,
    UndefinedType,
    _FromDict,
)
from altair.vegalite.v5.schema.channels import X
from altair.vegalite.v5.schema.core import FieldOneOfPredicate, Legend
from vega_datasets import data

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Sequence

    from narwhals.stable.v1.typing import IntoDataFrame

_JSON_SCHEMA_DRAFT_URL = load_schema()["$schema"]
# Make tests inherit from _TestSchema, so that when we test from_dict it won't
# try to use SchemaBase objects defined elsewhere as wrappers.


def test_actual_json_schema_draft_is_same_as_hardcoded_default():
    # See comments next to definition of _DEFAULT_JSON_SCHEMA_DRAFT_URL
    # for details why we need this test
    assert _DEFAULT_JSON_SCHEMA_DRAFT_URL == _JSON_SCHEMA_DRAFT_URL, (
        "The default json schema URL, which is hardcoded,"
        + " is not the same as the one used in the Vega-Lite schema."
        + " You need to update the default value."
    )


class _TestSchema(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return _TestSchema.__subclasses__()


class MySchema(_TestSchema):
    _schema = {
        "$schema": _JSON_SCHEMA_DRAFT_URL,
        "definitions": {
            "StringMapping": {
                "type": "object",
                "additionalProperties": {"type": "string"},
            },
            "StringArray": {"type": "array", "items": {"type": "string"}},
        },
        "properties": {
            "a": {"$ref": "#/definitions/StringMapping"},
            "a2": {"type": "object", "additionalProperties": {"type": "number"}},
            "b": {"$ref": "#/definitions/StringArray"},
            "b2": {"type": "array", "items": {"type": "number"}},
            "c": {"type": ["string", "number"]},
            "d": {
                "anyOf": [
                    {"$ref": "#/definitions/StringMapping"},
                    {"$ref": "#/definitions/StringArray"},
                ]
            },
            "e": {"items": [{"type": "string"}, {"type": "string"}]},
        },
    }


class StringMapping(_TestSchema):
    _schema = {"$ref": "#/definitions/StringMapping"}
    _rootschema = MySchema._schema


class StringArray(_TestSchema):
    _schema = {"$ref": "#/definitions/StringArray"}
    _rootschema = MySchema._schema


class Derived(_TestSchema):
    _schema = {
        "$schema": _JSON_SCHEMA_DRAFT_URL,
        "definitions": {
            "Foo": {"type": "object", "properties": {"d": {"type": "string"}}},
            "Bar": {"type": "string", "enum": ["A", "B"]},
        },
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "a": {"type": "integer"},
            "b": {"type": "string"},
            "c": {"$ref": "#/definitions/Foo"},
        },
    }


class Foo(_TestSchema):
    _schema = {"$ref": "#/definitions/Foo"}
    _rootschema = Derived._schema


class Bar(_TestSchema):
    _schema = {"$ref": "#/definitions/Bar"}
    _rootschema = Derived._schema


class SimpleUnion(_TestSchema):
    _schema = {
        "$schema": _JSON_SCHEMA_DRAFT_URL,
        "anyOf": [{"type": "integer"}, {"type": "string"}],
    }


class DefinitionUnion(_TestSchema):
    _schema = {"anyOf": [{"$ref": "#/definitions/Foo"}, {"$ref": "#/definitions/Bar"}]}
    _rootschema = Derived._schema


class SimpleArray(_TestSchema):
    _schema = {
        "$schema": _JSON_SCHEMA_DRAFT_URL,
        "type": "array",
        "items": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
    }


class InvalidProperties(_TestSchema):
    _schema = {
        "$schema": _JSON_SCHEMA_DRAFT_URL,
        "type": "object",
        "properties": {"for": {}, "as": {}, "vega-lite": {}, "$schema": {}},
    }


_validation_selection_schema = {
    "properties": {
        "e": {"type": "number", "exclusiveMinimum": 10},
    },
}


class Draft4Schema(_TestSchema):
    _schema = {
        **_validation_selection_schema,
        "$schema": "http://json-schema.org/draft-04/schema#",
    }


class Draft6Schema(_TestSchema):
    _schema = {
        **_validation_selection_schema,
        "$schema": "http://json-schema.org/draft-06/schema#",
    }


def test_construct_multifaceted_schema():
    dct = {
        "a": {"foo": "bar"},
        "a2": {"foo": 42},
        "b": ["a", "b", "c"],
        "b2": [1, 2, 3],
        "c": 42,
        "d": ["x", "y", "z"],
        "e": ["a", "b"],
    }

    myschema = MySchema.from_dict(dct)
    assert myschema.to_dict() == dct

    myschema2 = MySchema(**dct)
    assert myschema2.to_dict() == dct

    assert isinstance(myschema.a, StringMapping)
    assert isinstance(myschema.a2, dict)
    assert isinstance(myschema.b, StringArray)
    assert isinstance(myschema.b2, list)
    assert isinstance(myschema.d, StringArray)


def test_schema_cases():
    assert Derived(a=4, b="yo").to_dict() == {"a": 4, "b": "yo"}
    assert Derived(a=4, c={"d": "hey"}).to_dict() == {"a": 4, "c": {"d": "hey"}}
    assert Derived(a=4, b="5", c=Foo(d="val")).to_dict() == {
        "a": 4,
        "b": "5",
        "c": {"d": "val"},
    }
    assert Foo(d="hello", f=4).to_dict() == {"d": "hello", "f": 4}

    assert Derived().to_dict() == {}
    assert Foo().to_dict() == {}

    with pytest.raises(jsonschema.ValidationError):
        # a needs to be an integer
        Derived(a="yo").to_dict()

    with pytest.raises(jsonschema.ValidationError):
        # Foo.d needs to be a string
        Derived(c=Foo(4)).to_dict()

    with pytest.raises(jsonschema.ValidationError):
        # no additional properties allowed
        Derived(foo="bar").to_dict()


def test_round_trip():
    D = {"a": 4, "b": "yo"}
    assert Derived.from_dict(D).to_dict() == D

    D = {"a": 4, "c": {"d": "hey"}}
    assert Derived.from_dict(D).to_dict() == D

    D = {"a": 4, "b": "5", "c": {"d": "val"}}
    assert Derived.from_dict(D).to_dict() == D

    D = {"d": "hello", "f": 4}
    assert Foo.from_dict(D).to_dict() == D


def test_from_dict():
    D = {"a": 4, "b": "5", "c": {"d": "val"}}
    obj = Derived.from_dict(D)
    assert obj.a == 4
    assert obj.b == "5"
    assert isinstance(obj.c, Foo)


def test_simple_type():
    assert SimpleUnion(4).to_dict() == 4


def test_simple_array():
    assert SimpleArray([4, 5, "six"]).to_dict() == [4, 5, "six"]
    assert SimpleArray.from_dict(list("abc")).to_dict() == list("abc")  # pyright: ignore[reportArgumentType]


def test_definition_union():
    obj = DefinitionUnion.from_dict("A")  # pyright: ignore[reportArgumentType]
    assert isinstance(obj, Bar)
    assert obj.to_dict() == "A"

    obj = DefinitionUnion.from_dict("B")  # pyright: ignore[reportArgumentType]
    assert isinstance(obj, Bar)
    assert obj.to_dict() == "B"

    obj = DefinitionUnion.from_dict({"d": "yo"})
    assert isinstance(obj, Foo)
    assert obj.to_dict() == {"d": "yo"}


def test_invalid_properties():
    dct = {"for": 2, "as": 3, "vega-lite": 4, "$schema": 5}
    invalid = InvalidProperties.from_dict(dct)
    assert invalid["for"] == 2
    assert invalid["as"] == 3
    assert invalid["vega-lite"] == 4
    assert invalid["$schema"] == 5
    assert invalid.to_dict() == dct


def test_undefined_singleton():
    assert Undefined is UndefinedType()


def test_schema_validator_selection():
    # Tests if the correct validator class is chosen based on the $schema
    # property in the schema. This uses a backwards-incompatible change
    # in Draft 6 which introduced exclusiveMinimum as a number instead of a boolean.
    # Therefore, with Draft 4 there is no actual minimum set as a number and validating
    # the dictionary below passes. With Draft 6, it correctly checks if the number is
    # > 10 and raises a ValidationError. See
    # https://json-schema.org/draft-06/json-schema-release-notes.html#q-what-are-
    # the-changes-between-draft-04-and-draft-06 for more details
    dct = {
        "e": 9,
    }

    assert Draft4Schema.from_dict(dct).to_dict() == dct
    with pytest.raises(
        jsonschema.exceptions.ValidationError,
        match="9 is less than or equal to the minimum of 10",
    ):
        Draft6Schema.from_dict(dct)


@pytest.fixture
def dct():
    return {
        "a": {"foo": "bar"},
        "a2": {"foo": 42},
        "b": ["a", "b", "c"],
        "b2": [1, 2, 3],
        "c": 42,
        "d": ["x", "y", "z"],
    }


def test_copy_method(dct):
    myschema = MySchema.from_dict(dct)

    # Make sure copy is deep
    copy = myschema.copy(deep=True)
    copy["a"]["foo"] = "new value"
    copy["b"] = ["A", "B", "C"]
    copy["c"] = 164
    assert myschema.to_dict() == dct

    # If we ignore a value, changing the copy changes the original
    copy = myschema.copy(deep=True, ignore=["a"])
    copy["a"]["foo"] = "new value"
    copy["b"] = ["A", "B", "C"]
    copy["c"] = 164
    mydct = myschema.to_dict()
    assert mydct["a"]["foo"] == "new value"
    assert mydct["b"][0] == dct["b"][0]
    assert mydct["c"] == dct["c"]

    # If copy is not deep, then changing copy below top level changes original
    copy = myschema.copy(deep=False)
    copy["a"]["foo"] = "baz"
    copy["b"] = ["A", "B", "C"]
    copy["c"] = 164
    mydct = myschema.to_dict()
    assert mydct["a"]["foo"] == "baz"
    assert mydct["b"] == dct["b"]
    assert mydct["c"] == dct["c"]


def test_copy_module(dct):
    myschema = MySchema.from_dict(dct)

    cp = copy.deepcopy(myschema)
    cp["a"]["foo"] = "new value"
    cp["b"] = ["A", "B", "C"]
    cp["c"] = 164
    assert myschema.to_dict() == dct


def test_attribute_error():
    m = MySchema()
    invalid_attr = "invalid_attribute"
    with pytest.raises(AttributeError) as err:
        getattr(m, invalid_attr)
    assert str(err.value) == (
        "'MySchema' object has no attribute " "'invalid_attribute'"
    )


def test_to_from_json(dct):
    json_str = MySchema.from_dict(dct).to_json()
    new_dct = MySchema.from_json(json_str).to_dict()

    assert new_dct == dct


def test_to_from_pickle(dct):
    myschema = MySchema.from_dict(dct)
    output = io.BytesIO()
    pickle.dump(myschema, output)
    output.seek(0)
    myschema_new = pickle.load(output)

    assert myschema_new.to_dict() == dct


def test_class_with_no_schema():
    class BadSchema(SchemaBase):
        pass

    with pytest.raises(ValueError) as err:  # noqa: PT011
        BadSchema(4)
    assert str(err.value).startswith("Cannot instantiate object")


@pytest.mark.parametrize("use_json", [True, False])
def test_hash_schema(use_json):
    classes = _TestSchema._default_wrapper_classes()

    for cls in classes:
        hsh1 = _FromDict.hash_schema(cls._schema, use_json=use_json)
        hsh2 = _FromDict.hash_schema(cls._schema, use_json=use_json)
        assert hsh1 == hsh2
        assert hash(hsh1) == hash(hsh2)


def test_schema_validation_error():
    try:
        MySchema(a={"foo": 4})
        the_err = None
    except jsonschema.ValidationError as err:
        the_err = err

    assert isinstance(the_err, SchemaValidationError)
    message = str(the_err)

    assert the_err.message in message


def chart_error_example__layer():
    # Error: Width is not a valid property of a VConcatChart
    points = (
        alt.Chart(data.cars.url)
        .mark_point()
        .encode(
            x="Horsepower:Q",
            y="Miles_per_Gallon:Q",
        )
    )
    return (points & points).properties(width=400)


def chart_error_example__hconcat():
    # Error: Invalid value for title in Text
    source = data.cars()
    points = (
        alt.Chart(source)
        .mark_point()
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
        )
    )

    text = (
        alt.Chart(source)
        .mark_text()
        .encode(
            alt.Text("Horsepower:N", title={"text": "Horsepower", "align": "right"})  # pyright: ignore[reportArgumentType]
        )
    )

    return points | text


def chart_error_example__invalid_y_option_value_unknown_x_option():
    # Error 1: unknown is an invalid channel option for X
    # Error 2: Invalid Y option value "asdf" and unknown option "unknown" for X
    return (
        alt.Chart(data.barley())
        .mark_bar()
        .encode(
            x=alt.X("variety", unknown=2),
            y=alt.Y("sum(yield)", stack="asdf"),  # pyright: ignore[reportArgumentType]
        )
    )


def chart_error_example__invalid_y_option_value():
    # Error: Invalid Y option value "asdf"
    return (
        alt.Chart(data.barley())
        .mark_bar()
        .encode(
            x=alt.X("variety"),
            y=alt.Y("sum(yield)", stack="asdf"),  # pyright: ignore[reportArgumentType]
        )
    )


def chart_error_example__invalid_y_option_value_with_condition():
    # Error: Invalid Y option value "asdf". Condition is correct
    # but is added below as in previous implementations of Altair this interfered
    # with finding the invalidChannel error
    return (
        alt.Chart(data.barley())
        .mark_bar()
        .encode(
            x="variety",
            y=alt.Y("sum(yield)", stack="asdf"),  # pyright: ignore[reportArgumentType]
            opacity=alt.condition("datum.yield > 0", alt.value(1), alt.value(0.2)),
        )
    )


def chart_error_example__invalid_timeunit_value():
    # Error: Invalid value for Angle.timeUnit
    return alt.Chart().encode(alt.Angle().timeUnit("invalid_value"))  # pyright: ignore[reportArgumentType]


def chart_error_example__invalid_sort_value():
    # Error: Invalid value for Angle.sort
    return alt.Chart().encode(alt.Angle().sort("invalid_value"))


def chart_error_example__invalid_bandposition_value():
    # Error: Invalid value for Text.bandPosition
    return (
        alt.Chart(data.cars())
        .mark_text(align="right")
        .encode(alt.Text("Horsepower:N", bandPosition="4"))  # pyright: ignore[reportArgumentType]
    )


def chart_error_example__invalid_type():
    # Error: Invalid value for type
    return alt.Chart().encode(alt.X(type="unknown"))  # pyright: ignore[reportArgumentType]


def chart_error_example__additional_datum_argument():
    # Error: wrong_argument is not a valid argument to datum
    return alt.Chart().mark_point().encode(x=alt.datum(1, wrong_argument=1))


def chart_error_example__additional_value_argument():
    # Error: `ColorValue` has no parameter named 'predicate'
    return alt.Chart().mark_point().encode(color=alt.value("red", predicate=True))


def chart_error_example__invalid_value_type():
    # Error: Value cannot be an integer in this case
    return (
        alt.Chart(data.cars())
        .mark_point()
        .encode(
            x="Acceleration:Q",
            y="Horsepower:Q",
            color=alt.value(1),  # should be eg. alt.value('red')
        )
    )


def chart_error_example__wrong_tooltip_type_in_faceted_chart():
    # Error: Wrong data type to pass to tooltip
    return (
        alt.Chart(pd.DataFrame({"a": [1]}))
        .mark_point()
        .encode(tooltip=[{"wrong"}])  # pyright: ignore[reportArgumentType]
        .facet()
    )


def chart_error_example__wrong_tooltip_type_in_layered_chart():
    # Error: Wrong data type to pass to tooltip
    return alt.layer(alt.Chart().mark_point().encode(tooltip=[{"wrong"}]))  # pyright: ignore[reportArgumentType]


def chart_error_example__two_errors_in_layered_chart():
    # Error 1: Wrong data type to pass to tooltip
    # Error 2: `Color` has no parameter named 'invalidArgument'
    return alt.layer(
        alt.Chart().mark_point().encode(tooltip=[{"wrong"}]),  # pyright: ignore[reportArgumentType]
        alt.Chart().mark_line().encode(alt.Color(invalidArgument="unknown")),
    )


def chart_error_example__two_errors_in_complex_concat_layered_chart():
    # Error 1: Wrong data type to pass to tooltip
    # Error 2: Invalid value for bandPosition
    return (
        chart_error_example__wrong_tooltip_type_in_layered_chart()
        | chart_error_example__invalid_bandposition_value()
    )


def chart_error_example__three_errors_in_complex_concat_layered_chart():
    # Error 1: Wrong data type to pass to tooltip
    # Error 2: `Color` has no parameter named 'invalidArgument'
    # Error 3: Invalid value for bandPosition
    return (
        chart_error_example__two_errors_in_layered_chart()
        | chart_error_example__invalid_bandposition_value()
    )


def chart_error_example__two_errors_with_one_in_nested_layered_chart():
    # Error 1: invalidOption is not a valid option for Scale
    # Error 2: `Color` has no parameter named 'invalidArgument'

    # In the final chart object, the `layer` attribute will look like this:
    # [alt.Chart(...), alt.Chart(...), alt.LayerChart(...)]
    # We can therefore use this example to test if an error is also
    # spotted in a layered chart within another layered chart
    source = pd.DataFrame(
        [
            {"Day": 1, "Value": 103.3},
            {"Day": 2, "Value": 394.8},
            {"Day": 3, "Value": 199.5},
        ]
    )

    blue_bars = (
        alt.Chart(source)
        .encode(alt.X("Day:O").scale(invalidOption=10), alt.Y("Value:Q"))  # pyright: ignore[reportCallIssue]
        .mark_bar()
    )
    red_bars = (
        alt.Chart(source)
        .transform_filter(alt.datum.Value >= 300)
        .transform_calculate(as_="baseline", calculate="300")
        .encode(
            alt.X("Day:O"),
            alt.Y("baseline:Q"),
            alt.Y2("Value:Q"),
            color=alt.value("#e45755"),
        )
        .mark_bar()
    )

    bars = blue_bars + red_bars

    base = alt.Chart().encode(y=alt.datum(300))

    rule = base.mark_rule().encode(alt.Color(invalidArgument="unknown"))
    text = base.mark_text(text="hazardous")
    rule_text = rule + text

    chart = bars + rule_text
    return chart


def chart_error_example__four_errors_hide_fourth():
    # Error 1: unknown is not a valid encoding channel option
    # Error 2: Invalid Y option value "asdf".
    # Error 3: another_unknown is not a valid encoding channel option
    # Error 4: fourth_error is not a valid encoding channel option <- this error
    # should not show up in the final error message as it is capped at showing
    # 3 errors
    return (
        alt.Chart(data.barley())
        .mark_bar()
        .encode(
            x=alt.X("variety", unknown=2),
            y=alt.Y("sum(yield)", stack="asdf"),  # pyright: ignore[reportArgumentType]
            color=alt.Color("variety", another_unknown=2),
            opacity=alt.Opacity("variety", fourth_error=1),
        )
    )


def id_func_chart_error_example(val) -> str:
    """
    Ensures the generated test-id name uses only the unique portion of `chart_func`.

    Otherwise the name is like below, but ``...`` represents the full error message::

        "test_chart_validation_errors[chart_error_example__two_errors_with_one_in_nested_layered_chart-...]"
    """
    if isinstance(val, types.FunctionType):
        return val.__name__.replace("chart_error_example__", "")
    else:
        return ""


# NOTE: Avoids all cases appearing in a failure traceback
# At the time of writing, this is over 300 lines
chart_funcs_error_message: list[tuple[Callable[..., Any], str]] = [
    (
        chart_error_example__invalid_y_option_value_unknown_x_option,
        rf"""Multiple errors were found.

                Error 1: `X` has no parameter named 'unknown'

                    Existing parameter names are:
                    shorthand      bin      scale   timeUnit   
                    aggregate      field    sort    title      
                    axis           impute   stack   type       
                    bandPosition                               

                    See the help for `X` to read the full description of these parameters

                Error 2: 'asdf' is an invalid value for `stack`. Valid values are:

                    - One of \['zero', 'center', 'normalize'\]
                    - Of type {re.escape("`bool | None`")}$""",
    ),
    (
        chart_error_example__wrong_tooltip_type_in_faceted_chart,
        rf"""'\['wrong'\]' is an invalid value for `field`. Valid values are of type {re.escape("`str | Mapping[str, Any]`")}.$""",
    ),
    (
        chart_error_example__wrong_tooltip_type_in_layered_chart,
        rf"""'\['wrong'\]' is an invalid value for `field`. Valid values are of type {re.escape("`str | Mapping[str, Any]`")}.$""",
    ),
    (
        chart_error_example__two_errors_in_layered_chart,
        rf"""Multiple errors were found.

                Error 1: '\['wrong'\]' is an invalid value for `field`. Valid values are of type {re.escape("`str | Mapping[str, Any]`")}.

                Error 2: `Color` has no parameter named 'invalidArgument'

                    Existing parameter names are:
                    shorthand      bin         legend   timeUnit   
                    aggregate      condition   scale    title      
                    bandPosition   field       sort     type       

                    See the help for `Color` to read the full description of these parameters$""",
    ),
    (
        chart_error_example__two_errors_in_complex_concat_layered_chart,
        rf"""Multiple errors were found.

                Error 1: '\['wrong'\]' is an invalid value for `field`. Valid values are of type {re.escape("`str | Mapping[str, Any]`")}.

                Error 2: '4' is an invalid value for `bandPosition`. Valid values are of type `float`.$""",
    ),
    (
        chart_error_example__three_errors_in_complex_concat_layered_chart,
        rf"""Multiple errors were found.

                Error 1: '\['wrong'\]' is an invalid value for `field`. Valid values are of type {re.escape("`str | Mapping[str, Any]`")}.

                Error 2: `Color` has no parameter named 'invalidArgument'

                    Existing parameter names are:
                    shorthand      bin         legend   timeUnit   
                    aggregate      condition   scale    title      
                    bandPosition   field       sort     type       

                    See the help for `Color` to read the full description of these parameters

                Error 3: '4' is an invalid value for `bandPosition`. Valid values are of type `float`.$""",
    ),
    (
        chart_error_example__two_errors_with_one_in_nested_layered_chart,
        r"""Multiple errors were found.

                Error 1: `Scale` has no parameter named 'invalidOption'

                    Existing parameter names are:
                    align      domain      exponent       paddingOuter   round    
                    base       domainMax   interpolate    range          scheme   
                    bins       domainMid   nice           rangeMax       type     
                    clamp      domainMin   padding        rangeMin       zero     
                    constant   domainRaw   paddingInner   reverse                 

                    See the help for `Scale` to read the full description of these parameters

                Error 2: `Color` has no parameter named 'invalidArgument'

                    Existing parameter names are:
                    shorthand      bin         legend   timeUnit   
                    aggregate      condition   scale    title      
                    bandPosition   field       sort     type       

                    See the help for `Color` to read the full description of these parameters$""",
    ),
    (
        chart_error_example__layer,
        r"""`VConcatChart` has no parameter named 'width'

                Existing parameter names are:
                vconcat      center     description   params    title       
                autosize     config     name          resolve   transform   
                background   data       padding       spacing   usermeta    
                bounds       datasets                                       

                See the help for `VConcatChart` to read the full description of these parameters$""",
    ),
    (
        chart_error_example__invalid_y_option_value,
        rf"""'asdf' is an invalid value for `stack`. Valid values are:

                - One of \['zero', 'center', 'normalize'\]
                - Of type {re.escape("`bool | None`")}$""",
    ),
    (
        chart_error_example__invalid_y_option_value_with_condition,
        rf"""'asdf' is an invalid value for `stack`. Valid values are:

                - One of \['zero', 'center', 'normalize'\]
                - Of type {re.escape("`bool | None`")}$""",
    ),
    (
        chart_error_example__hconcat,
        rf"""'{{'text': 'Horsepower', 'align': 'right'}}' is an invalid value for `title`. Valid values are of type {re.escape("`str | Sequence | None`")}.$""",
    ),
    (
        chart_error_example__invalid_timeunit_value,
        rf"""'invalid_value' is an invalid value for `timeUnit`. Valid values are:

                - One of \['year', 'quarter', 'month', 'week', 'day', 'dayofyear', 'date', 'hours', 'minutes', 'seconds', 'milliseconds'\]
                - One of \['utcyear', 'utcquarter', 'utcmonth', 'utcweek', 'utcday', 'utcdayofyear', 'utcdate', 'utchours', 'utcminutes', 'utcseconds', 'utcmilliseconds'\]
                - One of \['yearquarter', 'yearquartermonth', 'yearmonth', 'yearmonthdate', 'yearmonthdatehours', 'yearmonthdatehoursminutes', 'yearmonthdatehoursminutesseconds', 'yearweek', 'yearweekday', 'yearweekdayhours', 'yearweekdayhoursminutes', 'yearweekdayhoursminutesseconds', 'yeardayofyear', 'quartermonth', 'monthdate', 'monthdatehours', 'monthdatehoursminutes', 'monthdatehoursminutesseconds', 'weekday', 'weekdayhours', 'weekdayhoursminutes', 'weekdayhoursminutesseconds', 'dayhours', 'dayhoursminutes', 'dayhoursminutesseconds', 'hoursminutes', 'hoursminutesseconds', 'minutesseconds', 'secondsmilliseconds'\]
                - One of \['utcyearquarter', 'utcyearquartermonth', 'utcyearmonth', 'utcyearmonthdate', 'utcyearmonthdatehours', 'utcyearmonthdatehoursminutes', 'utcyearmonthdatehoursminutesseconds', 'utcyearweek', 'utcyearweekday', 'utcyearweekdayhours', 'utcyearweekdayhoursminutes', 'utcyearweekdayhoursminutesseconds', 'utcyeardayofyear', 'utcquartermonth', 'utcmonthdate', 'utcmonthdatehours', 'utcmonthdatehoursminutes', 'utcmonthdatehoursminutesseconds', 'utcweekday', 'utcweekdayhours', 'utcweekdayhoursminutes', 'utcweekdayhoursminutesseconds', 'utcdayhours', 'utcdayhoursminutes', 'utcdayhoursminutesseconds', 'utchoursminutes', 'utchoursminutesseconds', 'utcminutesseconds', 'utcsecondsmilliseconds'\]
                - One of \['binnedyear', 'binnedyearquarter', 'binnedyearquartermonth', 'binnedyearmonth', 'binnedyearmonthdate', 'binnedyearmonthdatehours', 'binnedyearmonthdatehoursminutes', 'binnedyearmonthdatehoursminutesseconds', 'binnedyearweek', 'binnedyearweekday', 'binnedyearweekdayhours', 'binnedyearweekdayhoursminutes', 'binnedyearweekdayhoursminutesseconds', 'binnedyeardayofyear'\]
                - One of \['binnedutcyear', 'binnedutcyearquarter', 'binnedutcyearquartermonth', 'binnedutcyearmonth', 'binnedutcyearmonthdate', 'binnedutcyearmonthdatehours', 'binnedutcyearmonthdatehoursminutes', 'binnedutcyearmonthdatehoursminutesseconds', 'binnedutcyearweek', 'binnedutcyearweekday', 'binnedutcyearweekdayhours', 'binnedutcyearweekdayhoursminutes', 'binnedutcyearweekdayhoursminutesseconds', 'binnedutcyeardayofyear'\]
                - Of type {re.escape("`Mapping[str, Any]`")}$""",
    ),
    (
        chart_error_example__invalid_sort_value,
        rf"""'invalid_value' is an invalid value for `sort`. Valid values are:

                - One of \['ascending', 'descending'\]
                - One of \['x', 'y', 'color', 'fill', 'stroke', 'strokeWidth', 'size', 'shape', 'fillOpacity', 'strokeOpacity', 'opacity', 'text'\]
                - One of \['-x', '-y', '-color', '-fill', '-stroke', '-strokeWidth', '-size', '-shape', '-fillOpacity', '-strokeOpacity', '-opacity', '-text'\]
                - Of type {re.escape("`Sequence | Mapping[str, Any] | None`")}$""",
    ),
    (
        chart_error_example__invalid_bandposition_value,
        r"""'4' is an invalid value for `bandPosition`. Valid values are of type `float`.$""",
    ),
    (
        chart_error_example__invalid_type,
        r"""'unknown' is an invalid value for `type`. Valid values are one of \['quantitative', 'ordinal', 'temporal', 'nominal', 'geojson'\].$""",
    ),
    (
        chart_error_example__additional_datum_argument,
        r"""`XDatum` has no parameter named 'wrong_argument'

                Existing parameter names are:
                datum          impute   title   
                axis           scale    type    
                bandPosition   stack            

                See the help for `XDatum` to read the full description of these parameters$""",
    ),
    (
        chart_error_example__additional_value_argument,
        r"""`ColorValue` has no parameter named 'predicate'

                Existing parameter names are:
                value   condition   

                See the help for `ColorValue` to read the full description of these parameters$""",
    ),
    (
        chart_error_example__invalid_value_type,
        rf"""'1' is an invalid value for `value`. Valid values are of type {re.escape("`str | Mapping[str, Any] | None`")}.$""",
    ),
    (
        chart_error_example__four_errors_hide_fourth,
        r"""Multiple errors were found.

                Error 1: `Color` has no parameter named 'another_unknown'

                    Existing parameter names are:
                    shorthand      bin         legend   timeUnit   
                    aggregate      condition   scale    title      
                    bandPosition   field       sort     type       

                    See the help for `Color` to read the full description of these parameters

                Error 2: `Opacity` has no parameter named 'fourth_error'

                    Existing parameter names are:
                    shorthand      bin         legend   timeUnit   
                    aggregate      condition   scale    title      
                    bandPosition   field       sort     type       

                    See the help for `Opacity` to read the full description of these parameters

                Error 3: `X` has no parameter named 'unknown'

                    Existing parameter names are:
                    shorthand      bin      scale   timeUnit   
                    aggregate      field    sort    title      
                    axis           impute   stack   type       
                    bandPosition                               

                    See the help for `X` to read the full description of these parameters$""",
    ),
]


@pytest.mark.parametrize(
    ("chart_func", "expected_error_message"),
    chart_funcs_error_message,
    ids=id_func_chart_error_example,
)
def test_chart_validation_errors(chart_func, expected_error_message):
    # For some wrong chart specifications such as an unknown encoding channel,
    # Altair already raises a warning before the chart specifications are validated.
    # We can ignore these warnings as we are interested in the errors being raised
    # during validation which is triggered by to_dict
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        chart = chart_func()
    expected_error_message = inspect.cleandoc(expected_error_message)
    with pytest.raises(SchemaValidationError, match=expected_error_message):
        chart.to_dict()


def test_multiple_field_strings_in_condition():
    selection = alt.selection_point()
    expected_error_message = "A field cannot be used for both the `if_true` and `if_false` values of a condition. One of them has to specify a `value` or `datum` definition."
    with pytest.raises(ValueError, match=expected_error_message):
        chart = (  # noqa: F841
            alt.Chart(data.cars())
            .mark_circle()
            .add_params(selection)
            .encode(color=alt.condition(selection, "Origin", "Origin"))
            .to_dict()
        )


@pytest.mark.parametrize("tp", [pd.DataFrame, pl.DataFrame])
def test_non_existent_column_name(tp: Callable[..., IntoDataFrame]) -> None:
    df = tp({"a": [1, 2], "b": [4, 5]})
    msg = (
        'Unable to determine data type for the field "c"; verify that the field name '
        "is not misspelled. If you are referencing a field from a transform, also "
        "confirm that the data type is specified correctly."
    )
    with pytest.raises(ValueError, match=msg):
        alt.Chart(df).mark_line().encode(x="a", y="c").to_json()


def test_serialize_numpy_types():
    m = MySchema(
        a={"date": np.datetime64("2019-01-01")},
        a2={"int64": np.int64(1), "float64": np.float64(2)},
        b2=np.arange(4),
    )
    out = m.to_json()
    dct = json.loads(out)
    assert dct == {
        "a": {"date": "2019-01-01T00:00:00"},
        "a2": {"int64": 1, "float64": 2},
        "b2": [0, 1, 2, 3],
    }


def test_to_dict_no_side_effects():
    # Tests that shorthands are expanded in returned dictionary when calling to_dict
    # but that they remain untouched in the chart object. Goal is to ensure that
    # the chart object stays unchanged when to_dict is called
    def validate_encoding(encoding):
        assert encoding.x["shorthand"] == "a"
        assert encoding.x["field"] is alt.Undefined
        assert encoding.x["type"] is alt.Undefined
        assert encoding.y["shorthand"] == "b:Q"
        assert encoding.y["field"] is alt.Undefined
        assert encoding.y["type"] is alt.Undefined

    data = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(data).mark_bar().encode(x="a", y="b:Q")

    validate_encoding(chart.encoding)
    dct = chart.to_dict()
    validate_encoding(chart.encoding)

    assert "shorthand" not in dct["encoding"]["x"]
    assert dct["encoding"]["x"]["field"] == "a"

    assert "shorthand" not in dct["encoding"]["y"]
    assert dct["encoding"]["y"]["field"] == "b"
    assert dct["encoding"]["y"]["type"] == "quantitative"


def test_to_dict_expand_mark_spec():
    # Test that `to_dict` correctly expands marks to a dictionary
    # without impacting the original spec which remains a string
    chart = alt.Chart().mark_bar()
    assert chart.to_dict()["mark"] == {"type": "bar"}
    assert chart.mark == "bar"


@pytest.mark.parametrize(
    "expected",
    [list("cdfabe"), [0, 3, 4, 5, 8]],
)
@pytest.mark.parametrize(
    "tp",
    [
        tuple,
        list,
        deque,
        pl.Series,
        pd.Series,
        pd.Index,
        pd.Categorical,
        pd.CategoricalIndex,
        np.array,
    ],
)
@pytest.mark.parametrize(
    "schema_param",
    [
        (partial(X, "x:N"), "sort"),
        (partial(FieldOneOfPredicate, "name"), "oneOf"),
        (Legend, "values"),
    ],
)
def test_to_dict_iterables(
    tp: Callable[..., Iterable[Any]],
    expected: Sequence[Any],
    schema_param: tuple[Callable[..., SchemaBase], str],
) -> None:
    """
    Confirm `SchemaBase` can convert common `(Sequence|Iterable)` types to `list`.

    Parameters
    ----------
    tp
        Constructor for test `Iterable`.
    expected
        Values wrapped by `tp`.
    schema_param
        Constructor for `SchemaBase` subclass, and target parameter name.

    Notes
    -----
    `partial` can be used to reshape the `SchemaBase` constructor.

    References
    ----------
    - https://github.com/vega/altair/issues/2808
    - https://github.com/vega/altair/issues/2877
    """
    tp_schema, param = schema_param
    validated = tp_schema(**{param: tp(expected)}).to_dict()
    actual = validated[param]
    assert actual == expected


@pytest.mark.parametrize(
    "tp", [range, np.arange, partial(pl.int_range, eager=True), pd.RangeIndex]
)
def test_to_dict_range(tp) -> None:
    expected = [0, 1, 2, 3, 4]
    x_dict = alt.X("x:O", sort=tp(0, 5)).to_dict()
    actual = x_dict["sort"]  # type: ignore
    assert actual == expected


@pytest.fixture
def stocks() -> alt.Chart:
    source = "https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/sp500.csv"
    return alt.Chart(source).mark_area().encode(x="date:T", y="price:Q")


def DateTime(
    year: int,
    month: int,
    day: int,
    hour: int = 0,
    minute: int = 0,
    second: int = 0,
    milliseconds: int = 0,
    *,
    utc: bool | None = None,
) -> alt.DateTime:
    """Factory for positionally aligning `datetime.datetime`/ `alt.DateTime`."""
    kwds: dict[str, Any] = {}
    if utc is True:
        kwds.update(utc=utc)
    if (hour, minute, second, milliseconds) != (0, 0, 0, 0):
        kwds.update(
            hours=hour, minutes=minute, seconds=second, milliseconds=milliseconds
        )
    return alt.DateTime(year=year, month=month, date=day, **kwds)


@pytest.mark.parametrize(
    ("window", "expected"),
    [
        (
            (dt.date(2005, 1, 1), dt.date(2009, 1, 1)),
            (DateTime(2005, 1, 1), DateTime(2009, 1, 1)),
        ),
        (
            (dt.datetime(2005, 1, 1), dt.datetime(2009, 1, 1)),
            (
                # NOTE: Keep this to test truncating independently!
                alt.DateTime(year=2005, month=1, date=1),
                alt.DateTime(year=2009, month=1, date=1),
            ),
        ),
        (
            (
                dt.datetime(2001, 1, 1, 9, 30, 0, 2999),
                dt.datetime(2002, 1, 1, 17, 0, 0, 5000),
            ),
            (
                DateTime(2001, 1, 1, 9, 30, 0, 2),
                DateTime(2002, 1, 1, 17, 0, 0, 5),
            ),
        ),
        (
            (
                dt.datetime(2003, 5, 1, 1, 30, tzinfo=dt.timezone.utc),
                dt.datetime(2003, 6, 3, 4, 3, tzinfo=dt.timezone.utc),
            ),
            (
                DateTime(2003, 5, 1, 1, 30, 0, 0, utc=True),
                DateTime(2003, 6, 3, 4, 3, 0, 0, utc=True),
            ),
        ),
    ],
    ids=["date", "datetime (no time)", "datetime (microseconds)", "datetime (UTC)"],
)
def test_to_dict_datetime(
    stocks, window: tuple[dt.date, dt.date], expected: tuple[alt.DateTime, alt.DateTime]
) -> None:
    """
    Includes `datetime.datetime` with an empty time component.

    This confirms that conversion matches how `alt.DateTime` omits `Undefined`.
    """
    expected_dicts = [e.to_dict() for e in expected]
    brush = alt.selection_interval(encodings=["x"], value={"x": window})
    base = stocks

    upper = base.encode(alt.X("date:T").scale(domain=brush))
    lower = base.add_params(brush)
    chart = upper & lower
    mapping = chart.to_dict()
    params_value = mapping["params"][0]["value"]["x"]

    assert isinstance(params_value, list)
    assert params_value == expected_dicts


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
def test_to_dict_datetime_unsupported_timezone(tzinfo: dt.timezone) -> None:
    datetime = dt.datetime(2003, 5, 1, 1, 30)

    result = alt.FieldEqualPredicate(datetime, "column 1")
    assert result.to_dict()

    with pytest.raises(TypeError, match=r"Unsupported timezone.+\n.+UTC.+local"):
        alt.FieldEqualPredicate(datetime.replace(tzinfo=tzinfo), "column 1")


def test_to_dict_datetime_typing() -> None:
    """
    Enumerating various places that need updated annotations.

    All work at runtime, just need to give the type checkers the new info.

    Sub-issue of https://github.com/vega/altair/issues/3650
    """
    datetime = dt.datetime(2003, 5, 1, 1, 30)
    datetime_seq = [datetime, datetime.replace(2005), datetime.replace(2008)]
    assert alt.FieldEqualPredicate(datetime, field="column 1")
    assert alt.FieldOneOfPredicate(oneOf=datetime_seq, field="column 1")

    assert alt.Legend(values=datetime_seq)

    assert alt.Scale(domain=datetime_seq)
    assert alt.Scale(domainMin=datetime_seq[0], domainMax=datetime_seq[2])

    # NOTE: `datum` is not annotated?
    assert alt.XDatum(datum=datetime).to_dict()

    # NOTE: `*args` is not annotated?
    # - All of these uses *args incorrectly
    assert alt.Vector2DateTime(datetime_seq[:2])
