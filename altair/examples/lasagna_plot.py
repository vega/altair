"""
Lasagna Plot (Dense Time-Series Heatmap)
------------
"""
# category: tables
import altair as alt
from vega_datasets import data

source = data.stocks()

color_condition = alt.condition(
    "month(datum.value) == 1 && date(datum.value) == 1",
    alt.value("black"),
    alt.value(None),
)

alt.Chart(source, width=300, height=100).transform_filter(
    alt.datum.symbol != "GOOG"
).mark_rect().encode(
    x=alt.X(
        "yearmonthdate(date):O",
        axis=alt.Axis(
            format="%Y",
            labelAngle=0,
            labelOverlap=False,
            labelColor=color_condition,
            tickColor=color_condition,
        ),
        title="Time",
    ),
    y=alt.Y("symbol:N", title=None),
    color=alt.Color("sum(price)", title="Price"),
)
