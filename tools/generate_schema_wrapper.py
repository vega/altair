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
    with open(os.path.join(directory, 'vega-lite-schema.json')) as f:
        return json.load(f)
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
    contents.append(schema_class('Root', schema, CodeSnippet('load_schema()')))
    for name in schema['definitions']:
        defschema = {'$ref': '#/definitions/' + name,
                     'definitions': schema['definitions']}
        defschema_repr = {'$ref': '#/definitions/' + name,
                          'definitions': CodeSnippet("Root._Root__schema['definitions']")}

        contents.append(schema_class(get_valid_identifier(name),
                        defschema, defschema_repr))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def main():
    copy_schemapi_util()
    for library in ['vegalite']:
        for version in ['v2']:
            path = abspath(join(dirname(__file__), '..',
                                'altair', library, version))
            schema_file = join(path, 'vega-lite-schema.json')
            out_file = join(path, 'schema.py')
            print("Generating\n {0}\n  ->{1}".format(schema_file, out_file))
            file_contents = generate_schema_wrapper(schema_file)
            with open(out_file, 'w') as f:
                f.write(file_contents)


if __name__ == '__main__':
    main()
