.. currentmodule:: altair

.. _user-guide-interactions:

Interactive Charts
==================

One of the unique features of Altair, inherited from Vega-Lite, is a
declarative grammar of not just visualization, but also *interaction*.
This is both convenient and powerful,
as we will see in this section.
There are three core concepts of this grammar:

- Parameters are the basic building blocks in the grammar of interaction.
  They can either be a simple variables or more complex selections
  that map user input (e.g., mouse clicks and drags) to data queries.
- Conditions and filters can respond to changes in parameter values
  and update chart elements based on that input.
- Widgets and other chart input elements can bind to parameters
  so that charts can be manipulated via drop-down menus, radio buttons, sliders, legends, etc.

Parameters
~~~~~~~~~~

Parameters are the building blocks of interaction in Altair.
There are two types of parameters: *variables* (the :func:`param` function) and *selections* (the :func:`selection` function). We introduce these concepts through a series examples.

.. note::

   This material was changed considerably with the release of Altair 5.  In particular, Altair 4 had selections but not variables, and the term "parameter" first appeared in Altair 5.

.. _basic variable:

Variables: Storing and Reusing Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

In order to use this variable in the chart specification, we explicitly add it to the chart using the :meth:`add_params` method, and we can then reference the variable within the chart specification.  Here we set the opacity using our ``op_var`` parameter.

.. altair-plot::

    op_var = alt.param(value=0.1)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_params(
        op_var
    )

It's reasonable to ask whether all this effort is necessary. Here is a more natural way to accomplish the same thing that avoids the use of both :func:`param` and ``add_params``.

.. altair-plot::

    op_var2 = 0.1

    alt.Chart(cars).mark_circle(opacity=op_var2).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    )

The benefit of using :func:`param` doesn't become apparent until we incorporate an additional component. In the following example we use the ``bind`` property of the parameter, so that the parameter becomes bound to an input element. In this example, that input element is a slider widget.

.. altair-plot::

    slider = alt.binding_range(min=0, max=1, step=0.05, name='opacity:')
    op_var = alt.param(value=0.1, bind=slider)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_params(
        op_var
    )

Now we can dynamically change the opacity of the points in our chart using the slider. You will learn much more about binding parameters to input elements such as widgets in the section :ref:`binding-parameters`.

.. note::

    A noteworthy aspect of Altair's interactivity is that these effects are controlled entirely within the web browser. This means that you can save charts as HTML files and share them with your colleagues who can access the interactivity via their browser without the need to install Python.

Selections: Capturing Inputs to Query Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selection parameters define data queries that are driven by direct manipulation user input (e.g., mouse clicks or drags).
There are two types of selections:
:func:`selection_interval` and :func:`selection_point`.

Here we will create a simple chart and then add an selection interval to it.
We could create a selection interval via ``param(select="interval")``,
but it is more convenient to use the shorter ``selection_interval``
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
function (and interval selection is also referred to as a "brush"):

.. altair-plot::
    :output: none

    brush = alt.selection_interval()

We can now add this selection interval to our chart via ``add_params``:

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
One difference is that here we have not defined how the chart should respond to the selection; you will learn this in the next section.

Conditions & Filters
~~~~~~~~~~~~~~~~~~~~

Conditional Encodings
^^^^^^^^^^^^^^^^^^^^^

The example above is neat, but the selection interval doesn't actually *do* anything yet.
To make the chart respond to this selection, we need to reference the selection in within
the chart specification. Here, we will use the :func:`condition` function to create
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

As you can see, the color of the points now changes depending on whether they are inside or outside the selection.
Above we are using the selection parameter ``brush`` as a *predicate*
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

Filtering Data
^^^^^^^^^^^^^^

Using a selection parameter to filter data works in much the same way
as using it within ``condition``,
For example, in ``transform_filter(brush)``,
we are again using the selection parameter ``brush`` as a predicate.
Data points which evaluate to ``True`` (i.e., data points which lie within the selection) are kept,
and data points which evaluate to ``False`` are filtered out.

It is not possible to both select and filter in the same chart,
so typically this functionality will be used when at least two sub-charts are present.
In the following example,
we attach the selection parameter to the upper chart,
and then filter data in the lower chart based selection in the upper chart.
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

   interval_x = alt.selection_interval(encodings=['x'], empty=False)
   make_example(interval_x)

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
by clicking on them while holding the *shift* key, you can try in the two charts above.

