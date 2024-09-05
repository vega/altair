"""
Seattle Weather Interactive
===========================
This chart provides an interactive exploration of Seattle weather over the
course of the year. It includes a one-axis brush selection to easily
see the distribution of weather types in a particular date range.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

color = alt.Color('weather:N').scale(
    domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
    range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd']
)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_point(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_point().encode(
    alt.X('monthdate(date):T').title('Date'),
    alt.Y('temp_max:Q')
        .title('Maximum Daily Temperature (C)')
        .scale(domain=[-5, 40]),
    alt.Size('precipitation:Q').scale(range=[5, 200]),
    color=alt.condition(brush, color, alt.value('lightgray')),
).properties(
    width=550,
    height=300
).add_params(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart().mark_bar().encode(
    x='count()',
    y='weather:N',
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=550,
).add_params(
    click
)

alt.vconcat(
    points,
    bars,
    data=source,
    title="Seattle Weather: 2012-2015"
)
