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

For more discussion of approaches to chart customization, see
:ref:`user-guide-customization`.


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
- :meth:`Chart.configure_axisDiscrete`
- :meth:`Chart.configure_axisPoint`
- :meth:`Chart.configure_axisQuantitative`
- :meth:`Chart.configure_axisTemporal`
- :meth:`Chart.configure_axisXBand`
- :meth:`Chart.configure_axisXDiscrete`
- :meth:`Chart.configure_axisXPoint`
- :meth:`Chart.configure_axisXQuantitative`
- :meth:`Chart.configure_axisXTemporal`
- :meth:`Chart.configure_axisYBand`
- :meth:`Chart.configure_axisYDiscrete`
- :meth:`Chart.configure_axisYPoint`
- :meth:`Chart.configure_axisYQuantitative`
- :meth:`Chart.configure_axisYTemporal`

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

Additional properties are summarized in the following table:

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
Projections can be configured using :meth:`Chart.configure_projection`,
which has the following properties:

.. altair-object-table:: altair.ProjectionConfig


.. _config-selection:

Selection Configuration
-----------------------
Selections can be configured using :meth:`Chart.configure_selection`, 
which has the following properties:

.. altair-object-table:: altair.SelectionConfig


.. _config-title:

Title Configuration
-------------------
The :meth:`Chart.configure_title` method allows configuration of the chart
title, including the font, color, placement, and orientation.
Here is an example:

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

.. altair-object-table:: altair.TitleConfig


.. _config-view:

View Configuration
------------------
The :meth:`Chart.configure_view` method allows you to configure aspects of the
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
        continuousHeight=200,
        continuousWidth=200,
        strokeWidth=4,
        fill='#FFEEDD',
        stroke='red',
    )

Additional properties are summarized in the following table:

.. altair-object-table:: altair.ViewConfig

