"""
Interval Selection
==================

This is an example of creating a stacked chart for which the domain of the
top chart can be selected by interacting with the bottom chart.
"""
# category: area charts
import altair as alt
from vega_datasets import data

source = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

base = alt.Chart(source, width=600, height=200).mark_area().encode(
    x = 'date:T',
    y = 'price:Q'
)

upper = base.encode(
    alt.X('date:T').scale(domain=brush)
)

lower = base.properties(
    height=60
).add_params(brush)

upper & lower
