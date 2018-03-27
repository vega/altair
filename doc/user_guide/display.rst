.. _displaying-charts:

Displaying Charts
=================

Altair provides a high-level API for creating visualizations that are
encoded as declarative JSON objects. To display a visualization, those JSON
objects must be displayed using the `Vega-Lite`_ and `Vega`_ JavaScript packages.
This step of displaying a Vega-Lite or Vega JSON object is encoding in a renderer
abstraction. This section of the documentation describes renderers and how you
can use them to display Altair visualizations.

You may need to install an additional Python/npm package to display Altair
charts for a given frontend user-interface. See instructions for:
:ref:`display-notebook`, :ref:`display-jupyterlab`, :ref:`display-nteract`
and :ref:`display-colab`.

.. _altair-vega-versions:

Vega-Lite/Vega versions
-----------------------

As of version 2.0, Altair includes support for multiple version of both
Vega-Lite (2.x and 1.x) and Vega (3.x and 2.x) in a single Python package.
The default usage, including all examples in this documentation, makes use of
the newest available versions (Vega-Lite 2.X and Vega 3.X).

The vega-lite version used by default can be found as follows:

.. code-block:: python

   >>> import altair as alt
   >>> alt.schema.SCHEMA_VERSION
   'v2.3.0'

If you wish to use an older version of these libraries, see :ref:`importing`
for more information. We strongly recommend all users transition to
Vega-Lite 2.x and Vega 3.x. These versions support many new features, are more
stable, and Altair 2.0 works best with them.

For all users, the important point here is that you must have a renderer
installed that works with the appropriate version.

.. _renderers:

Renderers
---------

Altair displays visualizations using renderers. There are two aspects of renderers:

* The Python side :ref:`renderer-api` that sends display data to various frontend
  user-interfaces.
* Frontend user-interfaces that interpret that display data and render a visualization.
  See relevant instructions for:

  * :ref:`display-notebook`
  * :ref:`display-jupyterlab`
  * :ref:`display-nteract`

.. _renderer-api:

Renderer API
~~~~~~~~~~~~

In Altair, a renderer is any function that accepts a Vega-Lite or Vega
visualization specification as a Python ``dict``, and returns a Python ``dict``
in Jupyter's `MIME Bundle format
<https://jupyter-client.readthedocs.io/en/stable/messaging.html#display-data>`_.
The keys of the MIME bundle should be MIME types (such as ``image/png``) and the
values should be the data for that MIME type (text, base64 encoded binary or
JSON). The type signature of a renderer is thus::

    def renderer(spec: dict) -> dict:
        ...

Altair and various user-interfaces have standardized on a couple of custom MIME types
for Vega and Vega-Lite:

* Vega-Lite 2.x: ``application/vnd.vegalite.v2+json``
* Vega-Lite 1.x: ``application/vnd.vegalite.v1+json``
* Vega 3.x: ``application/vnd.vega.v3+json``
* Vega 2.x: ``application/vnd.vega.v2+json``

The default renderers simply take a JSON spec and return a MIME bundle with one
of these MIME types::

    def default_renderer(spec):
        bundle = {}
        metadata = {}
        bundle['text/plain'] = '<VegaLite object>`
        bundle[mime_type] = 'application/vnd.vegalite.v2+json'
        return bundle, metadata

If a renderer needs to do custom display logic that doesn't use Jupyter's display
system, it can return an empty MIME bundle ``dict``::

    def non_jupyter_renderer(spec):
        # Custom display logic that uses the spec
        ...
        # Return empty MIME bundle
        return {}

Altair offers an API to list the known renderers, register new ones and enable
a given one. To return the registered renderers as a Python list::

    >>> import altair as alt
    >>> alt.renderers.names()
    ['default', 'json']

To enable the JSON renderer, which results in a collapsible JSON tree view
in JupyterLab/nteract::

    >>> alt.renderers.enable('json')

To register and enable a new renderer::

    >>> alt.renderers.register('custom_renderer', custom_renderer)
    >>> alt.renderers.enable('custom_renderer')

Renderers can also be registered using the `entrypoints`_ API of Python packages.
For an example, see `ipyvega3`_.

