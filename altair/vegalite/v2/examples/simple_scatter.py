"""
Simple Scatter Plot
-------------------
A simple example of an interactive scatter plot using the well-known iris
dataset.
"""
# category: simple charts

import altair as alt


iris = alt.datasets.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species',
    tooltip='species'
).interactive()
