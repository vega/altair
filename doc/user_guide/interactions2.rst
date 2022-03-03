.. currentmodule:: altair

.. _user-guide-interactions2:

Parameters: Variables and Selections
====================================

Interactivity in Altair is built around *parameters*, of which there are two types: variables and selections.  We introduce these concepts through a series examples.

.. note::

   This material was changed considerably with the release of Altair 5.  In particular, Altair 4 had selections but not variables, and the term ``parameter`` first appeared in Altair 5.

.. _basic variable:

Basic Example: Using a variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

We can create a variable parameter using :func:`parameter`, and assign that parameter a default value of 0.1 using the ``value`` property, as follows:

.. altair-plot::
    :output: none

    op_var = alt.parameter(value=0.1)

In order to use this variable in the chart specification, we explicitly add it to the chart using the :meth:`Chart.add_parameter` method, and we can then reference the variable within the chart specification.  Here we set the opacity using our ``op_var`` parameter.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    op_var = alt.parameter(value=0.1)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_parameter(
        op_var
    )

It's reasonable to ask whether all this effort is necessary.  Here is a more natural way to accomplish the same thing.  We avoid the use of both :func:`alt.parameter` and ``add_parameter``.

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

The benefit of using :func:`alt.parameter` doesn't become apparent until we incorporate an additional component, such as in the following, where we use the ``bind`` property of the parameter, so that the parameter becomes bound to an input element.  In this example, that input element is a slider widget.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    slider = alt.binding_range(min=0, max=1, step=0.05, name='opacity:')
    op_var = alt.parameter(value=0.1, bind=slider)

    alt.Chart(cars).mark_circle(opacity=op_var).encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_parameter(
        op_var
    )

Now we can dynamically change the opacity of the points in our chart using the slider.  A noteworthy aspect of this chart is that these effects are controlled entirely within your web browser.  Once the Vega-Lite chart specification has been created by Altair, the result is an interactive chart, and that interactivity no longer requires a running Python environment.

The above example includes some aspects which occur frequently when creating interactive charts in Altair:

- Creating a variable parameter using :func:`parameter`.
- Attaching the parameter to a chart using the :meth:`Chart.add_parameter` method.
- Binding the parameter to an input widget using the parameter's ``bind`` property.  (In the above example, the input widget is a slider widget.)

Some further aspects that we will see below include:

- Creating a *selection* parameter.
- Using a parameter within a :func:`condition`.
- Using a parameter within a :meth:`Chart.transform_filter`.

Using selection parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

The basic syntax for adding a selection parameter to a chart is similar to the syntax for a variable parameter.  Instead of creating the parameter using ``alt.parameter``, we will typically use ``alt.selection_interval`` or ``alt.selection_point``.  Here is a basic example, again using the ``cars`` dataset:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    brush = alt.selection_interval()

    alt.Chart(cars).mark_circle().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color='Origin:N'
    ).add_parameter(
        brush
    )

    
If you click and drag on the above chart, you will see that the corresponding region gets highlighted.

So far this example is very similar to what we did in the :ref:`variable example <basic variable>`.  Here we have done two things: we created a selection parameter using ``brush = alt.selection_interval()``, and we attached that parameter to the chart using ``add_parameter``.

The line ``brush = alt.selection_interval()`` is equivalent to ``brush = alt.parameter(select="interval")``; we will typically use the ``selection_interval`` version, because it is shorter and because it matches the syntax that was used in Altair 4.

Typically selection parameters will be used in conjunction with ``condition`` or with ``transform_filter``.  Here are some possibilities.

Using a selection within a condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following example, we are using the selection parameter ``brush`` as a *predicate* (something that evaluates as `True` or `False`).  This is controlled by the line ``color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))``.  Data points which fall within the selection evaluate as ``True``, and data points which fall outside the selection evaluate to ``False``.  The ``'Origin:N'`` specifies how to color the points which fall within the selection, and the ``alt.value('lightgray')`` specifies that the outside points should be given a constant color value.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    brush = alt.selection_interval()

    alt.Chart(cars).mark_circle().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).add_parameter(
        brush
    )

Using a selection to filter the data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you are comfortable with using a parameter within ``alt.condition``, using a parameter within ``transform_filter`` works in much the same way.  For example, in ``transform_filter(brush)``, we are again using the selection parameter ``brush`` as a predicate.  Data points which evaluate to ``True`` (i.e., data points which lie within the selection) are kept, and data points which evaluate to ``False`` are removed.  

It is not possible to both select and filter in the same chart, so typically this functionality will be used when at least two sub-charts are present.  In the following example, we attach the selection parameter to the left chart, and then filter data using the selection parameter on the right chart.  We specify explicit domains for the right chart so that the positions of the points remain steady.

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    brush = alt.selection_interval()

    c1 = alt.Chart(cars).mark_point().encode(
        x = "Horsepower:Q",
        y = "Miles_per_Gallon:Q"
    ).add_parameter(brush)

    c2 = alt.Chart(cars).mark_point().encode(
        x = alt.X("Acceleration:Q", scale=alt.Scale(domain=[0,25])),
        y = alt.Y("Displacement:Q", scale=alt.Scale(domain=[0,500])),
    ).transform_filter(brush)

    alt.vconcat(c1,c2)


Limitations
^^^^^^^^^^^

Some possible use cases for the above interactivity are not currently supported by Vega-Lite, and hence are not currently supported by Altair.  Here are some examples.

1.  If we are using a ``selection_point``, it would be natural to want to return information about the chosen data point, and then process that information using Python.  This is not currently possible (and as of December 2021 it does not seem likely to become possible any time soon), so any data processing will have to be handled using tools such as ``transform_calculate``, etc.

2.  It is not possible to use an encoding such as ``y=column_variable`` to then dynamically display different charts based on different column choices.  Similar functionality could be created using for example ``ipywidgets``, but the resulting interactivity would be controlled by Python, and would not work for example as a stand-alone web page.  The underlying reason this is not possible is that in Vega-Lite, the ``field`` property does not accept a parameter as value; see the `field Vega-Lite documentation <https://vega.github.io/vega-lite/docs/field.html>`_.  A first approximation of a workaround is given in the following example.

.. altair-plot::
    import pandas as pd
    import altair as alt

    df = pd.DataFrame({'col0':range(4), 'col1':list('ABAA'), 'col2':list('CDDC')})
    df_long = df.melt(id_vars=['col0'], var_name='column')

    col_dropdown = alt.binding_select(options=df_long['column'].unique())
    col_param = alt.parameter(bind=col_dropdown, name="ColumnParam", value='col1')

    alt.Chart(df_long).mark_bar().encode(
        x = "value:N",
        y = "count()",
    ).transform_filter(
        "datum.column == ColumnParam"
    ).add_parameter(
        col_param
    )