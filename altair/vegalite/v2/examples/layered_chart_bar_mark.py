"""
LayerChart with Bar and Tick
-----------------------
This example shows how to layer two charts on top of one another.
"""

import altair as alt
import pandas as pd

data = {'project': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
       'score': [25, 57, 23, 19, 8, 47, 8],
       'goal': [25, 47, 30, 27, 38, 19,4]}

source = pd.DataFrame(data)

a = alt.Chart(source).mark_bar().encode(
    x='project',
    y='score')

b = alt.Chart(source).mark_tick(color='red').encode(
    x='project',
    y='goal')

chart = alt.layer(a, b, config={'tick': {'thickness': 2, 'bandSize': 50}})
