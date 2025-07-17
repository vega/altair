"""
Line Chart with Custom Order
----------------------------
By default, the line's path (order of points in the line) is
determined by data values on the temporal/ordinal field.
However, a field can be mapped to the order channel for a custom path.

For example, to show a pattern of data change over time between
gasoline price and average miles driven per capita we use
order channel to sort the points in the line by time field (year).
The earliest year (1956) is one endpoint and the latest year (2010)
is the other endpoint.

This is based on Hannah Fairfield's article 'Driving Shifts Into Reverse'.
See https://archive.nytimes.com/www.nytimes.com/imagepages/2010/05/02/business/02metrics.html.
"""
# category: line charts
import altair as alt
from altair.datasets import data

source = data.driving()

alt.Chart(source).mark_line(point=True).encode(
    alt.X("miles", scale=alt.Scale(zero=False)),
    alt.Y("gas", scale=alt.Scale(zero=False)),
    order="year",
    tooltip=["miles", "gas", "year"],
)
