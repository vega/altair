"""
Line Chart with Interpolation
-----------------------------
This chart shows a line chart with the path interpolated. A full list of interpolation methods is available `in the documentation <https://altair-viz.github.io/user_guide/generated/core/altair.LineConfig.html?highlight=interpolate#altair-lineconfig>`_.
"""
# category: line charts
import altair as alt
from vega_datasets import data

source = data.stocks()

alt.Chart(source).mark_line(interpolate="monotone").encode(
    x="date:T",
    y="price:Q",
    color="symbol:N"
)
