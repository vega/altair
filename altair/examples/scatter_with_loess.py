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

source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
                    columns=['A', 'B', 'C'], index=pd.RangeIndex(100, name='x'))
source = source.reset_index().melt('x', var_name='category', value_name='y')

base = alt.Chart(source).mark_circle(opacity=0.5).encode(
    alt.X('x'), 
    alt.Y('y'), 
    alt.Color('category')
)

base + base.transform_loess('x', 'y', groupby=['category']).mark_line(size=4)
