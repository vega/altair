.. currentmodule:: altair

.. _user-guide-customization:

Customizing Visualizations
==========================

Altair's goal is to automatically choose useful plot settings and configurations
so that the user is free to think about the data rather than the mechanics
of plotting. That said, once you have a useful visualization, you will often
want to adjust certain aspects of it. This section of the documentation
outlines some of the ways to make these adjustments.

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

1. “Global Config” acts on an entire chart object
2. “Local Config” acts on one mark of the chart
3. “Encoding” channels can also be used to set some chart properties

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

For a full discussion of global configuration options, see :ref:`user-guide-configuration`.

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


Adjusting the Title
-------------------
By default an Altair chart does not have a title, as seen in this example.

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   
   iowa = data.iowa_electricity.url
   
   alt.Chart(iowa).mark_area().encode(
       x="year:T",
       y=alt.Y("net_generation:Q", stack="normalize"),
       color="source:N"
   )

You can add a simple title by passing the `title` keyword argument with the data.

.. altair-plot::

   alt.Chart(iowa, title="Iowa's green energy boom").mark_area().encode(
       x="year:T",
       y=alt.Y("net_generation:Q", stack="normalize"),
       color="source:N"
   )

It is also possible to add a subtitle by passing in an `alt.TitleParams` object.

.. altair-plot::

   alt.Chart(
      iowa,
      title=alt.TitleParams(
          "Iowa's green energy boom",
          subtitle="A growing share of the state's energy has come from renewable sources"
      )
   ).mark_area().encode(
       x="year:T",
       y=alt.Y("net_generation:Q", stack="normalize"),
       color="source:N"
   )

The subtitle can run to two lines.

.. altair-plot::

   alt.Chart(
      iowa,
      title=alt.TitleParams(
          "Iowa's green energy boom",
          subtitle=["A growing share of the state's energy", "has come from renewable sources"]
      )
   ).mark_area().encode(
       x="year:T",
       y=alt.Y("net_generation:Q", stack="normalize"),
       color="source:N"
   )

The parameters object can also `configure <https://altair-viz.github.io/user_guide/configuration.html#config-title>`_ a number of other attributes.

.. altair-plot::

   alt.Chart(
      iowa,
      title=alt.TitleParams(
          "Iowa's green energy boom",
          subtitle=["A growing share of the state's energy", "has come from renewable sources"],
          anchor='start',
          orient='bottom',
          offset=20
      )
   ).mark_area().encode(
       x="year:T",
       y=alt.Y("net_generation:Q", stack="normalize"),
       color="source:N"
   )


Adjusting Axis Limits
---------------------
The default axis limit used by Altair is dependent on the type of the data.
To fine-tune the axis limits beyond these defaults, you can use the
:class:`Scale` property of the axis encodings. For example, consider the
following plot:

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
Altair also gives you tools to easily configure the appearance of axis labels.
For example consider this plot:

.. altair-plot::

   import pandas as pd
   df = pd.DataFrame({'x': [0.03, 0.04, 0.05, 0.12, 0.07, 0.15],
                      'y': [10, 35, 39, 50, 24, 35]})

   alt.Chart(df).mark_circle().encode(
       x='x',
       y='y'
   )

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

Axis labels can also be easily removed:

.. altair-plot::

   alt.Chart(df).mark_circle().encode(
       x=alt.X('x', axis=alt.Axis(labels=False)),
       y=alt.Y('y', axis=alt.Axis(labels=False))
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

Removing the Chart Border
-------------------------
Basic Altair charts are drawn with both a grid and an outside border.
To create a chart with no border, you will need to remove them both.

As an example, let's start with a simple scatter plot.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalWidth',
        y='petalLength',
        color='species'
    )

First remove the grid using the :meth:`Chart.configure_axis` method.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalWidth',
        y='petalLength',
        color='species'
    ).configure_axis(
        grid=False
    )

You'll note that while the inside rules are gone, the outside border remains.
Hide it by setting the `strokeWidth` or the `strokeOpacity` options on
:meth:`Chart.configure_view` to `0`:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalWidth',
        y='petalLength',
        color='species'
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    )


