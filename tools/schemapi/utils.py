"""Utilities for working with schemas"""

import json
import keyword
import pkgutil
import re
import textwrap

import jsonschema


EXCLUDE_KEYS = ('definitions', 'title', 'description', '$schema', 'id')


def load_metaschema():
    schema = pkgutil.get_data('schemapi', 'jsonschema-draft04.json')
    schema = schema.decode()
    return json.loads(schema)


def resolve_references(schema, root=None):
    """Resolve References within a JSON schema"""
    resolver = jsonschema.RefResolver.from_schema(root or schema)
    while '$ref' in schema:
        with resolver.resolving(schema['$ref']) as resolved:
            schema = resolved
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
    valid = re.sub(r'\W', replacement_character, prop, flags=flags)

    # If nothing is left, use just an underscore
    if not valid:
        valid = '_'

    # first character must be a non-digit. Prefix with an underscore
    # if needed
    if re.match(r'^[\d\W]', valid):
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
    is_valid = re.match(r"^[^\d\W]\w*\Z", var, flags)
    return is_valid and not keyword.iskeyword(var)


class SchemaProperties(object):
    """A wrapper for properties within a schema"""

    def __init__(self, properties, schema, rootschema=None):
        self._properties = properties
        self._schema = schema
        self._rootschema = rootschema or schema

    def __bool__(self):
        return bool(self._properties)

    def __dir__(self):
        return list(self._properties.keys())

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            return super(SchemaProperties, self).__getattr__(attr)

    def __getitem__(self, attr):
        dct = self._properties[attr]
        if 'definitions' in self._schema and 'definitions' not in dct:
            dct = dict(definitions=self._schema['definitions'], **dct)
        return SchemaInfo(dct, self._rootschema)

    def __iter__(self):
        return iter(self._properties)

    def items(self):
        return ((key, self[key]) for key in self)

    def keys(self):
        return self._properties.keys()

    def values(self):
        return (self[key] for key in self)


class SchemaInfo(object):
    """A wrapper for inspecting a JSON schema"""

    def __init__(self, schema, rootschema=None, validate=False):
        if hasattr(schema, '_schema'):
            if hasattr(schema, '_rootschema'):
                schema, rootschema = schema._schema, schema._rootschema
            else:
                schema, rootschema = schema._schema, schema._schema
        elif not rootschema:
            rootschema = schema
        if validate:
            metaschema = load_metaschema()
            jsonschema.validate(schema, metaschema)
            jsonschema.validate(rootschema, metaschema)
        self.raw_schema = schema
        self.rootschema = rootschema
        self.schema = resolve_references(schema, rootschema)

    def child(self, schema):
        return self.__class__(schema, rootschema=self.rootschema)

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
            keys.append('"{}": {}'.format(key, rval))
        return "SchemaInfo({\n  " + '\n  '.join(keys) + "\n})"

    @property
    def title(self):
        if self.is_reference():
            return get_valid_identifier(self.refname)
        else:
            return ''

    @property
    def short_description(self):
        if self.title:
            # use RST syntax for generated sphinx docs
            return ":class:`{}`".format(self.title)
        else:
            return self.medium_description

    @property
    def medium_description(self):
        _simple_types = {'string': 'string',
                         'number': 'float',
                         'integer': 'integer',
                         'object': 'mapping',
                         'boolean': 'boolean',
                         'array': 'list',
                         'null': 'None'}
        if self.is_list():
            return '[{0}]'.format(', '.join(self.child(s).short_description
                                            for s in self.schema))
        elif self.is_empty():
            return 'any object'
        elif self.is_enum():
            return 'enum({})'.format(', '.join(map(repr, self.enum)))
        elif self.is_anyOf():
            return 'anyOf({})'.format(', '.join(s.short_description
                                                for s in self.anyOf))
        elif self.is_oneOf():
            return 'oneOf({})'.format(', '.join(s.short_description
                                                for s in self.oneOf))
        elif self.is_allOf():
            return 'allOf({})'.format(', '.join(s.short_description
                                                for s in self.allOf))
        elif self.is_not():
            return 'not {}'.format(self.not_.short_description)
        elif isinstance(self.type, list):
            options = []
            subschema = SchemaInfo(dict(**self.schema))
            for typ_ in self.type:
                subschema.schema['type'] = typ_
                options.append(subschema.short_description)
            return "anyOf({})".format(', '.join(options))
        elif self.is_object():
            return "Mapping(required=[{}])".format(', '.join(self.required))
        elif self.is_array():
            return "List({})".format(self.child(self.items).short_description)
        elif self.type in _simple_types:
            return _simple_types[self.type]
        elif not self.type:
            import warnings
            warnings.warn("no short_description for schema\n{}"
                          "".format(self.schema))
            return 'any'

    @property
    def long_description(self):
        # TODO
        return 'Long description including arguments and their types'

    @property
    def properties(self):
        return SchemaProperties(self.schema.get('properties', {}),
                                self.schema, self.rootschema)

    @property
    def definitions(self):
        return SchemaProperties(self.schema.get('definitions', {}),
                                self.schema, self.rootschema)

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
        return [self.child(s) for s in self.schema.get('anyOf', [])]

    @property
    def oneOf(self):
        return [self.child(s) for s in self.schema.get('oneOf', [])]

    @property
    def allOf(self):
        return [self.child(s) for s in self.schema.get('allOf', [])]

    @property
    def not_(self):
        return self.child(self.schema.get('not_', {}))

    @property
    def items(self):
        return self.schema.get('items', {})

    @property
    def enum(self):
        return self.schema.get('enum', [])

    @property
    def refname(self):
        return self.raw_schema.get('$ref', '#/').split('/')[-1]

    @property
    def ref(self):
        return self.raw_schema.get('$ref', None)

    @property
    def description(self):
        return self.raw_schema.get('description',
                                   self.schema.get('description', ''))

    def is_list(self):
        return isinstance(self.schema, list)

    def is_reference(self):
        return '$ref' in self.raw_schema

    def is_enum(self):
        return 'enum' in self.schema

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

    def is_not(self):
        return 'not' in self.schema

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
            raise ValueError("Unknown type with keys {}".format(self.schema))

    def property_name_map(self):
        """
        Return a mapping of schema property names to valid Python attribute names

        Only properties which are not valid Python identifiers will be included in
        the dictionary.
        """
        pairs = [(prop, get_valid_identifier(prop)) for prop in self.properties]
        return {prop: val for prop, val in pairs if prop != val}


