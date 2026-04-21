.. currentmodule:: altair

.. _parameters:

Parameters, Conditions, & Filters
=================================

Parameters
~~~~~~~~~~

Parameters are the building blocks of interaction in Altair.
There are two types of parameters: *variables* and *selections*. We introduce these concepts through a series of examples.

.. note::

   This material was changed considerably with the release of Altair 5.

.. _basic variable:

Variables: Reusing Values
^^^^^^^^^^^^^^^^^^^^^^^^^

Variable parameters allow for a value to be defined once
and then reused throughout the rest of the chart.
Here is a simple scatter-plot created from the ``cars`` dataset:

.. altair-plot::

    import altair as alt
    from altair.datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_circle().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )

Variable parameters are created using the :func:`param` function.
Here,
we create a parameter with a default value of 0.1 using the ``value`` property:

.. altair-plot::
    :output: none

    op_var = alt.param(value=0.1)

In order to use this variable in the chart specification, we explicitly add it to the chart using the :meth:`add_params` method, and we can then reference the variable within the chart specification.  Here we set the opacity using our ``op_var`` parameter. The :meth:`add_params` method adds the parameter to the chart, making it available for use in encodings, conditions, and filters.

.. altair-plot::

    op_var = alt.param(value=0.1)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).add_params(
        op_var
    )

It's reasonable to ask whether all this effort is necessary. Here is a more natural way to accomplish the same thing that avoids the use of both :func:`param` and ``add_params``.

.. altair-plot::

    op_var2 = 0.1

    alt.Chart(cars).mark_circle(opacity=op_var2).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )

The benefit of using :func:`param` doesn't become apparent until we incorporate an additional component. In the following example we use the ``bind`` property of the parameter, so that the parameter becomes bound to an input element. In this example, that input element is a slider widget.

.. altair-plot::

    slider = alt.binding_range(min=0, max=1, step=0.05, name='opacity:')
    op_var = alt.param(value=0.1, bind=slider)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).add_params(
        op_var
    )

Now we can dynamically change the opacity of the points in our chart using the slider. You will learn much more about binding parameters to input elements such as widgets in the section :ref:`binding-parameters`.

.. note::

    A noteworthy aspect of Altair's interactivity is that these effects are controlled entirely within the web browser. This means that you can save charts as HTML files and share them with your colleagues who can access the interactivity via their browser without the need to install Python.

Selections: Capturing Chart Interactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selection parameters define data queries
that are driven by interactive manipulation of the chart
by the user (e.g., via mouse clicks or drags).
There are two types of selections:
:func:`selection_interval` and :func:`selection_point`.

Here we will create a simple chart and then add a selection interval to it.
We could create a selection interval via ``param(select="interval")``,
but it is more convenient to use the shorter ``selection_interval``.

Here is a simple scatter-plot created from the ``cars`` dataset:

.. altair-plot::

    import altair as alt
    from altair.datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )

First we'll create an interval selection using the :func:`selection_interval`
function (an interval selection is also referred to as a "brush"):

.. altair-plot::
    :output: none

    brush = alt.selection_interval()

We can now add this selection interval to our chart via ``add_params``:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).add_params(
        brush
    )

The result above is a chart that allows you to click and drag to create
a selection region, and to move this region once the region is created.

So far this example is very similar to what we did in the :ref:`variable example <basic variable>`:
we created a selection parameter using ``brush = alt.selection_interval()``,
and we attached that parameter to the chart using ``add_params``.
One difference is that here we have not defined how the chart should respond to the selection; you will learn this in the next section.

.. _conditions:

Conditions
~~~~~~~~~~

.. note::

   This material was changed considerably with the release of Altair ``5.5.0``.
   :func:`when` was introduced in ``5.4.0`` and should be preferred over :func:`condition`.

The example above is neat, but the selection interval doesn't actually *do* anything yet.
To make the chart respond to this selection, we need to reference ``brush`` within
the chart specification. Here, we will use the :func:`when` function to create
a conditional color encoding:

.. altair-plot::

    conditional = alt.when(brush).then("Origin:N").otherwise(alt.value("lightgray"))

    alt.Chart(cars).mark_point().encode(
        x="Horsepower:Q",
        y="Miles_per_Gallon:Q",
        color=conditional,
    ).add_params(
        brush
    )