It is also possible to completely remove all borders and axes by
combining the above option with setting `axis` to `None` during encoding.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        alt.X('petalWidth', axis=None),
        alt.Y('petalLength', axis=None),
        color='species'
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    )


Customizing Colors
------------------

As discussed in :ref:`type-legend-scale`, Altair chooses a suitable default color
scheme based on the type of the data that the color encodes. These defaults can
be customized using the `scale` argument of the :class:`Color` class.

The :class:`Scale` class passed to the `scale` argument provides a number of options
for customizing the color scale; we will discuss a few of them here.

Color Schemes
~~~~~~~~~~~~~
Altair  includes a set of named color schemes for both categorical and sequential
data, defined by the vega project; see the
`Vega documentation <https://vega.github.io/vega/docs/schemes/>`_
for a full gallery of available color schemes.  These schemes
can be passed to the `scheme` argument of the :class:`Scale` class:

.. altair-plot::

  import altair as alt
  from vega_datasets import data

  iris = data.iris()

  alt.Chart(iris).mark_point().encode(
      x='petalWidth',
      y='petalLength',
      color=alt.Color('species', scale=alt.Scale(scheme='dark2'))
  )

Color Domain and Range
~~~~~~~~~~~~~~~~~~~~~~

To make a custom mapping of discrete values to colors, use the
`domain` and `range` parameters of the :class:`Scale` class for
values and colors respectively.

.. altair-plot::

  import altair as alt
  from vega_datasets import data

  iris = data.iris()
  domain = ['setosa', 'versicolor', 'virginica']
  range_ = ['red', 'green', 'blue']

  alt.Chart(iris).mark_point().encode(
      x='petalWidth',
      y='petalLength',
      color=alt.Color('species', scale=alt.Scale(domain=domain, range=range_))
  )

Raw Color Values
~~~~~~~~~~~~~~~~
The ``scale`` is what maps the raw input values into an appropriate color encoding
for displaying the data. If your data entries consist of raw color names or codes,
you can set ``scale=None`` to use those colors directly:

.. altair-plot::

  import pandas as pd
  import altair as alt

  data = pd.DataFrame({
      'x': range(6),
      'color': ['red', 'steelblue', 'chartreuse', '#F4D03F', '#D35400', '#7D3C98']
  })

  alt.Chart(data).mark_point(
      filled=True,
      size=100
  ).encode(
      x='x',
      color=alt.Color('color', scale=None)
  )

Adjusting the Width of Bar Marks
--------------------------------
The width of the bars in a bar plot are controlled through the ``size`` property in the :meth:`~Chart.mark_bar()`:

.. altair-plot::

  import altair as alt
  import pandas as pd

  data = pd.DataFrame({'name': ['a', 'b'], 'value': [4, 10]})

  alt.Chart(data).mark_bar(size=10).encode(
      x='name:O',
      y='value:Q'
  )

But since ``mark_bar(size=10)`` only controls the width of the bars, it might become possible that the width of the chart is not adjusted accordingly:

.. altair-plot::

  alt.Chart(data).mark_bar(size=30).encode(
      x='name:O',
      y='value:Q'
  )

The width of the chart containing the bar plot can be controlled through setting the ``width``
property of the chart, either to a pixel value for any chart, or to a step value
in the case of discrete scales.

Here is an example of setting the width to a single value for the whole chart:

.. altair-plot::

  alt.Chart(data).mark_bar(size=30).encode(
      x='name:O',
      y='value:Q'
  ).properties(width=200)

The width of the bars are set using ``mark_bar(size=30)`` and the width of the chart is set using ``properties(width=100)``

Here is an example of setting the step width for a discrete scale:

.. altair-plot::

  alt.Chart(data).mark_bar(size=30).encode(
      x='name:N',
      y='value:Q'
  ).properties(width=alt.Step(100))

