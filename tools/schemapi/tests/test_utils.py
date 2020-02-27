import pytest

from ..utils import get_valid_identifier, SchemaInfo
from ..schemapi import _FromDict


@pytest.fixture
def refschema():
    return {
        "$ref": "#/definitions/Foo",
        "definitions": {
            "Foo": {"$ref": "#/definitions/Bar"},
            "Bar": {"$ref": "#/definitions/Baz"},
            "Baz": {"type": "string"},
        },
    }


def test_get_valid_identifier():
    assert get_valid_identifier("$schema") == "schema"
    assert get_valid_identifier("$ref") == "ref"
    assert get_valid_identifier("foo-bar") == "foobar"
    assert get_valid_identifier("$as") == "as_"
    assert get_valid_identifier("for") == "for_"
    assert get_valid_identifier("--") == "_"


@pytest.mark.parametrize("use_json", [True, False])
def test_hash_schema(refschema, use_json):
    copy = refschema.copy()
    copy["description"] = "A schema"
    copy["title"] = "Schema to test"
    assert _FromDict.hash_schema(refschema) == _FromDict.hash_schema(copy)


@pytest.mark.parametrize(
    "schema, expected",
    [
        ({}, "Any"),
        ({"type": "number"}, "float"),
        ({"enum": ["A", "B", "C"]}, "enum('A', 'B', 'C')"),
        ({"type": "array"}, "List(Any)"),
        ({"type": "object"}, "Mapping(required=[])"),
        (
            {"type": "string", "not": {"enum": ["A", "B", "C"]}},
            "not enum('A', 'B', 'C')",
        ),
    ],
)
def test_medium_description(schema, expected):
    description = SchemaInfo(schema).medium_description
    assert description == expected