As you can see, the color of the points now changes depending on whether they are inside or outside the selection.
Above we are using the selection parameter ``brush`` as a *predicate*
(something that evaluates as `True` or `False`).

This is controlled by our definition ``conditional``::

    conditional = alt.when(brush).then("Origin:N").otherwise(alt.value("lightgray"))

Data points which fall within the selection evaluate as ``True``,
and data points which fall outside the selection evaluate to ``False``.
The ``"Origin:N"`` specifies how to color the points which fall within the selection,
and the ``alt.value('lightgray')`` specifies that the outside points should be given a constant color value.

Understanding :func:`when`
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``when-then-otherwise`` syntax was directly inspired by `polars.when`_,
and is similar to an ``if-else`` statement written in Python::

    # alt.when(brush)
    if brush:
        # .then("Origin:N")
        color = "Origin:N"
    else:
        # .otherwise(alt.value("lightgray"))
        color = alt.value("lightgray")

Omitting the ``.otherwise()`` clause will use the channel default instead:

.. altair-plot::

    source = data.cars()
    brush = alt.selection_interval()

    points = alt.Chart(source).mark_point().encode(
        x="Horsepower",
        y="Miles_per_Gallon",
        color=alt.when(brush).then(alt.value("goldenrod"))
    ).add_params(
        brush
    )

    points

Multiple conditional branches (``if, elif, ..., elif`` in Python)
are expressed via chained calls to :func:`when`.
You will see an example with working code in :ref:`conditional-branches`
when you have learned about different selection types.

More advanced use of conditions can be found
in the :func:`when` API reference
and in these gallery examples:

- :ref:`gallery_dot_dash_plot`
- :ref:`gallery_interactive_bar_select_highlight`
- :ref:`gallery_multiline_tooltip_standard`
- :ref:`gallery_scatter_point_paths_hover`
- :ref:`gallery_waterfall_chart`

Linking Conditions Across Charts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Conditional encodings become even more powerful when the selection behavior is
tied across multiple views of the data within a compound chart.
For example, here we create a :class:`Chart` using the same code as
above, and horizontally concatenate two versions of this chart: one
with the x-encoding tied to ``"Horsepower"``, and one with the x-encoding
tied to ``"Acceleration"``

.. altair-plot::

    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.when(brush).then("Origin:N").otherwise(alt.value("lightgray")),
    ).properties(
        width=250,
        height=250
    ).add_params(
        brush
    )

    chart | chart.encode(x='Acceleration:Q')

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
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.when(brush).then("Origin:N").otherwise(alt.value("lightgray")),
    ).properties(
        width=250,
        height=250
    ).add_params(
        brush
    )

    chart | chart.encode(x='Acceleration:Q')

As you might have noticed,
the selected points are sometimes obscured by some of the unselected points.
To bring the selected points to the foreground,
we can change the order in which they are laid out via the following conditional ``order`` encoding:

.. altair-plot::

    # Lower numbers for `order` means further into the background
    selected_on_top = alt.when(brush).then(alt.value(1)).otherwise(alt.value(0))
    chart.encode(order=selected_on_top) | chart.encode(order=selected_on_top, x='Acceleration:Q')

You can see another example of this in the :ref:`gallery_selection_zorder` gallery example.

Filters
~~~~~~~

Using a selection parameter to filter data works in much the same way
as using it within :func:`when`.
For example, in ``transform_filter(brush)``,
we are again using the selection parameter ``brush`` as a predicate.
Data points which evaluate to ``True`` (i.e., data points which lie within the selection) are kept,
and data points which evaluate to ``False`` are filtered out.

It is not possible to both select and filter in the same chart,
so typically this functionality will be used when at least two sub-charts are present.
In the following example,
we attach the selection parameter to the upper chart,
and then filter data in the lower chart based on the selection in the upper chart.
You can explore how the counts change in the bar chart
depending on the size and position of the selection in the scatter plot.

