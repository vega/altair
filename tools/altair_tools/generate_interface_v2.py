"""Generate the Altair interface for Vega-Lite Version 1"""

import os
import shutil
from datetime import datetime
from itertools import chain
from collections import defaultdict
import copy

import jinja2

from schemapi import JSONSchema, JSONSchemaPlugin
from schemapi.utils import load_dynamic_module, save_module


from .utils import get_git_commit_info

# Encoding classes are those whose properties are simply a list of channels.
ENCODING_CLASSES = ['Encoding', 'EncodingWithFacet', 'Facet']


def channel_classes(schema, encoding_classes=ENCODING_CLASSES):
    """
    Find mapping of named channel classes to their base class name.
    For example:

    {'X': 'PositionFieldDef',
     'X2': 'FieldDef',
     'Color': 'ConditionalStringLegendDef',
     ...}
    """
    channels = {}
    wrapped_defs = schema.wrapped_definitions()
    for encoding_class in encoding_classes:
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


def channel_bases(schema, encoding_classes=ENCODING_CLASSES):
    """
    Return a sorted list of all unique channel base classes
    """
    return sorted(set(channel_classes(schema, encoding_classes).values()))


CHANNEL_WRAPPER_TEMPLATE = '''# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: {{ version }}
# - date: {{ date }}

import pandas as pd

from . import jstraitlets as jst
from . import schema
from ...traitlet_utils import parse_shorthand, infer_vegalite_type


{% for obj in objects -%}
class {{ obj.classname }}(schema.{{ obj.base.classname }}):
    """Wrapper for Vega-Lite {{ obj.base.classname }} definition.
    {{ obj.base.indented_description(1) }}
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    {%- for (name, prop) in obj.base.wrapped_properties().items() %}
    {{ name }} : {{ prop.type_description }}
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
    encoding_classes = ENCODING_CLASSES

    def wrapped_channel_classes(self, schema):
        """return a dictionary of channel base class info"""
        for base in channel_bases(schema, self.encoding_classes):
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
from .schema import NumberValueDef  # needed for channel collections import

{% for object in objects -%}
class {{ object.classname }}(channel_wrappers.{{ object.basename }}):
    pass


{% endfor -%}
'''

class NamedChannelPlugin(JSONSchemaPlugin):
    encoding_classes = ENCODING_CLASSES

    def module_imports(self, schema):
        return['from .named_channels import {0}'.format(name)
               for name in sorted(channel_classes(schema, self.encoding_classes))]

    def code_files(self, schema):
        template = jinja2.Template(NAMED_CHANNEL_TEMPLATE)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        version = get_git_commit_info()

        objects = [{'classname': name, 'basename': base.replace('Def', '')}
                   for (name, base)
                   in sorted(channel_classes(schema, self.encoding_classes).items())]
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
    {{ name }}: {{ prop.type_description }}
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
    encoding_classes = ENCODING_CLASSES

    def get_base(self, schema):
        if '$ref' in schema:
            return schema['$ref'].rsplit('/', 1)[-1]
        for subschema in schema.get('anyOf', []):
            if '$ref' in subschema:
                return subschema['$ref'].rsplit('/', 1)[-1]
        raise ValueError("Cannot get base for schema {0}".format(schema))

    def replace_base_with_name(self, name, basename, schema):
        schema = copy.deepcopy(schema)
        if '$ref' in schema:
            path, oldname = schema['$ref'].rsplit('/', 1)
            if oldname == basename:
                schema['$ref'] = '/'.join([path, name])
        if 'anyOf' in schema:
            schema['anyOf'] = [self.replace_base_with_name(name, basename, subschema)
                               for subschema in schema['anyOf']]
        if schema.get('type', None) == 'array':
            schema['items'] = self.replace_base_with_name(name, basename, schema['items'])
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
                obj.properties[name] = self.replace_base_with_name(name.title(), basename, prop)
            objects.append(obj)

        return {'channel_collections.py': template.render(date=date,
                                                          version=version,
                                                          objects=objects)}


def generate_interface_v2(schema_path,
                          schemafile='vega-lite-schema.json',
                          module='_interface'):
    if not os.path.exists(schema_path):
        raise ValueError("'{0}' does not exist".format(path))

    schemafile = os.path.join(schema_path, schemafile)
    modulepath = os.path.join(schema_path, module)

    if os.path.exists(modulepath):
        shutil.rmtree(modulepath)

    # Save the basic schema wrappers
    schema = JSONSchema.from_json_file(schemafile)
    schema.add_plugins(ChannelWrapperPlugin(),
                       NamedChannelPlugin(),
                       ChannelCollectionPlugin())
    schema.write_module(modulename=module,
                        location=os.path.abspath(schema_path),
                        quiet=False)
