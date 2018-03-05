"""
Line Chart with Percent axis
----------------------------
This example shows how to set an axis as a percent.
"""

import altair as alt
from vega_datasets import data

source = data.jobs.url

chart = alt.Chart(source).mark_line().encode(
    x=alt.X('year:O'),
    y=alt.Y('perc:Q', axis=alt.Axis(format='%')),
    color='sex:N'
).properties(
    title='Percent of work-force working as Welders'
).transform_filter("datum.job === 'Welder'")
