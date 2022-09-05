"""
Title: Scatterplot and histogram with interval selection  

Description: 
1. This example shows how to link a scatter plot and histograms
together such that an interval selection in the scatterplot will plot the selected
values in the histogram plots. 

2. The histograms represent the x and y axis data presented in scatterplot categorised as per 
a color grouping variable.  
"""

import altair as alt
from vega_datasets import data

source = data.cars()

brush = alt.selection(type = "interval")

# scatter plot (main)
points = (
    alt.Chart(source).mark_point(filled = True, opacity = 0.3)
    .encode(
        x = alt.X("Miles_per_Gallon:Q", title = "Miles per Gallon"),
        y = alt.Y("Horsepower:Q"),
        color = alt.condition(brush, "Origin:N", alt.value("lightgrey")),
        size = alt.value(100)
    )
).add_selection(brush)

# Histogram at top (x-axis)
x_hist = (
    alt.Chart(source).mark_bar(opacity=0.3)
    .encode(
        x = alt.X("Miles_per_Gallon:Q", bin = alt.Bin(maxbins=20), title = ""),
        y = alt.Y("count()", stack = None, title = "Count"),
        color = "Origin:N"
    )
).transform_filter(brush).properties(height = 100)

# Hsitogram at side (y-axis)
y_hist = (
    alt.Chart(source).mark_bar(opacity=0.3)
    .encode(
        x = alt.X("count()",stack = None, title = "Count"),
        y = alt.Y("Horsepower:Q", bin = alt.Bin(maxbins=20), title = ""),
        color = "Origin:N"
    )
).transform_filter(brush).properties(width = 100)

# Plot positioning
alt.vconcat(x_hist, alt.hconcat(points, y_hist))