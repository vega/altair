# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Grouped Bar Chart
-----------------
This example shows a grouped bar chart.
"""
# category: bar charts
import altair as alt
from altair.datasets import data

source = data.barley()

alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='sum(yield):Q',
    color='year:N',
    column='site:N'
)
