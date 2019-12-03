"""
Polynomial Fit Plot with Regression Transform
=============================================
This example shows how to overlay data with multiple fitted polynomials using
the regression transform.
"""
# category: scatter plots

import numpy as np
import pandas as pd
import altair as alt

# Generate some random data
rng = np.random.RandomState(1)
x = rng.rand(40) ** 2
y = 10 - 1. / (x + 0.1) + rng.randn(40)
source = pd.DataFrame({'x': x, 'y': y})

# Define the degree and color of the polynomial fits
degree_list = [1, 3, 5]
color_list = ['#5276A7', '#F18727', '#E0575A']

base = alt.Chart(source).mark_circle(color='black').encode(
    alt.X('x'), alt.Y('y')
)

polynomial_fit = (base.transform_regression('x', 'y', method='poly', order=order)
                  .mark_line(color=color) 
                  for order, color in zip(degree_list, color_list))

alt.layer(base, *polynomial_fit)
