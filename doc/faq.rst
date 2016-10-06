.. currentmodule:: altair

.. _altair-faq:

Altair Frequently Asked Questions
=================================

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
`Github Issue Tracker <https://github.com/altair-viz/altair/issues>`_,
and we will do our best to help. In the meantime, other means of displaying Altair
plots are listed in :ref:`displaying-plots`.


.. _altair-faq-recipes:

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
