.. currentmodule:: altair

.. _user-guide-configuration:

Top-Level Chart Configuration
=============================
Many aspects of a chart's appearance can be configured at the top level using
the ``configure_*()`` methods.
These methods and the properties that they set are only valid at the top level
of a chart, and can be thought of as a way of setting a chart theme: that is,
they set the default styles for the entire chart, and these defaults can be
overridden by specific style settings associated with chart elements.

These methods and their arguments will be outlined below:


- :ref:`config-chart` :meth:`Chart.configure`
- :ref:`config-axis` :meth:`Chart.configure_axis`
- :ref:`config-header` :meth:`Chart.configure_header`
- :ref:`config-legend` :meth:`Chart.configure_legend`
- :ref:`config-mark` :meth:`Chart.configure_mark`
- :ref:`config-scale` :meth:`Chart.configure_scale`
- :ref:`config-range` :meth:`Chart.configure_range`
- :ref:`config-projection` :meth:`Chart.configure_projection`
- :ref:`config-selection` :meth:`Chart.configure_selection`
- :ref:`config-title` :meth:`Chart.configure_title`
- :ref:`config-view` :meth:`Chart.configure_view`




.. _config-chart:

Chart Configuration
-------------------
The :meth:`Chart.configure` method adds a :class:`Config` instance to the chart,
and has the following attributes:

.. altair-object-table:: altair.Config



.. _config-axis:

Axis Configuration
------------------
Axis configuration defines default settings for axes, and can be set using
the :meth:`Chart.configure_axis` method.
Properties defined here are applied to all axes in the figure.

Additional property blocks can target more specific axis types based on the
orientation ("axisX", "axisY", "axisLeft", "axisTop", etc.) or band scale
type ("axisBand").
For example, properties defined under the "axisBand"
property will only apply to axes visualizing "band" scales.
If multiple axis config blocks apply to a single axis, type-based options
take precedence over orientation-based options, which in turn take precedence
over general options.

The methods are the following:

- :meth:`Chart.configure_axis`
- :meth:`Chart.configure_axisBand`
- :meth:`Chart.configure_axisBottom`
- :meth:`Chart.configure_axisLeft`
- :meth:`Chart.configure_axisRight`
- :meth:`Chart.configure_axisTop`
- :meth:`Chart.configure_axisX`
- :meth:`Chart.configure_axisY`

They have the following properties:

.. altair-object-table:: altair.AxisConfig


.. _config-header:

Header Configuration
--------------------
The :meth:`Chart.configure_header` method allows configuration of facet headers,
including the font, color, size, and position of the title and labels.
Here is an example:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        column='Origin:N'
    ).properties(
        width=180,
        height=180
    )

    chart.configure_header(
        titleColor='green',
        titleFontSize=14,
        labelColor='red',
        labelFontSize=14
    )

.. altair-object-table:: altair.HeaderConfig


.. _config-legend:

Legend Configuration
--------------------
The :meth:`Chart.configure_legend` allows you to customize the appearance of chart
legends, including location, fonts, bounding boxes, colors, and more.
Here is an example:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )

    chart.configure_legend(
        strokeColor='gray',
        fillColor='#EEEEEE',
        padding=10,
        cornerRadius=10,
        orient='top-right'
    )

Additional properties are  summarized in the following table:

.. altair-object-table:: altair.LegendConfig


.. _config-mark:

Mark and Mark Style Configuration
---------------------------------
The mark configuration can be set using the :meth:`Chart.configure_mark`
method, which sets the default properties for all marks in the chart.
In addition, the config object also provides mark-specific configuration
using the mark type (e.g. :meth:`Chart.configure_area`) for
defining default properties for each mark.

For general configuration of all mark types, use:

- :meth:`Chart.configure_mark`

For configurations specific to particular mark types, use:

- :meth:`Chart.configure_area`
- :meth:`Chart.configure_bar`
- :meth:`Chart.configure_circle`
- :meth:`Chart.configure_geoshape`
- :meth:`Chart.configure_line`
- :meth:`Chart.configure_point`
- :meth:`Chart.configure_rect`
- :meth:`Chart.configure_rule`
- :meth:`Chart.configure_square`
- :meth:`Chart.configure_text`
- :meth:`Chart.configure_tick`
- :meth:`Chart.configure_trail`

Each of the above methods accepts the following properties:

.. altair-object-table:: altair.MarkConfig

In addition to the default mark properties above, default values can be
further customized using named styles defined as keyword arguments to
the :meth:`Chart.configure_style` method.
Styles can then be invoked by including a style property within a mark
definition object.


.. _config-scale:

Scale Configuration
-------------------
Scales can be configured using :meth:`Chart.configure_scale`, which has
the following properties:

.. altair-object-table:: altair.ScaleConfig


.. _config-range:

Scale Range Configuration
-------------------------
Scale ranges can be configured using :meth:`Chart.configure_range`, which has
the following properties:

.. altair-object-table:: altair.RangeConfig


.. _config-projection:

Projection Configuration
------------------------
:meth:`Chart.configure_projection`

.. altair-object-table:: altair.ProjectionConfig


.. _config-selection:

Selection Configuration
-----------------------
:meth:`Chart.configure_selection`

.. altair-object-table:: altair.SelectionConfig


.. _config-title:

Title Configuration
-------------------
The :meth:`Chart.configure_title` method allows configuration of the chart
title, including the font, color, placement, and orientation.
Here is an example 
here is an example:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
    ).properties(
        title='Cars Data'
    )

    chart.configure_title(
        fontSize=20,
        font='Courier',
        anchor='start',
        color='gray'
    )

Additional title configuration options are listed in the following table:

.. altair-object-table:: altair.VgTitleConfig


.. _config-view:

View Configuration
------------------
The :meth:`Chart.configure_view` method allows you to configure aspecs of the
chart's *view*, i.e. the area of the screen in which the data and scales are
drawn. Here is an example to demonstrate some of the visual features that can
be controlled:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
    )

    chart.configure_view(
        height=200,
        width=200,
        strokeWidth=4,
        fill='#FFEEDD',
        stroke='red',
    )

Additional properties are summarized in the following table:

.. altair-object-table:: altair.ViewConfig


Removing the border
~~~~~~~~~~~~~~~~~~~

By default, charts have both a grid and an outside border. To create a chart with no border, you will need to remove them both.

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

You'll note that while the inside rules are gone, the outside border remains. Hide it by setting the `strokeWidth` or the `strokeOpacity` options on :meth:`Chart.configure_view` to `0`.

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


It is also possible to completely remove all borders and axes by combining the above option with setting `axis` to `None` during encoding.

..altair-plot::

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


.. _chart-themes:

Altair Themes
-------------
Altair makes available a theme registry that lets users apply chart configurations
globally within any Python session. This is done via the ``alt.themes`` object.

The themes registry consists of functions which define a specification dictionary
that will be added to every created chart.
For example, the default theme configures the default size of a single chart:

    >>> import altair as alt
    >>> default = alt.themes.get()
    >>> default()
    {'config': {'view': {'height': 300, 'width': 400}}}

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
                    'width': 400,
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
