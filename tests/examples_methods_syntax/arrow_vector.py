"""
Arrow Vector
------------------------------
This example shows a basic vector plot use point mark ``triangle`` as shape,
other shape options can be found in :ref:`Point Mark<user-guide-point-marks>`.
"""
# category: case studies
import altair as alt
import numpy as np
import pandas as pd

vector1 = [0, 0, 3, -1]
vector2 = [0, 0, 2, 3]

v = pd.DataFrame([vector1, vector2], columns=['x1','y1','x2','y2'])

# calculate the vector
v['x_'] = v['x2'] - v["x1"]
v['y_'] = v['y2'] - v["y1"]

# calculate the angle between current vector and the default point mark direction (0,1)
# dot product = (x_,y_) dot (0,1) = y_
v["norm"] = np.sqrt(v['x_']**2 + v['y_']**2)
v["theta"] = np.degrees(np.arccos(v['y_']/v["norm"]))

lines = alt.Chart(v).mark_line().encode(
    alt.X("x1")
    .title('x')
    .scale(domain=(-4, 4)),
    alt.Y("y1")
    .title('y')
    .scale(domain=(-4, 4)),
    alt.X2("x2"),
    alt.Y2("y2")
)

wedge = alt.Chart(v).mark_point(shape="triangle", filled=True).encode(
    alt.X("x2"),
    alt.Y("y2"),
    alt.Angle("theta")
    .scale(domain=[0, 360]),
    alt.SizeValue(300),
    alt.ColorValue('#000000')
)

lines + wedge