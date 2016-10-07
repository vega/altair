.. currentmodule:: altair

.. _configuring-altair:

Configuring Altair Visualizations
=================================

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

    from altair import Chart, load_dataset, X, Y, Scale
    data = load_dataset('cars', url_only=True)

.. altair-plot::

    Chart(data).mark_point().encode(
        x='Acceleration:Q',
        y='Horsepower:Q'
    )


Suppose you would like to adjust the limits of the x-axis. You can do this by
adding a :class:`Scale` property to the :class:`X` encoding that specifies
these limits:

.. altair-plot::

    Chart(data).mark_point().encode(
        X('Acceleration:Q', scale=Scale(domain=(5, 15))),
        y='Horsepower:Q'
    )

The problem is that the data still exists beyond the scale, and we need to tell
Altair what to do with this data. One option is to "clamp" the data; that is,
to adjust it so that data beyond the limits are moved to the limit:

.. altair-plot::

    Chart(data).mark_point().encode(
        X('Acceleration:Q', scale=Scale(domain=(5, 15), clamp=True)),
        y='Horsepower:Q'
    )

Another option is to *filter* the data, using the :meth:`Chart.transform_data`
method, to remove these values from the dataset:

.. altair-plot::

    Chart(data).mark_point().encode(
        X('Acceleration:Q', scale=Scale(domain=(5, 15))),
        y='Horsepower:Q'
    ).transform_data(filter='datum.Acceleration < 15')

Some combination of filtering and clamping is usually suitable for adjusting
of axis limits.
