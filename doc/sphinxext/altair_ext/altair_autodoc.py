""" Specialization of Sphinx autodoc for Altair objects"""
from __future__ import absolute_import, print_function

import types
import importlib
import warnings
import inspect

import jinja2
import traitlets

from six import class_types
from sphinx.ext.autodoc import ClassDocumenter
from sphinx.util.compat import Directive
from sphinx.util.nodes import nested_parse_with_titles

from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst.directives import flag

try:
    # Altair <= 1.2
    from altair.schema.baseobject import BaseObject as AltairBase
except ImportError:
    # Altair > 1.2
    from altair import jstraitlets as jst
    AltairBase = jst.JSONHasTraits

from .utils import import_obj
from .utils.altair_rst_table import altair_rst_table


def process_docstring(app, what, name, obj, options, lines):
    """Event hook for 'autodoc-process-docstring'

    This captures the extracted docstring, and modifies it in-place
    """
    if inspect.isclass(obj) and issubclass(obj, AltairBase):
        del lines[3:]
        table_rst = '.. altair-trait-table:: {0}'.format(obj.__name__)
        table_opt = '   :include-vegalite-link:'
        lines.extend(['', table_rst, table_opt, ''])

    elif hasattr(obj, '_uses_signature'):
        del lines[2:]
        args_description = ('Arguments are passed to :class:`~altair.{0}`.'
                            ''.format(obj._uses_signature.__name__))
        lines.extend(['', args_description])


def process_signature(app, what, name, obj, options, signature, return_annotation):
    """Event hook for 'autodoc-process-signature'

    This captures the signature and returns an updated version of
    (signature, return_annotation)
    """
    if inspect.isclass(obj) and issubclass(obj, AltairBase):
        signature = '(**kwargs)'
    return signature, return_annotation


class AltairClassDocumenter(ClassDocumenter):
    directivetype = 'altair-class'
    objtype = 'altairclass'

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return inspect.isclass(member) and issubclass(member, AltairBase)


ALTAIR_CLASS_TEMPLATE = jinja2.Template(
u"""
.. autoclass:: {{ classname }}
   :members:
   :inherited-members:
   :undoc-members:
   :exclude-members: {{ exclude_members }}

""")


def import_obj_from_args(args):
    """Utility to import the object given arguments to directive"""
    if len(args) == 1:
        mod, clsname = args[0].rsplit('.', 1)
    elif len(args) == 3 and args[1] == ':module:':
        mod = args[2]
        clsname = args[0].split('(')[0]
    else:
        raise ValueError("Args do not look as expected: {0}".format(args))
    return import_obj(clsname, default_module=mod)


class AltairClassDirective(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 2

    def run(self):
        # figure out what attributes to exclude:
        obj = import_obj_from_args(self.arguments)
        if not issubclass(obj, traitlets.HasTraits):
            raise ValueError('altair-class directive should only be used '
                             'on altair classes; not {0}'.format(obj))
        exclude = ['skip']
        exclude.extend(getattr(obj, 'skip', []))
        exclude.extend([attr for attr in obj.class_traits()])
        exclude.extend([attr for attr in dir(traitlets.HasTraits)
                        if not attr.startswith('_')])

        # generate the documentation string
        rst_text = ALTAIR_CLASS_TEMPLATE.render(
            classname=self.arguments[0],
            exclude_members=','.join(exclude)
        )

        # parse and return documentation
        result = ViewList()
        for line in rst_text.split("\n"):
            result.append(line, "<altair-class>")
        node = nodes.paragraph()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


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
    app.add_autodocumenter(AltairClassDocumenter)
    app.add_directive_to_domain('py', 'altair-class', AltairClassDirective)
    app.add_directive('altair-trait-table', AltairTraitTableDirective)
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect('autodoc-process-signature', process_signature)
