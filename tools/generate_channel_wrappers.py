import sys
import json
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__))))
from schemapi import SchemaInfo

from datetime import datetime

FIELD_TEMPLATE = '''
class {classname}(schema.{basename}):
    """{classname} channel"""
    def __init__(self, field, **kwargs):
        kwds = parse_shorthand(field)
        kwds.update(kwargs)
        super({classname}, self).__init__(**kwds)
'''

VALUE_TEMPLATE = '''
class {classname}Value(schema.{basename}):
    """{classname} channel"""
    def __init__(self, value, *args, **kwargs):
        super({classname}Value, self).__init__(value=value, *args, **kwargs)
'''

def generate_vegalite_channel_wrappers(schemafile, imports=None):
    with open(schemafile) as f:
        schema = json.load(f)
    if imports is None:
            imports = ["from altair.vegalite.v2 import schema",
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


def main():
    for library in ['vegalite']:
        for version in ['v2']:
            path = abspath(join(dirname(__file__), '..',
                            'altair', library, version))
            schema_file = join(path, 'vega-lite-schema.json')
            out_file = join(path, 'channels.py')
            print("Generating\n {0}\n  ->{1}".format(schema_file, out_file))
            code = generate_channel_wrappers(schema_file)
            with open(out_file, 'w') as f:
                f.write(code)


if __name__ == '__main__':
    main()
