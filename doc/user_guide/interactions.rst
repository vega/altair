.. currentmodule:: altair

.. _user-guide-interactions:

Interactive Charts: Parameters, Conditions, Bindings
====================================================

One of the unique features of Altair, inherited from Vega-Lite, is a
declarative grammar of not just visualization, but *interaction*.
This is both convenient and powerful,
as we will see in this section.
There are three core concepts of this grammar:

- Parameters are the basic building blocks in the grammar of interaction.
  They can either be a simple variable or the more complex :func:`selection`
  that map user input (e.g., mouse clicks and drags) to data queries.
- The :func:`condition` function takes the selection input
  and changes an element of the chart based on that input.
- The ``bind`` property of selections establishes a two-way binding
  between the selection and an input element of your chart,
  such as a drop-down, radio button or slider.

Interactive charts can use one or more of these elements to create rich interactivity between the viewer and the data.


Parameters: Building Blocks of Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Interactivity in Altair is built around *parameters*, of which there are two types: variables and selections.  We introduce these concepts through a series examples.

.. note::

   This material was changed considerably with the release of Altair 5.  In particular, Altair 4 had selections but not variables, and the term ``parameter`` first appeared in Altair 5.

.. _basic variable:

Variables: Storing and Reusing Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variables are the simplest forms of parameters can take.
Variable parameters allow for a value to be defined once
and then reused throughout the rest of the chart.
Here is a simple scatter-plot created from the ``cars`` dataset:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_circle().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    )

We can create a variable parameter using :func:`param`, and assign that parameter a default value of 0.1 using the ``value`` property, as follows:

.. altair-plot::
    :output: none

    op_var = alt.param(value=0.1)

In order to use this variable in the chart specification, we explicitly add it to the chart using the :meth:`Chart.add_params` method, and we can then reference the variable within the chart specification.  Here we set the opacity using our ``op_var`` parameter.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    op_var = alt.param(value=0.1)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_params(
        op_var
    )

It's reasonable to ask whether all this effort is necessary.  Here is a more natural way to accomplish the same thing.  We avoid the use of both :func:`param` and ``add_params``.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    op_var2 = 0.1

    alt.Chart(cars).mark_circle(opacity=op_var2).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    )

The benefit of using :func:`param` doesn't become apparent until we incorporate an additional component, such as in the following, where we use the ``bind`` property of the parameter, so that the parameter becomes bound to an input element.  In this example, that input element is a slider widget.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    slider = alt.binding_range(min=0, max=1, step=0.05, name='opacity:')
    op_var = alt.param(value=0.1, bind=slider)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_params(
        op_var
    )

Now we can dynamically change the opacity of the points in our chart using the slider.  A noteworthy aspect of this chart is that these effects are controlled entirely within your web browser.  Once the Vega-Lite chart specification has been created by Altair, the result is an interactive chart, and that interactivity no longer requires a running Python environment.

The above example includes some aspects which occur frequently when creating interactive charts in Altair:

1. Creating a variable parameter using :func:`param`.
2. Attaching the parameter to a chart using the :meth:`Chart.add_params` method.
3. Binding the parameter to an input widget (such as the slider above) using the parameter's ``bind`` property.


Selections: Capturing Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selections parameters capture inputs such as mouse clicks and they can be *bound* to
particular charts or sub-charts in your visualization, then referenced
in other parts of the visualization.
There are two types of selections:
:func:`selection_interval` and :func:`selection_point`.

Here we will create a simple chart and then add an selection interval to it.
We could create a selection interval via ``alt.param(select="interval")``,
but it is more convenient to use the shorter ``alt.selection_interval``
(and this also matches the syntax that was used in Altair 4).

Here is a simple scatter-plot created from the ``cars`` dataset:

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
    ).add_params(
        brush
    )

The result above is a chart that allows you to click and drag to create
a selection region, and to move this region once the region is created.

So far this example is very similar to what we did in the :ref:`variable example <basic variable>`:
we created a selection parameter using ``brush = alt.selection_interval()``,
and we attached that parameter to the chart using ``add_params``.

