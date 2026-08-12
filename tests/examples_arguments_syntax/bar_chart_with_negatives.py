"""
Bar Chart with Negative Values
==============================
This example shows a bar chart with both positive and negative values.
"""
# category: bar charts
import altair as alt
from altair.datasets import data

source = data.us_employment()

predicate = alt.datum.nonfarm_change > 0
color = alt.when(predicate).then(alt.value("steelblue")).otherwise(alt.value("orange"))

alt.Chart(source).mark_bar().encode(
    x="month:T",
    y="nonfarm_change:Q",
    color=color
).properties(width=600)
