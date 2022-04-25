.. currentmodule:: altair

.. _user-guide-mark-geoshape:

Geoshape
~~~~~~~~~~~~~
The ``mark_geoshape`` represents an arbitrary shapes whose geometry is determined by specified spatial data.

Basic Map
~~~~~~~~~
Its most convenient to use a GeoDataFrame as input. Here we load the Natural Earth dataset and create a basic map using the geoshape mark:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    fp = gpd.datasets.get_path('naturalearth_lowres')
    gdf_ne = gpd.read_file(fp)  # shapefile    

    alt.Chart(gdf_ne).mark_geoshape()

In the example above, Altair applies a default blue color and uses a default map projection (``equalEarth``). We can customize the colors and boundary stroke widths using standard mark properties. Using the ``project`` method we can also define the map projection manually:

.. altair-plot::

    alt.Chart(gdf_ne).mark_geoshape(
        fill='lightgray', stroke='white', strokeWidth=0.5
    ).project(
        type='equalEarth'
    )

Focus & Filtering
~~~~~~~~~~~~~~~~~
By default Altair automatically adjusts the projection so that all the data fits within the width and height of the chart. 
Multiple approaches can be used to focus on specific regions of your spatial data. 

The following examples show different approaches to focus on continental Africa:

1. Filter the source data within your GeoDataFrame:

.. altair-plot::

    gdf_sel = gdf_ne[gdf_ne.continent == 'Africa']

    alt.Chart(gdf_sel).mark_geoshape().project(
        type='equalEarth'
    )

2. Filter the source data using a ``transorm_filter``:

.. altair-plot::

    alt.Chart(gdf_ne).mark_geoshape().project(
        type='equalEarth'
    ).transform_filter(
        alt.datum.continent == 'Africa'
    )

3. Specify projection parameters, such as ``scale`` (zoom level) and ``translate`` (panning):

.. altair-plot::

    alt.Chart(gdf_ne).mark_geoshape().project(
        type='equalEarth', 
        scale=200, 
        translate=[160, 160]  # lon, lat rotation
    )

Cartesian coordinates
~~~~~~~~~~~~~~~~~~~~~
The default projection of Altair is ``equalEarth``. This default assumes that your geometries are in degrees and referenced by longitude and latitude values. 
Another widely used coordinate system for data visualization is the 2d cartesian coordinate system. This coordinate system does not take into account the curvature of the Earth.

In the following example the input geometry is not projected and is instead rendered directly in raw coordinates using the ``identity`` transformation. We have to define the ``reflectY`` as well since Canvas and SVG treats postive ``y`` as pointing down.

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape().project(
        type='identity', 
        reflectY=True
    )

Mapping Polygons
~~~~~~~~~~~~~~~~
The following example maps the visual property of the ``name`` column using the ``color`` encoding.

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape().encode(
        color='name:N'
    ).project(
        type='identity', 
        reflectY=True
    )

Since each country is represented by a (multi)polygon, one can separate the ``stroke`` and ``fill`` defintions as such: 

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape(
        stroke='white',
        strokeWidth=1.5
    ).encode(
        fill='name:N'
    ).project(
        type='identity', 
        reflectY=True
    ) 

Mapping Lines
~~~~~~~~~~~~~
By default Altair assumes for ``mark_geoshape`` that the mark's color is used for the fill color instead of the stroke color.
This means that if your source data contain (multi)lines, you will have to explicitly define the ``filled`` value as ``False``.

Compare:

.. altair-plot::
    
    gs_line = gpd.GeoSeries.from_wkt(['LINESTRING (0 0, 1 1, 0 2, 2 2, -1 1, 1 0)'])
    alt.Chart(gs_line).mark_geoshape().project(
        type='identity', 
        reflectY=True
    )    

With:

.. altair-plot::
    
    gs_line = gpd.GeoSeries.from_wkt(['LINESTRING (0 0, 1 1, 0 2, 2 2, -1 1, 1 0)'])
    alt.Chart(gs_line).mark_geoshape(
        filled=False
    ).project(
        type='identity', 
        reflectY=True
    ) 

Using this approach one can also style Polygons as if they are Linestrings:

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape(
        filled=False,
        strokeWidth=1.5
    ).encode(
        stroke='name:N'
    ).project(
        type='identity', 
        reflectY=True
    )

Mapping Points
~~~~~~~~~~~~~~
Points can be drawn when they are defined as ``Points`` within a GeoDataFrame using ``mark_geoshape``.
We first assign the centroids of Polygons as Point geometry and plot these:

.. altair-plot::

    gdf_centroid = gpd.GeoDataFrame(
        data=gdf_sel.drop('geometry', axis=1), 
        geometry=gdf_sel.geometry.centroid
    )

    alt.Chart(gdf_centroid).mark_geoshape().project(
        type='identity', 
        reflectY=True
    )


