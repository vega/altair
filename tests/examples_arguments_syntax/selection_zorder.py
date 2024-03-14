"""
Selection zorder
================
This example shows how to bring selected point to the front/foreground
by using a condition to change the point's (z)order
as it is hovered over with the pointer.
This prevents that the selected points are obscured
by those that are not selected.
"""
# category: interactive charts

import altair as alt
from vega_datasets import data


cars = data.cars.url

hover = alt.selection_point(on='mouseover', nearest=True, empty=False)

chart = alt.Chart(cars, title='Selection obscured by other points').mark_circle(opacity=1).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(hover, alt.value('coral'), alt.value('lightgray')),
    size=alt.condition(hover, alt.value(300), alt.value(30))
).add_params(
    hover
)

chart | chart.encode(
    order=alt.condition(hover, alt.value(1), alt.value(0))
).properties(
    title='Selection brought to front'
)
