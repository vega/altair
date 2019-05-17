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
:ref:`user-guide-filter-transform`         :meth:`~Chart.transform_filter`            Select a subset of data based on a condition.
:ref:`user-guide-flatten-transform`        :meth:`~Chart.transform_flatten`           Flatten array data into columns.
:ref:`user-guide-fold-transform`           :meth:`~Chart.transform_fold`              Convert wide-form data into long-form data.
:ref:`user-guide-impute-transform`         :meth:`~Chart.transform_impute`            Impute missing data.
:ref:`user-guide-joinaggregate-transform`  :meth:`~Chart.transform_joinaggregate`     Aggregate transform joined to original data.
:ref:`user-guide-lookup-transform`         :meth:`~Chart.transform_lookup`            One-sided join of two datasets based on a lookup key.
:ref:`user-guide-sample-transform`         :meth:`~Chart.transform_sample`            Random sub-sample of the rows in the dataset.
:ref:`user-guide-stack-transform`          :meth:`~Chart.transform_stack`             Compute stacked version of values.
:ref:`user-guide-timeunit-transform`       :meth:`~Chart.transform_timeunit`          Discretize/group a date by a time unit (day, month, year, etc.)
:ref:`user-guide-window-transform`         :meth:`~Chart.transform_window`            Compute a windowed aggregation
=========================================  =========================================  ================================================================================

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

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_aggregate` method is built on the :class:`~AggregateTransform`
class, which has the following options:

.. altair-object-table:: altair.AggregateTransform

The :class:`~AggregatedFieldDef` objects have the following options:

.. altair-object-table:: altair.AggregatedFieldDef

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

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_bin` method is built on the :class:`~BinTransform`
class, which has the following options:

.. altair-object-table:: altair.BinTransform

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

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_calculate` method is built on the :class:`~CalculateTransform`
class, which has the following options:

.. altair-object-table:: altair.CalculateTransform

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
        width=600, height=100
    ).add_selection(
        selection
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
(see `Issue 695 <https://github.com/altair-viz/altair/issues/695>`_)
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

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_filter` method is built on the :class:`~FilterTransform`
class, which has the following options:

.. altair-object-table:: altair.FilterTransform

.. _user-guide-flatten-transform:

Flatten Transform
~~~~~~~~~~~~~~~~~
The flatten transform can be used to extract the contents of arrays from data entries.
This will not generally be useful for well-structured data within pandas dataframes,
but it can be useful for working with data from other sources.

As an example, consider this dataset which uses a common convention in JSON data,
a set of fields each containing a list of entries:

.. altair-plot::
   :output: none

   import numpy as np

   rand = np.random.RandomState(0)

   def generate_data(N):
       mean = rand.randn()
       std = rand.rand()
       return list(rand.normal(mean, std, N))

   data = [
       {'label': 'A', 'values': generate_data(20)},
       {'label': 'B', 'values': generate_data(30)},
       {'label': 'C', 'values': generate_data(40)},
       {'label': 'D', 'values': generate_data(50)},   
   ]

This kind of data structure does not work well in the context of dataframe
representations, as we can see by loading this into pandas:

.. altair-plot::
   :output: repr

   import pandas as pd
   df = pd.DataFrame.from_records(data)
   df

Alair's flatten transform allows you to extract the contents of these arrays
into a column that can be referenced by an encoding:

.. altair-plot::

   alt.Chart(df).transform_flatten(
       ['values']
   ).mark_tick().encode(
       x='values:Q',
       y='label:N',
   )

This can be particularly useful in cleaning up data specified via a JSON URL,
without having to first load the data for manipulation in pandas.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_flatten` method is built on the :class:`~FlattenTransform`
class, which has the following options:

.. altair-object-table:: altair.FlattenTransform

.. _user-guide-fold-transform:

Fold Transform
~~~~~~~~~~~~~~
The fold transform is, in short, a way to convert wide-form data to long-form
data directly without any preprocessing (see :ref:`data-long-vs-wide` for more
information).

So, for example, if your data consist of multiple columns that record parallel
data for different categories, you can use the fold transform to encode based
on those categories:

.. altair-plot::

   import numpy as np
   import pandas as pd
   import altair as alt

   rand = np.random.RandomState(0)
   data = pd.DataFrame({
       'date': pd.date_range('2019-01-01', freq='D', periods=30),
       'A': rand.randn(30).cumsum(),
       'B': rand.randn(30).cumsum(),
       'C': rand.randn(30).cumsum(),
   })

   alt.Chart(data).transform_fold(
       ['A', 'B', 'C'],
   ).mark_line().encode(
       x='date:T',
       y='value:Q',
       color='key:N'
   )

