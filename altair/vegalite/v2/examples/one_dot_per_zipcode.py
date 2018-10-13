"""
One Dot Per Zipcode
-----------------------
This example shows a geographical plot with one dot per zipcode.
"""
# category: case studies
import altair as alt
from vega_datasets import data

zipcodes = data.zipcodes.url

alt.Chart(zipcodes).mark_circle(size=3).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='digit:N'
).project(
    type='albersUsa'
).properties(
    width=650,
    height=400
).transform_calculate(
    "digit", alt.expr.substring(alt.datum.zip_code, 0, 1)
)
