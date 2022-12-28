.. currentmodule:: altair

.. _user-guide-flatten-transform:

Flatten
~~~~~~~
The flatten transform can be used to extract the contents of arrays from data entries.
This will not generally be useful for well-structured data within pandas dataframes,
but it can be useful for working with data from other sources.

As an example, consider this dataset which uses a common convention in JSON data,
a set of fields each containing a list of entries:

.. altair-plot::
   :output: none

   import numpy as np

   rand = np.random.RandomState(0)

   def generate_data(N):
       mean = rand.randn()
       std = rand.rand()
       return list(rand.normal(mean, std, N))

   data = [
       {'label': 'A', 'values': generate_data(20)},
       {'label': 'B', 'values': generate_data(30)},
       {'label': 'C', 'values': generate_data(40)},
       {'label': 'D', 'values': generate_data(50)},
   ]

This kind of data structure does not work well in the context of dataframe
representations, as we can see by loading this into pandas:

.. altair-plot::
   :output: repr

   import pandas as pd
   df = pd.DataFrame.from_records(data)
   df

Alair's flatten transform allows you to extract the contents of these arrays
into a column that can be referenced by an encoding:

.. altair-plot::

   import altair as alt

   alt.Chart(df).transform_flatten(
       ['values']
   ).mark_tick().encode(
       x='values:Q',
       y='label:N',
   )

This can be particularly useful in cleaning up data specified via a JSON URL,
without having to first load the data for manipulation in pandas.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_flatten` method is built on the :class:`~FlattenTransform`
class, which has the following options:

.. altair-object-table:: altair.FlattenTransform
