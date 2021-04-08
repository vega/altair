.. currentmodule:: altair

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
distributions for all data *except* the years 1900-1950,
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

.. _Vega expression: https://vega.github.io/vega/docs/expressions/
