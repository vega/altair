"""Generate a schema wrapper from a schema"""
import copy
import os
import sys
import json
from datetime import datetime
from os.path import abspath, join, dirname

from urllib import request

# import schemapi from here
sys.path.insert(0, abspath(dirname(__file__)))
from schemapi import codegen
from schemapi.codegen import schema_class, CodeSnippet
from schemapi.utils import get_valid_identifier, SchemaInfo, indent_arglist

SCHEMA_URL_TEMPLATE = ('https://vega.github.io/schema/'
                       '{library}/{version}.json')

SCHEMA_VERSION = {
    'vega': {
        'v2': 'v2.6.5',
        'v3': 'v3.2.1'
    },
    'vega-lite': {
        'v1': 'v1.3.1',
        'v2': 'v2.3.0'
    }
}


BASE_SCHEMA = """
class {basename}(SchemaBase):
    @classmethod
    def _default_wrapper_classes(cls):
        return {basename}.__subclasses__()
"""

LOAD_SCHEMA = '''
import pkgutil
import json

def load_schema():
    """Load the json schema associated with this module's functions"""
    return json.loads(pkgutil.get_data(__name__, '{schemafile}').decode())
'''

FIELD_TEMPLATE = '''
class {classname}(core.{basename}):
    """{docstring}"""
    _class_is_valid_at_instantiation = False

    {init_code}

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {{}}
        if self.shorthand is Undefined:
            kwds = {{}}
        elif isinstance(self.shorthand, six.string_types):
            kwds = parse_shorthand(self.shorthand, data=context.get('data', None))
            type_defined = self._kwds.get('type', Undefined) is not Undefined
            if not (type_defined or 'type' in kwds):
                if isinstance(context.get('data', None), pd.DataFrame):
                    raise ValueError("{{0}} encoding field is specified without a type; "
                                     "the type cannot be inferred because it does not "
                                     "match any column in the data.".format(self.shorthand))
                else:
                    raise ValueError("{{0}} encoding field is specified without a type; "
                                     "the type cannot be automacially inferred because "
                                     "the data is not specified as a pandas.DataFrame."
                                     "".format(self.shorthand))
        else:
            # shorthand is not a string; we pass the definition to field
            if self.field is not Undefined:
                raise ValueError("both shorthand and field specified in {{0}}"
                                 "".format(self.__class__.__name__))
            # field is a RepeatSpec or similar; cannot infer type
            kwds = {{'field': self.shorthand}}

        # set shorthand to Undefined, because it's not part of the schema
        self.shorthand = Undefined
        self._kwds.update({{k: v for k, v in kwds.items()
                           if self._kwds.get(k, Undefined) is Undefined}})
        return super({classname}, self).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)
'''

VALUE_TEMPLATE = '''
class {classname}(core.{basename}):
    """{docstring}"""
    _class_is_valid_at_instantiation = False

    {init_code}

    def to_dict(self, validate=True, ignore=(), context=None):
        context = context or {{}}
        condition = getattr(self, 'condition', Undefined)
        copy = self  # don't copy unless we need to
        if condition is not Undefined:
            if isinstance(condition, core.SchemaBase):
                pass
            elif 'field' in condition and 'type' not in condition:
                kwds = parse_shorthand(condition['field'], context.get('data', None))
                copy = self.copy()
                copy.condition.update(kwds)
        return super({classname}, copy).to_dict(validate=validate,
                                                ignore=ignore,
                                                context=context)
'''


HEADER = """\
# -*- coding: utf-8 -*-
#
# The contents of this file are automatically written by
# tools/generate_schema_wrapper.py. Do not modify directly.
"""


def schema_url(library, version):
    version = SCHEMA_VERSION[library][version]
    return SCHEMA_URL_TEMPLATE.format(library=library, version=version)


def download_schemafile(library, version, schemapath):
    url = schema_url(library, version)
    filename = os.path.join(schemapath, '{library}-schema.json'.format(library=library))
    request.urlretrieve(url, filename)
    return filename


def copy_schemapi_util():
    """
    Copy the schemapi utility and its test file into altair/utils/
    """
    # copy the schemapi utility file
    source_path = abspath(join(dirname(__file__), 'schemapi', 'schemapi.py'))
    destination_path = abspath(join(dirname(__file__), '..', 'altair',
                                    'utils', 'schemapi.py'))

    print("Copying\n {0}\n  -> {1}".format(source_path, destination_path))
    with open(source_path, 'r', encoding='utf8') as source:
        with open(destination_path, 'w', encoding='utf8') as dest:
            dest.write(HEADER)
            dest.writelines(source.readlines())

    # Copy the schemapi test file
    source_path = abspath(join(dirname(__file__), 'schemapi',
                               'tests', 'test_schemapi.py'))
    destination_path = abspath(join(dirname(__file__), '..', 'altair',
                                    'utils', 'tests', 'test_schemapi.py'))

    print("Copying\n {0}\n  -> {1}".format(source_path, destination_path))
    with open(source_path, 'r', encoding='utf8') as source:
        with open(destination_path, 'w', encoding='utf8') as dest:
            dest.write(HEADER)
            dest.writelines(source.readlines())


