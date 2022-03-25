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

For a more detailed overview of the Altair's visualization grammar, see the following

.. raw:: html

  <div class="youtube-video">
    <iframe src="https://www.youtube-nocookie.com/embed/U7w1XumKK60?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>

.. _Vega: http://vega.github.io/vega
.. _Vega-Lite: http://vega.github.io/vega-lite
