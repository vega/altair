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
:meth:`~Chart.transform_aggregate`         Create a new data column by aggregating an existing column.
:meth:`~Chart.transform_bin`               Create a new data column by binning an existing column.
:meth:`~Chart.transform_calculate`         Create a new data column using an arithmetic calculation on an existing column.
:meth:`~Chart.transform_filter`            Select a subset of data based on a condition.
:meth:`~Chart.transform_lookup`            One-sided join of two datasets based on a lookup key.
:meth:`~Chart.transform_timeunit`          Discretize/group a date by a time unit (day, month, year, etc.)
:meth:`~Chart.transform_window`            Compute a windowed aggregation
=========================================  ================================================================================

We will see some examples of these transforms in the following sections.

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
    y='mean(acceleration):Q',
    # ...

is made available for convenience, and is equivalent to the longer form::

    # ...
    y=alt.Y(field='acceleration', aggregate='mean', type='quantitative'),
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

.. _user-guide-bin-transform:

Bin transforms
~~~~~~~~~~~~~~
As with :ref:`user-guide-aggregate-transform`, there are two ways to apply
a bin transform in Altair: within the encoding itself, or using a top-level
bin transform.

An common application of a bin transform is when creating a histogram:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    movies = data.movies.url

    alt.Chart(movies).mark_bar().encode(
        alt.X("IMDB_Rating:Q", bin=True),
        y='count()',
    )

But a bin transform can be useful in other applications; for example, here we
bin a continuous field to create a discrete color map:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.Color('Acceleration:Q', bin=alt.Bin(maxbins=5))
    )

In the first case we set ``bin = True``, which uses the default bin settings.
In the second case, we exercise more fine-tuned control over the bin parameters
by passing a :class:`~altair.Bin` object.

If you are using the same binnings in multiple chart components, it can be useful
to instead define the binning at the top level, using :meth:`~Chart.transform_bin`
method.

Here is the above histogram created using a top-level bin transform:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    movies = data.movies.url

    alt.Chart(movies).mark_bar().encode(
        x='binned_rating:O',
        y='count()',
    ).transform_bin(
        'binned_rating', field='IMDB_Rating'
    )

And here is the transformed color scale using a top-level bin transform:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='binned_acc:O'
    ).transform_bin(
        'binned_acc', 'Acceleration', bin=alt.Bin(maxbins=5)
    )

