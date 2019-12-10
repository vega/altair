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
        x='mean(Acceleration):Q',
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
:ref:`encoding-aggregates`.

The same plot can be shown using an explicitly computed aggregation, using the
:meth:`~Chart.transform_aggregate` method:

.. altair-plot::

    alt.Chart(cars).mark_bar().encode(
        y='Cylinders:O',
        x='mean_acc:Q'
    ).transform_aggregate(
        mean_acc='mean(Acceleration)',
        groupby=["Cylinders"]
    )

For a list of available aggregates, see :ref:`encoding-aggregates`.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_aggregate` method is built on the :class:`~AggregateTransform`
class, which has the following options:

.. altair-object-table:: altair.AggregateTransform

The :class:`~AggregatedFieldDef` objects have the following options:

.. altair-object-table:: altair.AggregatedFieldDef
