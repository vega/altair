"""
Wrap the altair schema and save to a source tree
"""
import subprocess
import os
import shutil
from datetime import datetime
from itertools import chain
from collections import defaultdict

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


CHANNEL_WRAPPER_TEMPLATE = '''# Auto-generated file: do not modify directly
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
    skip = ['shorthand']

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
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super({{ obj.classname }}, self)._finalize(**kwargs)


{% endfor %}
'''

class ChannelWrapperPlugin(JSONSchemaPlugin):
    def encoding_classes(self, schema):
        """return the list of encoding class names"""
        return [name for name in schema.definitions if 'Encoding' in name]

    def channel_classes(self, schema):
        """return the list of channel class names"""
        channels = set()
        wrapped_defs = schema.wrapped_definitions()
        for encoding_class in self.encoding_classes(schema):
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
        return channels

    def wrapped_channel_classes(self, schema):
        """return a dictionary of channel base class info"""
        for base in self.channel_classes(schema):
            yield dict(classname=base.replace('Def', ''),
                       base=schema.wrapped_definitions()[base.lower()],
                       root='channel_wrappers')

    def module_imports(self, schema):
        return['from .channel_wrappers import {0}'.format(cls['classname'])
               for cls in self.wrapped_channel_classes(schema)]

    def code_files(self, schema):
        template = jinja2.Template(CHANNEL_WRAPPER_TEMPLATE)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        version = get_git_commit_info()
        objects = list(self.wrapped_channel_classes(schema))
        return {'channel_wrappers.py': template.render(date=date,
                                                       version=version,
                                                       objects=objects)}
    

NAMED_CHANNEL_TEMPLATE = '''# Auto-generated file: do not modify directly
# - altair version info: {{ version }}
# - date: {{ date }}

{% for import_statement in objects|merge_imports -%}
  {{ import_statement }}
{% endfor %}

{% for object in objects -%}
class {{ object.name }}({{ object.base.name }}):
    pass


{% endfor -%}
'''


CHANNEL_COLLECTION_TEMPLATE = '''# Auto-generated file: do not modify directly
# - altair version info: {{ version }}
# - date: {{ date }}


import traitlets as T

from .. import _interface as schema

{% for import_statement in objects|merge_imports -%}
  {{ import_statement }}
{% endfor %}

{% for cls in objects -%}
class {{ cls.name }}(schema.{{ cls.basename }}):
    """Object for storing channel encodings

    Attributes
    ----------
    {% for attr in cls.attributes -%}
    {{ attr.name }}: {{ attr.trait_descr }}
        {{ attr.short_description }}
    {% endfor -%}
    """
    {% for attr in cls.attributes -%}
    {{ attr.name }} = {{ attr.trait_fulldef }}
    {% endfor %}

    {%- set comma = joiner(", ") %}
    channel_names = [{% for attr in cls.attributes %}{{ comma() }}'{{ attr.name }}'{% endfor %}]
    skip = ['channel_names']


{% endfor -%}
'''
                                  

# TODO: use vega-schema repo locally
schemafile = '../altair/schema/vega-lite-schema.json'
module = '_interface'
path = os.path.abspath(os.path.join('..', 'altair', 'schema'))
fullpath = os.path.join(path, module)

if not os.path.exists(path):
    raise ValueError("'{0}' does not exist".format(path))

if os.path.exists(fullpath):
    shutil.rmtree(fullpath)

# Save the basic schema wrappers
schema = JSONSchema.from_json_file(schemafile, module=module)
schema.add_plugins(ChannelWrapperPlugin())
schema.write_module(module=module, path=os.path.abspath(path))