.. altair-plot::

    brush = alt.selection_interval()

    points = alt.Chart(cars).mark_point().encode(
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


Selection Types
~~~~~~~~~~~~~~~

Now that we have seen the basics of how we can use a selection to interact with a chart,
let's take a more systematic look at the types of selection parameters available in Altair.
There are two main types of selections you'll work with through mouse actions:

1. **Interval selections**: Select ranges of data by clicking and dragging
2. **Point selections**: Select individual data points by clicking or hovering

To demonstrate these selection types clearly, we'll use a consistent visualization
approach. The following helper function creates a heatmap from the ``cars`` dataset
where the color encoding responds to our selection:

.. altair-plot::
    :output: none

    def make_example(selector: alt.Parameter) -> alt.Chart:
        cars = data.cars.url

        return alt.Chart(cars).mark_rect().encode(
            x="Cylinders:O",
            y="Origin:N",
            color=alt.when(selector).then("count()").otherwise(alt.value("lightgray")),
        ).properties(
            width=300,
            height=180
        ).add_params(
            selector
        )

Interval Selections
^^^^^^^^^^^^^^^^^^^
An *interval* selection allows you to select a range of data elements by clicking and dragging.
This is often referred to as a "brush" selection and is commonly used for filtering,
zooming, or highlighting ranges of data points.

Basic Interval Selection
""""""""""""""""""""""""
The simplest interval selection is created with the :func:`selection_interval` function:

.. altair-plot::

   interval = alt.selection_interval()
   make_example(interval)

As you click and drag on the plot, your mouse creates a selection region that can be
moved to change which data points are selected.

Customizing Interval Behavior
"""""""""""""""""""""""""""""
The :func:`selection_interval` function accepts several arguments for customization.
For example, you can limit the selection to only the x-axis and set it so that
an empty selection contains no points:

.. altair-plot::

   interval_x = alt.selection_interval(encodings=['x'], empty=False)
   make_example(interval_x)

The ``empty=False`` argument can also be set inside :func:`when` to control
how individual conditions respond to empty selections.  
By default, `empty=True`, which means the selection predicate evaluates to 
true for *all* data points when the selection is empty.  
With `empty=False`, the predicate evaluates to false for all points when 
the selection is empty. 
This affects what happens when no data points are selected yet::

    brush = alt.selection_interval()

    # Default behavior (empty=True): When no selection is made in this example, all points will be colored according to their "Origin" category (they are considered as *selected*, and colored according to the `then` clause)
    color=alt.when(brush).then("Origin:N").otherwise(alt.value("lightgray"))

    # Custom behavior (empty=False): When no selection is made in this example, all points will be lightgray (they are considered as *unselected*, and colored according to the `otherwise` clause )
    color=alt.when(brush, empty=False).then("Origin:N").otherwise(alt.value("lightgray"))

Setting Initial Values
""""""""""""""""""""""
When creating interactive visualizations, you often want to guide users by
starting with a pre-selected region rather than an empty selection. You can do this
using the ``value`` parameter of :func:`selection_interval`.

Setting initial values is particularly useful when:

- Creating a filtered overview-detail pattern where a detailed subset is shown
- Guiding viewer attention to a particular area of interest immediately
- Preserving selection states across different visualizations or user sessions

Here's an example using time series data where we initially focus on a specific date range
containing the 2008 financial crisis:

.. altair-plot::

    import altair as alt
    from altair.datasets import data
    import datetime as dt

    source = data.sp500.url

    # Define initial date range to select
    date_range = (dt.date(2007, 6, 30), dt.date(2009, 6, 30))

    # Create interval selection with initial value
    brush = alt.selection_interval(
        encodings=['x'],
        value={'x': date_range}
    )

    # Create base chart for both panels
    base = alt.Chart(source, width=600, height=200).mark_area().encode(
        x = 'date:T',
        y = 'price:Q'
    )

    # Upper panel shows detailed view filtered by the brush
    upper = base.encode(
        alt.X('date:T').scale(domain=brush)
    )

    # Lower panel shows overview with the brush control
    lower = base.properties(
        height=60
    ).add_params(brush)

    # Combine the two charts
    upper & lower

This example demonstrates an "overview+detail" pattern - a common visualization technique
where one chart shows the complete dataset while another shows a detailed view of the
selected portion.

When working with datetime values, you can use Python's native ``datetime.date`` or 
``datetime.datetime`` objects directly. Altair automatically handles the conversion of 
these objects to the appropriate format for Vega-Lite.

The format of the ``value`` parameter depends on the encodings used in the selection:

- For selections with `x` encoding: ``value={'x': [min, max]}``
- For selections with `y` encoding: ``value={'y': [min, max]}``
- For selections with both: ``value={'x': [xmin, xmax], 'y': [ymin, ymax]}``

You can also set initial values of a selection with categorical data. In this case the list/tuple specifies the exact categories to be selection rather than a range of categories. For example, to initially select only cars with 4 or 6 cylinders:

.. altair-plot::

    cylinder_select = alt.selection_interval(
        encodings=['x'],
        value={"x": [4, 6]}  # Select 4 and 6 (but not 5) cylinder cars
    )
    make_example(cylinder_select)


Point Selections
^^^^^^^^^^^^^^^^
A *point* selection allows you to select individual data elements one at a time.
Unlike interval selections which select ranges, point selections work with discrete 
data points, making them ideal for interactive legends, tooltips, and highlighting 
specific data points.

Basic Point Selection
"""""""""""""""""""""
The simplest point selection is created with the :func:`selection_point` function. 
By default, points are selected on click:

.. altair-plot::

    point = alt.selection_point()
    make_example(point)

By changing the ``on`` parameter to `'pointerover'`, we can select points when hovering over them rather than on
click.
The ``on`` parameter accepts `any "Event Stream Selector" supported by Vega
<https://vega.github.io/vega/docs/event-streams/#selector>`_
and you can see more elaborate example at the end of the :ref:`parameter-composition` section.
We can also set the ``nearest`` flag to ``True`` so that the nearest
point is highlighted instead of when the pointer is directly touching a point:

.. altair-plot::

    point_nearest = alt.selection_point(on='pointerover', nearest=True)
    make_example(point_nearest)

Point selections also support multi-selection. By default, you can add or remove 
data points from your selection by holding the *shift* key while clicking. Try this
behavior in the examples above to see how it works.

Setting Initial Values
""""""""""""""""""""""
You can also set initial values for point selections using the ``value`` parameter.  For point selections, the value is a dictionary specifying the initial selection based on fields or encodings.

.. altair-plot::

    point_initial = alt.selection_point(
        fields=['Origin'],
        value=[{'Origin': 'USA'}]  # Initially select USA
    )
    make_example(point_initial)

Selection Targets
~~~~~~~~~~~~~~~~~

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
    color = (
        alt.when(selection)
        .then(alt.Color("Origin:N").legend(None))
        .otherwise(alt.value("lightgray"))
    )

    scatter = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
        tooltip='Name:N'
    )

    legend = alt.Chart(cars).mark_point().encode(
        alt.Y('Origin:N').axis(orient='right'),
        color=color
    ).add_params(
        selection
    )

    scatter | legend

