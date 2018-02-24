"""
Line Chart with Percent axis
-----------------------
This example shows how to set an axis as a percent.
"""

import altair as alt
from vega_datasets import data

source = data.jobs()

source.year = source.year.astype(str)

welders = source[source.job == 'Welder']
    
chart = alt.Chart(welders).mark_line().encode(
    x=alt.X('year', timeUnit='year'),
    y=alt.Y('perc', axis=alt.Axis(format='%')),
    color='sex',
    detail='job'
).properties(
    title='Percent of work-force working as Welders'
)
