"""
Step Chart
-----------------
This example shows Google's stock price over time.
"""

import altair as alt
from vega_datasets import data

source = data.stocks()

chart = alt.Chart(source).mark_line(interpolate = 'step-after').encode(
    x = 'date',
    y = 'price'
)

chart.transform = [{"filter": "datum.symbol==='GOOG'"}]


chart
