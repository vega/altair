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

``alt.renderers.enable("html")``
  *(the default)* Output an HTML representation of the chart. The HTML renderer works
  in JupyterLab_, `Jupyter Notebook`_, `Zeppelin`_, `VSCode-Python`_ and many related notebook frontends,
  as well as Jupyter ecosystem tools like nbviewer_ and nbconvert_ HTML output.
  It requires a web connection in order to load relevant Javascript libraries.

``alt.renderers.enable("mimetype")``
  *(default prior to Altair 4.0):* Output a vega-lite specific mimetype that can be
  interpreted by appropriate frontend extensions to display charts. This also outputs
  a PNG representation of the plot, which is useful to view plots offline or on
  platforms that don't support rendering vegaspecs, such as GitHub. It works with
  newer versions of JupyterLab_, nteract_, and `VSCode-Python`_, but does not work
  with the `Jupyter Notebook`_, or with tools like nbviewer_ and nbconvert_.

In addition, Altair includes the following renderers:

- ``"default"``, ``"colab"``, ``"kaggle"``, ``"zeppelin"``: identical to ``"html"``
- ``"jupyterlab"``, ``"nteract"``: identical to ``"mimetype"``
- ``"png"``: renderer that renders and converts the chart to PNG, outputting it
  using the ``"image/png"`` MIME type.
- ``"svg"``: renderer that renders and converts the chart to an SVG image,
  outputting it using the ``"image/svg+xml"`` MIME type.
- ``"json"``: renderer that outputs the raw JSON chart specification, using the
  ``"application/json"`` MIME type.

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

.. _display-troubleshooting:

Troubleshooting
---------------
Altair has a number of moving parts: it creates data structures in Python, those
structures are passed to front-end renderers, and the renderers run JavaScript
code to generate the output. This complexity means that it's possible to get
into strange states where things don't immediately work as expected.

This section summarizes some of the most common problems and their solutions.

 
.. _troubleshooting-general:

General Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~

Chart does not display at all
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are expecting a chart output and see nothing at all, it means that the
Javascript rendering libraries are not being invoked.
This can happen for several reasons:

1. You have an old browser that doesn't support JavaScript's `ECMAScript 6`_:
   in this case, charts may not display properly or at all. For example, Altair
   charts will not render in any version of Internet Explorer.
   If this is the case, you will likely see syntax errors in your browser's
   `Javascript Console`_.

2. Your browser is unable to load the javascript libraries. This may be due to
   a local firewall, an adblocker, or because your browser is offline. Check your
   browser's `Javascript Console`_  to see if there are errors.

3. You may be failing to trigger the notebook's display mechanism (see below).

If you are working in a notebook environment, the chart is only displayed if the
**last line of the cell evaluates to a chart object**

By analogy, consider the output of simple Python operations::

    >>> x = 4  # no output here
    >>> x      # output here, because x is evaluated
    4
    >>> x * 2  # output here, because the expression is evaluated
    8

If the last thing you type consists of an assignment operation, there will be no
output displayed. This turns out to be true of Altair charts as well:

.. altair-plot::
    :output: none

    import altair as alt
    from vega_datasets import data
    cars = data.cars.url

    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    )

The last statement is an assignment, so there is no output and the chart is not
shown. If you have a chart assigned to a variable, you need to end the cell with
an evaluation of that variable:

.. altair-plot::

    chart = alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    )

    chart

Alternatively, you can evaluate a chart directly, and not assign it to a variable,
in which case the object definition itself is the final statement and will be
displayed as an output:

.. altair-plot::

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    )

Plot displays, but the content is empty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sometimes charts may appear, but the content is empty; for example:

.. altair-plot::

    import altair as alt

    alt.Chart('nonexistent_file.csv').mark_line().encode(
        x='x:Q',
        y='y:Q',
    )

If this is the case, it generally means one of two things:

1. your data is specified by a URL that is invalid or inaccessible
2. your encodings do not match the columns in your data source

In the above example, ``nonexistent_file.csv`` doesn't exist, and so the chart
does not render (associated warnings will be visible in the `Javascript Console`_).

Some other specific situations that may cause this:

You have an adblocker active
  Charts that reference data by URL can sometimes trigger false positives in your
  browser's adblocker. Check your browser's `Javascript Console`_ for errors, and
  try disabling your adblocker.

You are loading data cross-domain
  If you save a chart to HTML and open it using a ``file://`` url in your browser,
  most browsers will not allow the javascript to load datasets from an ``http://``
  domain. This is a security feature in your browser that cannot be disabled.
  To view such charts locally, a good approach is to use a simple local HTTP server
  like the one provided by Python::
  
      $ python -m http.server
  
