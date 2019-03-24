"""
Calculating Percentage of Total
-------------------------------
This chart demonstrates how to use a window transform to display data values
as a percentage of total values.
"""
# category: bar charts
import altair as alt
import pandas as pd

source = pd.DataFrame({'Activity': ['Sleeping', 'Eating', 'TV', 'Work', 'Exercise'],
                           'Time': [8, 2, 4, 8, 2]})

alt.Chart(source).mark_bar().encode(
    alt.X('PercentOfTotal:Q', axis=alt.Axis(format='.0%')),
    y='Activity:N'
).transform_window(
    TotalTime='sum(Time)',
    frame=[None, None]
).transform_calculate(
    PercentOfTotal="datum.Time / datum.TotalTime"
)
