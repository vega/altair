"""
LayerChart with Bar and Tick
----------------------------
This example shows how to layer two charts on top of one another.
"""
# category: bar charts
import altair as alt
import pandas as pd

data = pd.DataFrame({
    'project': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'score': [25, 57, 23, 19, 8, 47, 8],
    'goal': [25, 47, 30, 27, 38, 19, 4]}
)

a = alt.Chart().mark_bar().encode(
    x='project',
    y='score'
)

b = alt.Chart().mark_tick(
    color='red',
).encode(
    x='project',
    y='goal'
)

alt.layer(a, b).properties(
    data=data
).configure_tick(
    thickness=2,
    bandSize=35  # controls the width of the tick
).configure_scale(
    rangeStep=40  # controls the width of the bar
)
