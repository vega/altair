"""
Title: Scatterplot and boxplot with interval selection    

Description: 
1. This example shows how to link a scatter plot and boxplots
together such that an interval selection in the scatterplot will plot the selected
values in the boxplots. 

2. The two boxplots represent the x and y axis variables of scatterplot categorised as per 
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
        x = alt.X("Miles_per_Gallon:Q"),
        y = alt.Y("Horsepower:Q"),
        color = alt.condition(brush, "Origin:N", alt.value("lightgrey")),
        size = alt.value(100)
    )
).add_selection(brush)


x_box = (
    alt.Chart(source).mark_boxplot()
    .encode(
        x = alt.X("Miles_per_Gallon:Q", title = ""),
        y = alt.Y("Origin:N", ),
        color = "Origin:N"
    )
).transform_filter(brush).properties(height = 100)

y_box = (
    alt.Chart(source).mark_boxplot()
    .encode(
        x = alt.X("Origin:N"),
        y = alt.Y("Horsepower:Q", title = ""),
        color = "Origin:N"
    )
).transform_filter(brush).properties(width = 100)

alt.vconcat(x_box, alt.hconcat(points, y_box))