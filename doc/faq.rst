.. currentmodule:: altair

.. _altair-faq:

Altair Frequently Asked Questions
=================================

.. contents::
   :local:


.. _altair-faq-no-display:

Why isn't my plot displaying in the Jupyter Notebook?
-----------------------------------------------------
The most common cause of a non-displaying plot in the Jupyter Notebook is
incorrect configuration of the ipyvega jupyter extension, which is what
recognizes an Altair object and automatically renders the plot with the
Vega-Lite library.

If you install altair using ``conda``, this nbextension setup step should be
taken care of automatically.
If you install altair using ``pip``, there is an extra step to enable this
extension; see the discussion at :ref:`Installation`.

If this still is not addressing the problem, it may be due to having multiple
incompatible versions of altair and vega on your system. Try updating both
packages using, e.g. ``conda update altair vega`` or
``pip install altair vega --update``.

If this still doesn't work, please open an issue in the Altair's
`GitHub Issue Tracker <https://github.com/altair-viz/altair/issues>`_,
and we will do our best to help. In the meantime, other means of displaying Altair
plots are listed in :ref:`displaying-plots`.


.. _altair-faq-large-notebook:

Why do Altair plots lead to such extremely large notebooks?
-----------------------------------------------------------
By design, Altair does not produce plots consisting of pixels, but plots
consisting of data plus a visualization specification. As discussed in
:ref:`defining-data`, this data can be specified in one of several ways, either
via a pandas DataFrame, a file or URL, or a JSON data object. When you specify
the data as a pandas DataFrame, this data is converted to JSON and included
in its entirety in the plot spec.

For example, here is a simple chart made from a dataframe with three rows
of data:

.. testcode::

    import pandas as pd
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 1, 2]})

    from altair import Chart
    chart = Chart(data).mark_line().encode(
                 x='x',
                 y='y'
            )

    print(chart.to_json(indent=2))

.. testoutput::

    {
      "data": {
        "values": [
          {
            "x": 1,
            "y": 2
          },
          {
            "x": 2,
            "y": 1
          },
          {
            "x": 3,
            "y": 2
          }
        ]
      },
      "encoding": {
        "x": {
          "field": "x",
          "type": "quantitative"
        },
        "y": {
          "field": "y",
          "type": "quantitative"
        }
      },
      "mark": "line"
    }


The resulting specification includes a representation of the data converted
to JSON format, and this specification is embedded in the notebook or web page
where it can be used by Vega-Lite to render the plot.
As the size of the data grows, this explicit data storage can lead to some
very large specifications, and by extension, some very large notebooks or
web pages.

The best way around this is to specify the data not by value, but by URL.
Vega-Lite can then load the data from the URL at the time that it renders
the plot. For example, you can save your data in the appropriate format
as follows:


.. testsetup::

   import pandas as pd
   from altair import Chart
   data = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 1, 2]})

.. testcode::

   url = 'data.csv'
   data.to_csv(url, orient='records', index=False)

   chart = Chart(url).mark_line().encode(
                x='x:Q',
                y='y:Q'
           )
   print(chart.to_json(indent=2))


.. testoutput::

    {
      "data": {
        "url": "data.csv"
      },
      "encoding": {
        "x": {
          "field": "x",
          "type": "quantitative"
        },
        "y": {
          "field": "y",
          "type": "quantitative"
        }
      },
      "mark": "line"
    }


The data is now stored in a separate CSV file rather than embedded in the
notebook or web page, leading to much more compact plot specifications.
The disadvantage, of course, is a loss of portability: if the notebook is
ever moved, the data file must accompany it or the plot may not display.

In the future, we hope to add a third option for the notebook: adding an
option to rendering and embedd only the png or svg image.
This feature will require an update to Altair's dependencies, which currently
implement the notebook rendering of Altair plots.


.. _Altair-faq-recipes:

How do I make a heatmap / violin plot / histogram / regression plot?
--------------------------------------------------------------------

Altair currently provides the building blocks from which you can construct
relatively sophisticated plots. In the future we may add an interface to
construct some of the more common plot types, but for the time being some
visualizations will require composition of more fundamental elements.

The :ref:`plot-recipes` section of the documentation contains a growing list
of recipes for creating common plot types in Altair.



.. _altair-faq-configuration:

How can I configure the tick marks / labels / size / appearance of my plot?
---------------------------------------------------------------------------

Altair, via Vega-Lite, includes an extensive array of customizations. Many of
these are not yet well-documented in Altair's documentation, but we are working
on addressing that. You can find some information on this by using tab-completion
of methods and method arguments within the IPython notebook; for example, typing
``Chart.<TAB>`` in the notebook will show a list of available methods, and typing
``Chart.configure_<TAB>`` will list all of the chart configuration options.

It can be useful to peruse
`Vega-Lite's Documentation <http://vega.github.io/vega-lite/docs/>`_.
The structure of the traits within Altair's :class:`Chart` object directly mirrors
the JSON schema of Vega-Lite, so if you know how to do something in Vega-Lite you
are only a step or two away from knowing how to do it in Altair. Additionally, if
you find a Vega-Lite example specification and would like to know how to do the
equivalent in Altair, the :class:`Chart` object includes the ability to generate
Python code from a Vega-Lite JSON specification. For example, here we copied the
spec from `Vega-Lite's Bubble Plot Example <https://vega.github.io/vega-editor/?mode=vega-lite&spec=scatter_bubble>`_,
and use it to create an Altair plot, changing only the data URL to make it absolute:

.. altair-plot::

    from altair import Chart

    spec = """
    {
      "description": "A bubbleplot showing horsepower on x, miles per gallons on y, and binned acceleration on size.",
      "data": {"url": "http://vega.github.io/vega-datasets/data/cars.json"},
      "mark": "point",
      "encoding": {
        "x": {"field": "Horsepower", "type": "quantitative"},
        "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
        "size": {"field": "Acceleration", "type": "quantitative"}
      }
    }
    """
    Chart.from_json(spec)

The :meth:`Chart.to_altair` method outputs Python code that will reconstruct this chart:

.. testsetup::

    from altair import Chart

    spec = """
    {
      "description": "A bubbleplot showing horsepower on x, miles per gallons on y, and binned acceleration on size.",
      "data": {"url": "http://vega.github.io/vega-datasets/data/cars.json"},
      "mark": "point",
      "encoding": {
        "x": {"field": "Horsepower", "type": "quantitative"},
        "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
        "size": {"field": "Acceleration", "type": "quantitative"}
      }
    }
    """

.. testcode::

    chart = Chart.from_json(spec)
    print(chart.to_altair())

.. testoutput::

    Chart('http://vega.github.io/vega-datasets/data/cars.json',
        description='A bubbleplot showing horsepower on x, miles per gallons on y, and binned acceleration on size.',
    ).mark_point().encode(
        size='Acceleration:Q',
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
    )

In this way you can easily discover how Altair implements any Vega-Lite feature.
