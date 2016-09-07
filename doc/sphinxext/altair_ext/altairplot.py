"""Altair Directive for sphinx"""

import ast

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag
from sphinx import addnodes
from sphinx.util.nodes import set_source_info

try:
    import altair
    from altair.api import TopLevelMixin
except ImportError:
    altair = None


def exec_then_eval(code):
    """Exec a code block & return evaluation of the last line"""
    block = ast.parse(code, mode='exec')
    last = ast.Expression(block.body.pop().value)

    globals = {}
    locals = {}
    exec(compile(block, '<string>', mode='exec'), globals, locals)
    return eval(compile(last, '<string>', mode='eval'), globals, locals)


class AltairDirective(Directive):

    has_content = True

    option_spec = {'hide-code': flag,
                   'hide-json': flag}

    def run(self):
        code = '\n'.join(self.content)
        source_literal = nodes.literal_block(code, code)
        source_literal['language'] = 'python'

        output = []

        if 'hide-code' not in self.options:
            output.append(source_literal)

        if 'hide-json' not in self.options:
            chart = exec_then_eval(code)

            json = chart.to_json(indent=2)
            json_literal = nodes.literal_block(json, json)
            json_literal['language'] = 'json'
            output.append(json_literal)

        return output

AltairDirective.__doc__ = __doc__


def setup(app):
    setup.app = app
    setup.config = app.config
    setup.confdir = app.confdir

    options = {
        'code' : None,
        'json' : None
    }

    app.add_directive('altair', AltairDirective)
    app.add_config_value('altair_show_code', None, True)
    app.add_config_value('altair_show_json', None, True)

    return {'version': '0.1'}
