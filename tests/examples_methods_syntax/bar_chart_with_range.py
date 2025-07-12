"""
Bar Chart with Range
====================
This example shows a range bar chart where each bar displays information of a low and high value.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

bar = alt.Chart(source).mark_bar(cornerRadius=10, height=10).encode(
    x=alt.X('min(temp_min):Q').scale(domain=[-15, 45]).title('Temperature (°C)'),
    x2='max(temp_max):Q',
    y=alt.Y('month(date):O').title(None) 
)

text_min = alt.Chart(source).mark_text(align='right', dx=-5).encode(
    x='min(temp_min):Q',
    y=alt.Y('month(date):O'),
    text='min(temp_min):Q'
)

text_max = alt.Chart(source).mark_text(align='left', dx=5).encode(
    x='max(temp_max):Q',
    y=alt.Y('month(date):O'),
    text='max(temp_max):Q'
)

(bar + text_min + text_max).properties(
    title=alt.Title(text='Temperature variation by month', subtitle='Seatle weather, 2012-2015')
)