'''
Trellis Area Sort Chart
-----------------------
This example shows small multiples of an area chart.
Stock prices of four large companies 
sorted by `['MSFT', 'AAPL', 'IBM', 'AMZN']`
'''
# category: area charts
import altair as alt
from altair.expr import datum
from vega_datasets import data


alt.Chart(data.stocks.url).transform_filter(
    datum.symbol != 'GOOG'
).mark_area().encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
    row=alt.Row('symbol:N', sort=['MSFT', 'AAPL', 'IBM', 'AMZN']
    )
).properties(height=50, width=400)