Parameter Composition
~~~~~~~~~~~~~~~~~~~~~

Altair also supports combining multiple parameters using the ``&``, ``|``
and ``~`` for respectively ``AND``, ``OR`` and ``NOT`` logical composition
operands.

In the following example there are two people who can make an interval
selection in the chart. The person Alex makes a selection box when the
alt-key (macOS: option-key) is selected and Morgan can make a selection
box when the shift-key is selected.
We use the ``Brushconfig`` to give the selection box of Morgan a different
style.
Now, we color the rectangles when they fall within Alex's or Morgan's
selection
(note that you need to create both selections before seeing the effect).

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
    color = alt.condition(
        selection,
        alt.Color('Origin:N', legend=None),
        alt.value('lightgray')
    )

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
    color = alt.condition(
        selection,
        alt.Color('Origin:N', legend=None),
        alt.value('lightgray')
    )

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

.. _binding-parameters:

Bindings & Widgets
~~~~~~~~~~~~~~~~~~

With an understanding of the parameter types and conditions, you can now bind parameters to chart elements (e.g. legends) and widgets (e.g. drop-downs and sliders). This is done using the ``bind`` option inside ``param`` and ``selection``. As specified by `the Vega-lite binding docs <https://vega.github.io/vega-lite/docs/bind.html#input-element-binding>`_, bindings can be of three types:
to data-driven and logic-driven input elements,

1. Point and interval selections can be used for data-driven interactive elements, such as highlighting and filtering based on values in the data.
2. Sliders and checkboxes can be used for logic-driven interactive elements, such as highlighting and filtering based on the absolute values in these widgets.
3. Interval selections can be bound to a scale, such as zooming in on a map.

The following table summarizes the input elements that are supported in Vega-Lite:

========================= ===========================================================================  ===============================================
Input Element             Description                                                                   Example
========================= ===========================================================================  ===============================================
:class:`binding_checkbox` Renders as checkboxes allowing for multiple selections of items.                    :ref:`gallery_multiple_interactions`
:class:`binding_radio`    Radio buttons that force only a single selection                                    :ref:`gallery_multiple_interactions`
:class:`binding_select`   Drop down box for selecting a single item from a list                               :ref:`gallery_multiple_interactions`
:class:`binding_range`    Shown as a slider to allow for selection along a scale.                             :ref:`gallery_us_population_over_time`
:class:`binding`          General method that supports many HTML input elements
========================= ===========================================================================  ===============================================

Widgets
^^^^^^^

Widgets are HTML input elements, such as drop-downs, sliders, radio buttons, and search boxes.

Data-Driven Widgets
-------------------

Data-driven widgets use the active value(s) of the widget to look up matching points with matching values in the chart's dataset.
For example, we can establish a binding between an input widget and a point selection to filter the data as in the example below where a drop-down is used to highlight cars from a specific ``Origin``:

.. altair-plot::

    input_dropdown = alt.binding_select(options=['Europe','Japan','USA'], name='Region ')
    selection = alt.selection_point(fields=['Origin'], bind=input_dropdown)
    color = alt.condition(
        selection,
        alt.Color('Origin:N', legend=None),
        alt.value('lightgray')
    )

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
    ).add_params(
        selection
    )

As you can see above,
we are still using ``conditions`` to make the chart respond to the selection,
just as we did without widgets.
Bindings and input elements can also be used to filter data allowing the user to see just the selected points as in the example below.
In this example, we also add an empty selection
to illustrate how you can go back to showing all points
after a selection has been made in a radio button or drop-down 
(since these can't be deselected).


.. altair-plot::

    # Make radio button less cramped by adding a space after each label
    options = ['Europe', 'Japan', 'USA']
    labels = [option + ' ' for option in options]

    input_dropdown = alt.binding_radio(
        # Add the empty selection which shows all when clicked
        options=options + [None],
        labels=labels + ['All'],
        name='Region: '
    )
    selection = alt.selection_point(
        fields=['Origin'],
        bind=input_dropdown,
    )

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        # We need to set a constant domain to preserve the colors
        # when only one region is shown at a time
        color=alt.Color('Origin:N', scale=alt.Scale(domain=options)),
    ).add_params(
        selection
    ).transform_filter(
        selection
    )

