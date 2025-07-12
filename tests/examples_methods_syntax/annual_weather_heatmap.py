"""
Annual Weather Heatmap
----------------------
"""
# category: tables
import altair as alt
from vega_datasets import data

source = data.seattle_weather()

alt.Chart(source, title="Daily Max Temperatures (C) in Seattle, WA").mark_rect().encode(
    alt.X("date(date):O").title("Day").axis(format="%e", labelAngle=0),
    alt.Y("month(date):O").title("Month"),
    alt.Color("max(temp_max)").title(None),
    tooltip=[
        alt.Tooltip("monthdate(date)", title="Date"),
        alt.Tooltip("max(temp_max)", title="Max Temp"),
    ],
).configure_view(
    step=13,
    strokeWidth=0
).configure_axis(
    domain=False
)
