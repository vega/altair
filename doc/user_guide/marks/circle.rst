.. currentmodule:: altair

.. _user-guide-circle-marks:

Circle 
~~~~~~

``circle`` mark is similar to ``point`` mark, except that (1) the ``shape`` value is always set to ``circle`` (2) they are filled by default.

Scatterplot with Circle 
^^^^^^^^^^^^^^^^^^^^^^^

Here is an example scatter plot with ``circle`` marks:

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    alt.Chart(source).mark_circle().encode(
        x = ('Horsepower:Q'),
        y = ('Miles_per_Gallon:Q')
    )

Circle Config 
^^^^^^^^^^^^^

The ``circle`` property of the top-level ``config`` object sets the default properties for all circle marks. If mark property encoding channels are specified for marks, these config values will be overridden.

The circle config can contain any circle mark properties (except ``type``, ``style``, and ``clip``).