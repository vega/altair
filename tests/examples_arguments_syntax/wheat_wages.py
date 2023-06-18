"""
Wheat and Wages
---------------
A recreation of William Playfair's classic chart visualizing
the price of wheat, the wages of a mechanic, and the reigning British monarch.

This is a more polished version of the simpler chart in :ref:`gallery_bar_and_line_with_dual_axis`.
"""
# category: case studies
import altair as alt
import pandas as pd
from vega_datasets import data


base_wheat = alt.Chart(data.wheat.url).transform_calculate(year_end="+datum.year + 5")

base_monarchs = alt.Chart(data.monarchs.url).transform_calculate(
    offset="((!datum.commonwealth && datum.index % 2) ? -1: 1) * 2 + 95",
    off2="((!datum.commonwealth && datum.index % 2) ? -1: 1) + 95",
    y="95",
    x="+datum.start + (+datum.end - +datum.start)/2",
)

bars = base_wheat.mark_bar(fill="#aaa", stroke="#999").encode(
    x=alt.X("year:Q", bin="binned", axis=alt.Axis(format="d", tickCount=5)).scale(
        zero=False
    ),
    y=alt.Y("wheat:Q", axis=alt.Axis(zindex=1)),
    x2=alt.X2("year_end"),
)

section_data = pd.DataFrame(
    [
        {"year": 1600},
        {"year": 1650},
        {"year": 1700},
        {"year": 1750},
        {"year": 1800},
    ]
)

section_line = (
    alt.Chart(section_data)
    .mark_rule(stroke="#000", strokeWidth=0.6, opacity=0.7)
    .encode(x=alt.X("year"))
)

area = base_wheat.mark_area(color="#a4cedb", opacity=0.7).encode(
    x=alt.X("year:Q"), y=alt.Y("wages:Q")
)

area_line_1 = area.mark_line(color="#000", opacity=0.7)
area_line_2 = area.mark_line(yOffset=-2, color="#EE8182")

top_bars = base_monarchs.mark_bar(stroke="#000").encode(
    x=alt.X("start:Q"),
    x2=alt.X2("end"),
    y=alt.Y("y:Q"),
    y2=alt.Y2("offset"),
    fill=alt.Fill(
        "commonwealth:N", legend=None, scale=alt.Scale(range=["black", "white"])
    ),
)

top_text = base_monarchs.mark_text(yOffset=14, fontSize=9, fontStyle="italic").encode(
    x=alt.X("x:Q"), y=alt.Y("off2:Q"), text=alt.Text("name:N")
)

(
    (bars + section_line + area + area_line_1 + area_line_2 + top_bars + top_text)
    .properties(width=900, height=400)
    .configure_axis(title=None, gridColor="white", gridOpacity=0.25, domain=False)
    .configure_view(stroke="transparent")
)
