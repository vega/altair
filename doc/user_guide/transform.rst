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

This second approach -- specifying data transformations within the chart itself
-- can be accomplished using the ``transform_*`` methods of top-level objects:

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
