"""
Wrap the altair schema and save to a source tree
"""
import subprocess
import os
import shutil
from datetime import datetime
from itertools import chain
from collections import defaultdict
import copy

import jinja2

from altair_parser import JSONSchema, JSONSchemaPlugin
from altair_parser.utils import load_dynamic_module, save_module


def get_git_commit_info():
    """Return a string describing the git version information"""
    try:
        label = subprocess.check_output(["git", "describe"]).decode().strip()
    except subprocess.CalledProcessError:
        label = "<unavailable>"
    return label


CHANNEL_WRAPPER_TEMPLATE = '''# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: {{ version }}
# - date: {{ date }}

import pandas as pd

from . import jstraitlets as jst
from . import schema
from ...utils import parse_shorthand, infer_vegalite_type


{% for obj in objects -%}
class {{ obj.classname }}(schema.{{ obj.base.classname }}):
    """Wrapper for Vega-Lite {{ obj.base.classname }} definition.
    {{ obj.base.indented_description(1) }}
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    {%- for (name, prop) in obj.base.wrapped_properties().items() %}
    {{ name }} : {{ prop.type }}
        {{ prop.indented_description() }}
    {%- endfor %}
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    {%- set comma = joiner(", ") %}
    def __init__(self, shorthand='', {% for name in obj.base.wrapped_properties() %}{{ name }}=jst.undefined, {% endfor %}**kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict({% for name in obj.base.wrapped_properties() %}{{ comma() }}{{ name }}={{ name }}{% endfor %})
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super({{ obj.classname }}, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super({{ obj.classname }}, self)._finalize(**kwargs)


{% endfor %}
'''

class ChannelWrapperPlugin(JSONSchemaPlugin):
    encoding_classes = ['Encoding', 'UnitEncoding', 'Facet']

    def channel_classes(self, schema):
        """return the list of channel class names"""
        channels = set()
        wrapped_defs = schema.wrapped_definitions()
        for encoding_class in self.encoding_classes:
            childschema = schema.make_child(schema.definitions[encoding_class])
            for prop, propschema in childschema.wrapped_properties().items():
                if not propschema.is_reference:
                    subschemas = (propschema.make_child(s)
                                  for s in propschema['anyOf'])
                    propschema = next((sub for sub in subschemas
                                       if sub.is_reference), None)
                    if propschema is None:
                        raise ValueError("Could not find classname for "
                                         "property '{0}'".format(prop))
                channels.add(propschema.classname)
        return sorted(channels)

    def wrapped_channel_classes(self, schema):
        """return a dictionary of channel base class info"""
        for base in self.channel_classes(schema):
            yield dict(classname=base.replace('Def', ''),
                       base=schema.wrapped_definitions()[base.lower()],
                       root='channel_wrappers')

    def module_imports(self, schema):
        return ['from .channel_wrappers import {0}'.format(cls['classname'])
                for cls in self.wrapped_channel_classes(schema)]

    def code_files(self, schema):
        template = jinja2.Template(CHANNEL_WRAPPER_TEMPLATE)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        version = get_git_commit_info()
        objects = self.wrapped_channel_classes(schema)
        return {'channel_wrappers.py': template.render(date=date,
                                                       version=version,
                                                       objects=objects)}


NAMED_CHANNEL_TEMPLATE = '''# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: {{ version }}
# - date: {{ date }}

from . import channel_wrappers

{% for object in objects -%}
class {{ object.classname }}(channel_wrappers.{{ object.basename }}):
    pass


{% endfor -%}
'''

class NamedChannelPlugin(JSONSchemaPlugin):
    encoding_classes = ['Encoding', 'UnitEncoding', 'Facet']

    def channel_classes(self, schema):
        """return the list of channel class names"""
        channels = {}
        wrapped_defs = schema.wrapped_definitions()
        for encoding_class in self.encoding_classes:
            childschema = schema.make_child(schema.definitions[encoding_class])
            for prop, propschema in childschema.wrapped_properties().items():
                if not propschema.is_reference:
                    subschemas = (propschema.make_child(s)
                                  for s in propschema['anyOf'])
                    propschema = next((sub for sub in subschemas
                                       if sub.is_reference), None)
                    if propschema is None:
                        raise ValueError("Could not find classname for "
                                         "property '{0}'".format(prop))
                channels[prop.title()] = propschema.classname
        return channels

    def module_imports(self, schema):
        return['from .named_channels import {0}'.format(name)
               for name in sorted(self.channel_classes(schema))]

    def code_files(self, schema):
        template = jinja2.Template(NAMED_CHANNEL_TEMPLATE)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        version = get_git_commit_info()

        objects = [{'classname': name, 'basename': base.replace('Def', '')}
                   for (name, base)
                   in sorted(self.channel_classes(schema).items())]
        return {'named_channels.py': template.render(date=date,
                                                     version=version,
                                                     objects=objects)}



