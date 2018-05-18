"""
Interactive Rectangular Brush
=============================
This example shows how to add a simple rectangular brush to a scatter plot.
By clicking and dragging on the plot, you can highlight points within the
range.
"""
# category: interactive charts
import altair as alt


cars = alt.datasets.cars.url
brush = alt.selection(type='interval')

alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Cylinders:O', alt.value('grey'))
).add_selection(
    brush
)
