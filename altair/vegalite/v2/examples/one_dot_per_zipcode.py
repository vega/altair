"""
One Dot Per Zipcode
-----------------------
This example shows a geographical plot with one dot per zipcode.
"""

import altair as alt
from vega_datasets import data

zipcodes = data.zipcodes.url

chart = alt.Chart(zipcodes).mark_circle(size = 3).encode(
    x='longitude:lon',
    y='latitude:lat',
    color='digit:N'
).properties(
    projection={'type': 'albersUsa'},
    width=800,
    height=500
).transform_data(
    {"calculate": "substring(datum.zip_code, 0, 1)", "as": "digit"}
)
