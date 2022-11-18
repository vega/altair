.. currentmodule:: altair

.. _user-guide-bar-marks:

Bar
~~~

Bar marks are useful in many visualizations, including bar charts, stacked bar charts, and timelines.

Bar Mark Properties
-------------------
A ``bar`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: width height orient align baseline binSpacing cornerRadius cornerRadiusEnd cornerRadiusTopLeft cornerRadiusTopRight cornerRadiusBottomRight cornerRadiusBottomLeft

Examples
--------

Single Bar Chart
^^^^^^^^^^^^^^^^
Mapping a quantitative field to either ``x`` or ``y`` of the ``bar`` mark produces a single bar chart.

.. altair-plot::
    import altair as alt
    from altair import datum
    from vega_datasets import data

    source = data.population.url

    alt.Chart(source).mark_bar().encode(
        alt.X('sum(people):Q', title = "Population")
    ).transform_filter(
        datum.year == 2000
    )

Bar Chart
^^^^^^^^^
If we map a different discrete field to the ``y`` channel, we can produce a horizontal bar chart. Specifying ``alt.Step(20)`` will adjust the bar's height per discrete step.

.. altair-plot::
    import altair as alt
    from altair import datum
    from vega_datasets import data

    source = data.population.url

    alt.Chart(source).mark_bar().encode(
        alt.X("sum(people):Q", title="Population"), alt.Y("age:O")
    ).transform_filter(datum.year == 2000).properties(height=alt.Step(20))


Bar Chart with a Temporal Axis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While the ``bar`` mark typically uses the ``x`` and ``y`` channels to encode
a pair of discrete and continuous fields, it can also be used with continuous
fields on both channels. For example, given a bar chart with a temporal field
on ``x``, we can see that the x-scale is a continuous scale. By default, the size of
bars on continuous scales will be set based on the ``continuousBandSize`` config.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_bar().encode(
        alt.X('month(date):T', title = 'Date'),
        alt.Y('mean(precipitation):Q'),
    )

Histograms
^^^^^^^^^^

If the data is not pre-aggregated (i.e. each record in the data field represents one item), mapping a binned quantitative field to ``x`` and aggregate ``count`` to ``y`` produces a histogram.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.movies.url

    alt.Chart(source).mark_bar().encode(
        alt.X("IMDB_Rating:Q", bin=True),
        y='count()',
    )

Stacked Bar Chart
^^^^^^^^^^^^^^^^^
Adding color to the bar chart (by using the ``color`` attribute) creates a stacked bar chart by default. Here we also customize the color’s scale range to make the color a little nicer. (See ``stack`` for more details about customizing stack.)

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).mark_bar().encode(
        x='variety',
        y='sum(yield)',
        color='site'
    )

Grouped Bar Chart with Offset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({
        'category': ['A', 'A', 'B','B', "C", "C"],
        'group': ['x', 'y', 'z', 'x', 'y', 'z'],
        'value': [0.1, 0.6, 0.9, 0.7, 0.2, 0.6]
    })

    alt.Chart(source).mark_bar().encode(
        x = alt.X('category:N'),
        xOffset = 'group:N',
        y = alt.Y('value:Q'),
        color = alt.Color('group:N')
    )

