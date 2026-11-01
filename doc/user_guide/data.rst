.. currentmodule:: altair
    
.. _user-guide-data:

Specifying Data
---------------

The basic data model used by Altair is tabular data,
similar to a spreadsheet or database table.
Individual datasets are assumed to contain a collection of records (rows),
which may contain any number of named data fields (columns).
Each top-level chart object (i.e. :class:`Chart`, :class:`LayerChart`,
:class:`VConcatChart`, :class:`HConcatChart`, :class:`RepeatChart`,
and :class:`FacetChart`) accepts a dataset as its first argument.

There are many different ways of specifying a dataset:

- as an eager DataFrame or table supported by `Narwhals <https://narwhals-dev.github.io/narwhals/>`_,
  such as a pandas DataFrame, a Polars DataFrame, or a PyArrow Table.
  Objects implementing the DataFrame Interchange Protocol (``__dataframe__``)
  are also supported.
- as a :class:`Data` or related object (i.e. :class:`UrlData`, :class:`InlineData`, :class:`NamedData`)
- as a Python dictionary with inline ``values`` records
- as a URL string pointing to a data file
- as a `geopandas GeoDataFrame <http://geopandas.org/data_structures.html#geodataframe>`_, `Shapely Geometries <https://shapely.readthedocs.io/en/latest/manual.html#geometric-objects>`_, `GeoJSON Objects <https://github.com/jazzband/geojson#geojson-objects>`_ or other objects that support the ``__geo_interface__``
- as a generated dataset such as numerical sequences or geographic reference elements

.. _data-long-vs-wide:

Long-form vs. Wide-form Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two common conventions for storing tabular data, sometimes called
*long-form* and *wide-form*. Both are sensible patterns for storing data in
a tabular format; briefly, the difference is this:

- **Wide-form data** stores related measurements in separate columns, with some data such as categorical labelsstored in the column names.
- **Long-form data** stores those measurements in one or more value columns, with additional columns identifying the category, group, or measurement represented by each row, so that there is one row per observation.

A concrete example will help in making this distinction more clear.
Consider a dataset consisting of stock prices of several companies over time.
The wide-form version of the data might be arranged as follows:

.. altair-plot::
    :output: repr
    :chart-var-name: wide_form
    :remove-code:

    import polars as pl
    pl.Config(
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
        tbl_formatting="NOTHING"
    )

    wide_form = pl.DataFrame({
        'Date': ['2007-10-01', '2007-11-01', '2007-12-01'],
        'AAPL': [189.95, 182.22, 198.08],
        'AMZN': [89.15, 90.56, 92.64],
        'GOOG': [707.00, 693.00, 691.48]
    })
    wide_form

Notice that each row corresponds to a single time-stamp
(here time is the independent variable),
while the stock category for each observation
(i.e. company name) is stored within the column labels.
The long-form version of the same data would look like this:

.. altair-plot::
    :output: repr
    :chart-var-name: long_form
    :remove-code:

    long_form = pl.DataFrame({
        'Date': ['2007-10-01', '2007-11-01', '2007-12-01',
                 '2007-10-01', '2007-11-01', '2007-12-01',
                 '2007-10-01', '2007-11-01', '2007-12-01'],
        'company': ['AAPL', 'AAPL', 'AAPL',
                    'AMZN', 'AMZN', 'AMZN',
                    'GOOG', 'GOOG', 'GOOG'],
        'price': [189.95, 182.22, 198.08,
                  89.15,  90.56,  92.64,
                  707.00, 693.00, 691.48]
    })
    long_form

Notice here that each row contains a single observation (i.e. price), along
with the categorical labels for this observation (the date and company name).
Importantly, the column and index labels no longer contain any data,
just the name of the variables.

Altair's grammar works best with **long-form** data because all relevant
data are stored within the table itself, rather than within the
names of rows and columns.
Wide-form data can be visualized using e.g. layering
(see :ref:`layer-chart`), but it is far less convenient within Altair's grammar.

If you would like to convert data from wide-form to long-form, there are two possible
approaches: it can be done as a preprocessing step using the dataframe library,
e.g. by using `melt in pandas`_ or `unpivot in Polars`_,
or with the :ref:`Fold Transform <user-guide-fold-transform>` in Altair.

.. _pandas: http://pandas.pydata.org/
.. _melt in pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#melt-and-wide-to-long
.. _unpivot in Polars: https://docs.pola.rs/user-guide/transformations/unpivot/


