"""Generate a schema wrapper from a schema"""
import sys
import json
from datetime import datetime
from os.path import abspath, join, dirname

# import schemapi from here
sys.path.insert(0, abspath(dirname(__file__)))
from schemapi.codegen import schema_class, CodeSnippet
from schemapi.utils import get_valid_identifier, SchemaInfo


LOAD_SCHEMA = '''
import os
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, '..', 'vega-lite-schema.json')) as f:
        return json.load(f)
'''

FIELD_TEMPLATE = '''
class {classname}(core.{basename}):
    """{classname} channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super({classname}, self).__init__(**kwds)
'''

VALUE_TEMPLATE = '''
class {classname}Value(core.{basename}):
    """{classname} channel"""
    def __init__(self, value, *args, **kwargs):
        super({classname}Value, self).__init__(value=value, *args, **kwargs)
'''


def copy_schemapi_util():
    source_path = abspath(join(dirname(__file__), 'schemapi', 'schemapi.py'))
    destination_path = abspath(join(dirname(__file__), '..', 'altair',
                                    'utils', 'schemapi.py'))
    print("Copying\n {0}\n  -> {1}".format(source_path, destination_path))

    content = ["# The contents of this file are automatically written by\n",
               "# tools/generate_schema_wrapper.py. Do not modify directly\n"
               "# {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))]

    with open(source_path, 'r') as f:
        content += f.readlines()

    with open(destination_path, 'w') as f:
        f.writelines(content)


def generate_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    with open(schema_file) as f:
        schema = json.load(f)
    contents = ["# The contents of this file are automatically generated",
                "# at time {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                "from altair.utils.schemapi import SchemaBase, Undefined",
                LOAD_SCHEMA]
    contents.append(schema_class('Root', schema=schema,
                                 schemarepr=CodeSnippet('load_schema()')))
    for name in schema['definitions']:
        defschema = {'$ref': '#/definitions/' + name,
                     'definitions': schema['definitions']}
        defschema_repr = {'$ref': '#/definitions/' + name}

        contents.append(schema_class(get_valid_identifier(name),
                                     schema=defschema, schemarepr=defschema_repr,
                                     rootschema=CodeSnippet("Root._schema")))
    contents.append('')  # end with newline
    return '\n'.join(contents)

def generate_vegalite_channel_wrappers(schemafile, imports=None):
    with open(schemafile) as f:
        schema = json.load(f)
    if imports is None:
            imports = ["from . import core",
                       "from altair.utils import parse_shorthand"]
    contents = ["# The contents of this file are automatically generated",
                "# {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))]
    contents.extend(imports)
    contents.append('')

    encoding = SchemaInfo(schema['definitions']['EncodingWithFacet'])

    for prop, propschema in encoding.properties.items():
        if '$ref' in propschema:
            definitions = [propschema['$ref']]
        elif 'anyOf' in propschema:
            definitions = [s['$ref'] for s in propschema['anyOf'] if '$ref' in s]
        else:
            raise ValueError("either $ref or anyOf expected")
        for definition in definitions:
            basename = definition.split('/')[-1]
            classname = prop.title()
            if 'Value' in basename:
                template = VALUE_TEMPLATE
            else:
                template = FIELD_TEMPLATE
            contents.append(template.format(classname=classname,
                                            basename=basename))
    return '\n'.join(contents)


# TODO: generate useful docstrings & simple unit tests


def main():
    copy_schemapi_util()

    for library in ['vegalite']:
        for version in ['v2']:
            path = abspath(join(dirname(__file__), '..',
                                'altair', library, version))
            schemafile = join(path, 'vega-lite-schema.json')

            # Generate __init__.py file
            outfile = join(path, 'schema', '__init__.py')
            print("Writing {0}".format(outfile))
            with open(outfile, 'w') as f:
                f.write("from .core import *\nfrom .channels import *")

            # Generate the core schema wrappers
            outfile = join(path, 'schema', 'core.py')
            print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
            file_contents = generate_schema_wrapper(schemafile)
            with open(outfile, 'w') as f:
                f.write(file_contents)

            # Generate the channel wrappers
            outfile = join(path, 'schema', 'channels.py')
            print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
            code = generate_vegalite_channel_wrappers(schemafile)
            with open(outfile, 'w') as f:
                f.write(code)


if __name__ == '__main__':
    main()
