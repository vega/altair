.. currentmodule:: altair

.. _user-guide-marks:

Marks
~~~~~

We saw in :ref:`user-guide-encoding` that the :meth:`~Chart.encode` method is
used to map columns to visual attributes of the plot.
The ``mark`` property is what specifies how exactly those attributes
should be represented on the plot.

Altair provides a number of basic mark properties
(the mark properties column links to the Vega-Lite documentation
that allows you to interactively explore the effects of modifying each property):

=========================================  =========================================  ================================================================================
Mark                                       Method                                     Description
=========================================  =========================================  ================================================================================
:ref:`user-guide-arc-marks`                :meth:`~Chart.mark_arc`                    A pie chart.  
:ref:`user-guide-area-marks`               :meth:`~Chart.mark_area`                   A filled area plot.                                  
bar                                        :meth:`~Chart.mark_bar`                    A bar plot.                                          
circle                                     :meth:`~Chart.mark_circle`                 A scatter plot with filled circles.                  
geoshape                                   :meth:`~Chart.mark_geoshape`               Visualization containing spatial data
image                                      :meth:`~Chart.mark_image`                  A scatter plot with image markers.  
line                                       :meth:`~Chart.mark_line`                   A line plot.
point                                      :meth:`~Chart.mark_point`                  A scatter plot with configurable point shapes.
rect                                       :meth:`~Chart.mark_rect`                   A filled rectangle, used for heatmaps                
rule                                       :meth:`~Chart.mark_rule`                   A vertical or horizontal line spanning the axis.     
square                                     :meth:`~Chart.mark_square`                 A scatter plot with filled squares.                  
text                                       :meth:`~Chart.mark_text`                   A scatter plot with points represented by text.      
tick                                       :meth:`~Chart.mark_tick`                   A vertical or horizontal tick mark.                  
trail                                      :meth:`~Chart.mark_trail`                  A line with variable widths.
=========================================  =========================================  ================================================================================

In addition, Altair provides the following compound marks:

==========  ==============================  ================================  ==================================
Mark Name   Method                          Description                       Example
==========  ==============================  ================================  ==================================
box plot    :meth:`~Chart.mark_boxplot`     A box plot.                       :ref:`gallery_boxplot`
error band  :meth:`~Chart.mark_errorband`   A continuous band around a line.  :ref:`gallery_line_with_ci`
error bar   :meth:`~Chart.mark_errorbar`    An errorbar around a point.       :ref:`gallery_errorbars_with_ci`
==========  ==============================  ================================  ==================================

In Altair, marks can be most conveniently specified by the ``mark_*`` methods
of the Chart object, which take optional keyword arguments that are passed to
:class:`MarkDef` to configure the look of the marks.

Mark Properties
_______________

As seen in the last two examples, additional arguments to ``mark_*()`` methods are passed along to an
associated :class:`MarkDef` instance, which supports the following attributes:

.. altair-object-table:: altair.MarkDef

.. toctree::
   :hidden:

   arc
   area