Notice here that the fold transform essentially stacks all the values
from the specified columns into a single new field named ``"value"``,
with the associated names in a field named ``"key"``.

For an example of the fold transform in action, see :ref:`gallery_parallel_coordinates`.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_fold` method is built on the :class:`~FoldTransform`
class, which has the following options:

.. altair-object-table:: altair.FoldTransform

.. _user-guide-impute-transform:

Impute Transform
~~~~~~~~~~~~~~~~
The impute transform allows you to fill-in missing entries in a dataset.
As an example, consider the following data, which includes missing values
that we filter-out of the long-form representation (see :ref:`data-long-vs-wide`
for more on this):

.. altair-plot::
   :output: repr

   import numpy as np
   import pandas as pd

   data = pd.DataFrame({
       't': range(5),
       'x': [2, np.nan, 3, 1, 3],
       'y': [5, 7, 5, np.nan, 4]
   }).melt('t').dropna()
   data

Notice the result: the ``x`` series has no entry at ``t=1``, and the ``y``
series has a missing entry at ``t=3``. If we use Altair to visualize this
data directly, the line skips the missing entries:

.. altair-plot::

   raw = alt.Chart(data).mark_line(point=True).encode(
       x=alt.X('t:Q'),
       y='value:Q',
       color='variable:N'
   )
   raw

This is not always desireable, because (particularly for a line plot with
no points) it can imply the esistence of data that is not there.

Impute via Encodings
^^^^^^^^^^^^^^^^^^^^
To address this, you can use an impute argument to the encoding channel.
For example, we can impute using a constant value (we'll show the raw chart
lightly in the background for reference):

.. altair-plot::

   background = raw.encode(opacity=alt.value(0.2))
   chart = alt.Chart(data).mark_line(point=True).encode(
       x='t:Q',
       y=alt.Y('value:Q', impute=alt.ImputeParams(value=0)),
       color='variable:N'
   )
   background + chart

Or we can impute using any supported aggregate:

.. altair-plot::

   chart = alt.Chart(data).mark_line(point=True).encode(
       x='t:Q',
       y=alt.Y('value:Q', impute=alt.ImputeParams(method='mean')),
       color='variable:N'
   )
   background + chart

Impute via Transform
^^^^^^^^^^^^^^^^^^^^
Similar to the :ref:`user-guide-bin-transform` and :ref:`user-guide-aggregate-transform`,
it is also possible to specify the impute transform outside the encoding as a
transform. For example, here is the equivalent of the above two charts:

.. altair-plot::

   chart = alt.Chart(data).transform_impute(
       impute='value',
       key='t',
       value=0,
       groupby=['variable']
   ).mark_line(point=True).encode(
       x='t:Q',
       y='value:Q',
       color='variable:N'
   )
   background + chart

.. altair-plot::

   chart = alt.Chart(data).transform_impute(
       impute='value',
       key='t',
       method='mean',
       groupby=['variable']
   ).mark_line(point=True).encode(
       x='t:Q',
       y='value:Q',
       color='variable:N'
   )
   background + chart

If you would like to use more localized imputed values, you can specify a
``frame`` parameter similar to the :ref:`user-guide-window-transform` that
will control which values are used for the imputation. For example, here
we impute missing values using the mean of the neighboring points on either
side:

.. altair-plot::

   chart = alt.Chart(data).transform_impute(
       impute='value',
       key='t',
       method='mean',
       frame=[-1, 1],
       groupby=['variable']
   ).mark_line(point=True).encode(
       x='t:Q',
       y='value:Q',
       color='variable:N'
   )
   background + chart

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_impute` method is built on the :class:`~ImputeTransform`
class, which has the following options:

.. altair-object-table:: altair.ImputeTransform

.. _user-guide-joinaggregate-transform:

Join Aggregate Transform
~~~~~~~~~~~~~~~~~~~~~~~~
The Join Aggregate transform acts in almost every way the same as an Aggregate
transform, but the resulting aggregate is joined to the original dataset.
To make this more clear, consider the following dataset:

.. altair-plot::
   :output: repr

   import pandas as pd
   import numpy as np

   rand = np.random.RandomState(0)

   df = pd.DataFrame({
       'label': rand.choice(['A', 'B', 'C'], 10),
       'value': rand.randn(10),
   })
   df