Logic-Driven Widgets
--------------------

So far we have seen the use of selections to match and lookup values in our data.
In other cases,
we might want to make a logic comparison directly in the conditional statement,
For example, for a checkbox widget,
we want to check if the state of the checkbox is True or False
and execute some action depending on whether it is checked or not.
When we are using a checkbox as a toggle like this,
we need to use `param` instead of `selection_point`,
since we don't want to check if there are True/False values in our data,
just if the value of the check box is True (checked) or False (unchecked):

.. altair-plot::

    bind_checkbox = alt.binding_checkbox(name='Scale point size by "Acceleration": ')
    param_checkbox = alt.param(bind=bind_checkbox)

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        size=alt.condition(
            param_checkbox,
            alt.Size('Acceleration:Q'),
            alt.value(25)
        )
    ).add_params(
        param_checkbox
    )

Similarly, we might want to create a condition
where we want to access the value of a slider
to use directly in a logic expression,
e.g. compare if it is smaller or larger than the values in the data.
For this workflow it is also recommended to use ``param``,
and as you can see below,
we use the special syntax ``datum.xval``
to reference the column to compare again.
Prefixing the column name with ``datum``
tells Altair that we want to compare to a column in the dataframe,
rather than to a Python variable called ``xval``,
which would have been the case if we just wrote ``xval < selector``.

.. altair-plot::

    import numpy as np
    import pandas as pd


    rand = np.random.RandomState(42)
    df = pd.DataFrame({
        'xval': range(100),
        'yval': rand.randn(100).cumsum()
    })

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

In this particular case we could actually have used a selection
as selection values can be accessed directly and used in expressions that affect the
chart. For example, here we create a slider to choose a cutoff value, and color
points based on whether they are smaller or larger than the value:

.. altair-plot::

    slider = alt.binding_range(min=0, max=100, step=1, name='Cutoff ')
    selector = alt.selection_point(
        name="SelectorName",
        fields=['cutoff'],
        bind=slider,
        value=[{'cutoff': 50}]
    )

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

While it can be useful to know
how to access selection values
in expression strings,
using the parameters syntax introduced in Altair 5
often provides a more convenient syntax
for simple interactions like this one
since they can also be accessed in expression strings
as we saw above.

In addition to the widgets listed in the table above,
Altair has access to `any html widget <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input>`_
via the more general ``binding`` function.
In the example below,
we use a search input to filter points that match the search string exactly.
You can hover over the points to see the car names
and try typing one into the search box, e.g. ``vw pickup``
to see the point highlighted.

.. altair-plot::

    search_input = alt.param(
        value='',
        bind=alt.binding(
            input='search',
            placeholder="Car model",
            name='Search ',
        )
    )
    alt.Chart(data.cars.url).mark_point(size=60).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        tooltip='Name:N',
        opacity=alt.condition(
            alt.datum.Name == search_input,
            # f"datum.Name == {search_input.name}", # Equivalent alternative
            alt.value(0.8),
            alt.value(0.1)
        )
    ).add_params(
        search_input
    )

It is not always useful to require an exact match to the search syntax,and when we will be learning about expressions in the section :ref:`<expressions>`, we will see how we can match partial strings via regexes.


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

Expressions for Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair allows custom interactions by utilizing the expression language of Vega for writing basic formulas. A Vega expression string is a well-defined set of JavaScript-style operations.
To simplify building these expressions in Python, Altair provides the ``expr`` module, which offers constants and functions to construct expressions using Python syntax. Both JavaScript-syntax and Python-syntax are supported within Altair to define an expression,
and you can see an introductory example of each in the :ref:`user-guide-calculate-transform` transform documentation.

In the following example, we define a range connected to a parameter named ``width``. We then assign two expressions via ``param`` using both JavaScript and Python-syntax.
Using these two expressions defined as a parameter, we can connect them to an encoding channel option, such as the title color of the axis. If the width is below ``200``, then the color is ``red``; otherwise, the color is ``blue``.

