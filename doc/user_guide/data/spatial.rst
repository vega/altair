.. currentmodule:: altair

.. _user-guide-spatial-data:

Spatial Data
============

On this page we explain different methods for reading spatial data into Altair.
To learn more about how to work with this data after you have read it in,
please see the :ref:`user-guide-geoshape-marks` mark page.


.. _spatial-data-gdf:

GeoPandas GeoDataFrame
~~~~~~~~~~~~~~~~~~~~~~

It is convenient to use GeoPandas as the source for your spatial data.
GeoPandas can read many types of spatial data and Altair works well with GeoDataFrames.
Here we define four polygon geometries into a
GeoDataFrame and visualize these using the ``mark_geoshape``.

.. altair-plot::
   :output: repr

   from shapely import geometry
   import geopandas as gpd
   import altair as alt

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
geometries without applying a geographic projection. By using ``alt.Color(..., scale=None)`` we
disable the automatic color assignment in Altair
and instead directly use the provided Hex color codes.

.. altair-plot::

   alt.Chart(gdf_geoms, title="Vega-Altair").mark_geoshape().encode(
       color=alt.Color("color:N", scale=None)
   ).project(type="identity", reflectY=True)


.. _spatial-data-inline-geojson:

Inline GeoJSON object
~~~~~~~~~~~~~~~~~~~~~

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
can specify a nested variable name (here ``properties.location``) within the color
channel encoding. Here we change the coloring encoding to be based on this location label,
and apply a ``magma`` color scheme instead of the default one.
The `:O` suffix indicates that we want Altair to treat these values as ordinal,
and you can read more about it in the :ref:`_encoding-data-types` page.
for the ordinal structured data.

.. altair-plot::

   alt.Chart(data_obj_geojson, title="Vega-Altair - ordinal scale").mark_geoshape().encode(
       color=alt.Color("properties.location:O", scale=alt.Scale(scheme='magma'))
   ).project(type="identity", reflectY=True)


.. _spatial-data-remote-geojson:

GeoJSON file by URL
~~~~~~~~~~~~~~~~~~~

Altair can load GeoJSON resources directly from a web URL. Here we use
an example from geojson.xyz. As is explained in :ref:`spatial-data-inline-geojson`,
we specify ``features`` as
the value for the ``property`` parameter in the ``alt.DataFormat()`` object
and prepend the attribute we want to plot (``scalerank``)
with the name of the nested dictionary where the
information of each geometry is stored (``properties``).

.. altair-plot::
   :output: repr

   url_geojson = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
   data_url_geojson = alt.Data(url=url_geojson, format=alt.DataFormat(property="features"))
   data_url_geojson

.. altair-plot::

    alt.Chart(data_url_geojson).mark_geoshape().encode(color='properties.scalerank:N')


.. _spatial-data-inline-topojson:

Inline TopoJSON object
~~~~~~~~~~~~~~~~~~~~~~

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

TopoJSON file by URL
~~~~~~~~~~~~~~~~~~~~

Altair can load TopoJSON resources directly from a web URL. As
explained in :ref:`spatial-data-inline-topojson`, we have to
specify ``boroughs`` as the object name for the ``feature`` parameter and
define the type of data as ``topjoson`` in the ``alt.DataFormat()`` object.

.. altair-plot::
   :output: repr

   from vega_datasets import data

   url_topojson = data.londonBoroughs.url
    
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
       color=alt.Color("id:N", scale=alt.Scale(scheme='tableau20'), legend=alt.Legend(columns=2, symbolLimit=33))
   )



.. _spatial-data-nested-geojson:

Nested GeoJSON objects
~~~~~~~~~~~~~~~~~~~~~~

GeoJSON data can also be nested within another dataset. In this case it
is possible to use the ``shape`` encoding channel to visualize the
nested dictionary that contains the GeoJSON objects. In the following
example the GeoJSON object is nested in ``geo``:

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
       color=alt.Color("color:N", scale=None)
   ).project(type="identity", reflectY=True)


.. _data-projections:

Projections
~~~~~~~~~~~
For geographic data it is best to use the World Geodetic System 1984 as
its geographic coordinate reference system with units in decimal degrees.
Try to avoid putting projected data into Altair, but reproject your spatial data to
EPSG:4326 first.
If your data comes in a different projection (eg. with units in meters) and you don't
have the option to reproject the data, try using the project configuration
``(type: 'identity', reflectY': True)``. It draws the geometries without applying a projection.


.. _data-winding-order:

Winding Order
~~~~~~~~~~~~~
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