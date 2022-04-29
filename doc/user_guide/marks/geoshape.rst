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


Chloropleth Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~
Choropleth maps provide an easy way to visualize how a variable varies across a 
geographic area or show the level of variability within a region. 

Take for example the following example of unemployment statistics of 2018 of US counties 
(we define a utility function (`classify()` that we will use later again):

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    def classify(scale_type, breaks=None, nice=False, title=None, size='small'):

        if size =='default':
            width=400
            height=300
        else:
            width=200
            height=150
            
        us_counties = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='counties')
        us_states = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='states')    
        us_unemp = data.unemployment()  
        
        if title is None:
            title=scale_type
        
        if 'threshold' in scale_type:
            scale = alt.Scale(type=scale_type, domain=breaks, scheme='turbo')
        else:
            scale = alt.Scale(type=scale_type, nice=nice, scheme='turbo')
            
        fill = alt.Fill(
            'rate:Q', 
            scale=scale,
            legend=alt.Legend(direction='horizontal', orient='bottom', format='.1%')
        )    
        
        distrib_square = alt.Chart(
            us_unemp, 
            height=20,
            width=width
        ).mark_square(
            size=3,
            opacity=1
        ).encode(
            x=alt.X('rate:Q', title=None, axis=alt.Axis(format='.0%')),
            y=alt.Y('jitter:Q', title=None, axis=None),
            fill=fill
        ).transform_calculate(
            jitter='random()'
        )
        
        distrib_geoshape = alt.Chart(
            us_counties,
            width=width,
            height=height,
            title=title
        ).mark_geoshape().transform_lookup(
            lookup='id', 
            from_=alt.LookupData(data=us_unemp, key='id', fields=['rate'])
        ).encode(
            fill=fill
        ).project(
            type='albersUsa'
        )
        
        states_geoshape = alt.Chart(
            us_states,
            width=width,
            height=height
        ).mark_geoshape(filled=False, stroke='white', strokeWidth=0.75).project(
            type='albersUsa'
        )     
        
        return (distrib_geoshape + states_geoshape) & distrib_square

    classify('linear', size='default')


We visualise the unemployment `rate` in percentage of 2018 with a linear scale range 
using a `mark_geoshape()` to present the spatial patterns on a map and a _jitter_ plot 
(using `mark_square()`) to visualise the distribution of the `rate` values. Each value/
county has defined an unique color. This gives a bit of insight, but often we like to 
group the distribution into classes.

By grouping values in classes, you can classify the dataset so all values/geometries in 
each class get assigned the same color.

Here we present a number of scale methods how Altair can be used:
- _quantile_, this type will divide your dataset (`domain`) into intervals of similar 
sizes. Each class contains more or less the same number of values/geometries (equal 
counts). The scale definition will look as follow: 

```python
alt.Scale(type='quantile')
```

- _quantize_, this type will divide the extent of your dataset (`range`) in equal 
intervals. Each class contains different number of values, but the step size is equal 
(equal range). The scale definition will look as follow: 

```python
alt.Scale(type='quantize')
```

The `quantize` methode can also be used in combination with `nice`. This will "nice" 
the domain before applying quantization. As such:

```python
alt.Scale(type='quantize', nice=True)
```

- _threshold_, this type will divide your dataset in separate classes by manually 
specifying the cut values. Each class is separated by defined classes. The scale 
definition will look as follow: 

```python
alt.Scale(type='quantize', range=[0.05, 0.20])
```

This definition above will create 3 classes. One class with values below `0.05`, one 
class with values from `0.05` to `0.20` and one class with values higher than `0.20`.

So which method provides the optimal data classification for chloropleths maps? As 
usual, it depends. There is another popular method that aid in determining class breaks.
This method will maximize the similarity of values in a class while maximizing the 
distance between the classes (natural breaks). The method is also known by as the 
Fisher-Jenks algorithm and is similar to _k_-Means in 1D:
-  By using the external Python package `jenskpy` we can derive these _optimim_ breaks 
as such:

```python
>>> from jenkspy import JenksNaturalBreaks
>>> jnb = JenksNaturalBreaks(5)
>>> jnb.fit(us_unemp['rate'])
>>> jnb.inner_breaks_
[0.061, 0.088, 0.116, 0.161]
```
So when applying these different classification schemes to the county unemployment 
dataset, we get the following overview:

.. altair-plot::

    alt.concat(
        classify('linear'),
        classify('quantile', title=['quantile','equal counts']),
        classify('quantize', title=['quantize', 'equal range']),
        classify('quantize', nice=True, title=['quantize', 'equal range nice']),
        classify('threshold', breaks=[0.05, 0.20]),    
        classify('threshold', breaks=[0.061, 0.088, 0.116, 0.161], 
                title=['threshold Jenks','natural breaks']
        ),
        columns=3
    )


Caveats: 

- For the type `quantize` and `quantile` scales we observe that the default number of 
classes is 5. It is currently not possible to define a different number of classes in 
Altair in combination with a predefined color scheme. Track the following issue at the 
Vega-Lite repository: https://github.com/vega/vega-lite/issues/8127
- To define custom colors for each class, one should specify the `domain` and `range`. 
Where the `range` contains +1 values than the classes specified in the `domain`
For example: `alt.Scale(type='threshold', domain=[0.05, 0.20], range=['blue','white','red'])`
In this `blue` is the class for all values below `0.05`, `white` for all values between 
`0.05` and `0.20` and `red` for all values above `0.20`.
- The natural breaks method will determine the optimal class breaks given the required 
number of classes. But how many classes should one pick? One can investigate usage of 
goodness of variance fit (GVF), aka Jenks optimization method, to determine this.


