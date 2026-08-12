"""
Repeated Density Estimates
--------------------------
Density estimates for each measurement of penguins.
This is what we call a "repeated" plot, with one subplot
for each measurement type. All measurements are in millimeters,
making them directly comparable on a shared x-axis.
"""
# category: distributions

import altair as alt
from altair.datasets import data

source = data.penguins()

alt.Chart(source).transform_fold(
    [
        "Beak Length (mm)",
        "Beak Depth (mm)",
        "Flipper Length (mm)",
    ],
    as_=["Measurement Type", "value"],
).transform_density(
    density="value",
    groupby=["Measurement Type"]
).mark_area().encode(
    alt.X("value:Q"),
    alt.Y("density:Q"),
    alt.Row("Measurement Type:N").header(labelAngle=0, labelAlign="left")
).properties(
    width=300,
    height=50
)
