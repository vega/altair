"""
Polynomial Fit Plot
===================
This example shows how to overlay data with a fitted polynomial
"""
# category: scatter plots
import numpy as np
import pandas as pd
import altair as alt

# Generate some random data
rng = np.random.RandomState(1)
x = rng.rand(40) ** 2
y = 10 - 1. / (x + 0.1) + rng.randn(40)
df = pd.DataFrame({'x': x, 'y': y})

# Define the degree of the polynomial fit
degree_list = [1, 3, 5]

# Build a dataframe with the fitted data
poly_data = pd.DataFrame({'xfit': np.linspace(df['x'].min(), df['x'].max(), 500)})

for degree in degree_list:
    poly_data[str(degree)] = np.poly1d(np.polyfit(df['x'], df['y'], degree))(poly_data['xfit'])

# Tidy the dataframe so 'degree' is a variable
poly_data = pd.melt(poly_data,
                    id_vars=['xfit'],
                    value_vars=[str(deg) for deg in degree_list],
                    var_name='degree', value_name='yfit')

# Plot the data points on an interactive axis
points = alt.Chart(df).mark_circle(color='black').encode(
    x=alt.X('x', axis=alt.Axis(title='x')),
    y=alt.Y('y', axis=alt.Axis(title='y')),
).interactive()

# Plot the best fit polynomials
polynomial_fit = alt.Chart(poly_data).mark_line().encode(
    x='xfit',
    y='yfit',
    color='degree'
)

points + polynomial_fit
