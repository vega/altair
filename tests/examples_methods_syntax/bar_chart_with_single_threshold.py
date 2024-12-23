"""
Bar Chart Highlighting Values beyond a Threshold
------------------------------------------------
This example shows a bar chart highlighting values beyond a threshold.
"""
# category: bar charts
import pandas as pd
import altair as alt

source = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
    "Value": [55, 112, 65, 38, 80, 138, 120, 103, 395, 200, 72, 51, 112, 175, 131]
})
threshold = 300

bars = alt.Chart(source).mark_bar(color="steelblue").encode(
    x="Day:O",
    y="Value:Q",
)

highlight = bars.mark_bar(color="#e45755").encode(
    y2=alt.Y2(datum=threshold)
).transform_filter(
    alt.datum.Value > threshold
)

rule = alt.Chart().mark_rule().encode(
    y=alt.Y(datum=threshold)
)

label = rule.mark_text(
    x="width",
    dx=-2,
    align="right",
    baseline="bottom",
    text="hazardous"
)

(bars + highlight + rule + label)