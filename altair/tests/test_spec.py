from altair.schema import SCHEMA

def test_schema():
    assert SCHEMA["$schema"]=="http://json-schema.org/draft-04/schema#"
