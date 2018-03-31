.. currentmodule:: altair

.. _user-guide-transformations:

Data Transformations
--------------------
It is often necessary to transform or filter data in the process of visualizing
it. In Altair you can do this one of two ways:

1. Before the chart definition, using standard Pandas data transformations.
2. Within the chart definition, using Vega-Lite's data transformation tools.

In most cases, we suggest that you use the first approach, because it is more
straightforward to those who are familiar with data manipulation in Python, and
because the Pandas package offers much more flexibility than Vega-Lite in
available data manipulations.

The second approach becomes useful when the data source is not a dataframe, but,
for example, a URL pointer to a JSON or CSV file. It can also be useful in a
compound chart where different views of the dataset require different
transformations.

This second approach -- specifying data transformations within the chart
specification itself -- can be accomplished using the ``transform_*``
methods of top-level objects:

=========================================  ================================================================================
Method                                     Description
=========================================  ================================================================================
:meth:`~Chart.transform`                   Generic transform; passes keywords to any of the following methods.
:meth:`~Chart.transform_aggregate`         Create a new data column by aggregating an existing column.
:meth:`~Chart.transform_bin`               Create a new data column by binning an existing column.
:meth:`~Chart.transform_calculate`         Create a new data column using an arithmetic calculation on an existing column.
:meth:`~Chart.transform_filter`            Select a subset of data based on a condition.
:meth:`~Chart.transform_lookup`            One-sided join of two datasets based on a lookup key.
:meth:`~Chart.transform_timeunit`          Discretize/group a date by a time unit (day, month, year, etc.)
=========================================  ================================================================================

We will see some examples of these transforms in the following sections.

.. _user-guide-aggregate-transform

Aggregate Transforms
~~~~~~~~~~~~~~~~~~~~
There are two ways to aggregate data within Altair: within the encoding itself,
or within an aggregate transform.

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

    ...
    y='mean(acceleration):Q',
    ...

is made available for convenience, and is equivalent to the longer form::

    ...
    y=alt.Y(field='acceleration', aggregate='mean', type='quantitative')
    ...

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

.. _user-guide-expressions:

Altair Expressions
~~~~~~~~~~~~~~~~~~
Transformation expressions in Vega-Lite are specified as strings of javascript
code, with a well-defined set of functions and constants available
(see Vega's `Expression Documentation <https://github.com/vega/vega/wiki/Expressions>`_).
For convenience when when working from Python, Altair provides an API
in the :mod:`altair.expr` module to allow users to build these expressions
more idiomatically within Python.

So, for example, if you want to perform the following data filtration:

.. code-block:: python

   chart.transform_filter("datum.y < sin(datum.t + PI)")

You can instead write the following:

.. code-block:: python

   from altair.expr import datum, sin, PI
   chart.transform_filter(datum.y < sin(datum.t) + PI)

This approach has the benefit that syntax errors in the formula will be caught
in Python rather than in the chart renderer; you can also use Jupyter
tab-completion on the :mod:`expr` module to see what functions and constants
are available.

*TODO: section detailing each type of transform*
