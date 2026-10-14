# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Line Chart with Stroked Point Markers
-------------------------------------
This example shows a simple line chart with points in a different color.
"""
# category: line charts
import altair as alt
from altair.datasets import data

source = data.stocks()

alt.Chart(source).mark_line(
    point=alt.OverlayMarkDef(filled=False, fill="white")
).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
)
