"""
Trellis Area
-----------------
This example shows stock prices of four large companies as a small multiples of area charts.
"""

import altair as alt
from altair.expr import datum
from vega_datasets import data

source = data.stocks()

chart = alt.Chart(source).mark_area().encode(
    alt.X('date:T', axis=alt.Axis(format='%Y', title='Time', grid=False)),
    alt.Y('price:Q', axis=alt.Axis(title='Price', grid=False)),
    alt.Color('symbol', legend=None),
    alt.Row('symbol:N', header = alt.Header(title = 'Symbol'))
).properties(
    width=300,
    height=40
).transform_filter(
    datum.symbol != 'GOOG'
)