Conditions: Making the Chart Respond
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example above is neat, but the selection doesn't actually *do* anything yet.
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
    ).add_params(
        brush
    )

As you can see, with this simple change, the color of the points responds
to the selection.
In the sample above,
we are using the selection parameter ``brush`` as a *predicate*
(something that evaluates as `True` or `False`).
This is controlled by the line ``color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))``.
Data points which fall within the selection evaluate as ``True``,
and data points which fall outside the selection evaluate to ``False``.
The ``'Origin:N'`` specifies how to color the points which fall within the selection,
and the ``alt.value('lightgray')`` specifies that the outside points should be given a constant color value;
you can remember this as ``alt.condition(<condition>, <if_true>, <if_false>)``.

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
    ).add_params(
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
    ).add_params(
        brush
    )

    chart.encode(x='Acceleration:Q') | chart.encode(x='Miles_per_Gallon:Q')

Selection Types: Interval and Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have seen the basics of how we can use a selection to interact with a chart,
let's take a more systematic look at some of the types of selection parameters available in Altair.
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
        ).add_params(
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
    ).add_params(
        scales
    )

Because this is such a common pattern, Altair provides the :meth:`Chart.interactive`
method which creates such a selection more concisely.


Point Selections
^^^^^^^^^^^^^^^^
A *point* selection allows you to select chart elements one at a time
via mouse actions. By default, points are selected on click:

.. altair-plot::

    point = alt.selection_point()
    make_example(point)

By changing some arguments, we can select points on mouseover rather than on
click. We can also set the ``nearest`` flag to ``True`` so that the nearest
point is highlighted:

.. altair-plot::

    point_nearest = alt.selection_point(on='mouseover', nearest=True)
    make_example(point_nearest)

Point selections also allow for multiple chart objects to be selected.
By default, chart elements can be added to and removed from the selection
by clicking on them while holding the *shift* key:

The point selection accepts the ``toggle`` parameter,
which controls whether points can be removed from the selection
once they are added.
For example,
here is a plot where you can "paint" the chart objects
by hovering over them with your mouse:

.. altair-plot::

    point_mouseover = alt.selection_point(on='mouseover', toggle=False, empty='none')
    make_example(point_mouseover)

Composing Multiple Selections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair also supports combining multiple selections using the ``&``, ``|``
and ``~`` for respectively ``AND``, ``OR`` and ``NOT`` logical composition
operands.

In the following example there are two people who can make an interval
selection in the chart. The person Alex makes a selection box when the
alt-key (macOS: option-key) is selected and Morgan can make a selection
box when the shift-key is selected.
We use the alt.Brushconfig() to give the selection box of Morgan a different
style.
Now, we color the rectangles when they fall within Alex's or Morgan's
selection.

.. altair-plot::

    alex = alt.selection_interval(
        on="[mousedown[event.altKey], mouseup] > mousemove",
        name='alex'
    )
    morgan = alt.selection_interval(
        on="[mousedown[event.shiftKey], mouseup] > mousemove",
        mark=alt.BrushConfig(fill="#fdbb84", fillOpacity=0.5, stroke="#e34a33"),
        name='morgan'
    )

    alt.Chart(cars).mark_rect().encode(
        x='Cylinders:O',
        y='Origin:O',
        color=alt.condition(alex | morgan, 'count()', alt.ColorValue("grey"))
    ).add_params(
        alex, morgan
    ).properties(
        width=300,
        height=180
    )

With these operators, selections can be combined in arbitrary ways:

- ``~(alex & morgan)``: to select the rectangles that fall outside
  Alex's and Morgan's selections.

- ``alex | ~morgan``: to select the rectangles that fall within Alex's
  selection or outside the selection of Morgan


Selection Targets: Fields and Encodings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For any but the simplest selections, the user needs to think about exactly
what is targeted by the selection, and this can be controlled with either the
``fields`` or ``encodings`` arguments. These control what data properties are
used to determine which points are part of the selection.

For example, here we create a small chart that acts as an interactive legend,
by targeting the Origin field using ``fields=['Origin']``. Clicking on points
in the upper-right plot (the legend) will propagate a selection for all points
with a matching ``Origin``.

