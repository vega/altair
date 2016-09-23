.. _api-documentation:

Altair Documentation
====================

Altair's core functionality is to produce Vega-Lite JSON specifications, which
specify :ref:`mappings <encoding-reference>` between :ref:`data <defining-data>` and :ref:`graphical markings <mark-reference>`.


.. currentmodule:: altair


.. _defining-data:

Data in Altair
--------------

Each top-level chart object, including :class:`Chart`, :class:`LayeredChart`,
and :class:`FacetedChart`, can take a dataset as its first argument.
The dataset can be specified in one of three ways:

- as a `Pandas DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_
- as a :class:`Data` object
- as a url pointing to a ``json`` or ``csv`` formatted text file

For example, here we specify data via a dataframe:

.. altair-plot::

   from altair import Chart
   import pandas as pd

   data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                        'y': [5, 3, 6, 7, 2]})
   Chart(data).mark_bar().encode(
       x='x',
       y='y',
   )

When data is specified as a DataFrame, the encoding is quite simple, as Altair
uses the data type information provided by Pandas to automatically determine
the data types required in the encoding.

By comparison, here we create the same chart using a :class:`Data` object,
with the data specified as a JSON-style list of records:

.. altair-plot::

   from altair import Chart, Data

   data = Data(values=[{'x': 'A', 'y': 5},
                       {'x': 'B', 'y': 3},
                       {'x': 'C', 'y': 6},
                       {'x': 'D', 'y': 7},
                       {'x': 'E', 'y': 2}])
   Chart(data).mark_bar().encode(
       x='x:O',  # specify ordinal data
       y='y:Q',  # specify quantitative data
   )

notice the extra markup required in the encoding; because Altair cannot infer
the types within a :class:`Data` object, we must specify them manually
(here we use :ref:`shorthand-description` to specify *ordinal* (``O``) for ``x``
and *quantitative* (``Q``) for ``y``; see :ref:`data-types` below).

Similarly, we must also specify the data type when referencing data by URL:

.. altair-plot::

   from altair import Chart

   url = 'https://vega.github.io/vega-datasets/data/cars.json'

   Chart(url).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q'
   )

We will further discuss encodings and associated types below.

.. _encoding-reference:

Encodings
---------
The key to creating meaningful visualizations is to map *properties of the data*
to *visual properties* in order to effectively communicate information.
Altair abstracts this mapping through the idea of *channel encodings*.
For example, here we will plot the *cars* dataset using four of the available
channel encodings: ``x`` (the x-axis value), ``y`` (the y-axis value),
``color`` (the color of the marker), and ``shape`` (the shape of the point marker):

.. altair-plot::

   from altair import Chart, load_dataset

   cars = load_dataset('cars')

   Chart(cars).mark_point().encode(
       x='Horsepower',
       y='Miles_per_Gallon',
       color='Origin',
       shape='Origin'
   )

Altair automatically determines the correct datatype from the Data Frame columns,
and creates appropriate scales and legends to represent the data.

.. _encoding-channels:

Channels
~~~~~~~~

Altair provides a number of encoding channels that can be useful in different
circumstances; the following table summarizes them:

*TODO: link to examples of each*

Position Channels:

=======  ================  ============================  ===================================
Channel  Altair Class      Description                   Example
=======  ================  ============================  ===================================
column   :class:`Column`   The column of a faceted plot  :ref:`gallery_trellis_stacked_bar`
row      :class:`Row`      The row of a faceted plot     :ref:`gallery_trellis_barley`
x        :class:`X`        The x-axis value              :ref:`gallery_scatter`
y        :class:`Y`        The y-axis value              :ref:`gallery_circle`
=======  ================  ============================  ===================================

Channels with Legend:

=======  ================  ========================  =========================================
Channel  Altair Class      Description               Example
=======  ================  ========================  =========================================
color    :class:`Color`    The color of the mark     :ref:`gallery_stacked_area`
opacity  :class:`Opacity`  The opacity of the mark
shape    :class:`Shape`    The shape of the mark     :ref:`gallery_scatter_colored_with_shape`
size     :class:`Size`     The size of the mark      :ref:`gallery_scatter_binned`
=======  ================  ========================  =========================================

Order Channels:

=======  ================  ============================================  =================
Channel  Altair Class      Description                                   Example
=======  ================  ============================================  =================
order    :class:`Order`    --
path     :class:`Path`     --
=======  ================  ============================================  =================

Field Channels:

=======  ================  ============================================  ===========================
Channel  Altair Class      Description                                   Example
=======  ================  ============================================  ===========================
text     :class:`Text`     The text to display at each mark              :ref:`gallery_text_scatter_colored`
detail   :class:`Detail`   Additional level of detail for a grouping,
                           without mapping to any particular channel
label    :class:`Label`    --
=======  ================  ============================================  ===========================

.. _data-types:

Data Types
~~~~~~~~~~
The details of any mapping depend on the *type* of the data. Altair recognizes
four main data types:

============  ==============  ================================================
Data Type     Shorthand Code  Description
============  ==============  ================================================
quantitative  ``Q``           a continuous real-valued quantity
ordinal       ``O``           a discrete ordered quantity
nominal       ``N``           a discrete unordered category
temporal      ``T``           a time or date value
============  ==============  ================================================

These types can either be expressed in a long-form using the channel encoding
classes such as :class:`X` and :class:`Y`, or in short-form using the
:ref:`Shorthand Syntax <shorthand-description>` discussed below.
For example, the following two means of specifying the type result in identical
plot specifications:

>>> from altair import Chart, X
>>> chart = Chart().encode(
...             x=X('name', type='quantitative')
...         )
>>> print(chart.to_json())
{"encoding": {"x": {"field": "name", "type": "quantitative"}}}

>>> chart = Chart().encode(
...             x='name:Q'
...         )
>>> print(chart.to_json())
{"encoding": {"x": {"field": "name", "type": "quantitative"}}}

The shorthand form, ``"name:Q"``, is useful for its lack of boilerplate
when doing quick data explorations. The long-form,
``X('name', type='quantitative')``, is useful when adjusting binning, axis
properties, and other details of the mapping.

Specifying the correct type for your data is important, as it affects the
way Altair represents your encoding in the resulting plot.
As an example of this, here we will represent the same data three different ways,
with the color encoded as a *quantitative*, *ordinal*, and *nominal* type:

*TODO: use subplots here*

.. altair-setup::

   from altair import Chart, load_dataset
   cars = load_dataset('cars', url_only=True)

.. altair-plot::

   Chart(cars).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
       color='Cylinders:Q'           # Encode as quantitative (Q)
   )

.. altair-plot::

   Chart(cars).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
       color='Cylinders:O'           # Encode as ordinal (O)
   )

.. altair-plot::

   Chart(cars).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
       color='Cylinders:N'           # Encode as nominal (N)
   )

The type specification influences the way Altair, via Vega-Lite, chooses
a color scale to represent the value, and influences whether a discrete
or continuous legend is used.

.. _encoding-aggregates:

Binning and Aggregation
~~~~~~~~~~~~~~~~~~~~~~~

Beyond simple channel encodings, Altair's visualizations are built on the
concept of the database-style grouping and aggregation; that is, the
`split-apply-combine <https://www.jstatsoft.org/article/view/v040i01>`_
abstraction that underpins many data analyses.

