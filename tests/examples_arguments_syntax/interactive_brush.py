"""
Interactive Rectangular Brush
=============================
This example shows how to add a simple rectangular brush to a scatter plot.
By clicking and dragging on the plot, you can highlight points within the
range.
"""
# category: interactive charts
import altair as alt
from altair.datasets import data

source = data.cars()
brush = alt.selection_interval()

alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.when(brush).then("Cylinders:O").otherwise(alt.value("grey")),
).add_params(brush)
