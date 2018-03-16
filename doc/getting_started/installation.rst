.. _installation:

Installation
============

.. note::

   Altair version 2.0 requires Python 3.5 or later.
   It does not work with Python 2.

To use Altair for visualization, you need to install two sets of tools

1. The core Altair Package and its dependencies

2. The renderer for the frontend you wish to use (i.e. `Jupyter Notebook`_,
   `JupyterLab`_, or `nteract`_)

Here we will briefly describe installation with JupyterLab; for the Jupyter notebook
or for nteract see :ref:`displaying-charts`.

.. warning::

   conda installation is not yet available for the version 2.0 release
   candidate. Please install the release candidate with pip.

Both Altair and JupyterLab can be installed with `pip`::

    $ pip install altair==2.0.0rc1
    $ pip install jupyterlab

or with ``conda``::

    $ conda install altair jupyterlab --channel conda-forge

For JupyterLab version 0.32 or newer, nothing else needs to be done to use
the main Altair API. For JupyterLab version 0.31, you'll additionally need to
run the following::

    $ jupyter labextension install @jupyterlab/vega3-extension

.. note::

    Using Altair in the classic Jupyter Notebook (i.e. not JupyterLab)
    requires a slightly different setup. See :ref:`displaying-charts` for
    details.

Once altair and Jupyterlab are installed, launch Jupyterlab by running::

    $ jupyter lab

This should launch a web browser window. The first time JupyterLab is launched,
you will see a *Launcher* window: Under the "Notebook" section, click "Python 3"
to launch a new notebook. Then you should be able to execute Altair code and
see the rendered charts; to try it out, you can copy, paste, and execute the
following code to make certain everythin is working correctly:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    iris = data.iris()

    alt.Chart(iris).mark_point().encode(
        x='petalLength',
        y='petalWidth',
        color='species'
    )

Once things are up and running, you may wish to go through the tutorials at
:ref:`starting` and :ref:`exploring-weather`, read through the User Guide
indexed in the left panel, or check out the :ref:`example-gallery` for more ideas.


.. _install-dependencies:

Dependencies
------------

Altair has the following dependencies, all of which are installed automatically
with the above installation commands:

- python 3.5 or higher
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
.. _nteract: https://nteract.io
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
