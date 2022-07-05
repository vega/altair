"""
Multiple Series Line Chart
--------------------------

This example shows how to make a line chart with multiple series of data.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_line().encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
)
