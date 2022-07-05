import hashlib
import os
import json
import random
import collections
from operator import itemgetter
import warnings

import jinja2

from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag

from sphinx.util.nodes import nested_parse_with_titles

from .utils import (
    get_docstring_and_rest,
    prev_this_next,
    create_thumbnail,
    create_generic_image,
)
from altair.utils.execeval import eval_block
from altair.examples import iter_examples


EXAMPLE_MODULE = "altair.examples"


GALLERY_TEMPLATE = jinja2.Template(
    """
.. This document is auto-generated by the altair-gallery extension. Do not modify directly.

.. _{{ gallery_ref }}:

{{ title }}
{% for char in title %}-{% endfor %}

This gallery contains a selection of examples of the plots Altair can create.

Some may seem fairly complicated at first glance, but they are built by combining a simple set of declarative building blocks.

Many draw upon sample datasets compiled by the `Vega <https://vega.github.io/vega/>`_ project. To access them yourself, install `vega_datasets <https://github.com/altair-viz/vega_datasets>`_.

.. code-block:: none

   python -m pip install vega_datasets

{% for grouper, group in examples %}

.. _gallery-category-{{ grouper }}:

{{ grouper }}
{% for char in grouper %}~{% endfor %}

.. raw:: html

   <span class="gallery">
   {% for example in group %}
   <a class="imagegroup" href="{{ example.name }}.html">
     <span class="image" alt="{{ example.title }}" style="background-image: url(..{{ image_dir }}/{{ example.name }}-thumb.png);"></span>
     <span class="image-title">{{ example.title }}</span>
   </a>
   {% endfor %}
   </span>

   <div style='clear:both;'></div>

{% endfor %}


.. toctree::
   :maxdepth: 2
   :caption: Examples
   :hidden:

   Gallery <self>
   Tutorials <../case_studies/exploring-weather>
"""
)

MINIGALLERY_TEMPLATE = jinja2.Template(
    """
.. raw:: html

    <div id="showcase">
      <div class="examples">
      {% for example in examples %}
        <a class="preview" href="{{ gallery_dir }}/{{ example.name }}.html" style="background-image: url(.{{ image_dir }}/{{ example.name }}-thumb.png)"></a>
      {% endfor %}
      </div>
    </div>
"""
)


EXAMPLE_TEMPLATE = jinja2.Template(
    """
.. This document is auto-generated by the altair-gallery extension. Do not modify directly.

.. _gallery_{{ name }}:

{{ docstring }}

.. altair-plot::
    {% if code_below %}:code-below:{% endif %}
    {% if strict %}:strict:{% endif %}

    {{ code | indent(4) }}
"""
)


def save_example_pngs(examples, image_dir, make_thumbnails=True):
    """Save example pngs and (optionally) thumbnails"""
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # store hashes so that we know whether images need to be generated
    hash_file = os.path.join(image_dir, "_image_hashes.json")

    if os.path.exists(hash_file):
        with open(hash_file) as f:
            hashes = json.load(f)
    else:
        hashes = {}

    for example in examples:
        filename = example["name"] + ".png"
        image_file = os.path.join(image_dir, filename)

        example_hash = hashlib.md5(example["code"].encode()).hexdigest()
        hashes_match = hashes.get(filename, "") == example_hash

        if hashes_match and os.path.exists(image_file):
            print("-> using cached {}".format(image_file))
        else:
            # the file changed or the image file does not exist. Generate it.
            print("-> saving {}".format(image_file))
            chart = eval_block(example["code"])
            try:
                chart.save(image_file)
                hashes[filename] = example_hash
            except ImportError:
                warnings.warn("Unable to save image: using generic image")
                create_generic_image(image_file)

            with open(hash_file, "w") as f:
                json.dump(hashes, f)

        if make_thumbnails:
            params = example.get("galleryParameters", {})
            thumb_file = os.path.join(image_dir, example["name"] + "-thumb.png")
            create_thumbnail(image_file, thumb_file, **params)

    # Save hashes so we know whether we need to re-generate plots
    with open(hash_file, "w") as f:
        json.dump(hashes, f)


