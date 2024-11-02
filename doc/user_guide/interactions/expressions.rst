.. currentmodule:: altair

.. _expressions:

Expressions
~~~~~~~~~~~

Altair allows custom interactions by utilizing the `expression language of Vega <https://vega.github.io/vega/docs/expressions/>`_ for writing basic formulas. A Vega expression string is a well-defined set of JavaScript-style operations.
To simplify building these expressions in Python, Altair provides the ``expr`` module, which offers constants and functions to construct expressions using Python syntax. Both JavaScript-syntax and Python-syntax are supported within Altair to define an expression
and an introductory example of each is available in the :ref:`user-guide-calculate-transform` transform documentation so we recommend checking out that page before continuing.

Expressions inside Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following example, we define a range connected to a parameter named ``param_width``. We then assign two expressions via ``param`` using both JavaScript and Python-syntax.
As previously,
we access the parameter values by referencing the parameters by name;
in JavaScript that is done via ``f"{param_width.name}"``
whereas in Python it is sufficient to just type the variable name.
Using these two expressions defined inside parameters, we can connect them to an encoding channel option, such as the title color of the axis. If the width is below ``200``, then the color is ``red``; otherwise, the color is ``blue``.

.. altair-plot::

    import altair as alt
    import numpy as np
    import pandas as pd
    
    rand = np.random.RandomState(42)
    df = pd.DataFrame({
        'xval': range(100),
        'yval': rand.randn(100).cumsum()
    })

    bind_range = alt.binding_range(min=100, max=300, name='Slider value:  ')
    param_width = alt.param(bind=bind_range)

    # Examples of how to write both js and python expressions
    param_color_js_expr = alt.param(expr=f"{param_width.name} < 200 ? 'red' : 'black'")
    param_color_py_expr = alt.param(expr=alt.expr.if_(param_width < 200, 'red', 'black'))

    chart = alt.Chart(df).mark_point().encode(
        alt.X('xval').axis(titleColor=param_color_js_expr),
        alt.Y('yval').axis(titleColor=param_color_py_expr)
    ).add_params(
        param_width,
        param_color_js_expr,
        param_color_py_expr
    )
    chart

In the example above, we used a JavaScript-style ternary operator ``f"{param_width.name} < 200 ? 'red' : 'blue'"`` which is equivalent to the Python function ``expr.if_(param_width < 200, 'red', 'blue')``.
The expressions defined as parameters also needed to be added to the chart within ``.add_params()``.

Inline Expressions
^^^^^^^^^^^^^^^^^^

In addition to assigning an expression within a parameter definition as shown above,
the ``expr()`` utility function allows us to define inline expressions.
Inline expressions are not parameters,
so they can be added directly in the chart spec instead of via ``add_params``,
which is a convenient shorthand for writing out the full parameter code.

In this example, we modify the chart above to change the size of the points based on an inline expression. Instead of creating a conditional statement, we use the value of the expression as the size directly and therefore only need to specify the name of the parameter.

.. altair-plot::

    chart.mark_point(size=alt.expr(param_width.name))

In addition to modifying the ``mark_*`` parameters,
inline expressions can be passed to encoding channels as a value definition.
Here, we make the exact same modification to the chart as in the previous example
via this alternate approach:

.. altair-plot::

    chart.encode(size=alt.value(alt.expr(param_width.name)))

`Some parameter names have special meaning in Vega-Lite <https://vega.github.io/vega-lite/docs/parameter.html#built-in-variable-parameters>`_, for example, naming a parameter ``width`` will automatically link it to the width of the chart.

.. altair-plot::

    bind_range = alt.binding_range(min=100, max=300, name='Chart width: ')
    param_width = alt.param('width', bind=bind_range)

    alt.Chart(df).mark_point().encode(
        alt.X('xval'),
        alt.Y('yval')
    ).add_params(
        param_width
    )

.. _accessing-parameter-values:

Inline Expressions in Titles
----------------------------

An inline expression can be used to
update the chart title to show the current value of the parameter.
Here, we extend the code from the previous example
by using an f-string inside an inline expression.
The additional quotations and plus signs are needed
for the parameter value to be interpreted correctly.

.. altair-plot::

    bind_range = alt.binding_range(min=100, max=300, name='Chart width: ')
    param_width = alt.param('width', bind=bind_range)

    # In Javascript, a number is converted to a string when added to an existing string,
    # which is why we use this nested quotation.
    title=alt.Title(alt.expr(f'"This chart is " + {param_width.name} + " px wide"'))
    alt.Chart(df, title=title).mark_point().encode(
        alt.X('xval'),
        alt.Y('yval')
    ).add_params(
        param_width
    )

In the example above,
we accessed the value of a variable parameter
and inserted it into the chart title.
If we instead want our chart title to reflect the value from a selection parameter,
it is not enough to reference only the name of the parameter.
We also need to reference the field specified by the selection parameter
(i.e. ``Origin`` in the example below):

.. altair-plot::

    from vega_datasets import data
    
    cars = data.cars.url
    input_dropdown = alt.binding_select(options=['Europe', 'Japan', 'USA'], name='Region ')
    selection = alt.selection_point(fields=['Origin'], bind=input_dropdown, value='Europe')

    title = alt.Title(alt.expr(f'"Cars from " + {selection.name}.Origin'))

    alt.Chart(cars, title=title).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
    ).add_params(
        selection
    ).transform_filter(
        selection
    )


A Regex Search Widget
---------------------

Now that we know the basics of expressions,
let's see how we can improve on our search input example
to make the search string match via a regex pattern.
To do this we need to use ``expr.regex`` to define the regex string,
and ``expr.test`` to test it against another string
(in this case the string in the ``Name`` column).
The ``i`` option makes the regex case insensitive,
and you can see that we have switched to using ``param`` instead of ``selection_point``
since we are doing something more complex
than looking up values with an exact match in the data.
To try this out, you can type ``mazda|ford`` in the search input box below.

.. altair-plot::

    search_input = alt.param(
        value='',
        bind=alt.binding(
            input='search',
            placeholder="Car model",
            name='Search ',
        )
    )
    search_matches = alt.expr.test(alt.expr.regexp(search_input, "i"), alt.datum.Name)

    alt.Chart(cars).mark_point(size=60).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        tooltip='Name:N',
        opacity=alt.when(search_matches).then(alt.value(1)).otherwise(alt.value(0.05)),
    ).add_params(search_input)

And remember, all this interactivity is client side.
You can save this chart as an HTML file or put it on a static site generator such as GitHub/GitLab pages
and anyone can interact with it without having to install Python.
Quite powerful!

Summary of Expressions
^^^^^^^^^^^^^^^^^^^^^^

- Altair can utilize the expression language of Vega for writing basic formulas to enable custom interactions.
- Both JavaScript-style syntax and Python-style syntax are supported in Altair to define expressions.
- Altair provides the ``expr`` module which allows expressions to be constructed with Python syntax.
- Expressions can be included within a chart specification using two approaches: through a ``param(expr=...)`` parameter definition or inline using the ``expr(...)`` utility function.
- Expressions can be used anywhere the documentation mentions that an `ExprRef` is an accepted value. This is mainly in three locations within a chart specification: mark properties, encoding channel options, and within a value definition for an encoding channel. They are also supported in the chart title, but not yet for subtitles or guide titles (i.e. axis and legends, see https://github.com/vega/vega-lite/issues/7408 for details).
