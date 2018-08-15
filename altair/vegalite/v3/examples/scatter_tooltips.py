"""
Scatter Plot with Tooltips
--------------------------
A scatter plot of the cars dataset, with tooltips showing selected column
values when you hover over points. We make the points larger so that it is
easier to hover over them.
"""
# category: simple charts

import altair as alt
from vega_datasets import data

cars = data.cars()

alt.Chart(cars).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()
