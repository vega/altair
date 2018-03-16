"""
Stacked Bar Chart
-----------------

This example shows how to make a stacked bar chart of the weather type in Seattle from 2012 to 2015 by month.
"""

import altair as alt
from vega_datasets import data

weather = data.seattle_weather()

chart = alt.Chart(weather).mark_bar().encode(
    alt.Color('weather:N',
        legend=alt.Legend(title='Weather type'),
        scale=alt.Scale(
            domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
            range=['#e7ba42', '#c7c7c7', '#aec7e8', '#1f77b4', '#9467bd']
        ),
    ),
    alt.X('date:N',
        axis=alt.Axis(title='Month of the Year'),
        timeUnit='month',
    ),
    y='count(*):Q',
)
