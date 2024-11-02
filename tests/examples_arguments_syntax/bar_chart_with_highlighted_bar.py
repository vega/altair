"""
Bar Chart with Highlighted Bar
------------------------------
This example shows a basic bar chart with a single bar highlighted.
"""
# category: bar charts
import altair as alt
from vega_datasets import data

source = data.wheat()

# If the `year` column equals `1810`
# then, set the bar color to `"orange"`
# otherwise, use `"steelblue"`
color = alt.when(year=1810).then(alt.value("orange")).otherwise(alt.value("steelblue"))

alt.Chart(source).mark_bar().encode(
    x="year:O",
    y="wheat:Q",
    color=color
).properties(width=600)
