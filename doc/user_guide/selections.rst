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


Interval Selections
~~~~~~~~~~~~~~~~~~~
*TODO*

Single Selections
~~~~~~~~~~~~~~~~~
*TODO*

Multiple Selections
~~~~~~~~~~~~~~~~~~~
*TODO*
