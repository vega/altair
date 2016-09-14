import os
import warnings
from itertools import tee, chain, islice

import jinja2

from .utils import strip_vl_extension
from altair import Chart
from altair.examples import iter_examples_with_metadata


GALLERY_TEMPLATE = jinja2.Template(u"""
.. _{{ gallery_ref }}:

{{ title }}
{% for char in title %}-{% endfor %}

The following examples are automatically generated from
`Vega-Lite's Examples <http://vega.github.io/vega-lite/examples>`_

{% for example in examples %}
* |{{ example.name }}| :ref:`gallery_{{ example.name }}`
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
{%- endfor %}
""")


EXAMPLE_TEMPLATE = jinja2.Template(u"""
.. _gallery_{{ name }}:

{{ title }}
{% for char in title %}-{% endfor %}

{% if prev_ref -%} < :ref:`{{ prev_ref }}` {% endif %}
| :ref:`{{ gallery_ref }}` |
{%- if next_ref %} :ref:`{{ next_ref }}` >{% endif %}

.. altair-plot::
    {% if code_below %}:code-below:{% endif %}

    from altair import *

    {{ code | indent(4) }}
""")


def prev_this_next(it):
    """Utility to return (prev, this, next) tuples from an iterator"""
    i1, i2, i3 = tee(it, 3)
    next(i3, None)
    return zip(chain([None], i1), i2, chain(i3, [None]))


def populate_examples(**kwargs):
    """Iterate through Altair examples and extract code"""

    examples = list(iter_examples_with_metadata())

    for prev_ex, example, next_ex in prev_this_next(examples):
        try:
            code = Chart.from_dict(example['spec']).to_altair()
        except Exception as e:
            warnings.warn('altair-gallery: example {0} produced an error:\n'
                          '{1}\n{2}'.format(example['name'], type(e), str(e)))
            code = '# (Altair JSON conversion failed).\nChart()'

        example['code'] = code

        if prev_ex:
            example['prev_ref'] = "gallery_{name}".format(**prev_ex)

        if next_ex:
            example['next_ref'] = "gallery_{name}".format(**next_ex)

        example['filename'] = '{0}.rst'.format(example['name'])
        example.update(kwargs)

    return examples


def main(app):
    gallery_dir = app.builder.config.altair_gallery_dir
    target_dir = os.path.join(app.builder.srcdir, gallery_dir)

    gallery_ref = app.builder.config.altair_gallery_ref
    gallery_title = app.builder.config.altair_gallery_title
    examples = populate_examples(gallery_ref=gallery_ref,
                                 code_below=True)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Write the gallery index file
    with open(os.path.join(target_dir, 'index.rst'), 'w') as f:
        f.write(GALLERY_TEMPLATE.render(title=gallery_title,
                                        examples=examples,
                                        gallery_ref=gallery_ref))

    # Write the individual example files
    for example in examples:
        with open(os.path.join(target_dir, example['filename']), 'w') as f:
            f.write(EXAMPLE_TEMPLATE.render(example))


def setup(app):
    app.connect('builder-inited', main)
    app.add_config_value('altair_gallery_dir', 'gallery', 'env')
    app.add_config_value('altair_gallery_ref', 'example-gallery', 'env')
    app.add_config_value('altair_gallery_title', 'Example Gallery', 'env')
