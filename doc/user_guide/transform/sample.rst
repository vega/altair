.. currentmodule:: altair

.. _user-guide-sample-transform:

Sample Transform
~~~~~~~~~~~~~~~~
The sample transform is one of the simpler of all Altair's data transforms;
it takes a single parameter ``sample`` which specified a number of rows to
randomly choose from the dataset. The resulting chart will be created using
only this random subset of the data.

For example, here we chart the full cars dataset alongside a sample of 100
rows:

.. altair-plot::

   import altair as alt
   from vega_datasets import data

   source = data.cars.url

   chart = alt.Chart(source).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
       color='Origin:N'
   ).properties(
       width=200,
       height=200
   )

   chart | chart.transform_sample(100)


Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_sample` method is built on the :class:`~SampleTransform`
class, which has the following options:

.. altair-object-table:: altair.SampleTransform
