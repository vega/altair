.. currentmodule:: altair

.. _user-guide-regression-transform:

Regression Transform
~~~~~~~~~~~~~~~~~~~~

The regression transform fits two-dimensional regression models to smooth and
predict data. This transform can fit multiple models for input data (one per group) 
and generates new data objects that represent points for summary trend lines.
Alternatively, this transform can be used to generate a set of objects containing
regression model parameters, one per group.

This transform supports parametric models for the following functional forms:

- linear (``linear``): *y = a + b * x*
- logarithmic (``log``): *y = a + b * log(x)*
- exponential (``exp``): * y = a * e^(b * x)*
- power (``pow``): *y = a * x^b*
- quadratic (``quad``): *y = a + b * x + c * x^2*
- polynomial (``poly``): *y = a + b * x + … + k * x^(order)*

All models are fit using ordinary least squares.
For non-parametric locally weighted regression, see the
:ref:`user-guide-loess-transform`.

Here is an example of a simple linear regression plotted on top of data:

.. altair-plot::

   import altair as alt
   import pandas as pd
   import numpy as np

   np.random.seed(42)
   x = np.linspace(0, 10)
   y = x - 5 + np.random.randn(len(x))

   df = pd.DataFrame({'x': x, 'y': y})

   chart = alt.Chart(df).mark_point().encode(
       x='x',
       y='y'
   )

   chart + chart.transform_regression('x', 'y').mark_line()

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_regression` method is built on the :class:`~RegressionTransform`
class, which has the following options:

.. altair-object-table:: altair.RegressionTransform
