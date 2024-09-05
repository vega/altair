"""
Line Chart with Arrows
----------------------
This example shows a simple line chart with two types of arrow annotations.
The Unicode character approach is simpler, 
while the line plus triangle :ref:`point mark <user-guide-point-marks>` allows for greater flexibility,
such as customizable arrowheads.
"""
# category: line charts
import altair as alt
import numpy as np
import pandas as pd


x = np.linspace(1,7)
data = pd.DataFrame({
    "x": x,
    "y": np.sin(x),
})

unicode_arrow_with_text = alt.layer(
    # Arrow
    alt.Chart().mark_text(size=60, align="left", baseline="bottom", fontWeight=100, angle=340).encode(
        x=alt.datum(2.8),
        y=alt.datum(-0.3),
        text=alt.datum("🠃")  # Any unicode symbol could be used instead
    ),
    # Text
    alt.Chart().mark_text(size=14, align="center", baseline="bottom").encode(
        x=alt.datum(1.8),
        y=alt.datum(-0.1),
        text=alt.datum("decreasing")
    )
)

mark_arrow_with_text = alt.layer(
    # Arrow line
    alt.Chart().mark_line(size=2).encode(
        x=alt.datum(5.4),
        y=alt.datum(-0.4),
        x2=alt.datum(5.9),
        y2=alt.datum(0)
    ),
    # Arrow head
    alt.Chart().mark_point(shape="triangle", filled=True, fillOpacity=1).encode(
        x=alt.datum(5.9),
        y=alt.datum(0),
        angle=alt.AngleValue(23),
        size=alt.SizeValue(100),
        color=alt.ColorValue("#000000")
    ),
    # Text
    alt.Chart().mark_text(size=14, align="center", baseline="bottom").encode(
        x=alt.datum(4.7),
        y=alt.datum(-0.3),
        text=alt.datum("increasing")
    ),
)

line_with_points = alt.Chart(data).mark_line(point=True).encode(
    x=alt.X("x"),
    y=alt.Y("y"),
)

line_with_points + unicode_arrow_with_text + mark_arrow_with_text