def indent_arglist(args, indent_level, width=100, lstrip=True):
    """Indent an argument list for use in generated code"""
    wrapper = textwrap.TextWrapper(width=width,
                                   initial_indent=indent_level * ' ',
                                   subsequent_indent=indent_level * ' ',
                                   break_long_words=False)
    wrapped = '\n'.join(wrapper.wrap(', '.join(args)))
    if lstrip:
        wrapped = wrapped.lstrip()
    return wrapped


def indent_docstring(lines, indent_level, width=100, lstrip=True):
    """Indent a docstring for use in generated code"""
    final_lines = []

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped:
            leading_space = len(line) - len(stripped)
            indent = indent_level + leading_space
            wrapper = textwrap.TextWrapper(width=width - indent,
                                           initial_indent=indent * ' ',
                                           subsequent_indent=indent * ' ',
                                           break_long_words=False,
                                           break_on_hyphens=False,
                                           drop_whitespace=True)
            list_wrapper = textwrap.TextWrapper(width=width - indent,
                                                initial_indent=indent * ' ' + '* ',
                                                subsequent_indent=indent * ' ' + '  ',
                                                break_long_words=False,
                                                break_on_hyphens=False,
                                                drop_whitespace=True)
            for line in stripped.split("\n"):
                if line == '':
                    final_lines.append('')
                elif line.startswith('* '):
                    final_lines.extend(list_wrapper.wrap(line[2:]))
                else:
                    final_lines.extend(wrapper.wrap(line.lstrip()))

        # If this is the last line, put in an indent
        elif i + 1 == len(lines):
            final_lines.append(indent_level * ' ')
        # If it's not the last line, this is a blank line that should not indent.
        else:
            final_lines.append('')
    # Remove any trailing whitespaces on the right side
    stripped_lines = []
    for i, line in enumerate(final_lines):
        if i + 1 == len(final_lines):
            stripped_lines.append(line)
        else:
            stripped_lines.append(line.rstrip())
    # Join it all together
    wrapped = '\n'.join(stripped_lines)
    if lstrip:
        wrapped = wrapped.lstrip()
    return wrapped
