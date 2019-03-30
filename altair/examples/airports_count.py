"""
Locations of US Airports
========================
This is a layered geographic visualization that shows the positions of US
airports on a background of US states.
"""
# category: maps
import altair as alt
from vega_datasets import data

airports = data.airports()
airports_counts = airports[['state','latitude', 'longitude']]

# Take the mean as the position of state
agg = {'latitude': 'mean',
         'longitude': 'mean'
                  }
airports_counts = airports.groupby(['state']).agg(agg) 
agg = {'latitude': 'count',
      
                  }

airports_counts['Number of Airports'] =  airports.groupby(['state']).agg(agg)

states = alt.topo_feature(data.us_10m.url, feature='states')

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=500,
    height=300
).project('albersUsa')

# airport positions on background
points = alt.Chart(airports_counts).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size='Number of Airports:Q',
    color=alt.value('steelblue')
).properties(
    title='Number of airports in US'
)


background + points