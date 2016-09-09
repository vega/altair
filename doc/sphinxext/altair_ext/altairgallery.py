""" Generate a gallery of Altair plots from an iterable Vega-Lite JSON"""

import warnings
import os

from docutils import nodes
from docutils.parsers.rst.directives import flag, unchanged
from docutils.statemachine import ViewList

import jinja2

from sphinx.util.compat import Directive

from altair import Chart

from .utils import exec_then_eval, strip_vl_extension


GALLERY_TEMPLATE = jinja2.Template(u"""
{% for name in names %}
* |{{ name }}| {{ name }}
{% endfor %}

{% for name in names %}
.. |{{ name }}| image:: /_static/gray-square.png {# /_images/gallery/{{ name }}.png #}
    :target: gallery/{{ name }}.html
    :class: gallery
{% endfor %}
""")

DETAIL_TEMPLATE = jinja2.Template(u"""
.. _gallery_{{ name }}:

{{ name }}
{{ underline }}

{% if prev_ref -%} < :ref:`{{ prev_ref }}` | {% endif %}
:ref:`{{ up_ref }}`
{%- if next_ref %} | :ref:`{{ next_ref }}` >{% endif %}

.. altair-plot::
    {% if code_below %}:code-below:{% endif %}

    from altair import *

    {{ code | indent(4) }}
""")


class AltairGalleryDirective(Directive):

    has_content = True

    option_spec = {
        'code-below' : flag,
        'index-ref' : unchanged,
    }

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        env.note_reread()

        dest_dir = os.path.join(os.path.dirname(self.state_machine.node.source),
                                "gallery")

        target_id = "altair-plot-{0}".format(env.new_serialno('altair-plot'))
        target_node = nodes.target('', '', ids=[target_id])
        result = [target_node]

        code_below = 'code-below' in self.options
        index_ref = self.options.get('index-ref', 'examples-gallery')

        examples = exec_then_eval('\n'.join(self.content))
        examples = [{'name': strip_vl_extension(filename),
                     'json': json} for filename, json in examples]

        for i, example in enumerate(examples):
            name = example['name']
            try:
                code = Chart.from_dict(example['json']).to_altair()
            except Exception as e:
                warnings.warn('altair-gallery: example {0} did not compile.: '
                              '{1} {2}'.format(name, type(e), str(e)))
                code = '# (Altair JSON conversion failed).\nChart()'
            prev_ref, next_ref = None, None
            if i > 0:
                prev_ref = "gallery_" + examples[i-1]['name']
            if i < len(examples)-1:
                next_ref = "gallery_" + examples[i+1]['name']
            rst = DETAIL_TEMPLATE.render(
                name=name,
                underline="-"*len(name),
                code=code,
                prev_ref=prev_ref,
                up_ref=index_ref,
                next_ref=next_ref,
                code_below=code_below,
            )
            with open(os.path.join(dest_dir, "%s.rst" % name), "w") as f:
                f.write(rst)
            env.clear_doc(os.path.join("gallery", name))
            env.read_doc(os.path.join("gallery", name), app=app)

        result = ViewList()
        names = [example['name'] for example in examples]

        env.gallery_names = [os.path.join("gallery", n) for n in names]
        text = GALLERY_TEMPLATE.render(names=names)
        for line in text.split("\n"):
            result.append(line, "<altair-gallery>")
        node = nodes.paragraph()
        node.document = self.state.document
        self.state.nested_parse(result, 0, node)

        return node.children

def env_updated_handler(app, env):
    return getattr(env, 'gallery_names', [])

def setup(app):

    # Clear gallery before generating a new one
    dirname = 'gallery'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    for fname in os.listdir(dirname):
        os.remove(os.path.join(dirname, fname))

    app.connect('env-updated', env_updated_handler)
    app.add_directive('altair-gallery', AltairGalleryDirective)
