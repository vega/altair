"""
Waterfall Chart
-------------
This example shows how to recreate a vega lite implementation of a waterfall chart.
Original inspiration is from https://vega.github.io/vega-lite/examples/waterfall_chart.html
"""
# category: advanced calculations

import altair as alt
from altair import datum
import pandas as pd




## Compared to the original example, we have to add some more fields to help with color labeling and ordering the bars
the_data=[
      {"label": "Begin", "amount": 4000, "order":0, "color_label":'Begin'},
      {"label": "Jan", "amount": 1707, "order":1, "color_label":'+'},
      {"label": "Feb", "amount": -1425, "order":2, "color_label":'-'},
      {"label": "Mar", "amount": -1030, "order":3, "color_label":'-'},
      {"label": "Apr", "amount": 1812, "order":4, "color_label":'+'},
      {"label": "May", "amount": -1067, "order":5, "color_label":'-'},
      {"label": "Jun", "amount": -1481, "order":6, "color_label":'-'},
      {"label": "Jul", "amount": 1228, "order":7, "color_label":'+'},
      {"label": "Aug", "amount": 1176, "order":8, "color_label":'+'},
      {"label": "Sep", "amount": 1146, "order":9, "color_label":'+'},
      {"label": "Oct", "amount": 1205, "order":10, "color_label":'+'},
      {"label": "Nov", "amount": -1388, "order":11, "color_label":'-'},
      {"label": "Dec", "amount": 1492, "order":12, "color_label":'+'},
      {"label": "End", "amount": 0, "order":13, "color_label":'End'}
    ]
df=pd.DataFrame(the_data)


## This is a workaround to enable 3 different colors for the bars
color_coding=alt.Color(
    'color_label'
    , scale=alt.Scale(
        domain=['Begin','End','+','-']
        , range=['#878d96', '#878d96', '#24a148', '#fa4d56']
    )
    , legend=None
)
## This is where you use the "order" field in the_data to define the sort order
sort_x_by_order=alt.EncodingSortField(field="order", op="max", order='ascending')


## The "base_chart" defines the transform_window, transform_calculate, and X axis
base_chart=alt.Chart(df).transform_window(
    sort=[{'field': 'order'}],
    frame=[None, 0],
    window_sum_amount='sum(amount)',
    window_lead_label='lead(label)'
).transform_calculate(
    calc_lead="datum.window_lead_label === null ? datum.label : datum.window_lead_label"
    , calc_prev_sum="datum.label === 'End' ? 0 : datum.window_sum_amount - datum.amount"
    , calc_amount="datum.label === 'End' ? datum.window_sum_amount : datum.amount"
    , calc_text_amount="(datum.label !== 'Begin' && datum.label !== 'End' && datum.calc_amount > 0 ? '+' : '') + datum.calc_amount"
    , calc_center="(datum.window_sum_amount + datum.calc_prev_sum) / 2"
    , calc_sum_dec="datum.window_sum_amount < datum.calc_prev_sum ? datum.window_sum_amount : ''"
    , calc_sum_inc="datum.window_sum_amount > datum.calc_prev_sum ? datum.window_sum_amount : ''"
).encode(
    x=alt.X('label:O', title='Months', sort=sort_x_by_order)
)

bar=base_chart.mark_bar().encode(
    y=alt.Y('calc_prev_sum:Q',title='Amount')
    , y2=alt.Y2('window_sum_amount:Q')
    , color=color_coding
)

## the "rule" chart is for the lines that connect bars each month
rule=base_chart.mark_rule(color='#404040', opacity=0.9, strokeWidth=2, xOffset=-25, x2Offset=25, strokeDash=[3,3]).encode(
    #draw a horizontal line where the height (y) is at window_sum_amount, and the ending width (x2) is at calc_lead
    y='window_sum_amount:Q'
    , x2='calc_lead'
)

## create text values to display
text_pos_values_top_of_bar=base_chart.mark_text(baseline='bottom', dy=-4).encode(
    text=alt.Text('calc_sum_inc:N')
    , y='calc_sum_inc:Q'
)
text_neg_values_bot_of_bar=base_chart.mark_text(baseline='top', dy=4).encode(
    text=alt.Text('calc_sum_dec:N')
    , y='calc_sum_dec:Q'
)
text_bar_values_mid_of_bar=base_chart.mark_text(baseline='middle').encode(
    text=alt.Text('calc_text_amount:N')
    , y='calc_center:Q'
     , color=alt.condition("datum.label ==='Begin'||datum.label === 'End'", alt.value("white"), alt.value("white"))
)

## layer everything together
(bar+rule+text_pos_values_top_of_bar+text_neg_values_bot_of_bar+text_bar_values_mid_of_bar).properties(width=800, height=450)
