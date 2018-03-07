"""
Simple Scatter Plot
-------------------

A simple example of an interactive scatter plot using the well-known iris
dataset.
"""
# category: basic charts

from altair import Chart
from vega_datasets import data

iris = data.iris()

chart = Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
).interactive()
