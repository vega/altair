import os
import json
from itertools import chain

from jinja2 import Environment, FileSystemLoader

TYPE_MAP = {'oneOf': 'Union',
            "array": "List",
            "boolean": "Bool",
            "number": "CFloat",
            "string": "Unicode",
            "object": "Any",
           }


class SchemaProperty(object):
    """Class Wrapper for a property in a VegaLite Schema

    This class exposes methods used in the templating.
    """
    def __init__(self, schema, name, top):
        self.name = name
        self.schema = schema
        self.top = top

        self.properties = {k: SchemaProperty(v, k, self.top)
                           for k, v in self.schema.get('properties', {}).items()}

    @property
    def subtypes(self):
        trait = self.trait_name
        if trait == 'Union':
            return [self.__class__(s, '', self.top) for s in self.schema['oneOf']]
        elif trait == 'List':
            return [self.__class__(self.schema['items'], '', self.top)]
        else:
            return []

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
        trait = TYPE_MAP.get(self.type, None)
        if trait is not None:
            return trait

        trait = self.top.definitions[self.refname].trait_name
        if trait == 'Any':
            return 'Instance'
        else:
            return self.refname

    @property
    def trait_descr(self):
        trait = self.trait_name
        if trait == 'Instance':
            return self.refname
        elif self.subtypes:
            try:
                return '{0}({1})'.format(trait, ', '.join(t.trait_descr for t in self.subtypes))
            except TypeError:
                import IPython; IPython.embed()
                raise
        else:
            return trait

    @property
    def trait_fulldef(self):
        trait = self.trait_name
        kwds = "allow_none=True, default_value=None"
        if self.description:
            kwds += ', help="""{0}"""'.format(self.short_description)

        if trait == 'Union':
            return ('T.Union([{0}])'
                    ''.format(', '.join(t.trait_fulldef for t in self.subtypes)))
        elif trait == 'List':
            return 'T.List({0}, {1})'.format(*(t.trait_fulldef for t in self.subtypes), kwds)
        elif trait == 'Instance':
            return 'T.Instance({0}, {1})'.format(self.refname, kwds)
        elif trait == self.refname:
            return '{0}({1})'.format(self.refname, kwds)
        else:
            return 'T.{0}({1})'.format(trait, kwds)

    @property
    def description(self):
        return self.schema.get('description', '')

    @property
    def short_description(self):
        if self.description:
            return self.description.split('(e.g.')[0].split('.')[0] + '.'
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

    @property
    def imports(self):
        def gen_imports():
            if self.refname:
                yield self.refname
            for t in self.subtypes:
                yield from t.imports
            for v in self.properties.values():
                yield from v.imports
        return sorted(gen_imports())

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
            schema_file = os.path.join(os.path.dirname(__file__),
                                       '..',
                                       'altair', 'schema',
                                       'vega-lite-schema.json')
        with open(schema_file) as f:
            schema = json.load(f)

        self.definitions = {k: SchemaProperty(v, k, self)
                            for k, v in schema['definitions'].items()}

        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.templates = Environment(loader=FileSystemLoader(template_path))

        super(VegaLiteSchema, self).__init__(schema, 'VegaLiteSchema', self)

    def write_wrappers(self, path=None, verbose=True):
        def print_(*args, **kwargs):
            if verbose:
                print(*args, **kwargs)

        # Make sure the path is valid
        if path is None:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   '..', 'altair', 'schema', '_generated'))
        testpath = os.path.join(path, 'tests')
        if not os.path.exists(testpath):
            os.makedirs(testpath)

        print_("Writing code to {0}".format(path))

        # Write Init File
        template = self.templates.get_template('__init__.py.tpl')
        header="Auto-generated Python wrappers for Vega-Lite Schema"
        print_(" - Writing __init__.py")
        with open(os.path.join(path, '__init__.py'), 'w') as f:
            f.write(template.render(objects=sorted(self.definitions),
                                    header=header))

        # Write Class Definition files
        templates = {'string': self.templates.get_template('enum.py.tpl'),
                     'object': self.templates.get_template('object.py.tpl')}
        for key, prop in sorted(self.definitions.items()):
            if prop.type not in templates:
                raise ValueError("No template for type={0}".format(prop.type))
            outfile = os.path.join(path, '{0}.py'.format(key.lower()))
            print_(" - Writing {0}".format(os.path.basename(outfile)))
            with open(outfile, 'w') as f:
                f.write(templates[prop.type].render(cls=prop))

        print_("Writing tests to {0}".format(testpath))

        # Write test Init File
        template = self.templates.get_template('__init__.py.tpl')
        header = 'Auto-generated tests for Vega-Lite Schema wrappers'
        print_(" - Writing __init__.py")
        with open(os.path.join(testpath, '__init__.py'), 'w') as f:
            f.write(template.render(objects=[], header=header))

        # Write test file
        template = self.templates.get_template('test_instantiations.py.tpl')
        classes = [prop for key, prop in sorted(self.definitions.items())]
        print_(" - Writing test_instantiations.py")
        with open(os.path.join(testpath, 'test_instantiations.py'), 'w') as f:
            f.write(template.render(classes=classes))


if __name__ == '__main__':
    schema = VegaLiteSchema()
    schema.write_wrappers()
