"""
Bar Chart with Negative Values
==============================
This example shows a bar chart with both positive and negative values.
"""
# category: bar charts
import altair as alt

source = "https://raw.githubusercontent.com/datadesk/vega-datasets/gh-pages/data/us-employment.csv"

alt.Chart(source).mark_bar().encode(
    x="month:T",
    y="nonfarm_change:Q",
    color=alt.condition(
        alt.datum.nonfarm_change > 0,
        alt.value("steelblue"),  # The positive color
        alt.value("orange")  # The negative color
    ),
).properties(width=600)
