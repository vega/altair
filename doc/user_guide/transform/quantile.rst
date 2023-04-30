.. currentmodule:: altair

.. _user-guide-quantile-transform:

Quantile
~~~~~~~~
The quantile transform calculates empirical `quantile <https://en.wikipedia.org/wiki/Quantile>`_
values for input data. If a groupby parameter is provided, quantiles are estimated
separately per group. Among other uses, the quantile transform is useful for creating
`quantile-quantile (Q-Q) plots <https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot>`_.

Here is an example of a quantile plot of normally-distributed data:

.. altair-plot::

   import altair as alt
   import pandas as pd
   import numpy as np

   np.random.seed(42)
   df = pd.DataFrame({'x': np.random.randn(200)})

   alt.Chart(df).transform_quantile(
       'x', step=0.01
   ).mark_point().encode(
       x='prob:Q',
       y='value:Q'
   )

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_quantile` method is built on the :class:`~QuantileTransform`
class, which has the following options:

.. altair-object-table:: altair.QuantileTransform
