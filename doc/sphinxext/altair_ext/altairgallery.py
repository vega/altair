import os
import warnings

import jinja2

from .utils import strip_vl_extension
from altair import Chart
from altair.examples import iter_examples


GALLERY_TEMPLATE = jinja2.Template(u"""
.. _{{ index_ref }}:

Altair Example Gallery
----------------------

The following examples are automatically generated from
`Vega-Lite's Examples <http://vega.github.io/vega-lite/examples>`_

{% for example in examples %}
* |{{ example.name }}| {{ example.name }}
{% endfor %}

{% for example in examples %}
.. |{{ example.name }}| image:: /_static/gray-square.png {# /_images/gallery/{{ name }}.png #}
    :target: {{ example.name }}.html
    :class: gallery
{% endfor %}

.. toctree::
   :hidden:
{% for example in examples %}
   {{ example.name }}
{% endfor %}
""")


EXAMPLE_TEMPLATE = jinja2.Template(u"""
.. _gallery_{{ name }}:

{# Title with underline: #}
{{ name }}
{% for char in name %}-{% endfor %}

{% if prev_ref -%} < :ref:`{{ prev_ref }}` {% endif %}
| :ref:`{{ index_ref }}` |
{%- if next_ref %} :ref:`{{ next_ref }}` >{% endif %}

.. altair-plot::
    {% if code_below %}:code-below:{% endif %}

    from altair import *

    {{ code | indent(4) }}
""")


def populate_examples(**kwargs):
    """Iterate through Altair examples and extract code"""
    examples = [{'json': json, 'name': strip_vl_extension(filename)}
                 for i, (filename, json) in enumerate(iter_examples())]

    for i, example in enumerate(examples):
        try:
            example['code'] = Chart.from_dict(example['json']).to_altair()
        except Exception as e:
            warnings.warn('altair-gallery: example {0} did not compile.: '
                          '{1} {2}'.format(example['name'], type(e), str(e)))
            example['code'] = '# (Altair JSON conversion failed).\nChart()'

        if i > 0:
            example['prev_ref'] = "gallery_" + examples[i - 1]['name']
        else:
            example['prev_ref'] = None

        if i < len(examples) - 1:
            example['next_ref'] = "gallery_" + examples[i + 1]['name']
        else:
            example['next_ref'] = None

        example['filename'] = '{0}.rst'.format(example['name'])
        example.update(kwargs)

    return examples


def main(app):
    gallery_dir = app.builder.config.altair_gallery_dir
    target_dir = os.path.join(app.builder.srcdir, gallery_dir)

    index_ref = 'example-gallery'
    examples = populate_examples(index_ref=index_ref,
                                 code_below=True)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Write the gallery index file
    with open(os.path.join(target_dir, 'index.rst'), 'w') as f:
        f.write(GALLERY_TEMPLATE.render(examples=examples,
                                        index_ref=index_ref))

    # Write the individual example files
    for example in examples:
        with open(os.path.join(target_dir, example['filename']), 'w') as f:
            f.write(EXAMPLE_TEMPLATE.render(example))


def setup(app):
    app.connect('builder-inited', main)
    app.add_config_value('altair_gallery_dir', 'gallery', 'env')
