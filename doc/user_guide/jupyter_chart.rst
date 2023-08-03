.. _user-guide-jupyterchart:

JupyterChart
============
The ``JupyterChart`` class, introduced in Vega-Altair 5.1, makes it possible to update charts
after they have been displayed and access the state of :ref:`user-guide-interactions` from Python.

Supported Environments
----------------------
``JupyterChart`` is a `Jupyter Widget <https://ipywidgets.readthedocs.io/en/latest/>`_ built
on the `AnyWidget <https://anywidget.dev/>`_ library. As such, it's compatible with development
environments and dashboard toolkits that support third party Jupyter Widgets.
Tested environments include:

* Classic Jupyter Notebook
* JupyterLab
* Visual Studio Code
* Google Colab
* Voila

.. note::
    If you try ``JupyterChart`` in another environment that supports Jupyter Widgets,
    `let us know how it goes <https://github.com/altair-viz/altair/issues>`_ so that we can keep
    this list up to date.

Basic Usage
-----------
To create a ``JupyterChart``, pass a regular ``Chart`` instance to the ``alt.JupyterChart``
constructor. The chart will be displayed automatically if the last expression in a notebook
cell evaluates to a ``JupyterChart`` instance. For example:

.. code-block:: python

    import altair as alt
    import pandas as pd

    source = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })

    chart = alt.Chart(source).mark_bar().encode(
        x='a',
        y='b'
    )

    jchart = alt.JupyterChart(chart)
    jchart

.. image:: https://github.com/altair-viz/altair/assets/15064365/59cb2484-ad51-461a-8353-e1d4fa5f6bb6
  :alt: Bar chart with letters A through I on the x-axis


Updating Charts
---------------
The ``JupyterChart``'s ``chart`` property can be assigned to a new chart instance, and the new chart
will immediately be displayed in place of the old one.

.. code-block:: python

    jchart.chart = chart.mark_bar(color="crimson", cornerRadius=10)

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/21d580ef-4dec-4687-a765-9b6d6d84c61f">
      Your browser does not support the video tag.
    </video>

Params: Variables and Selections
--------------------------------
As described in :ref:`user-guide-interactions`, Vega-Altair's rich grammar of interactivity
is built on the concept of parameters. In particular, variable parameters (which store a
simple value) and selection parameters (which map user interactions to data queries).

The ``JupyterChart`` class makes both variable and selection parameters available for use
in Python.

Variable Params
---------------
JupyterChart makes it possible to access, observe, set, and link variable parameters.

Accessing Variable Params
~~~~~~~~~~~~~~~~~~~~~~~~~
A chart's variable parameters are stored in the ``params`` property of the ``JupyterChart``
instance. The values of individual named variable parameters may be accessed using
regular attribute access. Here is an example that uses :ref:`binding-parameters` to bind a
variable parameter named ``cutoff`` to a slider. The current value of the ``cutoff`` variable
is available as ``jchart.params.cutoff``.

.. code-block:: python

    import altair as alt
    import pandas as pd
    import numpy as np

    rand = np.random.RandomState(42)

    df = pd.DataFrame({
        'xval': range(100),
        'yval': rand.randn(100).cumsum()
    })

    slider = alt.binding_range(min=0, max=100, step=1)
    cutoff = alt.param(name="cutoff", bind=slider, value=50)

    chart = alt.Chart(df).mark_point().encode(
        x='xval',
        y='yval',
        color=alt.condition(
            alt.datum.xval < cutoff,
            alt.value('red'), alt.value('blue')
        )
    ).add_params(
        cutoff
    )
    jchart = alt.JupyterChart(chart)
    jchart


.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/0f979ed9-ff70-4198-bd83-f94e5f3e07e2">
      Your browser does not support the video tag.
    </video>


Observing Variable Params
~~~~~~~~~~~~~~~~~~~~~~~~~

The `observe <https://ipywidgets.readthedocs.io/en/8.1.0/examples/Widget%20Events.html#traitlet-events>`_
method on the ``params`` property may be used to register a callback that will be invoked when a
parameter changes. In this example, a simple callback function is registered to print the value of
the ``cutoff`` parameter.

.. code-block:: python

    def on_cutoff_change(change):
        print(change.new)

    jchart.params.observe(on_cutoff_change, ["cutoff"])

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/0d3787e8-984e-474a-923f-19c7a603bdef">
      Your browser does not support the video tag.
    </video>

Setting Variable Params
~~~~~~~~~~~~~~~~~~~~~~~
The value of variable parameters may be updated from Python by assigning to the corresponding ``params``
attribute. Here's an example of updating the ``cutoff`` variable parameter by assigning to ``jchart.params.cutoff``.

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/94ee9188-d582-4f51-aa30-1aaa11d6ed34">
      Your browser does not support the video tag.
    </video>


Linking Variable Params
~~~~~~~~~~~~~~~~~~~~~~~
Because ``params`` is a traitlet object, it's possible to use the ipywidgets
`link function <https://ipywidgets.readthedocs.io/en/8.1.0/examples/Widget%20Events.html#linking-widgets>`_
to bind params to other ipywidgets. Here is an example of linking the ``cutoff`` variable parameter
to the value of an ipywidgets ``IntSlider``.

.. code-block:: python

    from ipywidgets import IntSlider, link
    slider = IntSlider(23, min=0, max=100)
    link((slider, "value"), (jchart.params, "cutoff"))
    slider

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/b63549fb-6d19-4d38-862d-cb578b4327b3">
      Your browser does not support the video tag.
    </video>

If an ipywidget is linked to a Vega-Altair variable param, it's not necessary to also bind
the param to a Vega-Altair widget. Here, the example above is updated to control the ``cutoff``
variable's value only from the ``IntSlider`` ipywidget.

