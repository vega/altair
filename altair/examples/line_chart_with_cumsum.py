"""
Line Chart with Cumulative Sum
------------------------------
This chart creates a simple line chart from the cumulative sum of a fields.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.wheat()

alt.Chart(source).mark_line().transform_window(
    # Sort the data chronologically in this case
    sort=[{'field': 'year'}],
    # Include all previous records before the current record and none after
    frame=[None, 0],
    # What we want to add up
    cumulative_wheat='sum(wheat)',
).encode(
    x='year:O',
    # Plot the calculated field created by the transformation
    y='cumulative_wheat:Q'
).properties(width=600)