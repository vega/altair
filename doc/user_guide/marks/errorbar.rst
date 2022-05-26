.. currentmodule:: altair

.. _user-guide-errorbar-marks:

Error Bar
~~~~~~~~~~

An error bar summarizes an error range of quantitative values using a set of summary statistics, representing by rules (and optional end ticks). Error bars in Vega-Lite can either be used to aggregate raw data or directly visualize aggregated data.

To create an error bar, set ``mark`` to ``"errorbar"``.

Using Error Bars to Aggregate Raw Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If the data is not aggregated yet, Altair will aggregate the data based on the ``extent`` properties in the mark definition.

1. **Error bars showing standard error** is the default error bar in Vega-Lite. It can also be explicitly specified by setting ``extent`` to ``"stderr"``. The length of lower and upper rules represent standard error. By default, the rule marks expand from the mean.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    error_bars = alt.Chart(source).mark_errorbar().encode(
    x=alt.X('yield:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('variety:N')
    )

    points = alt.Chart(source).mark_point(filled=True, color='black').encode(
    x=alt.X('yield:Q', aggregate='mean'),
    y=alt.Y('variety:N'),
    )

    error_bars + points 

2. **Error bar showing standard deviation** can be specified by setting ``extent`` to ``"stdev"``. For this type of error bar, the length of lower and upper rules represent standard deviation. Like an error bar that shows Standard Error, the rule marks expand from the mean by default.

.. altair-plot::
   import altair as alt
    from vega_datasets import data

    source = data.barley()

    error_bars = alt.Chart(source).mark_errorbar(extent = 'stdev').encode(
    x=alt.X('yield:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('variety:N')
    )

    points = alt.Chart(source).mark_point(filled=True, color='black').encode(
    x=alt.X('yield:Q', aggregate='mean'),
    y=alt.Y('variety:N'),
    )

    error_bars + points 

3. **Error bars showing interquartile range** can be specified by setting ``extent`` to ``"iqr"``. For this type of error bar, the rule marks expand from the first quartile to the third quartile.

.. altair-plot::
   import altair as alt
    from vega_datasets import data

    source = data.barley()

    error_bars = alt.Chart(source).mark_errorbar(extent = 'iqr').encode(
    x=alt.X('yield:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('variety:N')
    )

    points = alt.Chart(source).mark_point(filled=True, color='black').encode(
    x=alt.X('yield:Q', aggregate='mean'),
    y=alt.Y('variety:N'),
    )

    error_bars + points 

Using Error Bars to Visualize Aggregated Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Data is aggregated with low and high values of the error bars
If the data is already pre-aggregated with low and high values of the error bars, you can directly specify ``x`` and ``x2`` (or ``y`` and ``y2``) to use error bar as a ranged mark.

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({
        'lower_yield': [23.1311, 23.9503, 24.7778, 21.7823],
        'upper_yield': [43.5522, 38.9775, 46.9167, 48.9732],
        'center': [32.4, 30.96667, 33.966665, 30.45],
        'variety': ["Glabron", "Manchuria", "No. 457", "No. 462"]
    })

    bar = alt.Chart(source).mark_errorbar().encode(
        alt.X('upper_yield:Q', scale=alt.Scale(zero=False), title = 'yield'),
        alt.X2('lower_yield:Q'),
        alt.Y('variety:N')
    )

    point = alt.Chart(source).mark_point(filled = True, color = 'black').encode(
        alt.X('center:Q'),
        alt.Y('variety:N')
    )

    point + bar

2. Data is aggregated with center and error value(s)
If the data is already pre-aggregated with center and error values of the error bars, you can directly specify ``x`` as center, ``xError`` and ``xError2`` as error values extended from center (or ``y``, ``yError``, and ``yError2``). If ``x/yError2`` is omitted, error bars have symmetric error values.

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame({
        'yield_error': [7.5522, 6.9775, 3.9167, 11.9732],
        'yield_center': [32.4, 30.96667, 33.966665, 30.45],
        'variety': ["Glabron", "Manchuria", "No. 457", "No. 462"]
    })

    bar = alt.Chart(source).mark_errorbar().encode(
        x = alt.X('yield_center:Q', scale=alt.Scale(zero=False), title = 'yield'),
        xError = ('yield_error:Q'),
        y = alt.Y('variety:N')
    )

    point = alt.Chart(source).mark_point(filled = True, color = 'black').encode(
        alt.X('yield_center:Q'),
        alt.Y('variety:N')
    )

    point + bar

**Note** if error is pre-aggregated with asymmetric error values one of ``x/yError`` and ``x/yError2`` has to be positive value and other has to be negative value.

Dimension & Orientation
^^^^^^^^^^^^^^^^^^^^^^^
Altair supports both 1D and 2D error bands:

A **1D error band** shows the error range of a continuous field.

The orientation of an error bar is automatically determined by the continuous field axis. For example, you can create a vertical 1D error bar by encoding a continuous field on the y axis.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    error_bars = alt.Chart(source).mark_errorbar().encode(
    alt.Y('yield:Q', scale=alt.Scale(zero=False))
    )

    points = alt.Chart(source).mark_point(filled=True, color='black').encode(
    alt.Y('yield:Q', aggregate='mean')
    )

    error_bars + points

A **2D error bar** shows the error range of a continuous field, broken down by categories.

For 2D error bars with one continuous field and one discrete field, the error bars will be horizontal if the continuous field is on the x axis. Alternatively, if the continuous field is on the y axis, the error bar will be vertical.
 
.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    error_bars = alt.Chart(source).mark_errorbar(extent = 'stdev').encode(
    alt.Y('yield:Q', scale=alt.Scale(zero=False)),
    alt.X('variety:N')
    )

    points = alt.Chart(source).mark_point(filled=True, color='black').encode(
    alt.Y('yield:Q', aggregate='mean'),
    alt.X('variety:N'),
    )

    error_bars + points

Color, and Opacity Encoding Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can customize the color, size, and opacity of the bar in the ``errorbar`` by using the ``color`` and ``opacity`` encoding channels, which are applied to the whole errorbar.

Here is an example of a ``errorbar`` with the ``color`` encoding channel set to ``alt.value("#4682b4")``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    error_bars = alt.Chart(source).mark_errorbar(ticks = True).encode(
        alt.X('yield:Q', scale=alt.Scale(zero=False)),
        alt.Y('variety:N'),
        color = alt.value("#4682b4")
    )

    points = alt.Chart(source).mark_point(filled=True, color='black').encode(
    alt.X('yield:Q', aggregate='mean'),
    alt.Y('variety:N'),
    )

    error_bars + points

Tooltip Encoding Channels
^^^^^^^^^^^^^^^^^^^^^^^^^
You can add custom tooltips to error bars. The custom tooltip will override the default error bar’s tooltips.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).mark_errorbar().encode(
        alt.X('yield:Q', scale=alt.Scale(zero=False)),
        alt.Y('variety:N'),
        tooltip = 'variety:N'
    )

Mark Config
^^^^^^^^^^^
The ``errorbar`` config object sets the default properties for ``errorbar`` marks.

