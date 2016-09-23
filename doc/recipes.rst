.. _plot-recipes:

Altair Plot Recipes
===================

Altair is a powerfully expressive system, but some standard plot types are
expressed more verbosely than in other graphics systems. This section contains
a few recipes for creating such plot types.

.. _recipes-histogram:

Histograms
----------

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

   # data will be 1000 normally-distributed values
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

.. recipes-heatmap:

Heatmaps
--------
A Heat Map is a two-dimensional gridded visualization, where the colors within
the grid cells are related to some aggregate of the data within them.
Altair provides the ability to create heatmaps using the :class:`Row` and
:class:`Column` encodings, with the colors controlled (somewhat confusingly)
by a specially-configured ``text`` mark with a :class:`Color` encoding.
Note that there is a proposal within Vega-Lite to replace this with a more
intuitive heatmap specification, but for the time being they can be created
as follows:

.. altair-setup::
   :show:

   from altair import Row, Column, Chart, Text

   def heatmap(data, row, column, color, cellsize=(30, 15)):
       """Create an Altair Heat-Map

       Parameters
       ----------
       row, column, color : str
           Altair trait shorthands
       cellsize : tuple
           specify (width, height) of cells in pixels
       """
       return Chart(data).mark_text(
                  applyColorToBackground=True,
              ).encode(
                  row=row,
                  column=column,
                  text=Text(value=' '),
                  color=color
              ).configure_scale(
                  textBandWidth=cellsize[0],
                  bandSize=cellsize[1]
              )

With this function defined, we can use it to plot a heat-map for a dataset.
Here let's look at the total US population by age and year:

.. altair-plot::

   from altair import load_dataset
   data = load_dataset('population')

   heatmap(data, row='age', column='year', color='sum(people)')

Apparent in the data is the post-World-War-II "Baby Boom", seen in the diagonal
stripe at the top-right.


.. recipe-grouped-regression:

Grouped Regression Plots
------------------------
Altair doesn't include any built-in statistical modeling functionality, but
it's fairly straightforward to create an Altair-style syntax that adds this.
Here we will extend the :class:`Chart` object and add a method which will
produce a grouped regression plot using Altair's syntax:


.. altair-setup::
   :show:

   from copy import deepcopy
   import numpy as np
   import pandas as pd
   import altair


   def linear_regression(x, y):
       """Return the linear regression of x & y evaluated at x"""
       p = np.polyfit(x, y, 1)
       return np.polyval(p, x)


   class RegressionChart(altair.Chart):
       @staticmethod
       def _add_regression_column(group, regression_func, x, y, yfit):
           group[yfit] = regression_func(group[x], group[y])
           return group

       def regression_plot(self, func=linear_regression):
           if not isinstance(self.data, pd.DataFrame):
               raise ValueError("data must be a DataFrame")

           # we need a points layer and a lines layer
           points = self.mark_point()
           lines = deepcopy(self).mark_line()

           # confirm that none of the encodings are binned
           encoding = points.encoding.to_dict()
           if any(enc.get('bin', False) for enc in encoding.values()):
               raise ValueError("regress() cannot handle binned variables")

           # find variables that define groups
           group_cols = [enc['field'] for key, enc in encoding.items()
                         if key not in ['x', 'y']]
           x = encoding['x']['field']
           y = encoding['y']['field']
           yfit = y + '_fit'
           lines.encode(y=yfit)

           # perform the regression within each group
           if group_cols:
               groups = self.data.groupby(group_cols)
               data = groups.apply(self._add_regression_column,
                                   regression_func=func,
                                   x=x, y=y, yfit=yfit)
           else:
               data = self._add_regression_column(self.data.copy(),
                                                  regression_func=func,
                                                  x='x', y='y', yfit='y_fit')

           return altair.LayeredChart(data).set_layers(points, lines)

Now let's create some data: we'll create three groups of data, each drawn from
a different model:

.. altair-setup::
   :show:

   def make_data(N, rseed=42):
       rng = np.random.RandomState(rseed)
       x = 100 * rng.rand(N)
       group = rng.randint(0, 3, N)
       y = (group - 2) * x + (10 + 0.2 * x) * rng.randn(N)
       return pd.DataFrame({'x': x, 'y': y, 'group': group})

   data = make_data(100)

If we do a regression plot over only ``x`` and ``y``, a single line is shown
for the entire dataset:

.. altair-plot::

   RegressionChart(data).encode(
       x='x',
       y='y',
   ).regression_plot()

If we specify another encoding, multiple regressions are added:

.. altair-plot::

   RegressionChart(data).encode(
       x='x',
       y='y',
       color='group:N',
   ).regression_plot()

In a similar manner, Altair's API could be easily extended to easily create
a wide variety of domain-specific visualizations.
