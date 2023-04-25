.. currentmodule:: altair

.. _user-guide-encoding-channels:

Channels
--------

Altair provides a number of encoding channels that can be useful in different
circumstances. The following sections summarize them:

Position
~~~~~~~~

==========  ===================  =================================  ===================================
Channel     Altair Class         Description                        Example
==========  ===================  =================================  ===================================
x           :class:`X`           The x-axis value                   :ref:`gallery_scatter_tooltips`
y           :class:`Y`           The y-axis value                   :ref:`gallery_scatter_tooltips`
x2          :class:`X2`          Second x value for ranges          :ref:`gallery_gantt_chart`
y2          :class:`Y2`          Second y value for ranges          :ref:`gallery_candlestick_chart`
longitude   :class:`Longitude`   Longitude for geo charts           :ref:`gallery_point_map`
latitude    :class:`Latitude`    Latitude for geo charts            :ref:`gallery_point_map`
longitude2  :class:`Longitude2`  Second longitude value for ranges  :ref:`gallery_airport_connections`
latitude2   :class:`Latitude2`   Second latitude value for ranges   :ref:`gallery_airport_connections`
xError      :class:`XError`      The x-axis error value             N/A
yError      :class:`YError`      The y-axis error value             N/A
xError2     :class:`XError2`     The second x-axis error value      N/A
yError2     :class:`YError2`     The second y-axis error value      N/A
xOffset     :class:`XOffset`     Offset to the x position           :ref:`gallery_grouped_bar_chart2`
yOffset     :class:`YOffset`     Offset to the y position           :ref:`gallery_strip_plot_jitter`
theta       :class:`Theta`       The start arc angle                :ref:`gallery_radial_chart`
theta2      :class:`Theta2`      The end arc angle (radian)         :ref:`gallery_pacman_chart`
==========  ===================  =================================  ===================================

Mark Property
~~~~~~~~~~~~~

=============  ======================  ==============================  =========================================
Channel        Altair Class            Description                     Example
=============  ======================  ==============================  =========================================
angle          :class:`Angle`          The angle of the mark           :ref:`gallery_wind_vector_map`
color          :class:`Color`          The color of the mark           :ref:`gallery_simple_heatmap`
fill           :class:`Fill`           The fill for the mark           :ref:`gallery_ridgeline_plot`
fillopacity    :class:`FillOpacity`    The opacity of the mark's fill  N/A
opacity        :class:`Opacity`        The opacity of the mark         :ref:`gallery_horizon_graph`
radius         :class:`Radius`         The radius or the mark          :ref:`gallery_radial_chart`
shape          :class:`Shape`          The shape of the mark           :ref:`gallery_us_incomebrackets_by_state_facet`
size           :class:`Size`           The size of the mark            :ref:`gallery_table_bubble_plot_github`
stroke         :class:`Stroke`         The stroke of the mark          N/A
strokeDash     :class:`StrokeDash`     The stroke dash style           :ref:`gallery_multi_series_line`
strokeOpacity  :class:`StrokeOpacity`  The opacity of the line         N/A
strokeWidth    :class:`StrokeWidth`    The width of the line           N/A
=============  ======================  ==============================  =========================================

Text and Tooltip
^^^^^^^^^^^^^^^^

=======  ================  ========================  =========================================
Channel  Altair Class      Description               Example
=======  ================  ========================  =========================================
text     :class:`Text`     Text to use for the mark  :ref:`gallery_scatter_with_labels`
tooltip  :class:`Tooltip`  The tooltip value         :ref:`gallery_scatter_tooltips`
=======  ================  ========================  =========================================

.. _hyperlink-channel:

Hyperlink
~~~~~~~~~

=======  ================  ========================  =========================================
Channel  Altair Class      Description               Example
=======  ================  ========================  =========================================
href     :class:`Href`     Hyperlink for  points     :ref:`gallery_scatter_href`
=======  ================  ========================  =========================================

Detail
~~~~~~

Grouping data is an important operation in data visualization. For line and area marks,
mapping an unaggregated data field to any
non-position channel will group the lines and stacked areas by that field.
For aggregated plots, all unaggregated fields encoded are used as grouping fields
in the aggregation (similar to fields in ``GROUP BY`` in SQL).

The ``detail`` channel specifies an additional grouping field (or fields) for grouping
data without mapping the field(s) to any visual properties.

=======  ================  ===============================  =========================================
Channel  Altair Class      Description                      Example
=======  ================  ===============================  =========================================
detail   :class:`Detail`   Additional property to group by  :ref:`gallery_ranged_dot_plot`
=======  ================  ===============================  =========================================

For example here is a line chart showing stock prices of 5 tech companies over time.
We map the ``symbol`` variable to ``detail`` to use them to group lines.

.. altair-plot::
    
    import altair as alt
    from vega_datasets import data

    source = data.stocks()
    alt.Chart(source).mark_line().encode(
        x="date:T",
        y="price:Q",
        detail="symbol:N"
    )


Order
~~~~~

The ``order`` option and :class:`Order` channel can sort how marks are drawn on the chart.

For stacked marks, this controls the order of components of the stack. Here, the elements of each bar are sorted alphabetically by the name of the nominal data in the color channel.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    barley = data.barley()

    alt.Chart(barley).mark_bar().encode(
        x='variety:N',
        y='sum(yield):Q',
        color='site:N',
        order=alt.Order("site").sort("ascending")
    )

The order can be reversed by changing the sort option to `descending`.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    barley = data.barley()

    alt.Chart(barley).mark_bar().encode(
        x='variety:N',
        y='sum(yield):Q',
        color='site:N',
        order=alt.Order("site").sort("descending")
    )

The same approach works for other mark types, like stacked areas charts.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    barley = data.barley()

    alt.Chart(barley).mark_area().encode(
        x='variety:N',
        y='sum(yield):Q',
        color='site:N',
        order=alt.Order("site").sort("ascending")
    )

Note that unlike the ``sort`` parameter to positional encoding channels,
the :class:`Order` channel cannot take a list of values to sort by
and is not automatically sorted when an ordered pandas categorical column is passed.
If we want to sort stacked segments in a custom order, we can `follow the approach in this issue comment <https://github.com/altair-viz/altair/issues/245#issuecomment-748443434>`_, although there might be edge cases where this is not fully supported. This workaround also makes the order of the segments align with the order that the colors shows up in a legend that uses custom sorting for the color domain.

For line marks, the :class:`Order` channel encodes the order in which data points are connected. This can be useful for creating a scatter plot that draws lines between the dots using a different field than the x and y axes.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    driving = data.driving()

    alt.Chart(driving).mark_line(point=True).encode(
        alt.X('miles').scale(zero=False),
        alt.Y('gas').scale(zero=False),
        order='year'
    )

Facet
~~~~~
For more information, see :ref:`facet-chart`.

=======  ================  ===============================================  =============================================
Channel  Altair Class      Description                                      Example
=======  ================  ===============================================  =============================================
column   :class:`Column`   The column of a faceted plot                     :ref:`gallery_trellis_scatter_plot`
row      :class:`Row`      The row of a faceted plot                        :ref:`gallery_beckers_barley_trellis_plot`
facet    :class:`Facet`    The row and/or column of a general faceted plot  :ref:`gallery_us_population_over_time_facet`
=======  ================  ===============================================  =============================================
