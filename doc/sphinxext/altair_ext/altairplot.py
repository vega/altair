"""
Altair Plot Sphinx Extension
============================

This extension provides a means of inserting live-rendered Altair plots within
sphinx documentation. There are two directives defined: ``altair-setup`` and
``altiar-plot``. ``altair-setup`` code is used to set-up various options
prior to running the plot code. For example::

    .. altair-setup::

        from altair import *
        import pandas as pd
        data = pd.DataFrame({'a': list('CCCDDDEEE'),
                             'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})

    .. altair-plot::

        Chart(data).mark_point().encode(
            x='a',
            y='b'
        )

In the case of the ``altair-plot`` code, the *last statement* of the code-block
should contain the chart object you wish to be rendered.

Options
-------
The directives have the following options::

    .. altair-setup::
        :show: # if set, then show the setup code as a code block

        pass

    .. altair-plot::
        :hide-code:  # if set, then hide the code and only show the plot
        :code-below:  # if set, then code is below rather than above the figure
        :alt: text  # Alternate text when plot cannot be rendered
        :links: editor source export  # specify one or more of these options

        Chart()

Additionally, this extension introduces a global configuration
``altair_plot_links``, set in your ``conf.py`` which is a dictionary
of links that will appear below plots, unless the ``:links:`` option
again overrides it. It should look something like this::

    # conf.py
    # ...
    altair_plot_links = {'editor': True, 'source': True, 'export': True}
    # ...

If this configuration is not specified, all are set to True.
"""

import os
import json
import warnings

import jinja2

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import flag, unchanged

from sphinx.locale import _
from sphinx import addnodes, directives
from sphinx.util.nodes import set_source_info

from altair.api import TopLevelMixin
from .utils import exec_then_eval


VGL_TEMPLATE = jinja2.Template("""
<div id="{{ div_id }}">
<script>
  vg.embed("#{{ div_id }}", "{{ filename }}", function(error, result) {});
</script>
</div>
""")


class altair_plot(nodes.General, nodes.Element):
    pass


class AltairSetupDirective(Directive):
    has_content = True

    option_spec = {'show': flag}

    def run(self):
        env = self.state.document.settings.env

        targetid = "altair-plot-{0}".format(env.new_serialno('altair-plot'))
        targetnode = nodes.target('', '', ids=[targetid])

        code = '\n'.join(self.content)

        # Here we cache the code for use in later setup
        if not hasattr(env, 'altair_plot_setup'):
            env.altair_plot_setup = []
        env.altair_plot_setup.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'code': code,
            'target': targetnode,
        })

        result = [targetnode]

        if 'show' in self.options:
            source_literal = nodes.literal_block(code, code)
            source_literal['language'] = 'python'
            result.append(source_literal)

        return result


def purge_altair_plot_setup(app, env, docname):
    if not hasattr(env, 'altair_plot_setup'):
        return
    env.altair_plot_setup = [item for item in env.altair_plot_setup
                             if item['docname'] != docname]


DEFAULT_LINKS = {'editor': True, 'source': True, 'export': True}


def validate_links(links):
    if links.strip().lower() == 'none':
        return {}

    links = links.strip().split()
    diff = set(links) - set(DEFAULT_LINKS.keys())
    if diff:
        raise ValueError("Following links are invalid: {0}".format(list(diff)))
    return dict((link, link in links) for link in DEFAULT_LINKS)


