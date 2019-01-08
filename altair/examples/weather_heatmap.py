"""
Seattle Weather Heatmap
-----------------------
This example shows the 2010 daily max temperature (F) in Seattle, WA.
"""
# category: line charts
import altair as alt
from vega_datasets import data

# Since the data is more than 5,000 rows we'll import it from a URL
source = data.seattle_temps.url

alt.Chart(
    source,
    title="2010 Daily Max Temperature (F) in Seattle, WA"
).mark_rect().encode(
    x=alt.X('date:O', timeUnit='date'),
    y=alt.Y('date:O', timeUnit='month'),
    color=alt.Color('temp:Q', aggregate='max'),
    tooltip=[
        alt.Tooltip('date:T', timeUnit='monthdate', title='Date'),
        alt.Tooltip('temp:Q', aggregate='max', title='Max Temp')
    ]
).properties(width=600)
