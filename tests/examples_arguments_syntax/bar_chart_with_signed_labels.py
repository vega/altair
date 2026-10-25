# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Horizontal Bar Chart with Signed Value Labels.
==============================================

Place a label to the left of a negative bar, or to the right of a
non-negative bar, without placing text inside the bars.
"""

# :new:
# category: bar charts
import pandas as pd

import altair as alt

source = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D", "E"],
        "value": [-28, 55, -33, 91, 0],
    }
)

base = alt.Chart(source).encode(
    x=alt.X("value:Q", scale=alt.Scale(padding=24), title="Change"),
    y=alt.Y("category:N", sort=None),
)

bars = base.mark_bar().encode(
    color=alt.condition(
        alt.datum.value < 0, alt.value("orange"), alt.value("steelblue")
    )
)

positive_labels = (
    base.transform_filter(alt.datum.value >= 0)
    .mark_text(align="left", dx=5)
    .encode(text="value:Q")
)
negative_labels = (
    base.transform_filter(alt.datum.value < 0)
    .mark_text(align="right", dx=-5)
    .encode(text="value:Q")
)

chart = (bars + positive_labels + negative_labels).properties(width=450, height=200)
chart  # noqa: B018
