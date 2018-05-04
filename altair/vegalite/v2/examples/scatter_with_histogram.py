"""
Scatter Plot and Histogram with Interval Selection
==================================================

This example shows how to link a scatter plot and a histogram 
together such that an interval selection in the histogram will 
plot the selected values in the scatter plot. 

Note that the binning  has to be applied to *both* 
the scatter plot and the bar chart via the `transform_bin` mehtod 
in order for this to work! 


"""
# category: interactive charts

import altair as alt
import pandas as pd
import numpy as np

x = np.random.normal(size=100)
y = np.random.normal(size=100)

m = np.random.normal(15, 1, size=100)

df = pd.DataFrame({"x": x, "y":y, "m":m})

pts = alt.selection(type="interval", encodings=["x"])

points = alt.Chart(df).mark_point(filled=True, color="black").encode(
    x = alt.X("x"),
    y = alt.Y("y")
).transform_filter(
    pts.ref()
).transform_bin(
 "mbin", field="m", bin=alt.Bin(maxbins=20)   
).properties(width=300, height=300)

mag = alt.Chart(df).mark_bar().encode(
    x = alt.X("mbin", type="nominal"),
    y = alt.Y("count()"),
    color = alt.condition(pts, alt.value("black"), alt.value("lightgray"))
).transform_bin(
    "mbin", field="m", bin=alt.Bin(maxbins=20)
).properties(
    selection=pts,
    width=300, 
    height=300)

points | mag
