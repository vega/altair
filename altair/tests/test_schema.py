from altair.schema import load_schema

def test_schema():
    schema = load_schema()
    assert schema["$schema"]=="http://json-schema.org/draft-04/schema#"
