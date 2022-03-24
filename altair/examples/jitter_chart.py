"""
Jitter Chart
------------
In this chart, we encode the ``Cylinders`` column from the ``cars`` dataset in the ``y``-channel.  Because most cars (all but seven) in this dataset have 4, 6, or 8 cylinders, the default presentation of this data would show most of the data concentrated on three horizontal lines.  Furthermore, in that default presentation, it would be difficult to gauge the relative frequencies with which different values occur (because there would be so much overlap).  To compensate for this, we use the ``yOffset`` channel to incorporate a random offset (jittering).  This is adapted from a corresponding Vega-Lite Example:
`Dot Plot with Jittering <https://vega.github.io/vega-lite/examples/point_offset_random.html>`_.
"""
# category: scatter plots
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Cylinders:O',
    yOffset='randomCalc:Q'
).transform_calculate(
    randomCalc='random()'
).properties(
    height=alt.Step(50)
)
