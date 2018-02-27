"""
One Dot Per Zipcode
-----------------------
This example shows a geographical plot with one dot per zipcode.
"""

import altair as alt
from vega_datasets import data

states = alt.UrlData(data.us_10m.url,
                     format=alt.TopoDataFormat(type='topojson',
                                               feature='states'))
zipcodes = data.zipcodes.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    projection={'type': 'albersUsa'},
    width=800,
    height=500
)

# Zip Codes labeled on background
points = alt.Chart(zipcodes).mark_circle(size = 2).encode(
    #alt.Text('city', type='nominal'),
    alt.X('longitude', type='longitude'),
    alt.Y('latitude', type='latitude'),
    color = 'digit:N'
)

points.transform = [{"calculate": "substring(datum.zip_code, 0, 1)", "as": "digit"}]
chart = background + points
