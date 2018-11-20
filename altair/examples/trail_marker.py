"""
Trail Marker
------------
The ``trail`` marker is like the ``line`` marker, but it allows properties of
the line (such as thickness) to vary along the length of the line.
This shows a simple example of the trail mark using stock prices.
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_trail().encode(
    x='date:T',
    y='price:Q',
    size='price:Q',
    color='symbol:N'
)
