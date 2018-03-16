"""
Layering text over a heatmap
----------------------------

An example of a layered chart of text over a heatmap using the cars dataset.
"""

import altair as alt
from vega_datasets import data

cars = data.cars.url

heatmap = alt.Chart(cars).mark_rect().encode(
    alt.X('Cylinders:O', scale=alt.Scale(paddingInner=0)),
    alt.Y('Origin:O', scale=alt.Scale(paddingInner=0)),
    alt.Color('count(*):Q')
)

text = alt.Chart(cars).mark_text(
    baseline='middle'
).encode(
    alt.X('Cylinders:O'),
    alt.Y('Origin:O'),
    alt.Text('count(*):Q'),
    color=alt.condition("datum['count_*'] > 100",
                        alt.value('black'),
                        alt.value('white'))
)

chart = heatmap + text
