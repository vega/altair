"""
Multi-Line Tooltip (Standard)
=============================
This example shows how to add a standard tooltip to the same chart 
as in :ref:`gallery_multiline_tooltip`. You can find another example
using this approach in the documentation on the :ref:`user-guide-pivot-transform` transformation.
"""
# category: interactive charts
import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)
columns = ["A", "B", "C"]
source = pd.DataFrame(
    np.cumsum(np.random.randn(100, 3), 0).round(2),
    columns=columns, index=pd.RangeIndex(100, name="x"),
)
source = source.reset_index().melt("x", var_name="category", value_name="y")

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection_point(nearest=True, on="pointerover", 
                              fields=["x"], empty=False)

# The basic line
line = alt.Chart(source).mark_line(interpolate="basis").encode(
    x="x:Q",
    y="y:Q",
    color="category:N"
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw a rule at the location of the selection
rules = alt.Chart(source).transform_pivot(
    "category",
    value="y",
    groupby=["x"]
).mark_rule(color="gray").encode(
    x="x:Q",
    opacity=alt.condition(nearest, alt.value(0.3), alt.value(0)),
    tooltip=[alt.Tooltip(c, type="quantitative") for c in columns],
).add_params(nearest)


# Put the five layers into a chart and bind the data
alt.layer(
    line, points, rules
).properties(
    width=600, height=300
)