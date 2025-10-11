"""
Parallel Coordinates
--------------------
A `Parallel Coordinates <https://en.wikipedia.org/wiki/Parallel_coordinates>`_
chart is a chart that lets you visualize the individual data points by drawing
a single line for each of them.
Such a chart can be created in Altair by first transforming the data into a
suitable representation.
This example shows a parallel coordinates chart with the Penguins dataset.
"""
# category: advanced calculations

import altair as alt
from altair.datasets import data

source = data.penguins()

alt.Chart(source, width=500).transform_window(
    index='count()'
).transform_fold(
    ['Beak Length (mm)', 'Beak Depth (mm)', 'Flipper Length (mm)']
).mark_line().encode(
    x='key:N',
    y='value:Q',
    color='Species:N',
    detail='index:N',
    opacity=alt.value(0.5)
)
