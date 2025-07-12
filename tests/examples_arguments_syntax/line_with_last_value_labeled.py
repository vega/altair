"""
Line Chart with Last Value Labeled
----------------------------------
This chart shows a line chart with a label annotating the final value 
"""
# category: line charts
import altair as alt
from vega_datasets import data

# Import example data
source = data.stocks()

# Create a common chart object
# Use `transform_filter` to reduce the dataset to clarify our example. Not required.
chart = (
    alt.Chart(source)
    .transform_filter(alt.datum.symbol != "IBM")
    .encode(color=alt.Color("symbol", legend=None))
)

# Draw the line
line = chart.mark_line().encode(x="date:T", y="price:Q")

# Use the `argmax` aggregate to limit the dataset to the final value
label = chart.encode(
    x=alt.X("max(date):T"),
    y=alt.Y("price:Q", aggregate=alt.ArgmaxDef(argmax="date")),
    text="symbol",
)

# Create a text label
text = label.mark_text(align="left", dx=4)

# Create a circle annotation
circle = label.mark_circle()

# Draw the chart with all the layers combined
line + circle + text
