.. currentmodule:: altair

.. _user-guide-mark:

Marks
-----

We saw in :ref:`user-guide-encoding` that the :meth:`~Chart.encode` method is
used to map columns to visual attributes of the plot.
The ``mark`` property is what specifies how exactly those attributes
should be represented on the plot.

Altair provides a number of basic mark properties:

==========  ============================  ===================================================  ====================================
Mark Name   Method                        Description                                          Example
==========  ============================  ===================================================  ====================================
arc         :meth:`~Chart.mark_arc`       A pie chart.                                         :ref:`gallery_pie_chart`
area        :meth:`~Chart.mark_area`      A filled area plot.                                  :ref:`gallery_simple_stacked_area_chart`
bar         :meth:`~Chart.mark_bar`       A bar plot.                                          :ref:`gallery_simple_bar_chart`
circle      :meth:`~Chart.mark_circle`    A scatter plot with filled circles.                  :ref:`gallery_one_dot_per_zipcode`
geoshape    :meth:`~Chart.mark_geoshape`  A geographic shape                                   :ref:`gallery_choropleth`
image       :meth:`~Chart.mark_image`     A scatter plot with image markers.                   :ref:`user-guide-image-mark`
line        :meth:`~Chart.mark_line`      A line plot.                                         :ref:`gallery_simple_line_chart`
point       :meth:`~Chart.mark_point`     A scatter plot with configurable point shapes.       :ref:`gallery_scatter_linked_brush`
rect        :meth:`~Chart.mark_rect`      A filled rectangle, used for heatmaps                :ref:`gallery_simple_heatmap`
rule        :meth:`~Chart.mark_rule`      A vertical or horizontal line spanning the axis.     :ref:`gallery_candlestick_chart`
square      :meth:`~Chart.mark_square`    A scatter plot with filled squares.                  N/A
text        :meth:`~Chart.mark_text`      A scatter plot with points represented by text.      :ref:`gallery_bar_chart_with_labels`
tick        :meth:`~Chart.mark_tick`      A vertical or horizontal tick mark.                  :ref:`gallery_strip_plot`
trail       :meth:`~Chart.mark_trail`     A line with variable widths.                         :ref:`gallery_trail_marker`
==========  ============================  ===================================================  ====================================

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

.. _user-guide-image-mark:

Image Mark
~~~~~~~~~~
The image mark, unlike other simple marks, requires the mark to include a
``url`` encoding, which specifies the PNG to use for the image:

.. altair-plot::

   import altair as alt
   import pandas as pd
   
   source = pd.DataFrame.from_records([
         {"x": 0.5, "y": 0.5, "img": "https://vega.github.io/vega-datasets/data/ffox.png"},
         {"x": 1.5, "y": 1.5, "img": "https://vega.github.io/vega-datasets/data/gimp.png"},
         {"x": 2.5, "y": 2.5, "img": "https://vega.github.io/vega-datasets/data/7zip.png"}
   ])
   
   alt.Chart(source).mark_image(
       width=50, 
       height=50
   ).encode(
       x='x', 
       y='y', 
       url='img'
   )

.. _user-guide-compound-marks:

Compound Marks
~~~~~~~~~~~~~~

BoxPlot
^^^^^^^

The compound mark :meth:`~Chart.mark_boxplot` can be used to create a boxplot without having to specify each part of the plot (box, whiskers, outliers) separately.


.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.population.url

    alt.Chart(source).mark_boxplot().encode(
        y='people:Q'
    ).properties(
        width=200, 
        height=300
    )


To create a side-by-side boxplot, simply encode the group column on the other axis.


.. altair-plot::

  import altair as alt
  from vega_datasets import data

  source = data.population.url

  alt.Chart(source).mark_boxplot().encode(
      x='age:O',
      y='people:Q'
  )

Note that the default behavior is to display outliers as points, where an outlier is defined as any point more than 1.5 IQRs from the box.  
Users can adjust this threshold using the ``extent`` property of the mark.


.. altair-plot::

  import altair as alt
  from vega_datasets import data

  source = data.population.url

  alt.Chart(source).mark_boxplot(extent=3.0).encode(
      x='age:O',
      y='people:Q'
  )


The outliers can be ignored completely using ``extent='min-max'``


.. altair-plot::


  import altair as alt
  from vega_datasets import data

  source = data.population.url

  alt.Chart(source).mark_boxplot(extent='min-max').encode(
      x='age:O',
      y='people:Q'
  )

Mark Properties
~~~~~~~~~~~~~~~

As seen in the last two examples, additional arguments to ``mark_*()`` methods are passed along to an
associated :class:`MarkDef` instance, which supports the following attributes:

.. altair-object-table:: altair.MarkDef

Marks can also be configured globally using chart-level configurations; see
:ref:`config-mark` for details.
