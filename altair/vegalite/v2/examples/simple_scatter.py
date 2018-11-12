"""
Simple Scatter Plot
-------------------
A simple example of an interactive scatter plot using the well-known iris
dataset.
"""
# category: simple charts

import altair as alt
from vega_datasets import data

source = data.iris()

alt.Chart(source).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species',
    tooltip='species'
).interactive()
