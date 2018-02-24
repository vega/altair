"""
Line Chart with Percent axis
-----------------------
This example shows how to set an axis as a percent.
"""

import altair as alt
from vega_datasets import data

source = data.jobs()

# The year here is stored by pandas as an integer. When treating columns as dates,
# it is best to use either a string representation or a datetime representation.
source.year = source.year.astype(str)

welders = source[source.job == 'Welder']
    
chart = alt.Chart(welders).mark_line().encode(
    x=alt.X('year', timeUnit='year'),
    y=alt.Y('perc', axis=alt.Axis(format='%')),
    color='sex'
).properties(
    title='Percent of work-force working as Welders'
)
