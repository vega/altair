"""
Simple Scatter Plot with Tooltips
---------------------------------

A simple example of an interactive scatter plot using the well-known iris
dataset, with tooltips that show the species name when the mouse hovers
over each point.
"""
# category: simple charts

import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species',
    tooltip='species'
).interactive()
