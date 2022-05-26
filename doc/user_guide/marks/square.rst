.. currentmodule:: altair

.. _user-guide-square-marks:

Square
~~~~~~
``square`` marks is similar to ``point`` mark, except that (1) the ``shape`` value is always set to ``square`` (2) they are filled by default.

Scatterplot with Square 
-----------------------
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source =  data.cars()

    alt.Chart(source).mark_square().encode(
        x = 'Horsepower:Q',
        y = 'Miles_per_Gallon:Q'
    )

Square Config 
^^^^^^^^^^^^^
The ``square`` property of the top-level ``config`` object sets the default properties for all square marks. If mark property encoding channels are specified for marks, these config values will be overridden.

The square config can contain any point mark properties (except ``type``, ``style``, and ``clip``).