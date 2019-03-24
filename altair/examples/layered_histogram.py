"""
Layered Histogram
=================
This example shows how to use opacity to make a layered histogram in Altair.
"""
# category: histograms
import pandas as pd
import altair as alt
import numpy as np
np.random.seed(42)

# Generating Data
source = pd.DataFrame({'Trial A': np.random.normal(0, 0.8, 1000),
                   'Trial B': np.random.normal(-2, 1, 1000),
                   'Trial C': np.random.normal(3, 2, 1000)})

# Tidying Data
source = pd.melt(
    source,
    id_vars=source.index.name,
    value_vars=source.columns,
    var_name='Experiment',
    value_name='Measurement'
)

alt.Chart(source).mark_area(
    opacity=0.3,
    interpolate='step'
).encode(
    alt.X('Measurement', bin=alt.Bin(maxbins=100)),
    alt.Y('count()', stack=None),
    alt.Color(
        'Experiment',
        scale=alt.Scale(range=['#0000ff', '#008000', '#ff0000'])
    )
)