For example, building a histogram from a one-dimensional dataset involves
splitting data based on the bin it falls in, aggregating the results within
each bin using a *count* of the data, and then combining the results into
a final figure.

In altair, such an operation looks like this:

.. altair-plot::

   from altair import load_dataset, Chart, X

   cars = load_dataset('cars')

   Chart(cars).mark_bar().encode(
       X('Horsepower', bin=True),
       y='count(*):Q'
       # could also use Y('*', aggregate='count', type='quantitative')
   )

Notice here we use the shorthand version of expressing an encoding channel
(see :ref:`shorthand-description`) with the ``count`` aggregation,
the special ``*`` wild-card identifier often used with counts,
and ``Q`` for quantitative type.

Similarly, we can create a two-dimensional histogram using, for example, the
size of points to indicate counts within the grid (sometimes called
a "Bubble Plot"):

.. altair-plot::

   from altair import load_dataset, Chart, X, Y

   cars = load_dataset('cars')

   Chart(cars).mark_point().encode(
       X('Horsepower', bin=True),
       Y('Miles_per_Gallon', bin=True),
       size='count(*):Q',
   )

There is no need, however, to limit aggregations to counts alone. For example,
we could similarly create a plot where the color of each point
represents the mean of a third quantity, such as acceleration:

.. altair-plot::

   from altair import load_dataset, Chart, X, Y

   cars = load_dataset('cars')

   Chart(cars).mark_circle().encode(
       X('Horsepower', bin=True),
       Y('Miles_per_Gallon', bin=True),
       size='count(*):Q',
       color='average(Acceleration):Q'
   )

