.. currentmodule:: altair

.. _user-guide-generator-data:

Generated data
~~~~~~~~~~~~~~

At times it is convenient to not use an external data source, but rather generate data for
display within the chart specification itself. The benefit is that the chart specification
can be made much smaller for generated data than for embedded data.

Sequence Generator
^^^^^^^^^^^^^^^^^^
Here is an example of using the :func:`sequence` function to generate a sequence of  *x*
data, along with a :ref:`user-guide-calculate-transform` to compute *y* data.

.. altair-plot::

   import altair as alt

   # Note that the following generator is functionally similar to
   # data = pd.DataFrame({'x': np.arange(0, 10, 0.1)})
   data = alt.sequence(0, 10, 0.1, as_='x')

   alt.Chart(data).transform_calculate(
       y='sin(datum.x)'
   ).mark_line().encode(
       x='x:Q',
       y='y:Q',
   )

Graticule Generator
^^^^^^^^^^^^^^^^^^^
Another type of data that is convenient to generate in the chart itself is the latitude/longitude
lines on a geographic visualization, known as a graticule. These can be created using Altair's
:func:`graticule` generator function. Here is a simple example:

.. altair-plot::

   import altair as alt

   data = alt.graticule(step=[15, 15])

   alt.Chart(data).mark_geoshape(stroke='black').project(
       'orthographic',
       rotate=[0, -45, 0]
   )

Sphere Generator
^^^^^^^^^^^^^^^^
Finally when visualizing the globe a sphere can be used as a background layer
within a map to represent the extent of the Earth. This sphere data can be
created using Altair's :func:`sphere` generator function. Here is an example:

.. altair-plot::

   import altair as alt

   sphere_data = alt.sphere()
   grat_data = alt.graticule(step=[15, 15])

   background = alt.Chart(sphere_data).mark_geoshape(fill='aliceblue')
   lines = alt.Chart(grat_data).mark_geoshape(stroke='lightgrey')

   alt.layer(background, lines).project('naturalEarth1')

.. _Pandas: http://pandas.pydata.org/
.. _Pandas pivot documentation: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html
.. _Pandas melt documentation: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.melt.html#pandas.DataFrame.melt
.. _Reshaping and Pivot Tables: https://pandas.pydata.org/pandas-docs/stable/reshaping.html