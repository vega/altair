# /// script
# requires-python = ">=3.11"
# dependencies = ["altair", "pandas"]
#
# [tool.marimo.display]
# cell_output = "above"
# ///
"""
Interactive Pie Chart
---------------------
This example shows how to highlight a pie slice by selecting its category in the
legend. Hover over a slice to see its value.
"""
# :new:
# category: circular plots

import altair as alt
import pandas as pd

source = pd.DataFrame(
    {
        "category": ["Rent", "Food", "Transport", "Utilities", "Other"],
        "value": [950, 420, 180, 150, 300],
    }
)

selection = alt.selection_point(fields=["category"], bind="legend")

base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True),
    color=alt.Color("category:N", legend=alt.Legend(title="Expense")),
    opacity=alt.when(selection).then(alt.value(1)).otherwise(alt.value(0.2)),
    tooltip=[
        alt.Tooltip("category:N", title="Expense"),
        alt.Tooltip("value:Q", title="Monthly amount", format=","),
    ],
)

pie = base.mark_arc(outerRadius=110)
labels = base.mark_text(radius=132, size=13).encode(text="category:N")

chart = (pie + labels).add_params(selection)
chart
