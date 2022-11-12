.. currentmodule:: altair

.. _user-guide-area-marks:

Area
~~~~~~~~~~
``area`` represent multple data element as a single area shape.
Area marks are often used to show change over time, using either a single area or stacked areas.

Examples
--------

Area Chart
^^^^^^^^^^
Using ``area`` mark with one temporal or ordinal field (typically on ``x``) and
one quantitative field (typically on ``y``) produces an area chart. For example,
the following area chart shows a number of unemployment people in the US over time.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.unemployment_across_industries.url

    alt.Chart(source).mark_area().encode(
        x = 'yearmonth(date):T',
        y = 'sum(count):Q',
    ).properties(
        width=300,
        height=200
    )

Area Chart with Overlaying Lines and Point Markers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By setting ``line`` and ``point`` properties of the mark definition
to ``true`` or an object defining a property of the overlaying point marks, we can overlay line and point markers on top of area.

.. altair-plot::
    import altair as alt
    from vega_datasets import data
    from altair.expr import datum

    source = data.stocks.url

    alt.Chart(source).mark_area(line = True, point = True).encode(
        x = 'date:T',
        y = 'price:Q',
    ).transform_filter(
        datum.symbol == 'GOOG'
    )

Instead of using a single color as the fill color of the area, we can set it to a gradient.
In this example, we are also customizing the overlay. For more information about gradient options see the Vega-Lite Gradient documentation.

.. altair-plot.::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).transform_filter(
        'datum.symbol==="GOOG"'
    ).mark_area(
        line={'color':'darkgreen'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='white', offset=0),
                alt.GradientStop(color='darkgreen', offset=1)],
            x1=1,
            x2=1,
            y1=1,
            y2=0
        )
    ).encode(
        alt.X('date:T'),
        alt.Y('price:Q')
    )

Stacked Area Chart
^^^^^^^^^^^^^^^^^^
Adding a color field to area chart creates stacked area chart by default. For example, here we split the area chart by industry.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.unemployment_across_industries.url

    alt.Chart(source).mark_area().encode(
        alt.X('yearmonth(date):T',
            axis=alt.Axis(format='%Y', domain=False, tickSize=0)
        ),
        alt.Y('sum(count):Q'),
        alt.Color('series:N',
            scale=alt.Scale(scheme='category20b')
    ))

Normalized Stacked Area Chart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also create a normalized stacked area chart by setting ``"stack"`` to ``"normalize"`` in the encoding channel. Here we can easily see the percentage of unemployment across industries.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.unemployment_across_industries.url

    alt.Chart(source).mark_area().encode(
        alt.X('yearmonth(date):T',
            axis=alt.Axis(format='%Y', domain=False, tickSize=0)
        ),
        alt.Y('sum(count):Q', stack = 'normalize'),
        alt.Color('series:N',
            scale=alt.Scale(scheme='category20b')
    ))

Steamgraph
^^^^^^^^^^^

We can also shift the stacked area chart’s baseline to center and produces a streamgraph by setting ``"stack"`` to ``"center"`` in the encoding channel.
Adding the ``interactive`` method allows for changing the scales.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.unemployment_across_industries.url

    alt.Chart(source).mark_area().encode(
        alt.X('yearmonth(date):T',
            axis=alt.Axis(format='%Y', domain=False, tickSize=0)
        ),
        alt.Y('sum(count):Q', stack='center', axis=None),
        alt.Color('series:N',
            scale=alt.Scale(scheme='category20b')
        )
    ).interactive()

Ranged Area
^^^^^^^^^^^
Specifying ``x2`` or ``y2`` for the quantitative axis of area marks produce ranged areas. For example, we can use ranged area with the ``ci0`` and ``ci0``
aggregation operators to highlight 95% confidence interval of a line chart that shows mean values over time.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_area(opacity=0.7).encode(
        alt.X('monthdate(date):T', title = 'Date'),
        alt.Y('mean(temp_max):Q', title = "Daily Temperature Range (C)"),
        alt.Y2('mean(temp_min):Q', )
    ).properties(
        width=600,
        height=300
    )
