"""Generate a schema wrapper from a schema"""
import sys
import json
from datetime import datetime
from os.path import abspath, join, dirname

# import schemapi from here
sys.path.insert(0, abspath(dirname(__file__)))
from schemapi import codegen
from schemapi.codegen import schema_class, CodeSnippet
from schemapi.utils import get_valid_identifier, SchemaInfo


LOAD_SCHEMA = '''
import os
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, '..', '{schemafile}')) as f:
        return json.load(f)
'''

FIELD_TEMPLATE = '''
class {classname}(core.{basename}):
    """{docstring}"""
    {init_code}

    def to_dict(self, validate=True, ignore=[], context={{}}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super({classname}, self).to_dict(validate=validate, ignore=ignore, context=context)
'''

VALUE_TEMPLATE = '''
class {classname}(core.{basename}):
    """{docstring}"""
    {init_code}
'''


HEADER = """\
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
# {0}
""".format(datetime.now().strftime('%Y-%m-%d %H:%M'))


def copy_schemapi_util():
    """
    Copy the schemapi utility and its test file into altair/utils/
    """
    # copy the schemapi utility file
    source_path = abspath(join(dirname(__file__), 'schemapi', 'schemapi.py'))
    destination_path = abspath(join(dirname(__file__), '..', 'altair',
                                    'utils', 'schemapi.py'))

    print("Copying\n {0}\n  -> {1}".format(source_path, destination_path))
    with open(source_path, 'r') as source:
        with open(destination_path, 'w') as dest:
            dest.write(HEADER)
            dest.writelines(source.readlines())

    # Copy the schemapi test file
    source_path = abspath(join(dirname(__file__), 'schemapi',
                               'tests', 'test_schemapi.py'))
    destination_path = abspath(join(dirname(__file__), '..', 'altair',
                                    'utils', 'tests', 'test_schemapi.py'))

    print("Copying\n {0}\n  -> {1}".format(source_path, destination_path))
    with open(source_path, 'r') as source:
        with open(destination_path, 'w') as dest:
            dest.write(HEADER)
            dest.writelines(source.readlines())


def generate_vegalite_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    with open(schema_file) as f:
        rootschema = json.load(f)
    contents = [HEADER,
                "from altair.utils.schemapi import SchemaBase, Undefined",
                LOAD_SCHEMA.format(schemafile='vega-lite-schema.json')]
    contents.append(schema_class('Root', schema=rootschema,
                                 schemarepr=CodeSnippet('load_schema()')))
    for name in rootschema['definitions']:
        defschema = {'$ref': '#/definitions/' + name}
        defschema_repr = {'$ref': '#/definitions/' + name}

        contents.append(schema_class(get_valid_identifier(name),
                                     schema=defschema, schemarepr=defschema_repr,
                                     rootschema=rootschema,
                                     rootschemarepr=CodeSnippet("Root._schema")))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def generate_vega_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    with open(schema_file) as f:
        rootschema = json.load(f)
    contents = [HEADER,
                "from altair.utils.schemapi import SchemaBase, Undefined",
                LOAD_SCHEMA.format(schemafile='vega-schema.json')]
    contents.append(schema_class('Root', schema=rootschema,
                                 schemarepr=CodeSnippet('load_schema()')))
    for deflist in ['defs', 'refs']:
        for name in rootschema[deflist]:
            defschema = {'$ref': '#/{0}/{1}'.format(deflist, name)}
            defschema_repr = {'$ref': '#/{0}/{1}'.format(deflist,name)}
            contents.append(schema_class(get_valid_identifier(name),
                                         schema=defschema, schemarepr=defschema_repr,
                                         rootschema=rootschema,
                                         rootschemarepr=CodeSnippet("Root._schema")))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def generate_vegalite_channel_wrappers(schemafile, imports=None,
                                       encoding_def='Encoding'):
    # TODO: generate __all__ for top of file
    with open(schemafile) as f:
        schema = json.load(f)
    if imports is None:
        imports = ["from . import core",
                   "from altair.utils.schemapi import Undefined",
                   "from altair.utils import parse_shorthand, parse_shorthand_plus_data"]
    contents = [HEADER]
    contents.extend(imports)
    contents.append('')

    encoding = SchemaInfo(schema['definitions'][encoding_def],
                          rootschema=schema)

    for prop, propschema in encoding.properties.items():
        if propschema.is_reference():
            definitions = [propschema.ref]
        elif propschema.is_anyOf():
            definitions = [s.ref for s in propschema.anyOf if s.is_reference()]
        else:
            raise ValueError("either $ref or anyOf expected")
        for definition in definitions:
            defschema = {'$ref': definition}
            basename = definition.split('/')[-1]
            classname = prop.title()

            if 'Value' in basename:
                template = VALUE_TEMPLATE
                classname += 'Value'
                nodefault = ['value']
            else:
                template = FIELD_TEMPLATE
                nodefault = ['field']
            docstring = codegen.docstring(classname=classname, schema=defschema,
                                          rootschema=schema, indent=4)
            init_code = codegen.init_code(classname=classname, schema=defschema,
                                          rootschema=schema, indent=4,
                                          nodefault=nodefault).rstrip()
            contents.append(template.format(classname=classname,
                                            basename=basename,
                                            docstring=docstring,
                                            init_code=init_code))
    return '\n'.join(contents)


def vegalite_main():
    encoding_defs = {'v1': 'Encoding', 'v2': 'EncodingWithFacet'}

    for version in ['v1', 'v2']:
        path = abspath(join(dirname(__file__), '..',
                            'altair', 'vegalite', version))
        schemafile = join(path, 'vega-lite-schema.json')

        # Generate __init__.py file
        outfile = join(path, 'schema', '__init__.py')
        print("Writing {0}".format(outfile))
        with open(outfile, 'w') as f:
            f.write("from .core import *\nfrom .channels import *")

        # Generate the core schema wrappers
        outfile = join(path, 'schema', 'core.py')
        print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
        file_contents = generate_vegalite_schema_wrapper(schemafile)
        with open(outfile, 'w') as f:
            f.write(file_contents)

        # Generate the channel wrappers
        outfile = join(path, 'schema', 'channels.py')
        print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
        code = generate_vegalite_channel_wrappers(schemafile, encoding_def=encoding_defs[version])
        with open(outfile, 'w') as f:
            f.write(code)


def vega_main():
    for version in ['v2', 'v3']:
        path = abspath(join(dirname(__file__), '..',
                            'altair', 'vega', version))
        schemafile = join(path, 'vega-schema.json')

        # Generate __init__.py file
        outfile = join(path, 'schema', '__init__.py')
        print("Writing {0}".format(outfile))
        with open(outfile, 'w') as f:
            f.write("from .core import *")

        # Generate the core schema wrappers
        outfile = join(path, 'schema', 'core.py')
        print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
        file_contents = generate_vega_schema_wrapper(schemafile)
        with open(outfile, 'w') as f:
            f.write(file_contents)


if __name__ == '__main__':
    copy_schemapi_util()
    vegalite_main()
    vega_main()
