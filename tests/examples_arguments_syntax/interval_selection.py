"""
Interval Selection with Initial Date Range
==========================================

This is an example of creating a stacked chart for which the domain of the
top chart can be selected by interacting with the bottom chart. The initial
selection range is set using Python's native datetime objects.
"""
# category: area charts
import altair as alt
from vega_datasets import data
import datetime as dt

source = data.sp500.url

date_range = (dt.date(2007, 6, 30), dt.date(2009, 6, 30))

brush = alt.selection_interval(encodings=['x'],
                               value={'x': date_range})

base = alt.Chart(source).mark_area().encode(
    x = 'date:T',
    y = 'price:Q'
).properties(
    width=600,
    height=200
)

upper = base.encode(
    alt.X('date:T', scale=alt.Scale(domain=brush))
)

lower = base.properties(
    height=60
).add_params(brush)

upper & lower
