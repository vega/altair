"""
This file generates a notebook that describes the API of Altair objects.

It uses the traitlets structure defined in the altair library.
"""


import types
from itertools import filterfalse
from operator import itemgetter

import jinja2
import traitlets

from ipykernel import kernelspec as ks
import nbformat
from nbformat.v4.nbbase import new_markdown_cell, new_code_cell, new_notebook

import os
import sys
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))
import altair


TEMPLATE = jinja2.Template("""### {{ obj.name }}

{% if obj.description %}*{{ obj.description }}*{% endif %}

| Trait | type | description |
|-------|------|-------------|
{% for trait in obj.traits -%}
| **{{ trait.name }}**| *{{ trait.type }}* | {{ trait.help }} |
{% endfor %}
""")

HEADER = """# Altair API Documentation
*(This is auto-generated from tools/generate_api_docs.py;
do not modify directly)*
"""

VEGALITE_DOC_URL = 'http://vega.github.io/vega-lite/docs/'
VEGALITE_DOC_PAGES = {'data': 'data.html',
                      'transform': 'transform.html',
                      'mark': 'mark.html',
                      'encoding': 'encoding.html',
                      'aggregate': 'aggregate.html',
                      'bin': 'bin.html',
                      'sort': 'sort.html',
                      'timeunit': 'timeunit.html',
                      'scale': 'scale.html',
                      'axis': 'axis.html',
                      'legend': 'legend.html',
                      'config': 'config.html#top-level-config',
                      'cellconfig': 'config.html#cell-config',
                      'markconfig': 'config.html#mark-config',
                      'scaleconfig': 'config.html#scale-config',
                      'axisconfig': 'config.html#axis-config',
                      'legendconfig': 'config.html#legend-config',
                      'facetconfig': 'config.html#facet-config'}

for channel in ['color', 'column', 'detail', 'opacity', 'order', 'path',
                'row', 'shape', 'size', 'text', 'x', 'y']:
    VEGALITE_DOC_PAGES[channel] = 'encoding.html#def'


def _get_trait_info(name, trait):
    """Get a dictionary of info for an object trait"""
    type_ = trait.info()
    help_ = trait.help

    if isinstance(trait, traitlets.List):
        trait_info = _get_trait_info('', trait._trait)
        type_ = 'list of {0}s'.format(trait_info['type'])
    elif isinstance(trait, traitlets.Enum):
        values = trait.values
        if all(isinstance(val, str) for val in values):
            type_ = 'string'
            help_ += ' One of {0}.'.format(values)
    elif isinstance(trait, traitlets.Union):
        trait_info = [_get_trait_info('', t) for t in trait.trait_types]
        type_ = ' or '.join(info['type'] for info in trait_info)
        help_ += '/'.join([info['help'] for info in trait_info
                           if info['help'] != '--'])
    elif isinstance(trait, traitlets.Instance):
        if issubclass(trait.klass, traitlets.HasTraits):
            type_ = '[{0}](#{0})'.format(trait.klass.__name__)

    type_ = type_.replace('a ', '')
    type_ = type_.replace('unicode string', 'string')
    return {'name': name, 'help': help_ or '--', 'type': type_ or '--'}


def _get_object_info(obj):
    """Get a dictionary of info for an object, suitable for the template"""
    D = {}
    name = obj.__name__
    D['name'] = name

    if name.lower() in VEGALITE_DOC_PAGES:
        D['description'] = ('Relevant Vega-Lite Documentation: '
                            '{0}'.format(VEGALITE_DOC_URL +
                                         VEGALITE_DOC_PAGES[name.lower()]))

    #if obj.__doc__:
    #    D['description'] = obj.__doc__.splitlines()[0]
    #else:
    #    D['description'] = 'no description available'

    D['traits'] = [_get_trait_info(name, trait)
                   for name, trait in sorted(obj.class_traits().items())]

    return D


def altair_nbdoc(obj):
    """Generate documentation for all objects in the namespace"""
    if obj is altair:
        for sub_obj in dir(obj):
            if sub_obj.startswith('_'):
                continue
            yield from altair_nbdoc(getattr(obj, sub_obj))
    elif isinstance(obj, type) and issubclass(obj, traitlets.HasTraits):
        yield _get_object_info(obj)


def create_doc_notebook(filename):
    kernelspec = {'display_name': 'Python 3',
                  'language': 'python',
                  'name': 'python3'}


    is_toplevel = lambda obj: 'Chart' in obj['name']
    content = sorted(altair_nbdoc(altair), key=itemgetter('name'))

    cells = [new_markdown_cell(source=(HEADER))]
    cells.append(new_markdown_cell(source='## Top-Level Objects'))
    cells.extend([new_markdown_cell(source=TEMPLATE.render(obj=obj))
                  for obj in filter(is_toplevel, content)])

    cells.append(new_markdown_cell(source='## Other Objects'))
    cells.extend([new_markdown_cell(source=TEMPLATE.render(obj=obj))
                  for obj in filterfalse(is_toplevel, content)])

    notebook = new_notebook(cells=cells,
                            metadata={'language': 'python',
                                      'kernelspec': kernelspec})
    nbformat.write(notebook, filename)


if __name__ == '__main__':
    import os
    API_notebook = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..',
                                                'altair',
                                                'notebooks',
                                                'API.ipynb'))
    print("Altair info:")
    print("- version", altair.__version__)
    print("- path:", altair.__path__)
    print("Writing API documentation to {0}".format(API_notebook))
    create_doc_notebook(API_notebook)
