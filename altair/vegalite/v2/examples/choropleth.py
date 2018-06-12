"""
Choropleth Map
==============
A choropleth map of unemployment rate per county in the US
"""
# category: maps
import altair as alt


counties = alt.topo_feature(alt.datasets.us_10m.url, 'counties')
unemp_data = alt.datasets.unemployment.url


alt.Chart(counties).mark_geoshape().encode(
    color='rate:Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(unemp_data, 'id', ['rate'])
).project(
    type='albersUsa'
).properties(
    width=500,
    height=300
)
