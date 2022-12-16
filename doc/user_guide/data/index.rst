.. currentmodule:: altair

.. _user-guide-data:

Data
~~~~

The basic data model used by Altair is tabular data,
similar to a spreadsheet or database table.
Individual datasets are assumed to contain a collection of records (rows),
which may contain any number of named data fields (columns).
Each top-level chart object (i.e. :class:`Chart`, :class:`LayerChart`,
:class:`VConcatChart`, :class:`HConcatChart`, :class:`RepeatChart`,
and :class:`FacetChart`) accepts a dataset as its first argument.

While the most common way to provide Altair with a dataset is via a pandas DataFrame,
there are many different ways of specifying a dataset:

=========================================  ================================================================================
Data                                       Description
=========================================  ================================================================================
:ref:`user-guide-dataframe-data`           A `pandas DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_.
:ref:`user-guide-dict-data`                A :class:`Data` or related object (i.e. :class:`UrlData`, :class:`InlineData`, :class:`NamedData`).                                 
:ref:`user-guide-url-data`                 A url string pointing to a ``json`` or ``csv`` formatted text file.                                       
:ref:`user-guide-spatial-data`             A `geopandas GeoDataFrame <http://geopandas.org/data_structures.html#geodataframe>`_, `Shapely Geometries <https://shapely.readthedocs.io/en/latest/manual.html#geometric-objects>`_, `GeoJSON Objects <https://github.com/jazzband/geojson#geojson-objects>`_ or other objects that support the ``__geo_interface__``.
:ref:`user-guide-generator-data`           A generated dataset such as numerical sequences or geographic reference elements.
=========================================  ================================================================================

When data is specified as a DataFrame, the encoding is quite simple, as Altair
uses the data type information provided by pandas to automatically determine
the data types required in the encoding. For example, here we specify data via a pandas DataFrame
and Altair automatically detects that the x-column should be visualized on a quantitative scale
and that the y-column should be visualized on a categorical scale:

.. altair-plot::

   import altair as alt
   import pandas as pd

   data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                        'y': [5, 3, 6, 7, 2]})
   alt.Chart(data).mark_bar().encode(
       x='x',
       y='y',
   )

If we are not happy with the scale that Altair chooses for visualizing that data,
we can change it by either changing the data types in the underlying pandas dataframe,
or by changing the :ref:`encoding-data-types` in Altair.

.. toctree::
   :hidden:

   dataframe
   dict   
   url
   spatial
   generator