"""
Strip Plot
-----------------
This example shows the relationship between horsepower and the numbver of cylinders using tick marks.
"""
# category: basic charts

import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_tick().encode(
    x='Horsepower:Q',
    y='Cylinders:O'
)
