.. currentmodule:: altair

.. _user-guide-rule-marks:

Rule
~~~~
The ``rule`` mark represents each data point as a line segment. It can be used in two ways. First, as a line segment that spans the complete width or height of a view. Second, a rule can be used to draw a line segment between two positions.

Examples
--------
Width/Height-Spanning Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If the ``rule`` mark only has ``y`` encoding, the output view produces horizontal rules that spans the complete width. Similarly, if the ``rule`` mark only has ``x`` encoding, the output view produces vertical rules that spans the height.

We can use rules to show the average price of different stocks akin to ``tick`` marks.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_rule().encode(
        y = 'mean(price):Q',
        size = alt.value(2),
        color = 'symbol:N'
    )

The fact that rule marks span the width or the height of a single view make them useful as an annotation layer. For example, we can use rules to show average values of different stocks alongside the price curve.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    base = alt.Chart(source).properties(width=550)

    line = base.mark_line().encode(
        x='date',
        y='price',
        color='symbol'
    )

    rule = base.mark_rule().encode(
        y='average(price)',
        color='symbol',
        size=alt.value(2)
    )

    line + rule

We can also use a rule mark to show global mean value over a histogram.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.movies.url

    base = alt.Chart(source)

    bar = base.mark_bar().encode(
        x=alt.X('IMDB_Rating:Q', bin=True, axis=None),
        y='count()'
    )

    rule = base.mark_rule(color='red').encode(
        x='mean(IMDB_Rating):Q',
        size=alt.value(5)
    )

    bar + rule

Ranged Rules
^^^^^^^^^^^^
To control the spans of horizontal/vertical rules, ``x`` and ``x2``/ ``y`` and ``y2`` channels can be specified.

For example, we can use ``y`` and ``y2 ``show the ``"min"`` and ``"max"`` values of horsepowers for cars from different locations.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_rule().encode(
        x = 'Origin',
        y = 'min(Horsepower)',
        y2 = 'max(Horsepower)'
    )

