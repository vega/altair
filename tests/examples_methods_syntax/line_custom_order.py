"""
Line Chart with Custom Order
----------------------------
By default, the line’s path (order of points in the line) is
determined by data values on the temporal/ordinal field.
However, a field can be mapped to the order channel for a custom path.

For example, to show a pattern of data change over time between
gasoline price and average miles driven per capita we use
order channel to sort the points in the line by time field (year).
The earliest year (1956) is one endpoint and the latest year (2010)
is the other endpoint.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.driving()

alt.Chart(source).mark_line(point=True).encode(
    x=alt.X("miles").scale(zero=False),
    y=alt.Y("gas").scale(zero=False),
    order="year",
    tooltip=["miles", "gas", "year"],
)
