"""
Stacked Density Estimates
-------------------------
To plot a stacked graph of estimates, use a shared ``extent`` and a fixed
number of subdivision ``steps`` to ensure that the points for each area align
well.  Density estimates of body mass for each penguin species are plotted
in a stacked method.  In addition, setting ``counts`` to true multiplies the
densities by the number of data points in each group, preserving proportional
differences.
"""
# category: distributions

import altair as alt
from altair.datasets import data

source = data.penguins()

alt.Chart(source).transform_density(
    density='Body Mass (g)',
    groupby=['Species'], 
    extent= [2500, 6500],
    counts = True,
    steps=200
).mark_area().encode(
    alt.X('value:Q').title('Body Mass (g)'), 
    alt.Y('density:Q', stack='zero'),
    alt.Color('Species:N')
).properties(
    width=400,
    height=80,
    title='Distribution of Body Mass of Penguins'
)
