.. currentmodule:: altair

.. _binding-parameters:

Bindings & Widgets
~~~~~~~~~~~~~~~~~~

With an understanding of the parameter types and conditions, you can now bind parameters to chart elements (e.g. legends) and widgets (e.g. drop-downs and sliders). This is done using the ``bind`` option inside ``param`` and ``selection``. As specified by `the Vega-lite binding docs <https://vega.github.io/vega-lite/docs/bind.html#input-element-binding>`_, there are three types of bindings available:

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

Widget Binding
^^^^^^^^^^^^^^

Widgets are HTML input elements, such as drop-downs, sliders, radio buttons, and search boxes.
There are a three strategies for how variable and selection parameters
can be used together with widgets:
data-driven lookups, data-driven comparisons, and logic-driven comparisons.

Data-Driven Lookups
-------------------

Data-driven lookups use the active value(s) of the widget
together with a ``selection`` parameter
to look up points with matching values in the chart's dataset.
For example,
we can establish a binding between an input widget and a point selection
to filter the data as in the example below
where a drop-down is used to highlight cars of a specific ``Origin``:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    input_dropdown = alt.binding_select(options=['Europe', 'Japan', 'USA'], name='Region ')
    selection = alt.selection_point(fields=['Origin'], bind=input_dropdown)
    color = (
        alt.when(selection)
        .then(alt.Color("Origin:N").legend(None))
        .otherwise(alt.value("lightgray"))
    )

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=color,
    ).add_params(
        selection
    )

Note that although it looks like a value is selected in the dropdown from the start,
we need to set `value=` to actually start out with an initial selection in the chart.
We did this previously with variable parameters
and selection parameters follow the same pattern as you will see further down
in the :ref:`encoding-channel-binding` section.

As you can see above,
we are still using :ref:`conditions <conditions>` to make the chart respond to the selection,
just as we did without widgets.
Bindings and input elements can also be used to filter data
allowing the user to see just the selected points as in the example below.
In this example, we also add an empty selection
to illustrate how to revert to showing all points
after a selection has been made in a radio button or drop-down
(which cannot be deselected).


.. altair-plot::

    # Make radio button less cramped by adding a space after each label
    # The spacing will only show up in your IDE, not on this doc page
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
        color=alt.Color('Origin:N').scale(domain=options),
    ).add_params(
        selection
    ).transform_filter(
        selection
    )

In addition to the widgets listed in the table above,
Altair has access to `any html widget <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input>`_
via the more general ``binding`` function.
In the example below,
we use a search input to filter points that match the search string exactly.
You can hover over the points to see the car names
and try typing one into the search box, e.g. ``vw pickup``
to see the point highlighted
(you need to type out the full name).

.. altair-plot::

    search_input = alt.selection_point(
        fields=['Name'],
        empty=False,  # Start with no points selected
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
        opacity=alt.when(search_input).then(alt.value(1)).otherwise(alt.value(0.05)),
    ).add_params(
        search_input
    )

It is not always useful to require an exact match to the search syntax,
and when we will be learning about :ref:`expressions`,
we will see how we can match partial strings via a regex instead.

Data-Driven Comparisons
-----------------------

So far we have seen the use of selections
to lookup points with precisely matching values in our data.
This is often useful,
but sometimes we might want to make a more complex comparison
than an exact match.
For example,
we might want to create a condition
we select the points in the data that are above or below a threshold value,
which is specified via a slider.
For this workflow it is recommended to use variable parameters via ``param``
and as you can see below,
we use the special syntax ``datum.xval``
to reference the column to compare against.
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
    predicate = alt.datum.xval < selector

    alt.Chart(df).mark_point().encode(
       x='xval',
       y='yval',
       color=alt.when(predicate).then(alt.value("red")).otherwise(alt.value("blue")),
    ).add_params(
       selector
    )

