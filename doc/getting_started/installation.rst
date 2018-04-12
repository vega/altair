.. _installation:

Installation
============

To use Altair for visualization, you need to install two sets of tools

1. The core Altair Package and its dependencies

2. The renderer for the frontend you wish to use (i.e. `Jupyter Notebook`_,
   `JupyterLab`_, `Colab`_, or `nteract`_)

See the following instructions for your chosen frontend:

- :ref:`installation-jupyterlab`
- :ref:`installation-notebook`
- :ref:`installation-colab`

.. _installation-jupyterlab:

Quick Start: Altair + JupyterLab
--------------------------------
We recommend installing Altair with JupyterLab. If you would like to use it
with the classic notebook, see :ref:`installation-notebook`.

To install JupyterLab and Altair with pip, run the following commands::

    $ pip install jupyterlab altair
    $ jupyter labextension install @jupyterlab/vega3-extension  # not needed for JupyterLab 0.32 or newer

Once this is finished, run::

    $ jupyter lab

In the browser window that launches, under "Notebook" click the first available
kernel (it should say "Python 2" or "Python 3" depending on which Python version
you are running).

In the notebook that opens, you can run the following code to ensure everything
is properly set up:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalLength',
        y='petalWidth',
        color='species'
    )

If the plot does not render, ensure you have installed the exact versions
mentioned above, and if it still does not work see
:ref:`troubleshooting-jupyterlab` for help.

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.


.. _installation-notebook:

Quick Start: Altair + Notebook
------------------------------
Altair, the jupyter notebook, and their dependencies can be installed with ``pip``.
Note that rendering Altair plots in the notebook also requires the vega3_ package
to be installed and configured::

    $ pip install altair notebook vega3
    $ jupyter nbextension install --sys-prefix --py vega3 # not needed in notebook >= 5.3

Once the packages and extensions are installed, launch the notebook by running::

    $ jupyter notebook

In the browser window that launches, click the *New* drop-down menu and
select either "Python 2" or "Python 3", depending on which version of Python
you are using (note that the kernel you choose *must* match the kernel where
you installed the vega3 extension).

In the notebook that opens, you can run the following code to ensure everything
is properly set up:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    # for the notebook only (not for JupyterLab) run this command once per session
    alt.renderers.enable('notebook')

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalLength',
        y='petalWidth',
        color='species'
    )

.. note::

    For the classic Jupyter notebook (not JupyterLab), each time you launch a
    notebook you must explicitly enable Altair rendering by running::

        alt.renderers.enable('notebook')

    If you neglect this step, charts will not be rendered, but instead
    displayed as a textual representation.

If the plot does not render, ensure you have installed the exact versions
mentioned above, and if it still does not work see
:ref:`troubleshooting-notebook` for help.

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.

.. _installation-colab:

Quick Start: Altair + Colab
---------------------------
Altair can be used directly in Google's Colab_. Open a notebook, and run the
following in a notebook cell:

.. code-block::

    !pip install altair
    import altair as alt
    # for colab only run this command once per session
    alt.renderers.enable('colab')

Once you have run this, paste the following code to check if renderings are working
correctly:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalLength',
        y='petalWidth',
        color='species'
    )

If the plot does not render, ensure you have installed the exact versions
mentioned above, and if it still does not work see
:ref:`display-troubleshooting` for help.

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.

.. _installation-with-conda:

Installation with Conda
-----------------------
If you wish to use conda instead of pip to install Altair and related packages,
the ``conda-forge`` channel is the best option. Simply the above ``pip install``
commands with the equivalent ``conda install`` commands.


.. _install-dependencies:

Dependencies
------------

Altair has the following dependencies, all of which are installed automatically
with the above installation commands:

- python 2.7, 3.5 or newer
- entrypoints_
- IPython_
- jsonschema_
- NumPy_
- Pandas_
- Six_
- Toolz_
- vega_datasets_


Development Install
-------------------

The `Altair source repository`_ is available on GitHub. Once you have cloned the
repository and installed all the above dependencies, run the following command
from the root of the repository to install the master version of Altair:

.. code-block:: bash

    $ pip install -e .

If you do not wish to clone the source repository, you can install the
development version directly from GitHub using:

.. code-block:: bash

    $ pip install git+https://github.com/altair-viz/altair


.. _entrypoints: https://github.com/takluyver/entrypoints
.. _IPython: https://github.com/ipython/ipython
.. _jsonschema: https://github.com/Julian/jsonschema
.. _NumPy: http://www.numpy.org/
.. _Pandas: http://pandas.pydata.org
.. _Six: http://six.readthedocs.io/
.. _Toolz: https://github.com/pytoolz/toolz
.. _vega_datasets: https://github.com/altair-viz/vega_datasets

.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Vega: https://vega.github.io/vega/
.. _conda: http://conda.pydata.org
.. _Altair source repository: http://github.com/altair-viz/altair
.. _JupyterLab: http://jupyterlab.readthedocs.io/en/stable/
.. _Colab: https://colab.research.google.com
.. _nteract: https://nteract.io
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
.. _vega3: https://pypi.python.org/pypi/vega3/
