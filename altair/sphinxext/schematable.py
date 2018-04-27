import importlib
import warnings

from docutils.parsers.rst import Directive
from docutils.statemachine import ViewList
from docutils import nodes
from sphinx.util.nodes import nested_parse_with_titles


def type_description(schema):
    """Return a concise type description for the given schema"""
    if schema == {}:
        return 'any'
    elif "$ref" in schema:
        return ":class:`{0}`".format(schema['$ref'].split('/')[-1])
    elif 'enum' in schema:
        return "[{0}]".format(', '.join(repr(s) for s in schema['enum']))
    elif 'type' in schema:
        if isinstance(schema['type'], list):
            return '[{0}]'.format(', '.join(schema['type']))
        elif schema['type'] == 'array':
            return 'array({0})'.format(type_description(schema.get('items', {})))
        elif schema['type'] == 'object':
            return 'dict'
        else:
            return schema['type']
    elif 'anyOf' in schema:
        return "anyOf({0})".format(', '.join(type_description(s)
                                             for s in schema['anyOf']))
    else:
        warnings.warn('cannot infer type for schema with keys {0}'
                      ''.format(schema.keys()))
        return '--'


def iter_properties(cls):
    """Iterate over (property, type, description)"""
    schema = cls.resolve_references(cls._schema)
    properties = schema.get('properties', {})
    for prop, propschema in properties.items():
        yield (prop,
               type_description(propschema),
               propschema.get('description', ' '))


def build_rst_table(rows, titles):
    """Build an rst table from a table of entries (i.e. list of lists)"""
    ncols = len(titles)
    assert all(len(row) == ncols for row in rows)

    lengths = [max(map(len, col)) for col in zip(*rows)]

    def make_line(row, fill=' '):
        return ' '.join(entry.ljust(length, fill)
                        for length, entry in zip(lengths, row))

    divider = make_line(ncols * [''], '=')

    return ([divider, make_line(titles), divider] +
            [make_line(row) for row in rows] +
            [divider])


def construct_schema_table(cls):
    """Construct an RST table describing the properties within a schema."""
    props = list(iter_properties(cls))
    names, types, defs = zip(*props)
    defs = [defn.replace('\n', ' ') for defn in defs]
    props = list(zip(names, types, defs))
    return build_rst_table(props, ["Property", "Type", "Description"])


class AltairObjectTableDirective(Directive):
    """
    Directive for building a table of attribute descriptions.

    Usage:

    .. altair-object-table:: altair.MarkConfig

    """
    has_content = False
    required_arguments = 1

    def run(self):
        objectname = self.arguments[0]
        modname, classname = objectname.rsplit('.', 1)
        module = importlib.import_module(modname)
        cls = getattr(module, classname)

        # create the table from the object
        table = construct_schema_table(cls)

        # parse and return documentation
        result = ViewList()
        for line in table:
            result.append(line, "<altair-class>")
        node = nodes.paragraph()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


def setup(app):
    app.add_directive('altair-object-table', AltairObjectTableDirective)
