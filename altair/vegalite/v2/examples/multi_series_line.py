"""
Multi Series Line Chart
-----------------------

This example shows how to make a multi series line chart of the daily closing stock prices for AAPL, AMZN, GOOG, IBM, and MSFT between 2000 and 2010.
"""
# category: line charts
import altair as alt


stocks = alt.datasets.stocks()

alt.Chart(stocks).mark_line().encode(
    x='date',
    y='price',
    color='symbol'
)
