"""
Horizontal Aggregate Bar Chart
------------------------------
This example is a bar chart showing the distribution of US population
by age in the year 2000.
"""

import altair as alt
from altair.expr import datum

from vega_datasets import data
pop = data.population.url

chart = alt.Chart(pop).mark_bar().encode(
    x = alt.X('sum(people):Q', axis=alt.Axis(title='population')),
    y = 'age:O'
).properties(
    height=300,
    width=300
).transform_filter(datum.year == 2000)
