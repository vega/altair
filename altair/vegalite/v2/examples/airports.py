"""
Locations of US Airports
========================
This is a layered geographic visualization that shows the positions of US
airports on a background of US states.
"""
# category: maps
import altair as alt


states = alt.topo_feature(alt.datasets.us_10m.url, feature='states')
airports = alt.datasets.airports.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=500,
    height=300
).project('albersUsa')

# airport positions on background
points = alt.Chart(airports).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size=alt.value(10),
    color=alt.value('steelblue')
)

background + points
