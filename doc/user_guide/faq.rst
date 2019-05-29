.. currentmodule:: altair

.. _frequently-asked-questions:

Frequently Asked Questions
==========================

.. _faq-other-ides:

Does Altair work with IPython Terminal/PyCharm/Spyder/<my favorite IDE>
-----------------------------------------------------------------------
Altair can be used to create chart specifications with any frontend that
executes Python code, but in order to *render* those charts requires connecting
altair to an environment capable of executing the javascript code that
turns the JSON specification into a visual chart.

There are extensions included in JupyterLab, Jupyter Notebook, Colab,
Kaggle kernels, Hydrogen, and nteract that know how to automatically perform
this rendering (see :ref:`installation` for details).

For other frontends that don't have vega-lite rendering built-in, it is
possible to work with Altair charts using either the ``vegascope`` project,
or the build-in :meth:`Chart.serve` or :meth:`Chart.save` methods.
For more information on thse, see :ref:`display-general`.

.. _faq-no-display:

I tried to make a plot but it doesn't show up
---------------------------------------------
There are two basic reasons that a chart might not show up:

1. You have not installed and/or enabled the appropriate renderer for your
   frontend, which means charts cannot be displayed.
2. You have inadvertently created an invalid chart, and there is a javascript
   error preventing it from being displayed.

For details on how to trouble-shoot these kinds of display issues on various
front-ends, see :ref:`display-troubleshooting`.

.. _altair-faq-large-notebook:

Why does Altair lead to such extremely large notebooks?
-------------------------------------------------------
By design, Altair does not produce plots consisting of pixels, but plots
consisting of data plus a visualization specification. As discussed in
:ref:`user-guide-data`, this data can be specified in one of several ways,
either via a pandas DataFrame, a file or URL, or a JSON data object.
When you specify the data as a pandas DataFrame, this data is converted to
JSON and included in its entirety in the plot spec.

For example, here is a simple chart made from a dataframe with three rows
of data:

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
very large specifications, and by extension, some very large notebooks or
web pages.

The best way around this is to store the data in an external file, and
pass it to the chart by URL. You can do this manually if you wish:

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

For other strategies for effectively working with large datasets in Altair, see
:ref:`altair-faq-max-rows`

With this type of approach, the data is now stored as an external file
rather than being embedded in the notebook,
leading to much more compact plot specifications.
The disadvantage, of course, is a loss of portability: if the notebook is
ever moved, the data file must accompany it or the plot may not display.


.. _altair-faq-max-rows:

MaxRowsError: How can I plot Large Datasets?
--------------------------------------------
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
is important for the user to think carefully about how large datasets are handled.
As noted above in :ref:`altair-faq-large-notebook`, it is quite easy to end up with
very large notebooks if you make many visualizations of a large dataset, and this
error is a way of preventing that.

You can get around it in a few ways:

Disabling MaxRowsError
~~~~~~~~~~~~~~~~~~~~~~
If you are certain you would like to embed your dataset within the visualization
specification, you can disable the ``MaxRows`` check with the following::

    alt.data_transformers.disable_max_rows()

If you choose this route, please be careful: if you are making multiple plots
with the dataset in a particular notebook, the notebook will grow very large
and performance may suffer.

Passing Data by URL
~~~~~~~~~~~~~~~~~~~
A better solution when working with large datasets is to not embed the data
in the notebook, but rather store it separately pass it to the chart by URL.
This not only addresses the issue of large notebooks, but also leads to better
interactivity performance with large datasets.

Vega Datasets
^^^^^^^^^^^^^
If you are working with one of the vega datasets, you can pass the data by URL
using the ``url`` attribute:

.. code-block:: python

   from vega_datasets import data
   source = data.cars.url

   alt.Chart(source).mark_point() # etc.

Local Filesystem
^^^^^^^^^^^^^^^^
You may also save data to a local filesystem and reference the data by
file path. Altair has a ``JSON`` data transformer that will do this
transparently when enabled::

    alt.data_transformers.enable('json')

With this data transformer enabled, each time you make a plot the data will be
serialized to disk and referenced by URL, rather than being embedded in the
notebook output.
You may also manually save the data to file and reference it that way
(see :ref:`altair-faq-large-notebook`).

There is a similar CSV data transformer, but it must be used more carefully
because CSV does not preserve data types as JSON does.

Note that the filesystem approach may not work on some cloud-based Jupyter
notebook services.

Local Data Server
^^^^^^^^^^^^^^^^^
It is also possible to serve your data from a local threaded server to avoid writing
datasets to disk. The `altair_data_server <https://github.com/altair-viz/altair_data_server>`_
package makes this easy. First install the package:

.. code-block:: none

   pip install altair_data_server

And then enable the data transformer::

    import altair as alt
    alt.data_transformers.enable('data_server')

Note that this may not approach on some cloud-based Jupyter notebook services.