In addition to ``count`` and ``average``, there are a large number of available
aggregation functions built into Altair; they are listed in the following table:

*TODO: fill-in examples*

=========  ========================================  =================================
Aggregate  Description                               Example
=========  ========================================  =================================
sum        Sum of values                             :ref:`gallery_bar_aggregate`
mean       Arithmetic mean of values                 :ref:`gallery_text_table_heatmap`
average    Arithmetic mean of values
count      Total number of values                    :ref:`gallery_scatter_binned`
distinct   Number of distinct values
variance   Variance of values
variancep  ??
stdev      Standard Deviation of values
stdevp     ??
median     Median of values
q1         First quartile of values
q3         Third quartile of values
modeskew   ??
min        Minimum value
max        Maximum value
argmin     Index of minimum value
argmax     Index of maximum value
values     ??
valid      ??
missing    ??
=========  ========================================  =================================


.. _shorthand-description:

Encoding Shorthands
~~~~~~~~~~~~~~~~~~~

For convenience, Altair allows the specification of the variable name along
with the aggregate and type within a simple shorthand string syntax.
This makes use of the type shorthand codes listed in :ref:`data-types`
as well as the aggregate names listed in :ref:`encoding-aggregates`.
The following table shows examples of the shorthand specification alongside
the long-form equivalent:

===================  ===================================================
Shorthand            Equivalent long-form
===================  ===================================================
``x='name'``         ``X('name')``
``x='name:Q'``       ``X('name', type='quantitative')``
``x='sum(name)'``    ``X('name', aggregate='sum')``
``x='sum(name):Q'``  ``X('name', aggregate='sum', type='quantitative')``
===================  ===================================================


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


.. _data-transformations:

Data Transformations
--------------------

Altair provides a data transformation API that allows both *filtering* and
*transformation* of values within the plot renderer. In both cases, the
expressions are given in terms of *javascript strings* passed to the
``transform_data`` method.

For example, consider this visualization of the historical US population,
split by age and gender:

.. altair-plot::

    from altair import Chart, Color, Scale

    data = 'https://vega.github.io/vega-datasets/data/population.json'
    pink_blue = Scale(range=["lightblue", "pink"])

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('sex:N', scale=pink_blue)
    )

This visualization shows that on average over the course of history, the
younger population has far outnumbered the older population.

1. We might wish to zero-in on a particular year, rather than taking a
   mean over all years.
2. The "1" and "2" labels for gender are not all that informative; we should
   probably be change them to "Male" and "Female" for clarity.

We could certainly accomplish this by downloading the dataset, manipulating it
in, say, pandas, and building a chart using the result, but it would be nice to
do this within the Altair spec itself so that we can use the original data
source.

What we're looking for is a ``filter`` operation in the first case, and a
``calculate`` operation in the second. Altair exposes these via the
:meth:`Chart.transform_data` method, which passes its arguments to the
:class:`Transform` class:

.. altair-trait-table:: Transform

Let's remake the plot, using these transformation operations: we'll use
``filter`` to limit the year to 2000, and ``calculate`` to convert the
*1/2* labels to *Male/Female*:

.. altair-plot::

    from altair import Chart, Color, Scale, Formula

    data = 'https://vega.github.io/vega-datasets/data/population.json'
    pink_blue = Scale(range=["pink", "lightblue"])

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('gender:N', scale=pink_blue)
    ).transform_data(
        filter='datum.year == 2000',
        calculate=[Formula(field='gender',
                           expr='datum.sex == 1 ? "Male" : "Female"')],
    )

The ``filter`` attribute of :meth:`~Chart.transform_data` accepts a string of
javascript code, referring to the data column name as an attribute of
``datum``, which you can think of as the row within the dataset.
The `calculate`` attribute accepts a list of :class:`Formula` objects, which
each define a new column using a javascript expression over existing columns.

The :ref:`gallery_bar_grouped` example shows a more refined view of this dataset
using these techniques.


.. _configuring-altair:

Configuring Plots
-----------------

.. todo

*Coming soon*
