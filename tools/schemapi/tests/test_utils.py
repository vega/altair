import pytest

from ..utils import resolve_references, get_valid_identifier
from ..schemapi import _FromDict


@pytest.fixture
def refschema():
    return {
        '$ref': '#/definitions/Foo',
        'definitions': {
            'Foo': {'$ref': '#/definitions/Bar'},
            'Bar': {'$ref': '#/definitions/Baz'},
            'Baz': {'type': 'string'}
        }
    }


def test_get_valid_identifier():
    assert get_valid_identifier('$schema') == 'schema'
    assert get_valid_identifier('$ref') == 'ref'
    assert get_valid_identifier('foo-bar') == 'foobar'
    assert get_valid_identifier('$as') == 'as_'
    assert get_valid_identifier('for') == 'for_'
    assert get_valid_identifier('--') == '_'


@pytest.mark.parametrize('use_json', [True, False])
def test_hash_schema(refschema, use_json):
    copy = refschema.copy()
    copy['description'] = "A schema"
    copy['title'] = "Schema to test"
    assert _FromDict.hash_schema(refschema) == _FromDict.hash_schema(copy)
