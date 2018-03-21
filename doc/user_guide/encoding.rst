.. currentmodule:: altair

.. _user-guide-encoding:

Encodings
---------

The key to creating meaningful visualizations is to map *properties of the data*
to *visual properties* in order to effectively communicate information.
Altair abstracts this mapping through the idea of *channel encodings*.
For example, here we will plot the *cars* dataset using four of the available
channel encodings: ``x`` (the x-axis value), ``y`` (the y-axis value),
``color`` (the color of the marker), and ``shape`` (the shape of the point marker):

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   cars = data.cars()

   alt.Chart(cars).mark_point().encode(
       x='Horsepower',
       y='Miles_per_Gallon',
       color='Origin',
       shape='Origin'
   )

For data specified as a DataFrame, Altair can automatically determine the
correct data type for each encoding, and creates appropriate scales and
legends to represent the data.

.. _encoding-channels:

Channels
~~~~~~~~

Altair provides a number of encoding channels that can be useful in different
circumstances; the following table summarizes them:

*TODO: link to examples of each*

Position Channels:

==========  ===================  =================================  ===================================
Channel     Altair Class         Description                        Example
==========  ===================  =================================  ===================================
x           :class:`X`           The x-axis value
y           :class:`Y`           The y-axis value
x2          :class:`X2`          Second x value for ranges
y2          :class:`Y2`          Second y value for ranges
longitude   :class:`Longitude`   Longitude for geo charts
latitude    :class:`Latitude`    Latitude for geo charts
longitude2  :class:`Longitude2`  Second longitude value for ranges
latitude2   :class:`Latitude2`   Second latitude value for ranges
==========  ===================  =================================  ===================================

Mark Property Channels:

=======  ================  ========================  =========================================
Channel  Altair Class      Description               Example
=======  ================  ========================  =========================================
color    :class:`Color`    The color of the mark
fill     :class:`Fill`     The fill for the mark
opacity  :class:`Opacity`  The opacity of the mark
shape    :class:`Shape`    The shape of the mark
size     :class:`Size`     The size of the mark
stroke   :class:`Stroke`   The stroke of the mark
=======  ================  ========================  =========================================

Text and Tooltip Channels:

=======  ================  ========================  =========================================
Channel  Altair Class      Description               Example
=======  ================  ========================  =========================================
text     :class:`Text`     Text to use for the mark
key      :class:`Key`      --
tooltip  :class:`Tooltip`  The tooltip value
=======  ================  ========================  =========================================

Hyperlink Channel:

=======  ================  ========================  =========================================
Channel  Altair Class      Description               Example
=======  ================  ========================  =========================================
href     :class:`Href`     Hyperlink for  points
=======  ================  ========================  =========================================

Level of Detail Channel:

=======  ================  ===============================  =========================================
Channel  Altair Class      Description                      Example
=======  ================  ===============================  =========================================
detail   :class:`Detail`   Additional property to group by
=======  ================  ===============================  =========================================

Order Channels:

=======  ================  ============================================  =================
Channel  Altair Class      Description                                   Example
=======  ================  ============================================  =================
order    :class:`Order`    --
=======  ================  ============================================  =================

Facet Channels:

=======  ================  ============================  ===================================
Channel  Altair Class      Description                   Example
=======  ================  ============================  ===================================
column   :class:`Column`   The column of a faceted plot
row      :class:`Row`      The row of a faceted plot
=======  ================  ============================  ===================================



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

If types are not specified for data input as a DataFrame, Altair defaults to
``quantitative`` for any numeric data, ``temporal`` for date/time data, and
``nominal`` for string data, but be aware that these defaults are by no means
always the correct choice!

The types can either be expressed in a long-form using the channel encoding
classes such as :class:`X` and :class:`Y`, or in short-form using the
:ref:`Shorthand Syntax <shorthand-description>` discussed below.
For example, the following two methods of specifying the type will lead to
identical plots:

.. altair-plot::

   alt.Chart(cars).mark_point().encode(
       x='Acceleration:Q',
       y='Miles_per_Gallon:Q',
       color='Origin:N'
   )

.. altair-plot::

  alt.Chart(cars).mark_point().encode(
      alt.X('Acceleration', type='quantitative'),
      alt.Y('Miles_per_Gallon', type='quantitative'),
      alt.Color('Origin', type='nominal')
  )

The shorthand form, ``x="name:Q"``, is useful for its lack of boilerplate
when doing quick data explorations. The long-form,
``alt.X('name', type='quantitative')``, is useful when doing more fine-tuned
adjustments to the encoding, such as binning, axis and scale properties,
or more.

Specifying the correct type for your data is important, as it affects the
way Altair represents your encoding in the resulting plot.

.. _type-legend-scale:

Effect of Data Type on Color Scales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As an example of this, here we will represent the same data three different ways,
with the color encoded as a *quantitative*, *ordinal*, and *nominal* type,
using three vertically-concatenated charts (see :ref:`vconcat`):

.. altair-plot::

   base = alt.Chart(cars).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
   ).properties(
       width=150,
       height=150
   )

   alt.vconcat(
      base.encode(color='Cylinders:Q').properties(title='quantitative'),
      base.encode(color='Cylinders:O').properties(title='ordinal'),
      base.encode(color='Cylinders:N').properties(title='nominal'),
   )

