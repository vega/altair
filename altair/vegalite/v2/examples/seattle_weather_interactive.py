"""
Seattle Weather Interactive
===========================
This chart provides an interactive exploration of Seattle weather over the
course of the year. It includes a one-axis brush selection to easily
see the distribution of weather types in a particular date range.
"""
# category: interactive

import altair as alt
from vega_datasets import data

scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
                 range=['#e7ba52', '#c7c7c7', '#aec7e8', '#1f77b4', '#9467bd'])

brush = alt.selection_interval(encodings=['x'])

points = alt.Chart().mark_point().encode(
    alt.X('date:T', timeUnit='monthdate', axis=alt.Axis(title='Date')),
    alt.Y('temp_max:Q', axis=alt.Axis(title='Maximum Daily Temperature (C)')),
    color=alt.condition(brush, 'weather:N', alt.value('lightgray'), scale=scale),
    size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
).properties(
    width=600,
    height=400,
    selection=brush
)

bars = alt.Chart().mark_bar().encode(
    x='count(*):Q',
    y='weather:N',
    color=alt.Color('weather:N', scale=scale),
).transform_filter(
    brush.ref()
).properties(
    width=600
)

chart = alt.vconcat(points, bars, data=data.seattle_weather.url)