In this particular case we could actually have used a selection parameter
since selection values can be accessed directly and used in expressions that affect the
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
    predicate = alt.datum.xval < selector.cutoff

    alt.Chart(df).mark_point().encode(
        x='xval',
        y='yval',
        color=alt.when(predicate).then(alt.value("red")).otherwise(alt.value("blue")),
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
Similarly,
it is often possible to use equality statements
such as ``alt.datum.xval == selector`` to lookup exact values
but it is often more convenient to switch to a selection parameter
and specify a field/encoding.

Logic-Driven Comparisons
------------------------

A logic comparison is a type of comparison
that is based on logical rules and conditions,
rather than on the actual data values themselves.
For example, for a checkbox widget
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
        size=alt.when(param_checkbox).then("Acceleration:Q").otherwise(alt.value(25)),
    ).add_params(
        param_checkbox
    )

Another example of creating a widget binding that is independent of the data,
involves an interesting use case for the more general ``binding`` function.
In the next example,
this function introduces a color picker
where the user can choose the colors of the chart interactively:

.. altair-plot::

    color_usa = alt.param(value="#317bb4", bind=alt.binding(input='color', name='USA '))
    color_europe = alt.param(value="#ffb54d", bind=alt.binding(input='color', name='Europe '))
    color_japan = alt.param(value="#adadad", bind=alt.binding(input='color', name='Japan '))

    alt.Chart(data.cars.url).mark_circle().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.Color(
            'Origin:N',
            scale=alt.Scale(
                domain=['USA', 'Europe', 'Japan'],
                range=[color_usa, color_europe, color_japan]
            )
        )
    ).add_params(
        color_usa, color_europe, color_japan
    )

.. _legend-binding:

Legend Binding
^^^^^^^^^^^^^^

An interactive legend can often be helpful to assist in focusing in on groups of data.
Instead of manually having to build a separate chart to use as a legend,
Altair provides the ``bind='legend'`` option to facilitate the creation of clickable legends:

.. altair-plot::

    selection = alt.selection_point(fields=['Origin'], bind='legend')

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        opacity=alt.when(selection).then(alt.value(0.8)).otherwise(alt.value(0.2)),
    ).add_params(
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
    ).add_params(
        selection
    )

Because this is such a common pattern,
Altair provides the :meth:`interactive` method
which creates a scale-bound selection more concisely:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    ).interactive()

.. _encoding-channel-binding:

Encoding Channel Binding
^^^^^^^^^^^^^^^^^^^^^^^^

To update which columns are displayed in a chart
based on the selection in a widget,
we would need to bind the widget to an encoding channel.
In contrast to legend and scale bindings,
it is not possible to setup a binding to an encoding channel
in the selection initialization
(e.g. by typing ``bind='x'``).
Instead,
parameters can be used to pass the value of a selection
to an encoding channel.
This gives more flexibility,
but requires the use of a separate calculation transform
(as in the example below)
until https://github.com/vega/vega-lite/issues/7365 is resolved.

In this example,
we access the parameter value by referencing the parameter by name.
By indexing the data with the parameter value (via ``datum[]``)
we can extract the data column that matches the selected value of the parameter,
and populate the x-channel with the values from this data column.

.. altair-plot::

    dropdown = alt.binding_select(
        options=['Horsepower', 'Displacement', 'Weight_in_lbs', 'Acceleration'],
        name='X-axis column '
    )
    xcol_param = alt.param(
        value='Horsepower',
        bind=dropdown
    )

    alt.Chart(data.cars.url).mark_circle().encode(
        x=alt.X('x:Q').title(''),
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).transform_calculate(
        x=f'datum[{xcol_param.name}]'
    ).add_params(
        xcol_param
    )

Using parameters inside calculate transforms allows us to define dynamic computations
(e.g. subtracting different pairs of columns),
as you can see in the :ref:`gallery_interactive_column_selection` gallery example.
In that example,
the chart title is also dynamically updated using a parameter inside an expression
which is described in more detail in :ref:`accessing-parameter-values`.
Note that it is currently not possible to change the axis titles dynamically based on the selected parameter value,
but a text mark could be used instead
(as in `this SO answer <https://stackoverflow.com/questions/71210072/can-i-turn-altair-axis-titles-into-links>`_),
until https://github.com/vega/vega-lite/issues/7264 is resolved.
