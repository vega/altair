"""
Waterfall Chart
-----------------
This example shows how to make a simple waterfall chart.
"""
# category: bar charts
import altair as alt
import pandas as pd
from altair import datum

data = pd.DataFrame([
    {"task": "A", "start": 0, "end": 3},
    {"task": "B", "start": 3, "end": 8},
    {"task": "C", "start": 8, "end": 10}
])

waterfall_bars = alt.Chart(data).mark_bar(size=100).encode(
    y2=alt.Y2('end:Q'),
    y=alt.Y('start:Q', axis=alt.Axis(grid=False)),
    x=alt.X('task:N')
)

ticks = alt.Chart(data).mark_tick(
    color="grey",
    size=150,
    xOffset=100
).encode(
    y='end:Q',
    x='task:N'
).transform_filter(
    datum.task != "C"
)

(waterfall_bars + ticks).properties(
    width=500
)
