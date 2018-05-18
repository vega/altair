"""
Layered Area Chart
------------------
This example shows a layered area chart.
"""
# category: area charts
import altair as alt


iowa = alt.datasets.iowa_electricity()

alt.Chart(iowa).mark_area(opacity=0.3).encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack=None),
    color="source:N"
)
