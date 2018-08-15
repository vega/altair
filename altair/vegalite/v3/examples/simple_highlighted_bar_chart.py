"""
Simple Highlighted Bar Chart
============================
This example shows a basic bar chart with a single bar singled out for a highlight.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

population = data.population.url

alt.Chart(population).mark_bar().encode(
    x="year:O",
    y="sum(people):Q",
    # The highlight will be set on the result of a conditional statement
    color=alt.condition(
        alt.datum.year == 1970,  # If the year is 1970 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    )
)
