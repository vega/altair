"""
Line Chart with Percent axis
----------------------------
This example shows how to format the tick labels of the y-axis of a chart as percentages.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.jobs()
welders = source[source.job == 'Welder']

alt.Chart(welders).mark_line().encode(
    alt.X('year:O'),
    alt.Y('perc:Q', axis=alt.Axis(format='%')),
    color='sex:N'
)
