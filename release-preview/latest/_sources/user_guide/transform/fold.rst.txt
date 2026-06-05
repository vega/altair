.. currentmodule:: altair

.. _user-guide-fold-transform:

Fold
~~~~
The fold transform is, in short, a way to convert wide-form data to long-form
data directly without any preprocessing (see :ref:`data-long-vs-wide` for more
information). Fold transforms are the opposite of the :ref:`user-guide-pivot-transform`.

So, for example, if your data consist of multiple columns that record parallel
data for different categories, you can use the fold transform to encode based
on those categories:

.. altair-plot::

   import numpy as np
   import pandas as pd
   import altair as alt

   rand = np.random.RandomState(0)
   data = pd.DataFrame({
       'date': pd.date_range('2019-01-01', freq='D', periods=30),
       'A': rand.randn(30).cumsum(),
       'B': rand.randn(30).cumsum(),
       'C': rand.randn(30).cumsum(),
   })

   alt.Chart(data).transform_fold(
       ['A', 'B', 'C'],
   ).mark_line().encode(
       x='date:T',
       y='value:Q',
       color='key:N'
   )

Notice here that the fold transform essentially stacks all the values
from the specified columns into a single new field named ``"value"``,
with the associated names in a field named ``"key"``.

For an example of the fold transform in action, see :ref:`gallery_parallel_coordinates`.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_fold` method is built on the :class:`~FoldTransform`
class, which has the following options:

.. altair-object-table:: altair.FoldTransform
