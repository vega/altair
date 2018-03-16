"""
Step Chart
-----------------
This example shows Google's stock price over time.
"""
# category: basic charts

import altair as alt
from altair.expr import datum
from vega_datasets import data

stocks = data.stocks()

chart = alt.Chart(stocks).mark_line(interpolate='step-after').encode(
    x = 'date',
    y = 'price'
).transform_filter(
    datum.symbol =='GOOG'
)
