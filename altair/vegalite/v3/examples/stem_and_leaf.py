"""
Stem and Leaf Plot
------------------
This example shows how to make a stem and leaf plot.
"""
# category: other charts
import altair as alt
import pandas as pd
import numpy as np
np.random.seed(42)

# Generating random data
df = pd.DataFrame({'samples': np.random.normal(50, 15, 100).astype(int).astype(str)})

# Splitting stem and leaf
df['stem'] = df['samples'].str[:-1]
df['leaf'] = df['samples'].str[-1]

df = df.sort_values(by=['stem', 'leaf'])

# Determining leaf position
df['position'] = df.groupby('stem').cumcount().add(1)

# Creating stem and leaf plot
alt.Chart(df).mark_text(
    align='left',
    baseline='middle',
    dx=-5
).encode(
    alt.X('position:Q',
        axis=alt.Axis(title='', ticks=False, labels=False, grid=False)
    ),
    alt.Y('stem:N', axis=alt.Axis(title='', tickSize=0)),
    text='leaf:N'
).configure_axis(
    labelFontSize=20
).configure_text(
    fontSize=20
)
