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

A data transformer is a Python function that takes in the item passed in as the data and
transforms it. If it can't handle the type passed in, it should return it unchanged::

    def data_transformer(data):
        if isinstance(data, MyType):
            # Transform and return the data
            return fn(data)    
        return data

Built-in data transformers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair includes a default set of data transformers with the following signatures.

Convert strings into URL data::

    to_url(data)

Raise a ``MaxRowsError`` if a Dataframe has more than ``max_rows`` rows::

    limit_rows(data, max_rows=5000)

Randomly sample a DataFrame (without replacement) before visualizing::

    sample(data, n=None, frac=None)

Convert a Dataframe to a separate ``.json`` file before visualization::

    to_json(data, prefix='altair-data'):

Convert a Dataframe to a separate ``.csv`` file before visualiztion::

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