Here is a pandas operation that is equivalent to Altair's Aggregate transform,
using the mean as an example:

.. altair-plot::
   :output: repr

   mean = df.groupby('label').mean().reset_index()
   mean

And here is an output that is equivalent to Altair's Join Aggregate:

.. altair-plot::
   :output: repr

   pd.merge(df, mean, on='label', suffixes=['', '_mean'])
   
Notice that the join aggregate joins the aggregated value with the original
dataframe, such that the aggregated values can be used in tandem with the
original values if desired.

Here is an example of how the join aggregate might be used: we compare the
IMDB and Rotten Tomatoes movie ratings, normalized by their mean and
standard deviation, which requires calculations on the joined data:

.. altair-plot::

   import altair as alt
   from vega_datasets import data

   alt.Chart(data.movies.url).transform_filter(
       'datum.IMDB_Rating != null  && datum.Rotten_Tomatoes_Rating != null'  
   ).transform_joinaggregate(
       IMDB_mean='mean(IMDB_Rating)',
       IMDB_std='stdev(IMDB_Rating)',
       RT_mean='mean(Rotten_Tomatoes_Rating)',
       RT_std='stdev(Rotten_Tomatoes_Rating)'
   ).transform_calculate(
       IMDB_Deviation="(datum.IMDB_Rating - datum.IMDB_mean) / datum.IMDB_std",
       Rotten_Tomatoes_Deviation="(datum.Rotten_Tomatoes_Rating - datum.RT_mean) / datum.RT_std"
   ).mark_point().encode(
       x='IMDB_Deviation:Q',
       y="Rotten_Tomatoes_Deviation:Q"
   )

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_joinaggregate` method is built on the
:class:`~JoinAggregateTransform` class, which has the following options:

.. altair-object-table:: altair.JoinAggregateTransform

.. _user-guide-lookup-transform:

Lookup Transform
~~~~~~~~~~~~~~~~
The Lookup transform extends a primary data source by looking up values from
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

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_lookup` method is built on the :class:`~LookupTransform`
class, which has the following options:

.. altair-object-table:: altair.LookupTransform

.. _user-guide-sample-transform:

Sample Transform
~~~~~~~~~~~~~~~~
The sample transform is one of the simpler of all Altair's data transforms;
it takes a single parameter ``sample`` which specified a number of rows to
randomly choose from the dataset. The resulting chart will be created using
only this random subset of the data.

For example, here we chart the full cars dataset alongside a sample of 100
rows:

.. altair-plot::

   import altair as alt
   from vega_datasets import data

   source = data.cars.url

   chart = alt.Chart(source).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
       color='Origin:N'
   ).properties(
       width=200,
       height=200
   )

   chart | chart.transform_sample(100)


Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_sample` method is built on the :class:`~SampleTransform`
class, which has the following options:

.. altair-object-table:: altair.SampleTransform

.. _user-guide-stack-transform:

Stack Transform
~~~~~~~~~~~~~~~
The stack transform allows you to compute values associated with stacked versions
of encodings. For example, consider this stacked bar chart:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).mark_bar().encode(
        column='year:O',
        x='yield:Q',
        y='variety:N',
        color='site:N'
    ).properties(width=220)

Implicitly, this data is being grouped and stacked, but what if you would like to
access those stacked values directly?
We can construct that same chart manually using the stack transform:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).transform_stack(
        stack='yield',
        as_=['yield_1', 'yield_2'],
        groupby=['year', 'variety'],
        sort=[alt.SortField('site', 'descending')]
    ).mark_bar().encode(
        column='year:O',
        x=alt.X('yield_1:Q', title='yield'),
        x2='yield_2:Q',
        y='variety:N',
        color='site:N',
        tooltip=['site', 'yield', 'variety']
    ).properties(width=220)

Notice that the bars are now explicitly drawn between values computed and
specified within the x and x2 encodings.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_stack` method is built on the :class:`~StackTransform`
class, which has the following options:

.. altair-object-table:: altair.StackTransform

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

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_timeunit` method is built on the :class:`~TimeUnitTransform`
class, which has the following options:

.. altair-object-table:: altair.TimeUnitTransform


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

.. _Vega expression: https://vega.github.io/vega/docs/expressions/
.. _z-scores: https://en.wikipedia.org/w/index.php?title=Z-score
