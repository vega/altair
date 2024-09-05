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
   alt.Chart(data).mark_point()

.. code-block:: none

    MaxRowsError: The number of rows in your dataset is greater than the maximum allowed (5000).

    Try enabling the VegaFusion data transformer which raises this limit by pre-evaluating data
    transformations in Python.
        >> import altair as alt
        >> alt.data_transformers.enable("vegafusion")

    Or, see https://altair-viz.github.io/user_guide/large_datasets.html for additional information
    on how to plot large datasets.

This is not because Altair cannot handle larger datasets, but it is because it
is important for the user to think carefully about how large datasets are handled. 
The following sections describe various considerations as well as approaches to deal with
large datasets.

If you are certain you would like to embed your full untransformed dataset within the visualization
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

.. _vegafusion-data-transformer:

VegaFusion Data Transformer
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The easiest and most flexible approach for addressing a ``MaxRowsError`` is to
enable the ``"vegafusion"`` data transformer, which was added in Altair 5.1.
`VegaFusion`_ is an external project that provides efficient Rust implementations
of most of Altair's data transformations. By evaluating data transformations (e.g. binning
and aggregations) in Python, the size of the datasets that must be included in the final chart
specification are often greatly reduced. In addition, VegaFusion automatically removes
unused columns, which reduces dataset size even for charts without data transformations.

When the ``"vegafusion"`` data transformer is active, data transformations will be
pre-evaluated when :ref:`displaying-charts`, :ref:`user-guide-saving`, converted charts a dictionaries,
and converting charts to JSON. When combined with :ref:`user-guide-jupyterchart` or the ``"jupyter"``
renderer (See :ref:`customizing-renderers`), data transformations will also be evaluated in Python
dynamically in response to chart selection events.

VegaFusion's development is sponsored by `Hex <https://hex.tech>`_.

Installing VegaFusion
^^^^^^^^^^^^^^^^^^^^^
The VegaFusion dependencies can be installed using pip

.. code-block:: none

   pip install "vegafusion[embed]"

or conda

.. code-block:: none

   conda install -c conda-forge vegafusion vegafusion-python-embed vl-convert-python

Enabling the VegaFusion Data Transformer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Activate the VegaFusion data transformer with:

.. code-block:: python

    import altair as alt
    alt.data_transformers.enable("vegafusion")

All charts created after activating the VegaFusion data transformer
will work with datasets containing up to 100,000 rows.
VegaFusion's row limit is applied after all supported data transformations have been applied.
So you are unlikely to reach it with a chart such as a histogram,
but you may hit it in the case of a large scatter chart or a chart that includes interactivity
when not using ``JupyterChart`` or the ``"jupyter"`` renderer.

If you need to work with larger datasets, you can disable the maximum row limit
or switch to using ``JupyterChart`` or the ``"jupyter"`` renderer described below.

Converting to JSON or dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When converting a VegaFusion chart to JSON with ``chart.to_json`` or to a Python dictionary with
``chart.to_dict``, the ``format`` argument must be set to ``"vega"`` rather than the
default of ``"vega-lite"``. For example:

.. code-block:: python

    chart.to_json(format="vega")
    chart.to_dict(format="vega")

This is because VegaFusion works with Vega chart specifications
rather than the Vega-Lite specifications produced by Altair. When the VegaFusion
data transformer is enabled, the `vl-convert`_
library is used to perform the conversion from Vega-Lite to Vega.

Local Timezone Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some Altair transformations (e.g. :ref:`user-guide-timeunit-transform`) are based on
a local timezone. Normally, the browser's local timezone is used. However, because
VegaFusion evaluates these transforms in Python before rendering, it's not always possible
to access the browser's timezone. Instead, the local timezone of the Python kernel will be
used by default. In the case of a cloud notebook service, this may be difference than
the browser's local timezone.

VegaFusion's local timezone may be customized using the ``vegafusion.set_local_tz``
function. For example:

.. code-block:: python

    import vegafusion as vf
    vf.set_local_tz("America/New_York")

When using ``JupyterChart`` or the ``"jupyter"`` renderer, the browser's local timezone
is used.

DuckDB Integration
^^^^^^^^^^^^^^^^^^
VegaFusion provides optional integration with `DuckDB`_. Because DuckDB can perform queries on pandas
DataFrames without converting through Arrow, it's often faster than VegaFusion's default query engine
which requires this conversion. See the `VegaFusion DuckDB`_ documentation for more information.

Interactivity
^^^^^^^^^^^^^
When using the default ``"html"`` renderer with charts that use selections to filter data interactively,
the VegaFusion data transformer will include all of the data that participates in the interaction in the resulting chart specification. This makes it an unsuitable approach for building interactive charts that filter large datasets (e.g. crossfiltering a dataset with over a million rows).

The ``JupyterChart`` widget and the ``"jupyter"`` renderer are designed to work with the VegaFusion
data transformer to evaluate data transformations interactively in response to selection events.
This avoids the need to transfer the full dataset to the browser, and so supports
interactive exploration of aggregated datasets on the order of millions of rows.

Either use ``JupyterChart`` directly:

.. code-block:: python

    import altair as alt
    alt.data_transformers.enable("vegafusion")
    ...
    alt.JupyterChart(chart)

Or, enable the ``"jupyter"`` renderer and display charts as usual:

.. code-block:: python

    import altair as alt
    alt.data_transformers.enable("vegafusion")
    alt.renderers.enable("jupyter")
    ...
    chart

Charts rendered this way require a running Python kernel and Jupyter Widget extension to
display, which works in many frontends including locally in the classic notebook, JupyterLab, and VSCode,
as well as remotely in Colab and Binder.

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

Both renderers require you to install the `vl-convert`_ package, see :ref:`saving-png`.

.. _preaggregate-and-filter:

Preaggregate and Filter in pandas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Another common approach is to perform data transformations such as aggregations
and filters using pandas before passing the data to Altair.

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

You could also precalculate the sum in pandas which would reduce the size of the dataset even more:

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

If you have a lot of data, you can perform the necessary calculations in pandas and only
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

.. _VegaFusion: https://vegafusion.io
.. _DuckDB: https://duckdb.org/
.. _VegaFusion DuckDB: https://vegafusion.io/duckdb.html
.. _vl-convert: https://github.com/vega/vl-convert
