"""
Multiple Marks
==============
This example demonstrates creating a single chart with multiple markers
representing the same data.
"""
# category: other charts
import altair as alt


stocks = alt.datasets.stocks()

alt.Chart(stocks).mark_line(point=True).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
)
