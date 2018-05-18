"""
Repeated Choropleth Map
=======================
Three choropleths representing disjoint data from the same table.
"""
# category: maps
import altair as alt


states = alt.topo_feature(alt.datasets.us_10m.url, 'states')

pop_eng_hur = alt.datasets.population_engineers_hurricanes.url

variable_list = ['population', 'engineers', 'hurricanes']

alt.Chart(states).mark_geoshape().encode(
    alt.Color(alt.repeat('row'), type='quantitative')
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(pop_eng_hur, 'id', variable_list)
).properties(
    width=500,
    height=300
).project(
    type='albersUsa'
).repeat(
    row=variable_list
).resolve_scale(
    color='independent'
)
