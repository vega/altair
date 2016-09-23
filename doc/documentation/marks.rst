.. _mark-reference:

Marks
-----
The chart encoding maps data columns to visual plot attributes; the ``mark``
property specifies how those attributes should be represented.
Altair provides a number of mark properties:

*TODO: fill-in examples*

==========  ==========================  ===================================================  ====================================
Mark Name   Method                      Description                                          Example
==========  ==========================  ===================================================  ====================================
area        :meth:`~Chart.mark_area`    A filled area plot.                                  :ref:`gallery_area`
bar         :meth:`~Chart.mark_bar`     A bar plot.                                          :ref:`gallery_bar_aggregate`
circle      :meth:`~Chart.mark_circle`  A scatter plot with filled circles.                  :ref:`gallery_bubble_health_income`
line        :meth:`~Chart.mark_line`    A line plot.                                         :ref:`gallery_line_color`
point       :meth:`~Chart.mark_point`   A scatter plot with configurable point shapes.       :ref:`gallery_scatter_binned`
rule        :meth:`~Chart.mark_rule`    A vertical or horizontal line spanning the axis.
square      :meth:`~Chart.mark_square`  A scatter plot with filled squares.
text        :meth:`~Chart.mark_text`    A scatter plot with points represented by text       :ref:`gallery_text_scatter_colored`
tick        :meth:`~Chart.mark_tick`    A vertical or horizontal tick mark.                  :ref:`gallery_tick_strip`
==========  ==========================  ===================================================  ====================================

In Altair, marks can be most conveniently specified by the ``mark_*`` methods
of the Chart object, which take optional keyword arguments that are passed
to :class:`MarkConfig` to configure the look of the marks.
For example, the following uses :meth:`~Chart.mark_circle` to represent
points as red semi-transparent filled circles:

.. altair-plot::

   from altair import Chart

   url = 'https://vega.github.io/vega-datasets/data/cars.json'

   Chart(url).mark_circle(
       color='red',
       opacity=0.3
   ).encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q'
   )