.. altair-plot::

    bind_range = alt.binding_range(min=100, max=300, name='Slider value:  ')
    param_width = alt.param(bind=bind_range)

    param_color_js_expr = alt.param(expr=f"{param_width.name} < 200 ? 'red' : 'black'")
    param_color_py_expr = alt.param(expr=alt.expr.if_(param_width < 200, 'red', 'black'))

    chart = alt.Chart(df).mark_point().encode(
        x=alt.X('xval').axis(titleColor=param_color_js_expr),
        y=alt.Y('yval').axis(titleColor=param_color_py_expr)
    ).add_params(
        param_width, 
        param_color_js_expr, 
        param_color_py_expr
    )
    chart

In this example, we use a JavaScript-style ternary operator ``f"{param_width.name} < 200 ? 'red' : 'blue'"`` which is equivalent to the Python function ``expr.if_(param_width < 200, 'red', 'blue')``.
The expressions defined as parameters also need to be added to the chart within ``.add_params()`` to be usable within the chart.

Expressions can be included within a chart specification using two approaches. One approach is to assign an expression within a parameter definition, as shown above.
The second approach is to use an inline expression using the ``expr()`` utility function.
Here, we modify the chart above to change the size of the points based on an inline expression. Instead of creating a conditional statement, we use the value of the expression as the size directly and therefore only need to specify the name of the parameter.

.. altair-plot::

    chart.mark_point(size=alt.expr(param_width.name))

Inline expressions defined by ``expr(...)`` are not parameters and, therefore, do not need to be added within the ``add_params``.

Another option to include an expression within a chart specification is as a value definition to an encoding channel. Here, we make the exact same modification to the chart as in the previous example via this alternate approach:

.. altair-plot::

    chart.encode(size=alt.value(alt.expr(param_width.name)))

`Some parameter names have special meaning in Vega-Lite <https://vega.github.io/vega-lite/docs/parameter.html#built-in-variable-parameters>`_, for example, naming a parameter ``width`` will automatically link it to the width of the chart. In the example below, we also modify the chart title to show the value of the parameter:

.. altair-plot::
    bind_range = alt.binding_range(min=100, max=300, name='Chart width: ')
    param_width = alt.param('width', bind=bind_range)
    
    # In Javascript, a number is converted to a string when added to an existing string,
    # which is why we use this nested quotation.
    title=alt.Title(alt.expr(f'"This chart is " + {param_width.name} + " px wide"'))
    alt.Chart(df, title=title).mark_point().encode(
        x=alt.X('xval'),
        y=alt.Y('yval')
    ).add_params(
        param_width,
    )

Now that we know the basics of expressions,
let's see how we can improve on our search input example
and make the search string match via a regex pattern.
To do this we need to use ``expr.regex`` to define the regex string,
and ``expr.test`` to test it against another string
(in this case the string in the ``Name`` column).
The ``i`` option makes the regex case insensitive.
To try this out, you can write ``mazda|ford`` in the search input box.

.. altair-plot::

    search_input = alt.param(
        value='',
        bind=alt.binding(
            input='search',
            placeholder="Car model",
            name='Search ',
        )
    )
    alt.Chart(data.cars.url).mark_point(size=60).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        tooltip='Name:N',
        opacity=alt.condition(
            alt.expr.test(alt.expr.regexp(search_input, 'i'), alt.datum.Name),
            # f"test(regexp({search_input.name}, 'i'), datum.Name)",  # Equivalent js alternative
            alt.value(0.8),
            alt.value(0.1)
        )
    ).add_params(
        search_input
    )

And remember, all this interactivity is client side.
You can save this chart as an HTML file or put it on a static site generator such as GitHub/GitLab pages
and anyone can interact with it without having to install Python.
Quite powerful!

To summarize expressions:

- Altair can utilize the expression language of Vega for writing basic formulas to enable custom interactions.
- Both JavaScript-style syntax and Python-style syntax are supported in Altair to define expressions.
- Altair provides the ``expr`` module which allows expressions to be constructed with Python syntax.
- Expressions can be included within a chart specification using two approaches: through a ``param(expr=...)`` parameter definition or inline using the ``expr(...)`` utility function.
- Expressions can be used anywhere the documentation mentions that an `ExprRef` is an accepted value. This is mainly in three locations within a chart specification: mark properties, encoding channel options, and within a value definition for an encoding channel. They are also supported in the chart title, but not yet for subtitles or guide titles (i.e. axis and legends, see https://github.com/vega/vega-lite/issues/7408 for details).

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
    ).add_params(
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