Alternatively, we could express ``fields=['Origin']`` as ``encodings=['color']``, because our chart maps ``color`` to
``'Origin'``. Also note that there is a shortcut to create interactive legends in Altair
described in the section :ref:`legend-binding`.

Similarly, we can specify multiple fields and/or encodings that must be
matched in order for a datum to be included in a selection.
For example, we could modify the above chart to create a two-dimensional
clickable legend that will select points by both Origin and number of
cylinders:

.. altair-plot::

    selection = alt.selection_point(fields=['Origin', 'Cylinders'])
    color = (
        alt.when(selection)
        .then(alt.Color("Origin:N").legend(None))
        .otherwise(alt.value("lightgray"))
    )

    scatter = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
        tooltip='Name:N'
    )

    legend = alt.Chart(cars).mark_rect().encode(
        alt.Y('Origin:N').axis(orient='right'),
        x='Cylinders:O',
        color=color
    ).add_params(
        selection
    )

    scatter | legend

By fine-tuning the behavior of selections in this way, they can be used to
create a wide variety of linked interactive chart types.

Combining Parameters
~~~~~~~~~~~~~~~~~~~~

Multiple parameters can be combined in a single chart,
either via multiple separate response conditions,
different conditional branches in :func:`when`,
or parameter composition.

Multiple conditions
^^^^^^^^^^^^^^^^^^^

In this example,
points that are hovered with the pointer
will increase in size
and those that are clicked
will be filled in with red.
The ``empty=False`` is to ensure that no points are selected to start.
Try holding shift to select multiple points on either hover or click.

