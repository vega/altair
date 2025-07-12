"""
Faceted County-Level Choropleth Maps
-------------------
A set of maps arranged in a grid, each showing the distribution of a species' projected habitat across US counties. 

Each choropleth map uses color intensity to represent the percentage values within county boundaries.
"""
# category: maps

import altair as alt
from altair.datasets import data

# Parse county_id as number for lookup (URL ref)
csv_data = alt.UrlData(data.species.url, format=alt.CsvDataFormat(parse={'county_id': 'number'}))

# Load US counties topology (URL ref)
counties = alt.topo_feature(data.us_10m.url, 'counties')

chart = alt.Chart(csv_data).mark_geoshape().encode(
    shape='geo:G',  # Geographic shape encoding for map rendering
    color=alt.Color('habitat_yearround_pct:Q')
    .scale(domain=[0, 1], scheme='viridis', zero=True, nice=False)
    .title(['Suitable Habitat', '% of County'])
    .legend(format='.0%'),
    tooltip=[
        alt.Tooltip('id:N').title('County ID'),
        alt.Tooltip('habitat_yearround_pct:Q').title('Habitat %').format('.2%')
    ],
    facet=alt.Facet('common_name:N', columns=2).title(None),
).transform_lookup(
    lookup='county_id',
    from_=alt.LookupData(data=counties, key='id'),
    as_='geo'  # Join county geometry data
).project(type='albers').properties(width=300, height=200)

# Display the chart
chart