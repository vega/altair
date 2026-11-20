.. currentmodule:: altair

.. _user-guide-compound:

Layered & Multi-View Charts
---------------------------
Along with the basic :class:`Chart` object, Altair provides a number of
compound plot types that can be used to create stacked, layered, faceted,
and repeated charts. They are summarized in the following tables:

======================  ===============================  ===================  ======================
class                   functional form                  operator form        reference
======================  ===============================  ===================  ======================
:class:`LayerChart`     ``alt.layer(chart1, chart2)``    ``chart1 + chart2``  :ref:`layer-chart`
:class:`HConcatChart`   ``alt.hconcat(chart1, chart2)``  ``chart1 | chart2``  :ref:`hconcat-chart`
:class:`VConcatChart`   ``alt.vconcat(chart1, chart2)``  ``chart1 & chart2``  :ref:`vconcat-chart`
======================  ===============================  ===================  ======================

======================  ====================================  ======================
class                   method form                           reference
======================  ====================================  ======================
:class:`RepeatChart`    ``chart.repeat(row, column)``         :ref:`repeat-chart`
:class:`FacetChart`     ``chart.facet(facet, row, column)``   :ref:`facet-chart`
======================  ====================================  ======================

.. _layer-chart:

Layered Charts
~~~~~~~~~~~~~~
Layered charts allow you to overlay two different charts on the same set of axes.
They can be useful, for example, when you wish to draw multiple marks for the
same data; for example:

