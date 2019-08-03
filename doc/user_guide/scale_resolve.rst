.. currentmodule:: altair

.. _user-guide-resolve:

Scale and Guide Resolution
--------------------------
When creating compound charts (see :ref:`user-guide-compound`), altair defaults
to using shared chart scales and guides (e.g. axes, legends, etc.).
This default can be adjusted using the :meth:`Chart.resolve_scale`,
:meth:`Chart.resolve_axis`, and :meth:`Chart.resolve_legend` functions.

For example, suppose you would like to concatenate two charts with separate
color scales; the default behavior is for the color scale to be created for
a union of the two color encoding domains:

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   
   source = data.cars()
   
   base = alt.Chart(source).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q'
   ).properties(
       width=200,
       height=200
   )
   
   alt.concat(
       base.encode(color='Origin:N'),
       base.encode(color='Cylinders:O')
   )

This default can be changed by setting the scale resolution for the color to
``"independent"`` (rather than the default, ``"shared"``):

.. altair-plot::
   
   alt.concat(
       base.encode(color='Origin:N'),
       base.encode(color='Cylinders:O')
   ).resolve_scale(
       color='independent'
   )