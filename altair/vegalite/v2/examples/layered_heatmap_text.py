"""
Layering text over a heatmap
----------------------------

An example of a layered chart of text over a heatmap using the cars dataset.
"""
# category: other charts
import altair as alt
from altair.expr import datum
from vega_datasets import data

cars = data.cars.url

heatmap = alt.Chart(cars).mark_rect().encode(
    alt.X('Cylinders:O', scale=alt.Scale(paddingInner=0)),
    alt.Y('Origin:O', scale=alt.Scale(paddingInner=0)),
    color='count()'
)

text = alt.Chart(cars).mark_text(baseline='middle').encode(
    x='Cylinders:O',
    y='Origin:O',
    text='count()',
    color=alt.condition(datum['count_*'] > 100,
                        alt.value('black'),
                        alt.value('white'))
)

heatmap + text
