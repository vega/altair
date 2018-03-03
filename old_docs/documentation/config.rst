.. currentmodule:: altair

.. _configuring-altair:

Configuring Visualizations
==========================

Altair's goal is to automatically choose useful plot settings and configurations
so that the user is free to think about the data rather than the plotting
machinery. That said, once you have a useful visualization, you will often want
to adjust certain aspects of it. This section of the documentation outlines
some of these adjustments.

.. note::

   This section is currently not complete; for more information on the adjustments
   available, see Vega-Lite's `Configuration Documentation <https://vega.github.io/vega-lite/docs/config.html>`_


Adjusting Axis Limits
---------------------
Axis limits can be adjusted using the :class:`Scale` property of the axis
encodings. For example, consider the following plot:

.. altair-setup::
    :show:

    import altair as alt
    data = alt.load_dataset('cars', url_only=True)

.. altair-plot::

    import altair as alt

    alt.Chart(data).mark_point().encode(
        x='Acceleration:Q',
        y='Horsepower:Q'
    )


Suppose you would like to adjust the limits of the x-axis. You can do this by
adding a :class:`Scale` property to the :class:`X` encoding that specifies
these limits:

.. altair-plot::

    alt.Chart(data).mark_point().encode(
        alt.X('Acceleration:Q', scale=alt.Scale(domain=(5, 15))),
        y='Horsepower:Q'
    )

The problem is that the data still exists beyond the scale, and we need to tell
Altair what to do with this data. One option is to "clamp" the data; that is,
to adjust it so that data beyond the limits are moved to the limit:

.. altair-plot::

    alt.Chart(data).mark_point().encode(
        alt.X('Acceleration:Q', scale=alt.Scale(domain=(5, 15), clamp=True)),
        y='Horsepower:Q'
    )

Another option is to *filter* the data, using the :meth:`Chart.transform_data`
method, to remove these values from the dataset:

.. altair-plot::

    alt.Chart(data).mark_point().encode(
        alt.X('Acceleration:Q', scale=alt.Scale(domain=(5, 15))),
        y='Horsepower:Q'
    ).transform_data(filter='datum.Acceleration < 15')

Some combination of filtering and clamping is usually suitable for adjusting
of axis limits.


Adjusting Axis Labels
---------------------
Altair also gives you tool to easily configure the appearance of axis labels.
For example consider this plot:

.. altair-plot::

   import pandas as pd
   df = pd.DataFrame({'x': [0.03, 0.04, 0.05, 0.12, 0.07, 0.15],
                      'y': [10, 35, 39, 50, 24, 35]})

   alt.Chart(df).mark_circle().encode(
       x='x',
       y='y'
   )

The x labels are automatically rendered in SI prefix notation (i.e. 3m = 0.03)
which may not be desirable.

To fine-tune the formatting of the tick labels and to add a custom title to
each axis, we can pass to the :class:`X` and :class:`Y` encoding a custom
:class:`Axis` definition.
Here is an example of formatting the x labels as a percentage, and
the y labels as a dollar value:

.. altair-setup::

   import pandas as pd
   df = pd.DataFrame({'x': [0.03, 0.04, 0.05, 0.12, 0.07, 0.15],
                      'y': [10, 35, 39, 50, 24, 35]})


.. altair-plot::

   alt.Chart(df).mark_circle().encode(
       x=alt.X('x', axis=alt.Axis(format='%', title='percentage')),
       y=alt.Y('y', axis=alt.Axis(format='$', title='dollar amount'))
   )


Additional formatting codes are available; for a listing of these see the
`d3 Format Code Documentation <https://github.com/d3/d3-format/blob/master/README.md#format>`_.
