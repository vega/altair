"""
U.S. State Capitals Overlayed on a Map of the U.S
-------------------------------------------------
This is a layered geographic visualization that shows US capitals
overlayed on a map.
"""
# category: case studies
import altair as alt
from vega_datasets import data

states = alt.topo_feature(data.us_10m.url, 'states')
capitals = data.us_state_capitals.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    title='US State Capitols',
    width=650,
    height=400
).project('albersUsa')

# Points and text
hover = alt.selection_point(on='pointerover', nearest=True,
                      fields=['lat', 'lon'])

base = alt.Chart(capitals).encode(
    longitude='lon:Q',
    latitude='lat:Q',
)

text = base.mark_text(dy=-5, align='right').encode( 
    alt.Text('city:N'),
    opacity=alt.when(~hover).then(alt.value(0)).otherwise(alt.value(1))
)

points = base.mark_point().encode(
    color=alt.value('black'),
    size=alt.when(~hover).then(alt.value(30)).otherwise(alt.value(100))
).add_params(hover)

background + points + text
