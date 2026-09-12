"""
Change Series Colors with Color Inputs
======================================
This example shows how to bind HTML color inputs to parameters and use the
parameters as the range of a color scale so that readers can pick the color
of each series interactively.
"""

# :new:
# category: interactive charts
import altair as alt
import pandas as pd

source = pd.DataFrame(
    {
        "quarter": ["Q1", "Q2", "Q3", "Q4"] * 3,
        "revenue": [120, 145, 160, 190, 80, 95, 110, 140, 60, 75, 85, 100],
        "product": ["Hardware"] * 4 + ["Software"] * 4 + ["Services"] * 4,
    }
)

hardware_color = alt.param(
    name="hardware_color",
    value="#4c78a8",
    bind=alt.binding(input="color", name="Hardware color "),
)
software_color = alt.param(
    name="software_color",
    value="#f58518",
    bind=alt.binding(input="color", name="Software color "),
)
services_color = alt.param(
    name="services_color",
    value="#54a24b",
    bind=alt.binding(input="color", name="Services color "),
)

chart = (
    alt.Chart(source)
    .mark_line(point=True)
    .encode(
        x=alt.X("quarter:O"),
        y=alt.Y("revenue:Q"),
        color=alt.Color(
            "product:N",
            scale=alt.Scale(
                domain=["Hardware", "Software", "Services"],
                range=[hardware_color, software_color, services_color],
            ),
        ),
    )
    .add_params(hardware_color, software_color, services_color)
)

chart
