"""
Line Chart with Point Markers
-----------------------------
This chart shows a simple line chart with points marking each value.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_line(point=True).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
)