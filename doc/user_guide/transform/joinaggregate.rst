.. currentmodule:: altair

.. _user-guide-joinaggregate-transform:

Join Aggregate Transform
~~~~~~~~~~~~~~~~~~~~~~~~
The Join Aggregate transform acts in almost every way the same as an Aggregate
transform, but the resulting aggregate is joined to the original dataset.
To make this more clear, consider the following dataset:

.. altair-plot::
   :output: repr

   import pandas as pd
   import numpy as np

   rand = np.random.RandomState(0)

   df = pd.DataFrame({
       'label': rand.choice(['A', 'B', 'C'], 10),
       'value': rand.randn(10),
   })
   df

Here is a pandas operation that is equivalent to Altair's Aggregate transform,
using the mean as an example:

.. altair-plot::
   :output: repr

   mean = df.groupby('label').mean().reset_index()
   mean

And here is an output that is equivalent to Altair's Join Aggregate:

.. altair-plot::
   :output: repr

   pd.merge(df, mean, on='label', suffixes=['', '_mean'])

Notice that the join aggregate joins the aggregated value with the original
dataframe, such that the aggregated values can be used in tandem with the
original values if desired.

Here is an example of how the join aggregate might be used: we compare the
IMDB and Rotten Tomatoes movie ratings, normalized by their mean and
standard deviation, which requires calculations on the joined data:

.. altair-plot::

   import altair as alt
   from vega_datasets import data

   alt.Chart(data.movies.url).transform_filter(
       'datum.IMDB_Rating != null  && datum.Rotten_Tomatoes_Rating != null'
   ).transform_joinaggregate(
       IMDB_mean='mean(IMDB_Rating)',
       IMDB_std='stdev(IMDB_Rating)',
       RT_mean='mean(Rotten_Tomatoes_Rating)',
       RT_std='stdev(Rotten_Tomatoes_Rating)'
   ).transform_calculate(
       IMDB_Deviation="(datum.IMDB_Rating - datum.IMDB_mean) / datum.IMDB_std",
       Rotten_Tomatoes_Deviation="(datum.Rotten_Tomatoes_Rating - datum.RT_mean) / datum.RT_std"
   ).mark_point().encode(
       x='IMDB_Deviation:Q',
       y="Rotten_Tomatoes_Deviation:Q"
   )

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_joinaggregate` method is built on the
:class:`~JoinAggregateTransform` class, which has the following options:

.. altair-object-table:: altair.JoinAggregateTransform
