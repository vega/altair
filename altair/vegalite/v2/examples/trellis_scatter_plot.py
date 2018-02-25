"""
Trellis Scatter Plot
-----------------------
This example shows how to make a trellis scatter plot.
"""

import altair as alt
from vega_datasets import data

source = data.movies()

chart = alt.Chart(source).mark_point().encode(
    x = 'Worldwide_Gross', 
    y = 'US_DVD_Sales', 
    column = 'MPAA_Rating'
)
