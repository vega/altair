.. currentmodule:: altair

.. _user-guide-tick-marks:

Tick
~~~~
The ``tick`` mark represents each data point as a short line. This is a useful mark for displaying the distribution of values in a field.

Examples 
--------
Dot Plot 
^^^^^^^^
The following dot plot uses tick marks to show the distribution of precipitation in Seattle.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_tick().encode(
        x='precipitation:Q'
    )
Strip Plot
^^^^^^^^^^
By adding a ``y`` field, a strip plot can be created that shows the distribution of horsepower by number of cylinders. 

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_tick().encode(
        x='Horsepower:Q',
        y='Cylinders:O'
    )

Tick Config 
^^^^^^^^^^^
The ``tick`` property of the top-level ``config`` object sets the default properties for all tick marks. If mark property encoding channels are specified for marks, these config values will be overridden.

Besides standard mark config properties, tick config can contain the following additional properties: ``bandSize`` and ``thickness``. 

Customizing Tick’s Size and Thickness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_tick().encode(
        x='precipitation:Q'
    ).configure_tick(
        thickness = 2,
        bandSize = 10
    )