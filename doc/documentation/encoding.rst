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