def populate_examples(**kwds):
    """Iterate through Altair examples and extract code"""

    examples = sorted(iter_examples(), key=itemgetter("name"))

    for example in examples:
        docstring, category, code, lineno = get_docstring_and_rest(example["filename"])
        example.update(kwds)
        if category is None:
            category = "other charts"
        example.update(
            {
                "docstring": docstring,
                "title": docstring.strip().split("\n")[0],
                "code": code,
                "category": category.title(),
                "lineno": lineno,
            }
        )

    return examples


class AltairMiniGalleryDirective(Directive):
    has_content = False

    option_spec = {
        "size": int,
        "names": str,
        "indices": lambda x: list(map(int, x.split())),
        "shuffle": flag,
        "seed": int,
        "titles": bool,
        "width": str,
    }

    def run(self):
        size = self.options.get("size", 15)
        names = [name.strip() for name in self.options.get("names", "").split(",")]
        indices = self.options.get("indices", [])
        shuffle = "shuffle" in self.options
        seed = self.options.get("seed", 42)
        titles = self.options.get("titles", False)
        width = self.options.get("width", None)

        env = self.state.document.settings.env
        app = env.app

        gallery_dir = app.builder.config.altair_gallery_dir

        examples = populate_examples()

        if names:
            if len(names) < size:
                raise ValueError(
                    "altair-minigallery: if names are specified, "
                    "the list must be at least as long as size."
                )
            mapping = {example["name"]: example for example in examples}
            examples = [mapping[name] for name in names]
        else:
            if indices:
                examples = [examples[i] for i in indices]
            if shuffle:
                random.seed(seed)
                random.shuffle(examples)
            if size:
                examples = examples[:size]

        include = MINIGALLERY_TEMPLATE.render(
            image_dir="/_static",
            gallery_dir=gallery_dir,
            examples=examples,
            titles=titles,
            width=width,
        )

        # parse and return documentation
        result = ViewList()
        for line in include.split("\n"):
            result.append(line, "<altair-minigallery>")
        node = nodes.paragraph()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


def main(app):
    gallery_dir = app.builder.config.altair_gallery_dir
    target_dir = os.path.join(app.builder.srcdir, gallery_dir)
    image_dir = os.path.join(app.builder.srcdir, "_images")

    gallery_ref = app.builder.config.altair_gallery_ref
    gallery_title = app.builder.config.altair_gallery_title
    examples = populate_examples(gallery_ref=gallery_ref, code_below=True, strict=False)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    examples = sorted(examples, key=lambda x: x["title"])
    examples_toc = collections.OrderedDict(
        {
            "Simple Charts": [],
            "Bar Charts": [],
            "Line Charts": [],
            "Area Charts": [],
            "Circular Plots": [],
            "Scatter Plots": [],
            "Histograms": [],
            "Maps": [],
            "Interactive Charts": [],
            "Advanced Calculations": [],
            "Case Studies": [],
        }
    )
    for d in examples:
        examples_toc[d["category"]].append(d)

    # Write the gallery index file
    with open(os.path.join(target_dir, "index.rst"), "w") as f:
        f.write(
            GALLERY_TEMPLATE.render(
                title=gallery_title,
                examples=examples_toc.items(),
                image_dir="/_static",
                gallery_ref=gallery_ref,
            )
        )

    # save the images to file
    save_example_pngs(examples, image_dir)

    # Write the individual example files
    for prev_ex, example, next_ex in prev_this_next(examples):
        if prev_ex:
            example["prev_ref"] = "gallery_{name}".format(**prev_ex)
        if next_ex:
            example["next_ref"] = "gallery_{name}".format(**next_ex)
        target_filename = os.path.join(target_dir, example["name"] + ".rst")
        with open(os.path.join(target_filename), "w", encoding="utf-8") as f:
            f.write(EXAMPLE_TEMPLATE.render(example))


def setup(app):
    app.connect("builder-inited", main)
    app.add_css_file("altair-gallery.css")
    app.add_config_value("altair_gallery_dir", "gallery", "env")
    app.add_config_value("altair_gallery_ref", "example-gallery", "env")
    app.add_config_value("altair_gallery_title", "Example Gallery", "env")
    app.add_directive_to_domain("py", "altair-minigallery", AltairMiniGalleryDirective)
