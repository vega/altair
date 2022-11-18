.. currentmodule:: altair

.. _user-guide-point-marks:

Point
~~~~~
``point`` mark represents each data point with a symbol. Point marks are commonly used in visualizations like scatter plots.

Point Mark Properties
---------------------
A ``point`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: shape size

Examples
--------
Dot Plot
^^^^^^^^
Mapping a field to either only ``x`` or only ``y`` of point marks creates a dot plot.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.movies()
    alt.Chart(source).mark_point().encode(x="IMDB_Rating:Q")

Scatter Plot
^^^^^^^^^^^^
Mapping fields to both the ``x`` and ``y`` channels creates a scatter plot.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_point().encode(x="Horsepower:Q", y="Miles_per_Gallon:Q")

By default, ``point`` marks only have borders and are transparent inside. You can create a filled point by setting ``filled`` to ``True``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_point(filled=True).encode(
        x="Horsepower:Q", y="Miles_per_Gallon:Q"
    )

Bubble Plot
^^^^^^^^^^^
By mapping a third field to the ``size`` channel in the scatter plot, we can create a bubble plot instead.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_point().encode(
        x="Horsepower:Q", y="Miles_per_Gallon:Q", size="Acceleration:Q"
    )

Scatter Plot with Color and/or Shape
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fields can also be encoded in the scatter plot using the ``color`` or ``shape`` channels. For example, this specification encodes the field ``Origin`` with both ``color`` and ``shape``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_point().encode(
        alt.X("Miles_per_Gallon:Q", scale=alt.Scale(zero=False)),
        alt.Y("Horsepower:Q", scale=alt.Scale(zero=False)),
        color="Origin:N",
        shape="Origin:N",
    )


Dot Plot with Jittering
^^^^^^^^^^^^^^^^^^^^^^^
To jitter points on a discrete scale, you can add a random offset:

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_point().encode(
        x="Horsepower:Q", y="Cylinders:O", yOffset="random:Q"
    ).transform_calculate(random="random()").properties(height=alt.Step(50))

Wind Vector Example
^^^^^^^^^^^^^^^^^^^
We can also use point mark with ``wedge`` as ``shape`` and ``angle`` encoding to create a wind vector map. Other shape options are:
``"circle"``, ``"square"``, ``"cross"``, ``"diamond"``, ``"triangle-up"``, ``"triangle-down"``, ``"triangle-right"``, ``"triangle-left"``, ``"stroke"``, ``"arrow"``, and ``"triangle"``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.windvectors()

    alt.Chart(source).mark_point(shape="wedge", filled=True).encode(
        latitude="latitude",
        longitude="longitude",
        color=alt.Color(
            "dir", scale=alt.Scale(domain=[0, 360], scheme="rainbow"), legend=None
        ),
        angle=alt.Angle("dir", scale=alt.Scale(domain=[0, 360], range=[180, 540])),
        size=alt.Size("speed", scale=alt.Scale(rangeMax=500)),
    ).project("equalEarth")

Geo Point
^^^^^^^^^
By mapping geographic coordinate data to ``longitude`` and ``latitude`` channels of a corresponding projection, we can visualize geographic points. The example below shows major airports in the US.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    airports = data.airports()
    states = alt.topo_feature(data.us_10m.url, feature="states")

    # US states background
    background = (
        alt.Chart(states)
        .mark_geoshape(fill="lightgray", stroke="white")
        .properties(width=500, height=300)
        .project("albersUsa")
    )

    # airport positions on background
    points = (
        alt.Chart(airports)
        .mark_circle(size=10, color="steelblue")
        .encode(
            longitude="longitude:Q",
            latitude="latitude:Q",
            tooltip=["name", "city", "state"],
        )
    )

    background + points

