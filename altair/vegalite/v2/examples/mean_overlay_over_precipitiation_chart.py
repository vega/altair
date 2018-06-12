"""
Layered Bar Chart with Line as Mean
-----------------------------------
This example shows mean overlay over precipitation chart.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

bar = alt.Chart(source).mark_bar().encode(
    x='month(date):O',
    y='mean(precipitation):Q'
)

rule = alt.Chart(source).mark_rule(color='red').encode(
    y='mean(precipitation)',
    size=alt.value(3)
)

bar + rule
