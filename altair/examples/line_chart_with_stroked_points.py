"""
Line Chart with Stroked Points
------------------------------
This chart shows a line chart with stroked points marking each value.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.wheat()

base = alt.Chart(source).encode(
    x="year:O",
    y="wheat:Q"
)

line = base.mark_line()

point = base.mark_point(fill="white", stroke="steelblue")

(line + point).properties(width=600)
