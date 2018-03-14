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
*TODO*

.. _facet-chart:

Faceted Charts
~~~~~~~~~~~~~~
*TODO*

.. _compound-charts-data

Compound Charts and Data Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Altair's compound charts give you a couple options about where your data should
be specified.

*TODO*