The advantage of the top-level transform is that the same named field can be
used in multiple places in the chart if desired.
Note the slight difference in binning behavior between the encoding-based binnings
(which preserve the range of the bins) and the transform-based binnings (which
collapse each bin to a single representative value.

.. _user-guide-calculate-transform:

Calculate Transform
~~~~~~~~~~~~~~~~~~~
The calculate transform allows the user to define new fields in the dataset
which are calculated from other fields using an expression syntax.

As a simple example, here we take data with a simple input sequence, and compute
a some trigonometric quantities:

.. altair-plot::

    import altair as alt
    import pandas as pd

    data = pd.DataFrame({'t': range(101)})

    alt.Chart(data).mark_line().encode(
        x='x:Q',
        y='y:Q',
        order='t:Q'
    ).transform_calculate(
        x='cos(datum.t * PI / 50)',
        y='sin(datum.t * PI / 25)'
    )

Each argument within ``transform_calculate`` is a `Vega expression`_ string,
which is a well-defined set of javascript-style operations that can be used
to calculate a new field from an existing one.

To streamline building these vega expressions in Python, Altair provides the
:mod:`altair.expr` module which provides constants and functions to allow
these expressions to be constructed with Python syntax; for example:

.. altair-plot::

    from altair import expr, datum

    alt.Chart(data).mark_line().encode(
        x='x:Q',
        y='y:Q',
        order='t:Q'
    ).transform_calculate(
        x=expr.cos(datum.t * expr.PI / 50),
        y=expr.sin(datum.t * expr.PI / 25)
    )

Altair expressions are designed to output valid Vega expressions. The benefit of
using them is that proper syntax is ensured by the Python interpreter, and tab
completion of the :mod:`~expr` submodule can be used to explore the
available functions and constants.

These expressions can also be used when constructing a
:ref:`user-guide-filter-transform`, as we shall see next.

.. _user-guide-filter-transform:

Filter Transform
~~~~~~~~~~~~~~~~
The filter transform removes objects from a data stream based on a provided
filter expression, selection, or other filter predicate. A filter can be
added at the top level of a chart using the :meth:`Chart.transform_filter`
method. The argument to ``transform_filter`` can be one of a number of
expressions and objects:

1. A `Vega expression`_ expressed as a string or built using the :mod:`~expr` module
2. A Field predicate, such as :class:`~FieldOneOfPredicate`,
   :class:`~FieldRangePredicate`, :class:`~FieldEqualPredicate`,
   :class:`~FieldLTPredicate`, :class:`~FieldGTPredicate`,
   :class:`~FieldLTEPredicate`, :class:`~FieldGTEPredicate`,
3. A Selection predicate or object created by :func:`selection`
4. A Logical operand that combines any of the above

We'll show a brief example of each of these in the following sections

Filter Expression
^^^^^^^^^^^^^^^^^
A filter expression uses the `Vega expression`_ language, either specified
directly as a string, or built using the :mod:`~expr` module.
This can be useful when, for example, selecting only a subset of data.

For example:

.. altair-plot::

    import altair as alt
    from altair import datum

    from vega_datasets import data
    pop = data.population.url

    alt.Chart(pop).mark_area().encode(
        x='age:O',
        y='people:Q',
    ).transform_filter(
        (datum.year == 2000) & (datum.sex == 1)
    )

Notice that, like in the :ref:`user-guide-filter-transform`, data values are
referenced via the name ``datum``.

Field Predicates
^^^^^^^^^^^^^^^^
Field predicates overlap somewhat in function with expression predicates, but
have the advantage that their contents are validated by the schema. Examples
are:

- :class:`~FieldEqualPredicate` evaluates whether a field is equal to
  a particular value
- :class:`~FieldOneOfPredicate` evaluates whether a field is among a list of
  specified values.
- :class:`~FieldRangePredicate` evaluates whether a continuous field is within
  a range of values.
- :class:`~FieldLTPredicate` evaluates whether a continuous field is less
  than a given value
- :class:`~FieldGTPredicate` evaluates whether a continuous field is greater
  than a given value
- :class:`~FieldLTEPredicate` evaluates whether a continuous field is less
  than or equal to a given value
- :class:`~FieldGTEPredicate` evaluates whether a continuous field is greater
  than or equal to a given value

Here is an example of a :class:`~FieldEqualPredicate` used to select just the
values from year 2000 as in the above chart:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    pop = data.population.url

    alt.Chart(pop).mark_line().encode(
        x='age:O',
        y='sum(people):Q',
        color='year:O'
    ).transform_filter(
        alt.FieldEqualPredicate(field='year', equal=2000)
    )

A :class:`~FieldOneOfPredicate` is similar, but allows selection of any number
of specific values:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    pop = data.population.url

    alt.Chart(pop).mark_line().encode(
        x='age:O',
        y='sum(people):Q',
        color='year:O'
    ).transform_filter(
        alt.FieldOneOfPredicate(field='year', oneOf=[1900, 1950, 2000])
    )

Finally, a :meth:`~FieldRangePredicate` allows selecting values within a
particular continuous range:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    pop = data.population.url

    alt.Chart(pop).mark_line().encode(
        x='age:O',
        y='sum(people):Q',
        color='year:O'
    ).transform_filter(
        alt.FieldRangePredicate(field='year', range=[1960, 2000])
    )

Selection Predicates
^^^^^^^^^^^^^^^^^^^^
Selection predicates can be used to filter data based on a selection. While
these can be constructed directly using a :class:`~SelectionPredicate` class,
in Altair it is often more convenient to construct them using the
:func:`~selection` function. For example, this chart uses a multi-selection
that allows the user to click or shift-click on the bars in the bottom chart
to select the data to be shown in the top chart:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    pop = data.population.url

    selection = alt.selection_multi(fields=['year'])

    top = alt.Chart().mark_line().encode(
        x='age:O',
        y='sum(people):Q',
        color='year:O'
    ).properties(
        width=600, height=200
    ).transform_filter(
        selection
    )

    bottom = alt.Chart().mark_bar().encode(
        x='year:O',
        y='sum(people):Q',
        color=alt.condition(selection, alt.value('steelblue'), alt.value('lightgray'))
    ).properties(
        width=600, height=100,
        selection=selection
    )

    alt.vconcat(
        top, bottom,
        data=pop
    )

Logical Operands
^^^^^^^^^^^^^^^^
At times it is useful to combine several types of predicates into a single
selection. This can be accomplished using the various logical operand classes:

- :class:`~LogicalOrPredicate`
- :class:`~LogicalAndPredicate`
- :class:`~LogicalNotPredicate`

These are not yet part of the Altair interface
(see `Issue 693 <https://github.com/altair-viz/altair/pull/693>`_)
but can be constructed explicitly; for example, here we plot US population
distributions for all data *except* the years 1950-1960,
by applying a ``LogicalNotPredicate`` schema to a ``FieldRangePredicate``:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    pop = data.population.url

    alt.Chart(pop).mark_line().encode(
        x='age:O',
        y='sum(people):Q',
        color='year:O'
    ).properties(
        width=600, height=200
    ).transform_filter(
        {'not': alt.FieldRangePredicate(field='year', range=[1900, 1950])}
    )


.. _user-guide-lookup-transform:

Lookup Transform
~~~~~~~~~~~~~~~~
The lookup transform extends a primary data source by looking up values from
another data source; it is similar to a one-sided join. A lookup can be added
at the top level of a chart using the :meth:`Chart.transform_lookup` method.

By way of example, imagine you have two sources of data that you would like
to combine and plot: one is a list of names of people along with their height
and weight, and the other is some information about which groups they belong
to. This example data is available in ``vega_datasets``:

.. altair-plot::
   :output: none

   from vega_datasets import data
   people = data.lookup_people()
   groups = data.lookup_groups()

We know how to visualize each of these datasets separately; for example:

.. altair-plot::

    top = alt.Chart(people).mark_square(size=200).encode(
        x=alt.X('age:Q', scale=alt.Scale(zero=False)),
        y=alt.Y('height:Q', scale=alt.Scale(zero=False)),
        color='name:N',
        tooltip='name:N'
    ).properties(
        width=400, height=200
    )

    bottom = alt.Chart(groups).mark_rect().encode(
        x='person:N',
        y='group:O'
    ).properties(
        width=400, height=100
    )

    alt.vconcat(top, bottom)

If we would like to plot features that reference both datasets (for example, the
average age within each group), we need to combine the two datasets.
This can be done either as a data preprocessing step, using tools available
in Pandas, or as part of the visualization using a :class:`~LookupTransform`
in Altair.

Combining Datasets with pandas.merge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pandas provides a wide range of tools for merging and joining datasets; see
`Merge, Join, and Concatenate <https://pandas.pydata.org/pandas-docs/stable/merging.html>`_
for some detailed examples.
For the above data, we can merge the data and create a combined chart as follows:

.. altair-plot::

    import pandas as pd
    merged = pd.merge(groups, people, how='left',
                      left_on='person', right_on='name')

    alt.Chart(merged).mark_bar().encode(
        x='mean(age):Q',
        y='group:O'
    )

We specify a left join, meaning that for each entry of the "person" column in
the groups, we seek the "name" column in people and add the entry to the data.
From this, we can easily create a bar chart representing the mean age in each group.

Combining Datasets with a Lookup Transform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For some data sources (e.g. data available at a URL, or data that is streaming),
it is desirable to have a means of joining data without having to download
it for pre-processing in Pandas.
This is where Altair's :meth:`~Chart.transform_lookup` comes in.
To reproduce the above combined plot by combining datasets within the
chart specification itself, we can do the following:

.. altair-plot::

    alt.Chart(groups).mark_bar().encode(
        x='mean(age):Q',
        y='group:O'
    ).transform_lookup(
        lookup='person',
        from_=alt.LookupData(data=people, key='name',
                             fields=['age', 'height'])
    )

Here ``lookup`` names the field in the groups dataset on which we will match,
and the ``from_`` argument specifies a :class:`~LookupData` structure where
we supply the second dataset, the lookup key, and the fields we would like to
extract.

Example: Lookup Transforms for Geographical Visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Lookup transforms are often particularly important for geographic visualization,
where it is common to combine tabular datasets with datasets that specify
geographic boundaries to be visualized; for example, here is a visualization
of unemployment rates per county in the US:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    counties = alt.topo_feature(data.us_10m.url, 'counties')
    unemp_data = data.unemployment.url

    alt.Chart(counties).mark_geoshape().encode(
        color='rate:Q'
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(unemp_data, 'id', ['rate'])
    ).properties(
        projection={'type': 'albersUsa'},
        width=500, height=300
    )


.. _user-guide-timeunit-transform:

TimeUnit Transform
~~~~~~~~~~~~~~~~~~
TimeUnit transforms are used to discretize dates and times within Altair.
As with the :ref:`user-guide-aggregate-transform` and :ref:`user-guide-bin-transform`
discussed above, they can be defined either as part of the encoding, or as a
top-level transform.

These are the available time units:

- ``"year"``, ``"yearquarter"``, ``"yearquartermonth"``, ``"yearmonth"``,
  ``"yearmonthdate"``, ``"yearmonthdatehours"``, ``"yearmonthdatehoursminutes"``,
  ``"yearmonthdatehoursseconds"``.
- ``"quarter"``, ``"quartermonth"``
- ``"month"``, ``"monthdate"``
- ``"date"`` (Day of month, i.e., 1 - 31)
- ``"day"`` (Day of week, i.e., Monday - Friday)
- ``"hours"``, ``"hoursminutes"``, ``"hoursminutesseconds"``
- ``"minutes"``, ``"minutesseconds"``
- ``"seconds"``, ``"secondsmilliseconds"``
- ``"milliseconds"``

TimeUnit Within Encoding
^^^^^^^^^^^^^^^^^^^^^^^^
Any temporal field definition can include a ``timeUnit`` argument to discretize
the temporal data.

For example, here we plot a dataset that consists of hourly temperature
measurements in Seattle during the year 2010:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    temps = data.seattle_temps.url

    alt.Chart(temps).mark_line().encode(
        x='date:T',
        y='temp:Q'
    )

The plot is too busy due to the amount of data points squeezed into the short
time; we can make it a bit cleaner by discretizing it, for example, by month
and plotting only the mean monthly temperature:

.. altair-plot::

    alt.Chart(temps).mark_line().encode(
        x='month(date):T',
        y='mean(temp):Q'
    )

Notice that by default timeUnit output is a continuous quantity; if you would
instead like it to be a categorical, you can specify the ordinal (``O``) or
nominal (``N``) type.
This can be useful when plotting a bar chart or other discrete chart type:

.. altair-plot::

    alt.Chart(temps).mark_bar().encode(
        x='month(date):O',
        y='mean(temp):Q'
    )

Multiple time units can be combined within a single plot to yield interesting
views of your data; for example, here we extract both the month and the day
to give a profile of Seattle temperatures through the year:

.. altair-plot::

    alt.Chart(temps).mark_rect().encode(
        alt.X('date(date):O', title='day'),
        alt.Y('month(date):O', title='month'),
        color='max(temp):Q'
    ).properties(
        title="2010 Daily High Temperatures in Seattle (F)"
    )

TimeUnit as a Transform
^^^^^^^^^^^^^^^^^^^^^^^
Other times it is convenient to specify a timeUnit as a top-level transform,
particularly when the value may be reused.
This can be done most conveniently using the :meth:`Chart.transform_timeunit`
method. For example:

.. altair-plot::

    alt.Chart(temps).mark_line().encode(
        alt.X('month:T', axis=alt.Axis(format='%b')),
        y='mean(temp):Q'
    ).transform_timeunit(
        month='month(date)'
    )

Notice that because the ``timeUnit`` is not part of the encoding channel here,
it is often necessary to add an axis formatter to ensure appropriate axis
labels.


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
    ).mark_area().encode(x='IMDB_Rating:Q', y='cumulative_count:Q')

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

For more information about the arguments to the window transform, see :class:`WindowTransform` and `the Vega-Lite documentation <https://vega.github.io/vega-lite/docs/window.html>`_.

.. _Vega expression: https://vega.github.io/vega/docs/expressions/
