.. currentmodule:: altair

.. _user-guide-geoshape-marks:

Geoshape
^^^^^^^^^^^^^
``mark_geoshape`` represents an arbitrary shapes whose geometry is determined by specified spatial data.

Basic Map
^^^^^^^^^
Altair can work with many different geographical data formats, including geojson and topojson files. Often, the most convenient input format to use is a ``GeoDataFrame``. Here we load the Natural Earth dataset and create a basic map using ``mark_geoshape``:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    fp = gpd.datasets.get_path('naturalearth_lowres')
    gdf_ne = gpd.read_file(fp)  # shapefile

    alt.Chart(gdf_ne).mark_geoshape()

In the example above, Altair applies a default blue ``fill`` color and uses a default map projection (``equalEarth``). We can customize the colors and boundary stroke widths using standard mark properties. Using the ``project`` method we can also define a custom map projection manually:

.. altair-plot::

    alt.Chart(gdf_ne).mark_geoshape(
        fill='lightgrey', stroke='white', strokeWidth=0.5
    ).project(
        type='albers'
    )

Focus & Filtering
^^^^^^^^^^^^^^^^^
By default Altair automatically adjusts the projection so that all the data fits within the width and height of the chart.
Multiple approaches can be used to focus on specific regions of your spatial data. Namely:

1. Filter the source data within your GeoDataFrame.
2. Filter the source data using a ``transform_filter``.
3. Specify ``scale`` (zoom level) and ``translate`` (panning) within the ``project`` method.
4. Specify ``fit`` (extent) within the ``project`` & ``clip=True`` in the mark properties.

The following examples applies these approaches to focus on continental Africa:

1. Filter the source data within your GeoDataFrame:

.. altair-plot::

    gdf_sel = gdf_ne[gdf_ne.continent == 'Africa']

    alt.Chart(gdf_sel).mark_geoshape()

2. Filter the source data using a ``transform_filter``:

.. altair-plot::

    alt.Chart(gdf_ne).mark_geoshape().transform_filter(
        alt.datum.continent == 'Africa'
    )

3. Specify ``scale`` (zoom level) and ``translate`` (panning) within the ``project`` method:

.. altair-plot::

    alt.Chart(gdf_ne).mark_geoshape().project(
        scale=200,
        translate=[160, 160]  # lon, lat
    )

3. Specify ``fit`` (extent) within the ``project`` method & ``clip=True`` in the mark properties:

.. altair-plot::

    from shapely.ops import orient
    from shapely.geometry import mapping

    extent_roi = gdf_ne.query("continent == 'Africa'").unary_union.envelope

    # fit object should be an array of GeoJSON-like features
    # order polygon exterior needs to be clock-wise (left-hand-rule)
    if extent_roi.exterior.is_ccw:
        extent_roi = orient(extent_roi, -1)
    extent_roi_geojson = [mapping(extent_roi)]

    alt.Chart(gdf_ne).mark_geoshape(clip=True).project(
        fit=extent_roi_geojson
    )

Cartesian coordinates
^^^^^^^^^^^^^^^^^^^^^
The default projection of Altair is ``equalEarth``, which accurately represents the areas of the world's landmasses relative each other. This default assumes that your geometries are in degrees and referenced by longitude and latitude values.
Another widely used coordinate system for data visualization is the 2d cartesian coordinate system. This coordinate system does not take into account the curvature of the Earth.

In the following example the input geometry is not projected and is instead rendered directly in raw coordinates using the ``identity`` projection type. We have to define the ``reflectY`` as well since Canvas and SVG treats positive ``y`` as pointing down.

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape().project(
        type='identity',
        reflectY=True
    )

Mapping Polygons
^^^^^^^^^^^^^^^^
The following example maps the visual property of the ``name`` column using the ``color`` encoding.

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape().encode(
        color='name:N'
    )

Since each country is represented by a (multi)polygon, we can separate the ``stroke`` and ``fill`` definitions as such:

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape(
        stroke='white',
        strokeWidth=1.5
    ).encode(
        fill='name:N'
    )

Mapping Lines
^^^^^^^^^^^^^
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
    )

Mapping Points
^^^^^^^^^^^^^^
Points can be drawn when they are defined as ``Points`` within a GeoDataFrame using ``mark_geoshape``.
We first assign the centroids of Polygons as Point geometry and plot these:

.. altair-plot::

    gdf_centroid = gpd.GeoDataFrame(
        data=gdf_sel.copy(),  # .copy() to prevent changing the original `gdf_sel` variable
        geometry=gdf_sel.geometry.centroid
    )

    alt.Chart(gdf_centroid).mark_geoshape()


Caveat: To use the ``size`` encoding for the Points you will need to use the ``mark_circle`` in combination with the ``latitude`` and ``longitude`` encoding channel definitions.