class AltairPlotDirective(Directive):

    has_content = True

    option_spec = {'hide-code': flag,
                   'code-below': flag,
                   'alt': unchanged,
                   'links': validate_links}

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        show_code = 'hide-code' not in self.options
        code_below = 'code-below' in self.options

        setupcode = '\n'.join(item['code']
                              for item in getattr(env, 'altair_plot_setup', [])
                              if item['docname'] == env.docname)

        code = '\n'.join(self.content)

        if show_code:
            source_literal = nodes.literal_block(code, code)
            source_literal['language'] = 'python'

        #get the name of the source file we are currently processing
        rst_source = self.state_machine.document['source']
        rst_dir = os.path.dirname(rst_source)
        rst_filename = os.path.basename(rst_source)

        # use the source file name to construct a friendly target_id
        serialno = env.new_serialno('altair-plot')
        rst_base = rst_filename.replace('.', '-')
        div_id = "{0}-altair-plot-{1}".format(rst_base, serialno)
        target_id = "{0}-altair-source-{1}".format(rst_base, serialno)
        target_node = nodes.target('', '', ids=[target_id])

        # create the node in which the plot will appear;
        # this will be processed by html_visit_altair_plot
        plot_node = altair_plot()
        plot_node['target_id'] = target_id
        plot_node['div_id'] = div_id
        plot_node['code'] = code
        plot_node['setupcode'] = setupcode
        plot_node['relpath'] = os.path.relpath(rst_dir, env.srcdir)
        plot_node['rst_source'] = rst_source
        plot_node['rst_lineno'] = self.lineno
        default_links = app.builder.config.altair_plot_links
        plot_node['links'] = self.options.get('links', default_links)

        if 'alt' in self.options:
            plot_node['alt'] = self.options['alt']

        result = [target_node]

        if code_below:
            result += [plot_node]
        if show_code:
            result += [source_literal]
        if not code_below:
            result += [plot_node]

        return result


def html_visit_altair_plot(self, node):
    # Execute the setup code, saving the global & local state
    namespace = {}
    if node['setupcode']:
        exec(node['setupcode'], namespace)

    # Execute the plot code in this context, evaluating the last line
    try:
        chart = exec_then_eval(node['code'], namespace)
    except Exception as e:
        warnings.warn("altair-plot: {0}:{1} Code Execution failed:"
                      "{2}: {3}".format(node['rst_source'], node['rst_lineno'],
                                        e.__class__.__name__, str(e)))
        raise nodes.SkipNode

    if isinstance(chart, TopLevelMixin):
        # Last line should be a chart; convert to spec dict
        spec = chart.to_dict()

        # Create the vega-lite spec to embed
        embed_spec = json.dumps({'mode': 'vega-lite',
                                 'actions': node['links'],
                                 'spec': spec})

        # Prevent http/https request errors by doing this
        embed_spec.replace('http://', '//')
        embed_spec.replace('https://', '//')

        # Write embed_spec to a *.vl.json file
        dest_dir = os.path.join(self.builder.outdir, node['relpath'])
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        filename = "{0}.vl.json".format(node['div_id'])
        dest_path = os.path.join(dest_dir, filename)
        with open(dest_path, 'w') as f:
            f.write(embed_spec)

        # Pass relevant info into the template and append to the output
        html = VGL_TEMPLATE.render(div_id=node['div_id'],
                                   filename=filename)
        self.body.append(html)
    else:
        warnings.warn('altair-plot: {0}:{1} Malformed block. Last line of '
                      'code block should define a valid altair Chart object.'
                      ''.format(node['rst_source'], node['rst_lineno']))
    raise nodes.SkipNode


def generic_visit_altair_plot(self, node):
    # TODO: generate PNGs and insert them here
    if 'alt' in node.attributes:
        self.body.append(_('[ graph: %s ]') % node['alt'])
    else:
        self.body.append(_('[ graph ]'))
    raise nodes.SkipNode


def setup(app):
    setup.app = app
    setup.config = app.config
    setup.confdir = app.confdir

    app.add_stylesheet('altair-plot.css')

    app.add_javascript("https://d3js.org/d3.v3.min.js")
    app.add_javascript("https://vega.github.io/vega/vega.js")
    app.add_javascript("https://vega.github.io/vega-lite/vega-lite.js")
    app.add_javascript("https://vega.github.io/vega-editor/vendor/vega-embed.js")
    app.add_config_value('altair_plot_links', DEFAULT_LINKS, 'env')

    app.add_node(altair_plot,
                 html=(html_visit_altair_plot, None),
                 latex=(generic_visit_altair_plot, None),
                 texinfo=(generic_visit_altair_plot, None),
                 text=(generic_visit_altair_plot, None),
                 man=(generic_visit_altair_plot, None))

    app.add_directive('altair-plot', AltairPlotDirective)
    app.add_directive('altair-setup', AltairSetupDirective)
    app.connect('env-purge-doc', purge_altair_plot_setup)

    return {'version': '0.1'}
