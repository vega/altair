"""
Normalized Stacked Area Chart
-----------------------------
This example shows how to make a normalized stacked area chart.
"""
# category: area charts
import altair as alt


iowa = alt.datasets.iowa_electricity()

alt.Chart(iowa).mark_area().encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack="normalize"),
    color="source:N"
)
