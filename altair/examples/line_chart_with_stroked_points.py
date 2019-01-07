"""
Line Chart with Stroked Points
------------------------------
This chart shows a line chart with stroked points marking each value.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.iowa_electricity()

base = alt.Chart(source).encode(
    x="year",
    y="net_generation",
    color="source"
)

line = base.mark_line()

point = base.mark_point(fill="white")

line + point