This same ``renderer`` objects exists separately on all of the Python APIs
for Vega-Lite/Vega described in :ref:`importing`.

.. _display-notebook:

Jupyter Notebook
~~~~~~~~~~~~~~~~

To render Vega-Lite 2.x or Vega 3.x in the Jupyter Notebook (as mentioned above
we recommend these versions), you will need to install and enable the
`ipyvega3`_ Python package using conda:

.. code-block:: bash

    $ conda install vega3 --channel conda-forge

or ``pip``:

.. code-block:: bash

    $ pip install jupyter pandas vega3
    $ jupyter nbextension install --sys-prefix --py vega3 # not needed in notebook >= 5.3


For Vega-Lite 1.x or Vega 2.x, you will need to install and enable the `ipyvega`_ Python
package using:

.. code-block:: bash

    $ conda install vega --channel conda-forge

or ``pip``:

.. code-block:: bash

    $ pip install jupyter pandas vega
    $ jupyter nbextension install --sys-prefix --py vega # not needed in notebook >= 5.3

Once you have installed one of these packages, enable the corresponding renderer in Altair::

    alt.renderers.enable('notebook')



.. _display-jupyterlab:

JupyterLab
~~~~~~~~~~

JupyterLab 0.31
+++++++++++++++++

Version 0.31 of JupyterLab includes built-in support for VegaLite 1.x and Vega
2.x. This will work with Altair's Vega-Lite 1.x API out of the box::

    import altair.vegalite.v1 as alt

To add support for Vega-Lite 2.x and Vega 3.x install the following JupyterLab
extension (which requires nodejs)::

    conda install -c conda-forge nodejs  # if you do not already have nodejs installed
    jupyter labextension install @jupyterlab/vega3-extension

and then import Altair as::

    import altair as alt

JupyterLab 0.32 and later
+++++++++++++++++++++++++++

JupyterLab versions 0.32 and later include built-in support for Vega-Lite 2.x and
Vega 3.x. These will work out of the box with Altair imported as::

    import altair as alt

An extension is available with the older Vega-Lite 1.x and Vega 2.x renderers
(labextension install requires nodejs)::

    conda install -c conda-forge nodejs  # if you do not already have nodejs installed
    jupyter labextension install @jupyterlab/vega2-extension

.. _display-nteract:

nteract
~~~~~~~

nteract will render Vega-Lite 1.x and Vega out of the box. Support for Vega-Lite 2.x
and Vega 3.x will likely be released soon.

.. _display-colab:

Colab
~~~~~
Google's Colab is a cloud-based notebook backed by Google Drive. Altair works
with the public version of Colab once the package is installed and ``'colab'``
renderer is enabled.

At the top of your Colab session, run the following::

    !pip install altair
    import altair as alt
    alt.renderers.enable('colab')

And then you can create Altair plots normally within the notebook.

.. _data-transformers:

Data transformers
-----------------

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

Built-in data transformers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair includes a default set of data transformers with the following signatures.

Raise a ``MaxRowsError`` if a Dataframe has more than ``max_rows`` rows::

    limit_rows(data, max_rows=5000)

Randomly sample a DataFrame (without replacement) before visualizing::

    sample(data, n=None, frac=None)

Convert a Dataframe to a separate ``.json`` file before visualization::

    to_json(data, filename=None, prefix='altair-data', base_url='/', nbserver_cwd='~'):

Convert a Dataframe to a separate ``.csv`` file before visualiztion::

    to_csv(data, filename=None, prefix='altair-data', base_url='/', nbserver_cwd='~'):

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

    alt.data_transformers.register('s3', lambda data: pipe(sample, to_s3('mybucket')))
    alt.data_transformers.enable('s3')



.. _entrypoints: https://github.com/takluyver/entrypoints
.. _ipyvega: https://github.com/vega/ipyvega/tree/master
.. _ipyvega3: https://github.com/vega/ipyvega/tree/vega3
.. _JupyterLab: http://jupyterlab.readthedocs.io/en/stable/
.. _nteract: https://nteract.io
.. _Colab: https://colab.research.google.com
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Vega: https://vega.github.io/vega/
