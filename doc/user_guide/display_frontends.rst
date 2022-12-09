.. _displaying-charts:

Displaying Altair Charts
========================

Altair produces `Vega-Lite`_ visualizations, which require a Javascript frontend to
display the charts.
Because notebook environments combine a Python backend with a Javascript frontend,
many users find them convenient for using Altair.

Altair charts work out-of-the-box on `Jupyter Notebook`_, `JupyterLab`_, `Zeppelin`_,
and related notebook environments, so long as there is a web connection to load the
required javascript libraries.

Altair can also be used with various IDEs that are enabled to display Altair charts,
and can be used offline in most platforms with an appropriate frontend extension enabled;
details are below.


.. _renderers:

Altair's Renderer Framework
---------------------------
Because different display systems have different requirements and constraints, Altair provides
an API to switch between various *renderers* to tune Altair's chart representation.
These can be chosen with the renderer registry in ``alt.renderers``.
The most used built-in renderers are:

``alt.renderers.enable('html')``
  *(the default)* Output an HTML representation of the chart. The HTML renderer works
  in JupyterLab_, `Jupyter Notebook`_, `Zeppelin`_, `VSCode-Python`_ and many related notebook frontends,
  as well as Jupyter ecosystem tools like nbviewer_ and nbconvert_ HTML output.
  It requires a web connection in order to load relevant Javascript libraries.

``alt.renderers.enable('mimetype')``
  *(default prior to Altair 4.0):* Output a vega-lite specific mimetype that can be
  interpreted by appropriate frontend extensions to display charts. This also outputs
  a PNG representation of the plot, which is useful to view plots offline or on
  platforms that don't support rendering vegaspecs, such as GitHub. It works with
  newer versions of JupyterLab_, nteract_, and `VSCode-Python`_, but does not work
  with the `Jupyter Notebook`_, or with tools like nbviewer_ and nbconvert_.

In addition, Altair includes the following renderers:

- ``"default"``, ``colab``, ``kaggle``, ``zeppelin``: identical to ``"html"``
- ``"jupyterlab"``, ``"nteract"``: identical to ``"mimetype"``
- ``"png"``: renderer that renders and converts the chart to PNG, outputting it
  using the ``'image/png'`` MIME type.
- ``"svg"``: renderer that renders and converts the chart to an SVG image,
  outputting it using the ``'image/svg+xml'`` MIME type.
- ``"json"``: renderer that outputs the raw JSON chart specification, using the
  ``'application/json'`` MIME type.

You can use ``alt.renderers.names()`` to return all registered renderers as a Python list.

Other renderers can be installed by third-party packages via Python's entrypoints_ system or you can create your own,
see :ref:`customizing-renderers`.


.. _display-jupyterlab:

Displaying in JupyterLab
------------------------
JupyterLab 1.0 and later will work with Altair's default renderer with
a live web connection: no render enable step is required.

Optionally, for offline rendering in JupyterLab, you can use the mimetype renderer::

    # Optional in JupyterLab: requires an up-to-date vega labextension.
    alt.renderers.enable('mimetype')

and ensure you have the proper version of the vega labextension installed; for
Altair 4 this can be installed with:

.. code-block:: bash

    $ jupyter labextension install @jupyterlab/vega5-extension

In JupyterLab version 2.0 or newer, this extension is installed by default, though the
version available in the JupyterLab release often takes a few months to catch up with
new Altair releases.


.. _display-notebook:

Displaying in Jupyter Notebook
------------------------------
The classic Jupyter Notebook will work with Altair's default renderer with
a live web connection: no render enable step is required.

Optionally, for offline rendering in Jupyter Notebook, you can use the notebook renderer::

    # Optional in Jupyter Notebook: requires an up-to-date vega nbextension.
    alt.renderers.enable('notebook')
    
This renderer is provided by the `ipyvega`_ notebook extension, which can be
installed and enabled either using pip:

.. code-block:: bash

    $ pip install vega

or conda:

.. code-block:: bash

    $ conda install vega --channel conda-forge

In older versions of the notebook (<5.3) you need to additionally enable the extension:

.. code-block:: bash

    $ jupyter nbextension install --sys-prefix --py vega


.. _display-nteract:

Displaying in nteract
---------------------
nteract_ cannot display HTML outputs natively, and so Altair's default ``html`` renderer
will not work. However, nteract natively includes vega and vega-lite mimetype-based rendering.
To use Altair in nteract, ensure you are using a version that supports the Vega-Lite v5
mimetype, and use::

    alt.renderers.enable('mimetype')


.. _display-vscode:

Displaying in VSCode
--------------------
`VSCode-Python`_ works with Altair's default renderer with a live web connection: no render enable step is required.

Optionally, for offline rendering, you can use the mimetype renderer::

    # Optional in VS Code
    alt.renderers.enable('mimetype')

.. _display-general:

Working in non-Notebook Environments
------------------------------------
The Vega-Lite specifications produced by Altair can be produced in any Python
environment, but to render these specifications currently requires a javascript
engine. For this reason, Altair works most seamlessly with the browser-based
environments mentioned above.

If you would like to render plots from another Python interface that does not
have a built-in javascript engine, you'll need to somehow connect your charts
to a second tool that can execute javascript.

There are a few options available for this:

Vega-enabled IDEs
~~~~~~~~~~~~~~~~~
Some IDEs have extensions that natively recognize and display Altair charts.
Examples are:

- The `VSCode-Python`_ extension, which supports native Altair and Vega-Lite
  chart display as of November 2019.
- The Hydrogen_ project, which is built on nteract_ and renders Altair charts
  via the ``mimetype`` renderer.

Altair Viewer
~~~~~~~~~~~~~
For non-notebook IDEs, a useful companion is the `Altair Viewer`_ package,
which provides an Altair renderer that works directly from any Python terminal.
Start by installing the package::

    $ pip install altair_viewer

When enabled, this will serve charts via a local HTTP server and automatically open
a browser window in which to view them, with subsequent charts displayed in the
same window.

If you are using an IPython-compatible terminal ``altair_viewer`` can be enabled via
Altair's standard renderer framework::

    import altair as alt
    alt.renderers.enable('altair_viewer')

If you prefer to manually trigger chart display, you can use the built-in :meth:`Chart.show`
method to manually trigger chart display::

    import altair as alt

    # load a simple dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

    chart.show()

This command will block the Python interpreter until the browser window containing
the chart is closed.

Manual ``save()`` and display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you would prefer, you can save your chart to a file (html, png, etc.) first and then display it.
See :ref:`user-guide-saving` for more information.

.. _entrypoints: https://github.com/takluyver/entrypoints
.. _ipyvega: https://github.com/vega/ipyvega/
.. _JupyterLab: http://jupyterlab.readthedocs.io/en/stable/
.. _nteract: https://nteract.io
.. _nbconvert: https://nbconvert.readthedocs.io/
.. _nbviewer: https://nbviewer.jupyter.org/
.. _Altair Viewer: https://github.com/altair-viz/altair_viewer/
.. _Colab: https://colab.research.google.com
.. _Hydrogen: https://github.com/nteract/hydrogen
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Vega: https://vega.github.io/vega/
.. _VSCode-Python: https://code.visualstudio.com/docs/python/python-tutorial
.. _Zeppelin: https://zeppelin.apache.org/
