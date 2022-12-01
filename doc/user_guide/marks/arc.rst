.. currentmodule:: altair

.. _user-guide-arc-marks:

Arc
~~~

Arc marks are circular arcs defined by a center point plus angular and radial extents.
Arc marks are typically used for radial plots such as pie and donut charts.

Arc Mark Properties
-------------------
.. altair-plot::
    :hide-code:
    :div_class: properties-example

    import altair as alt
    import numpy as np
    import pandas as pd

    rad_slider = alt.binding_range(min=0, max=100, step=1)
    rad_var = alt.param(bind=rad_slider, value=0, name="radius")

    rad2_slider = alt.binding_range(min=0, max=100, step=1)
    rad_var2 = alt.param(bind=rad_slider, value=50, name="radius2")

    theta_slider = alt.binding_range(min=-2 * np.pi, max=2 * np.pi)
    theta_var = alt.param(bind=theta_slider, value=-0.73, name="theta_single_arc")

    theta_slider2 = alt.binding_range(min=-2 * np.pi, max=2 * np.pi)
    theta2_var = alt.param(bind=theta_slider, value=0.73, name="theta2_single_arc")

    corner_slider = alt.binding_range(min=0, max=50, step=1)
    corner_var = alt.param(bind=corner_slider, value=0, name="cornerRadius")

    pad_slider = alt.binding_range(min=0, max=np.pi / 2)
    pad_var = alt.param(bind=pad_slider, value=0, name="padAngle")

    source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

    c1 = alt.Chart(source, title="Single Arc").mark_arc(
        radius=rad_var,
        radius2=rad_var2,
        theta=theta_var,
        theta2=theta2_var,
        cornerRadius=corner_var,
        padAngle=pad_var,
    )

    c2 = (
        alt.Chart(source, title="Stacked Arcs")
        .mark_arc(
            radius=rad_var,
            radius2=rad_var2,
            cornerRadius=corner_var,
            padAngle=pad_var,
        )
        .encode(
            theta=alt.Theta(field="value", type="quantitative"),
            color=alt.Color(field="category", type="nominal"),
        )
    )

    alt.hconcat(c1.properties(width=200), c2.properties(width=200)).add_params(
        rad_var, rad_var2, theta_var, theta2_var, corner_var, pad_var
    )

An ``arc`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: radius radius2 innerRadius outerRadius theta theta2 cornerRadius padAngle radiusOffset radius2Offset thetaOffset theta2Offset

Examples
--------

We can create a pie chart by encoding ``theta`` or ``color`` arc marks.

.. altair-plot::
    import pandas as pd
    import altair as alt

    source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

    alt.Chart(source).mark_arc().encode(
        theta=alt.Theta(field="value", type="quantitative"),
        color=alt.Color(field="category", type="nominal"),
    )


Setting ``innerRadius`` to non-zero values will create a donut chart.

.. altair-plot::
    import pandas as pd
    import altair as alt

    source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

    alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="value", type="quantitative"),
        color=alt.Color(field="category", type="nominal"),
    )


You can also add a text layer to add labels to a pie chart.

.. altair-plot::
    import pandas as pd
    import altair as alt

    source = pd.DataFrame(
        {"category": ["a", "b", "c", "d", "e", "f"], "value": [4, 6, 10, 3, 7, 8]}
    )

    base = alt.Chart(source).encode(
        theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
    )

    pie = base.mark_arc(outerRadius=120)
    text = base.mark_text(radius=140, size=20).encode(text="category:N")

    pie + text

