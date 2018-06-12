"""
Table Bubble Plot (Github Punch Card)
-------------------------------------
This example shows github contributions by the day of week and hour of the day.
"""
# category: scatter plots
import altair as alt


source = alt.datasets.github.url

alt.Chart(source).mark_circle().encode(
    x='hours(time):O',
    y='day(time):O',
    size='sum(count):Q'
)
