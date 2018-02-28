"""
Aggregate Bar Chart
-----------------
This example is a bar chart showing the US population distribution of age groups in 2000..
"""

import altair as alt
from vega_datasets import data

source = data.population()

chart = alt.Chart(source).mark_bar().encode(
    x = alt.X('sum(people):Q', axis = alt.Axis(title = 'population')),
    y = alt.Y('age:O', scale = alt.Scale(rangeStep = 17))
).transform_filter("datum.year == 2000")
