"""
Locations of US Airports
========================
This is a layered geographic visualization that shows the positions of US
airports on a background of US states.
"""
# category: geographic
import altair as alt
from vega_datasets import data

states = alt.UrlData(data.us_10m.url,
                     format=alt.TopoDataFormat(type='topojson',
                                               feature='states'))
airports = data.airports.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    projection={'type': 'albersUsa'},
    width=500,
    height=300
)

# airport positions on background
points = alt.Chart(airports).mark_circle().encode(
    alt.X('longitude:lon'),
    alt.Y('latitude:lat'),
    alt.SizeValue(10),
    alt.ColorValue('steelblue')
)

chart = background + points
