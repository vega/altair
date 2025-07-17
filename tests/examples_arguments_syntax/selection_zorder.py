"""
Selection zorder
================
This example shows how to bring selected points to the front/foreground
by using a condition to change the point's (z)order
as it is hovered over with the pointer.
This prevents that the selected points are obscured
by those that are not selected.
"""
# category: interactive charts

import altair as alt
from altair.datasets import data


cars = data.cars.url

hover = alt.selection_point(on='pointerover', nearest=True, empty=False)
when_hover = alt.when(hover)

chart = alt.Chart(cars, title='Selection obscured by other points').mark_circle(opacity=1).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=when_hover.then(alt.value("coral")).otherwise(alt.value("lightgray")),
    size=when_hover.then(alt.value(300)).otherwise(alt.value(30))
).add_params(
    hover
)

chart | chart.encode(
    order=when_hover.then(alt.value(1)).otherwise(alt.value(0))
).properties(
    title='Selection brought to front'
)
