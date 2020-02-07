"""
Scatter Plot with LOESS Lines
-----------------------------
This example shows how to add a trend line to a scatter plot using 
the LOESS transform (LOcally Estimated Scatterplot Smoothing).
"""
# category: scatter plots

import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)

source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0),
                      columns=['A', 'B', 'C'], 
                      index=pd.RangeIndex(100, name='x')).reset_index()

base = alt.Chart(source).mark_circle(opacity=0.5).transform_fold(
    fold=['A', 'B', 'C'], 
    as_=['category', 'y']
).encode(
    alt.X('x:Q'), 
    alt.Y('y:Q'), 
    alt.Color('category:N')
)

base + base.transform_loess('x', 'y', groupby=['category']).mark_line(size=4)
