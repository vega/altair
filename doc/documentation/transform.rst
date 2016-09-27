.. _data-transformations:

Data Transformations
--------------------

Altair provides a data transformation API that allows both *filtering* and
*transformation* of values within the plot renderer. In both cases, the
expressions are given in terms of *javascript strings* passed to the
``transform_data`` method.

For example, consider this visualization of the historical US population,
split by age and gender:

.. altair-plot::

    from altair import Chart, Color, Scale

    data = 'https://vega.github.io/vega-datasets/data/population.json'
    pink_blue = Scale(range=["lightblue", "pink"])

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('sex:N', scale=pink_blue)
    )

This visualization shows that on average over the course of history, the
younger population has far outnumbered the older population.

1. We might wish to zero-in on a particular year, rather than taking a
   mean over all years.
2. The "1" and "2" labels for gender are not all that informative; we should
   probably be change them to "Male" and "Female" for clarity.

We could certainly accomplish this by downloading the dataset, manipulating it
in, say, pandas, and building a chart using the result, but it would be nice to
do this within the Altair spec itself so that we can use the original data
source.

What we're looking for is a ``filter`` operation in the first case, and a
``calculate`` operation in the second. Altair exposes these via the
:meth:`Chart.transform_data` method, which passes its arguments to the
:class:`Transform` class:

.. altair-trait-table:: Transform

Let's remake the plot, using these transformation operations: we'll use
``filter`` to limit the year to 2000, and ``calculate`` to convert the
*1/2* labels to *Male/Female*:

.. altair-plot::

    from altair import Chart, Color, Scale, Formula

    data = 'https://vega.github.io/vega-datasets/data/population.json'
    pink_blue = Scale(range=["pink", "lightblue"])

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('gender:N', scale=pink_blue)
    ).transform_data(
        filter='datum.year == 2000',
        calculate=[Formula(field='gender',
                           expr='datum.sex == 1 ? "Male" : "Female"')],
    )

The ``filter`` attribute of :meth:`~Chart.transform_data` accepts a string of
javascript code, referring to the data column name as an attribute of
``datum``, which you can think of as the row within the dataset.
The `calculate`` attribute accepts a list of :class:`Formula` objects, which
each define a new column using an valid javascript expression over existing
columns. For details on how this expression can be formed, see Vega's
`Expression Documentation <https://github.com/vega/vega/wiki/Expressions>`_.

The :ref:`gallery_bar_grouped` example shows a more refined view of this dataset
using some of these techniques.
