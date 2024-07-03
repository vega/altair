"""
Scatter plot with point paths on hover with search box
======================================================
This example demonstrates an interactive visualization technique inspired by [this Vega example](https://vega.github.io/vega/examples/global-development/), 
adapted for Altair's higher-level API. Key features:

1. Visual Hint Paths: Displays trajectories of data items across time on hover, enabling intuitive understanding of how data evolves.
2. Search Box: Allows filtering of data points by country name, extending the original concept with improved data exploration capabilities

"""
# category: interactive charts

import altair as alt
from vega_datasets import data

# Data source
source = data.gapminder.url

# X-value slider
x_slider = alt.binding_range(min=1955, max=2005, step=5, name='Year: ')
x_select = alt.selection_point(name="x_select", fields=['year'], bind=x_slider, value=1980)

# Hover selection
hover = alt.selection_point(on='mouseover', fields=['country'], empty=False)

# Search box for country name
search_box = alt.param(
    value='',
    bind=alt.binding(input='search', placeholder="Country", name='Search ')
)

# Base chart
base = alt.Chart(source).encode(
    x=alt.X('fertility:Q', scale=alt.Scale(zero=False), title='Fertility'),
    y=alt.Y('life_expect:Q', scale=alt.Scale(zero=False), title='Life Expectancy'),
    color=alt.Color('region_name:N').legend(title='Region'),
    detail='country:N'
).transform_calculate(
    region_name="{'0': 'South Asia', '1': 'Europe & Central Asia', '2': 'Sub-Saharan Africa', '3': 'America', '4': 'East Asia & Pacific', '5': 'Middle East & North Africa'}[datum.cluster]"
)

# Points that are always visible (filtered by slider and search)
visible_points = base.mark_circle(size=100).encode(
    opacity=alt.condition(x_select | search_box, alt.value(1), alt.value(0))
).add_params(x_select).transform_filter(
    x_select
).transform_filter(
    alt.expr.test(alt.expr.regexp(search_box, 'i'), alt.datum.country)
).add_params(hover)

# Line that appears on hover
hover_line = base.mark_line(point=True).encode(
    opacity=alt.condition(hover, alt.value(0.3), alt.value(0))
)

# Year labels
year_labels = base.mark_text(align='left', dx=5, dy=-5).encode(
    text='year:O'
).transform_filter(hover)

# Country labels
country_labels = base.mark_text(align='left', dx=5, dy=-25, fontSize=24).encode(
    text='country:N'
).transform_filter(hover).transform_filter(x_select)

background_year = alt.Chart(source).mark_text(
    align='center',
    baseline='middle',
    fontSize=96,
    opacity=0.2,
    x='width',
    y='height',
    dx=-400,
    dy=-300
).encode(
    text='year:O'
).transform_filter(
    x_select
).transform_aggregate(
    year='max(year)'  # This ensures we only get one label
)

# Combine all layers
chart = alt.layer(
    visible_points, year_labels, country_labels, hover_line, background_year
).properties(
    width=800,
    height=600,
    padding=50  # Padding required to ensure country labels fit
).configure_axis(
    labelFontSize=14,
    titleFontSize=14
).add_params(search_box)

chart