CHANNEL_COLLECTION_TEMPLATE = '''# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: {{ version }}
# - date: {{ date }}

import traitlets as T
from . import jstraitlets as jst
from . import schema


def _localname(name):
    return '.'.join(__name__.split('.')[:-1] + ['named_channels', name])


{% for obj in objects -%}
class {{ obj.classname }}(schema.{{ obj.classname }}):
    """Object for storing channel encodings

    Attributes
    ----------
    {% for (name, prop) in obj.wrapped_properties().items() -%}
    {{ name }}: {{ prop.type }}
        {{ prop.indented_description() }}
    {% endfor -%}
    """
    _skip_on_export = ['channel_names']
    {%- set comma = joiner(", ") %}
    channel_names = [{% for name, prop in obj.wrapped_properties().items() %}{{ comma() }}'{{ name }}'{% endfor %}]
    {% for (name, prop) in obj.wrapped_properties().items() %}
    {{ name }} = {{ prop.trait_code }}
    {%- endfor %}


{% endfor -%}
'''


class ChannelCollectionPlugin(JSONSchemaPlugin):
    encoding_classes = ['Encoding', 'UnitEncoding', 'Facet']

    def get_base(self, schema):
        if '$ref' in schema:
            return schema['$ref'].rsplit('/', 1)[-1]
        for subschema in schema.get('anyOf', []):
            if '$ref' in subschema:
                return subschema['$ref'].rsplit('/', 1)[-1]
        raise ValueError("Cannot get base for schema {0}".format(schema))

    def replace_base_with_name(self, name, schema):
        schema = copy.deepcopy(schema)
        if '$ref' in schema:
            a, b = schema['$ref'].rsplit('/', 1)
            schema['$ref'] = '/'.join([a, name])
        if 'anyOf' in schema:
            schema['anyOf'] = [self.replace_base_with_name(name, subschema)
                               for subschema in schema['anyOf']]
        if schema.get('type', None) == 'array':
            schema['items'] = self.replace_base_with_name(name, schema['items'])
        return schema

    def module_imports(self, schema):
        return ['from .channel_collections import {0}'.format(name)
                for name in self.encoding_classes]

    def code_files(self, schema):
        # This creates a specialization of each of the encoding classes, where
        # the generic channel names are replaced by named classes derived
        # from the channels (in named_channels.py)
        # We do this by copying and modifying the schema dictionary before
        # generating the code for these three classes.
        template = jinja2.Template(CHANNEL_COLLECTION_TEMPLATE)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        version = get_git_commit_info()

        # Here's where the schema is copied: we use a deep copy because we
        # are going to modify pieces of the dictionary.
        toplevel = schema.copy(deepcopy=True)

        # Now we cycle though the encoding classes and modify their schema
        # dictionaries, such that the properties point to the named channel
        # definitions rather than pointing to the generic channel definitions.
        objects = []
        definitions = toplevel.wrapped_definitions()
        for classname in self.encoding_classes:
            obj = definitions[classname.lower()]
            for name, prop in obj.properties.items():
                basename = self.get_base(prop)
                # add a new definition
                toplevel.definitions[name.title()] = toplevel.definitions[basename]
                # rewrite the object schema to point to this definition
                obj.properties[name] = self.replace_base_with_name(name.title(), prop)
            objects.append(obj)

        return {'channel_collections.py': template.render(date=date,
                                                          version=version,
                                                          objects=objects)}


def write_wrappers():
    # TODO: use vega-schema repo locally
    schemafile = '../altair/schema/vega-lite-schema.json'
    module = '_interface'
    filepath = os.path.dirname(__file__)

    path = os.path.abspath(os.path.join(filepath, '..', 'altair', 'schema'))
    fullpath = os.path.join(path, module)
    schemafile = os.path.abspath(os.path.join(filepath, schemafile))

    if not os.path.exists(path):
        raise ValueError("'{0}' does not exist".format(path))

    if os.path.exists(fullpath):
        shutil.rmtree(fullpath)

    # Save the basic schema wrappers
    schema = JSONSchema.from_json_file(schemafile, module=module)
    schema.add_plugins(ChannelWrapperPlugin(),
                       NamedChannelPlugin(),
                       ChannelCollectionPlugin())
    schema.write_module(module=module, path=os.path.abspath(path), quiet=False)


if __name__ == '__main__':
    write_wrappers()