Repeat a Map
~~~~~~~~~~~~
The :class:`RepeatChart` pattern, accessible via the :meth:`Chart.repeat` method 
provides a convenient interface for a particular type of horizontal or vertical 
concatenation of a multi-dimensional dataset.

In the following example we have a dataset referenced as `source` from which we use 
three columns defining the `population`, `engineers` and `hurricanes` of each US state.

The `states` is defined by making use of :func:`topo_feature` using `url` and `feature`
as parameters. This is a convenience function for extracting features from a topojson url.

These variables we provide as list in the `.repeat()` operator, which we refer to within
the color encoding as `alt.repeat('row')`

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    states = alt.topo_feature(data.us_10m.url, 'states')
    source = data.population_engineers_hurricanes.url
    variable_list = ['population', 'engineers', 'hurricanes']

    alt.Chart(states).mark_geoshape(tooltip=True).encode(
        alt.Color(alt.repeat('row'), type='quantitative')
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(source, 'id', variable_list)
    ).project(
        type='albersUsa'
    ).repeat(
        row=variable_list
    ).resolve_scale(
        color='independent'
    )

Facet a Map
~~~~~~~~~~~
The :class:`FacetChart` pattern, accessible via the :meth:`Chart.facet` method 
provides a convenient interface for a particular type of horizontal or vertical 
concatenation of a dataset where one field contain multiple `variables`.

Unfortuantely, the following open issue https://github.com/altair-viz/altair/issues/2369 
will make the following not work for geographic visualization:

.. altair-plot::

    source = data.population_engineers_hurricanes().melt(id_vars=['state', 'id'])
    us_states = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='states')  
    gdf_comb = gpd.GeoDataFrame(source.join(us_states, on='id', rsuffix='_y'))

    alt.Chart(gdf_comb).mark_geoshape().encode(
        color=alt.Color('value:Q'),
        facet=alt.Facet('variable:N', columns=3)
    ).properties(
        width=200,
        height=200
    ).resolve_scale('independent')

For now, the following workaround can be adopted to facet a map, manually filter the 
data in pandas, and create a small multiples chart via concatenation. For example:

.. altair-plot::

    alt.concat(*(
        alt.Chart(gdf_comb[gdf_comb.variable == var], title=var).mark_geoshape().encode(
        color='value:Q',
        ).properties(
        width=200
        )
        for var in gdf_comb.variable.unique()
    ), columns=3
    ).resolve_scale(color='independent')


Interaction
~~~~~~~~~~~
Often a map does not come alone, but is used in combination with another chart. 
Here we provide an example of an interactive visualization of a bar chart and a map.

The data shows the states of the US in combination with a bar chart showing the 15 most 
populous states.

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

Expression
~~~~~~~~~~
Altair expressions can be used within a geographical visualization. The following example
visualize earthquakes on the globe using an `orthographic` projection. Where we can rotate
the earth on a single-axis. (`rotate0`). The utility function :func:sphere is adopted to 
get a disk of the earth as background. 

The earthquakes are displayed using a `mark_geoshape` and filtered once out of sight of 
the the visible part of the world.

An hover highlighting is added to get more insight of each earthquake.

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    # load data
    gdf_quakies = gpd.read_file(data.earthquakes.url, driver='GeoJSON')
    gdf_world = gpd.read_file(data.world_110m.url, driver='TopoJSON')

    # define parameters
    range0 = alt.binding_range(min=-180, max=180, step=5)
    rotate0 = alt.parameter(value=120, bind=range0, name='rotate0')
    hover = alt.selection_point(on='mouseover', clear='mouseout')

    # world disk
    sphere = alt.Chart(alt.sphere()).mark_geoshape(
        fill='aliceblue', 
        stroke='black',
        strokeWidth=1.5
    )

    # countries as shapes
    world = alt.Chart(gdf_world).mark_geoshape(
        fill='mintcream', 
        stroke='black', 
        strokeWidth=0.35
    )

    # earthquakes as circles with fill for depth and size for magnitude
    # the hover param is added on the mar_circle only
    quakes = alt.Chart(gdf_quakies).mark_circle(
        opacity=0.35,
        tooltip=True,
        stroke='black'
    ).transform_calculate(
        lon="datum.geometry.coordinates[0]",
        lat="datum.geometry.coordinates[1]",
        depth="datum.geometry.coordinates[2]"
    ).transform_filter('''
        (rotate0 * -1) - 90 < datum.lon && datum.lon < (rotate0 * -1) + 90
        '''
    ).encode(
        longitude='lon:Q',    
        latitude='lat:Q',
        strokeWidth=alt.condition(hover, alt.value(1, empty=False), alt.value(0)),
        size=alt.Size('mag:Q', scale=alt.Scale(type='pow', range=[1,1000], domain=[0,6], exponent=4)),
        fill=alt.Fill('depth:Q', scale=alt.Scale(scheme='lightorange', domain=[0,400]))
    ).add_parameter(hover)

    # define projection and add the rotation param for all layers
    comb = alt.layer(sphere, world, quakes).project(
        'orthographic',
        rotate=[90, 0, 0]
    ).add_parameter(rotate0)

    # temporary changing params to top-level
    # and defining the rotate reference expression on compiled VL directly
    chart_vl = comb.to_dict()
    chart_vl['params'] =  chart_vl['layer'][0].pop('params')
    chart_vl['projection']['rotate'] = {'expr':'[rotate0, 0, 0]'}
    alt.Chart().from_dict(chart_vl)

Geoshape Options
~~~~~~~~~~~~~~~~

Additional arguments to ``mark_geoshape()`` method are passed along to an
associated :class:`MarkDef` instance, which supports the following attributes:

.. altair-object-table:: altair.MarkDef

Marks can also be configured globally using chart-level configurations; see
:ref:`config-mark` for details.
