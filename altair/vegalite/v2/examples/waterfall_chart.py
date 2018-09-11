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
    {"costs": "Advertising costs", "start": 0, "end": 3},
    {"costs": "Fixed costs", "start": 3, "end": 8},
    {"costs": "Other costs", "start": 8, "end": 10},
    {"costs": "Total costs", "start": 0, "end": 10}

])

waterfall_bars = alt.Chart(data).mark_bar(size=100).encode(
    y2=alt.Y2('end:Q'),
    y=alt.Y('start:Q', axis=alt.Axis(grid=False)),
    x=alt.X('costs:N')
)

ticks = alt.Chart(data).mark_tick(
    color="grey",
    size=150,
    xOffset=100
).encode(
    y='end:Q',
    x='costs:N'
).transform_filter(
    datum.costs != "Total costs"
)

(waterfall_bars + ticks).configure_axisX(
    labelAngle=0
).properties(
    width=500
)
