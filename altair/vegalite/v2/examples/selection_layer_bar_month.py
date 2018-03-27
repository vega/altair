"""
Interactive Average
===================
The plot below uses an interval selection, which causes the chart to include an interactive brush
(shown in grey). The brush selection parameterizes the red guideline, which visualizes the average
value within the selected interval.
"""
# category: interactive

import altair as alt
from vega_datasets import data

weather = data.seattle_weather.url
brush = alt.selection(type='interval', encodings=['x'])

bars = alt.Chart().mark_bar().encode(
    alt.X('date:O', timeUnit='month'),
    y='mean(precipitation):Q',
    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.7))
).properties(
    selection=brush
)

line = alt.Chart().mark_rule(color='firebrick').encode(
    y='mean(precipitation):Q',
    size=alt.SizeValue(3)
).transform_filter(brush.ref())

chart = alt.layer(bars + line, data=weather)
