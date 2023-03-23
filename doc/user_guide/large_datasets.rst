.. _large-datasets:

Large Datasets
--------------
If you try to create a plot that will directly embed a dataset with more than
5000 rows, you will see a ``MaxRowsError``:

.. altair-plot::
   :output: none
   
   import altair as alt
   import pandas as pd

   data = pd.DataFrame({"x": range(10000)})
   alt.Chart(data).mark_line()

.. code-block:: none

    MaxRowsError: The number of rows in your dataset is greater than the maximum
                  allowed (5000). For information on how to plot larger datasets
                  in Altair, see the documentation.

This is not because Altair cannot handle larger datasets, but it is because it
is important for the user to think carefully about how large datasets are handled. 
The following sections describe various considerations as well as approaches to deal with
large datasets.

If you are certain you would like to embed your full dataset within the visualization
specification, you can disable the ``MaxRows`` check::

    alt.data_transformers.disable_max_rows()

Challenges
~~~~~~~~~~
By design, Altair does not produce plots consisting of pixels, but plots
consisting of data plus a visualization specification. For example, here is a 
simple chart made from a dataframe with three rows of data:

.. altair-plot::
    :output: none

    import altair as alt
    import pandas as pd
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 1, 2]})

    chart = alt.Chart(data).mark_line().encode(
         x='x',
         y='y'
    )

    from pprint import pprint
    pprint(chart.to_dict())

.. code-block:: none

    {'$schema': 'https://vega.github.io/schema/vega-lite/v2.4.1.json',
     'config': {'view': {'height': 300, 'width': 300}},
     'data': {'values': [{'x': 1, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 2}]},
     'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                  'y': {'field': 'y', 'type': 'quantitative'}},
     'mark': 'line'}

The resulting specification includes a representation of the data converted
to JSON format, and this specification is embedded in the notebook or web page
where it can be used by Vega-Lite to render the plot.
As the size of the data grows, this explicit data storage can lead to some
very large specifications which can have various negative implications:

* large notebook files which can slow down your notebook environment such as JupyterLab
* if you display the chart on a website it slows down the loading of the page
* slow evaluation of transforms as the calculations are performed in JavaScript which is not the fastest language for processing large amounts of data


.. _passing-data-by-url:

Passing Data by URL
~~~~~~~~~~~~~~~~~~~
A common approach when working with large datasets is to not embed the data directly,
but rather store it separately and pass it to the chart by URL. 
This not only addresses the issue of large notebooks, but also leads to better
interactivity performance with large datasets.


Local Data Server
^^^^^^^^^^^^^^^^^
A convenient way to do this is by using the `altair_data_server <https://github.com/altair-viz/altair_data_server>`_
package. It serves your data from a local threaded server. First install the package:

.. code-block:: none

   pip install altair_data_server

And then enable the data transformer::

    import altair as alt
    alt.data_transformers.enable('data_server')

Note that this approach may not work on some cloud-based Jupyter notebook services.
A disadvantage of this method is that if you reopen the notebook, the plot may no longer display
as the data server is no longer running.

Local Filesystem
^^^^^^^^^^^^^^^^
You can also persist the data to disk and then pass the path to Altair:

.. altair-plot::
   :output: none

   url = 'data.json'
   data.to_json(url, orient='records')

   chart = alt.Chart(url).mark_line().encode(
       x='x:Q',
       y='y:Q'
   )
   pprint(chart.to_dict())


.. code-block:: none

    {'$schema': 'https://vega.github.io/schema/vega-lite/v2.4.1.json',
     'config': {'view': {'height': 300, 'width': 300}},
     'data': {'url': 'data.json'},
     'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                  'y': {'field': 'y', 'type': 'quantitative'}},
     'mark': 'line'}


Altair also has a ``JSON`` data transformer that will do this
transparently when enabled::

    alt.data_transformers.enable('json')

