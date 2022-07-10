.. currentmodule:: altair

.. _user-guide-aggregate-transform:

Aggregate Transforms
~~~~~~~~~~~~~~~~~~~~
There are two ways to aggregate data within Altair: within the encoding itself,
or using a top level aggregate transform.

The aggregate property of a field definition can be used to compute aggregate
summary statistics (e.g., median, min, max) over groups of data.

If at least one fields in the specified encoding channels contain aggregate,
the resulting visualization will show aggregate data. In this case, all
fields without aggregation function specified are treated as group-by fields
in the aggregation process.

For example, the following bar chart aggregates mean of ``acceleration``,
grouped by the number of Cylinders.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_bar().encode(
        y='Cylinders:O',
        x='mean(Acceleration):Q'
    )

The Altair shorthand string::

    # ...
    x='mean(Acceleration):Q',
    # ...

is made available for convenience, and is equivalent to the longer form::

    # ...
    x=alt.X(field='Acceleration', aggregate='mean', type='quantitative'),
    # ...

For more information on shorthand encodings specifications, see
:ref:`shorthand-description`.

The same plot can be shown via an explicitly computed aggregation, using the
:meth:`~Chart.transform_aggregate` method:

.. altair-plot::

    alt.Chart(cars).mark_bar().encode(
        y='Cylinders:O',
        x='mean_acc:Q'
    ).transform_aggregate(
        mean_acc='mean(Acceleration)',
        groupby=["Cylinders"]
    )

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_aggregate` method is built on the :class:`~AggregateTransform`
class, which has the following options:

.. altair-object-table:: altair.AggregateTransform

The :class:`~AggregatedFieldDef` objects have the following options:

.. altair-object-table:: altair.AggregatedFieldDef

.. _agg-func-table:

Aggregation Functions
^^^^^^^^^^^^^^^^^^^^^

In addition to ``count`` and ``average``, there are a large number of available
aggregation functions built into Altair; they are listed in the following table:

=========  ===========================================================================  =====================================
Aggregate  Description                                                                  Example
=========  ===========================================================================  =====================================
argmin     An input data object containing the minimum field value.                     N/A
argmax     An input data object containing the maximum field value.                     :ref:`gallery_line_chart_with_custom_legend`
average    The mean (average) field value. Identical to mean.                           :ref:`gallery_layer_line_color_rule`
count      The total count of data objects in the group.                                :ref:`gallery_simple_heatmap`
distinct   The count of distinct field values.                                          N/A
max        The maximum field value.                                                     :ref:`gallery_boxplot`
mean       The mean (average) field value.                                              :ref:`gallery_scatter_with_layered_histogram`
median     The median field value                                                       :ref:`gallery_boxplot`
min        The minimum field value.                                                     :ref:`gallery_boxplot`
missing    The count of null or undefined field values.                                 N/A
q1         The lower quartile boundary of values.                                       :ref:`gallery_boxplot`
q3         The upper quartile boundary of values.                                       :ref:`gallery_boxplot`
ci0        The lower boundary of the bootstrapped 95% confidence interval of the mean.  :ref:`gallery_sorted_error_bars_with_ci`
ci1        The upper boundary of the bootstrapped 95% confidence interval of the mean.  :ref:`gallery_sorted_error_bars_with_ci`
stderr     The standard error of the field values.                                      N/A
stdev      The sample standard deviation of field values.                               N/A
stdevp     The population standard deviation of field values.                           N/A
sum        The sum of field values.                                                     :ref:`gallery_streamgraph`
product    The product of field values.                                                 N/A
valid      The count of field values that are not null or undefined.                    N/A
values     ??                                                                           N/A
variance   The sample variance of field values.                                         N/A
variancep  The population variance of field values.                                     N/A
=========  ===========================================================================  =====================================
