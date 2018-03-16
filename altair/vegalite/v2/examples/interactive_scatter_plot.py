"""
Simple Interactive Colored Scatterplot
--------------------------------------
This example shows how to make an interactive scatterplot.
"""
# category: interactive

import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()
