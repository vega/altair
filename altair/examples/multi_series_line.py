"""
Multiple-Series Line Chart
--------------------------

This example shows how to make a line chart with multiple series of data.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

alt.Chart(source).mark_line().encode(
    x="year",
    y="net_generation",
    color="source"
)
