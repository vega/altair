.. currentmodule:: altair

.. _user-guide-rect-marks:

Rect
~~~~

The ``rect`` mark represents an arbitrary rectangle.

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
        alt.X('date(date):O', title = 'Day', axis = alt.Axis(labelAngle = 0, format = '%e')),
        alt.Y('month(date):O', title = 'Month'),
        alt.Color('max(temp_max):Q', title = "Max Temp")
    )

Ranged Rectangles
^^^^^^^^^^^^^^^^^
Specifying both ``x`` and ``x2`` and/or ``y`` and ``y2`` creates a rectangle that spans over certain x and/or y values.

For example, we can use ``rect`` to create an annotation ``layer`` that provides a shading between global ``min`` and ``max`` values.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source =  data.cars()

    point = alt.Chart(source).mark_point().encode(
        x = 'Horsepower:Q',
        y = 'Miles_per_Gallon:Q'
    )

    rect = alt.Chart(source).mark_rect().encode(
        y = 'max(Miles_per_Gallon)',
        y2 = 'min(Miles_per_Gallon)',
        opacity = alt.value(0.2)
    )

    point + rect

Rect Config 
^^^^^^^^^^^
The ``rect`` property of the top-level ``config`` object sets the default properties for all rect marks. If mark property encoding channels are specified for marks, these config values will be overridden.

The rect config can contain any rect mark properties (except ``type``, ``style``, and ``clip``).