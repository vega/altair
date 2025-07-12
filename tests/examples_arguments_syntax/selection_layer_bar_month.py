"""
Interactive Average
===================
The plot below uses an interval selection, which causes the chart to include an interactive brush
(shown in grey). The brush selection parameterizes the red guideline, which visualizes the average
value within the selected interval.
"""
# category: interactive charts
import altair as alt
from vega_datasets import data

source = data.seattle_weather()
brush = alt.selection_interval(encodings=['x'])

bars = alt.Chart().mark_bar().encode(
    x='month(date):O',
    y='mean(precipitation):Q',
    opacity = alt.when(brush).then(alt.value(1)).otherwise(alt.value(0.7)),
).add_params(
    brush
)

line = alt.Chart().mark_rule(color='firebrick').encode(
    y='mean(precipitation):Q',
    size=alt.SizeValue(3)
).transform_filter(
    brush
)

alt.layer(bars, line, data=source)
