.. currentmodule:: altair

.. _user-guide-line-marks:

Line
~~~~
The ``line`` mark represents the data points stored in a field with a line connecting all of these points. Line marks are commonly used to depict trajectories or change over time. Unlike most other marks that represent one data element per mark, one line mark represents multiple data element as a single line, akin to ``area`` and ``trail``.

Note: For line segments that connect (x,y) positions to (x2,y2) positions, please use ``rule`` marks. For continuous lines with varying size, please use ``trail`` marks.

Examples 
--------
Line Chart
^^^^^^^^^^
Using line with one temporal or ordinal field (typically on ``x``) and another quantitative field (typically on ``y``) produces a simple line chart with a single line.

.. altair-plot::
    import altair as alt
    from altair import datum
    from vega_datasets import data


    source = data.stocks()

    alt.Chart(source).mark_line().encode(
        x='date',
        y='price',
    ).transform_filter(
        datum.symbol == 'GOOG')

We can add create multiple lines by grouping along different attributes, such as ``color`` or ``detail``.

Multi-series Colored Line Chart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Adding a field to a mark property channel such as ``color`` groups data points into different series, producing a multi-series colored line chart.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line().encode(
        x='date',
        y='price',
        color='symbol',
    )

We can further apply selection to highlight a certain line on hover.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    highlight = alt.selection(type='single', on='mouseover',
                            fields=['symbol'], nearest=True)

    base = alt.Chart(source).encode(
        x='date:T',
        y='price:Q',
        color='symbol:N'
    )

    points = base.mark_circle().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = base.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    points + lines

Multi-series Line Chart with Varying Dashes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Adding a field to ``strokeDash`` also produces a multi-series line chart.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line().encode(
        x='date',
        y='price',
        strokeDash='symbol',
    )

We can also use line grouping to create a line chart that has multiple parts with varying styles.

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({ 
        'a' : ['A', 'B', 'D', 'E', 'E', 'G', 'H'],
        'b' : [28, 55, 91, 81, 81, 19, 87],
        'predicted' : [False, False, False, False, True, True, True]
    })

    alt.Chart(source).mark_line().encode(
        x = 'a:O',
        y = 'b:Q',
        strokeDash = 'predicted:N'
    )
  
Multi-series Line Chart with the Detail Channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To group lines by a field without mapping the field to any visual properties, we can map the field to the ``detail`` channel to create a multi-series line chart with the same color.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line().encode(
        x='date',
        y='price',
        detail='symbol',
    )

The same method can be used to group lines for a ranged dot plot.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.countries()

    base = alt.Chart(source).encode(
        alt.X('life_expect:Q', title= 'Life Expectancy (years)', scale=alt.Scale(zero=False)),
        alt.Y('country:N', title = 'Country', axis = alt.Axis(offset = 5, ticks = False, minExtent = 70, domain = False)),
    ).transform_filter(
        alt.FieldOneOfPredicate(field = 'country', 
                                oneOf = ["China", "India", "United States", "Indonesia", "Brazil"])
    )

    line = base.mark_line().encode(
        detail = 'country',
        color = alt.value("#db646f")
    ).transform_filter(
        alt.FieldOneOfPredicate(field = 'year', oneOf = [1995, 2000])
    )

    point = base.mark_point(filled = True).encode(
        alt.Color(field = 'year', 
                scale = alt.Scale(range = ["#e6959c", "#911a24"], domain = [1995, 2000])),
        size = alt.value(100),
        opacity = alt.value(1)
    )

    line + point

Line Chart with Point Markers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By setting the ``point`` property of the mark definition to ``true`` or an object defining a property of the overlaying point marks, we can overlay point markers on top of line.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line(point=True).encode(
        x='year(date)',
        y='mean(price):Q',
        color='symbol:N'
    )

This is equivalent to adding another layer of filled point marks.

Note that the overlay point marks have ``opacity`` = 1 by default (instead of semi-transparent like normal point marks).

Here we create stroked points by setting their ``\"filled\"`` to ``false`` and their fill to ``\"white\"``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line(point= alt.OverlayMarkDef(filled = False, fill = 'white')).encode(
        x='year(date)',
        y='mean(price):Q',
        color='symbol:N'
    )

Connected Scatter Plot (Line Chart with Custom Path)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The line’s path (order of points in the line) is determined by data values on the temporal/ordinal field by default. However, a field can be mapped to the ``order`` channel for determining a custom path.

For example, to show a pattern of data change over time between gasoline price and average miles driven per capita we use ``order`` channel to sort the points in the line by time field (year). In this example, we also use the ``point`` property to overlay point marks over the line marks to highlight each data point.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.driving()

    alt.Chart(source).mark_line(point=True).encode(
        alt.X('miles', scale=alt.Scale(zero=False)),
        alt.Y('gas', scale=alt.Scale(zero=False)),
        order='year'
    )

Line interpolation
^^^^^^^^^^^^^^^^^^
The ``interpolate`` property of a mark definition can be used to change line interpolation method. For example, we can set ``interpolate`` to ``"monotone"``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line(interpolate='monotone').encode(
        x='date',
        y='price'
    ).transform_filter(
        alt.datum.symbol == 'GOOG'
    )

We can also set ``interpolate`` to ``"step-after"`` to create a step-chart.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_line(interpolate='step-after').encode(
        x='date',
        y='price'
    ).transform_filter(
        alt.datum.symbol == 'GOOG'
    )

Geo Line 
^^^^^^^^
By mapping geographic coordinate data to ``longitude`` and ``latitude`` channels of a corresponding projection, we can draw lines through geographic points.


.. altair-plot::
    import altair as alt
    from vega_datasets import data
    import pandas as pd

    airports = data.airports.url
    flights_airport = data.flights_airport.url

    states = alt.topo_feature(data.us_10m.url, feature="states")

    lookup_data = alt.LookupData(
        airports, key="iata", fields=["state", "latitude", "longitude"]
    )

    source = pd.DataFrame({ 
        'airport' : ['SEA', 'SFO', 'LAX', 'LAS', 'DFW', 'DEN', 'ORD', 'JFK'],
        'order' : [1, 2, 3, 4, 5, 6, 7, 8],
    })

    background = alt.Chart(states).mark_geoshape(
        fill="lightgray",
        stroke="white"
    ).properties(
        width=750,
        height=500
    ).project("albersUsa")

    line = alt.Chart(source).mark_line().encode(
        latitude="latitude:Q",
        longitude="longitude:Q",
        order = 'order'
    ).transform_lookup(
        lookup = 'airport',
        from_ = lookup_data
    )

    background + line

Line Config
^^^^^^^^^^^

The ``line`` property of the top-level ``config`` object sets the default properties for all line marks. If mark property encoding channels are specified for marks, these config values will be overridden.

The line config can contain any line mark properties (except ``type``, ``style``, and ``clip``).