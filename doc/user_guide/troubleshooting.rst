.. _display-troubleshooting:

Display Troubleshooting
=======================
Altair has a number of moving parts: it creates data structures in Python, those
structures are passed to front-end renderers, and the renderers run JavaScript
code to generate the output. This complexity means that it's possible to get
into strange states where things don't immediately work as expected.

This section summarizes some of the most common problems and their solutions.

.. _troubleshooting-jupyterlab:

Trouble-shooting Altair with JupyterLab
---------------------------------------

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
   0.35.1

If this is the problem, then use ``pip install -U jupyterlab`` or
``conda update jupyterlab`` to update JupyterLab, depending on how you
first installed it.

*Note: until JupyterLab 1.0 is released, you will need to use the 1.0
pre-release with Altair 3. This can be installed using*::

    $ pip install -U --pre jupyterlab

.. _jupyterlab-vega-lite-2-object:

JupyterLab: VegaLite 2 Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*If you are using the Jupyter notebook rather than JupyterLab, then refer to*
:ref:`notebook-vega-lite-2-object`

If you are using JupyterLab (not Jupyter notebook) and see the following output::

    <VegaLite 2 object>

This means that you are using Altair version 2, which is not supported by newer
versions of JupyterLab. The best option is to update to Altair version 3, and
make certain you have JupyterLab version 1.0 or later.

JavaScript output is disabled in JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using JupyterLab and see the following ouput::

    JavaScript output is disabled in JupyterLab

it can mean one of two things is wrong

1. You are using an old version of Altair. JupyterLab only works with Altair
   version 2.0 or newer; you can check the altair version by executing the
   following in a notebook code cell::

       import altair as alt
       alt.__version__

   If the version is older than 2.0, then exit JupyterLab and follow the
   installation instructions at :ref:`installation-jupyterlab`.

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

.. _notebook-vega-lite-3-object:

Notebook: VegaLite 3 object
~~~~~~~~~~~~~~~~~~~~~~~~~~~
*If you are using JupyterLab rather than the Jupyter notebook, then refer to*
:ref:`jupyterlab-vega-lite-3-object`

If you are using the notebook (not JupyterLab) and see the the following output::

    <Vegalite 3 object>

it means that either:

1. You have forgotten to enable the notebook renderer. As mentioned
   in :ref:`installation-notebook`, you need to install version 2.0 or newer
   of the ``vega`` package and Jupyter extension, and then enable it using::

       import altair as alt
       alt.renderers.enable('notebook')

   in order to render charts in the classic notebook.

   If the above code gives an error::

       NoSuchEntryPoint: No 'notebook' entry point found in group 'altair.vegalite.v2.renderer'

   This means that you have not installed the vega package. If you see this error,
   please make sure to follow the standard installation instructions at
   :ref:`installation-notebook`.

2. You have too old a version of Jupyter notebook. Run::

       $ jupyter notebook --version

   and make certain you have version 5.3 or newer. If not, then update the notebook
   using either ``pip install -U jupyter notebook`` or ``conda update jupyter notebook``
   depending on how you first installed the packages.

If you have done the above steps and charts still do not render, it likely means
that you are using a different *Kernel* within your notebook. Switch to the kernel
named *Python 2* if you are using Python 2, or *Python 3* if you are using Python 3.


.. _notebook-vega-lite-2-object:

Notebook: VegaLite 2 object
~~~~~~~~~~~~~~~~~~~~~~~~~~~
*If you are using JupyterLab rather than the Jupyter notebook, then refer to*
:ref:`jupyterlab-vega-lite-2-object`

If you are using the notebook (not JupyterLab) and see the the following output::

    <Vegalite 2 object>

it usually means that you are using Altair version 2. The best option is to update
to Altair version 3 and follow the instructions at :ref:`notebook-vega-lite-3-object`.

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


.. _troubleshooting-general:

General Trouble-shooting
------------------------

Plot displays, but the content is empty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sometimes you end up with an empty plot; for example:

.. altair-plot::

    import altair as alt

    alt.Chart('nonexistent_file.csv').mark_line().encode(
        x='x:Q',
        y='y:Q',
    )

In this case, the plot was empty because the data, ``'nonexistent_file.csv'``,
does not exist, or contains a typo in the URL.

A similar blank chart results if you refer to a field that does not exist
in the data; for example:

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

For interactive charts, an empty plot can also be caused by your adblocker.
Disabling the adblocker should fix this.

Chart does not display at all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For all renderers, the chart is only displayed if the **last line of the cell
evaluates to a chart object**

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
