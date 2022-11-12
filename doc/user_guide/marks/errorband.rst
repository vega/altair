.. currentmodule:: altair

.. _user-guide-errorband-marks:

Error Band
~~~~~~~~~~

An error band summarizes an error range of quantitative values using a set of summary statistics, representing by area. Error band in Altair can either be used to aggregate raw data or directly visualize aggregated data.

To create an error band, set ``mark`` to ``"errorband"``.

Comparing the usage of Error Band to the usage of Error Bar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All the properties and usage of error band are identical to error bar’s, except the ``band`` and ``borders`` that replace the error bar’s ``rule`` and ``ticks``.

**Error Band**

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    alt.Chart(source).mark_errorband(extent = 'ci', borders = True).encode(
        x = 'year(Year)',
        y = alt.Y('Miles_per_Gallon:Q', scale=alt.Scale(zero=False), title = 'Miles per Gallon (95% CIs)')
    )

**Error Bar**

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    alt.Chart(source).mark_errorbar(extent = 'ci', ticks = True).encode(
        x = 'year(Year)',
        y = alt.Y('Miles_per_Gallon:Q', scale=alt.Scale(zero=False), title = 'Miles per Gallon (95% CIs)')
    )

Using Error Band to Aggregate Raw Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the data is not aggregated yet, Altair will aggregate the data based on the ``extent`` properties in the mark definition as done in the error band showing confidence interval above. All other ``extent`` values are defined in Error Bar.

Using Error Band to Visualize Aggregated Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Data is aggregated with low and high values of the error band
If the data is already pre-aggregated with low and high values of the error band, you can directly specify ``x`` and ``x2`` (or ``y`` and ``y2``) to use error band as a ranged mark.

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({
        'ci1': [23.5007, 25.8214, 26.4472, 27.7074],
        'ci0': [19.6912, 20.8554, 21.9749, 22.6203],
        'center': [21.5735, 23.3750, 24.0611, 25.0931],
        'Year': [189302400000, 220924800000, 252460800000, 283996800000]
    })

    band = alt.Chart(source).mark_errorband().encode(
        alt.Y('ci1:Q', scale=alt.Scale(zero=False), title = 'Mean of Miles per Gallon (95% CIs)'),
        alt.Y2('ci0:Q'),
        alt.X('year(Year)')
    )

    line = alt.Chart(source).mark_line().encode(
        alt.Y('center:Q'),
        alt.X('year(Year)')
    )

    band + line

2. Data is aggregated with center and error value(s)
If the data is already pre-aggregated with center and error values of the error band, you can use ``x/y``, ``x/yError``, and ``x/yError2`` as defined in Error Bar.

Dimension
^^^^^^^^^

Altair supports both 1D and 2D error bands:

A **1D error band** shows the error range of a continuous field; it can be used to show the global error range of the whole plot.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    band = alt.Chart(source).mark_errorband(extent = 'stdev').encode(
        alt.Y('Miles_per_Gallon:Q', title = "Miles per Gallon")
    )

    points = alt.Chart(source).mark_point().encode(
        x = 'Horsepower:Q',
        y = 'Miles_per_Gallon:Q'
    )

    band + points

A **2D error** band shows the error range of a continuous field for each dimension value such as year.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    line = alt.Chart(source).mark_line().encode(
        x='Year',
        y='mean(Miles_per_Gallon)'
    )

    band = alt.Chart(source).mark_errorband(extent='ci').encode(
        x='Year',
        y=alt.Y('Miles_per_Gallon', title='Miles/Gallon'),
    )

    band + line

Color and Opacity Encoding Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can customize the color, size, and opacity of the band in the ``errorband`` by using the ``color`` and ``opacity`` encoding channels, which applied to the whole ``errorband``.

Here is an example of a ``errorband`` with the ``color`` encoding channel set to ``alt.value('black')``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars.url

    alt.Chart(source).mark_errorband(extent = 'ci', borders = True).encode(
        x = 'year(Year)',
        y = alt.Y('Miles_per_Gallon:Q', scale=alt.Scale(zero=False), title = 'Miles per Gallon (95% CIs)'),
        color = alt.value('black')
    )

