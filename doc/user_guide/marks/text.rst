.. currentmodule:: altair

.. _user-guide-text-marks:

Text
~~~~~~
``text`` mark represents each data point with a text instead of a point.

Text Mark Properties
--------------------
A ``text`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: angle align baseline dir dx dy ellipsis font fontSize fontStyle fontWeight limit lineHeight radius text theta

Examples
--------
Text Table Heatmap
^^^^^^^^^^^^^^^^^^
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    base = alt.Chart(source).transform_aggregate(
        num_cars='count()',
        groupby=['Origin', 'Cylinders']
    ).encode(
        alt.X('Cylinders:O', scale=alt.Scale(paddingInner=0)),
        alt.Y('Origin:O', scale=alt.Scale(paddingInner=0)),
    )

    heatmap = base.mark_rect().encode(
        color=alt.Color('num_cars:Q',
            scale=alt.Scale(scheme='viridis'),
            legend=alt.Legend(direction='horizontal')
        )
    )

    text = base.mark_text(baseline='middle').encode(
        text='num_cars:Q',
        color=alt.condition(
            alt.datum.num_cars > 100,
            alt.value('black'),
            alt.value('white')
        )
    )

    heatmap + text

Labels
^^^^^^
You can also use ``text`` marks as labels for other marks and set offset (``dx`` or ``dy``), ``align``, and ``baseline`` properties of the mark definition.

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({
        'a' : ['A', 'B', 'C'],
        'b' : [28, 55, 43]
    })

    bar = alt.Chart(source).mark_bar().encode(
        y = 'a:N',
        x = alt.X('b:Q', scale = alt.Scale(domain = [0,60]))
    )

    text = bar.mark_text(
                align = 'left',
                baseline = 'middle',
                dx = 3
    ).encode(
        text = 'b'
    )

    bar + text

Scatterplot with Text
^^^^^^^^^^^^^^^^^^^^^
Mapping a field to ``text`` channel of text mark sets the mark’s text value. For example, we can make a colored scatterplot with text marks showing the initial character of its origin, instead of ``point`` marks.

.. altair-plot::
    import altair as alt
    from vega_datasets import data
    from altair import datum

    source =  data.cars()

    alt.Chart(source).mark_text().encode(
        x = 'Horsepower:Q',
        y = 'Miles_per_Gallon:Q',
        color = 'Origin:N',
        text = 'Origin[0]:N'
    )

Geo Text
^^^^^^^^
By mapping geographic coordinate data to ``longitude`` and ``latitude`` channels of a corresponding projection, we can show text at accurate locations. The example below shows the name of every US state capital at the location of the capital.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    states = alt.topo_feature(data.us_10m.url, feature="states")

    source = data.us_state_capitals()

    background = alt.Chart(states).mark_geoshape(
        fill="lightgray",
        stroke="white"
    ).properties(
        width=750,
        height=500
    ).project("albersUsa")

    line = alt.Chart(source).mark_text(dy = -10).encode(
        latitude="lat:Q",
        longitude="lon:Q",
        text = 'city:N'
    )

    point = alt.Chart(source).mark_circle().encode(
        latitude="lat:Q",
        longitude="lon:Q",
        color = alt.value('orange')
    )

    background + line + point

