"""
Steam and Leaf Plot
-------------------
This example shows how to make a steam and leaf plot.
"""

import altair as alt
import pandas as pd
import numpy as np
np.random.seed(42)

# Generating random data
original_data = pd.DataFrame({'samples':np.array(np.random.normal(50, 15, 100), dtype=np.int)})

# Splitting steam and leaf
original_data['stem'] = original_data['samples'].apply(lambda x: str(x)[:-1])
original_data['leaf'] = original_data['samples'].apply(lambda x: str(x)[-1])

original_data.sort_values(by=['stem', 'leaf'], inplace=True)
original_data.reset_index(inplace=True, drop=True)

# Determining leaf position
get_position = lambda x: 1 + pd.Series(range(len(x)))

original_data['position'] = original_data.groupby('stem')\
                                         .apply(get_position)\
                                         .reset_index(drop=True)

# Creating stem and leaf plot
chart = alt.Chart(original_data).mark_text(
    align='left',
    baseline='middle',
    dx=-5
).encode(
    alt.X('position:Q',
        axis=alt.Axis(title='', ticks=False,labels=False,grid=False)
    ),
    alt.Y('stem:N', axis=alt.Axis(title='', tickSize=0)),
    text = 'leaf:N'
).configure_axis(
    labelFontSize=20
).configure_text(
    fontSize=20
)