.. altair-plot::

    gdf_centroid["lon"] = gdf_centroid.geometry.x
    gdf_centroid["lat"] = gdf_centroid.geometry.y

    alt.Chart(gdf_centroid).mark_circle().encode(
        longitude="lon:Q", latitude="lat:Q", size="pop_est:Q"
    )

Altair also contains expressions related to geographical features. We can for example define the ``centroids`` using a ``geoCentroid`` expression:

.. altair-plot::

    from altair.expr import datum, geoCentroid

    basemap = alt.Chart(gdf_sel).mark_geoshape(
         fill='lightgray', stroke='white', strokeWidth=0.5
    )

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

Choropleths
^^^^^^^^^^^

An alternative to showing the population sizes as bubbles, is to create a "Choropleth" map. These are geographical heatmaps where the color or each region are mapped to the values of a column in the dataframe.

.. altair-plot::

    alt.Chart(gdf_sel).mark_geoshape().encode(
        color='pop_est'
    )

When we create choropleth maps, we need to be careful, because although the color changes according to the value of the column we are interested in, the size is tied to the area of each country and we might miss interesting values in small countries just because we can't easily see them on the map (e.g. if we were to visualize population density).

Lookup datasets
^^^^^^^^^^^^^^^
Sometimes your data is separated in two datasets. One ``DataFrame`` with the data and one ``GeoDataFrame`` with the geometries.
In this case you can use the ``lookup`` transform to collect related information from the other dataset.

You can use the ``lookup`` transform in two directions:

1. Use a ``GeoDataFrame`` with geometries as source and lookup related information in another ``DataFrame``.
2. Use a ``DataFrame`` as source and lookup related geometries in a ``GeoDataFrame``.

Depending on your use-case one or the other is more favorable.

First we show an example of the first approach.
Here we lookup the field ``rate`` from the ``df_us_unemp`` DataFrame, where the ``gdf_us_counties`` GeoDataFrame is used as source:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    gdf_us_counties = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='counties')
    df_us_unemp = data.unemployment()

    alt.Chart(gdf_us_counties).mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(data=df_us_unemp, key='id', fields=['rate'])
    ).encode(
        alt.Color('rate:Q')
    ).project(
        type='albersUsa'
    )

Next, we show an example of the second approach.
Here we lookup the geometries through the fields ``geometry`` and ``type`` from the ``gdf_us_counties`` GeoDataFrame, where the ``df_us_unemp`` DataFrame is used as source.

.. altair-plot::

    alt.Chart(df_us_unemp).mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(data=gdf_us_counties, key='id', fields=['geometry', 'type'])
    ).encode(
        alt.Color('rate:Q')
    ).project(
        type='albersUsa'
    )

Choropleth Classification
^^^^^^^^^^^^^^^^^^^^^^^^^
In addition to displaying a continuous quantitative variable, choropleths can also be used to show discrete levels of a variable. While we should generally be careful to not create artificial groups when discretizing a continuous variable, it can be very useful when we have natural cutoff levels of a variable that we want to showcase clearly.
We first define a utility function ``classify()`` that we will use to showcase different approaches to make a choropleth map.
We apply it to define a choropleth map of the unemployment statistics of 2018 of US counties using a ``linear`` scale.

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    def classify(type, breaks=None, nice=False, title=None):
        # define data
        us_counties = alt.topo_feature(data.us_10m.url, "counties")
        us_unemp = data.unemployment.url

        # define choropleth scale
        if "threshold" in type:
            scale = alt.Scale(type=type, domain=breaks, scheme="inferno")
        else:
            scale = alt.Scale(type=type, nice=nice, scheme="inferno")

        # define title
        if title is None:
            title = type

        # define choropleth chart
        choropleth = (
            alt.Chart(us_counties, title=title)
            .mark_geoshape()
            .transform_lookup(
                lookup="id", from_=alt.LookupData(data=us_unemp, key="id", fields=["rate"])
            )
            .encode(
                alt.Color(
                    "rate:Q",
                    scale=scale,
                    legend=alt.Legend(
                        direction="horizontal", orient="bottom", format=".1%"
                    ),
                )
            )
            .project(type="albersUsa")
        )
        return choropleth

    classify(type='linear')

We visualize the unemployment ``rate`` in percentage of 2018 with a ``linear`` scale range
using a ``mark_geoshape()`` to present the spatial patterns on a map. Each value/
county has defined a `unique` color. This gives a bit of insight, but often we like to
group the distribution into classes.

By grouping values in classes, you can classify the dataset so all values/geometries in
each class get assigned the same color.

Here we present a number of scale methods how Altair can be used:

- ``quantile``, this type will divide your dataset (`domain`) into intervals of similar sizes. Each class contains more or less the same number of values/geometries (`equal counts`). The scale definition will look as follow:

.. code:: python

    alt.Scale(type='quantile')

And applied in our utility function:

.. altair-plot::

    classify(type='quantile', title=['quantile', 'equal counts'])

- ``quantize``, this type will divide the extent of your dataset (`range`) in equal intervals. Each class contains different number of values, but the step size is equal (`equal range`). The scale definition will look as follow:

.. code:: python

    alt.Scale(type='quantize')

And applied in our utility function:

.. altair-plot::

    classify(type='quantize', title=['quantile', 'equal range'])


The ``quantize`` method can also be used in combination with ``nice``. This will `"nice"` the domain before applying quantization. As such:

.. code:: python

    alt.Scale(type='quantize', nice=True)

And applied in our utility function:

.. altair-plot::

    classify(type='quantize', nice=True, title=['quantize', 'equal range nice'])

- ``threshold``, this type will divide your dataset in separate classes by manually specifying the cut values. Each class is separated by defined classes. The scale definition will look as follow:

.. code:: python

    alt.Scale(type='threshold', breaks=[0.05, 0.20])

And applied in our utility function:

.. altair-plot::

    classify(type='threshold', breaks=[0.05, 0.20])

The definition above will create 3 classes. One class with values below `0.05`, one
class with values from `0.05` to `0.20` and one class with values higher than `0.20`.

So which method provides the optimal data classification for choropleth maps? As
usual, it depends.

There is another popular method that aid in determining class breaks.
This method will maximize the similarity of values in a class while maximizing the
distance between the classes (`natural breaks`). The method is also known as the
Fisher-Jenks algorithm and is similar to k-Means in 1D:

-  By using the external Python package ``jenskpy`` we can derive these `optimum` breaks
as such:

.. code:: python

    >>> from jenkspy import JenksNaturalBreaks
    >>> jnb = JenksNaturalBreaks(5)
    >>> jnb.fit(df_us_unemp['rate'])
    >>> jnb.inner_breaks_
    [0.061, 0.088, 0.116, 0.161]

And applied in our utility function:

.. altair-plot::

    classify(type='threshold', breaks=[0.061, 0.088, 0.116, 0.161],
            title=['threshold Jenks','natural breaks'])

Caveats:

- For the type ``quantize`` and ``quantile`` scales we observe that the default number of classes is 5. You can change the number of classes using a ``SchemeParams()`` object. In the above specification we can change ``scheme='turbo'`` into ``scheme=alt.SchemeParams('turbo', count=2)`` to manually specify usage of 2 classes for the scheme within the scale.
- The natural breaks method will determine the optimal class breaks given the required number of classes, but how many classes should you pick? One can investigate usage of goodness of variance fit (GVF), aka Jenks optimization method, to determine this.

Repeat a Map
^^^^^^^^^^^^
The :class:`RepeatChart` pattern, accessible via the :meth:`Chart.repeat` method
provides a convenient interface for a particular type of horizontal or vertical
concatenation of a multi-dimensional dataset.

In the following example we have a dataset referenced as ``source`` from which we use
three columns defining the ``population``, ``engineers`` and ``hurricanes`` of each US state.

The ``states`` is defined by making use of :func:`topo_feature` using ``url`` and ``feature``
as parameters. This is a convenience function for extracting features from a topojson url.

These variables we provide as list in the ``.repeat()`` operator, which we refer to within
the color encoding as ``alt.repeat('row')``

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
^^^^^^^^^^^
The :class:`FacetChart` pattern, accessible via the :meth:`Chart.facet` method
provides a convenient interface for a particular type of horizontal or vertical
concatenation of a dataset where one field contain multiple ``variables``.

Unfortunately, the following open issue https://github.com/altair-viz/altair/issues/2369
will make the following not work for geographic visualization:

.. altair-plot::

    source = data.population_engineers_hurricanes().melt(id_vars=['state', 'id'])
    us_states = gpd.read_file(data.us_10m.url, driver='TopoJSON', layer='states')
    gdf_comb = gpd.GeoDataFrame(source.join(us_states, on='id', rsuffix='_y'))

    alt.Chart(gdf_comb).mark_geoshape().encode(
        color=alt.Color('value:Q'),
        facet=alt.Facet('variable:N', columns=3)
    ).properties(
        width=180,
        height=130
    ).resolve_scale('independent')

For now, the following workaround can be adopted to facet a map, manually filter the
data in pandas, and create a small multiples chart via concatenation. For example:

.. altair-plot::

    alt.concat(
        *(
            alt.Chart(gdf_comb[gdf_comb.variable == var], title=var)
            .mark_geoshape()
            .encode(
                color=alt.Color(
                    "value:Q", legend=alt.Legend(orient="bottom", direction="horizontal")
                )
            )
            .project('albersUsa')
            .properties(width=180, height=130)
            for var in gdf_comb.variable.unique()
        ),
        columns=3
    ).resolve_scale(color="independent")