.. altair-plot::

    import altair as alt
    from altair.datasets import data

    stocks = data.stocks.url

    base = alt.Chart(stocks).encode(
        x='date:T',
        y='price:Q',
        color='symbol:N'
    ).transform_filter(
        alt.datum.symbol == 'GOOG'
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

Normally, the output of both of these patterns is a :class:`LayerChart` object,
which has properties and methods similar to the :class:`Chart` object. If all
charts share identical ``row``, ``column``, or ``facet`` encoding channels, those
encodings are hoisted automatically and a :class:`FacetChart` is returned instead
(see :ref:`layer-shared-facet`).

Order of Layers
^^^^^^^^^^^^^^^
In a layered chart, the order of layers is determined from the order in which
they are specified. For example, when creating a chart using ``layer1 + layer2``
or ``alt.layer(layer1, layer2)``, ``layer1`` will appear below ``layer2``,
and ``layer2`` may obscure the marks of ``layer1``.

For example, consider the following chart where we plot points on top of a
heat-map:

.. altair-plot::

    import altair as alt
    from altair.datasets import data

    source = data.movies.url

    heatmap = alt.Chart(source).mark_rect().encode(
        alt.X('IMDB Rating:Q').bin(),
        alt.Y('Rotten Tomatoes Rating:Q').bin(),
        alt.Color('count()').scale(scheme='greenblue')
    )

    points = alt.Chart(source).mark_circle(
        color='black',
        size=5,
    ).encode(
        x='IMDB Rating:Q',
        y='Rotten Tomatoes Rating:Q',
    )

    heatmap + points

If we put the two layers in the opposite order, the points will be drawn first
and will be obscured by the heatmap marks:

.. altair-plot::

    points + heatmap

If you do not see the expected output when creating a layered chart, make certain
that you are ordering the layers appropriately.

Opacity and Blending
^^^^^^^^^^^^^^^^^^^^
Layer order determines which marks are drawn first. Opacity and blending
determine how their colors combine where they overlap.

Circle marks have a default opacity of 0.7 in non-aggregate plots, so a line
drawn underneath can show through them. Set ``opacity=1`` to make the circles
opaque. The following panels compare the default with an opaque fill and a
translucent fill.

.. altair-plot::

    import altair as alt

    source = alt.Data(values=[{"x": 1, "y": 1}, {"x": 2, "y": 1}, {"x": 3, "y": 1}])
    base = alt.Chart(source).encode(
        x=alt.X("x:Q").scale(domain=[0, 4]).axis(None),
        y=alt.Y("y:Q").scale(domain=[0, 2]).axis(None),
    ).properties(width=180, height=100)
    line = base.mark_line(color="black", strokeWidth=3)

    alt.hconcat(
        (line + base.mark_circle(color="red", size=900)).properties(title="Default opacity"),
        (line + base.mark_circle(color="red", size=900, opacity=1)).properties(title="Opaque"),
        (line + base.mark_circle(
            color="red", size=900, opacity=1, fillOpacity=0.4
        )).properties(title="Translucent fill"),
    )

``opacity`` affects the whole mark, while ``fillOpacity`` and ``strokeOpacity``
affect its fill and outline separately. When both overall opacity and fill
opacity are set, their values multiply. For example, ``opacity=0.5`` and
``fillOpacity=0.4`` give the fill an effective opacity of 0.2.
To control transparency explicitly, set ``opacity`` along with the fill or
stroke opacity.

The ``blend`` mark property selects how a mark's color combines with the
content already drawn underneath it. With the default compositing behavior,
an opaque mark covers earlier marks. Two other useful modes are
``"multiply"``, which darkens overlapping colors, and ``"screen"``, which
lightens them. These modes can reveal overlaps even when ``opacity=1``.

.. altair-plot::

    import altair as alt

    source = alt.Data(values=[{"x": 1.5}, {"x": 2.5}])
    base = alt.Chart(source).encode(
        x=alt.X("x:Q").scale(domain=[0, 4]).axis(None),
        y=alt.value(60),
    ).properties(width=180, height=120)
    left = base.transform_filter(alt.datum.x == 1.5)
    right = base.transform_filter(alt.datum.x == 2.5)

    panels = []
    for mode in [None, "multiply", "screen"]:
        first = left.mark_circle(color="#e76f51", size=6000, opacity=1)
        second = right.mark_circle(
            color="#457b9d", size=6000, opacity=1, blend=mode
        )
        panels.append(
            (first + second).properties(title=mode or "Default")
        )

    alt.hconcat(*panels).configure_view(fill="#eeeeee", stroke=None)

In the default panel, the blue circle covers the orange circle at the
intersection. In the other panels, the blue circle blends with both the orange
circle and the light gray view background. The background participates in the
calculation even outside the intersection. Multiplying a color by white leaves
it unchanged, while screening a color against black leaves it unchanged.
Choose the background deliberately when comparing blend modes.

Blending uses the content present when each mark is drawn, so layer order also
matters. In this example, only the second circle has a blend mode. Moving it to
the first layer makes it blend with the background before the opaque orange
circle is drawn over it.

Use ``alt.layer(line, points)`` or ``line + points`` to put points above a
line. Vega's mark-level ``zindex`` property is not exposed by Altair's
:class:`MarkDef`. Axis and legend ``zindex`` settings control those guides;
the order of the charts passed to ``alt.layer`` controls the layers.


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
    from altair.datasets import data

    penguins = data.penguins.url

    chart1 = alt.Chart(penguins).mark_point().encode(
        x=alt.X('Flipper Length (mm):Q', scale=alt.Scale(zero=False)),
        y=alt.Y('Body Mass (g):Q', scale=alt.Scale(zero=False)),
        color='Species:N'
    ).properties(
        height=300,
        width=300
    )

    chart2 = alt.Chart(penguins).mark_bar().encode(
        x='count()',
        y=alt.Y('Body Mass (g):Q', bin=alt.Bin(maxbins=30)),
        color='Species:N'
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
    from altair.datasets import data

    source = data.sp500.url

    brush = alt.selection_interval(encodings=['x'])

    base = alt.Chart(source).mark_area().encode(
        x = 'date:T',
        y = 'price:Q'
    ).properties(
        width=600,
        height=200
    )

    upper = base.encode(alt.X('date:T').scale(domain=brush))

    lower = base.properties(
        height=60
    ).add_params(brush)

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
Let's first create such a chart manually using ``hconcat`` and ``vconcat``, before
showing how ``repeat`` can be used to build the chart more efficiently:

.. altair-plot::

    import altair as alt
    from altair.datasets import data

    penguins = data.penguins.url

    base = alt.Chart().mark_point().encode(
        color='Species:N'
    ).properties(
        width=200,
        height=200
    ).interactive()

    chart = alt.vconcat(data=penguins)
    for y_encoding in ['Flipper Length (mm):Q', 'Body Mass (g):Q']:
        row = alt.hconcat()
        for x_encoding in ['Beak Length (mm):Q', 'Beak Depth (mm):Q']:
            row |= base.encode(
                       x=alt.X(x_encoding, scale=alt.Scale(zero=False)),
                       y=alt.Y(y_encoding, scale=alt.Scale(zero=False)),
                   )
        chart &= row
    chart

In this example, we explicitly loop over different x and y encodings
to create a 2 x 2 grid of charts showing different views of the data.
The code is straightforward, if a bit verbose.

The :class:`RepeatChart` pattern, accessible via the :meth:`Chart.repeat`
method, makes this type of chart a bit easier to produce:

.. altair-plot::

    import altair as alt
    from altair.datasets import data
    penguins = data.penguins.url

    alt.Chart(penguins).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative', scale=alt.Scale(zero=False)),
        alt.Y(alt.repeat("row"), type='quantitative', scale=alt.Scale(zero=False)),
        color='Species:N'
    ).properties(
        width=200,
        height=200
    ).repeat(
        row=['Flipper Length (mm)', 'Body Mass (g)'],
        column=['Beak Length (mm)', 'Beak Depth (mm)']
    ).interactive()

The :meth:`Chart.repeat` method is the key here: it lets you specify a set of
encodings for the row and/or column which can be referred to in the chart's
encoding specification using ``alt.repeat('row')`` or ``alt.repeat('column')``.

Another option to use the ``repeat`` method is for layering. Here below the
columns ``US Gross`` and ``Worldwide Gross`` are layered on the ``y``-axis
using ``alt.repeat('layer')``:

.. altair-plot::

    import altair as alt
    from altair.datasets import data

    source = data.movies()

    alt.Chart(source).mark_line().encode(
        x=alt.X("IMDB Rating").bin(),
        y=alt.Y(alt.repeat('layer')).aggregate('mean').title("Mean of US and Worldwide Gross"),
        color=alt.ColorDatum(alt.repeat('layer'))
    ).repeat(layer=["US Gross", "Worldwide Gross"])

Currently ``repeat`` can only be encodings (not, e.g., data transforms)
but there is discussion within the Vega-Lite community about making this pattern
more general in the future.

.. _facet-chart:

Faceted Charts
~~~~~~~~~~~~~~
Like repeated charts, Faceted charts provide multiple views of a dataset.
But instead of having different panels for different encodings,
we have different panels for different subsets of data. For example,
one panel for each of the three species of penguin in the penguins dataset.

This is also called a `small multiple <https://en.wikipedia.org/wiki/Small_multiple>`_
chart, trellis chart, lattice chart, grid chart, or panel chart.

We could do this manually using a filter transform along with a horizontal
concatenation:

.. altair-plot::

    import altair as alt
    from altair.datasets import data
    penguins = data.penguins.url

    base = alt.Chart(penguins).mark_point().encode(
        x=alt.X('Flipper Length (mm):Q').scale(zero=False),
        y=alt.Y('Body Mass (g):Q').scale(zero=False),
        color='Species:N'
    ).properties(
        width=160,
        height=160
    )

    chart = alt.hconcat()
    for species in ['Adelie', 'Chinstrap', 'Gentoo']:
        chart |= base.transform_filter(alt.datum.Species == species)
    chart

As with the manual approach to :ref:`repeat-chart`, this is straightforward,
if a bit verbose.

Using ``.facet`` it becomes a bit cleaner:

.. altair-plot::

    alt.Chart(penguins).mark_point().encode(
        x=alt.X('Flipper Length (mm):Q').scale(zero=False),
        y=alt.Y('Body Mass (g):Q').scale(zero=False),
        color='Species:N'
    ).properties(
        width=180,
        height=180
    ).facet(
        column='Species:N'
    )

For simple charts like this, there is also a ``column`` encoding channel that
can give the same results:

.. altair-plot::

    alt.Chart(penguins).mark_point().encode(
        x=alt.X('Flipper Length (mm):Q').scale(zero=False),
        y=alt.Y('Body Mass (g):Q').scale(zero=False),
        color='Species:N',
        column='Species:N'
    ).properties(
        width=180,
        height=180
    )

The advantage of using ``.facet`` is that it can create faceted views of
more complicated compound charts. For example, here is a faceted view of a
layered chart with a hover selection:

.. altair-plot::

    hover = alt.selection_point(on='pointerover', nearest=True, empty=False)
    when_hover = alt.when(hover)

    base = alt.Chart(penguins).encode(
        x=alt.X('Flipper Length (mm):Q').scale(zero=False),
        y=alt.Y('Body Mass (g):Q').scale(zero=False),
        color=alt.condition(hover, 'Species:N', alt.value('lightgray'))
    ).properties(
        width=180,
        height=180,
    )

    points = base.mark_point().add_params(hover)

    text = base.mark_text(dy=-5).encode(
        text = 'Species:N',
        opacity = alt.condition(hover, alt.value(1), alt.value(0))
    )

    alt.layer(points, text).facet(
        'Species:N',
    )

Though each of the above examples have faceted the data across columns,
faceting across rows (or across rows *and* columns) is supported as
well.

.. _layer-shared-facet:

Layering charts that share a facet encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When every chart passed to :func:`layer` (or combined with ``+``) carries
identical ``row``, ``column``, or ``facet`` encoding channels, those encodings
are hoisted automatically and a :class:`FacetChart` is returned. The two forms
below produce the same Vega-Lite specification:

.. altair-plot::

    import altair as alt
    from altair.datasets import data
    penguins = data.penguins.url

    base = alt.Chart(penguins).encode(
        x=alt.X('Flipper Length (mm):Q').scale(zero=False),
        y=alt.Y('Body Mass (g):Q').scale(zero=False),
        row='Species:N',
    )

    # facet encoding shared on each layer — hoisted automatically
    alt.layer(
        base.mark_point(),
        base.mark_line(),
    )

The equivalent explicit form is:

.. code-block:: python

    base = alt.Chart(penguins).encode(
        x=alt.X('Flipper Length (mm):Q').scale(zero=False),
        y=alt.Y('Body Mass (g):Q').scale(zero=False),
    )

    alt.layer(
        base.mark_point(),
        base.mark_line(),
    ).facet(row='Species:N')

If the facet encodings differ across layers, or only some layers carry them,
a ``TypeError`` is raised as before.
