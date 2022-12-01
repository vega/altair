.. currentmodule:: altair

.. _user-guide-rect-marks:

Rect
~~~~

The ``rect`` mark represents an arbitrary rectangle.

Rect Mark Properties
--------------------
.. altair-plot::
    :hide-code:
    :div_class: properties-example

    import altair as alt

    x_slider = alt.binding_range(min=1, max=100, step=1, name="x")
    x_var = alt.param(bind=x_slider, value=25)

    x2_slider = alt.binding_range(min=1, max=100, step=1, name="x2")
    x2_var = alt.param(bind=x2_slider, value=75)

    y_slider = alt.binding_range(min=1, max=100, step=1, name="y")
    y_var = alt.param(bind=y_slider, value=25)

    y2_slider = alt.binding_range(min=1, max=100, step=1, name="y2")
    y2_var = alt.param(bind=y2_slider, value=75)

    cornerRadius_slider = alt.binding_range(min=0, max=50, step=1)
    cornerRadius_var = alt.param(bind=cornerRadius_slider, value=0, name="cornerRadius")

    alt.Chart().mark_rect(cornerRadius=cornerRadius_var, color="orange").encode(
        x=alt.XDatum(x_var, type="quantitative", scale=alt.Scale(domain=[0, 100])),
        x2=alt.X2Datum(x2_var),
        y=alt.XDatum(y_var, type="quantitative", scale=alt.Scale(domain=[0, 100])),
        y2=alt.X2Datum(y2_var),
    ).add_params(x_var, x2_var, y_var, y2_var, cornerRadius_var)


A ``rect`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: width height align baseline cornerRadius

Examples
--------
Heatmap
^^^^^^^

Using the ``rect`` marks with discrete fields on ``x`` and ``y`` channels creates a heatmap.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_rect().encode(
        alt.X("date(date):O", title="Day", axis=alt.Axis(labelAngle=0, format="%e")),
        alt.Y("month(date):O", title="Month"),
        alt.Color("max(temp_max):Q", title="Max Temp"),
    )


Ranged Rectangles
^^^^^^^^^^^^^^^^^
Specifying both ``x`` and ``x2`` and/or ``y`` and ``y2`` creates a rectangle that spans over certain x and/or y values.

For example, we can use ``rect`` to create an annotation ``layer`` that provides a shading between global ``min`` and ``max`` values.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    point = alt.Chart(source).mark_point().encode(x="Horsepower:Q", y="Miles_per_Gallon:Q")

    rect = (
        alt.Chart(source)
        .mark_rect()
        .encode(
            y="max(Miles_per_Gallon)", y2="min(Miles_per_Gallon)", opacity=alt.value(0.2)
        )
    )

    point + rect

