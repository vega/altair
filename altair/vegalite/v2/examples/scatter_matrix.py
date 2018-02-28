"""
Scatter Matrix
--------------
An example of using a RepeatChart to construct a multi-panel scatter plot
with linked panning and zooming.
"""

import altair as alt
from vega_datasets import data

chart = alt.Chart(data.cars.url).mark_circle().encode(
    alt.X(alt.repeat_column(), type='quantitative'),
    alt.Y(alt.repeat_row(), type='quantitative'),
    color='Origin:N'
).properties(
    width=250,
    height=250
).interactive()

alt.RepeatChart(chart).set_repeat(
    row=['Horsepower', 'Acceleration', 'Miles_per_Gallon'],
    column=['Miles_per_Gallon', 'Acceleration', 'Horsepower']
)
