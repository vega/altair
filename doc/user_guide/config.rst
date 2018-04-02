.. currentmodule:: altair

.. _user-guide-config:

Configuring Visualizations
==========================

Altair's goal is to automatically choose useful plot settings and configurations
so that the user is free to think about the data rather than the mechanics
of plotting. That said, once you have a useful visualization, you will often
want to adjust certain aspects of it. This section of the documentation
outlines some of these adjustments.

Global Config vs. Local Config vs. Encoding
-------------------------------------------
There are often two or three different ways to specify the look of your plots
depending on the situation.
For example, suppose we are creating a scatter plot of the ``cars`` dataset:

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   cars = data.cars.url

   alt.Chart(cars).mark_point().encode(
       x='Acceleration:Q',
       y='Horsepower:Q'
   )

Suppose you wish to change the color of the points to red, and the opacity
of the points to 20%. There are three possible approaches to these:

Global Config
~~~~~~~~~~~~~
First, every chart type has a ``"config"`` property at the top level that acts
as a sort of theme for the whole chart and all of its sub-charts.
Here you can specify things like axes properties, mark properties, selection
properties, and more.

Altair allows you to access these through the ``configure_*`` methods of the
chart. Here we will use the :meth:`~Chart.configure_mark` property:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Acceleration:Q',
        y='Horsepower:Q'
    ).configure_mark(
        opacity=0.2,
        color='red'
    )

There are a couple things to be aware of when using this kind of global configuration:

1. By design configurations will affect *every mark* used within the chart

2. The global configuration is only permissible at the top-level; so, for example,
   if you tried to layer the above chart with another, it would result in an error.

Local Config
~~~~~~~~~~~~
If you would like to configure the look of the mark locally, such that the setting
only affects the particular chart property you reference, this can be done via a
local configuration setting.

In the case of mark properties, the best approach is to set the property as an
argument to the ``mark_*`` method. Here we will use :meth:`~Chart.mark_point`:

.. altair-plot::

    alt.Chart(cars).mark_point(opacity=0.2, color='red').encode(
        x='Acceleration:Q',
        y='Horsepower:Q'
    )

Unlike when using the global configuration, here it is possible to use the resulting
chart as a layer or facet in a compound chart.

Local config settings like this one will always override global settings.

Encoding
~~~~~~~~
Finally, it is possible to set chart properties via the encoding channel
(see :ref:`user-guide-encoding`). Rather than mapping a property to a data column,
you can map a property directly to a value using the :func:`value` function:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Acceleration:Q',
        y='Horsepower:Q',
        opacity=alt.value(0.2),
        color=alt.value('red')
    )

Note that only a limited set of mark properties can be bound to encodings, so
for some (e.g. ``fillOpacity``, ``strokeOpacity``, etc.) the encoding approach
is not available.

Encoding settings will always override local or global configuration settings.

Which to Use?
~~~~~~~~~~~~~
The precedence order for the three approaches is (from lowest to highest)
*global config*, *local config*, *encoding*. That is, if a chart property is
set both globally and locally, the local setting will win-out. If a property
is set both via a configuration and an encoding, the encoding will win-out.

In most usage, we recommend always using the highest-precedence means of
setting properties; i.e. an encoding, or a local configuration for properties
that are not tied to an encoding.
Global configurations should be reserved for creating themes that are applied
just before the chart is rendered.


Adjusting Axis Limits
---------------------
The default axis limit used by Altair is dependent on the type of the data
(see, for example, :ref:`type-axis-scale`). To fine-tune the axis limits
beyond these defaults, you can use the :class:`Scale` property of the axis
encodings. For example, consider the following plot:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Acceleration:Q',
        y='Horsepower:Q'
    )

Altair inherits from Vega-Lite the convention of always including the zero-point
in quantitative axes; if you would like to turn this off, you can add a
:class:`Scale` property to the :class:`X` encoding that specifies ``zero=False``:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        alt.X('Acceleration:Q',
            scale=alt.Scale(zero=False)
        ),
        y='Horsepower:Q'
    )

