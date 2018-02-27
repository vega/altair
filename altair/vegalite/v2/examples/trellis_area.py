"""
Trellis Area
-----------------
This example shows stock prices of four large companies as a small multiples of area charts.
"""

import altair as alt
from vega_datasets import data

source = data.stocks()

chart = alt.Chart(source).mark_area().encode(
    x=alt.X('date:T',
        axis=alt.Axis(format='%Y', title='Time', grid=False)
    ),
    y=alt.Y('price:Q',
        axis=alt.Axis(title='Price', grid=False)
    ),
    color=alt.Color('symbol', legend=None),
    row=alt.Row('symbol:N',
        header = alt.Header(title = 'Symbol')
    )
).properties(
    width=300,
    height=40
).transform_data(
    {"filter": "datum.symbol !== 'GOOG'"}
)