.. code-block:: python

    import pandas as pd
    import numpy as np

    rand = np.random.RandomState(42)

    df = pd.DataFrame({
        'xval': range(100),
        'yval': rand.randn(100).cumsum()
    })

    cutoff = alt.param(name="cutoff", value=50)

    chart = alt.Chart(df).mark_point().encode(
        x='xval',
        y='yval',
        color=alt.condition(
            alt.datum.xval < cutoff,
            alt.value('red'), alt.value('blue')
        )
    ).add_params(
        cutoff
    )
    jchart = alt.JupyterChart(chart)
    jchart


.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/b8f70490-6a0b-4032-8ef8-95a21004b7ed">
      Your browser does not support the video tag.
    </video>


Selection Params
----------------
JupyterChart makes it possible to access and observe selection parameters. For the purpose of accessing
selections from Python, selection parameters are divided into three types:
Point selections, index selections, and interval selection. These selection types are
represented by Python classes named ``PointSelection``, ``IndexSelection``, and ``IntervalSelection``
respectively.

Instances of these selection classes are available as properties of the JupyterChart's
``selections`` property.

Point Selections
~~~~~~~~~~~~~~~~
The ``PointSelection`` class is used to store the current state of a Vega-Altair point selection
(as created by ``alt.selection_point()``) when either a ``fields`` or ``encodings`` specification
is provided. One common example is a point selection with ``encodings=["color"]`` that is bound to
the legend.

.. code-block:: python

    import altair as alt
    from vega_datasets import data

    source = data.cars()
    brush = alt.selection_point(name="point", encodings=["color"], bind="legend")

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('grey')),
    ).add_params(brush)

    jchart = alt.JupyterChart(chart)
    jchart

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/9a48c9d7-ed84-4405-9125-8da58238f03b">
      Your browser does not support the video tag.
    </video>

The ``PointSelection`` instance may be accessed as ``jchart.selections.point`` (Where "point" is the
value of the ``name`` argument to ``alt.selection_point``).

The ``jchart.selections.point.value`` property contains a list of dictionaries where each element
represents a single point in the selection.

Index Selections
~~~~~~~~~~~~~~~~
The ``IndexSelection`` class is used to store the current state of a Vega-Altair point selection
(as created by ``alt.selection_point()``) when neither a ``fields`` nor ``encodings`` specification
is provided.  In this case, the ``value`` property of the selection is a list of the indices
of the selected rows. These indices can be used with the pandas DataFrame's ``iloc`` attribute to
extract the selected rows in the input DataFrame.

.. code-block:: python

    import altair as alt
    from vega_datasets import data

    source = data.cars()
    brush = alt.selection_point(name="point")

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('grey')),
    ).add_params(brush)

    widget = alt.ChartWidget(chart)
    widget

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/2960fc28-885e-40a4-8bd5-9e4b56616afe">
      Your browser does not support the video tag.
    </video>


.. warning::
    The indices returned will only correspond to the input DataFrame for charts that do not include
    aggregations. If a chart includes aggregations, then the ``alt.selection_point`` specification
    should include either a ``fields`` or ``encodings`` argument, which will result in the
    ``JupyterChart`` containing a ``PointSelection`` rather than an ``IndexSelection``.


Interval Selections
~~~~~~~~~~~~~~~~~~~
The ``IntervalSelection`` class is used to store the current state of a Vega-Altair interval selection
(as created by ``alt.selection_interval()``). In this case, the ``value`` property of the selection
is a dictionary from column names to selection intervals

.. code-block:: python

    import altair as alt
    from vega_datasets import data

    source = data.cars()
    brush = alt.selection_interval(name="interval")

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Cylinders:O', alt.value('grey')),
    ).add_params(brush)

    jchart = alt.JupyterChart(chart)
    jchart


.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/8b1b6ea6-6d9d-4a53-aac9-3e120609d99d">
      Your browser does not support the video tag.
    </video>


Observing Selections
~~~~~~~~~~~~~~~~~~~~
As with variable parameters, it's possible to register a callback function to be invoked
when a selection changes by using the ``observe`` method on the ``selections`` property.
Here is an example that listens for changes to an interval selection, then uses the selection
value to filter the input DataFrame and display it's HTML representation. An ipywidgets ``VBox``
is used to combine the chart and HTML table in a column layout.

.. code-block:: python

    import ipywidgets
    from IPython.display import display
    from ipywidgets import HTML, VBox

    import altair as alt
    from vega_datasets import data

    source = data.cars()
    brush = alt.selection_interval(name="brush")

    chart_widget = alt.JupyterChart(alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Cylinders:O', alt.value('grey')),
    ).add_params(brush))

    table_widget = HTML(value=source.iloc[:0].to_html())

    def on_select(change):
        sel = change.new.value
        if sel is None or 'Horsepower' not in sel:
            filtered = source.iloc[:0]
        else:
            filtered = source.query(
                f"{sel['Horsepower'][0]} <= `Horsepower` <= {sel['Horsepower'][1]} & "
                f"{sel['Miles_per_Gallon'][0]} <= `Miles_per_Gallon` <= {sel['Miles_per_Gallon'][1]}"
            )
        table_widget.value = filtered.to_html()

    chart_widget.selections.observe(on_select, ["brush"])

    VBox([chart_widget, table_widget])

.. raw:: html

    <video controls>
      <source src="https://github.com/altair-viz/altair/assets/15064365/1414ed59-8782-4c2e-8dd3-905d2f85fa7e">
      Your browser does not support the video tag.
    </video>

Limitations
-----------

Internet Connection Required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The JupyterChart class currently loads its JavaScript dependencies dynamically from a CDN location.
This keeps the ``altair`` package small, but it means that an internet connection is required
to display JupyterChart instances. In the future, we would like to provide optional offline support.

