# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
# ///
"""
Simple Stacked Area Chart
-------------------------
This example shows how to make a simple stacked area chart.
"""
# category: simple charts
import altair as alt
from altair.datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
)
