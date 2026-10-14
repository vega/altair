# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Multiple Series Line Chart
--------------------------

This example shows how to make a line chart with multiple series of data.
"""
# category: line charts
import altair as alt
from altair.datasets import data

source = data.stocks()

alt.Chart(source).mark_line().encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
)
