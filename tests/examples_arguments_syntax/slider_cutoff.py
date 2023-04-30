"""
Slider Cutoff
=============
This example shows how to bind a variable parameter to a slider, and how to use the corresponding bound value to color data points.  This example is based on an example from the Altair 4 documentation for Interactions, in which the  interactivity was accomplished using a selection.  The version below has been simplified significantly through the use of a variable parameter.  Variable parameters were added in Altair 5.
"""
# category: interactive charts
import altair as alt
import pandas as pd
import numpy as np

rand = np.random.RandomState(42)

df = pd.DataFrame({
    'xval': range(100),
    'yval': rand.randn(100).cumsum()
})

slider = alt.binding_range(min=0, max=100, step=1)
cutoff = alt.param(bind=slider, value=50)

alt.Chart(df).mark_point().encode(
    x='xval',
    y='yval',
    color=alt.condition(
        alt.datum.xval < cutoff,
        alt.value('red'), alt.value('blue')
    )
).add_params(
    cutoff
)