DataFrames and Tables
~~~~~~~~~~~~~~~~~~~~~

When data is specified as a DataFrame (or Table),
Altair uses the data type information
provided by the dataframe library to automatically determine
the data types required in the encoding.
For example,
here Altair automatically detects that the y-column
should be visualized on a categorical (nominal) scale
and that the x-column should be visualized on a quantitative scale
based on the column data types stored in the Polars dataframes:

.. altair-plot::

   import altair as alt
   import polars as pl

   df = pl.DataFrame({
       'x': [5, 3, 6, 7, 2],
       'y': ['A', 'B', 'C', 'D', 'E']
   })
   alt.Chart(df).mark_bar().encode(
       x='x',
       y='y',
   )

And here we do the same thing for pandas:

.. altair-plot::

   import pandas as pd

   df = pd.DataFrame({
       'x': [5, 3, 6, 7, 2],
       'y': ['A', 'B', 'C', 'D', 'E']
   })
   alt.Chart(df).mark_bar().encode(
       x='x',
       y='y',
   )

By comparison,
for inline records, URL data, and named data,
field encoding types generally need to be specified explicitly,
as can be seen in `Inline Data`_ and `Data by URL`_.

.. _data-in-index:

Including Pandas Index Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^
By design Altair only accesses dataframe columns, not dataframe indices.
At times, relevant data appears in the index. For example:

.. altair-plot::
   :output: repr

   import numpy as np
   rand = np.random.RandomState(0)

   df = pd.DataFrame(
       {'value': rand.randn(100).cumsum()},
       index=pd.date_range('2018', freq='D', periods=100)
    )
   df.head()

If you would like the index to be available to the chart, you can explicitly
turn it into a column using the ``reset_index()`` method of pandas dataframes.
If the index object does not have a ``name`` attribute set, the resulting
column will be called ``"index"``.
More information is available in the
`pandas documentation <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html>`_.


.. altair-plot::

   alt.Chart(df.reset_index()).mark_line().encode(
       x='index:T',
       y='value:Q'
   )

.. _data-dictionary:

Inline Data
~~~~~~~~~~~

Here we create the same bar chart shown in `DataFrames and Tables`_
using inline data,
which needs to be defined as a list of records/observations.
We can specify inline data
using the :class:`Data` helper class as we do here,
but it is also possible to use a Python dictionary
with a ``"values"`` key.

.. altair-plot::

   data = alt.Data(
       values=[
           {'y': 'A', 'x': 5},
           {'y': 'B', 'x': 3},
           {'y': 'C', 'x': 6},
           {'y': 'D', 'x': 7},
           {'y': 'E', 'x': 2}
       ]
   )
   alt.Chart(data).mark_bar().encode(
       x='x:Q',  # specify quantitative data
       y='y:N',  # specify nominal data
   )

Notice the extra markup required in the encoding;
because there is no underlying
dataframe library providing the columns data type for each column,
we must specify them manually
(here we use :ref:`shorthand-description` to specify *nominal* (``N``) for ``y``
and *quantitative* (``Q``) for ``x``; see :ref:`encoding-data-types`).

.. _data-url:

Data by URL
~~~~~~~~~~~

A URL string pointing to a JSON or CSV dataset can be passed directly to
:class:`Chart`. The URL is stored in the chart specification and resolved
when the chart is rendered; the data is not embedded in the specification.
Altair cannot infer field types from remote data, so specify them explicitly.

.. altair-plot::

   from altair.datasets import data

   alt.Chart(data.cars.url).mark_point().encode(
       x="Horsepower:Q",
       y="Miles_per_Gallon:Q",
   )


.. _data-generated:

Generated Data
~~~~~~~~~~~~~~
At times it is convenient to not use an external data source, but rather generate data for
display within the chart specification itself. The benefit is that the chart specification
can be made much smaller for generated data than for embedded data.

Sequence Generator
^^^^^^^^^^^^^^^^^^
Here is an example of using the :func:`sequence` function to generate a sequence of  *x*
data, along with a :ref:`user-guide-calculate-transform` to compute *y* data.