But to use the ``size`` encoding for the Points you will need to use the ``mark_circle`` plus defining the ``latitude`` and ``longitude`` encoding channels.

.. altair-plot::

    gdf_centroid['lon'] = gdf_centroid['geometry'].x
    gdf_centroid['lat'] = gdf_centroid['geometry'].y

    alt.Chart(gdf_centroid).mark_circle().encode(
        latitude='lat:Q',
        longitude='lon:Q',
        size="pop_est:Q"
    ).project(
        type='identity', 
        reflectY=True
    )

You could skip the extra assingment to the ``lon`` and ``lat`` column in the GeoDataFrame and use the coordinates directly.  We combine the chart with a basemap to bring some perspective to the points:

.. altair-plot::

    basemap = alt.Chart(gdf_sel).mark_geoshape(
        fill='lightgray', stroke='white', strokeWidth=0.5
    )

    bubbles = alt.Chart(gdf_centroid).mark_circle(
        stroke='black'
    ).encode(
        latitude='geometry.coordinates[1]:Q',
        longitude='geometry.coordinates[0]:Q',
        size="pop_est:Q" 
    )

    (basemap + bubbles).project(
        type='identity', 
        reflectY=True
    )

Altair also contains expressions related to geographical features. One could for example define the ``centroids`` using a ``geoCentroid`` expression:

.. altair-plot::

    from altair.expr import datum, geoCentroid

    bubbles = alt.Chart(gdf_sel).transform_calculate(
        centroid=geoCentroid(None, datum)
    ).mark_circle(
        stroke='black'
    ).encode(
        longitude='centroid[0]:Q',
        latitude='centroid[1]:Q',
        size="pop_est:Q" 
    )

    (basemap + bubbles).project(
        type='identity', reflectY=True
    )

Lookup datasets
~~~~~~~~~~~~~~~
Sometimes your data is separated in two datasets. One ``DataFrame`` with the data and one ``GeoDataFrame`` with the geometries.
In this case you can use the ``lookup`` transform to connect related information in the other dataset.

You can use the ``lookup`` transform in two directions. 

1. Use a GeoDataFrame with geometries as source and lookup related information in another DataFrame.
2. Use a DataFrame as source and lookup related geometries in a GeoDataFrame.

Depending on your usecase one or the other is more favorable.

First show an example of the first approach. 
Here we lookup the field ``rate`` from the ``us_unemp`` DataFrame, where the ``us_counties`` GeoDataFrame is used as source: 

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    us_counties = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='counties')
    us_unemp = data.unemployment()

    alt.Chart(us_counties).mark_geoshape().transform_lookup(
        lookup='id', 
        from_=alt.LookupData(data=us_unemp, key='id', fields=['rate'])
    ).encode(
        alt.Color('rate:Q')
    ).project(
        type='albersUsa'
    )

Next, we show an example of the second approach.
Here we lookup the geometries through the fields ``geometry`` and ``type`` from the ``us_counties`` GeoDataFrame, where the ``us_unemp`` DataFrame is used as source.

.. altair-plot::

    alt.Chart(us_unemp).mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(data=us_counties, key='id', fields=['geometry', 'type'])
    ).encode(
        alt.Color('rate:Q')
    ).project(
        type='albersUsa'
    )


Interaction
~~~~~~~~~~~
Often a map does not come alone, but is used in combination with another chart. 
Here we provide an example of an interactive visualization of a bar chart and a map.

The data shows the states of the US in combination with a bar chart showing the 15 most populous states.

 .. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    # load the data
    us_states = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='states')
    us_population = data.population_engineers_hurricanes()[['state', 'id', 'population']]

    # define a pointer selection
    click_state = alt.selection_point(fields=['state'])

    # create a chloropleth map using a lookup transform 
    # define a condition on the opacity encoding depending on the selection
    choropleth = alt.Chart(us_states).mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(us_population, 'id', ['population', 'state'])
    ).encode(
        color='population:Q',
        opacity=alt.condition(click_state, alt.value(1), alt.value(0.2)),
        tooltip=['state:N', 'population:Q']
    ).project(type='albersUsa').add_parameter(click_state)

    # create a bar chart with a similar condition on the opacity encoding.
    bars = alt.Chart(
        us_population.nlargest(15, 'population'),
        title='Top 15 states by population').mark_bar(
    ).encode(
        x='population',
        opacity=alt.condition(click_state, alt.value(1), alt.value(0.2)),
        color='population',
        y=alt.Y('state', sort='-x')
    ).add_parameter(click_state)


    choropleth & bars


Geoshape Options
~~~~~~~~~~~~~~~~

Additional arguments to ``mark_geoshape()`` method are passed along to an
associated :class:`MarkDef` instance, which supports the following attributes:

.. altair-object-table:: altair.MarkDef

Marks can also be configured globally using chart-level configurations; see
:ref:`config-mark` for details.
