"""
Choropleth Map
==============
A choropleth map of unemployment rate per county in the US
"""
# category: geographic

import altair as alt
from vega_datasets import data

counties = alt.topo_feature(data.us_10m.url,'counties')
unemp_data = alt.UrlData(data.unemployment.url)


chart = alt.Chart(counties).mark_geoshape().properties(
    projection={'type': 'albersUsa'},
    width=500,
    height=300
).encode(
    color='rate:Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(unemp_data, 'id', ['rate'])
)
