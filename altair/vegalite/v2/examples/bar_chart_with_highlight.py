"""
Bar Chart with Highlight
------------------------
This example shows a Bar chart that highlights values beyond a threshold.
"""
# category: bar charts
import altair as alt
import pandas as pd

data = pd.DataFrame({"Day": range(1, 16),
                     "Value": [54.8, 112.1, 63.6, 37.6, 79.7, 137.9, 120.1, 103.3,
                               394.8, 199.5, 72.3, 51.1, 112.0, 174.5, 130.5]})

data2 = pd.DataFrame([{"ThresholdValue": 300, "Threshold": "hazardous"}])

bar1 = alt.Chart(data).mark_bar().encode(
    x='Day:O',
    y='Value:Q'
)

bar2 = alt.Chart(data).mark_bar(color="#e45755").encode(
    x='Day:O',
    y='baseline:Q',
    y2='Value:Q'
).transform_filter(
    "datum.Value >= 300"
).transform_calculate(
    "baseline", "300"
)

rule = alt.Chart(data2).mark_rule().encode(
    y='ThresholdValue:Q'
)

text = alt.Chart(data2).mark_text(
    align='left', dx=215, dy=-5
).encode(
    alt.Y('ThresholdValue:Q', axis=alt.Axis(title='PM2.5 Value')),
    text=alt.value('hazardous')
)

bar1 + text + bar2 + rule
