"""
Faceted Area Chart
------------------
Multiple area subcharts, one for each company.
We also show filtering out one of the companies,
and sorting the companies in a custom order.
"""
# category: area charts
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).transform_filter(alt.datum.symbol != "GOOG").mark_area().encode(
    x="date:T",
    y="price:Q",
    color="symbol:N",
    row=alt.Row("symbol:N").sort(["MSFT", "AAPL", "IBM", "AMZN"]),
).properties(height=50, width=400)
