"""
Scatter Plot with Image Marks
----------------------------
This example shows how to make a scatter plot using images as markers. 
"""
# category: scatter plots

import altair as alt
import pandas as pd

source = pd.DataFrame.from_records([
      {"x": 0.5, "y": 0.5, "img": "https://vega.github.io/vega-datasets/data/ffox.png"},
      {"x": 1.5, "y": 1.5, "img": "https://vega.github.io/vega-datasets/data/gimp.png"},
      {"x": 2.5, "y": 2.5, "img": "https://vega.github.io/vega-datasets/data/7zip.png"}
])

alt.Chart(source).mark_image(
    width=50, 
    height=50
).encode(
    x='x', 
    y='y', 
    url='img'
)
