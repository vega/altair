"""
Bar and Tick Chart
------------------
How to layer a tick chart on top of a bar chart.
"""
# category: bar charts
import altair as alt
import pandas as pd

source = pd.DataFrame({
    'project': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'score': [25, 57, 23, 19, 8, 47, 8],
    'goal': [25, 47, 30, 27, 38, 19, 4]
})

base = alt.Chart(source)

bar = base.mark_bar().encode(
    x='project',
    y='score'
)

tick = base.mark_tick(
    color='red',
    thickness=2
).encode(
    x='project',
    y='goal'
)

(bar + tick).configure_tick(
    bandSize=35  # controls the width of the tick
).configure_scale(
    rangeStep=40  # controls the width of the bar
)