The type specification influences the way Altair, via Vega-Lite, decides on
the color scale to represent the value, and influences whether a discrete
or continuous legend is used.

.. _type-axis-scale:

Effect of Data Type on Axis Scales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similarly, for x and y axis encodings, the type used for the data will affect
the scales used and the characteristics of the mark. For example, here is the
difference between a ``quantitative`` and ``ordinal`` scale for an column
that contains integers specifying a year:

.. altair-plot::

    pop = data.population.url

    base = alt.Chart(pop).mark_bar().encode(
        alt.Y('mean(people):Q', axis=alt.Axis(title='total population'))
    ).properties(
        width=200,
        height=200
    )

    alt.hconcat(
        base.encode(x='year:Q').properties(title='year=quantitative'),
        base.encode(x='year:O').properties(title='year=ordinal')
    )

In altair, quantitative scales always start at zero unless otherwise
specified, while ordinal scales are limited to the values within the data.

Overriding the behavior of including zero in the axis, we see that even then
the precise appearance of the marks representing the data are affected by
the data type:

.. altair-plot::

    base.encode(
        alt.X('year:Q',
            scale=alt.Scale(zero=False)
        )
    )

Because quantitative values do not have an inherent width, the bars do not
fill the entire space between the values.
This view also makes clear the missing year of data that was not immediately
apparent when we treated the years as categories.

This kind of behavior is sometimes surprising to new users, but it emphasizes
the importance of thinking carefully about your data types when visualizing
data: a visual encoding that is suitable for categorical data may not be
suitable for quantitative data, and vice versa.


.. _encoding-aggregates:

Binning and Aggregation
~~~~~~~~~~~~~~~~~~~~~~~

Beyond simple channel encodings, Altair's visualizations are built on the
concept of the database-style grouping and aggregation; that is, the
`split-apply-combine <https://www.jstatsoft.org/article/view/v040i01>`_
abstraction that underpins many data analysis approaches.

For example, building a histogram from a one-dimensional dataset involves
splitting data based on the bin it falls in, aggregating the results within
each bin using a *count* of the data, and then combining the results into
a final figure.

In Altair, such an operation looks like this:

.. altair-plot::

   alt.Chart(cars).mark_bar().encode(
       alt.X('Horsepower', bin=True),
       y='count(*):Q'
       # could also use alt.Y(aggregate='count', type='quantitative')
   )

Notice here we use the shorthand version of expressing an encoding channel
(see :ref:`shorthand-description`) with the ``count`` aggregation,
the special ``*`` wild-card identifier often used with counts,
and ``Q`` for quantitative type.

Similarly, we can create a two-dimensional histogram using, for example, the
size of points to indicate counts within the grid (sometimes called
a "Bubble Plot"):

.. altair-plot::

   alt.Chart(cars).mark_point().encode(
       alt.X('Horsepower', bin=True),
       alt.Y('Miles_per_Gallon', bin=True),
       size='count(*):Q',
   )

There is no need, however, to limit aggregations to counts alone. For example,
we could similarly create a plot where the color of each point
represents the mean of a third quantity, such as acceleration:

.. altair-plot::

   alt.Chart(cars).mark_circle().encode(
       alt.X('Horsepower', bin=True),
       alt.Y('Miles_per_Gallon', bin=True),
       size='count(*):Q',
       color='average(Acceleration):Q'
   )

In addition to ``count`` and ``average``, there are a large number of available
aggregation functions built into Altair; they are listed in the following table:

=========  ===========================================================================  =================================
Aggregate  Description                                                                  Example
=========  ===========================================================================  =================================
argmin     An input data object containing the minimum field value.
argmax     An input data object containing the maximum field value.
average    The mean (average) field value. Identical to mean.
count      The total count of data objects in the group.
distinct   The count of distinct field values.
max        The maximum field value.
mean       The mean (average) field value.
median     The median field value
min        The minimum field value.
missing    The count of null or undefined field values.
q1         The lower quartile boundary of values.
q3         The upper quartile boundary of values.
ci0        The lower boundary of the bootstrapped 95% confidence interval of the mean.
ci1        The upper boundary of the bootstrapped 95% confidence interval of the mean.
stderr     The standard error of the field values.
stdev      The sample standard deviation of field values.
stdevp     The population standard deviation of field values.
sum        The sum of field values.
valid      The count of field values that are not null or undefined.
values     ??
variance   The sample variance of field values
variancep  The population variance of field values
=========  ===========================================================================  =================================


.. _shorthand-description:

Encoding Shorthands
~~~~~~~~~~~~~~~~~~~

For convenience, Altair allows the specification of the variable name along
with the aggregate and type within a simple shorthand string syntax.
This makes use of the type shorthand codes listed in :ref:`data-types`
as well as the aggregate names listed in :ref:`encoding-aggregates`.
The following table shows examples of the shorthand specification alongside
the long-form equivalent:

===================  =======================================================
Shorthand            Equivalent long-form
===================  =======================================================
``x='name'``         ``alt.X('name')``
``x='name:Q'``       ``alt.X('name', type='quantitative')``
``x='sum(name)'``    ``alt.X('name', aggregate='sum')``
``x='sum(name):Q'``  ``alt.X('name', aggregate='sum', type='quantitative')``
``x='sum(*):Q'``     ``alt.X(aggregate='sum', type='quantitative')``
===================  =======================================================
