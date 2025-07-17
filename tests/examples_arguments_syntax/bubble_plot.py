"""
Bubble Plot
-----------------
This example shows how to make a bubble plot.
"""
# category: scatter plots
import altair as alt
from altair.datasets import data

source = data.cars()

alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    size='Acceleration'
)
