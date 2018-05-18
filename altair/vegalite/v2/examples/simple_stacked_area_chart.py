"""
Simple Stacked Area Chart
-------------------------
This example shows how to make a simple stacked area chart.
"""
# category: simple charts
import altair as alt


iowa = alt.datasets.iowa_electricity()

alt.Chart(iowa).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
)
