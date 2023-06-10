.. currentmodule:: altair

.. _user-guide-trail-marks:

Trail
~~~~~
The ``trail`` mark represents the data points stored in a field with a line connecting all of these points. Trail is similar to the ``line`` mark but a trail can have variable widths determined by backing data. Unlike lines, trails do not support different interpolation methods and use ``fill`` (not ``stroke``) for their color. Trail marks are useful if you want to draw lines with changing size to reflect the underlying data.

Trail Mark Properties
---------------------
A ``trail`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: orient

Examples
--------
Line Chart with Varying Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.stocks()

    alt.Chart(source).mark_trail().encode(
        x="date",
        y="price",
        color="symbol",
        size="price",
    )

Comet Chart Showing Changes Between Two States
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    alt.Chart(data.barley.url).transform_pivot(
        "year",
        value="yield",
        groupby=["variety", "site"]
    ).transform_fold(
        ["1931", "1932"],
        as_=["year", "yield"]
    ).transform_calculate(
        calculate="datum['1932'] - datum['1931']",
        as_="delta"
    ).mark_trail().encode(
        alt.X("year:O").title(None),
        alt.Y("variety:N").title("Variety"),
        alt.Size("yield:Q")
            .scale(range=[0, 12])
            .legend(values=[20, 60])
            .title("Barley Yield (bushels/acre)"),
        alt.Color("delta:Q")
            .scale(domainMid=0)
            .title("Yield Delta (%)"),
        alt.Tooltip(["year:O", "yield:Q"]),
        alt.Column("site:N").title("Site"),
    ).configure_legend(
        orient='bottom',
        direction='horizontal'
    ).configure_view(
        stroke=None
    ).properties(
        title="Barley Yield comparison between 1932 and 1931"
    )
