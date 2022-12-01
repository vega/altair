.. currentmodule:: altair

.. _user-guide-text-marks:

Text
~~~~~~
``text`` mark represents each data point with a text instead of a point.

Text Mark Properties
--------------------
.. altair-plot::
    :hide-code:
    :div_class: properties-example

    import altair as alt
    import pandas as pd

    angle_slider = alt.binding_range(min=-180, max=180, step=1)
    angle_var = alt.param(bind=angle_slider, value=0, name="angle")

    dx_slider = alt.binding_range(min=-20, max=20, step=1)
    dx_var = alt.param(bind=dx_slider, value=5, name="dx")

    dy_slider = alt.binding_range(min=-20, max=20, step=1)
    dy_var = alt.param(bind=dy_slider, value=0, name="dy")

    xOffset_slider = alt.binding_range(min=-20, max=20, step=1)
    xOffset_var = alt.param(bind=xOffset_slider, value=0, name="xOffset")

    yOffset_slider = alt.binding_range(min=-20, max=20, step=1)
    yOffset_var = alt.param(bind=yOffset_slider, value=0, name="yOffset")

    fontSize_slider = alt.binding_range(min=1, max=36, step=1)
    fontSize_var = alt.param(bind=fontSize_slider, value=14, name="fontSize")

    limit_slider = alt.binding_range(min=0, max=150, step=1)
    limit_var = alt.param(bind=limit_slider, value=0, name="limit")

    align_select = alt.binding_select(options=["left", "center", "right"])
    align_var = alt.param(bind=align_select, value="left", name="align")

    baseline_select = alt.binding_select(options=["alphabetic", "top", "middle", "bottom"])
    baseline_var = alt.param(bind=baseline_select, value="midle", name="baseline")

    font_select = alt.binding_select(options=["sans-serif", "serif", "monospace"])
    font_var = alt.param(bind=font_select, value="sans-serif", name="font")

    fontWeight_select = alt.binding_select(options=["normal", "bold"])
    fontWeight_var = alt.param(bind=fontWeight_select, value="normal", name="fontWeight")

    fontStyle_select = alt.binding_select(options=["normal", "italic"])
    fontStyle_var = alt.param(bind=fontStyle_select, value="normal", name="fontStyle")

    source = pd.DataFrame(
        {
            "a": [30, 25, 70],
            "b": [28, 65, 43],
            "label": ["Andy", "Brian", "Charlie"],
        }
    )

    base = alt.Chart(source).encode(
        x=alt.X("a:Q", axis=alt.Axis(labelAngle=0), scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("b:Q", scale=alt.Scale(domain=[0, 100])),
    )

    pts = base.mark_point()

    text = base.mark_text(
        dx=dx_var,
        dy=dy_var,
        xOffset=xOffset_var,
        yOffset=yOffset_var,
        angle=angle_var,
        align=align_var,
        baseline=baseline_var,
        font=font_var,
        fontSize=fontSize_var,
        fontStyle=fontStyle_var,
        fontWeight=fontWeight_var,
        limit=limit_var,
    ).encode(text="label:N")

    (pts + text).add_params(
        dx_var,
        dy_var,
        xOffset_var,
        yOffset_var,
        angle_var,
        align_var,
        baseline_var,
        font_var,
        fontSize_var,
        fontStyle_var,
        fontWeight_var,
        limit_var,
    )


A ``text`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: angle align baseline dir dx dy ellipsis font fontSize fontStyle fontWeight limit lineHeight radius text theta

Examples
--------
Text Table Heatmap
^^^^^^^^^^^^^^^^^^
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    base = (
        alt.Chart(source)
        .transform_aggregate(num_cars="count()", groupby=["Origin", "Cylinders"])
        .encode(
            alt.X("Cylinders:O", scale=alt.Scale(paddingInner=0)),
            alt.Y("Origin:O", scale=alt.Scale(paddingInner=0)),
        )
    )

    heatmap = base.mark_rect().encode(
        color=alt.Color(
            "num_cars:Q",
            scale=alt.Scale(scheme="viridis"),
            legend=alt.Legend(direction="horizontal"),
        )
    )

    text = base.mark_text(baseline="middle").encode(
        text="num_cars:Q",
        color=alt.condition(
            alt.datum.num_cars > 100, alt.value("black"), alt.value("white")
        ),
    )

    heatmap + text

Labels
^^^^^^
You can also use ``text`` marks as labels for other marks and set offset (``dx`` or ``dy``), ``align``, and ``baseline`` properties of the mark definition.

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({"a": ["A", "B", "C"], "b": [28, 55, 43]})

    bar = (
        alt.Chart(source)
        .mark_bar()
        .encode(y="a:N", x=alt.X("b:Q", scale=alt.Scale(domain=[0, 60])))
    )
    text = bar.mark_text(align="left", baseline="middle", dx=3).encode(text="b")

    bar + text

Scatter Plot with Text
^^^^^^^^^^^^^^^^^^^^^^
Mapping a field to ``text`` channel of text mark sets the mark’s text value. For example, we can make a colored scatter plot with text marks showing the initial character of its origin, instead of ``point`` marks.

.. altair-plot::
    import altair as alt
    from vega_datasets import data
    from altair import datum

    source = data.cars()

    alt.Chart(source).mark_text().encode(
        x="Horsepower:Q", y="Miles_per_Gallon:Q", color="Origin:N", text="Origin[0]:N"
    )

Geo Text
^^^^^^^^
By mapping geographic coordinate data to ``longitude`` and ``latitude`` channels of a corresponding projection, we can show text at accurate locations. The example below shows the name of every US state capital at the location of the capital.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    states = alt.topo_feature(data.us_10m.url, feature="states")

    source = data.us_state_capitals()

    background = (
        alt.Chart(states)
        .mark_geoshape(fill="lightgray", stroke="white")
        .properties(width=750, height=500)
        .project("albersUsa")
    )

    line = (
        alt.Chart(source)
        .mark_text(dy=-10)
        .encode(latitude="lat:Q", longitude="lon:Q", text="city:N")
    )

    point = (
        alt.Chart(source)
        .mark_circle()
        .encode(latitude="lat:Q", longitude="lon:Q", color=alt.value("orange"))
    )

    background + line + point
