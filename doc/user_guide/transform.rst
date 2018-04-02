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
   :class:`~FieldRangePredicate`, or :class:`~FieldEqualPredicate`
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

Here is an examaple of a :class:`~FieldEqualPredicate` used to select just the
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

.. _Vega expression: https://vega.github.io/vega/docs/expressions/
