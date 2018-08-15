"""
Line Chart with Layered Aggregates
----------------------------------
This example shows how to make a multi series line chart of the daily closing
stock prices for AAPL, AMZN, GOOG, IBM, and MSFT between 2000 and 2010, along
with a layered rule showing the average values.
"""
# category: line charts
import altair as alt
from vega_datasets import data

stocks = data.stocks()

line = alt.Chart(stocks).mark_line().encode(
    x='date',
    y='price',
    color='symbol'
).properties(
    width=600,
    title="Daily closing prices with their aggregate prices"
).interactive(bind_y=False)

rule = alt.Chart(stocks).mark_rule().encode(
    alt.Y('average(price)'),
    color='symbol',
    size=alt.value(2)
)

line + rule