.. altair-plot::

   # Note that the following generator is functionally similar to
   # data = pd.DataFrame({'x': np.arange(0, 10, 0.1)})
   seq_data = alt.sequence(0, 10, 0.1, as_='x')

   alt.Chart(seq_data).transform_calculate(
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

   grat_data = alt.graticule(step=[15, 15])

   alt.Chart(grat_data).mark_geoshape(stroke='black').project(
       'orthographic',
       rotate=[0, -45, 0]
   )

Sphere Generator
^^^^^^^^^^^^^^^^
Finally when visualizing the globe a sphere can be used as a background layer
within a map to represent the extent of the Earth. This sphere data can be
created using Altair's :func:`sphere` generator function. Here is an example:

.. altair-plot::

   sphere_data = alt.sphere()

   background = alt.Chart(sphere_data).mark_geoshape(fill='aliceblue')
   lines = alt.Chart(grat_data).mark_geoshape(stroke='lightgrey')

   alt.layer(background, lines).project('naturalEarth1')


.. _spatial-data:

Spatial Data
~~~~~~~~~~~~

In this section, we explain different methods for reading spatial data into Altair.
To learn more about how to work with this data after you have read it in,
please see the :ref:`user-guide-geoshape-marks` mark page.


.. _spatial-data-gdf:

GeoPandas GeoDataFrame
^^^^^^^^^^^^^^^^^^^^^^

It is convenient to use GeoPandas as the source for your spatial data.
GeoPandas can read many types of spatial data and Altair works well with GeoDataFrames.
Here we define four polygon geometries into a
GeoDataFrame and visualize these using the ``mark_geoshape``.

.. altair-plot::
   :output: repr

   from shapely import geometry
   import geopandas as gpd

   data_geoms = [
       {"color": "#F3C14F", "geometry": geometry.Polygon([[1.45, 3.75], [1.45, 0], [0, 0], [1.45, 3.75]])},
       {"color": "#4098D7", "geometry": geometry.Polygon([[1.45, 0], [1.45, 3.75], [2.57, 3.75], [2.57, 0], [2.33, 0], [1.45, 0]])},
       {"color": "#66B4E2", "geometry": geometry.Polygon([[2.33, 0], [2.33, 2.5], [3.47, 2.5], [3.47, 0], [3.2, 0], [2.57, 0], [2.33, 0]])},
       {"color": "#A9CDE0", "geometry": geometry.Polygon([[3.2, 0], [3.2, 1.25], [4.32, 1.25], [4.32, 0], [3.47, 0], [3.2, 0]])},
   ]

   gdf_geoms = gpd.GeoDataFrame(data_geoms)
   gdf_geoms


Since the spatial data in our example is not geographic,
we use ``project`` configuration ``type="identity", reflectY=True`` to draw the
geometries without applying a geographic projection. By using ``alt.Color(...).scale(None)`` we
disable the automatic color assignment in Altair
and instead directly use the provided Hex color codes.

.. altair-plot::

   alt.Chart(gdf_geoms, title="Vega-Altair").mark_geoshape().encode(
       alt.Color("color:N").scale(None)
   ).project(type="identity", reflectY=True)


.. _spatial-data-inline-geojson:

Inline GeoJSON Object
^^^^^^^^^^^^^^^^^^^^^

If your source data is a GeoJSON file and you do not want to load it
into a GeoPandas GeoDataFrame you can provide it as a dictionary to the Altair ``Data`` class. A
GeoJSON file normally consists of a ``FeatureCollection`` with a list of
``features`` where the information for each geometry is specified within a
``properties`` dictionary. In the following example a GeoJSON-like data
object is specified into a ``Data`` class using the ``property``
value of the ``key`` that contain the nested list (here named
``features``).

.. altair-plot::
   :output: repr

   obj_geojson = {
       "type": "FeatureCollection",
       "features":[
           {"type": "Feature", "properties": {"location": "left"}, "geometry": {"type": "Polygon", "coordinates": [[[1.45, 3.75], [1.45, 0], [0, 0], [1.45, 3.75]]]}},
           {"type": "Feature", "properties": {"location": "middle-left"}, "geometry": {"type": "Polygon", "coordinates": [[[1.45, 0], [1.45, 3.75], [2.57, 3.75], [2.57, 0], [2.33, 0], [1.45, 0]]]}},
           {"type": "Feature", "properties": {"location": "middle-right"}, "geometry": {"type": "Polygon", "coordinates": [[[2.33, 0], [2.33, 2.5], [3.47, 2.5], [3.47, 0], [3.2, 0], [2.57, 0], [2.33, 0]]]}},
           {"type": "Feature", "properties": {"location": "right"}, "geometry": {"type": "Polygon", "coordinates": [[[3.2, 0], [3.2, 1.25], [4.32, 1.25], [4.32, 0], [3.47, 0], [3.2, 0]]]}}
       ]
   }
   data_obj_geojson = alt.Data(values=obj_geojson, format=alt.DataFormat(property="features"))
   data_obj_geojson

The label for each objects location is stored within the ``properties`` dictionary. To access these values
you can specify a nested variable name (here ``properties.location``) within the color
channel encoding. Here we change the coloring encoding to be based on this location label,
and apply a ``magma`` color scheme instead of the default one.
The ``:O`` suffix indicates that we want Altair to treat these values as ordinal,
and you can read more about it in the :ref:`encoding-data-types` page.
for the ordinal structured data.

.. altair-plot::

   alt.Chart(data_obj_geojson, title="Vega-Altair - ordinal scale").mark_geoshape().encode(
       alt.Color("properties.location:O").scale(scheme='magma')
   ).project(type="identity", reflectY=True)


.. _spatial-data-remote-geojson:

GeoJSON File by URL
^^^^^^^^^^^^^^^^^^^

Altair can load GeoJSON resources directly from a web URL. Here we use
an example from geojson.xyz. As is explained in :ref:`spatial-data-inline-geojson`,
we specify ``features`` as
the value for the ``property`` parameter in the ``alt.DataFormat()`` object
and prepend the attribute we want to plot (``continent``)
with the name of the nested dictionary where the
information of each geometry is stored (``properties``).

.. altair-plot::
   :output: repr

   url_geojson = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson"
   data_url_geojson = alt.Data(url=url_geojson, format=alt.DataFormat(property="features"))
   data_url_geojson

.. altair-plot::

    alt.Chart(data_url_geojson).mark_geoshape().encode(color='properties.continent:N')


.. _spatial-data-inline-topojson:

Inline TopoJSON Object
^^^^^^^^^^^^^^^^^^^^^^

TopoJSON is an extension of GeoJSON, where the geometry of the features
are referred to from a top-level object named arcs. Each shared arc is
only stored once to reduce the size of the data. A TopoJSON file object can contain
multiple objects (eg. boundary border and province border). When
defining a TopoJSON object for Altair we specify the ``topojson``
data format type and the name of the object we like to visualize using the
``feature`` parameter. Here the name of this object key is ``MY_DATA``,
but this differs in each dataset.

.. altair-plot::
   :output: repr

   obj_topojson = {
       "arcs": [
           [[1.0, 1.0], [0.0, 1.0], [0.0, 0.0], [1.0, 0.0]],
           [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0]],
           [[1.0, 1.0], [1.0, 0.0]],
       ],
       "objects": {
           "MY_DATA": {
               "geometries": [
                   {"arcs": [[-3, 0]], "properties": {"name": "abc"}, "type": "Polygon"},
                   {"arcs": [[1, 2]], "properties": {"name": "def"}, "type": "Polygon"},
               ],
               "type": "GeometryCollection",
           }
       },
       "type": "Topology",
   }
   data_obj_topojson = alt.Data(
       values=obj_topojson, format=alt.DataFormat(feature="MY_DATA", type="topojson")
   )
   data_obj_topojson

