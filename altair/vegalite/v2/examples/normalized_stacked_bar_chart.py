"""
Normalized Stacked Bar Chart
----------------------------
This example shows how to make a normalized stacked bar chart.
"""

import altair as alt
from altair.expr import datum, if_
from vega_datasets import data

source = data.population.url

chart = alt.Chart(source).mark_bar().encode(
    alt.X('age:O', scale=alt.Scale(rangeStep=17)),
    alt.Y('sum(people):Q',
        axis=alt.Axis(title='population'),
        stack='normalize'
    ),
    alt.Color('gender:N',
        scale=alt.Scale(range=["#EA98D2", "#659CCA"])
    )
).transform_filter(
    datum.year == 2000
).transform_calculate(
    "gender", if_(datum.sex == 2, 'Female', 'Male')
)
