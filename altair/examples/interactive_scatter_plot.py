"""
Simple Interactive Colored Scatter Plot
--------------------------------------
This example shows how to make an interactive scatter plot.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()
