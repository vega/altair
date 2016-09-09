.. _displaying-plots:

Displaying Altair Visualizations
================================

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

>>> print(chart.to_json(indent=2, sort_keys=True))
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


.. _Vega-Lite Schema: https://vega.github.io/vega-lite/vega-lite-schema.json
.. _Vega-Lite Online Editor: https://vega.github.io/vega-editor/?mode=vega-lite
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
