"""
Faceted Stacked Bar Chart
=========================
A horizontal stacked bar chart using barley crop yield data.
The chart is horizontally faceted based on the year,
and vertically faceted based on variety.
"""
# category: bar charts
import altair as alt
from altair.datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    column="year:O",
    x="yield",
    y="variety",
    color="site",
).properties(width=220)
