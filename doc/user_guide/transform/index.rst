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

=========================================  =========================================  ================================================================================
Transform                                  Method                                     Description
=========================================  =========================================  ================================================================================
:ref:`user-guide-aggregate-transform`      :meth:`~Chart.transform_aggregate`         Create a new data column by aggregating an existing column.
:ref:`user-guide-bin-transform`            :meth:`~Chart.transform_bin`               Create a new data column by binning an existing column.
:ref:`user-guide-calculate-transform`      :meth:`~Chart.transform_calculate`         Create a new data column using an arithmetic calculation on an existing column.
:ref:`user-guide-density-transform`        :meth:`~Chart.transform_density`           Create a new data column with the kernel density estimate of the input.
:ref:`user-guide-filter-transform`         :meth:`~Chart.transform_filter`            Select a subset of data based on a condition.
:ref:`user-guide-flatten-transform`        :meth:`~Chart.transform_flatten`           Flatten array data into columns.
:ref:`user-guide-fold-transform`           :meth:`~Chart.transform_fold`              Convert wide-form data into long-form data (opposite of pivot).
:ref:`user-guide-impute-transform`         :meth:`~Chart.transform_impute`            Impute missing data.
:ref:`user-guide-joinaggregate-transform`  :meth:`~Chart.transform_joinaggregate`     Aggregate transform joined to original data.
:ref:`user-guide-loess-transform`          :meth:`~Chart.transform_loess`             Create a new column with LOESS smoothing of data.
:ref:`user-guide-lookup-transform`         :meth:`~Chart.transform_lookup`            One-sided join of two datasets based on a lookup key.
:ref:`user-guide-pivot-transform`          :meth:`~Chart.transform_pivot`             Convert long-form data into wide-form data (opposite of fold).
:ref:`user-guide-quantile-transform`       :meth:`~Chart.transform_quantile`          Compute empirical quantiles of a dataset.
:ref:`user-guide-regression-transform`     :meth:`~Chart.transform_regression`        Fit a regression model to a dataset.
:ref:`user-guide-sample-transform`         :meth:`~Chart.transform_sample`            Random sub-sample of the rows in the dataset.
:ref:`user-guide-stack-transform`          :meth:`~Chart.transform_stack`             Compute stacked version of values.
:ref:`user-guide-timeunit-transform`       :meth:`~Chart.transform_timeunit`          Discretize/group a date by a time unit (day, month, year, etc.)
:ref:`user-guide-window-transform`         :meth:`~Chart.transform_window`            Compute a windowed aggregation
=========================================  =========================================  ================================================================================


.. toctree::
   :hidden:

   aggregate
   bin
   calculate
   density
   filter
   flatten
   fold
   impute
   joinaggregate
   lookup
   loess
   pivot
   quantile
   regression
   sample
   stack
   timeunit
   window