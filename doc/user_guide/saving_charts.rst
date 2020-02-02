.. currentmodule:: altair

.. _user-guide-saving:

Saving Altair Charts
--------------------
Altair chart objects have a :meth:`Chart.save` method which allows charts
to be saved in a variety of formats. 

.. saving-json:

JSON format
~~~~~~~~~~~
The fundamental chart representation output by Altair is a JSON string format;
one of the core methods provided by Altair is :meth:`Chart.to_json`, which
returns a JSON string that represents the chart content.
Additionally, you can save a chart to a JSON file using :meth:`Chart.save`,
by passing a filename with a ``.json`` extension.

For example, here we save a simple scatter-plot to JSON:

.. code-block:: python

    import altair as alt
    from vega_datasets import data

    chart = alt.Chart(data.cars.url).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )

    chart.save('chart.json')

The contents of the resulting file will look something like this:

.. code-block:: json

    {
      "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
      "config": {
        "view": {
          "continuousHeight": 300,
          "continuousWidth": 400
        }
      },
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

This JSON can then be inserted into any web page using the vegaEmbed_ library.

.. saving-html:

HTML format
~~~~~~~~~~~
If you wish for Altair to take care of the HTML embedding for you, you can
save a chart directly to an HTML file using

.. code-block:: python

    chart.save('chart.html')

This will create a simple HTML template page that loads Vega, Vega-Lite, and
vegaEmbed, such that when opened in a browser the chart will be rendered.

For example, saving the above scatter-plot to HTML creates a file with
the following contents, which can be opened and rendered in any modern
javascript-enabled web browser:

.. code-block:: HTML

    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
      <script src="https://cdn.jsdelivr.net/npm/vega-lite@4"></script>
      <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    </head>
    <body>
      <div id="vis"></div>
      <script type="text/javascript">
        var spec = {
          "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
          "config": {
            "view": {
              "continuousHeight": 300,
              "continuousWidth": 400
            }
          },
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
        };
        var opt = {"renderer": "canvas", "actions": false};
        vegaEmbed("#vis", spec, opt);
      </script>
    </body>
    </html>

You can view the result here: `chart.html </_static/chart.html>`_.

By default, ``canvas`` is used for rendering the visualization in vegaEmbed. To 
change to ``svg`` rendering, use the ``embed_options`` as such:

.. code-block:: python

    chart.save('chart.html', embed_options={'renderer':'svg'})


.. note::

   This is not the same as ``alt.renderers.enable('svg')``, what renders the 
   chart as a static ``svg`` image within a Jupyter notebook.

.. _saving-png:

PNG, SVG, and PDF format
~~~~~~~~~~~~~~~~~~~~~~~~
To save an Altair chart object as a PNG, SVG, or PDF image, you can use

.. code-block:: python

    chart.save('chart.png')
    chart.save('chart.svg')
    chart.save('chart.pdf')

However, saving these images requires some additional extensions to run the
javascript code necessary to interpret the Vega-Lite specification and output
it in the form of an image.

Altair can do this via the altair_saver_ package, which can be installed with::

    $ conda install altair_saver

or::

    $ pip install altair_saver

See the altair_saver_ documentation for information about additional installation
requirements.

Figure Size/Resolution
^^^^^^^^^^^^^^^^^^^^^^
When using ``chart.save()`` above, the resolution of the resulting PNG is
controlled by the resolution of your screen. The easiest way to produce a
higher-resolution PNG image is to scale the image to make it larger, and thus
to contain more pixels at a given resolution.

This can be done with the ``scale_factor`` argument, which defaults to 1.0::

    chart.save('chart.png', scale_factor=2.0)


.. _altair_saver http://github.com/altair-viz/altair_saver/
.. _vegaEmbed: https://github.com/vega/vega-embed
