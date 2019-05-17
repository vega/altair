.. _displaying-charts:

Displaying Charts in Various Frontends
======================================

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
  * :ref:`display-colab`

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
For an example, see `ipyvega`_.

This same ``renderer`` objects exists separately on all of the Python APIs
for Vega-Lite/Vega described in :ref:`importing`.

.. _display-notebook:

Displaying in the Jupyter Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To render Vega-Lite 2.x or Vega 3.x in the Jupyter Notebook (as mentioned above
we recommend these versions), you will need to install and enable the
`ipyvega`_ Python package using conda:

.. code-block:: bash

    $ conda install vega --channel conda-forge

or ``pip``:

.. code-block:: bash

    $ pip install jupyter pandas vega
    $ jupyter nbextension install --sys-prefix --py vega # not needed in notebook >= 5.3


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

Displaying in JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~~
JupyterLab version 1.0 and later includes built-in support for Altair 3 charts
(If you are using older versions of Altair, they will work with JupyterLab
versions between 0.32 and 0.35).

These will work out of the box with Altair imported as::

    import altair as alt

The Vega jupyterlab extension is included with the main jupyterlab installation,
so no additional steps are necessary.

.. _display-nteract:

Displaying in nteract
~~~~~~~~~~~~~~~~~~~~~

Current versions of nteract have Vega and Vega-Lite built-in, and will render
Altair plots without any extra configuration.

.. _display-colab:

Displaying in Colab
~~~~~~~~~~~~~~~~~~~
Google's Colab is a cloud-based notebook backed by Google Drive.
Colab comes with Altair pre-installed and with the ``'colab'`` renderer
enabled, so Altair will work out-of-the-box.

.. _display-general:

Working in non-Notebook Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Vega-Lite specifications produced by Altair can be produced in any Python
environment, but to render these specifications currently requires a javascript
engine. For this reason, Altair works most seamlessly with the browser-based
environments mentioned above.

If you would like to render plots from another Python interface that does not
have a built-in javascript engine, you'll need to somehow connect your charts
to a second tool that can execute javascript.

There are a few options available for this:

Built-in ``serve()`` method
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Altair includes a :meth:`Chart.serve` method which will seamlessly convert a
chart to HTML, start a webserver serving that HTML, and open your system's
default web browser to view it.

For example, you can serve a chart to a web browser like this::

    import altair as alt

    # load a simple dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

    chart.serve()

The command will block the Python interpreter, and will have to be canceled with
``Ctrl-C`` to execute any further code.

Manual ``save()`` and display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you would prefer, you can manually save your chart as html and open it with
a web browser. Once you have created your chart, run::

    chart.save('filename.html')

and use a web browser to open this file.

The Vegascope Renderer
~~~~~~~~~~~~~~~~~~~~~~
The `VegaScope`_ project provides an Altair renderer that works seamlessly with
the IPython terminal. Start by installing the package::

    $ pip install vegascope

Now in your Python script you can enable the vegascope renderer::

    import altair as alt
    alt.renderers.enable('vegascope')

    # load a simple dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

In an IPython environment, this will automatically trigger vegascope to serve
the chart in a background process to your web browser, and unlike Altair's
:meth:`Chart.serve` method, any subsequently created charts will use
the same server.

If you are in a non-IPython environment, you can trigger the renderer manually
using the :meth:`Chart.display` method::

   chart.display()

.. _entrypoints: https://github.com/takluyver/entrypoints
.. _ipyvega: https://github.com/vega/ipyvega/
.. _JupyterLab: http://jupyterlab.readthedocs.io/en/stable/
.. _nteract: https://nteract.io
.. _Colab: https://colab.research.google.com
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Vega: https://vega.github.io/vega/
.. _VegaScope: https://github.com/scikit-hep/vegascope
