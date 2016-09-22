Altair Plot Recipes
===================

Altair is a powerfully expressive system, but some standard plot types are
expressed more verbosely than in other graphics systems. This section contains
a few recipes for creating such plot types.

Histogram
---------
A classic histogram involves a binning in one dimension, with the relevant
count in the other. Binning and aggregation are covered in detail in
:ref:`encoding-aggregates`; here is a simple recipe function to create a
standard one-dimensional histogram:

.. altair-setup::
   :show:

   from altair import Chart, Bin, X, Axis
   import pandas as pd

   def histogram(data, **bin_kwds):
       """
       Create a Histogram of a 1-dimensional array or series of data
       All parameters are passed to the altair's ``Bin`` class
       """
       data = pd.DataFrame({'x': data})

       return Chart(data).mark_bar().encode(
                  x=X('x', bin=Bin(**bin_kwds)),
                  y='count(*):Q'
              )

Usage of this function is straightforward:

.. altair-setup::

   from numpy.random import RandomState
   data = RandomState(0).randn(1000)

.. altair-plot::

   histogram(data, maxbins=20)

Of course, you might want to be able to further adjust the result. You could
do this by creating the chart from scratch. However, because the function
does not return an image, but rather a fully-functioning :class:`Chart` object,
you can modify the output of the function directly. For example:

.. altair-plot::

   hist = histogram(data, maxbins=20)

   # modify traits directly
   hist.encoding.x.axis = Axis(title='Values')
   hist.encoding.y.axis = Axis(title='Number of Values')

   # modify traits via methods
   hist.configure_mark(
       color='salmon'
   ).configure_cell(
       height=200,
       width=300
   )
