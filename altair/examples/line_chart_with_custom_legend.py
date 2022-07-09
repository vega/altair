"""
Line Chart with Custom Legend
-----------------------------
This example uses the argmax aggregation function in order to create a custom
legend for a line chart.
"""
# category: line charts
import altair as alt
from vega_datasets import data


source = data.stocks()

base = (
    alt.Chart(source)
    .transform_filter("datum.symbol !== 'IBM'")
    .encode(color=alt.Color("symbol", legend=None))
    .properties(width=500)
)

line = base.mark_line().encode(x="date", y="price")


last_price = (
    base.mark_circle()
    .transform_aggregate(last_date="argmax(date)", groupby=["symbol"])
    .encode(x=alt.X("last_date['date']:T"), y=alt.Y("last_date['price']:Q"))
)

company_name = last_price.mark_text(align="left", dx=4).encode(text="symbol")

chart = (line + last_price + company_name).encode(
    x=alt.X(title="date"),
    y=alt.Y(title="price"),
)

chart
