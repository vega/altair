import inspect

from .. import SchemaBase, Undefined, schemaclass


@schemaclass
class MySchema(SchemaBase):
    _schema = {
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
        },
        "required": ["a", "b"],
    }


@schemaclass
class StringArray(SchemaBase):
    _schema = MySchema._schema["definitions"]["StringArray"]
    _rootschema = MySchema._schema


def test_myschema_decorator():
    myschema = MySchema({"foo": "bar"}, ["foo", "bar"])
    assert myschema.to_dict() == {"a": {"foo": "bar"}, "b": ["foo", "bar"]}

    myschema = MySchema.from_dict({"a": {"foo": "bar"}, "b": ["foo", "bar"]})
    assert myschema.to_dict() == {"a": {"foo": "bar"}, "b": ["foo", "bar"]}

    assert MySchema.__doc__.startswith("MySchema schema wrapper")
    argspec = inspect.getfullargspec(MySchema.__init__)
    assert argspec.args == ["self", "a", "b", "a2", "b2", "c", "d"]
    assert argspec.defaults == 6 * (Undefined,)
    assert argspec.varargs is None
    assert argspec.varkw == "kwds"


def test_stringarray_decorator():
    arr = StringArray(["a", "b", "c"])
    assert arr.to_dict() == ["a", "b", "c"]

    arr = StringArray.from_dict(["a", "b", "c"])
    assert arr.to_dict() == ["a", "b", "c"]

    assert arr.__doc__.startswith("StringArray schema wrapper")
    argspec = inspect.getfullargspec(StringArray.__init__)
    assert argspec.args == ["self"]
    assert argspec.varargs == "args"
    assert argspec.varkw is None
