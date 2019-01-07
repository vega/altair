"""
Line Chart with Points
----------------------
This chart shows a line chart with points marking each value.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.wheat()

alt.Chart(source).mark_line(point=True).encode(
    x="year:O",
    y="wheat:Q"
).properties(width=600)
