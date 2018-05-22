"""
Simple Highlighted Bar Chart
============================
This example shows a basic bar chart with a single bar singled out for a highlight.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

population = data.population()

alt.Chart(population).mark_bar().transform_calculate(
    # Using a simple boolean test to calculate a new column on the fly
    # allows the chart creator to decide which bar they'd like to highlight.
    "highlight",
    alt.datum.year == 2000
).encode(
    x="year:O",
    y="sum(people):Q",
    # The highlight is then applied by using the calculate column
    # to set the color.
    color="highlight:N"
)
