"""
Multi Series Line Chart Layered With Rule Aggregate Lines
---------------------------------------------------------
This example shows how to make a multi series line chart of the daily closing stock prices for AAPL, AMZN, GOOG, IBM, and MSFT between 2000 and 2010.
"""

import altair as alt
from vega_datasets import data

stocks = data.stocks()

line = alt.Chart(stocks).mark_line().encode(
    x = 'date',
    y = 'price',
    color = 'symbol'
).properties(width = 800,
            title = "Daily closing prices with their aggregate prices").interactive()

rule = alt.Chart(stocks).mark_rule().encode(
    y = alt.Y('average(price)', ),
    color = 'symbol',
    size = alt.SizeValue(2)
)

chart = (line + rule)