Interaction
^^^^^^^^^^^
Often a map does not come alone, but is used in combination with another chart.
Here we provide an example of an interactive visualization of a bar chart and a map.

The data shows the states of the US in combination with a bar chart showing the 15 most
populous states. Using an ``alt.selection_point()`` we define a selection parameter that connects to our left-mouseclick.

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    # load the data
    us_states = gpd.read_file(data.us_10m.url, driver="TopoJSON", layer="states")
    us_population = data.population_engineers_hurricanes()[["state", "id", "population"]]

    # define a pointer selection
    click_state = alt.selection_point(fields=["state"])

    # create a choropleth map using a lookup transform
    # define a condition on the opacity encoding depending on the selection
    choropleth = (
        alt.Chart(us_states)
        .mark_geoshape()
        .transform_lookup(
            lookup="id", from_=alt.LookupData(us_population, "id", ["population", "state"])
        )
        .encode(
            color="population:Q",
            opacity=alt.condition(click_state, alt.value(1), alt.value(0.2)),
            tooltip=["state:N", "population:Q"],
        )
        .project(type="albersUsa")
    )

    # create a bar chart with a similar condition on the opacity encoding.
    bars = (
        alt.Chart(
            us_population.nlargest(15, "population"), title="Top 15 states by population"
        )
        .mark_bar()
        .encode(
            x="population",
            opacity=alt.condition(click_state, alt.value(1), alt.value(0.2)),
            color="population",
            y=alt.Y("state", sort="-x"),
        )
    )

    (choropleth & bars).add_params(click_state)


The interaction is two-directional. If you click (shift-click for multi-selection) on a geometry or bar the selection receive an ``opacity`` of ``1`` and the remaining an ``opacity`` of ``0.2``.

Expression
^^^^^^^^^^
Altair expressions can be used within a geographical visualization. The following example
visualize earthquakes on the globe using an ``orthographic`` projection. Where we can rotate
the earth on a single-axis. (``rotate0``). The utility function :func:`sphere` is adopted to
get a disk of the earth as background. The GeoDataFrame with the earthquakes has an ``XYZ``` point geometry, where each coordinate represent ``lon``, ``lat`` and ``depth`` respectively.
We use here an elegant way to access the nested point coordinates from the geometry column directly to draw circles. Using this approach we do not need to assign them to three separate columns first.

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    import geopandas as gpd

    # load data
    gdf_quakies = gpd.read_file(data.earthquakes.url, driver="GeoJSON")
    gdf_world = gpd.read_file(data.world_110m.url, driver="TopoJSON")

    # define parameters
    range0 = alt.binding_range(min=-180, max=180, step=5)
    rotate0 = alt.param(value=120, bind=range0, name='rotate0')
    rotate_param = alt.param(expr=f"[{rotate0.name}, 0, 0]")
    hover = alt.selection_point(on="mouseover", clear="mouseout")

    # world disk
    sphere = alt.Chart(alt.sphere()).mark_geoshape(
        fill="aliceblue", stroke="black", strokeWidth=1.5
    )

    # countries as shapes
    world = alt.Chart(gdf_world).mark_geoshape(
        fill="mintcream", stroke="black", strokeWidth=0.35
    )

    # earthquakes as circles with fill for depth and size for magnitude
    # the hover param is added on the mar_circle only
    quakes = (
        alt.Chart(gdf_quakies)
        .mark_circle(opacity=0.35, tooltip=True, stroke="black")
        .transform_calculate(
            lon="datum.geometry.coordinates[0]",
            lat="datum.geometry.coordinates[1]",
            depth="datum.geometry.coordinates[2]",
        )
        .transform_filter(
            ((rotate0 * -1 - 90 < alt.datum.lon) & (alt.datum.lon < rotate0 * -1 + 90)).expr
        )
        .encode(
            longitude="lon:Q",
            latitude="lat:Q",
            strokeWidth=alt.condition(hover, alt.value(1, empty=False), alt.value(0)),
            size=alt.Size(
                "mag:Q",
                scale=alt.Scale(type="pow", range=[1, 1000], domain=[0, 6], exponent=4),
            ),
            fill=alt.Fill(
                "depth:Q", scale=alt.Scale(scheme="lightorange", domain=[0, 400])
            ),
        )
        .add_params(hover, rotate0)
    )

    # define projection and add the rotation param for all layers
    comb = (
        alt.layer(sphere, world, quakes)
        .project("orthographic", rotate=rotate_param)
        .add_params(rotate_param)
    )
    comb

The earthquakes are displayed using a ``mark_geoshape`` and filtered once out of sight of
the visible part of the world. A hover highlighting is added to get more insight of each earthquake.
