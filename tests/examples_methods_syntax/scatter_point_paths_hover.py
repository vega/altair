"""
Scatter plot with point paths on hover with search box
======================================================
This example demonstrates an interactive visualization technique inspired by [this Vega example](https://vega.github.io/vega/examples/global-development/), 
adapted for Altair's higher-level API. Key features:

1. Point Paths. On hover, shows data trajectories using a trail mark that thickens from past to present, clearly indicating the direction of time.
2. Search Box. Implements a case-insensitive regex filter for country names, enabling dynamic, flexible data point selection to enhance exploratory analysis.

"""
# category: interactive charts

import altair as alt
from vega_datasets import data

# Data source
source = data.gapminder.url

# X-value slider
x_slider = alt.binding_range(min=1955, max=2005, step=5, name='Year ')
x_select = alt.selection_point(name="x_select", fields=['year'], bind=x_slider, value=1980)

# Hover selection
hover = alt.selection_point(on='mouseover', fields=['country'], empty=False)
# A separate hover for the points since these need empty=True  
hover_point_opacity = alt.selection_point(on='mouseover', fields=['country'])  

# Search box for country name
search_box = alt.param(
    value='',
    bind=alt.binding(input='search', placeholder="Country", name='Search ')
)

# Base chart
base = alt.Chart(source).encode(
    x=alt.X('fertility:Q', scale=alt.Scale(zero=False, nice=False), title='Fertility'),
    y=alt.Y('life_expect:Q', scale=alt.Scale(zero=False, nice=False), title='Life Expectancy'),
    color=alt.Color('region:N', title='Region').legend(orient='bottom-left', titleFontSize=14, labelFontSize=12).scale(scheme='dark2'),
    detail='country:N'
).transform_calculate(
    region="""{
        '0': 'South Asia',
        '1': 'Europe & Central Asia',
        '2': 'Sub-Saharan Africa',
        '3': 'The Americas',
        '4': 'East Asia & Pacific',
        '5': 'Middle East & North Africa'
    }[datum.cluster]"""
)

# Points that are always visible (filtered by slider and search)
visible_points = base.mark_circle(size=100).encode(
    opacity=alt.condition(
            hover_point_opacity & 
        alt.expr.test(alt.expr.regexp(search_box, 'i'), alt.datum.country),
        alt.value(0.8),
        alt.value(0.1))
).transform_filter(
    x_select
).add_params(
    hover,
    hover_point_opacity,
    x_select
)


hover_line = alt.layer(
    # Line layer
    base.mark_trail().encode(
        order=alt.Order(
            'year:Q',
            sort='ascending'
        ),
        size=alt.Size(
            'year:Q',
            scale=alt.Scale(domain=[1955, 2005], range=[1, 12]),
            legend=None
        ),
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        color=alt.value('#222222')
    ),
    # Point layer
    base.mark_point(size=50).encode(
        opacity=alt.condition(hover, alt.value(0.8), alt.value(0)),
    )
)

# Year labels
year_labels = base.mark_text(align='left', dx=5, dy=-5, fontSize=14).encode(
    text='year:O', color=alt.value('#222222')
).transform_filter(hover)


# Country labels
country_labels = alt.Chart(source).mark_text(
    align='left',
    dx=-15,
    dy=-25,
    fontSize=18,
    fontWeight='bold'
).encode(
    x='fertility:Q',
    y='life_expect:Q',
    text='country:N',
    color=alt.value('black'),
    opacity=alt.condition(hover, alt.value(1), alt.value(0))
).transform_window(
    rank='rank(life_expect)', # 
    sort=[alt.SortField('life_expect', order='descending')], 
    groupby=['country'] # places label atop highest point on y-axis on hover
).transform_filter(
    alt.datum.rank == 1
).transform_aggregate(
    life_expect='max(life_expect)',
    fertility='max(fertility)',
    groupby=['country']
)

background_year = alt.Chart(source).mark_text(
    align='center',
    baseline='middle',
    fontSize=96,
    opacity=0.2
).encode(
    text='year:O',
    x=alt.X('width:Q', axis=None, scale=None),
    y=alt.Y('height:Q', axis=None, scale=None)
).transform_filter(
    x_select
).transform_aggregate(
    year='max(year)'
).transform_calculate(
    width='width/2',
    height='height/2'
)

# Combine all layers
chart = alt.layer(
    visible_points, year_labels, country_labels, hover_line, background_year
).properties(
    width=500,
    height=500,
    padding=35  # Padding ensures labels fit
).configure_axis(
    labelFontSize=12,
    titleFontSize=12
).add_params(search_box)

chart