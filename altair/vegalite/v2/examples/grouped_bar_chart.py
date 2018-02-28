"""
Grouped Bar Chart
-----------------------
This example shows a population broken out by gender and age for a specific year.
"""

import altair as alt
from vega_datasets import data

source = data.population()

chart = alt.Chart(source).mark_bar(stroke = 'transparent').encode(
    x = alt.X('gender:N', scale = alt.Scale(rangeStep = 12), axis = alt.Axis(title = '')),
    y = alt.Y('sum(people):Q', axis = alt.Axis(title = 'population', grid = False)),
    color = alt.Color('gender:N', scale = alt.Scale(range = ["#EA98D2", "#659CCA"])),
    column = 'age:O'
).configure_view(
    stroke='transparent'
).configure_axis(
    domainWidth=1
).transform_filter(
    "datum.year == 2000"
).transform_calculate(
    'gender',
    calculate= "datum.sex == 2 ? 'Female' : 'Male'"
)
