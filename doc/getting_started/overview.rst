.. _overview:

Overview
========

Altair is a declarative statistical visualization library for Python, based on
Vega_ and Vega-Lite_.

Altair offers a powerful and concise visualization grammar that enables you to build
a wide range of statistical visualizations quickly. Here is an example of using the
Altair API to quickly visualize a dataset with
an interactive scatter plot:

.. altair-plot::

    import altair as alt

    # load a simple dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

The key idea is that you are declaring links between *data columns* and *visual encoding
channels*, such as the x-axis, y-axis, color, etc. The rest of the plot details are
handled automatically. Building on this declarative plotting idea, a surprising range
of simple to sophisticated plots and visualizations can be created using a relatively
concise grammar.

.. _Vega: http://vega.github.io/vega
.. _Vega-Lite: http://vega.github.io/vega-lite


.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   self
   installation
   starting
   getting_help
   project_philosophy
