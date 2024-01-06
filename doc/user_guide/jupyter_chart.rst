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

.. image:: /_static/jupyter_chart/simple_bar.svg
  :alt: Bar chart with letters A through I on the x-axis


Updating Charts
---------------
The ``JupyterChart``'s ``chart`` property can be assigned to a new chart instance, and the new chart
will immediately be displayed in place of the old one.

.. code-block:: python

    jchart.chart = chart.mark_bar(color="crimson", cornerRadius=10)

.. raw:: html

    <video controls>
      <source src="/_static/jupyter_chart/updating_charts.mov">
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
      <source src="/_static/jupyter_chart/accessing_variable_params.mov">
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
      <source src="/_static/jupyter_chart/observing_variable_params.mov">
      Your browser does not support the video tag.
    </video>

Setting Variable Params
~~~~~~~~~~~~~~~~~~~~~~~
The value of variable parameters may be updated from Python by assigning to the corresponding ``params``
attribute. Here's an example of updating the ``cutoff`` variable parameter by assigning to ``jchart.params.cutoff``.

.. raw:: html

    <video controls>
      <source src="/_static/jupyter_chart/setting_variable_params.mov">
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
      <source src="/_static/jupyter_chart/linking_variable_params.mov">
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
      <source src="/_static/jupyter_chart/linking_variable_params2.mov">
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
      <source src="/_static/jupyter_chart/point_selection_param.mov">
      Your browser does not support the video tag.
    </video>

The ``PointSelection`` instance may be accessed as ``jchart.selections.point`` (Where "point" is the
value of the ``name`` argument to ``alt.selection_point``).

The ``jchart.selections.point.value`` property contains a list of dictionaries where each element
represents a single point in the selection. This list of dictionaries may be converted into a pandas
`query <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html>`_ string as follows

.. code-block:: python

    filter = " or ".join([
        " and ".join([
            f"`{col}` == {repr(val)}" for col, val in sel.items()
        ])
        for sel in jchart.selections.point.value
    ])
    source.query(filter)

For example, when the Japan and Europe legend entries are selected, the ``filter`` string above will
evaluate to ``"`Origin` == 'Japan' or `Origin` == 'Europe'"``, and the ``source.query(filter)`` expression
will evaluate to a pandas ``DataFrame`` containing the rows of ``source`` that are in the selection.

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

    jchart = alt.JupyterChart(chart)
    jchart

.. raw:: html

    <video controls>
      <source src="/_static/jupyter_chart/index_selection_param.mov">
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
      <source src="/_static/jupyter_chart/interval_selection_param.mov">
      Your browser does not support the video tag.
    </video>

The selection dictionary may be converted into a pandas
`query <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html>`_ string as follows

.. code-block:: python

    filter = " and ".join([
        f"{v[0]} <= `{k}` <= {v[1]}"
        for k, v in jchart.selections.interval.value.items()
    ])
    source.query(filter)


For example, when the x-selection is from 120 to 160 and the y-selection is from 25 to 35,
``jchart.selections.interval.value`` will be ``{'Horsepower': [120, 160], 'Miles_per_Gallon': [25, 30]}``,
the ``filter`` string will be ``"120 <= `Horsepower` <= 160 and 25 <= `Miles_per_Gallon` <= 35"``, and the
``source.query(filter)`` expression will evaluate to a pandas ``DataFrame`` that contains the rows of
``source`` that are in the selection.

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
            filter_query = (
                f"{sel['Horsepower'][0]} <= `Horsepower` <= {sel['Horsepower'][1]} and "
                f"{sel['Miles_per_Gallon'][0]} <= `Miles_per_Gallon` <= {sel['Miles_per_Gallon'][1]}"
            )
            filtered = source.query(filter_query)

        table_widget.value = filtered.to_html()

    chart_widget.selections.observe(on_select, ["brush"])

    VBox([chart_widget, table_widget])

.. raw:: html

    <video controls>
      <source src="/_static/jupyter_chart/linking_interval_selection.mov">
      Your browser does not support the video tag.
    </video>

.. _user-guide-jupyterchart-offline:

Offline Usage
-------------
By default, the ``JupyterChart`` widget loads its JavaScript dependencies dynamically from a CDN
location, which requires an active internet connection. Starting in Altair 5.3, JupyterChart supports
loading its JavaScript dependencies from the ``vl-convert-python`` package, which enables offline usage.

Offline mode is enabled using the ``JupyterChart.enable_offline`` class method.

.. code-block:: python

    import altair as alt
    alt.JupyterChart.enable_offline()

This only needs to be called once, after which all displayed JupyterCharts will operate in offline mode.

Offline mode can be disabled by passing ``offline=False`` to this same method.

.. code-block:: python

    import altair as alt
    alt.JupyterChart.enable_offline(offline=False)

Limitations
-----------

Setting Selections
~~~~~~~~~~~~~~~~~~
It's not currently possible to set selection states from Python.