.. altair-plot::

    click = alt.selection_point(empty=False)
    hover = alt.selection_point(on='pointerover', empty=False)

    points = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        fill=alt.when(click).then(alt.value('red')),
        size=alt.when(hover).then(alt.value(1000))
    ).add_params(
        click, hover
    )

    points

.. _conditional-branches:

Conditional branches
^^^^^^^^^^^^^^^^^^^^

:func:`when` allows the use of multiple ``then`` (``elif``) branches
which can change the behavior of a single encoding
in response to multiple different parameters.
Here,
we fill hovered points in yellow,
before changing the fill to red
when a point is clicked.
Since the mouse is hovering over points
while clicking them,
both conditions will be active
and the earlier branch takes precedence
(you can try by changing the order of the two ``when.then`` clauses
and observing that the points will not change to red when clicked).

.. altair-plot::

    click = alt.selection_point(empty=False)
    hover = alt.selection_point(on='pointerover', empty=False)

    points = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        fill=(
            alt.when(click)
            .then(alt.value('red'))
            .when(hover)
            .then(alt.value('gold'))
        ),
        size=alt.when(hover).then(alt.value(1000))
    ).add_params(
        click, hover
    )

    points

.. _parameter-composition:

Parameter Composition
^^^^^^^^^^^^^^^^^^^^^

Altair also supports combining multiple parameters using the ``&``, ``|``
and ``~`` for respectively ``AND``, ``OR`` and ``NOT`` logical composition
operands.
These parameter compositions can be used with both filters and conditions in Altair.
In the following example,
only the points that fall within the interval selections of both the scatter plots
will be counted in the bar chart
(so you will need to make a selection in both charts
before the bars shows up).

.. altair-plot::

    # empty=False ensure that no points are selected before a selection is drawn
    brush = alt.selection_interval(empty=False)
    brush2 = alt.selection_interval(empty=False)

    points = alt.Chart(cars).mark_point(size=10).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )

    points2 = points.encode(
        x='Acceleration:Q',
        y='Miles_per_Gallon:Q',
    )

    bars = alt.Chart(cars).mark_bar().encode(
        x='count()',
        y='Origin:N',
        color='Origin:N'
    ).transform_filter(
        brush & brush2
    )

    (points.add_params(brush) | points2.add_params(brush2)) & bars

To illustrate how a more complex parameter composition
can be applied to a conditional encoding,
we can return to our heatmap example.
Let's construct a scenario where there are two people who can make an interval
selection in the same chart. The person Alex makes a selection box when the
alt-key (macOS: option-key) is selected and Morgan can make a selection
box when the shift-key is selected.
Now, we color the chart marks when they fall within Alex's or Morgan's
selection, but not both's
(note that you need to create both selections before seeing the effect).
Here, we also use We use :class:`BrushConfig` to give the selection box of Morgan a different
style to be able to tell them apart.

.. altair-plot::

    alex = alt.selection_interval(
        on="[pointerdown[event.altKey], pointerup] > pointermove",
        empty=False,
    )
    morgan = alt.selection_interval(
        on="[pointerdown[event.shiftKey], pointerup] > pointermove",
        mark=alt.BrushConfig(fill="#fdbb84", fillOpacity=0.5, stroke="#e34a33"),
        empty=False,
    )

    exlusive_or = (alex | morgan) & ~(alex & morgan)

    alt.Chart(cars).mark_rect().encode(
        x='Cylinders:O',
        y='Origin:O',
        color=alt.when(exlusive_or).then("count()").otherwise(alt.value("grey")),
    ).add_params(
        alex, morgan
    ).properties(
        width=300,
        height=180
    )

With these operators, selections can be combined in arbitrary ways:

- ``alex | morgan``: to select the rectangles that fall inside either
  Alex's or Morgans' selection.
- ``~(alex & morgan)``: to select the rectangles that fall outside
  Alex's and Morgan's selections.
- ``alex | ~morgan``: to select the rectangles that fall within Alex's
  selection or outside the selection of Morgan

For more information on how to fine-tune selections, including specifying other
mouse and keystroke options, see the `Vega-Lite Selection documentation
<https://vega.github.io/vega-lite/docs/selection.html>`_.  Also see :class:`BrushConfig` for information on how to customize the appearance of the brush.

.. _polars.when:
    https://docs.pola.rs/py-polars/html/reference/expressions/api/polars.when.html
