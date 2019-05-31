.. _installation:

Installation
============

To use Altair for visualization, you need to install two sets of tools

1. The core Altair Package and its dependencies

2. The renderer for the frontend you wish to use (i.e. `Jupyter Notebook`_,
   `JupyterLab`_, `Colab`_, or `nteract`_)

3. Additionally, Altair's documentation makes use of the vega_datasets_ package,
   and so it is included in the installation instructions below.

Depending on the frontend you would like to use, the instructions differ slightly.
See the following instructions for your chosen frontend:

- :ref:`installation-jupyterlab`
- :ref:`installation-notebook`
- :ref:`installation-colab`

.. _installation-jupyterlab:

Quick Start: Altair + JupyterLab
--------------------------------
We recommend installing Altair with JupyterLab. If you would like to use it
with the classic notebook, see :ref:`installation-notebook`.

Altair version 3 works best with JupyterLab version 1.0 or later.

To install JupyterLab and Altair with conda, run the following command::

    $ conda install -c conda-forge altair vega_datasets jupyterlab

To install JupyterLab and Altair with pip, run the following command::

    $ pip install -U altair vega_datasets jupyterlab

Once this is finished, run::

    $ jupyter lab

In the browser window that launches, select "File"->"New"->"Notebook" and then
click "Select" without changing the kernel  (it should say "Python 2" or
"Python 3" depending on which Python version you are running).

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

If the plot does not render, make certain you have installed the most recent
versions of the packages above, and if it still does not work see
:ref:`troubleshooting-jupyterlab` for help.

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.


.. _installation-notebook:

Quick Start: Altair + Notebook
------------------------------
Altair works in the Jupyter notebook, though we recommend using it in JupyterLab
if available (see :ref:`installation-jupyterlab`).

If using the notebook, Altair works best with notebook version 5.3 or newer.
Note that using Altair 3 in the notebook also requires version 2 or newer of
the vega_ package to be installed and configured.

To install the notebook and Altair with conda, run the following command::

    $ conda install -c conda-forge altair vega_datasets notebook vega

To install the notebook and Altair with pip, run the following command::

    $ pip install -U altair vega_datasets notebook vega

.. note::

   If you have multiple Python environments, you need to install the
   vega_ package in the Python environment that runs ipykernel *and*
   the Python environment that runs the Jupyter Notebook server.  You
   only need to install Altair in the Python environment that runs
   ipykernel.

Once the packages and extensions are installed, launch the notebook by running::

    $ jupyter notebook

In the browser window that launches, click the *New* drop-down menu and
select either "Python 2" or "Python 3", depending on which version of Python
you are using (note that the kernel you choose *must* match the kernel where
you installed the vega extension).

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

If the plot does not render, ensure you have installed the most recent versions
of the above packages, and if it still does not work see
:ref:`troubleshooting-notebook` for help.

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.

.. _installation-colab:

Quick Start: Altair + Colab
---------------------------
Altair can be used directly in Google's Colab_ with no additional setup by the
user.
Open a new Colab_ notebook, and paste the following code to confirm that
renderings are working correctly:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalLength',
        y='petalWidth',
        color='species'
    )

If the plot does not render, see :ref:`display-troubleshooting` for help.

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.

.. _install-dependencies:

Dependencies
------------

Altair has the following dependencies, all of which are installed automatically
with the above installation commands:

- python 2.7, 3.5 or newer
- entrypoints_
- jsonschema_
- NumPy_
- Pandas_
- Six_
- Toolz_

To run altair's full test suite and build Altair's documentation requires a few
additional dependencies:

- flake8
- pytest
- jinja2
- sphinx
- m2r
- docutils
- vega_datasets_
- ipython


Development Install
-------------------

The `Altair source repository`_ is available on GitHub. Once you have cloned the
repository and installed all the above dependencies, run the following command
from the root of the repository to install the master version of Altair:

.. code-block:: bash

    $ pip install -e .

To install development dependencies as well, run

.. code-block:: bash

    $ pip install -e .[dev]

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
.. _conda: http://conda.pydata.org
.. _Altair source repository: http://github.com/altair-viz/altair
.. _JupyterLab: http://jupyterlab.readthedocs.io/en/stable/
.. _Colab: https://colab.research.google.com
.. _nteract: https://nteract.io
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
.. _vega: https://pypi.python.org/pypi/vega/
