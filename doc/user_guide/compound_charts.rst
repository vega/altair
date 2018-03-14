.. currentmodule:: altair

.. _user-guide-compound:

Compound Charts: Layer, HConcat, VConcat, Repeat, Facet
-------------------------------------------------------
Along with the basic :class:`Chart` object, Altair provides a number of
compound plot types that can be used to create stacked, layered, faceted,
and repeated charts. They are summarized in the following table:

======================  ===============================  ===================  ======================
class                   functional form                  operator form        reference
======================  ===============================  ===================  ======================
:class:`LayerChart`     ``alt.layer(chart1, chart2)``    ``chart1 + chart2``  :ref:`layer-chart`
:class:`HConcatChart`   ``alt.hconcat(chart1, chart2)``  ``chart1 | chart2``  :ref:`hconcat-chart`
:class:`VConcatChart`   ``alt.vconcat(chart1, chart2)``  ``chart1 & chart2``  :ref:`vconcat-chart`
:class:`RepeatChart`    N/A                              N/A                  :ref:`repeat-chart`
:class:`FacetChart`     N/A                              N/A                  :ref:`facet-chart`
======================  ===============================  ===================  ======================

.. _layer-chart:

Layered Charts
~~~~~~~~~~~~~~
Layered charts allow you to overlay two different charts on the same set of axes.
They can be useful, for example, when you wish to draw multiple marks for the
same data; for example:

.. altair-plot::

    import altair as alt
    from altair.expr import datum

    from vega_datasets import data
    stocks = data.stocks.url

    base = alt.Chart(stocks).encode(
        x='date:T',
        y='price:Q',
        color='symbol:N'
    ).transform_filter(
        datum.symbol == 'GOOG'
    )

    base.mark_line() + base.mark_point()

Here we have used the ``+`` operator to create a layered chart; alternatively
we could use the ``alt.layer`` function, which accepts as its arguments any
number of charts:

.. altair-plot::

    alt.layer(
      base.mark_line(),
      base.mark_point(),
      base.mark_rule()
    ).interactive()

The output of both of these patterns is a :class:`LayerChart` object, which
can has properties and methods similar to the :class:`Chart` object.


.. _hconcat-chart:

Horizontal Concatenation
~~~~~~~~~~~~~~~~~~~~~~~~
Displaying two plots side-by-side is most generally accomplished with the
:class:`HConcatChart` object, which can be created using the :class:`hconcat`
function or the ``|`` operator.

For example, here is a scatter-plot concatenated with a histogram showing the
distribution of its points:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris.url

    chart1 = alt.Chart(iris).mark_point().encode(
        x='petalLength:Q',
        y='petalWidth:Q',
        color='species:N'
    ).properties(
        height=300,
        width=300
    )

    chart2 = alt.Chart(iris).mark_bar().encode(
        x='count(*):Q',
        y=alt.Y('petalWidth:Q', bin=alt.Bin(maxbins=30)),
        color='species:N'
    ).properties(
        height=300,
        width=100
    )

    chart1 | chart2

This example uses the ``|`` operator, but could similarly have been created
with the :func:`hconcat` function:

.. altair-plot::

   alt.hconcat(chart1, chart2)

The output of both of these is an :class:`HConcatChart` object, which has
many of the same top-level methods and attributes as the :class:`Chart`
object.

Finally, keep in mind that for certain types of horizontally-concatenated
charts, where each panel modifies just one aspect of the visualization,
repeated and faceted charts are more convenient (see :ref:`repeat-chart`
and :ref:`facet-chart` for more explanation).

.. _vconcat-chart:

Vertical Concatenation
~~~~~~~~~~~~~~~~~~~~~~
Similarly to :ref:`hconcat-chart` above, Altair offers vertical concatenation
via the :func:`vconcat` function or the ``&`` operator.

For example, here we vertically-concatenate two views of the same data,
with a ``brush`` selection to add interaction:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    sp500 = data.sp500.url

    brush = alt.selection(type='interval', encodings=['x'])

    upper = alt.Chart(sp500).mark_area().encode(
        x=alt.X('date:T', scale={'domain': brush.ref()}),
        y='price:Q'
    ).properties(
        width=600,
        height=200
    )

    lower = upper.properties(
        selection=brush,
        height=60
    )

    alt.vconcat(upper, lower)

Note that we could just as well have used ``upper & lower`` rather than the
more verbose ``alt.vconcat(upper, lower)``.

As with horizontally-concatenated charts, keep in mind that for concatenations
where only one data grouping or encoding is changing in each panel, using
:ref:`repeat-chart` or :ref:`facet-chart` can be more efficient.

.. _repeat-chart:

Repeated Charts
~~~~~~~~~~~~~~~
The :class:`RepeatChart` object provides a convenient interface for a particular
type of horizontal or vertical concatenation, in which the only difference between
the concatenated panels is modification of *one or more encodings*.

For example, suppose you would like to create a multi-panel scatter-plot to show
different projections of a multi-dimensional dataset.
Let's first create sucha chart manually using ``hconcat`` and ``vconcat``, before
showing how ``repeat`` can be used to build the chart more efficiently:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris.url

    base = alt.Chart().mark_point().encode(
        color='species:N'
    ).properties(
        width=200,
        height=200
    ).interactive()

    chart = alt.vconcat(data=iris)
    for y_encoding in ['petalLength:Q', 'petalWidth:Q']:
        row = alt.hconcat()
        for x_encoding in ['sepalLength:Q', 'sepalWidth:Q']:
            row |= base.encode(x=x_encoding, y=y_encoding)
        chart &= row
    chart

In this example, we explicitly loop over different x and y encodings
to create a 2 x 2 grid of charts showing different views of the data.
The code is straightforward, if a bit verbose.

