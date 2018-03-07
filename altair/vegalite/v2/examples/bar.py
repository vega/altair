"""
Simple Bar Chart
================
This example shows a basic bar chart created with Altair.
"""
# category: basic charts
from altair import Chart
import pandas as pd

data = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

chart = Chart(data).mark_bar().encode(
    x='a',
    y='b'
)
