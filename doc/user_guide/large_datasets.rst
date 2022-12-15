.. _large-datasets:

Large Datasets
--------------
If you try to create a plot that will directly embed a dataset with more than
5000 rows, you will see a ``MaxRowsError``:

.. altair-plot::
   :output: none

   data = pd.DataFrame({'x': range(10000)})
   alt.Chart(data).mark_line()

.. code-block:: none

    MaxRowsError: The number of rows in your dataset is greater than the maximum
                  allowed (5000). For information on how to plot larger datasets
                  in Altair, see the documentation.

This is not because Altair cannot handle larger datasets, but it is because it
is important for the user to think carefully about how large datasets are handled. The following sections
describe various considerations and approaches you can take.

If you are certain you would like to embed your full dataset within the visualization
specification, you can disable the ``MaxRows`` check with the following::

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
     'config': {'view': {'height': 300, 'width': 400}},
     'data': {'values': [{'x': 1, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 2}]},
     'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                  'y': {'field': 'y', 'type': 'quantitative'}},
     'mark': 'line'}

The resulting specification includes a representation of the data converted
to JSON format, and this specification is embedded in the notebook or web page
where it can be used by Vega-Lite to render the plot.
As the size of the data grows, this explicit data storage can lead to some
very large specifications which can have various negative implications:

* large notebook files which can slow down your notebook environment/IDE
* if you display the chart on a website it slows down the loading of the page
* slow evaluation of transforms as calculations happen in JavaScript which is not the fastest language for processing large amounts of data

A common approach is to transform or filter your data already in Python as described in :ref:`user-guide-transformations`
and to subset to only the columns which are relevant for your chart. However, sometimes this might not be possible or
not convenient. The following sections describe various approaches you can try with their advantages and disadvantages.

.. _passing-data-by-url:

Passing Data by URL
~~~~~~~~~~~~~~~~~~~
A better solution when working with large datasets is to not embed the data directly,
but rather store it separately and pass it to the chart by URL. This not only addresses the issue of large notebooks, but also leads to better
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
A disadvantage of this method is that if you reopen the notebook, the plot may initially not display
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
     'config': {'view': {'height': 300, 'width': 400}},
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

A further speedup might be achieved by enabling either the PNG or SVG renderer 
as described in :ref:`renderers`. This will lead to only the final static image being sent
to your notebook, in some cases greatly reducing the amount of data transmitted. The downside with this approach is,
that all interactivity features of Altair will no longer work.

Both renderers require you to install either the `vl-convert`_ or the `altair_saver`_ package, see :ref:`saving-png`,
whereas `vl-convert`_ is expected to provide the better performance.


VegaFusion
~~~~~~~~~~
If you work with large datasets and require your charts to be interactive, the `VegaFusion`_ package might be
a good option for you. Make sure to check out it's documentation on how to use it as well as the current limitations.

.. _VegaFusion: https://vegafusion.io
.. _vl-convert: https://github.com/vega/vl-convert
.. _altair_saver: http://github.com/altair-viz/altair_saver/