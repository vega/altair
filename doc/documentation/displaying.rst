.. _displaying-plots:

Displaying and Saving Altair Visualizations
===========================================

Fundamentally, Altair does one thing: create Vega-Lite JSON specifications of
visualizations. For example, consider the following plot specification

>>> from altair import Chart, load_dataset
>>> data = load_dataset('cars', url_only=True)
>>> chart = Chart(data).mark_point().encode(
...             x='Horsepower:Q',
...             y='Miles_per_Gallon:Q',
...             color='Origin:N',
...         )

The ``chart`` object defined here is an Altair chart, which contains functionality
to generate a JSON encoding that conforms to the `Vega-Lite Schema`_:

>>> print(chart.to_json(indent=2))
{
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/cars.json"
  },
  "encoding": {
    "color": {
      "field": "Origin",
      "type": "nominal"
    },
    "x": {
      "field": "Horsepower",
      "type": "quantitative"
    },
    "y": {
      "field": "Miles_per_Gallon",
      "type": "quantitative"
    }
  },
  "mark": "point"
}

This specification is a full definition of a Vega-Lite visualization, and
can be rendered in one of several ways.

.. _displaying-plots-jupyter:

Displaying Plots in Jupyter Notebook
------------------------------------

Perhaps the most straightforward way to interactively create and render
Altair visualizations is in the `Jupyter Notebook`_.
If you have installed correctly configured the `ipyvega`_ package
(See :ref:`Installation`), then a chart on the last line of a code cell
will automatically be represented within the notebook as a rendered plot:

.. altair-plot::

    # Within Jupyter Notebook
    from altair import Chart, load_dataset
    data = load_dataset('cars', url_only=True)
    Chart(data).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    )

Alternatively, you can use ``chart.display()`` to more explicitly display
any chart object

.. _displaying-plots-html:

Outputting Plots as HTML
------------------------
If you prefer working outside the notebook, Altair includes the ability to
generate a stand-alone HTML document containing the JSON specification along
with the javascript commands to render it:

>>> html = chart.to_html()
>>> with open('chart.html', 'w') as f:
...     f.write(html)  # doctest: +SKIP

If you then point your browser at ``chart.html``, you will see the rendered result.
For more information on embedding Vega-Lite plots within HTML pages, see
Vega-Lite's documentation, in particular
`Embedding Vega-Lite <http://vega.github.io/vega-lite/usage/embed.html>`_.

.. _displaying-plots-server:

Displaying Plots via a Local HTTP Server
----------------------------------------
Because the above exercise (outputting html, saving to file, and opening a
web browser) can be a bit tedious, Altair provides a ``chart.serve()`` method
that will use Python's ``HTTPServer`` to launch a local web server and open
the visualization in your browser.
Given a chart object, you can do this with

>>> chart.serve()   # doctest: +SKIP
Serving to http://127.0.0.1:8888/    [Ctrl-C to exit]
127.0.0.1 - - [15/Sep/2016 14:40:39] "GET / HTTP/1.1" 200 -

.. _displaying-plots-vega-editor:

Online Vega-Lite Editor
-----------------------

Finally, if you wish to play with Vega/Vega-Lite specifications directly, you
can paste the JSON into the `Vega-Lite Online Editor`_.
This provides an interface in which to directly explore the plot outputs
of Vega-Lite specifications.

Saving Figures as PNG and SVG
-----------------------------
The easiest way to export figures to PNG or EPS is to click the
"Open In Vega Editor" link under any rendered figure, and then use the "Export"
command to save the figure as either PNG format (With the Renderer set to
"Canvas") or SVG format (with the renderer set to "SVG").

Saving Figures Programatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you would like to save an Altair visualization as PNG or EPS *from a script*,
Altair does provide an interface that allows this, though it requires some
extra setup.

.. note::

   This feature is experimental and relatively brittle; we are working on
   improving it and this API will likely change in the future.

The `Vega-Lite`_ javascript library provides a NodeJS_ command-line tool to
generate ``png`` and ``svg`` outputs from Altair/Vega-Lite specifications.
The :func:`altair.utils.node.savechart` function provides an interface that
will use these command-line tools to output PNG or SVG outputs of a chart.

If you have ``nodejs`` and ``npm`` available on your system, you can install
the required command-line tools using::

    $ npm install canvas vega-lite

If you don't have ``nodejs`` and are using ``conda``, you can create an
environment with nodejs/npm and the required packages as follows
(note that the canvas tool seems to require Python 2.7):

    $ conda create -n nodejs-env -c conda-forge python=2.7 nodejs altair
    $ source activate nodejs-env
    $ npm install canvas vega-lite

Once you have successfully installed these packages, you should have new binary
files ``vl2vg``, ``vg2png``, and ``vg2eps`` within your node root directory.

With this set-up, you can use the installed command-line utilities to save your chart:

>>> from altair import Chart, load_dataset
>>> data = load_dataset('cars', url_only=True)
>>> chart = Chart(data).mark_point().encode(
...             x='Horsepower:Q',
...             y='Miles_per_Gallon:Q',
...             color='Origin:N',
...         )

>>> from altair.utils.node import savechart, savechart_available
>>> # save as PNG
>>> savechart(chart, 'mychart.png')  # doctest: +SKIP
>>> # save as SVG
>>> savechart(chart, 'mychart.svg')  # doctest: +SKIP

Internally, the code executes ``npm root`` to determine the installation directory,
and calls the ``vl2vg``, ``vg2png``, and ``vg2eps`` executables within this root.
If you want to manually specify the npm executable directory, you can use the
``node_bin_dir`` keyword:

>>> savechart(chart, 'mychart.svg', node_bin_dir='~/node_modules/.bin/')

We hope to find a way to streamline this in the future, but creating transparent
interactions between Python packages and NodeJS packages remains challenging.
If you have ideas on how to improve this aspect of Altair's user experience,
please send comments or contributions via Altair's
`Github Issue Tracker <https://github.com/altair-viz/altair/issues>`_.


.. _NodeJS: https://nodejs.org/en/
.. _Vega-Lite Schema: https://vega.github.io/vega-lite/vega-lite-schema.json
.. _Vega-Lite Online Editor: https://vega.github.io/vega-editor/?mode=vega-lite
.. _Vega-Lite: https://github.com/vega/vega-lite
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
