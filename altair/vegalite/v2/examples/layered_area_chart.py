"""
Layered Area Chart
------------------
This example shows a layered area chart.
"""
# category: area charts
import altair as alt
from vega_datasets import data

iowa = data.iowa_electricity()

alt.Chart(iowa).mark_area(opacity=0.3).encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack=None),
    color="source:N"
)
