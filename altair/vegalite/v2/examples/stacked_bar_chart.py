"""
Stacked Bar Chart
-----------------

This example shows how to make a stacked bar chart of the weather type in Seattle from 2012 to 2015 by month.
"""
# category: bar charts
import altair as alt


weather = alt.datasets.seattle_weather()

alt.Chart(weather).mark_bar().encode(
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
    y='count()',
)
