"""
Connected Scatterplot (Lines with Custom Paths)
-----------------------------------------------

This example shows how layering can be used to build a plot. This dataset tracks miles driven per capita along with gas prices annually from 1956 to 2010. It is based on the May 2, 2010 New York Times article 'Driving Shifts Into Reverse'. See http://mbostock.github.io/protovis/ex/driving.html .
"""

import altair as alt
from vega_datasets import data

driving = data.driving()

lines = alt.Chart(driving).mark_line().encode(
    alt.X('miles', scale=alt.Scale(zero=False)),
    alt.Y('gas', scale=alt.Scale(zero=False)),
    order='year'
)

points = alt.Chart(driving).mark_circle().encode(
    alt.X('miles', scale=alt.Scale(zero=False)),
    alt.Y('gas', scale=alt.Scale(zero=False)),
    order='year'
)

chart = lines + points
