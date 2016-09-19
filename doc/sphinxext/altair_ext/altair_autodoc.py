""" Specialization of Sphinx autodoc for Altair objects"""


from __future__ import absolute_import, print_function

import types

import jinja2
import traitlets

from six import class_types
from sphinx.ext.autodoc import ClassDocumenter, AttributeDocumenter
from sphinx.util.compat import Directive
from sphinx.util.nodes import nested_parse_with_titles

from docutils import nodes
from docutils.statemachine import ViewList

from altair.schema.baseobject import BaseObject

from .altair_rst_table import altair_rst_table



def process_docstring(app, what, name, obj, options, lines):
    """Event hook for 'autodoc-process-docstring'

    This captures the extracted docstring, and modifies it in-place
    """
    if isinstance(obj, class_types) and issubclass(obj, BaseObject):
        for i in range(len(lines)):
            lines.pop()
        lines.extend(altair_rst_table(obj))

    elif isinstance(obj, types.MethodType) and hasattr(obj, '_uses_signature'):
        if lines:
            for i in range(len(lines) - 1):
                lines.pop()
        lines.extend(['', ('Arguments are passed to :class:`~altair.{0}`.'
                           ''.format(obj._uses_signature.__name__)]))


def process_signature(app, what, name, obj, options, signature, return_annotation):
    """Event hook for 'autodoc-process-signature'

    This captures the signature and returns an updated version of
    (signature, return_annotation)
    """
    if isinstance(obj, class_types) and issubclass(obj, BaseObject):
        signature = '(**kwargs)'
    return signature, return_annotation


class AltairClassDocumenter(ClassDocumenter):
    directivetype = 'altair-class'
    objtype = 'altairclass'

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, class_types) and issubclass(member, BaseObject)


ALTAIR_CLASS_TEMPLATE = jinja2.Template(
u"""
.. autoclass::  {{ classname }}
   :members:
   :inherited-members:
   :undoc-members:
   :exclude-members: {{ exclude_members }}

""")


class AltairClassDirective(Directive):

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        rst_text = ALTAIR_CLASS_TEMPLATE.render(
            classname=self.arguments[0],
            exclude_members=','.join(dir(traitlets.HasTraits))
        )

        result = ViewList()
        for line in rst_text.split("\n"):
            result.append(line, "<altair-class>")
        node = nodes.paragraph()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect('autodoc-process-signature', process_signature)
    app.add_autodocumenter(AltairClassDocumenter)
    app.add_directive_to_domain('py', 'altair-class', AltairClassDirective)    #app.add_directive_to_domain('py', 'altair-trait', AltairTraitDirective)
