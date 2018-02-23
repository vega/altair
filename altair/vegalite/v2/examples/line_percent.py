"""
Line Chart with Percent axis
-----------------------
This example shows how to set an axis as a percent.
"""

import altair as alt
from vega_datasets import data

source = data.jobs()

base = source[source['job'] == 'Welder']
    
chart = alt.Chart(base).mark_line().encode(
    x='year:T',
    y=alt.Y('perc', axis=alt.Axis(format='%')),
    color='sex')
