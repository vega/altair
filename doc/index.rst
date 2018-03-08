Declarative Visualization in Python
===================================

Altair is a declarative statistical visualization library for Python, based on
Vega_ and Vega-Lite_.

With Altair, you can spend more time understanding your data and its meaning.
Altair's API is simple, friendly and consistent and built on top of the
powerful Vega-Lite_ visualization grammar. This elegant simplicity produces
beautiful and effective visualizations with a minimal amount of code.

**Note: Altair and the underlying Vega-Lite library are under active
development. We are currently (March 2018) working on a 2.0 release, and
this documentation site is under construction.**


Example
-------
Here is an example of using the Altair API to quickly visualize a dataset with
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
handled automatically. Building on this declarative plotting idea, a surprising number
of useful plots and visualizations can be created using a relatively concise grammar.

This visualization grammar also includes a declarative grammar of interaction,
which allows construction of various interactive chart types.
So, for example, by adding a few lines to the basic chart above,
we can allow the viewer to highlight points by clicking and dragging:

.. altair-plot::

    brush = alt.selection(type='interval')

    alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color=alt.condition(brush, 'Origin', alt.value('lightgray'))
    ).properties(
        selection=brush,
    )

And with a few more modifications, we can extend this brush selection across
multiple panels containing different views of the data:

.. altair-plot::

    brush = alt.selection(type='interval')

    alt.Chart(cars).mark_point().encode(
        alt.X(alt.repeat('column'), type='quantitative'),
        y='Miles_per_Gallon',
        color=alt.condition(brush, 'Origin', alt.value('lightgray'))
    ).properties(
        selection=brush,
        width=280, height=280
    ).repeat(
        column=['Horsepower', 'Acceleration']
    )

In this manner, even quite sophisticated interactive multi-panel dashboards
can be created from simple declarative building blocks.


Documentation
-------------

.. toctree::
   :maxdepth: 2

   gallery/index
   tutorials/index

Bug Reports & Questions
-----------------------

Altair is BSD-licensed and the source is available on `GitHub`_. If any
questions or issues come up as you use Altair, please get in touch via
`Git Issues`_ or our `Google Group`_.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _GitHub: http://github.com/altair-viz/altair
.. _Git Issues: http://github.com/altair-viz/altair/issues
.. _Vega: http://vega.github.io/vega
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Google Group: https://groups.google.com/forum/#!forum/altair-viz
