"""Utilities for working with schemas"""

import keyword
import re
import textwrap

import jsonschema
import pkgutil
import json


EXCLUDE_KEYS = ('definitions', 'title', 'description', '$schema', 'id')


def load_metaschema():
    schema = pkgutil.get_data('schemapi', 'jsonschema-draft04.json')
    schema = schema.decode()
    return json.loads(schema)


def resolve_references(schema, root=None):
    """Resolve References within a JSON schema"""
    resolver = jsonschema.RefResolver.from_schema(root or schema)
    while '$ref' in schema:
        ref, schema = resolver.resolve(schema['$ref'])
    return schema


def get_valid_identifier(prop, replacement_character='', allow_unicode=False):
    """Given a string property, generate a valid Python identifier

    Parameters
    ----------
    replacement_character: string, default ''
        The character to replace invalid characters with.
    allow_unicode: boolean, default False
        If True, then allow Python 3-style unicode identifiers.

    Examples
    --------
    >>> get_valid_identifier('my-var')
    'myvar'

    >>> get_valid_identifier('if')
    'if_'

    >>> get_valid_identifier('$schema', '_')
    '_schema'

    >>> get_valid_identifier('$*#$')
    '_'
    """
    # First substitute-out all non-valid characters.
    flags = re.UNICODE if allow_unicode else re.ASCII
    valid = re.sub('\W', replacement_character, prop, flags=flags)

    # If nothing is left, use just an underscore
    if not valid:
        valid = '_'

    # first character must be a non-digit. Prefix with an underscore
    # if needed
    if re.match('^[\d\W]', valid):
        valid = '_' + valid

    # if the result is a reserved keyword, then add an underscore at the end
    if keyword.iskeyword(valid):
        valid += '_'
    return valid


def is_valid_identifier(var, allow_unicode=False):
    """Return true if var contains a valid Python identifier

    Parameters
    ----------
    val : string
        identifier to check
    allow_unicode : bool (default: False)
        if True, then allow Python 3 style unicode identifiers.
    """
    flags = re.UNICODE if allow_unicode else re.ASCII
    is_valid = re.match("^[^\d\W]\w*\Z", var, flags)
    return is_valid and not keyword.iskeyword(var)


class SchemaProperties(object):
    """A wrapper for properties within a schema

    """
    def __init__(self, properties, schema):
        self.__properties = properties
        self.__schema = schema

    def __dir__(self):
        return list(self.__properties.keys())

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            return super(SchemaProperties, self).__getattr__(attr)

    def __getitem__(self, attr):
        dct = self.__properties[attr]
        if 'definitions' in self.__schema and 'definitions' not in dct:
            dct = dict(definitions=self.__schema['definitions'], **dct)
        return SchemaInfo(dct)

    def __iter__(self):
        return iter(self.__properties)

    def items(self):
        return self.__properties.items()

    def keys(self):
        return self.__properties.keys()

    def values(self):
        return self.__properties.values()


class SchemaInfo(object):
    """A wrapper for inspecting a JSON schema"""
    def __init__(self, schema, rootschema=None, validate=True):
        if hasattr(schema, '_schema'):
            if hasattr(schema, '_rootschema'):
                schema, rootschema = schema._schema, schema._rootschema
            else:
                schema, rootschema = schema._schema, schema._schema
        if validate:
            metaschema = load_metaschema()
            jsonschema.validate(schema, metaschema)
            jsonschema.validate(rootschema, metaschema)
        self.raw_schema = schema
        self.schema = resolve_references(schema, rootschema)

    def __repr__(self):
        keys = []
        for key in sorted(self.schema.keys()):
            val = self.schema[key]
            rval = repr(val).replace('\n', '')
            if len(rval) > 30:
                rval = rval[:30] + '...'
            if key == 'definitions':
                rval = "{...}"
            elif key == 'properties':
                rval = '{\n    ' + '\n    '.join(sorted(map(repr, val))) + '\n  }'
            keys.append('"{0}": {1}'.format(key, rval))
        return "SchemaInfo({\n  " + '\n  '.join(keys) + "\n})"

    @property
    def short_description(self):
        # TODO
        return 'schema'

    @property
    def medium_description(self):
        # TODO
        return 'A schema of type <type>'

    @property
    def long_description(self):
        # TODO
        return 'Long description including arguments and their types'

    @property
    def properties(self):
        return SchemaProperties(self.schema.get('properties', {}), self.schema)

    @property
    def definitions(self):
        return SchemaProperties(self.schema.get('definitions', {}), self.schema)

    @property
    def required(self):
        return self.schema.get('required', [])

    @property
    def patternProperties(self):
        return self.schema.get('patternProperties', {})

    @property
    def additionalProperties(self):
        return self.schema.get('additionalProperties', True)

    @property
    def type(self):
        return self.schema.get('type', None)

    @property
    def anyOf(self):
        return self.schema.get('anyOf', [])

    @property
    def oneOf(self):
        return self.schema.get('oneOf', [])

    @property
    def allOf(self):
        return self.schema.get('allOf', [])

    @property
    def items(self):
        return self.schema.get('items', {})

    @property
    def enum(self):
        return self.schema.get('enum', [])

    def is_reference(self):
        return '$ref' in self.raw_schema

    def is_empty(self):
        return set(self.schema.keys()) - set(EXCLUDE_KEYS) == {}

    def is_compound(self):
        return any(key in self.schema for key in ['anyOf', 'allOf', 'oneOf'])

    def is_anyOf(self):
        return 'anyOf' in self.schema

    def is_allOf(self):
        return 'allOf' in self.schema

    def is_oneOf(self):
        return 'oneOf' in self.schema

    def is_object(self):
        if self.type == 'object':
            return True
        elif self.type is not None:
            return False
        elif self.properties or self.required or self.patternProperties or self.additionalProperties:
            return True
        else:
            raise ValueError("Unclear whether schema.is_object() is True")

    def is_value(self):
        return not self.is_object()

    def is_array(self):
        return (self.type == 'array')

    def schema_type(self):
        if self.is_empty():
            return 'empty'
        elif self.is_compound():
            for key in ['anyOf', 'oneOf', 'allOf']:
                if key in self.schema:
                    return key
        elif self.is_object():
            return 'object'
        elif self.is_array():
            return 'array'
        elif self.is_value():
            return 'value'
        else:
            raise ValueError("Unknown type with keys {0}".format(self.schema))

    def property_name_map(self):
        """
        Return a mapping of schema property names to valid Python attribute names

        Only properties which are not valid Python identifiers will be included in
        the dictionary.
        """
        pairs = [(prop, get_valid_identifier(prop)) for prop in self.properties]
        return {prop: val for prop, val in pairs if prop != val}
