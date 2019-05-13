"""
Simple Scatter Plot with Large Square Marks
-------------------------------------------
This example shows how to create scatter plot with large square marks
"""
# category: simple charts
import altair as alt
from vega_datasets import data

people = data.lookup_people()

alt.Chart(people).mark_square(size=200).encode(
    x="age",
    y="height",
    color="name",
    tooltip='name'
).properties(
    width=400, height=200
)
