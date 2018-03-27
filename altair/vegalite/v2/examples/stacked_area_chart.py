"""
Stacked Area Chart
==================
This example shows how to make a stacked area chart using a dataset containing monthly casualty counts from the Crimean war. Note that the dataset is reshaped into a tidy format before plotting.
"""

import altair as alt
from vega_datasets import data
import pandas as pd

crimea = data.crimea()

crimea = pd.melt(crimea, id_vars=['date'],
                 value_vars=['disease', 'other', 'wounds'],
                 var_name='cause',
                 value_name='deaths')

chart = alt.Chart(crimea).mark_area().encode(
    x='date',
    y='sum(deaths)', 
    color='cause'
)
