.. currentmodule:: altair

.. _user-guide-tick-marks:

Tick
~~~~
The ``tick`` mark represents each data point as a short line. This is a useful mark for displaying the distribution of values in a field.

Tick Mark Properties
--------------------
A ``tick`` mark definition can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: cornerRadius orient

Examples
--------
Dot Plot
^^^^^^^^
The following dot plot uses tick marks to show the distribution of precipitation in Seattle.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_tick().encode(x="precipitation:Q")

Strip Plot
^^^^^^^^^^
By adding a ``y`` field, a strip plot can be created that shows the distribution of horsepower by number of cylinders.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_tick().encode(x="Horsepower:Q", y="Cylinders:O")


Customizing Tick’s Size and Thickness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.seattle_weather()

    alt.Chart(source).mark_tick().encode(x="precipitation:Q").configure_tick(
        thickness=2, bandSize=10
    )
