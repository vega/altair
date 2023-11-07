"""
Line Chart with Arrows
----------------------
This example shows a simple line chart with arrow annotations.
It utilizes a Unicode character for quick arrow insertion, 
and employs the triangle :ref:`point mark <user-guide-point-marks>` for customizable arrowheads.
The Unicode method offers ease of use, while the triangle point mark provides greater flexibility.
"""
# category: line charts
import numpy as np
import pandas as pd
import altair as alt

x = np.linspace(1,7)
y = np.sin(x)

data = pd.DataFrame({
            "x": x,
            "y": y,
        })

alt.layer(
    alt.Chart(data).mark_line(point=True,tooltip=True).encode(
        x=alt.X("x").title("x"),
        y=alt.Y("y").title("y"),
    ),
     alt.Chart().mark_text(size=14, align="center", baseline="bottom").encode(
        x=alt.datum(1.8),
        y=alt.datum(-0.1),
        text=alt.datum("decreasing")
    ),
    alt.Chart().mark_text(size=14, align="center", baseline="bottom").encode(
        x=alt.datum(4.7),
        y=alt.datum(-0.3),
        text=alt.datum("increasing")
    ),
    # unicode arrow
    alt.Chart().mark_text(size=60, align="left", baseline="bottom", fontWeight=100, angle=340).encode(
        x=alt.datum(2.8),
        y=alt.datum(-0.3),
        text=alt.datum("🠃")
    ),
    # arrow line
    alt.Chart().mark_line(size=2).encode(
        x=alt.datum(5.4),
        y=alt.datum(-0.4),
        x2=alt.datum(6),
        y2=alt.datum(0)
    ),
    # arrow head
    alt.Chart().mark_point(shape="triangle", filled=True, fillOpacity=1).encode(
        x=alt.datum(6),
        y=alt.datum(0),
        angle=alt.AngleValue(23),
        size=alt.SizeValue(100),
        color=alt.ColorValue("#000000")
    )
)