Your encodings do not match your data
  A similar blank chart results if you refer to a field that does not exist
  in the data, either because of a typo in your field name, or because the
  column contains special characters (see below).

Here is an example of a mis-specified field name leading to a blank chart:

.. altair-plot::

   import pandas as pd

   data = pd.DataFrame({'x': [1, 2, 3],
                        'y': [3, 1, 4]})

   alt.Chart(data).mark_point().encode(
       x='x:Q',
       y='y:Q',
       color='color:Q'  # <-- this field does not exist in the data!
     )
  
Altair does not check whether fields are valid, because there are many avenues
by which a field can be specified within the full schema, and it is too difficult
to account for all corner cases. Improving the user experience in this is a
priority; see https://github.com/vega/vega-lite/issues/3576.

Encodings with special characters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Vega-Lite grammar on which Altair is based allows for encoding names to use
special characters to access nested properties (See Vega-Lite's Field_ documentation).

This can lead to errors in Altair when trying to use such columns in your chart.
For example, the following chart is invalid:

.. altair-plot::

   import pandas as pd
   data = pd.DataFrame({'x.value': [1, 2, 3]})

   alt.Chart(data).mark_point().encode(
       x='x.value:Q',
   )

To plot this data directly, you must escape the period in the field name:

.. altair-plot::

   import pandas as pd
   data = pd.DataFrame({'x.value': [1, 2, 3]})

   alt.Chart(data).mark_point().encode(
       x=r'x\.value:Q',
   )

In general, it is better to avoid special characters like ``"."``, ``"["``, and ``"]"``
in your data sources where possible.

.. _troubleshooting-jupyterlab:

Troubleshooting in JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
.. _jupyterlab-vega-lite-4-object:

VegaLite 4 Object
^^^^^^^^^^^^^^^^^
*If you are using the Jupyter notebook rather than JupyterLab, then refer to*
:ref:`notebook-vega-lite-4-object`

If you are using JupyterLab (not Jupyter notebook) and see the following output::

    <VegaLite 4 object>

This means that you have enabled the ``mimetype`` renderer, but that your JupyterLab
frontend does not support the VegaLite 4 mimetype.

The easiest solution is to use the default renderer::

    alt.renderers.enable('default')

and rerun the cell with the chart.

If you would like to use the mimetype rendering with the JupyterLab frontend extension,
then make certain the extension is installed and enabled:

    $ jupyter labextension install @jupyterlab/vega5-extension

and then restart your jupyter frontend.
  
.. _jupyterlab-vega-lite-3-object:

VegaLite 3 Object
^^^^^^^^^^^^^^^^^
*If you are using the Jupyter notebook rather than JupyterLab, then refer to*
:ref:`notebook-vega-lite-3-object`

If you are using JupyterLab (not Jupyter notebook) and see the following output::

    <VegaLite 3 object>

This most likely means that you are using too old a version of JupyterLab.
Altair 3.0 or later works best with JupyterLab version 1.0 or later;
check the version with::

   $ jupyter lab --version
   1.2.0

If you have an older jupyterlab version, then use ``pip install -U jupyterlab``
or ``conda update jupyterlab`` to update JupyterLab, depending on how you
first installed it.

JavaScript output is disabled in JupyterLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using JupyterLab and see the following output::

    JavaScript output is disabled in JupyterLab

it can mean one of two things is wrong

1. You are using an old version of Altair. JupyterLab only works with Altair
   version 2.0 or newer; you can check the altair version by executing the
   following in a notebook code cell::

       import altair as alt
       alt.__version__

   If the version is older than 2.0, then exit JupyterLab and follow the
   installation instructions at :ref:`display-jupyterlab`.

2. You have enabled the wrong renderer. JupyterLab works with the default
   renderer, but if you have used ``alt.renderers.enable()`` to enable
   another renderer, charts will no longer render correctly in JupyterLab.
   You can check which renderer is active by running::

       import altair as alt
       print(alt.renderers.active)

   JupyterLab rendering will work only if the active renderer is ``"default"``
   or ``"jupyterlab"``. You can re-enable the default renderer by running::

       import altair as alt
       alt.renderers.enable('default')

   (Note that the default renderer is enabled, well, by default, and so this
   is only necessary if you've somewhere changed the renderer explicitly).

.. _jupyterlab-textual-chart-representation:

Textual Chart Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*If you are using the Notebook rather than the JupyterLab, then refer to*
:ref:`notebook-textual-chart-representation`

If you are using JupyterLab and see a textual representation of the Chart object
similar to this::

    Chart({
      data: 'https://vega.github.io/vega-datasets/data/cars.json',
      encoding: FacetedEncoding({
        x: X({
          shorthand: 'Horsepower'
        })
      }),
      mark: 'point'
    })

it probably means that you are using an older Jupyter kernel.
You can confirm this by running::

   import IPython; IPython.__version__
   # 6.2.1

Altair will not display correctly if using a kernel with IPython version 4.X or older.

The easiest way to address this is to change your kernel: choose "Kernel"->"Change Kernel"
and then use the first kernel that appears.

.. _jupyterlab-notebook-backend:

Javascript Error: require is not defined
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you are using JupyterLab and see the error::

    Javascript Error: require is not defined

This likely means that you have enabled the notebook renderer, which is not
supported in JupyterLab: that is, you have somewhere run
``alt.renderers.enable('notebook')``.
JupyterLab supports Altair's default renderer, which you can re-enable using::

    alt.renderers.enable('default')


.. _troubleshooting-notebook:

Troubleshooting in Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _notebook-vega-lite-4-object:

Notebook: VegaLite 4 object
^^^^^^^^^^^^^^^^^^^^^^^^^^^
*If you are using JupyterLab rather than the Jupyter notebook, then refer to*
:ref:`jupyterlab-vega-lite-3-object`

If you are using Jupyter Notebook (not JupyterLab) and see the following output::

    <VegaLite 4 object>

This means that you have enabled the ``mimetype`` renderer.

The easiest solution is to use the default renderer::

    alt.renderers.enable('default')

and rerun the cell with the chart.


.. _notebook-vega-lite-3-object:

Notebook: VegaLite 3 object
^^^^^^^^^^^^^^^^^^^^^^^^^^^
*If you are using JupyterLab rather than the Jupyter notebook, then refer to*
:ref:`jupyterlab-vega-lite-3-object`

If you are using the notebook (not JupyterLab) and see the the following output::

    <Vegalite 3 object>

it means that either:

1. You have forgotten to enable the notebook renderer. As mentioned
   in :ref:`display-notebook`, you need to install version 2.0 or newer
   of the ``vega`` package and Jupyter extension, and then enable it using::

       import altair as alt
       alt.renderers.enable('notebook')

   in order to render charts in the classic notebook.

   If the above code gives an error::

       NoSuchEntryPoint: No 'notebook' entry point found in group 'altair.vegalite.v2.renderer'

   This means that you have not installed the vega package. If you see this error,
   please make sure to follow the standard installation instructions at
   :ref:`display-notebook`.

2. You have too old a version of Jupyter notebook. Run::

       $ jupyter notebook --version

   and make certain you have version 5.3 or newer. If not, then update the notebook
   using either ``pip install -U jupyter notebook`` or ``conda update jupyter notebook``
   depending on how you first installed the packages.

If you have done the above steps and charts still do not render, it likely means
that you are using a different *Kernel* within your notebook. Switch to the kernel
named *Python 2* if you are using Python 2, or *Python 3* if you are using Python 3.

.. _notebook-textual-chart-representation:

Notebook: Textual Chart Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*If you are using the Notebook rather than the JupyterLab, then refer to*
:ref:`jupyterlab-textual-chart-representation`

*If you are not using a Jupyter notebook environment, then refer to*
:ref:`troubleshooting-non-notebook`.

If you are using Jupyter notebook and see a textual representation of the Chart
object similar to this::

    Chart({
      data: 'https://vega.github.io/vega-datasets/data/cars.json',
      encoding: FacetedEncoding({
        x: X({
          shorthand: 'Horsepower'
        })
      }),
      mark: 'point'
    })

it probably means that you are using an older Jupyter kernel.
You can confirm this by running::

   import IPython; IPython.__version__
   # 6.2.1

Altair will not display correctly if using a kernel with IPython version 4.X or older.

The easiest way to address this is to change your kernel:
choose "Kernel"->"Change Kernel" and then select "Python 2" or "Python 3",
depending on what version of Python you used when installing Altair.


.. _troubleshooting-non-notebook:

Troubleshooting outside of Jupyter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are using Altair outside of a Jupyter notebook environment (such as a
Python or IPython terminal) charts will be displayed as a textual
representation. Rendering of Altair charts requires executing Javascript code,
which your Python terminal cannot do natively.

For recommendations on how to use Altair outside of notebook environments,
see :ref:`display-general`.


.. _`ECMAScript 6`: https://www.w3schools.com/js/js_es6.asp
.. _`Javascript Console`: https://webmasters.stackexchange.com/questions/8525/how-do-i-open-the-javascript-console-in-different-browsers
.. _Field: https://vega.github.io/vega-lite/docs/field.html

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