.. altair-plot::

    selection = alt.selection_point(fields=['Origin'])
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
    ).add_params(
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

    selection = alt.selection_point(fields=['Origin', 'Cylinders'])
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
    ).add_params(
        selection
    )

    scatter | legend

By fine-tuning the behavior of selections in this way, they can be used to
create a wide variety of linked interactive chart types.


Filtering Data with Selections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using a selection parameter to filter data works in much the same way
as using it within ``alt.condition``,
For example, in ``transform_filter(brush)``,
we are again using the selection parameter ``brush`` as a predicate.
Data points which evaluate to ``True`` (i.e., data points which lie within the selection) are kept,
and data points which evaluate to ``False`` are filtered out.

It is not possible to both select and filter in the same chart,
so typically this functionality will be used when at least two sub-charts are present.
In the following example,
we attach the selection parameter to the upper chart,
and then filter data in the lower chart based selection in the upper chart.
You can explore how the counts changes in the bar chart
depending on the size and position of the selection in the scatter plot.

.. altair-plot::

    brush = alt.selection_interval()

    points = alt.Chart(cars).mark_circle().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).add_params(
        brush
    )

    bars = alt.Chart(cars).mark_bar().encode(
        x='count()',
        y='Origin:N',
        color='Origin:N'
    ).transform_filter(
        brush
    )

    points & bars


Binding: Adding Data Driven Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
With an understanding of the selection types and conditions, you can now add data-driven input elements to the charts using the ``bind`` option. As specified by `Vega-lite binding <https://vega.github.io/vega-lite/docs/bind.html#input-element-binding>`_, selections can be bound two-ways:

1. Point selections can be bound directly to an input element, *for example, a radio button.*
2. Interval selections which can be bound to scale, *for example, zooming in on a map.*

Input Element Binding
^^^^^^^^^^^^^^^^^^^^^
With point selections, an input element can be added to the chart to establish a binding between the input and the selection.

For instance, using our example from above a dropdown can be used to highlight cars from a specific ``origin`` :

.. altair-plot::

    input_dropdown = alt.binding_select(options=['Europe','Japan','USA'], name='Region ')
    selection = alt.selection_point(fields=['Origin'], bind=input_dropdown)
    color = alt.condition(selection,
                        alt.Color('Origin:N', legend=None),
                        alt.value('lightgray'))

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
        tooltip='Name:N'
    ).add_params(
        selection
    )




The above example shows all three elements at work. The ``input_dropdown`` is ``bind`` to the ``selection`` which is called from the ``condition`` encoded through the data.

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

    input_dropdown = alt.binding_select(options=['Europe','Japan','USA'], name='Region ')
    selection = alt.selection_point(fields=['Origin'], bind=input_dropdown)

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        tooltip='Name:N'
    ).add_params(
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
    ).add_params(
        selection
    )


Parameter Values in Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selection Parameters
^^^^^^^^^^^^^^^^^^^^

Selection values can be accessed directly and used in expressions that affect the
chart. For example, here we create a slider to choose a cutoff value, and color
points based on whether they are smaller or larger than the value:

.. altair-plot::

   import altair as alt
   import pandas as pd
   import numpy as np

   rand = np.random.RandomState(42)

   df = pd.DataFrame({
       'xval': range(100),
       'yval': rand.randn(100).cumsum()
   })

   slider = alt.binding_range(min=0, max=100, step=1, name='Cutoff ')
   selector = alt.selection_point(name="SelectorName", fields=['cutoff'],
                                   bind=slider, value=[{'cutoff': 50}])

   alt.Chart(df).mark_point().encode(
       x='xval',
       y='yval',
       color=alt.condition(
           alt.datum.xval < selector.cutoff,
           # 'datum.xval < SelectorName.cutoff',  # An equivalent alternative
           alt.value('red'), alt.value('blue')
       )
   ).add_params(
       selector
   )

Selector values can be similarly used anywhere that expressions are valid, for
example, in a :ref:`user-guide-calculate-transform` or a
:ref:`user-guide-filter-transform`.

