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

opacity = alt.when(selection).then(alt.value(1)).otherwise(alt.value(0.2))

base = alt.Chart(source).encode(
    alt.Theta("value:Q").stack(True),
    alt.Color("category:N").legend(alt.Legend(title="Expense")),
    alt.Tooltip("category:N").title("Expense"),
    alt.Tooltip("value:Q").title("Monthly amount").format(","),
).encode(opacity=opacity)


pie = base.mark_arc(outerRadius=110)
labels = base.mark_text(radius=132, size=13).encode(alt.Text("category:N"))

chart = (pie + labels).add_params(selection)
chart
