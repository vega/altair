"""
Grouped Bar Chart
-----------------------
This example shows a population broken out by gender and age for a specific year.
The grouping is achieved by building a trellis plot with narrow column
encoded on the age groups and x-axes encoded on gender.
"""
# category: bar charts
import altair as alt
from altair.expr import datum, if_
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_bar(stroke='transparent').encode(
    alt.X('gender:N', scale=alt.Scale(rangeStep=12), axis=alt.Axis(title='')),
    alt.Y('sum(people):Q', axis=alt.Axis(title='population', grid=False)),
    color=alt.Color('gender:N', scale=alt.Scale(range=["#EA98D2", "#659CCA"])),
    column='age:O'
).configure_view(
    stroke='transparent'
).configure_axis(
    domainWidth=0.8
).transform_filter(
    datum.year == 2000
).transform_calculate(
    'gender', if_(datum.sex == 2, 'Female', 'Male')
)
