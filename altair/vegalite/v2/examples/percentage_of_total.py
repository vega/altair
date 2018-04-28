"""
Calculating Percentage of Total
-------------------------------
This chart demonstrates how to use a window transform to display data values
as a percentage of total values.
"""
# category: bar charts
import altair as alt
import pandas as pd

activities = pd.DataFrame({'Activity': ['Sleeping', 'Eating', 'TV', 'Work', 'Exercise'],
                           'Time': [8, 2, 4, 8, 2]})

alt.Chart(activities).mark_bar().encode(
    x='PercentOfTotal:Q',
    y='Activity:N'
).transform_window(
    window=[alt.WindowFieldDef(op='sum', field='Time', **{'as': 'TotalTime'})],
    frame=[None, None]
).transform_calculate(
    PercentOfTotal="datum.Time / datum.TotalTime * 100"
)
