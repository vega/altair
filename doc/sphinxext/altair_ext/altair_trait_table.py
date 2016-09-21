import warnings
import importlib

from docutils.parsers.rst import Directive
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst.directives import flag

from sphinx.util.nodes import nested_parse_with_titles

from .utils.altair_rst_table import altair_rst_table
from .utils import import_obj


class AltairTraitTableDirective(Directive):
    has_content = False
    required_arguments = 1

    option_spec = {'include-vegalite-link': flag}

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        classname = self.arguments[0].split('(')[0].strip()

        try:
            obj = import_obj(classname, default_module='altair')
        except ImportError:
            raise
            warnings.warn('Could not make table for {0}. Unable to import'
                          ''.format(object))

        # create the table from the object
        include_vl_link = ('include-vegalite-link' in self.options)
        table = altair_rst_table(obj, include_description=include_vl_link)

        # parse and return documentation
        result = ViewList()
        for line in table:
            result.append(line, "<altair-class>")
        node = nodes.paragraph()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


def setup(app):
    setup.app = app
    setup.config = app.config
    setup.confdir = app.confdir

    app.add_directive('altair-trait-table', AltairTraitTableDirective)

    return {'version': '0.1'}
