"""
Faceted County-Level Choropleth Maps
-------------------
A set of maps arranged in a grid, each showing the distribution of a species' projected habitat across US counties. 

Each choropleth map uses color intensity to represent the percentage values within county boundaries.
"""
# category: maps

import altair as alt
from altair.datasets import data

# Load the CSV data
df = data.species()

# Disable row limit for Altair
alt.data_transformers.disable_max_rows()

# Load US counties topology
counties = alt.topo_feature(data.us_10m.url, 'counties')

# Create a chart for each unique species (limiting to first 4 for demonstration)
species_list = df['common_name'].unique()[:4]

charts = [
    alt.Chart(counties).mark_geoshape()
    .encode(
        color=alt.Color("habitat_yearround_pct:Q")
        .scale(domain=[0, 1], scheme='viridis', zero=True, nice=False)
        .title(['Suitable Habitat', '% of County'])
        .legend(format=".0%"),
        tooltip=[
            alt.Tooltip("id:N").title('County ID'),
            alt.Tooltip("habitat_yearround_pct:Q").title('Habitat %').format('.2%')
        ]
    )
    .transform_lookup(
        lookup='id',
        from_=alt.LookupData(
            data=df[df['common_name'] == species],
            key='county_id',
            fields=['habitat_yearround_pct']
        )
    )
    .project(type='albers')
    .properties(width=300, height=200)
    .properties(title=species)
    for species in species_list
]

# Combine charts into a grid
chart = alt.concat(*charts, columns=2)

# Display the chart
chart