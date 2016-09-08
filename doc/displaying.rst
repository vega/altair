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

>>> print(chart.to_json(indent=2))
{
  "encoding": {
    "color": {
      "field": "Origin",
      "type": "nominal"
    },
    "y": {
      "field": "Miles_per_Gallon",
      "type": "quantitative"
    },
    "x": {
      "field": "Horsepower",
      "type": "quantitative"
    }
  },
  "mark": "point",
  "data": {
    "url": "https://vega.github.io/vega-datasets/data/cars.json"
  }
}

This specification is a full definition of a Vega-Lite visualization, and
can be rendered in one of several ways.

Jupyter Notebook
----------------
Perhaps the most straightforward way to render Altair visualizations is in
the `Jupyter Notebook`_.
If you have correctly configured the optional `ipyvega`_ dependency
(See :ref:`Installation`), then the chart object will automatically
be represented within the notebook as a rendered plot:

.. altair-plot::

    # Within Jupyter Notebook
    from altair import Chart, load_dataset
    data = load_dataset('cars', url_only=True)
    Chart(data).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    )


Outputting HTML
---------------
If you prefer working outside the notebook, Altair includes the ability to
generate a stand-alone HTML document containing the JSON specification along
with the javascript commands to render it:

>>> html = chart.to_html()
>>> with open('chart.html', 'w') as f:
...     f.write(html)

If you then point your browser at ``chart.html``, you will see the rendered result.
For more information on embedding Vega-Lite plots within HTML pages, see
Vega-Lite's documentation, in particular
`Embedding Vega-Lite <http://vega.github.io/vega-lite/usage/embed.html>`_.

Local HTTP Server
-----------------
Because the above exercise (outputting html, saving to file, and opening a
web browser) can be a bit tedious, Altair provides a ``chart.serve()`` method
that will use Python's ``HTTPServer`` to launch a local web server and open
the visualization in your browser.
Given a chart object, you can do this with

>>> chart.serve()   # doctest: +SKIP

*TODO: add output here*


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
