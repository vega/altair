.. currentmodule:: altair

.. _user-guide-density-transform:

Density Transform
~~~~~~~~~~~~~~~~~
The density transform performs one-dimensional
`kernel density estimation <https://en.wikipedia.org/wiki/Kernel_density_estimation>`_
over input data and generates a new column of samples of the estimated densities.

Here is a simple example, showing the distribution of IMDB ratings from the movies
dataset:

.. altair-plot::
   
   import altair as alt
   from vega_datasets import data
   
   alt.Chart(data.movies.url).transform_density(
       'IMDB Rating',
       as_=['IMDB Rating', 'density'],
   ).mark_area().encode(
       x="IMDB Rating:Q",
       y='density:Q',
   )

The density can also be computed on a per-group basis, by specifying the ``groupby``
argument. Here we split the above density computation across movie genres:

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   
   alt.Chart(
       data.movies.url,
       width=120,
       height=80
   ).transform_filter(
       "isValid(datum['Major Genre'])"
   ).transform_density(
       'IMDB Rating',
       groupby=['Major Genre'],
       as_=['IMDB Rating', 'density'],
       extent=[1, 10],
   ).mark_area().encode(
       x="IMDB Rating:Q",
       y='density:Q',
   ).facet(
       'Major Genre:N',
       columns=4
   )


Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_density` method is built on the
:class:`~DensityTransform` class, which has the following options:

.. altair-object-table:: altair.DensityTransform
