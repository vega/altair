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
:ref:`user-guide-extent-transform`         :meth:`~Chart.transform_extent`            Find the extent of a field and store the result in a parameter.
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

Accessing Transformed Data
~~~~~~~~~~~~~~~~~~~~~~~~~~
When charts are displayed, data transformations are performed in the browser by
the Vega JavaScript library. It's often helpful to inspect transformed data
results in the process of building a chart. One approach is to display the
transformed data results in a table composed of :ref:`Text<user-guide-text-marks>`
marks as in the :ref:`gallery_scatter_linked_table` gallery example.

While this approach works, it's somewhat cumbersome, and still does not make it
possible to access the transformed data from Python. To make transformed data
results available in Python, Altair provides the :meth:`~Chart.transformed_data`
Chart method which integrates with `VegaFusion <https://vegafusion.io/>`_
to evaluate data transformations in the Python kernel.

First, install VegaFusion with the embed extras enabled.

.. code-block:: none

   pip install "vegafusion[embed]"

Then create an Altair chart and call the :meth:`~Chart.transformed_data` method
to extract a pandas DataFrame containing the transformed data.

.. altair-plot::
    :output: repr

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url
    chart = alt.Chart(cars).mark_bar().encode(
        y='Cylinders:O',
        x='mean_acc:Q'
    ).transform_aggregate(
        mean_acc='mean(Acceleration)',
        groupby=["Cylinders"]
    )
    chart.transformed_data()

The :meth:`~Chart.transformed_data` method currently supports most, but not all,
of Altair's transforms. See the table below.

=========================================  =========
Transform                                  Supported
=========================================  =========
:ref:`user-guide-aggregate-transform`        ✔
:ref:`user-guide-bin-transform`              ✔
:ref:`user-guide-calculate-transform`        ✔
:ref:`user-guide-density-transform`
:ref:`user-guide-extent-transform`           ✔
:ref:`user-guide-filter-transform`           ✔
:ref:`user-guide-flatten-transform`
:ref:`user-guide-fold-transform`             ✔
:ref:`user-guide-impute-transform`           ✔
:ref:`user-guide-joinaggregate-transform`    ✔
:ref:`user-guide-loess-transform`
:ref:`user-guide-lookup-transform`
:ref:`user-guide-pivot-transform`            ✔
:ref:`user-guide-quantile-transform`
:ref:`user-guide-regression-transform`
:ref:`user-guide-sample-transform`
:ref:`user-guide-stack-transform`            ✔
:ref:`user-guide-timeunit-transform`         ✔
:ref:`user-guide-window-transform`           ✔
=========================================  =========

.. toctree::
   :hidden:

   aggregate
   bin
   calculate
   density
   extent
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