def generate_vegalite_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    basename = 'VegaLiteSchema'

    with open(schema_file, encoding='utf8') as f:
        rootschema = json.load(f)
    contents = [HEADER,
                "from altair.utils.schemapi import SchemaBase, Undefined",
                LOAD_SCHEMA.format(schemafile='vega-lite-schema.json')]
    contents.append(BASE_SCHEMA.format(basename=basename))
    contents.append(schema_class('Root', schema=rootschema, basename=basename,
                                 schemarepr=CodeSnippet('load_schema()')))

    for name in rootschema['definitions']:
        defschema = {'$ref': '#/definitions/' + name}
        defschema_repr = {'$ref': '#/definitions/' + name}

        contents.append(schema_class(get_valid_identifier(name),
                                     schema=defschema, schemarepr=defschema_repr,
                                     rootschema=rootschema, basename=basename,
                                     rootschemarepr=CodeSnippet("Root._schema")))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def generate_vega_schema_wrapper(schema_file):
    """Generate a schema wrapper at the given path."""
    # TODO: generate simple tests for each wrapper
    basename = 'VegaSchema'

    with open(schema_file, encoding='utf8') as f:
        rootschema = json.load(f)
    contents = [HEADER,
                "from altair.utils.schemapi import SchemaBase, Undefined",
                LOAD_SCHEMA.format(schemafile='vega-schema.json')]
    contents.append(BASE_SCHEMA.format(basename=basename))
    contents.append(schema_class('Root', schema=rootschema, basename=basename,
                                 schemarepr=CodeSnippet('load_schema()')))
    for deflist in ['defs', 'refs']:
        for name in rootschema[deflist]:
            defschema = {'$ref': '#/{0}/{1}'.format(deflist, name)}
            defschema_repr = {'$ref': '#/{0}/{1}'.format(deflist,name)}
            contents.append(schema_class(get_valid_identifier(name),
                                         schema=defschema, schemarepr=defschema_repr,
                                         rootschema=rootschema, basename=basename,
                                         rootschemarepr=CodeSnippet("Root._schema")))
    contents.append('')  # end with newline
    return '\n'.join(contents)


def generate_vegalite_channel_wrappers(schemafile, imports=None,
                                       encoding_def='Encoding'):
    # TODO: generate __all__ for top of file
    with open(schemafile, encoding='utf8') as f:
        schema = json.load(f)
    if imports is None:
        imports = ["import six",
                   "from . import core",
                   "import pandas as pd",
                   "from altair.utils.schemapi import Undefined",
                   "from altair.utils import parse_shorthand"]
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
                nodefault = []
                defschema = copy.deepcopy(schema['definitions'][basename])
                defschema['properties']['shorthand'] = {'type': 'string',
                                                        'description': 'shorthand for field, aggregate, and type'}
                defschema['required'] = ['shorthand']
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


MARK_METHOD = '''
def mark_{mark}({def_arglist}):
    """Set the chart's mark to '{mark}'

    For information on additional arguments, see ``alt.MarkDef``
    """
    kwds = dict({dict_arglist})
    copy = self.copy(deep=True, ignore=['data'])
    if any(val is not Undefined for val in kwds.values()):
        copy.mark = core.MarkDef(type="{mark}", **kwds)
    else:
        copy.mark = "{mark}"
    return copy
'''


def generate_vegalite_mark_mixin(schemafile, mark_enum='Mark',
                                 mark_def='MarkDef'):
    with open(schemafile, encoding='utf8') as f:
        schema = json.load(f)
    marks = schema['definitions'][mark_enum]['enum']
    info = SchemaInfo({'$ref': '#/definitions/' + mark_def},
                      rootschema=schema)

    # adapted from SchemaInfo.init_code
    nonkeyword, required, kwds, invalid_kwds, additional = codegen._get_args(info)
    required -= {'type'}
    kwds -= {'type'}

    def_args = ['self'] + ['{0}=Undefined'.format(p)
                           for p in (sorted(required) + sorted(kwds))]
    dict_args = ['{0}={0}'.format(p)
                 for p in (sorted(required) + sorted(kwds))]

    if additional or invalid_kwds:
        def_args.append('**kwds')
        dict_args.append('**kwds')

    imports = ["from altair.utils.schemapi import Undefined",
               "from . import core"]

    code = ["class MarkMethodMixin(object):",
            '    """A mixin class that defines mark methods"""']

    for mark in marks:
        # TODO: only include args relevant to given type?
        mark_method = MARK_METHOD.format(mark=mark,
                                         def_arglist=indent_arglist(def_args, indent_level=10 + len(mark)),
                                         dict_arglist=indent_arglist(dict_args, indent_level=16))
        code.append('\n    '.join(mark_method.splitlines()))

    return imports, '\n'.join(code)


