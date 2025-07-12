"""
Polar Bar Chart
---------------
This example shows how to make a polar bar chart using ``mark_arc``.
This could also have been called a "pie chart with axis labels",
but is more commonly referred to as a polar bar chart.
The axis lines are created using pie charts with only the stroke visible.
"""
# category: circular plots

import math
import altair as alt
import pandas as pd

source = pd.DataFrame({
    "hour": range(24),
    "observations": [2, 2, 2, 2, 2, 3, 4, 4, 8, 8, 9, 7, 5, 6, 8, 8, 7, 7, 4, 3, 3, 2, 2, 2]
})

polar_bars = alt.Chart(source).mark_arc(stroke='white', tooltip=True).encode(
    theta=alt.Theta("hour:O"),
    radius=alt.Radius('observations', scale=alt.Scale(type='linear')),
    radius2=alt.datum(1),
)

# Create the circular axis lines for the number of observations
axis_rings = alt.Chart(pd.DataFrame({"ring": range(2, 11, 2)})).mark_arc(stroke='lightgrey', fill=None).encode(
    theta=alt.value(2 * math.pi),
    radius=alt.Radius('ring', stack=False)
)
axis_rings_labels = axis_rings.mark_text(color='grey', radiusOffset=5, align='left').encode(
    text="ring",
    theta=alt.value(math.pi / 4)
)

# Create the straight axis lines for the time of the day
axis_lines = alt.Chart(pd.DataFrame({
    "radius": 10,
    "theta": math.pi / 2,
    'hour': ['00:00', '06:00', '12:00', '18:00']
})).mark_arc(stroke='lightgrey', fill=None).encode(
    theta=alt.Theta('theta', stack=True),
    radius=alt.Radius('radius'),
    radius2=alt.datum(1),
)
axis_lines_labels = axis_lines.mark_text(
        color='grey',
        radiusOffset=5,
        thetaOffset=-math.pi / 4,
        # These adjustments could be left out with a larger radius offset, but they make the label positioning a bit cleaner
        align=alt.expr('datum.hour == "18:00" ? "right" : datum.hour == "06:00" ? "left" : "center"'),
        baseline=alt.expr('datum.hour == "00:00" ? "bottom" : datum.hour == "12:00" ? "top" : "middle"'),
    ).encode(text="hour")

alt.layer(
    axis_rings,
    polar_bars,
    axis_rings_labels,
    axis_lines,
    axis_lines_labels,
    title=['Observations throughout the day', '']
)
