.. currentmodule:: altair

.. _user-guide-arc-marks:

Arc
~~~

Arc marks are circular arcs defined by a center point plus angular and radial extents. 
Arc marks are typically used for radial plots such as pie and donut charts.

Examples
--------

We can create a pie chart by encoding ``theta`` or ``color`` arc marks.

.. altair-plot::
    import pandas as pd
    import altair as alt

    source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

    alt.Chart(source).mark_arc().encode(
        theta=alt.Theta(
            field="value", 
            type="quantitative"),
        color=alt.Color(
            field="category", 
            type="nominal"),
        )

Setting ``innerRadius`` to non-zero values will create a donut chart. 

.. altair-plot::
    import pandas as pd
    import altair as alt

    source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

    alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(
            field="value", 
            type="quantitative"),
        color=alt.Color(
            field="category", 
            type="nominal"),
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

Area Config 
^^^^^^^^^^^
The ``arc`` property of the top-level ``config`` object sets the default properties for all arc marks. If mark property encoding channels are specified for marks, these config values will be overridden.

The area config can contain any area mark properties (except ``type``, ``style``, and ``clip``).
