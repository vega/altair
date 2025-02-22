"""
Faceted County-Level Choropleth Maps
-------------------
A set of maps arranged in a grid, each showing the distribution of a species' projected habitat across US counties. 

Each choropleth map uses color intensity to represent the percentage values within county boundaries.
"""
# category: maps

import altair as alt
import pandas as pd
from vega_datasets import data

# Load the CSV data
url = "https://raw.githubusercontent.com/vega/vega-datasets/e40833e505c7212bf28b5d3bf4d5f1d84baaa69b/data/species.csv" # temporary until vega/vega-datasets#684 is merged
df = pd.read_csv(url)

# Disable row limit for Altair
alt.data_transformers.disable_max_rows()

# Load US counties topology
counties = alt.topo_feature(data.us_10m.url, 'counties')

# Create a chart for each unique species (limiting to first 4 for demonstration)
species_list = df['common_name'].unique()[:4]

charts = [
    alt.Chart(counties).mark_geoshape(tooltip=True)
    .encode(
        color=alt.Color("habitat_pct:Q")
        .scale(domain=[0, 1], scheme='viridis', zero=True, nice=False)
        .title(['Suitable Habitat', '% of County'])
        .legend(format=".0%"),
        tooltip=[
            alt.Tooltip("id:N").title('County ID'),
            alt.Tooltip("habitat_pct:Q").title('Habitat %').format('.2%')
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
    .transform_filter(
        "indexof(['2', '15'], '' + floor(datum.id / 1000)) == -1"
    )
    .transform_calculate(
        habitat_pct="datum.habitat_yearround_pct === null ? 0 : datum.habitat_yearround_pct"
    )
    .project(type='albersUsa')
    .properties(width=300, height=200)
    .properties(title=species)
    for species in species_list
]

# Combine charts into a grid
chart = alt.concat(*charts, columns=2).configure_view(
    stroke=None
).configure_mark(
    invalid='filter'
)

# Display the chart
chart