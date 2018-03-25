.. currentmodule:: altair

.. _user-guide-selections:

Selections: Building Blocks of Interactions
-------------------------------------------
One of the unique features of Altair, inherited from Vega-Lite, is a
declarative grammar of not just visualization, but *interaction*. The
core concept of this grammar is the *selection* object.

Selections in Altair come in a few flavors, and they can be *bound* to
particular charts or sub-charts in your visualization, then referenced
in other parts of the visualization.

Example: Linked-Brush Scatter-Plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a motivation, let's create a simple chart and then add some selections
to it. Here is a simple scatter-plot created from the ``cars`` dataset:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    )

First we'll create an interval selection using the :func:`selection_interval`
function:

.. altair-plot::
    :output: none

    brush = alt.selection_interval()  # selection of type "interval"

We can now bind this brush to our chart by setting the ``selection``
property:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).properties(
        selection=brush
    )

The result above is a chart that allows you to click and drag to create
a selection region, and to move this region once the region is created.

This is neat, but the selection doesn't actually *do* anything yet.
To use this selection, we need to reference it in some way within
the chart. Here, we will use the :func:`condition` function to create
a conditional color encoding: we'll tie the color to the ``"Origin"``
column for points in the selection, and set the color to ``"lightgray"``
for points outside the selection:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).properties(
        selection=brush
    )

As you can see, with this simple change, the color of the points responds
to the selection.

This approach becomes even more powerful when the selection behavior is
tied across multiple views of the data within a compound chart.
For example, here we create a ``chart`` object using the same code as
above, and horizontally concatenate two versions of this chart: one
with the x-encoding tied to ``"Acceleration"``, and one with the x-encoding
tied to ``"Miles_per_Gallon"``

.. altair-plot::

    chart = alt.Chart(cars).mark_point().encode(
        y='Horsepower:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).properties(
        width=250,
        height=250,
        selection=brush
    )

    chart.encode(x='Acceleration:Q') | chart.encode(x='Miles_per_Gallon:Q')

Because both copies of the chart reference the same selection object, the
renderer ties the selections together across panels, leading to a dynamic
display that helps you gain insight into the relationships within the
dataset.

Each selection type has attributes through which its behavior can be
customized; for example we might wish for our brush to be tied only
to the ``"x"`` encoding to emphasize that feature in the data.
We can modify the brush definition, and leave the rest of the code unchanged:

.. altair-plot::

    brush = alt.selection_interval(encodings=['x'])

    chart = alt.Chart(cars).mark_point().encode(
        y='Horsepower:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).properties(
        width=250,
        height=250,
        selection=brush
    )

    chart.encode(x='Acceleration:Q') | chart.encode(x='Miles_per_Gallon:Q')

Selection Types: Interval, Single, Multi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this interesting example under our belt, let's take a more systematic
look at some of the types of selections available in Altair.
For simplicity, we'll use a common chart in all the following examples; a
simple heat-map based on the ``cars`` dataset.
For convenience, let's write a quick Python function that will take a selection
object and create a chart with the color of the chart elements linked to this
selection:

.. altair-plot::
    :output: none

    def make_example(selector):
        cars = data.cars.url

        return alt.Chart(cars).mark_rect().encode(
            x="Cylinders:O",
            y="Origin:N",
            color=alt.condition(selector, 'count()', alt.value('lightgray'))
        ).properties(
            width=300,
            height=180,
            selection=selector
        )

Next we'll use this function to demonstrate the properties of various selections.

Interval Selections
^^^^^^^^^^^^^^^^^^^
An *interval* selection allows you to select chart elements by clicking and dragging.
You can create such a selection using the :func:`selection_interval` function:

.. altair-plot::

   interval = alt.selection_interval()
   make_example(interval)

As you click and drag on the plot, you'll find that your mouse creates a box
that can be subsequently moved to change the selection.

The :func:`selection_interval` function takes a few additional arguments; for
example we can bind the interval to only the x-axis, and set it such that the
empty selection contains none of the points:

.. altair-plot::

   interval_x = alt.selection_interval(encodings=['x'], empty='none')
   make_example(interval_x)

A special case of an interval selection is when the interval is bound to the
chart scales; this is how Altair plots can be made interactive:

.. altair-plot::

    scales = alt.selection_interval(bind='scales')

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).properties(
        selection=scales
    )

Because this is such a common pattern, Altair provides the :meth:`Chart.interactive`
method which creates such a selection more concisely.


Single Selections
^^^^^^^^^^^^^^^^^
A *single* selection allows you to select a single chart element at a time using
mouse actions. By default, points are selected on click:

.. altair-plot::

    single = alt.selection_single()
    make_example(single)

By changing some arguments, we can select points on mouseover rather than on
click. We can also set the ``nearest`` flag to ``True`` so that the nearest
point is highlighted:

.. altair-plot::

    single_nearest = alt.selection_single(on='mouseover', nearest=True)
    make_example(single_nearest)

Multiple Selections
^^^^^^^^^^^^^^^^^^^
A *multi* selection is similar to a *single* selection, but it allows for
multiple chart objects to be selected at once.
By default, chart elements can be added to and removed from the selection
by clicking on them while holding the *shift* key:

.. altair-plot::

    multi = alt.selection_multi()
    make_example(multi)

In addition to the options seen in :func:`selection_single`, the multi selection
accepts the ``toggle`` parameter, which controls whether points can be removed
from the selection once they are added.

For example, here is a plot where you can "paint" the chart objects by hovering
over them with your mouse:

.. altair-plot::

    multi_mouseover = alt.selection_multi(on='mouseover', toggle=False, empty='none')
    make_example(multi_mouseover)

Further Examples
~~~~~~~~~~~~~~~~
Now that you understand the basics of Altair selections, you might wish to look
through the :ref:`gallery-category-interactive` section of the example gallery
for ideas about how they can be applied to more interesting charts.

For more information on how to fine-tune selections, including specifying other
mouse and keystroke options, see the `Vega-Lite Selection documentation
<https://vega.github.io/vega-lite/docs/selection.html>`_.
