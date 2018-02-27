"""
One Dot Per Zipcode
-----------------------
This example shows a geographical plot with one dot per zipcode.
"""

import altair as alt
from vega_datasets import data

states = alt.UrlData(data.us_10m.url,
                     format=alt.TopoDataFormat(type='topojson',
                                               feature='states'))
zipcodes = data.zipcodes.url

chart = alt.Chart(zipcodes).mark_circle(size = 3).encode(
    #alt.Text('city', type='nominal'),
    alt.X('longitude', type='longitude'),
    alt.Y('latitude', type='latitude'),
    color = 'digit:N'
).properties(
    projection={'type': 'albersUsa'},
    width=800,
    height=500)

chart.transform = [{"calculate": "substring(datum.zip_code, 0, 1)", "as": "digit"}]
