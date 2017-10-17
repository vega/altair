.. currentmodule:: altair

.. _displaying-plots:

Displaying and Saving Visualizations
===========================================

.. contents::

Vega-Lite JSON specification
----------------------------

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

>>> print(chart.to_json(indent=2))  # doctest: +SKIP
{
  "data": { "url": "https://vega.github.io/vega-datasets/data/cars.json" },
  "encoding": {
    "color": { "field": "Origin", "type": "nominal" },
    "x": { "field": "Horsepower", "type": "quantitative" },
    "y": { "field": "Miles_per_Gallon", "type": "quantitative" }
  },
  "mark": "point"
}

This specification is a full definition of a Vega-Lite visualization, and
can be rendered in one of several ways.

.. _displaying-plots-jupyter:

Displaying in Jupyter notebooks
-------------------------------

Usually, you will want to render your Altair visualization in your Jupyter notebooks.
The following Jupyter notebook user interfaces can render Altair visualizations:

- `Jupyter Notebook`_ (the ipyvega_ package is required)
- `JupyterLab`_ (built-in support)
- `nteract`_ (built-in-support)

In these environments, you can trigger the rendering of an Altair visualization by simply
returning your Chart at the end of a cell:

.. code-block:: python

    c = alt.Chart(...)
    c

Of you can use IPython's :func:`display` function at any point:

.. code-block:: python

    from IPython.display import display

    c = alt.Chart(...)
    display(c)

Lastly, there is a :meth:`Chart.display` method on the :class:`Chart` object itself:

.. code-block:: python

    c = alt.Chart(...)
    c.display()

Both JupyterLab_ and nteract_ have builtin rendering for Vega-Lite, so ipyvega_
doesn't need to be installed. However, to get Altair to emit the right data
to render in these more modern frontends, you must call the :func:`enable_mime_rendering`
function before trying to render a visualization:

.. code-block:: python

    import altair as alt

    # load built-in dataset as a pandas DataFrame
    cars = alt.load_dataset('cars')

    # For rendering in JupyterLab & nteract
    alt.enable_mime_rendering()

    alt.Chart(cars).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    )

Eventually this will not be needed, but is being provided to keep Altair working
without change in the classic Jupyter Notebook.

.. _displaying-plots-html:

Displaying via a Local HTTP Server
----------------------------------

Because the above exercise (outputting html, saving to file, and opening a
web browser) can be a bit tedious, Altair provides a ``chart.serve()`` method
that will use Python's ``HTTPServer`` to launch a local web server and open
the visualization in your browser.
Given a chart object, you can do this with

>>> chart.serve()   # doctest: +SKIP
Serving to http://127.0.0.1:8888/    [Ctrl-C to exit]
127.0.0.1 - - [15/Sep/2016 14:40:39] "GET / HTTP/1.1" 200 -

Saving as PNG and SVG
---------------------

The easiest way to export figures to PNG is to render them in a Jupyter notebook and then
click on the "Export as PNG" link below the visualization.

Previous releases of Altair had support for saving Altair visualizations to PNG or SVG
programmatically. The code for that remains in Altair, but it is based on a NodeJS_ package
that we are currently unable to build and use. 

Saving to an HTML file
----------------------

Altair supports writing visualizations to an image or HTML file. 
This file can be an HTML or  JSON file. This functionality
is available through :meth:`Chart.savechart`.

An example useage of :meth:`Chart.savechart`:

>>> chart.savechart('plot.html')  # doctest: +SKIP

If you then point your browser at ``chart.html``, you will see the rendered result.
For more information on embedding Vega-Lite plots within HTML pages, see
Vega-Lite's documentation, in particular
`Embedding Vega-Lite <http://vega.github.io/vega-lite/usage/embed.html>`_.

Obtaining other representations
-------------------------------

Altair charts can be represented as HTML, a Python dict, a JSON object and an
Altair chart. To convert between these representations, Altair provides

* :meth:`Chart.to_dict`, :meth:`Chart.from_dict`
* :meth:`Chart.to_json`, :meth:`Chart.from_json`
* :meth:`Chart.to_altair`

provides several methods to variety of methods to convert between
different representations.

Online Vega-Lite Editor
-----------------------

Finally, if you wish to play with Vega/Vega-Lite specifications directly, you
can paste the JSON into the `Vega-Lite Online Editor`_.
This provides an interface in which to directly explore the plot outputs
of Vega-Lite specifications.




.. _NodeJS: https://nodejs.org/en/
.. _Vega-Lite Schema: https://vega.github.io/vega-lite/vega-lite-schema.json
.. _Vega-Lite Online Editor: https://vega.github.io/vega-editor/?mode=vega-lite
.. _Vega-Lite: https://github.com/vega/vega-lite
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _JupyterLab: https://github.com/jupyterlab/jupyterlab
.. _nteract: https://github.com/nteract/nteract
