"""
Line chart with Confidence Interval Band
========================================
This example shows how to make a line chart with a bootstrapped 95% confidence interval band.
"""
# category: line charts
import altair as alt
from vega_datasets import data

cars = data.cars()

line = alt.Chart(cars).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)'
)

confidence_interval = alt.Chart(cars).mark_area(opacity=0.3).encode(
    x='Year',
    y=alt.Y('ci0(Miles_per_Gallon)', axis=alt.Axis(title='Miles/Gallon')),
    y2='ci1(Miles_per_Gallon)'
)

confidence_interval + line
