.. currentmodule:: altair

.. _user-guide-mark:

Marks
-----

We saw in :ref:`user-guide-encoding` that the :meth:`~Chart.encode` method is
used to map columns to visual attributes of the plot.
The ``mark`` property is what specifies how exactly those attributes
should be represented on the plot.

Altair provides a number of mark properties:

==========  ============================  ===================================================  ====================================
Mark Name   Method                        Description                                          Example
==========  ============================  ===================================================  ====================================
area        :meth:`~Chart.mark_area`      A filled area plot.
bar         :meth:`~Chart.mark_bar`       A bar plot.
circle      :meth:`~Chart.mark_circle`    A scatter plot with filled circles.
geoshape    :meth:`~Chart.mark_geoshape`  A geographic shape
line        :meth:`~Chart.mark_line`      A line plot.
point       :meth:`~Chart.mark_point`     A scatter plot with configurable point shapes.
rect        :meth:`~Chart.mark_rect`      A filled rectangle, used for heatmaps
rule        :meth:`~Chart.mark_rule`      A vertical or horizontal line spanning the axis.
square      :meth:`~Chart.mark_square`    A scatter plot with filled squares.
text        :meth:`~Chart.mark_text`      A scatter plot with points represented by text
tick        :meth:`~Chart.mark_tick`      A vertical or horizontal tick mark.
==========  ============================  ===================================================  ====================================

In Altair, marks can be most conveniently specified by the ``mark_*`` methods
of the Chart object, which take optional keyword arguments that are passed to
:class:`MarkDef` to configure the look of the marks.

For example, the following uses :meth:`~Chart.mark_circle` with additional
arguments to represent points as red semi-transparent filled circles:

.. altair-plot::

   import altair as alt
   from vega_datasets import data

   url = data.cars.url

   alt.Chart(url).mark_circle(
       color='red',
       opacity=0.3
   ).encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q'
   )

The additional arguments to ``mark_*()`` methods are passed along to an
associated :class:`MarkDef` instance, which supports the following attributes:

.. altair-object-table:: altair.MarkDef

Marks can also be configured globally using chart-level configurations; see
:ref:`config-mark` for details.
