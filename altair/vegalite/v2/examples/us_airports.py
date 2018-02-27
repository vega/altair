"""
US Airports
-----------------------
This example shows one dot per airport in the US overlayed on geoshape.
"""

import altair as alt
from vega_datasets import data

states = alt.UrlData(data.us_10m.url,
                     format=alt.TopoDataFormat(type='topojson',
                                               feature='states'))
zipcodes = data.airports.url

background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    projection={'type': 'albersUsa'},
    width=800,
    height=500
)

points = alt.Chart(zipcodes).mark_circle(size = 10).encode(
    alt.X('longitude', type='longitude'),
    alt.Y('latitude', type='latitude')
)

points.transform = [{"calculate": "substring(datum.zip_code, 0, 1)", "as": "digit"}]

chart = background + points
