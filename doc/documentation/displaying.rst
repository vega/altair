.. currentmodule:: altair

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
The easiest way to export figures to PNG or SVG is to click the
"Open In Vega Editor" link under any rendered figure, and then use the "Export"
command to save the figure as either PNG format (With the Renderer set to
"Canvas") or SVG format (with the renderer set to "SVG").

Saving Figures Programmatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you would like to save an Altair visualization as PNG or SVG *from a script*,
Altair does provide an interface that allows this, though it requires some
extra setup.

The `Vega-Lite`_ javascript library provides a NodeJS_ command-line tool to
generate ``png`` and ``svg`` outputs from Altair/Vega-Lite specifications.
The :meth:`Chart.savechart` method provides an interface that
will use these command-line tools to output PNG or SVG outputs of a chart.

If you have ``nodejs`` and ``npm`` available on your system, you can install
the required command-line tools using::

    $ npm install canvas vega vega-lite

If you don't have ``nodejs`` and are using ``conda``, you can create an
environment with nodejs/npm and the required packages as follows
(note that the ``node-gyp`` tool related to canvas seems to require Python 2.7)::

    $ conda create -n nodejs-env -c conda-forge python=2.7 nodejs cairo altair
    $ source activate nodejs-env
    $ npm install canvas vega vega-lite

On Linux systems, the required tools can be installed with `Apt <https://wiki.debian.org/Apt>`_::

    $ sudo apt-get install libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++
    $ npm install canvas vega vega-lite

As above, this appears to work only when using Python 2.7 because of the ``node-gyp`` dependency.

More information on installing node and associated packages can be found on the
`Node Installation Page <https://nodejs.org/en/download/>`_.

If the installation was successful, you should have new executables called
``vl2png`` and ``vl2svg`` within your node root directory, which you can determine
by running::

    $ npm bin
    /Users/username/node_modules/.bin

    $ ls /Users/username/node_modules/.bin
    vg2png  vg2svg  vl2png  vl2svg  vl2vg

With these packages properly installed, you can use the :meth:`Chart.savechart`
method to save a chart to file:

>>> from altair import Chart, load_dataset
>>> data = load_dataset('cars', url_only=True)
>>> chart = Chart(data).mark_point().encode(
...             x='Horsepower:Q',
...             y='Miles_per_Gallon:Q',
...             color='Origin:N',
...         )
>>> # save as PNG
>>> chart.savechart('mychart.png')  # doctest: +SKIP
>>> # save as SVG
>>> chart.savechart('mychart.svg')  # doctest: +SKIP

This command searches for the ``vl2png`` or ``vl2svg`` executable either in
the ``npm bin`` location or in the system ``$PATH`` variable.

The extra requirements here are straightforward, but the manual installation
process is admittedly a bit clunky.
We hope to find a way to streamline this in the future, but creating transparent
interactions between Python packages and NodeJS packages remains a
challenging area in general.
If you have ideas on how to improve this aspect of Altair's user experience,
please send comments or contributions via Altair's
`Github Issue Tracker <https://github.com/altair-viz/altair/issues>`_.


.. _NodeJS: https://nodejs.org/en/
.. _Vega-Lite Schema: https://vega.github.io/vega-lite/vega-lite-schema.json
.. _Vega-Lite Online Editor: https://vega.github.io/vega-editor/?mode=vega-lite
.. _Vega-Lite: https://github.com/vega/vega-lite
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
