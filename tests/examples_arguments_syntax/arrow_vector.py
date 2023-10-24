"""
Arrow Vector
------------------------------
This example shows a basic vector plot using point mark ``triangle`` as shape,
other shape options can be found in :ref:`Point Mark<user-guide-point-marks>`.
"""
# category: line charts
import altair as alt
import numpy as np
import pandas as pd

vector1 = [0, 0, 3, -1]
vector2 = [0, 0, 2, 3]

v = pd.DataFrame([vector1, vector2], columns=["x1","y1","x2","y2"])

# calculate the vector
v["x_"] = v["x2"] - v["x1"]
v["y_"] = v["y2"] - v["y1"]

# calculate the angle between current vector and the default point mark direction (0,1)
# dot product = (x_,y_) dot (0,1) = y_
v["norm"] = np.sqrt(v["x_"]**2 + v["y_"]**2)
v["theta"] = np.degrees(np.arccos(v["y_"]/v["norm"] ))


lines = alt.Chart(v).mark_line().encode(
    x=alt.X("x1", scale=alt.Scale(domain=(-4, 4)), title="x"),
    y=alt.Y("y1", scale=alt.Scale(domain=(-4, 4)), title="y"),
    x2="x2",
    y2="y2"
)

wedge = alt.Chart(v).mark_point(shape="triangle", filled=True).encode(
    x="x2",
    y="y2",
    angle=alt.Angle("theta", scale=alt.Scale(domain=[0, 360])),
    size=alt.value(300),
    color=alt.value("#000000")
)

lines + wedge