There is a similar CSV data transformer, but it must be used more carefully
because CSV does not preserve data types as JSON does.

Note that the filesystem approach may not work on some cloud-based Jupyter
notebook services. A disadvantage of this method is also a loss of portability: if the notebook is
ever moved, the data file must accompany it or the plot may not display.

Vega Datasets
^^^^^^^^^^^^^
If you are working with one of the vega datasets, you can pass the data by URL
using the ``url`` attribute:

.. code-block:: python

   from vega_datasets import data
   source = data.cars.url

   alt.Chart(source).mark_point() # etc.


PNG and SVG Renderers
~~~~~~~~~~~~~~~~~~~~~
The approaches presented in :ref:`passing-data-by-url` have the disadvantage that the data is no longer
contained in the notebook and you therefore lose portability or don't see the charts when you reopen the notebook.
Furthermore, the data still needs to be sent to the frontend, e.g. your browser, and any calculations will happen there.

You might achieve a speedup by enabling either the PNG or SVG renderer 
as described in :ref:`renderers`. Instead of a Vega-Lite specification, they will 
prerender the visualization and send only a static image to your notebook. This can
greatly reduce the amount of data that is being transmitted. The downside with this approach is,
that you loose all interactivity features of Altair.

Both renderers require you to install either the `vl-convert`_ or the `altair_saver`_ package, see :ref:`saving-png`,
whereas `vl-convert`_ is expected to provide the better performance.

.. _preaggregate-and-filter:

Preaggregate and Filter in Pandas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Another common approach is to perform data transformations such as aggregations
and filters using Pandas before passing the data to Altair.

For example, to create a bar chart for the ``barley`` dataset summing up ``yield`` grouped by ``site``,
it is convenient to pass the unaggregated data to Altair:

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).mark_bar().encode(
        x="sum(yield):Q",
        y=alt.Y("site:N").sort("-x")
    )


The above works well for smaller datasets but let's imagine that the ``barley`` dataset
is larger and the resulting Altair chart slows down your notebook environment.
To reduce the data being passed to Altair, you could subset the dataframe to 
only the necessary columns:

.. code-block:: python

    alt.Chart(source[["yield", "site"]]).mark_bar().encode(
        x="sum(yield):Q",
        y=alt.Y("site:N").sort("-x")
    )

You could also precalculate the sum in Pandas which would reduce the size of the dataset even more:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.barley()
    source_aggregated = (
        source.groupby("site")["yield"].sum().rename("sum_yield").reset_index()
    )

    alt.Chart(source_aggregated).mark_bar().encode(
        x="sum_yield:Q",
        y=alt.Y("site:N").sort("-x")
    )


Preaggregate Boxplot
^^^^^^^^^^^^^^^^^^^^
A boxplot is a useful way to visualize the distribution of data and it is simple to create
in Altair.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    df = data.cars()

    alt.Chart(df).mark_boxplot().encode(
        x="Miles_per_Gallon:Q",
        y="Origin:N",
        color=alt.Color("Origin").legend(None)
    )

If you have a lot of data, you can perform the necessary calculations in Pandas and only
pass the resulting summary statistics to Altair.

First, let's define a few parameters where ``k`` stands for the multiplier which is used
to calculate the boundaries of the whiskers.

.. altair-plot::
    :output: none
    
    import altair as alt
    import pandas as pd
    from vega_datasets import data

    k = 1.5
    group_by_column = "Origin"
    value_column = "Miles_per_Gallon"


In the next step, we will calculate the summary statistics which are needed for the boxplot.

