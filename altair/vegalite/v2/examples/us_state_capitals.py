"""
U.S. state capitals overlayed on a map of the U.S
-------------------------------------------------
This is a layered geographic visualization that shows US capitals
overlayed on a map.
"""
# category: geographic

import altair as alt
from vega_datasets import data

states = alt.UrlData(data.us_10m.url,
                     format=alt.TopoDataFormat(type='topojson',
                                               feature='states'))
capitals = data.us_state_capitals.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    projection={'type': 'albersUsa'},
    width=800,
    height=500
)

# State capitals labeled on background
points = alt.Chart(capitals).mark_text(dy=-5, align='right').encode(
    alt.Text('city', type='nominal'),
    alt.X('lon', type='longitude'),
    alt.Y('lat', type='latitude'),
)

chart = background + points + points.mark_point(color='black')
