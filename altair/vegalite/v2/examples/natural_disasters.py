"""
Natural Disasters
-----------------
This example shows a visualization of global deaths from natural disasters.
"""

import altair as alt
from vega_datasets import data

source = data.disasters()

chart = alt.Chart(source).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1
).encode(
    x = alt.X('Year:O', axis = alt.Axis(labelAngle = 0)),
    y = alt.X('Entity:N'),
    size = alt.Size('Deaths:Q',
        scale = alt.Scale(range = [0, 5000]),
        legend = alt.Legend(title = 'Annual Global Deaths')
    ),
    color = alt.Color('Entity', legend = None)
).properties(
    width=600,
    height=400
).add_transform(
    {"filter": "datum.Entity !== 'All natural disasters'"}
)
