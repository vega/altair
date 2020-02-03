.. currentmodule:: altair

.. _user-guide-window-transform:

Window Transform
~~~~~~~~~~~~~~~~
The window transform performs calculations over sorted groups of data objects.
These calculations include ranking, lead/lag analysis, and aggregates such as cumulative sums and averages.
Calculated values are written back to the input data stream, where they can be referenced by encodings.

For example, consider the following cumulative frequency distribution:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    alt.Chart(data.movies.url).transform_window(
        sort=[{'field': 'IMDB_Rating'}],
        frame=[None, 0],
        cumulative_count='count(*)',
    ).mark_area().encode(
        x='IMDB_Rating:Q',
        y='cumulative_count:Q',
    )

First, we pass a sort field definition, which indicates how data objects should be sorted within the window.
Here, movies should be sorted by their IMDB rating.
Next, we pass the frame, which indicates how many data objects before and after the current data object should be included within the window.
Here, all movies up to and including the current movie should be included.
Finally, we pass a window field definition, which indicates how data objects should be aggregated within the window.
Here, the number of movies should be counted.

There are many aggregation functions built into Altair.
As well as those given in :ref:`encoding-aggregates`, we can use the following within window field definitions:

============  =========  =========================================================================================================================================================================================================================================================================================================================
Aggregate     Parameter  Description
============  =========  =========================================================================================================================================================================================================================================================================================================================
row_number    None       Assigns each data object a consecutive row number, starting from 1.
rank          None       Assigns a rank order value to each data object in a window, starting from 1. Peer values are assigned the same rank. Subsequent rank scores incorporate the number of prior values. For example, if the first two values tie for rank 1, the third value is assigned rank 3.
dense_rank    None       Assigns dense rank order values to each data object in a window, starting from 1. Peer values are assigned the same rank. Subsequent rank scores do not incorporate the number of prior values. For example, if the first two values tie for rank 1, the third value is assigned rank 2.
percent_rank  None       Assigns a percentage rank order value to each data object in a window. The percent is calculated as (rank - 1) / (group_size - 1).
cume_dist     None       Assigns a cumulative distribution value between 0 and 1 to each data object in a window.
ntile         Number     Assigns a quantile (e.g., percentile) value to each data object in a window. Accepts an integer parameter indicating the number of buckets to use (e.g., 100 for percentiles, 5 for quintiles).
lag           Number     Assigns a value from the data object that precedes the current object by a specified number of positions. If no such object exists, assigns ``null``. Accepts an offset parameter (default ``1``) that indicates the number of positions. This operation must have a corresponding entry in the `fields` parameter array.
lead          Number     Assigns a value from the data object that follows the current object by a specified number of positions. If no such object exists, assigns ``null``. Accepts an offset parameter (default ``1``) that indicates the number of positions. This operation must have a corresponding entry in the `fields` parameter array.
first_value   None       Assigns a value from the first data object in the current sliding window frame. This operation must have a corresponding entry in the `fields` parameter array.
last_value    None       Assigns a value from the last data object in the current sliding window frame. This operation must have a corresponding entry in the `fields` parameter array.
nth_value     Number     Assigns a value from the nth data object in the current sliding window frame. If no such object exists, assigns ``null``. Requires a non-negative integer parameter that indicates the offset from the start of the window frame. This operation must have a corresponding entry in the `fields` parameter array.
============  =========  =========================================================================================================================================================================================================================================================================================================================

While an aggregate transform computes a single value that summarises all data objects, a window transform adds a new property to each data object.
This new property is computed from the neighbouring data objects: that is, from the data objects delimited by the window field definition.
For example, consider the following time series of stock prices:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    alt.Chart(data.stocks.url).mark_line().encode(
        x='date:T',
        y='price:Q',
        color='symbol:N',
    )

It's hard to see the overall pattern in the above example, because Google's stock price is much higher than the other stock prices.
If we plot the `z-scores`_ of the stock prices, rather than the stock prices themselves, then the overall pattern becomes clearer:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    alt.Chart(data.stocks.url).transform_window(
        mean_price='mean(price)',
        stdev_price='stdev(price)',
        frame=[None, None],
        groupby=['symbol'],
    ).transform_calculate(
        z_score=(alt.datum.price - alt.datum.mean_price) / alt.datum.stdev_price,
    ).mark_line().encode(
        x='date:T',
        y='z_score:Q',
        color='symbol:N',
    )

By using two aggregation functions (``mean`` and ``stdev``) within the window transform, we are able to compute the z-scores within the calculate transform.

For more information about the arguments to the window transform, see :class:`WindowTransform` and `the Vega-Lite documentation <https://vega.github.io/vega-lite/docs/window.html>`_.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_window` method is built on the :class:`~WindowTransform`
class, which has the following options:

.. altair-object-table:: altair.WindowTransform

.. _z-scores: https://en.wikipedia.org/w/index.php?title=Z-score