CONFIG_METHOD = """
@use_signature(core.{classname})
def {method}(self, *args, **kwargs):
    copy = self.copy()
    copy.config = core.{classname}(*args, **kwargs)
    return copy
"""

CONFIG_PROP_METHOD = """
@use_signature(core.{classname})
def configure_{prop}(self, *args, **kwargs):
    copy = self.copy(deep=False)
    if copy.config is Undefined:
        copy.config = core.Config()
    else:
        copy.config = copy.config.copy(deep=False)
    copy.config["{prop}"] = core.{classname}(*args, **kwargs)
    return copy
"""


def generate_vegalite_config_mixin(schemafile):
    imports = ["from . import core",
               "from altair.utils import use_signature"]
    code = ["class ConfigMethodMixin(object):",
            '    """A mixin class that defines config methods"""']
    with open(schemafile, encoding='utf8') as f:
        schema = json.load(f)
    info = SchemaInfo({'$ref': '#/definitions/Config'},
                      rootschema=schema)

    # configure() method
    method = CONFIG_METHOD.format(classname='Config', method='configure')
    code.append('\n    '.join(method.splitlines()))

    # configure_prop() methods
    for prop, prop_info in info.properties.items():
        classname = prop_info.refname
        if classname:
            method = CONFIG_PROP_METHOD.format(classname=classname,
                                               prop=prop)
            code.append('\n    '.join(method.splitlines()))
    return imports, '\n'.join(code)


def vegalite_main():
    library = 'vega-lite'
    encoding_defs = {'v1': 'Encoding', 'v2': 'EncodingWithFacet'}

    for version in ['v1', 'v2']:
        path = abspath(join(dirname(__file__), '..',
                            'altair', 'vegalite', version))
        schemapath = os.path.join(path, 'schema')
        schemafile = download_schemafile(library=library,
                                         version=version,
                                         schemapath=schemapath)

        # Generate __init__.py file
        outfile = join(schemapath, '__init__.py')
        print("Writing {0}".format(outfile))
        with open(outfile, 'w', encoding='utf8') as f:
            f.write("from .core import *\nfrom .channels import *\n")
            f.write("SCHEMA_VERSION = {0!r}\n"
                    "".format(SCHEMA_VERSION[library][version]))
            f.write("SCHEMA_URL = {0!r}\n"
                    "".format(schema_url(library, version)))

        # Generate the core schema wrappers
        outfile = join(schemapath, 'core.py')
        print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
        file_contents = generate_vegalite_schema_wrapper(schemafile)
        with open(outfile, 'w', encoding='utf8') as f:
            f.write(file_contents)

        # Generate the channel wrappers
        outfile = join(schemapath, 'channels.py')
        print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
        code = generate_vegalite_channel_wrappers(schemafile, encoding_def=encoding_defs[version])
        with open(outfile, 'w', encoding='utf8') as f:
            f.write(code)

        if version != 'v1':
            # generate the mark mixin
            outfile = join(schemapath, 'mixins.py')
            print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
            mark_imports, mark_mixin = generate_vegalite_mark_mixin(schemafile)
            config_imports, config_mixin = generate_vegalite_config_mixin(schemafile)
            imports = sorted(set(mark_imports + config_imports))
            with open(outfile, 'w', encoding='utf8') as f:
                f.write(HEADER)
                f.write('\n'.join(imports))
                f.write('\n\n\n')
                f.write(mark_mixin)
                f.write('\n\n\n')
                f.write(config_mixin)


def vega_main():
    library = 'vega'

    for version in ['v2', 'v3']:
        path = abspath(join(dirname(__file__), '..',
                            'altair', 'vega', version))
        schemapath = os.path.join(path, 'schema')
        schemafile = download_schemafile(library=library,
                                         version=version,
                                         schemapath=schemapath)

        # Generate __init__.py file
        outfile = join(schemapath, '__init__.py')
        print("Writing {0}".format(outfile))
        with open(outfile, 'w', encoding='utf8') as f:
            f.write("from .core import *\n\n")
            f.write("SCHEMA_VERSION = {0!r}\n"
                    "".format(SCHEMA_VERSION[library][version]))
            f.write("SCHEMA_URL = {0!r}\n"
                    "".format(schema_url(library, version)))

        # Generate the core schema wrappers
        outfile = join(schemapath, 'core.py')
        print("Generating\n {0}\n  ->{1}".format(schemafile, outfile))
        file_contents = generate_vega_schema_wrapper(schemafile)
        with open(outfile, 'w', encoding='utf8') as f:
            f.write(file_contents)


if __name__ == '__main__':
    copy_schemapi_util()
    vegalite_main()
    vega_main()