.. altair-plot::

   alt.Chart(data_obj_topojson).mark_geoshape(
   ).encode(
       color="properties.name:N"
   ).project(
       type='identity', reflectY=True
   )


.. _spatial-data-remote-topojson:

TopoJSON File by URL
^^^^^^^^^^^^^^^^^^^^

Altair can load TopoJSON resources directly from a web URL. As
explained in :ref:`spatial-data-inline-topojson`, we have to use the
``feature`` parameter to specify the object name (here ``boroughs``) and
define the type of data as ``topjoson`` in the ``alt.DataFormat()`` object.

.. altair-plot::
   :output: repr

   url_topojson = data.london_boroughs.url

   data_url_topojson = alt.Data(
       url=url_topojson, format=alt.DataFormat(feature="boroughs", type="topojson")
   )

   data_url_topojson

Note: There also exist a shorthand to extract the objects from a
topojson file if this file is accessible by URL:
``alt.topo_feature(url=url_topojson, feature="boroughs")``

We color encode the Boroughs by there names as they are stored as an
unique identifier (``id``). We use a ``symbolLimit`` of 33 in two
columns to display all entries in the legend
and change the color scheme to have more distinct colors.
We also add a tooltip which shows the name of the borough
as we hover over it with the mouse.

.. altair-plot::

   alt.Chart(data_url_topojson, title="London-Boroughs").mark_geoshape(
       tooltip=True
   ).encode(
       alt.Color("id:N").scale(scheme='tableau20').legend(columns=2, symbolLimit=33)
   )