The width of the bars are set using ``mark_bar(size=30)`` and the width that is allocated for each bar bar in the the chart is set using ``width=alt.Step(100)``


.. _customization-chart-size:

Adjusting Chart Size
--------------------
The size of charts can be adjusted using the ``width`` and ``height`` properties.
For example:

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   
   cars = data.cars()
   
   alt.Chart(cars).mark_bar().encode(
       x='Origin',
       y='count()'
   ).properties(
       width=200,
       height=150
   )

Note that in the case of faceted or other compound charts, this width and height applies to
the subchart rather than to the overall chart:

.. altair-plot::

   alt.Chart(cars).mark_bar().encode(
       x='Origin',
       y='count()',
       column='Cylinders:Q'
   ).properties(
       width=100,
       height=100
   )

If you want your chart size to respond to the width of the HTML page or container in which
it is rendererd, you can set ``width`` or ``height`` to the string ``"container"``:

.. altair-plot::
    :div_class_: full-width-plot

    alt.Chart(cars).mark_bar().encode(
        x='Origin',
        y='count()',
    ).properties(
        width='container',
        height=200
    )

Note that this will only scale with the container if its parent element has a size determined
outside the chart itself; For example, the container may be a ``<div>`` element that has style
``width: 100%; height: 300px``. 


.. _chart-themes:

Chart Themes
------------
Altair makes available a theme registry that lets users apply chart configurations
globally within any Python session. This is done via the ``alt.themes`` object.

The themes registry consists of functions which define a specification dictionary
that will be added to every created chart.
For example, the default theme configures the default size of a single chart:

    >>> import altair as alt
    >>> default = alt.themes.get()
    >>> default()
    {'config': {'view': {'continuousWidth': 300, 'continuousHeight': 300}}}

You can see that any chart you create will have this theme applied, and these configurations
added to its specification:

.. altair-plot::
    :output: repr

    import altair as alt
    from vega_datasets import data

    chart = alt.Chart(data.cars.url).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q'
    )

    chart.to_dict()

The rendered chart will then reflect these configurations:

.. altair-plot::

    chart

Changing the Theme
~~~~~~~~~~~~~~~~~~
If you would like to enable any other theme for the length of your Python session,
you can call ``alt.themes.enable(theme_name)``.
For example, Altair includes a theme in which the chart background is opaque
rather than transparent:

.. altair-plot::
    :output: repr

    alt.themes.enable('opaque')
    chart.to_dict()

.. altair-plot::

    chart

Notice that the background color of the chart is now set to white.
If you would like no theme applied to your chart, you can use the
theme named ``'none'``:

.. altair-plot::
    :output: repr

    alt.themes.enable('none')
    chart.to_dict()

.. altair-plot::

    chart

Because the view configuration is not set, the chart is smaller
than the default rendering.

If you would like to use any theme just for a single chart, you can use the
``with`` statement to enable a temporary theme:

.. altair-plot::
   :output: none

   with alt.themes.enable('default'):
       spec = chart.to_json()

Currently Altair does not offer many built-in themes, but we plan to add
more options in the future.

Defining a Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~
The theme registry also allows defining and registering custom themes.
A theme is simply a function that returns a dictionary of default values
to be added to the chart specification at rendering time, which is then
registered and activated.

For example, here we define a theme in which all marks are drawn with black
fill unless otherwise specified:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    # define the theme by returning the dictionary of configurations
    def black_marks():
        return {
            'config': {
                'view': {
                    'height': 300,
                    'width': 300,
                },
                'mark': {
                    'color': 'black',
                    'fill': 'black'
                }
            }
        }

    # register the custom theme under a chosen name
    alt.themes.register('black_marks', black_marks)

    # enable the newly registered theme
    alt.themes.enable('black_marks')

    # draw the chart
    cars = data.cars.url
    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q'
    )


If you want to restore the default theme, use:

.. altair-plot::
   :output: none

   alt.themes.enable('default')


For more ideas on themes, see the `Vega Themes`_ repository.


.. _Vega Themes: https://github.com/vega/vega-themes/
