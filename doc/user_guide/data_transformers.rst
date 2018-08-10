.. _data-transformers:

Data transformers
=================

Before a Vega-Lite or Vega specification can be passed to a renderer, it typically
has to be transformed in a number of ways:

* Pandas Dataframe has to be sanitized and serialized to JSON.
* The rows of a Dataframe might need to be sampled or limited to a maximum number.
* The Dataframe might be written to a ``.csv`` of ``.json`` file for performance
  reasons.

These data transformations are managed by the data transformation API of Altair.

.. note::

    The data transformation API of Altair should not be confused with the ``transform``
    API of Vega and Vega-Lite.

A data transformer is a Python function that takes a Vega-Lite data ``dict`` or
Pandas ``DataFrame`` and returns a transformed version of either of these types::

    from typing import Union
    Data = Union[dict, pd.DataFrame]

    def data_transformer(data: Data) -> Data:
        # Transform and return the data
        return transformed_data

Dataset Consolidation
~~~~~~~~~~~~~~~~~~~~~
Datasets passed as Pandas dataframes can be represented in the chart in two
ways:

- As literal dataset values in the ``data`` attribute at any level of the
  specification
- As a named dataset in the ``datasets`` attribute of the top-level
  specification.

The former is a bit more simple, but common patterns of usage in Altair can
often lead to full datasets being listed multiple times in their entirety
within a single specification.

For this reason, Altair 2.2 and newer will by default move all
directly-specified datasets into the top-level ``datasets`` entry, and
reference them by a unique name determined from the hash of the data
representation. The benefit of using a hash-based name is that even if the
user specifies a dataset in multiple places when building the chart, the
specification will only include one copy.

This behavior can be modified by setting the ``consolidate_datasets`` attribute
of the data transformer.

For example, consider this simple layered chart:

.. altair-plot::
   :chart-var-name: chart
		    
   import altair as alt
   import pandas as pd

   df = pd.DataFrame({'x': range(5),
                      'y': [1, 3, 4, 3, 5]})

   line = alt.Chart(df).mark_line().encode(x='x', y='y')
   points = alt.Chart(df).mark_point().encode(x='x', y='y')
   chart = line + points

If we look at the resulting specification, we see that although the dataset
was specified twice, only one copy of it is output in the spec:

.. altair-plot::
   :output: stdout

   from pprint import pprint
   pprint(chart.to_dict())

This consolidation of datasets is an extra bit of processing that is turned on
by default in all renderers.

If you would like to disable this dataset consolidation for any reason, you can
do so by setting ``alt.data_transformers.consolidate_datasets = False``, or
by using the ``enable()`` context manager to do it only temporarily:

.. altair-plot::
   :output: stdout

   with alt.data_transformers.enable(consolidate_datasets=False):
       pprint(chart.to_dict())
   
Notice that now the dataset is not specified within the top-level ``datasets``
attribute, but rather as values within the ``data`` attribute of each
individual layer. This duplication of data is the reason that dataset
consolidation is set to ``True`` by default.


Built-in data transformers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair includes a default set of data transformers with the following signatures.

Raise a ``MaxRowsError`` if a Dataframe has more than ``max_rows`` rows::

    limit_rows(data, max_rows=5000)

Randomly sample a DataFrame (without replacement) before visualizing::

    sample(data, n=None, frac=None)

Convert a Dataframe to a separate ``.json`` file before visualization::

    to_json(data, prefix='altair-data'):

Convert a Dataframe to a separate ``.csv`` file before visualization::

    to_csv(data, prefix='altair-data'):

Convert a Dataframe to inline JSON values before visualization::

    to_values(data):

Piping
~~~~~~

Multiple data transformers can be piped together using ``pipe``::

    from altair import pipe, limit_rows, to_values
    pipe(data, limit_rows(10000), to_values)

Managing data transformers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair maintains a registry of data transformers, which includes a default
data transformer that is automatically applied to all Dataframes before rendering.

To see the registered transformers::

    >>> import altair as alt
    >>> alt.data_transformers.names()
    ['default', 'json', 'csv']

The default data transformer is the following::

    def default_data_transformer(data):
        return pipe(data, limit_rows, to_values)

The ``json`` and ``csv`` data transformers will save a Dataframe to a temporary
``.json`` or ``.csv`` file before rendering. There are a number of performance
advantages to these two data transformers:

* The full dataset will not be saved in the notebook document.
* The performance of the Vega-Lite/Vega JavaScript appears to be better
  for standalone JSON/CSV files than for inline values.

There are disadvantages of the JSON/CSV data transformers:

* The Dataframe will be exported to a temporary ``.json`` or ``.csv``
  file that sits next to the notebook.
* That notebook will not be able to re-render the visualization without
  that temporary file (or re-running the cell).

In our experience, the performance improvement is significant enough that
we recommend using the ``json`` data transformer for any large datasets::

    alt.data_transformers.enable('json')

We hope that others will write additional data transformers - imagine a
transformer which saves the dataset to a JSON file on S3, which could
be registered and enabled as::

    alt.data_transformers.register('s3', lambda data: pipe(data, to_s3('mybucket')))
    alt.data_transformers.enable('s3')
