.. currentmodule:: altair

.. _user-guide-data:

Data
~~~~

The basic data model used by Altair is tabular data, similar to a spreadsheet, pandas DataFrame or a database table. Individual data sets are assumed to contain a collection of records, which may contain any number of named data fields.

Each top-level chart object (i.e. :class:`Chart`, :class:`LayerChart`,
and :class:`VConcatChart`, :class:`HConcatChart`, :class:`RepeatChart`,
:class:`FacetChart`) accepts a dataset as its first argument.

Altair provides the following ways to specify a dataset:

=========================================  ================================================================================
Data                                       Description
=========================================  ================================================================================
:ref:`user-guide-dataframe-data`           A `Pandas DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_.
:ref:`user-guide-dict-data`                A :class:`Data` or related object (i.e. :class:`UrlData`, :class:`InlineData`, :class:`NamedData`).                                 
:ref:`user-guide-url-data`                 A url string pointing to a ``json`` or ``csv`` formatted text file.                                       
:ref:`user-guide-spatial-data`             An object that supports the `__geo_interface__` (eg. `Geopandas GeoDataFrame <http://geopandas.org/data_structures.html#geodataframe>`_, `Shapely Geometries <https://shapely.readthedocs.io/en/latest/manual.html#geometric-objects>`_, `GeoJSON Objects <https://github.com/jazzband/geojson#geojson-objects>`_).
:ref:`user-guide-generator-data`           A generated dataset such as numerical sequences or geographic reference elements.
=========================================  ================================================================================

When data is specified as a DataFrame, the encoding is quite simple, as Altair
uses the data type information provided by Pandas to automatically determine
the data types required in the encoding. For example, here we specify data via a Pandas DataFrame:

.. altair-plot::

   import altair as alt
   import pandas as pd

   data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                        'y': [5, 3, 6, 7, 2]})
   alt.Chart(data).mark_bar().encode(
       x='x',
       y='y',
   )

.. toctree::
   :hidden:

   dataframe
   dict   
   url
   spatial
   generator