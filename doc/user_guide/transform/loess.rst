.. currentmodule:: altair

.. _user-guide-loess-transform:

LOESS Transform
~~~~~~~~~~~~~~~
The LOESS transform (LOcally Estimated Scatterplot Smoothing) uses a
locally-estimated regression  to produce a trend line.
LOESS performs a sequence of local weighted regressions over a sliding
window of nearest-neighbor points. For standard parametric regression options,
see the :ref:`user-guide-regression-transform`.

Here is an example of using LOESS to smooth samples from a Gaussian random walk:

.. altair-plot::

   import altair as alt
   import pandas as pd
   import numpy as np
   
   np.random.seed(42)
   
   df = pd.DataFrame({
       'x': range(100),
       'y': np.random.randn(100).cumsum()
   })
   
   chart = alt.Chart(df).mark_point().encode(
       x='x',
       y='y'
   )
   
   chart + chart.transform_loess('x', 'y').mark_line()


Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_loess` method is built on the
:class:`~LoessTransform` class, which has the following options:

.. altair-object-table:: altair.LoessTransform