The :class:`RepeatChart` pattern makes this type of chart a bit easier
to produce:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    iris = data.iris.url

    alt.Chart(iris).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color='species:N'
    ).properties(
        width=200,
        height=200
    ).repeat(
        row=['petalLength', 'petalWidth'],
        column=['sepalLength', 'sepalWidth']
    ).interactive()

The :meth:`Chart.repeat` method is the key here: it lets you specify a set of
encodings for the row and/or column which can be referred to in the chart's
encoding specification using ``alt.repeat('row')`` or ``alt.repeat('column')``.

Currently ``repeat`` can only be specified for rows and column (not, e.g., for
layers) and the target can only be encodings (not, e.g., data transforms)
but there is discussion within the Vega-Lite community about making this pattern
more general in the future.

.. _facet-chart:

Faceted Charts
~~~~~~~~~~~~~~
Like repeated charts, Faceted charts provide a more convenient API for creating
multiple views of a dataset for a specific type of chart: one where each panel
contains a different subset of data.

We could do this manually using a filter transform along with a horizontal
concatenation:

.. altair-plot::

    import altair as alt
    from altair.expr import datum
    from vega_datasets import data
    iris = data.iris.url

    base = alt.Chart(iris).mark_point().encode(
        x='petalLength:Q',
        y='petalWidth:Q',
        color='species:N'
    ).properties(
        width=160,
        height=160
    )

    chart = alt.hconcat()
    for species in ['setosa', 'versicolor', 'virginica']:
        chart |= base.transform_filter(datum.species == species)
    chart

As with the manual approach to :ref:`repeat-chart`, this is straightforward,
if a bit verbose.

Using ``alt.facet`` it becomes a bit cleaner:

.. altair-plot::

    chart = alt.Chart(iris).mark_point().encode(
        x='petalLength:Q',
        y='petalWidth:Q',
        color='species:N'
    ).properties(
        width=180,
        height=180
    ).facet(
        column='species:N'
    )

For simple charts like this, there is also a ``column`` encoding channel that
can give the same results:

.. altair-plot::

    alt.Chart(iris).mark_point().encode(
        x='petalLength:Q',
        y='petalWidth:Q',
        color='species:N',
        column='species:N'
    ).properties(
        width=180,
        height=180
    )

The advantage of using ``alt.facet`` is that it can create faceted views of
more complicated compound charts. For example, here is a faceted view of a
layered chart with a hover selection:

.. altair-plot::

    hover = alt.selection_single(on='mouseover', nearest=True, empty='none')

    base = alt.Chart().encode(
        x='petalLength:Q',
        y='petalWidth:Q',
        color=alt.condition(hover, 'species:N', alt.value('lightgray'))
    ).properties(
        width=180,
        height=180,
    )

    chart = base.mark_point().properties(
        selection=hover
    )

    chart += base.mark_text(dy=-5).encode(
        text = 'species:N',
        opacity = alt.condition(hover, alt.value(1), alt.value(0))
    )

    chart.facet(
        data=iris,
        column='species:N'
    )

Though each of the above examples have faceted the data across columns,
faceting across rows (or across rows *and* columns) is supported as
well.


.. _compound-charts-data:

Advanced: Compound Charts and Data Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When using compound charts, it is possible to specify data in multiple places,
and if you are using large datasets it can be pertinent to think about where
you specify data.

For example, suppose you are creating a layered plot with a dataset marked by
both points and lines:

.. altair-plot::
    :chart-var-name: chart

    import altair as alt
    import pandas as pd

    data = pd.DataFrame({'x': [0, 1, 2], 'y': [0, 1, 0]})

    base = alt.Chart(data).encode(x='x', y='y')

    chart = base.mark_point() + base.mark_line()

The visualization turns out as expected, but if you examine the JSON specification
generated by this chart, you see that the data is specified twice -- one time
for each layer:

.. code-block:: python

    >>> import pprint
    >>> pprint.pprint(chart.to_dict())
    {'$schema': 'https://vega.github.io/schema/vega-lite/v2.json',
     'config': {'view': {'height': 300, 'width': 400}},
     'layer': [{'data': {'values': [{'x': 0, 'y': 0},
                                    {'x': 1, 'y': 1},
                                    {'x': 2, 'y': 0}]},
                'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                             'y': {'field': 'y', 'type': 'quantitative'}},
                'mark': 'point'},
               {'data': {'values': [{'x': 0, 'y': 0},
                                    {'x': 1, 'y': 1},
                                    {'x': 2, 'y': 0}]},
                'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                             'y': {'field': 'y', 'type': 'quantitative'}},
                'mark': 'line'}]}

This happens because our top chart contains two layers, each with its own
data explicitly specified.

In the compound charts created by methods in this section, sub-charts are aware
of the data defined in their parents, and so you can make certain the data is
defined only once by leaving it out of the individual layers, and instead defining
it once the compound chart is created:

.. altair-plot::
    :chart-var-name: chart

    base = alt.Chart().encode(x='x', y='y')

    chart = alt.layer(
        base.mark_point(),
        base.mark_line(),
        data=data
    )

When the cart is created this way, the spec contains only one copy of the data,
at the top level:

.. code-block:: python

    >>> pprint.pprint(chart.to_dict())
    {'$schema': 'https://vega.github.io/schema/vega-lite/v2.json',
     'config': {'view': {'height': 300, 'width': 400}},
     'data': {'values': [{'x': 0, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 0}]},
     'layer': [{'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                             'y': {'field': 'y', 'type': 'quantitative'}},
                'mark': 'point'},
               {'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                             'y': {'field': 'y', 'type': 'quantitative'}},
                'mark': 'line'}]}

For small datasets, this kind of consideration is not particularly important.
But as datasets grow larger, thinking about how your data is defined can lead
to much more efficient plot specifications.
