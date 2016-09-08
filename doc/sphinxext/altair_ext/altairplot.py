"""Altair Directive for sphinx"""

import ast
import os

import jinja2

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag, unchanged

from sphinx.locale import _
from sphinx import addnodes, directives
from sphinx.util.nodes import set_source_info

try:
    import altair
    from altair.api import TopLevelMixin
except ImportError:
    altair = None


VGL_TEMPLATE = jinja2.Template("""
<div id="vis{{ uid }}"></div>
<script src="https://d3js.org/d3.v3.min.js"></script>
<script src="https://vega.github.io/vega/vega.js"></script>
<script src="https://vega.github.io/vega-lite/vega-lite.js"></script>
<script src="https://vega.github.io/vega-editor/vendor/vega-embed.js" charset="utf-8"></script>
<script>
var vlSpec = {{ spec }}

var embedSpec = {
  mode: "vega-lite",
  spec: vlSpec
}

vg.embed("#vis{{ uid }}", embedSpec, function(error, result) {
  // Callback receiving the View instance and parsed Vega spec
  // result.view is the View, which resides under the '#vis' element
});
</script>
""")


def exec_then_eval(code):
    """Exec a code block & return evaluation of the last line"""
    block = ast.parse(code, mode='exec')
    last = ast.Expression(block.body.pop().value)

    globals = {}
    locals = {}
    exec(compile(block, '<string>', mode='exec'), globals, locals)
    return eval(compile(last, '<string>', mode='eval'), globals, locals)


class altair_plot(nodes.General, nodes.Element):
    pass


class AltairPlotDirective(Directive):

    has_content = True

    option_spec = {'show-json': flag,
                   'hide-code': flag,
                   'alt': unchanged}

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        code = '\n'.join(self.content)
        source_literal = nodes.literal_block(code, code)
        source_literal['language'] = 'python'

        #get the name of the source file we are currently processing
        rst_source = self.state_machine.document['source']
        rst_dir = os.path.dirname(rst_source)
        rst_filename = os.path.basename(rst_source)

        # use the source file name to construct a friendly target_id
        target_id = "%s.bokeh-plot-%d" % (rst_filename, env.new_serialno('bokeh-plot'))
        target_node = nodes.target('', '', ids=[target_id])
        result = [target_node]

        if 'hide-code' not in self.options:
            result.append(source_literal)

        chart = exec_then_eval(code)

        if 'show-json' in self.options:
            json = chart.to_json(indent=2)
            json_literal = nodes.literal_block(json, json)
            json_literal['language'] = 'json'
            result.append(json_literal)

        node = altair_plot()
        node['target_id'] = target_id
        node['source'] = source_literal
        node['relpath'] = os.path.relpath(rst_dir, env.srcdir)
        node['rst_source'] = rst_source
        node['rst_lineno'] = self.lineno
        node['spec'] = chart.to_json()
        node['uid'] = env.new_serialno('altair-plot')
        if 'alt' in self.options:
            node['alt'] = self.options['alt']
        result += [node]

        return result


def html_visit_altair_plot(self, node):
    html = VGL_TEMPLATE.render(uid=node['uid'], spec=node['spec'])
    self.body.append(html)
    raise nodes.SkipNode


def generic_visit_altair_plot(self, node):
    if 'alt' in node.attributes:
        self.body.append(_('[ graph: %s ]') % node['alt'])
    else:
        self.body.append(_('[ graph ]'))
    raise nodes.SkipNode


latex_visit_altair_plot = generic_visit_altair_plot
texinfo_visit_altair_plot = generic_visit_altair_plot
text_visit_altair_plot = generic_visit_altair_plot
man_visit_altair_plot = generic_visit_altair_plot


def setup(app):
    setup.app = app
    setup.config = app.config
    setup.confdir = app.confdir

    app.add_node(altair_plot,
                 html=(html_visit_altair_plot, None),
                 latex=(latex_visit_altair_plot, None),
                 texinfo=(texinfo_visit_altair_plot, None),
                 text=(text_visit_altair_plot, None),
                 man=(man_visit_altair_plot, None))

    app.add_directive('altair-plot', AltairPlotDirective)

    return {'version': '0.1'}
