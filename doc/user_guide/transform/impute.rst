.. currentmodule:: altair

.. _user-guide-impute-transform:

Impute
~~~~~~
The impute transform allows you to fill-in missing entries in a dataset.
As an example, consider the following data, which includes missing values
that we filter-out of the long-form representation (see :ref:`data-long-vs-wide`
for more on this):

.. altair-plot::
   :output: repr

   import numpy as np
   import pandas as pd

   data = pd.DataFrame({
       't': range(5),
       'x': [2, np.nan, 3, 1, 3],
       'y': [5, 7, 5, np.nan, 4]
   }).melt('t').dropna()
   data

Notice the result: the ``x`` series has no entry at ``t=1``, and the ``y``
series has a missing entry at ``t=3``. If we use Altair to visualize this
data directly, the line skips the missing entries:

.. altair-plot::

   import altair as alt

   raw = alt.Chart(data).mark_line(point=True).encode(
       x=alt.X('t:Q'),
       y='value:Q',
       color='variable:N'
   )
   raw

This is not always desirable, because (particularly for a line plot with
no points) it can imply the existence of data that is not there.

Impute via Encodings
^^^^^^^^^^^^^^^^^^^^
To address this, you can use an impute argument to the encoding channel.
For example, we can impute using a constant value (we'll show the raw chart
lightly in the background for reference):

.. altair-plot::

   background = raw.encode(opacity=alt.value(0.2))
   chart = alt.Chart(data).mark_line(point=True).encode(
       x='t:Q',
       y=alt.Y('value:Q', impute=alt.ImputeParams(value=0)),
       color='variable:N'
   )
   background + chart

Or we can impute using any supported aggregate:

.. altair-plot::

   chart = alt.Chart(data).mark_line(point=True).encode(
       x='t:Q',
       y=alt.Y('value:Q', impute=alt.ImputeParams(method='mean')),
       color='variable:N'
   )
   background + chart

Impute via Transform
^^^^^^^^^^^^^^^^^^^^
Similar to the :ref:`user-guide-bin-transform` and :ref:`user-guide-aggregate-transform`,
it is also possible to specify the impute transform outside the encoding as a
transform. For example, here is the equivalent of the above two charts:

.. altair-plot::

   chart = alt.Chart(data).transform_impute(
       impute='value',
       key='t',
       value=0,
       groupby=['variable']
   ).mark_line(point=True).encode(
       x='t:Q',
       y='value:Q',
       color='variable:N'
   )
   background + chart

.. altair-plot::

   chart = alt.Chart(data).transform_impute(
       impute='value',
       key='t',
       method='mean',
       groupby=['variable']
   ).mark_line(point=True).encode(
       x='t:Q',
       y='value:Q',
       color='variable:N'
   )
   background + chart

If you would like to use more localized imputed values, you can specify a
``frame`` parameter similar to the :ref:`user-guide-window-transform` that
will control which values are used for the imputation. For example, here
we impute missing values using the mean of the neighboring points on either
side:

.. altair-plot::

   chart = alt.Chart(data).transform_impute(
       impute='value',
       key='t',
       method='mean',
       frame=[-1, 1],
       groupby=['variable']
   ).mark_line(point=True).encode(
       x='t:Q',
       y='value:Q',
       color='variable:N'
   )
   background + chart

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_impute` method is built on the :class:`~ImputeTransform`
class, which has the following options:

.. altair-object-table:: altair.ImputeTransform
