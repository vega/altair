"""
Waterfall Chart
---------------
This example shows how to recreate a Vega-Lite implementation of a waterfall chart.
Original inspiration is from https://vega.github.io/vega-lite/examples/waterfall_chart.html
"""
# category: advanced calculations

import altair as alt
import pandas as pd

data = [
    {"label": "Begin", "amount": 4000},
    {"label": "Jan", "amount": 1707},
    {"label": "Feb", "amount": -1425},
    {"label": "Mar", "amount": -1030},
    {"label": "Apr", "amount": 1812},
    {"label": "May", "amount": -1067},
    {"label": "Jun", "amount": -1481},
    {"label": "Jul", "amount": 1228},
    {"label": "Aug", "amount": 1176},
    {"label": "Sep", "amount": 1146},
    {"label": "Oct", "amount": 1205},
    {"label": "Nov", "amount": -1388},
    {"label": "Dec", "amount": 1492},
    {"label": "End", "amount": 0},
]
source = pd.DataFrame(data)

# Define frequently referenced fields
amount = alt.datum.amount
label = alt.datum.label
window_lead_label = alt.datum.window_lead_label
window_sum_amount = alt.datum.window_sum_amount

# Define frequently referenced/long expressions
calc_prev_sum = alt.expr.if_(label == "End", 0, window_sum_amount - amount)
calc_amount = alt.expr.if_(label == "End", window_sum_amount, amount)
calc_text_amount = (
    alt.expr.if_((label != "Begin") & (label != "End") & calc_amount > 0, "+", "")
    + calc_amount
)

# The "base_chart" defines the transform_window, transform_calculate, and X axis
base_chart = alt.Chart(source).transform_window(
    window_sum_amount="sum(amount)",
    window_lead_label="lead(label)",
).transform_calculate(
    calc_lead=alt.expr.if_((window_lead_label == None), label, window_lead_label),
    calc_prev_sum=calc_prev_sum,
    calc_amount=calc_amount,
    calc_text_amount=calc_text_amount,
    calc_center=(window_sum_amount + calc_prev_sum) / 2,
    calc_sum_dec=alt.expr.if_(window_sum_amount < calc_prev_sum, window_sum_amount, ""),
    calc_sum_inc=alt.expr.if_(window_sum_amount > calc_prev_sum, window_sum_amount, ""),
).encode(
    x=alt.X("label:O", axis=alt.Axis(title="Months", labelAngle=0), sort=None)
)

color_coding = (
    alt.when((label == "Begin") | (label == "End"))
    .then(alt.value("#878d96"))
    .when(calc_amount < 0)
    .then(alt.value("#fa4d56"))
    .otherwise(alt.value("#24a148"))
)

bar = base_chart.mark_bar(size=45).encode(
    y=alt.Y("calc_prev_sum:Q", title="Amount"),
    y2=alt.Y2("window_sum_amount:Q"),
    color=color_coding,
)

# The "rule" chart is for the horizontal lines that connect the bars
rule = base_chart.mark_rule(xOffset=-22.5, x2Offset=22.5).encode(
    y="window_sum_amount:Q",
    x2="calc_lead",
)

# Add values as text
text_pos_values_top_of_bar = base_chart.mark_text(baseline="bottom", dy=-4).encode(
    text=alt.Text("calc_sum_inc:N"),
    y="calc_sum_inc:Q",
)
text_neg_values_bot_of_bar = base_chart.mark_text(baseline="top", dy=4).encode(
    text=alt.Text("calc_sum_dec:N"),
    y="calc_sum_dec:Q",
)
text_bar_values_mid_of_bar = base_chart.mark_text(baseline="middle").encode(
    text=alt.Text("calc_text_amount:N"),
    y="calc_center:Q",
    color=alt.value("white"),
)

alt.layer(
    bar,
    rule,
    text_pos_values_top_of_bar,
    text_neg_values_bot_of_bar,
    text_bar_values_mid_of_bar
).properties(
    width=800,
    height=450
)