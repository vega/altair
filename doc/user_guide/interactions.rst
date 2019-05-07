.. currentmodule:: altair

.. _user-guide-interactions:

Bindings, Selections, Conditions: Making Charts Interactive
===========================================================

One of the unique features of Altair, inherited from Vega-Lite, is a
declarative grammar of not just visualization, but *interaction*. There are three
core concepts of this grammar:

- the :func:`selection` object which captures interactions from the mouse or through other inputs to effect the chart. Inputs can either be events like mouse clicks or drags. Inputs can also be elements like a drop-down, radio button or slider. Selections can be used alone but if you want to change any element of your chart you will need to connect them to a *condition*. 
- the :func:`condition` function takes the selection input and changes an element of the chart based on that input. 
- the ``bind`` property of a selection which establishes a two-way binding between the selection and an input element of your chart. 

Interactive charts can use one or more of these elements to create rich interactivity between the viewer and the data. 


Selections: Building Blocks of Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Selections in Altair come in a few flavors, and they can be *bound* to
particular charts or sub-charts in your visualization, then referenced
in other parts of the visualization.

Example: Linked-Brush Scatter-Plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    ).add_selection(
        brush
    )

The result above is a chart that allows you to click and drag to create
a selection region, and to move this region once the region is created.

Conditions: Making the chart respond
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    ).add_selection(
        brush
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
        height=250
    ).add_selection(
        brush
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
        height=250
    ).add_selection(
        brush
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
            height=180
        ).add_selection(
            selector
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
    ).add_selection(
        scales
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

Selection Targets: Fields and Encodings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For any but the simplest selections, the user needs to think about exactly
what is targeted by the selection, and this can be controlled with either the
``fields`` or ``encodings`` arguments. These control what data properties are
used to determine which points are part of the selection.

For example, here we create a small chart that acts as an interactive legend,
by targeting the Origin field using ``fields=['Origin']``. Clicking on points
in the upper-left plot (the legend) will propagate a selection for all points
with a matching ``Origin``.

.. altair-plot::

    selection = alt.selection_multi(fields=['Origin'])
    color = alt.condition(selection,
                          alt.Color('Origin:N', legend=None),
                          alt.value('lightgray'))

    scatter = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
        tooltip='Name:N'
    )

    legend = alt.Chart(cars).mark_point().encode(
        y=alt.Y('Origin:N', axis=alt.Axis(orient='right')),
        color=color
    ).add_selection(
        selection
    )

    scatter | legend

The above could be equivalently replace ``fields=['Origin']`` with
``encodings=['color']``, because in this case the chart maps ``color`` to
``'Origin'``.

Similarly, we can specify multiple fields and/or encodings that must be
matched in order for a datum to be included in a selection.
For example, we could modify the above chart to create a two-dimensional
clickable legend that will select points by both Origin and number of
cylinders:

.. altair-plot::
   
    selection = alt.selection_multi(fields=['Origin', 'Cylinders'])
    color = alt.condition(selection,
                          alt.Color('Origin:N', legend=None),
                          alt.value('lightgray'))

    scatter = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
        tooltip='Name:N'
    )

    legend = alt.Chart(cars).mark_rect().encode(
        y=alt.Y('Origin:N', axis=alt.Axis(orient='right')),
        x='Cylinders:O',
        color=color
    ).add_selection(
        selection
    )

    scatter | legend

By fine-tuning the behavior of selections in this way, they can be used to
create a wide variety of linked interactive chart types.

Binding: Adding Data Driven Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
With an understanding of the selection types and conditions, you can now add data-driven input elements to the charts using the ``bind`` option. As specified by `Vega-lite binding <https://vega.github.io/vega-lite/docs/bind.html#input-element-binding>`_, selections can be bound two-ways:

1. Single selections can be bound directly to an input elements. *For example, a radio button.*
2. Interval selections which can be bound to scale. *for example, zooming in on a map.*

Input Element Binding
^^^^^^^^^^^^^^^^^^^^^
With single selections, an input element can be added to the chart to establish a binding between the input and the selection. 

For instance, using our example from above a dropdown can be used to highlight cars from a specific ``origin`` :

.. altair-plot::

    input_dropdown = alt.binding_select(options=['Europe','Japan','USA'])
    selection = alt.selection_single(fields=['Origin'], bind=input_dropdown, name='Country of ')
    color = alt.condition(selection,
                        alt.Color('Origin:N', legend=None),
                        alt.value('lightgray'))

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
        tooltip='Name:N'
    ).add_selection(
        selection
    )


    

The above example shows all three elements at work. The :input_dropdown: is :bind: to the :selection: which is called from the :condition: encoded through the data. 

The following are the input elements supported in vega-lite: 


========================= ===========================================================================  ===============================================
Input Element             Description                                                                   Example
========================= ===========================================================================  ===============================================
:class:`binding_checkbox` Renders as checkboxes allowing for multiple selections of items.                    :ref:`gallery_multiple_interactions`
:class:`binding_radio`    Radio buttons that force only a single selection                                    :ref:`gallery_multiple_interactions`
:class:`binding_select`   Drop down box for selecting a single item from a list                               :ref:`gallery_multiple_interactions`
:class:`binding_range`    Shown as a slider to allow for selection along a scale.                             :ref:`gallery_us_population_over_time`
========================= ===========================================================================  ===============================================


Bindings and input elements can also be used to filter data on the client side. Reducing noise in the chart and allowing the user to see just certain selected elements:

.. altair-plot::

    input_dropdown = alt.binding_select(options=['Europe','Japan','USA'])
    selection = alt.selection_single(fields=['Origin'], bind=input_dropdown, name='Country of ')
    color = alt.condition(selection,
                        alt.Color('Origin:N', legend=None),
                        alt.value('lightgray'))

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        tooltip='Name:N'
    ).add_selection(
        selection
    ).transform_filter(
        selection
    )


Scale Binding
^^^^^^^^^^^^^
With interval selections, the ``bind`` property can be set to the value of ``"scales"``. In these cases, the binding will automatically respond to the panning and zooming along the chart:

.. altair-plot::

    selection = alt.selection_interval(bind='scales')

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        tooltip='Name:N'
    ).add_selection(
        selection
    )
    



Further Examples
~~~~~~~~~~~~~~~~
Now that you understand the basics of Altair selections and bindings, you might wish to look
through the :ref:`gallery-category-Interactive Charts` section of the example gallery
for ideas about how they can be applied to more interesting charts.

For more information on how to fine-tune selections, including specifying other
mouse and keystroke options, see the `Vega-Lite Selection documentation
<https://vega.github.io/vega-lite/docs/selection.html>`_.
