"""
Filled Step Chart
-----------------
This example shows Google's stock price over time as a step chart with its area filled in. 
"""
# category: line charts
import altair as alt
from vega_datasets import data

stocks = data.stocks()

chart = alt.Chart(stocks).encode(
    x='date',
    y='price'
).transform_filter(
    alt.datum.symbol == 'GOOG'
)

line = chart.mark_line(color="darkblue")
area = chart.mark_area(color="lightblue")

(line + area).configure_mark(interpolate='step-after')
