"""
Multiple Marks
==============
This example demonstrates creating a single chart with multiple markers
representing the same data.
"""
# category: other charts
import altair as alt


stocks = alt.datasets.stocks()

alt.LayerChart(stocks).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
).add_layers(
    alt.Chart().mark_point(),
    alt.Chart().mark_line()
)
