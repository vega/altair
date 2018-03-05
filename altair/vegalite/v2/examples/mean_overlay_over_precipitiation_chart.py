"""
Layered Bar Chart with Line as Mean
-----------------------------------
This example shows mean overlay over precipitation chart.
"""

import altair as alt
from vega_datasets import data

source = data.seattle_weather()

bar = alt.Chart(source).mark_bar().encode(
    x = alt.X('date:O', timeUnit = 'month'),
    y = alt.Y('mean(precipitation):Q'))

rule = alt.Chart(source).mark_rule(color = 'red').encode(
    y = 'mean(precipitation)',
    size = alt.SizeValue(3))
chart = bar + rule