.. altair-plot::
    :output: repr
    :chart-var-name: agg_stats
    
    df = data.cars()

    agg_stats = df.groupby(group_by_column)[value_column].describe()
    agg_stats["iqr"] = agg_stats["75%"] - agg_stats["25%"]
    agg_stats["min_"] = agg_stats["25%"] - k * agg_stats["iqr"]
    agg_stats["max_"] = agg_stats["75%"] + k * agg_stats["iqr"]
    data_points = df[[value_column, group_by_column]].merge(
        agg_stats.reset_index()[[group_by_column, "min_", "max_"]]
    )
    # Lowest data point which is still above or equal to min_
    # This will be the lower end of the whisker
    agg_stats["lower"] = (
        data_points[data_points[value_column] >= data_points["min_"]]
        .groupby(group_by_column)[value_column]
        .min()
    )
    # Highest data point which is still below or equal to max_
    # This will be the upper end of the whisker
    agg_stats["upper"] = (
        data_points[data_points[value_column] <= data_points["max_"]]
        .groupby(group_by_column)[value_column]
        .max()
    )
    # Store all outliers as a list
    agg_stats["outliers"] = (
        data_points[
            (data_points[value_column] < data_points["min_"])
            | (data_points[value_column] > data_points["max_"])
        ]
        .groupby(group_by_column)[value_column]
        .apply(list)
    )
    agg_stats = agg_stats.reset_index()
    
    # Show whole dataframe
    pd.set_option("display.max_columns", 15)
    print(agg_stats)

And finally, we can create the same boxplot as above but we only pass the calculated
summary statistics to Altair instead of the full dataset.

.. altair-plot::

    base = alt.Chart(agg_stats).encode(
        y="Origin:N"
    )

    rules = base.mark_rule().encode(
        x=alt.X("lower").title("Miles_per_Gallon"),
        x2="upper",
    )

    bars = base.mark_bar(size=14).encode(
        x="25%",
        x2="75%",
        color=alt.Color("Origin").legend(None),
    )

    ticks = base.mark_tick(color="white", size=14).encode(
        x="50%"
    )

    outliers = base.transform_flatten(
        flatten=["outliers"]
    ).mark_point(
        style="boxplot-outliers"
    ).encode(
        x="outliers:Q",
        color="Origin",
    )
    
    rules + bars + ticks + outliers


VegaFusion
~~~~~~~~~~
`VegaFusion`_ is a third-party package that re-implements most Vega-Lite transforms for evaluation
in the Python kernel.  This makes it possible to scale many Altair charts to millions of rows as long as
they include some form of aggregation.

VegaFusion 1.0 provides two rendering modes that are useful in different situations.

Mime Renderer
^^^^^^^^^^^^^
The `VegaFusion mime renderer`_ is a good choice for charts that do not re-aggregate or re-filter data in response
to selections. It is enabled with:

.. code-block:: python

    import vegafusion as vf
    vf.enable()

The mime renderer automates the :ref:`preaggregate-and-filter` workflow described above. Right before
a chart is rendered, VegaFusion extracts the datasets and supported transforms and evaluates them in the
Python kernel. It then removes any unused columns and inlines the transformed data into the chart specification
for rendering.

Charts rendered this way are self-contained and do not require the Python kernel or a custom
notebook extension to display.  They are rendered with the same frontend functionality that
is already used to display regular Altair charts.

Widget Renderer
^^^^^^^^^^^^^^^
The `VegaFusion widget renderer`_ is a good choice for charts that re-aggregate or re-filter data in response
to selections. It is enabled with:

.. code-block:: python

    import vegafusion as vf
    vf.enable_widget()

The widget renderer uses a Jupyter Widget extension to maintain a live connection between the displayed
chart and the Python kernel. This makes it possible for transforms to be evaluated interactively in response to
changes in selections. Charts rendered this way require a running Python kernel and Jupyter Widget extension to
display.

.. _VegaFusion: https://vegafusion.io
.. _VegaFusion mime renderer: https://vegafusion.io/mime_renderer.html
.. _VegaFusion widget renderer: https://vegafusion.io/widget_renderer.html
.. _vl-convert: https://github.com/vega/vl-convert
.. _altair_saver: http://github.com/altair-viz/altair_saver/
