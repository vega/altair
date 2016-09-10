.. _basic-tutorial:

Getting Started with Altair
===========================

.. currentmodule:: altair

This tutorial will guide you through the basic process of creating
visualizations in Altair.
First, you will need to make sure you have the Altair package and its
dependencies installed (see :ref:`Installation`)
and make sure you understand how altair
plots are displayed (see :ref:`displaying-plots`).
This tutorial will assume you are working within the Jupyter Notebook,
so that plots are automatically rendered.

In short, perhaps the easiest way to get started is to run

.. code-block:: bash

    $ conda install altair --channel conda-forge
    $ jupyter notebook

and then follow along with this tutorial in the notebook.

Here is the outline of this basic tutorial:

- :ref:`basic-tutorial-data`
- :ref:`basic-tutorial-encodings-and-marks`
- :ref:`basic-tutorial-aggregation`
- :ref:`basic-tutorial-customization`
- :ref:`basic-tutorial-publishing`

.. _basic-tutorial-data:

The Data
--------
Data in Altair is built around the Pandas Dataframe. For the purposes of
this tutorial, we'll start by importing Pandas and creating a simple
DataFrame to visualize, with a categorical variable in column a and a
numerical variable in column b:

.. code-block:: python

    import pandas as pd
    data = pd.DataFrame({'a': list('CCCDDDEEE'),
                         'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})

.. testsetup:: *

    from altair import *
    import pandas as pd
    data = pd.DataFrame({'a': list('CCCDDDEEE'),
                         'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})

.. altair-plot-setup::

    from altair import *
    import pandas as pd
    data = pd.DataFrame({'a': list('CCCDDDEEE'),
                         'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})



When using Altair, datasets are most commonly provided as a Dataframe.
As we will see, the labeled columns of the dataframe are an essential
piece of plotting with Altair.

.. _basic-tutorial-chart-object:

The Chart Object
----------------
The fundamental object in Altair is the :class:`Chart`, which takes a
dataframe as a single argument:

.. testcode::

    from altair import Chart
    chart = Chart(data)

So far, we have defined the Chart object, but we have not yet told the chart
to *do* anything with the data. That will come next.

.. _basic-tutorial-encodings-and-marks:

Encodings and Marks
-------------------
With this chart object in hand, we can now specify how we would like the
data to be visualized. This is done via the ``mark`` attribute of the chart
object, which is most conveniently accessed via the ``Chart.mark_*`` methods.
For example, we can show the data as a point using :meth:`~Chart.mark_point`:


.. altair-plot::

    Chart(data).mark_point()

Here the rendering consists of one point per row in the dataset, all plotted
on top of each other since we have not yet specified the point's position.

To visually separate the points, we can map various *encoding channels*, or
*channels* for short, to columns in the dataset.
For example, we could *encode* the variable ``a`` of the data with the
``x`` channel, which represents the x-axis position of the points.
This can be done straightforwardly via the :meth:`Chart.encode` method:

.. altair-plot::

    Chart(data).mark_point().encode(
        x='a',
    )


The ``encode()`` method builds a key-value mapping between encoding channels
(such as ``x``, ``y``, ``color``, ``shape``, ``size``, etc.) to columns in
the dataset, accessed by column name.
By default, Altair automatically determines the appropriate data type for
the mapped column, which in this case is a *nominal* value, or an unordered
categorical (see :ref:`data-types` for more information).

Though we've now separated the data by one attribute, we still have multiple
points overlapping within each category. Let's further separate these by
adding a ``y`` encoding channel, mapped to the ``"b"`` column:

.. altair-plot::

    Chart(data).mark_point().encode(
        x='a',
        y='b'
    )

The type of the data in the ``"b"`` column is again automatically-inferred
by altair, and this time is treated as a *quantitative* type (i.e. real-value).
Additionally, we see that grid lines and appropriate axis titles are
automatically added as well.

For more information on available marks and encodings, see :ref:`mark-reference`
and :ref:`encoding-reference`.


.. _basic-tutorial-aggregation:

Data Transformation: Aggregation
--------------------------------
To allow for more flexibility in how data are visualized, Altair has a built-in
syntax for *aggregation* of data.
For example, we can compute the average of all values by specifying this
aggregate within the column identifier:

.. altair-plot::

    Chart(data).mark_point().encode(
        x='a',
        y='average(b)'
    )

Now within each x-axis category, we see a single point reflecting the
average of the values within that category.

Typically, aggregated values are not represented by point markings,
but by bar markings. We can do this by replacing :meth:`~Chart.mark_point`
with :meth:`~Chart.mark_bar`:

.. altair-plot::

    Chart(data).mark_bar().encode(
        x='a',
        y='average(b)'
    )

Because the categorical feature is mapped to the ``x``-axis, the result is
a vertical bar chart. To get a horizontal bar chart, all we need is to
swap the ``x`` and ``y`` keywords:

.. altair-plot::

    Chart(data).mark_bar().encode(
        y='a',
        x='average(b)'
    )

Aside: Examining the JSON Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recall that Altair's main purpose is to convert plot specifications to a JSON
string that conforms to the Vega-Lite schema.
It is instructive here to use the :meth:`~Chart.to_json` method to inspect the
JSON specification that Altair is exporting and sending to Vega-Lite.
For clarity, we'll leave out the data and make a nicely-formatted output:

.. testcode::

    chart = Chart(data).mark_bar().encode(
        x='a',
        y='average(b)',
    )
    print(chart.to_json(data=False, indent=2, sort_keys=True))

.. testoutput::

    {
      "encoding": {
        "x": {
          "field": "a",
          "type": "nominal"
        },
        "y": {
          "aggregate": "average",
          "field": "b",
          "type": "quantitative"
        }
      },
      "mark": "bar"
    }

Notice here that ``encode(x='a')`` has been expanded to a JSON structure with
a ``field`` name, and a ``type`` for the data.
The ``encode(y='b')`` has been expanded similarly and includes an ``aggregate``
field.

Altair's full shorthand syntax includes a way to specify the type of the
column as well:

.. testcode::

    from altair import Y
    y = Y('average(b):Q')
    print(y.to_json(sort_keys=True))

.. testoutput::

    {"aggregate": "average", "field": "b", "type": "quantitative"}

This short-hand is equivalent to spelling-out the attributes by name:

.. testcode::

    y = Y(field='b', type='quantitative', aggregate='average')
    print(y.to_json(sort_keys=True))

.. testoutput::

    {"aggregate": "average", "field": "b", "type": "quantitative"}

This more verbose means of specifying channels can be used directly in
Altair chart specifications, a fact that becomes useful when using some
of the more advanced field configurations:

.. altair-plot::

    from altair import X, Y

    Chart(data).mark_bar().encode(
        X('a', type='nominal'),
        Y('b', type='quantitative', aggregate='average')
    )


.. _basic-tutorial-customization:

Customizing your Visualization
------------------------------
By default, Altair via Vega-Lite makes some choices about default properties
of the visualization.
Altair also provides an API to customize the look of the visualization.
For example, we can specify the axis titles using the ``axis`` attribute
of channel classes, and we can specify the color of the marking by setting
the ``color`` keyword of the ``Chart.mark_*`` methods to any valid HTML
color string:

.. altair-plot::

    from altair import X, Y, Axis

    Chart(data).mark_bar(color='lightgreen').encode(
        X('a', axis=Axis(title='category')),
        Y('average(b)', axis=Axis(title='avg(b) by category'))
    )


.. _basic-tutorial-publishing:

Publishing your Visualization
-----------------------------
Once you have visualized your data, perhaps you would like to publish it
somewhere on the web. This can be done straightforwardly using the
Vega-Embed_ javascript package.
A simple example of a stand-alone HTML document can be generated for any
chart using the :meth:`Chart.to_html` method:

.. test-code::

    chart = Chart(data).mark_bar().encode(
        x='a',
        y='average(b)',
    )
    html = chart.to_html()

The basic HTML template produces output that looks like this, where the JSON
specification for your plot produced by :meth:`Chart.to_json` should be stored
in the ``vlSpec`` Javascript variable:

.. code-block:: html

    <!DOCTYPE html>
    <head>
      <title>Vega-Lite Chart</title>
      <meta charset="utf-8">

      <script src="https://d3js.org/d3.v3.min.js"></script>
      <script src="https://vega.github.io/vega/vega.js"></script>
      <script src="https://vega.github.io/vega-lite/vega-lite.js"></script>
      <script src="https://vega.github.io/vega-editor/vendor/vega-embed.js" charset="utf-8"></script>

      <style media="screen">
        /* Add space between vega-embed links  */
        .vega-actions a {
          margin-right: 5px;
        }
      </style>
    </head>
    <body>
      <!-- Container for the visualization -->
      <div id="vis"></div>

      <script>
      var vlSpec = // output of chart.to_json() goes here

      var embedSpec = {
        mode: "vega-lite",  // Instruct Vega-Embed to use the Vega-Lite compiler
        spec: vlSpec
      };

      // Embed the visualization in the container with id `vis`
      vg.embed("#vis", embedSpec, function(error, result) {
        // Callback receiving the View instance and parsed Vega spec
        // result.view is the View, which resides under the '#vis' element
      });
      </script>
    </body>
    </html>

For more information on embedding Altair/Vega-Lite, see the documentation of the Vega-Embed_ project.



.. _Vega-Embed: https://github.com/vega/vega-embed
