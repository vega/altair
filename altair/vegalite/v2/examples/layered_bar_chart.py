"""
Layered Bar Chart
-----------------------
This example shows a bar chart showing the US population distribution of age groups and gender in 2000.
"""

import altair as alt
from vega_datasets import data

source = data.population.url

chart = alt.Chart(source).mark_bar(opacity = 0.7).encode(
    x = alt.X('age:O', scale = alt.Scale(rangeStep = 17)), 
    y = alt.Y('sum(people):Q', axis = alt.Axis(title = 'population'), stack = None),
    color = alt.Color('gender:N',
                      scale=alt.Scale(
            range = ["#EA98D2", "#659CCA"]))
)
chart.transform = [{"filter": "datum.year == 2000"},
                  {"calculate": "datum.sex == 2 ? 'Female' : 'Male'", "as": "gender"}]
