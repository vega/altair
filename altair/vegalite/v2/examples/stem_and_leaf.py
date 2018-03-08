"""
Steam and Leaf Plot
-------------------
This example shows how to make a steam and leaf plot. 
"""

import altair as alt
import pandas as pd
import numpy as np
np.random.seed(42)

# Generating Random Data
original_data = pd.DataFrame({'samples':np.array(np.random.normal(50, 15, 100), dtype=np.int)})

# Splitting Steam and Leaf
original_data['stem'] = original_data['samples'].apply(lambda x: str(x)[:-1])
original_data['leaf'] = original_data['samples'].apply(lambda x: str(x)[-1])

# Grouping Leafs for each Stem
grouped_data = pd.DataFrame(columns=['stem', 'leaf'])
for key, group in original_data.groupby('stem'):
    grouped_data = grouped_data.append({'stem':key,
                                        'leaf': ''.join(group['leaf'].sort_values())},
                                        ignore_index=True)

# Plotting Stems and Leafs 
chart = alt.Chart(grouped_data).mark_text(align='left', baseline='middle',dx=-40).encode(
    y = alt.Y('stem', axis=alt.Axis(title='', tickSize=0)), 
    text = 'leaf'
).properties(width=400).configure_axis(labelFontSize=20).configure_text(fontSize=20)