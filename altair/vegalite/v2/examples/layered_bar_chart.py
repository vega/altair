"""
Layered Bar Chart
-----------------
This example shows a bar chart showing the US population distribution of age groups and gender in 2000.
"""
# category: bar charts
import altair as alt
from altair.expr import datum, if_
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_bar(opacity=0.7).encode(
    alt.X('age:O', scale=alt.Scale(rangeStep=17)),
    alt.Y('sum(people):Q', axis=alt.Axis(title='population'), stack=None),
    alt.Color('gender:N', scale=alt.Scale(range=["#EA98D2", "#659CCA"]))
).transform_filter(
    datum.year == 2000
).transform_calculate(
    "gender", if_(datum.sex == 2, 'Female', 'Male')
)
