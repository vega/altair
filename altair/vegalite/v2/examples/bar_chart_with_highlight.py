"""
Bar Chart with Highlight
-----------------------
This example shows a Bar chart that highlights values beyond a threshold.
"""

import altair as alt

data = [
          {"Day": 1, "Value": 54.8},
          {"Day": 2, "Value": 112.1},
          {"Day": 3, "Value": 63.6},
          {"Day": 4, "Value": 37.6},
          {"Day": 5, "Value": 79.7},
          {"Day": 6, "Value": 137.9},
          {"Day": 7, "Value": 120.1},
          {"Day": 8, "Value": 103.3},
          {"Day": 9, "Value": 394.8},
          {"Day": 10, "Value": 199.5},
          {"Day": 11, "Value": 72.3},
          {"Day": 12, "Value": 51.1},
          {"Day": 13, "Value": 112.0},
          {"Day": 14, "Value": 174.5},
          {"Day": 15, "Value": 130.5}
        ]

data2 = [
    {"ThresholdValue": 300, "Threshold": "hazardous"}
    ]

source = alt.pd.DataFrame(data)
source2 = alt.pd.DataFrame(data2)

bar1 = alt.Chart(source).mark_bar().encode(
    x = 'Day:O',
    y = 'Value:Q')

bar2 = alt.Chart(source).mark_bar(color = "#e45755").encode(
    x = 'Day:O',
    y = 'baseline:Q',
    y2 = 'Value:Q')

bar2.transform = [alt.FilterTransform("datum.Value >= 300"),
          {"calculate": "300", "as": "baseline"}]

rule = alt.Chart(source2).mark_rule().encode(
    y = 'ThresholdValue:Q')

text = alt.Chart(source2).mark_text().encode(
    y = alt.Y('ThresholdValue:Q', axis = alt.Axis(title = 'PM2.5 Value')),
    text = 'Threshold:O'
    )

chart = bar1 + text + bar2 + bar2 + rule
