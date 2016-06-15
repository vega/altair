import os
import json
import re
import copy
from itertools import chain, groupby
from collections import defaultdict
from operator import itemgetter

from jinja2 import Environment, FileSystemLoader, environmentfilter


def ensure_ascii_compatible(s):
    """Ensure a string is ascii-compatible.
    This is not an issue for Python 3, but if used in code will break Python 2
    """
    # Replace common non-ascii characters with suitable equivalents
    s = s.replace('\u2013', '-')
    s.encode('ascii')  # if this errors, then add more replacements above
    return s


@environmentfilter
def merge_imports(env, objects):
    """Jinja filter to merge all imports from a list of objects"""
    imports = chain(*(env.getattr(obj, 'imports') for obj in objects))
    modules = defaultdict(set)
    for imp in imports:
        modules[env.getattr(imp, 'module')] |= set(env.getattr(imp, 'names'))
    return ["from {0} import {1}".format(module, ', '.join(sorted(names)))
            for module, names in sorted(modules.items())]


def getpath(*args):
    """Get absolute path of joined directories relative to this file"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))


# Construct the jinja template environment
JINJA_ENV = Environment(loader=FileSystemLoader(getpath('templates')))
JINJA_ENV.filters['repr'] = repr
JINJA_ENV.filters['merge_imports'] = merge_imports

TYPE_MAP = {'oneOf': 'Union',
            "array": "List",
            "boolean": "Bool",
            "number": "CFloat",
            "string": "Unicode",
            "object": "Any",
            }

# Map class names to their bases
BASE_MAP = defaultdict(lambda: 'BaseObject')
BASE_MAP['ExtendedUnitSpec'] = 'UnitSpec'
BASE_MAP['Encoding'] = 'UnitEncoding'


CHANNEL_COLLECTIONS = ['Encoding', 'Facet']


class SchemaProperty(object):
    """Class Wrapper for a property in a VegaLite Schema

    This class exposes methods used in the templating.
    """
    def __init__(self, schema, name, top):
        self.name = name
        self.schema = schema
        self.top = top

        self.properties = {k: SchemaProperty(v, k, self.top)
                           for k, v in self.schema.get('properties',
                                                       {}).items()}

    @property
    def subtypes(self):
        if hasattr(self, '_subtypes'):
            return self._subtypes
        trait = self.trait_name
        if trait == 'Union':
            return [self.__class__(s, '', self.top)
                    for s in self.schema['oneOf']]
        elif trait == 'List':
            return [self.__class__(self.schema['items'], '', self.top)]
        else:
            return []

    @subtypes.setter
    def subtypes(self, arg):
        self._subtypes = arg

    def rename(self, newname):
        return self.__class__(self.schema, newname, self.top)

    def copy(self):
        return self.__class__(copy.deepcopy(self.schema), self.name, self.top)

    def replace_refs(self, dct, module=None):
        """Return a new object with all references replaced according to dct"""
        refname = self.refname
        if refname in dct:
            newname = dct[refname]
            self.top.definitions[newname] = self.top.definitions[refname]
            self.refname = newname
            if module is not None:
                self.module = module
        self.subtypes = [subtype.replace_refs(dct, module=module)
                        for subtype in self.subtypes]
        return self

    @property
    def type(self):
        if '$ref' in self.schema:
            return '$ref'
        elif 'oneOf' in self.schema:
            return 'oneOf'
        else:
            return self.schema.get('type', '')

    @property
    def trait_name(self):
        if self.refname:
            trait = self.top.definitions[self.refname].trait_name
            if trait == 'Any':
                return 'Instance'
            else:
                return self.refname
        else:
            return TYPE_MAP.get(self.type, "Any")

    @property
    def trait_descr(self):
        trait = self.trait_name
        if trait == 'Instance':
            return self.refname
        elif self.subtypes:
            return '{0}({1})'.format(trait, ', '.join(t.trait_descr
                                                      for t in self.subtypes))
        else:
            return trait

    def _trait_fulldef(self, kwds=('allow_none=True', 'default_value=None')):
        """This returns the full trait definition; e.g.

        T.List(T.CFloat(), allow_none=True, default_value=None,
               help="The offset (in pixels)"
        """
        kwds = list(kwds)
        trait = self.trait_name
        if 'minimum' in self.schema:
            kwds.append('min={0}'.format(self.schema['minimum']))
        if 'maximum' in self.schema:
            kwds.append('max={0}'.format(self.schema['maximum']))
        if self.description:
            kwds.append('help="""{0}"""'.format(self.short_description))

        def _join(kwds, precomma=False):
            if precomma and kwds:
                kwds = [''] + kwds
            return ', '.join(kwds)

        if trait == 'Union':
            return ('T.Union([{0}])'
                    ''.format(_join(t._trait_fulldef()
                                    for t in self.subtypes)))
        elif trait == 'List':
            subtrait = list(self.subtypes)[0]._trait_fulldef(kwds=[])
            return 'T.List({0}{1})'.format(subtrait, _join(kwds, True))
        elif trait == 'Instance':
            return 'T.Instance({0}{1})'.format(self.refname, _join(kwds, True))
        elif trait == self.refname:
            return '{0}({1})'.format(self.refname, _join(kwds))
        else:
            return 'T.{0}({1})'.format(trait, _join(kwds))

    trait_fulldef = property(_trait_fulldef)

    @property
    def trait_or_subtrait(self):
        if self.refname is not None:
            return self.refname
        elif self.trait_name in ['Union', 'List']:
            for t in self.subtypes:
                if t.trait_or_subtrait is not None:
                    return t.trait_or_subtrait
            else:
                return None
        else:
            return None

    @property
    def description(self):
        return ensure_ascii_compatible(self.schema.get('description', ''))

    @property
    def short_description(self):
        if self.description:
            # replace all whitespace with single spaces.
            desc = re.sub(r"\s+", ' ', self.description)
            # truncate description in appropriate place
            for lineend in ['(e.g.', '.', ';']:
                desc = desc.split(lineend)[0]
            return desc + '.'
        else:
            return ''

    @property
    def long_description(self):
        return self.description

    @property
    def refname(self):
        if '$ref' in self.schema:
            return self.schema['$ref'].split('/')[-1]
        else:
            return None

    @refname.setter
    def refname(self, refname):
        if not self.refname:
            raise AttributeError("cannot set refname")
        self.schema['$ref'] = 'definitions/{0}'.format(refname)

    @property
    def module(self):
        mod = getattr(self, '_module', '')
        if mod:
            return mod
        elif self.refname:
            return '.' + self.refname.lower()
        else:
            return ''

    @module.setter
    def module(self, mod):
        self._module = mod

    @property
    def channelclassname(self):
        refname = self.refname
        if refname:
            return refname

        for subtype in self.subtypes:
            name = subtype.channelclassname
            if name:
                return name

        return None

    @property
    def imports(self):
        if self.refname:
            yield dict(module=self.module, names=[self.refname])
        for t in self.subtypes:
            yield from t.imports
        for v in self.properties.values():
            yield from v.imports

    @property
    def base_import(self):
        if self.basename == 'BaseObject':
            return 'from ..baseobject import BaseObject'
        else:
            return 'from .{0} import {1}'.format(self.basename.lower(),
                                                 self.basename)

    @property
    def basename(self):
        return getattr(self, '_basename', None) or BASE_MAP[self.name]

    @basename.setter
    def basename(self, name):
        self._basename = name

    @property
    def attributes(self):
        return [v for k, v in sorted(self.properties.items())]

    @property
    def enum(self):
        return self.schema.get('enum', [])


class VegaLiteSchema(SchemaProperty):
    """
    This is a wrapper for the vegalite JSON schema that provides tools to
    export Python wrappers.
    """
    def __init__(self, schema_file=None):
        if schema_file is None:
            schema_file = getpath('..', 'altair', 'schema',
                                  'vega-lite-schema.json')
        with open(schema_file) as f:
            schema = json.load(f)

        self.definitions = {k: SchemaProperty(v, k, self)
                            for k, v in schema['definitions'].items()}

        super(VegaLiteSchema, self).__init__(schema, 'VegaLiteSchema', self)

    def wrappers(self):
        """Iterator over all class aliases to generate.

        These will be passed via jinja to ``templates/{template}.tpl``
        and saved to ``altair/schema/_wrappers/{template}.py``
        """

        # Channel wrapper classes
        for base in ['PositionChannelDef', 'ChannelDefWithLegend',
                     'FieldDef', 'OrderChannelDef']:
            wrappername = base.replace('Def', '')
            yield dict(name=wrappername,
                       base=self.definitions[base],
                       imports=[dict(module='.._interface', names=[base])],
                       root='channel_wrappers')

        # Encoding channel specializations
        encoding = self.definitions['Encoding']
        for attr in encoding.attributes:
            base = attr.trait_or_subtrait
            wrappername = base.replace('Def', '')
            yield dict(name=attr.name.title(),
                       base=self.definitions[base].rename(wrappername),
                       imports=[dict(module='.channel_wrappers', names=[wrappername])],
                       root='named_channels')

        # Channel collections
        def construct_dct(name):
            return {key: name for key in ['PositionChannelDef', 'FieldDef',
                                          'OrderChannelDef', 'ChannelDefWithLegend']}
        for name in CHANNEL_COLLECTIONS:
            obj = self.top.definitions[name].copy()
            obj.basename = name
            obj.root = 'channel_collections'
            for prop, val in obj.properties.items():
                obj.properties[prop] = val.replace_refs(construct_dct(prop.title()),
                                                        module='.named_channels')
            yield obj

    def write_interface(self, path=None):
        # Make sure the path is valid
        if path is None:
            path = getpath('..', 'altair', 'schema', '_interface')
        if not os.path.exists(path):
            os.makedirs(path)

        print("Writing code to {0}".format(path))

        # Write Init File
        template = JINJA_ENV.get_template('interface_init.tpl')
        header = "Auto-generated Python wrappers for Vega-Lite Schema"
        print(" - Writing __init__.py")
        objects = [dict(module=obj.lower(), classname=obj)
                   for obj in sorted(self.definitions)]
        with open(os.path.join(path, '__init__.py'), 'w') as f:
            f.write(template.render(objects=objects,
                                    header=header))

        # Write Class Definition files
        templates = {'string': JINJA_ENV.get_template('interface_enum.tpl'),
                     'object': JINJA_ENV.get_template('interface_object.tpl')}
        for key, prop in sorted(self.definitions.items()):
            if prop.type not in templates:
                raise ValueError("No template for type={0}".format(prop.type))
            outfile = os.path.join(path, '{0}.py'.format(key.lower()))
            print(" - Writing {0}".format(os.path.basename(outfile)))
            with open(outfile, 'w') as f:
                f.write(templates[prop.type].render(cls=prop))

    def write_interface_tests(self, path=None):
        # Make sure the path is valid
        if path is None:
            path = getpath('..', 'altair', 'schema', '_interface', 'tests')
        if not os.path.exists(path):
            os.makedirs(path)

        print("Writing tests to {0}".format(path))

        # Write test Init File
        template = JINJA_ENV.get_template('interface_init.tpl')
        header = 'Auto-generated tests for Vega-Lite Schema wrappers'
        print(" - Writing __init__.py")
        with open(os.path.join(path, '__init__.py'), 'w') as f:
            f.write(template.render(objects=[], header=header))

        # Write test file
        template = JINJA_ENV.get_template('interface_test.tpl')
        classes = [prop for key, prop in sorted(self.definitions.items())]
        print(" - Writing test_instantiations.py")
        with open(os.path.join(path, 'test_instantiations.py'), 'w') as f:
            f.write(template.render(classes=classes))

    def write_wrappers(self, path=None):
        # make sure the path is valid
        if path is None:
            path = getpath('..', 'altair', 'schema', '_wrappers')
        if not os.path.exists(path):
            os.makedirs(path)

        print("Writing wrappers to {0}".format(path))

        # Write wrapper definition files
        groups = groupby(self.wrappers(), lambda w: JINJA_ENV.getattr(w, 'root'))
        for root, wrappers in groups:
            template = JINJA_ENV.get_template('{0}.tpl'.format(root))
            filename = os.path.join(path, '{0}.py'.format(root))
            print("- writing {0}".format(filename))
            with open(filename, 'w') as f:
                f.write(template.render(objects=list(wrappers)))

        # Write wrapper __init__.py file
        template = JINJA_ENV.get_template('wrapper_init.tpl')
        filename = os.path.join(path, '__init__.py')
        header = 'Wrappers for low-level schema objects'
        print("- writing {0}".format(filename))
        with open(filename, 'w') as f:
            f.write(template.render(objects=list(self.wrappers()),
                                    header=header))


if __name__ == '__main__':
    schema = VegaLiteSchema()
    schema.write_interface()
    schema.write_interface_tests()
    schema.write_wrappers()
