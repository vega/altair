"""
Line Chart with Confidence Interval Band
========================================
How to make a line chart with a bootstrapped 95% confidence interval band.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.cars()

# Configure the base chart
base = alt.Chart(source)

# Configure the line
line = base.mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)'
)

# Configure the confidence interval
confidence_interval = base.mark_area(opacity=0.3).encode(
    x='Year',
    y=alt.Y('ci0(Miles_per_Gallon)', axis=alt.Axis(title='Miles/Gallon')),
    y2='ci1(Miles_per_Gallon)'
)

# Draw the chart
confidence_interval + line