Variable Parameters
^^^^^^^^^^^^^^^^^^^

While it is useful to know
how to access selection parameter values
in expression strings,
the variable parameters introduced in Altair 5
often provides a more convenient syntax
for simple interactions like this one
since they can also be accessed in expression strings:

.. altair-plot::

    slider = alt.binding_range(min=0, max=100, step=1, name='Cutoff ')
    selector = alt.param(name='SelectorName', value=50, bind=slider)

    alt.Chart(df).mark_point().encode(
       x='xval',
       y='yval',
       color=alt.condition(
           alt.datum.xval < selector,
           # 'datum.xval < SelectorName',  # An equivalent alternative
           alt.value('red'), alt.value('blue')
       )
    ).add_params(
       selector
    )


Further Examples
~~~~~~~~~~~~~~~~
Now that you understand the basics of Altair selections and bindings, you might wish to look
through the :ref:`gallery-category-Interactive Charts` section of the example gallery
for ideas about how they can be applied to more interesting charts.

For more information on how to fine-tune selections, including specifying other
mouse and keystroke options, see the `Vega-Lite Selection documentation
<https://vega.github.io/vega-lite/docs/selection.html>`_.

Limitations
~~~~~~~~~~~

Some possible use cases for the above interactivity are not currently supported by Vega-Lite, and hence are not currently supported by Altair.  Here are some examples.

1. If we are using a ``selection_point``, it would be natural to want to return information about the chosen data point, and then process that information using Python.  This is not currently possible (and as of December 2021 it does not seem likely to become possible any time soon), so any data processing will have to be handled using tools such as ``transform_calculate``, etc. You can follow the progress on this in the following issue: https://github.com/altair-viz/altair/issues/1153.

   - The dashboarding package ``Panel`` has added support for processing Altair selections with custom callbacks in their 0.13 release. This is currently the only Python dashboarding package that supports custom callbacks for Altair selections and you can read more about how to use this functionality in `the Panel documentation <https://pyviz-dev.github.io/panel/reference/panes/Vega.html#selections>`_.

2. It is not possible to use an encoding such as ``y=column_variable`` to then dynamically display different charts based on different column choices.  Similar functionality could be created using for example ``ipywidgets`` or ``panel``, but the resulting interactivity would be controlled by Python, and would not work for example as a stand-alone web page.  The underlying reason this is not possible is that in Vega-Lite, the ``field`` property does not accept a parameter as value; see the `field Vega-Lite documentation <https://vega.github.io/vega-lite/docs/field.html>`_. You can follow the discussion in this issue https://github.com/vega/vega-lite/issues/7365. In the meantime you can workaround this by transforming the data into long form using either `melt` in pandas or :meth:`transform_fold` in Altair.

.. altair-plot::
    source = data.cars().melt(id_vars=['Origin', 'Name', 'Year', 'Horsepower', 'Cylinders'])
    dropdown_options = source['variable'].drop_duplicates().tolist()

    dropdown = alt.binding_select(
        options=dropdown_options,
        name='X-axis column'
    )
    selection = alt.selection_point(
        fields=['variable'],
        value=[{'variable': dropdown_options[0]}],
       # init={'variable': dropdown_options[0]},  # For Altair 4
        bind=dropdown
    )

    alt.Chart(source).mark_circle().encode(
        x=alt.X('value:Q', title=''),
        y='Horsepower',
        color='Origin',
    ).add_selection(
        selection
    ).transform_filter(
        selection
    )

Taking advantage of the parameter interface introduced in Altair 5, we can express this more succinctly:

.. altair-plot::
    dropdown = alt.binding_select(
        options=['Miles_per_Gallon', 'Displacement', 'Weight_in_lbs', 'Acceleration'],
        name='X-axis column '
    )
    param = alt.param(
        name='selected_column',
        value='Miles_per_Gallon',
        bind=dropdown
    )

    alt.Chart(data.cars.url).mark_circle().encode(
        x='x:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).transform_calculate(
        x='datum[selected_column]'
    ).add_params(
        param
    )
