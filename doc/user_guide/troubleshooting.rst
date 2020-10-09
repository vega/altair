.. currentmodule:: altair

.. _display-troubleshooting:

Display Troubleshooting
=======================
Altair has a number of moving parts: it creates data structures in Python, those
structures are passed to front-end renderers, and the renderers run JavaScript
code to generate the output. This complexity means that it's possible to get
into strange states where things don't immediately work as expected.

This section summarizes some of the most common problems and their solutions.

 
.. _troubleshooting-general:

General Trouble-shooting
------------------------

Chart does not display at all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Trouble-shooting Altair with JupyterLab
---------------------------------------
  
.. _jupyterlab-vega-lite-4-object:

JupyterLab: VegaLite 4 Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

JupyterLab: VegaLite 3 Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

JupyterLab: Textual Chart Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

JupyterLab: require is not defined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are using JupyterLab and see the error::

    Javascript Error: require is not defined

This likely means that you have enabled the notebook renderer, which is not
supported in JupyterLab: that is, you have somewhere run
``alt.renderers.enable('notebook')``.
JupyterLab supports Altair's default renderer, which you can re-enable using::

    alt.renderers.enable('default')


.. _troubleshooting-notebook:

Trouble-shooting Altair with Notebook
-------------------------------------

.. _notebook-vega-lite-4-object:

Notebook: VegaLite 4 object
~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Trouble-shooting Altair outside of Jupyter
------------------------------------------
If you are using Altair outside of a Jupyter notebook environment (such as a
Python or IPython terminal) charts will be displayed as a textual
representation. Rendering of Altair charts requires executing Javascript code,
which your Python terminal cannot do natively.

For recommendations on how to use Altair outside of notebook environments,
see :ref:`display-general`.


.. _`ECMAScript 6`: https://www.w3schools.com/js/js_es6.asp
.. _`Javascript Console`: https://webmasters.stackexchange.com/questions/8525/how-do-i-open-the-javascript-console-in-different-browsers
.. _Field: https://vega.github.io/vega-lite/docs/field.html