Similar to the ``feature`` option, there also exists the ``mesh``
parameter. This parameter extracts a named TopoJSON object set.
Unlike the feature option, the corresponding geo data is returned as
a single, unified mesh instance, not as individual GeoJSON features.
Extracting a mesh is useful for more efficiently drawing borders
or other geographic elements that you do not need to associate with
specific regions such as individual countries, states or counties.

Here below we draw the same Boroughs of London, but now as mesh only.

Note: you have to explicitly define ``filled=False`` to draw multi(lines)
without fill color.

.. altair-plot::

   url_topojson = data.london_boroughs.url

   data_url_topojson_mesh = alt.Data(
       url=url_topojson, format=alt.DataFormat(mesh="boroughs", type="topojson")
   )

   alt.Chart(data_url_topojson_mesh, title="Border London-Boroughs").mark_geoshape(
       filled=False
   )

.. _spatial-data-nested-geojson:

Nested GeoJSON Objects
^^^^^^^^^^^^^^^^^^^^^^

GeoJSON data can also be nested within another dataset. In this case it
is possible to use the ``shape`` encoding channel in combination with the
``:G`` suffix to visualize the nested features as GeoJSON objects.
In the following example the GeoJSON object are nested within ``geo``
in the list of dictionaries:

.. altair-plot::

   nested_features = [
       {"color": "#F3C14F", "geo": {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[1.45, 3.75], [1.45, 0], [0, 0], [1.45, 3.75]]]}}},
       {"color": "#4098D7", "geo": {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[1.45, 0], [1.45, 3.75], [2.57, 3.75], [2.57, 0], [2.33, 0], [1.45, 0]]]}}},
       {"color": "#66B4E2", "geo": {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[2.33, 0], [2.33, 2.5], [3.47, 2.5], [3.47, 0], [3.2, 0], [2.57, 0], [2.33, 0]]]}}},
       {"color": "#A9CDE0", "geo": {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[3.2, 0], [3.2, 1.25], [4.32, 1.25], [4.32, 0], [3.47, 0], [3.2, 0]]]}}},
   ]
   data_nested_features = alt.Data(values=nested_features)

   alt.Chart(data_nested_features, title="Vega-Altair").mark_geoshape().encode(
       shape="geo:G",
       color=alt.Color("color:N").scale(None)
   ).project(type="identity", reflectY=True)


.. _data-projections:

Projections
^^^^^^^^^^^
For geographic data it is best to use the World Geodetic System 1984 as
its geographic coordinate reference system with units in decimal degrees.
Try to avoid putting projected data into Altair, but reproject your spatial data to
EPSG:4326 first.
If your data comes in a different projection (eg. with units in meters) and you don't
have the option to reproject the data, try using the project configuration
``(type: 'identity', reflectY': True)``. It draws the geometries without applying a projection.


.. _data-winding-order:

Winding Order
^^^^^^^^^^^^^
LineString, Polygon and MultiPolygon geometries contain coordinates in an order: lines
go in a certain direction, and polygon rings do too. The GeoJSON-like structure of the
``__geo_interface__`` recommends the right-hand rule winding order for Polygon and
MultiPolygons. Meaning that the exterior rings should be counterclockwise and interior
rings are clockwise. While it recommends the right-hand rule winding order, it does not
reject geometries that do not use the right-hand rule.

Altair does NOT follow the right-hand rule for geometries, but uses the left-hand rule.
Meaning that exterior rings should be clockwise and interior rings should be
counterclockwise.
If you face a problem regarding winding order, try to force the left-hand rule on your
data before usage in Altair using GeoPandas for example as such:

.. code:: python

    from shapely.ops import orient
    gdf.geometry = gdf.geometry.apply(orient, args=(-1,))

.. toctree::
   :maxdepth: 1
   :caption: User Guide
   :hidden:

   self
   encodings/index
   marks/index
   transform/index
   interactions/index
   compound_charts
   scale_resolve
   times_and_dates
   customization
   configuration
   saving_charts


.. toctree::
   :maxdepth: 1
   :caption: Advanced Usage
   :hidden:

   internals
   display_frontends
   custom_renderers
   data_transformers
   large_datasets