To specify exact axis limits, you can use the ``domain`` property of the scale:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        alt.X('Acceleration:Q',
            scale=alt.Scale(domain=(5, 20))
        ),
        y='Horsepower:Q'
    )

The problem is that the data still exists beyond the scale, and we need to tell
Altair what to do with this data. One option is to "clip" the data by setting
the ``"clip"`` property of the mark to True:

.. altair-plot::

    alt.Chart(cars).mark_point(clip=True).encode(
        alt.X('Acceleration:Q',
            scale=alt.Scale(domain=(5, 20))
        ),
        y='Horsepower:Q'
    )

Another option is to "clamp" the data; that is, to move points beyond the
limit to the edge of the domain:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        alt.X('Acceleration:Q',
            scale=alt.Scale(
                domain=(5, 20),
                clamp=True
            )
        ),
        y='Horsepower:Q'
    ).interactive()

For interactive charts like the one above, the clamping happens dynamically,
which can be useful for keeping in mind outliers as you pan and zoom on the
chart.


Adjusting Axis Labels
---------------------
Altair also gives you tool to easily configure the appearance of axis labels.
For example consider this plot:

.. altair-plot::

   import pandas as pd
   df = pd.DataFrame({'x': [0.03, 0.04, 0.05, 0.12, 0.07, 0.15],
                      'y': [10, 35, 39, 50, 24, 35]})

   alt.Chart(df).mark_circle().encode(
       x='x',
       y='y'
   )

The x labels are automatically rendered in SI prefix notation (i.e. 3m = 0.03)
which may not be desirable.

To fine-tune the formatting of the tick labels and to add a custom title to
each axis, we can pass to the :class:`X` and :class:`Y` encoding a custom
:class:`Axis` definition.
Here is an example of formatting the x labels as a percentage, and
the y labels as a dollar value:


.. altair-plot::

   alt.Chart(df).mark_circle().encode(
       x=alt.X('x', axis=alt.Axis(format='%', title='percentage')),
       y=alt.Y('y', axis=alt.Axis(format='$', title='dollar amount'))
   )


Additional formatting codes are available; for a listing of these see the
`d3 Format Code Documentation <https://github.com/d3/d3-format/blob/master/README.md#format>`_.


Adjusting the Legend
--------------------

A legend is added to the chart automatically when the `color`, `shape` or `size` arguments are passed to the :func:`encode` function. In this example we'll use `color`.

.. altair-plot::

  import altair as alt
  from vega_datasets import data

  iris = data.iris()

  alt.Chart(iris).mark_point().encode(
      x='petalWidth',
      y='petalLength',
      color='species'
  )

In this case, the legend can be customized by introducing the :class:`Color` class and taking advantage of its `legend` argument. The `shape` and `size` arguments have their own corresponding classes.

The legend option on all of them expects a :class:`Legend` object as its input, which accepts arguments to customize many aspects of its appearance. One simple example is giving the legend a `title`.

.. altair-plot::

  import altair as alt
  from vega_datasets import data

  iris = data.iris()

  alt.Chart(iris).mark_point().encode(
      x='petalWidth',
      y='petalLength',
      color=alt.Color('species', legend=alt.Legend(title="Species by color"))
  )

Another thing you can do is move the legend to another position with the `orient` argument.

.. altair-plot::

  import altair as alt
  from vega_datasets import data

  iris = data.iris()

  alt.Chart(iris).mark_point().encode(
      x='petalWidth',
      y='petalLength',
      color=alt.Color('species', legend=alt.Legend(orient="left")),
  )

You can remove the legend entirely by submitting a null value.

.. altair-plot::

  import altair as alt
  from vega_datasets import data

  iris = data.iris()

  alt.Chart(iris).mark_point().encode(
      x='petalWidth',
      y='petalLength',
      color=alt.Color('species', legend=None),
  )
