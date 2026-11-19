"""
Grouped Bar Chart with xOffset and overlapping bars
---------------------------------------------------
Like :ref:`gallery_grouped_bar_chart2`, this example shows a grouped bar chart using the ``xOffset`` encoding channel, but in this example the bars are partly overlapping within each group.
"""
# category: bar charts
import altair as alt
import pandas as pd

source = pd.DataFrame(
    {
        "category": list("AABBCC"),
        "group": list("xyxyxy"),
        "value": [0.1, 0.6, 0.7, 0.2, 0.6, 0.1],
    }
)

base = alt.Chart(source, width=alt.Step(12)).encode(
    x="category:N",
    y="value:Q",
    xOffset=alt.XOffset("group:N").scale(paddingOuter=0.5),
)

alt.layer(
    base.mark_bar(size=20, stroke="white", fillOpacity=0.9).encode(fill="group:N"),
    base.mark_text(dy=-5).encode(text="value:Q"),
)