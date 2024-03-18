.. currentmodule:: altair

.. _installation:

Installation
============

Altair can be installed, along with all its optional dependencies, using:

.. code-block:: bash

    pip install "altair[all]"

If you are using the conda_ package manager, the equivalent is:

.. code-block:: bash

    conda install -c conda-forge altair-all

At this point, you should be able to open any IDE compatible with Jupyter Notebooks,
and execute any of the code from the :ref:`example-gallery`.
For more information on how to display charts in various notebook environments
and non-notebook IDEs, see :ref:`displaying-charts`.
If you wish to install Altair with only the required dependencies,
you can omit the ``[all]``/``-all`` suffix.

Development Installation
========================

The `Altair source repository`_ is available on GitHub. Once you have cloned the
repository and installed all the above dependencies, run the following command
from the root of the repository to install the main version of Altair:

.. code-block:: bash

    pip install -e .

To install optional and development dependencies as well, run

.. code-block:: bash

    pip install -e ".[all, dev]"

If you do not wish to clone the source repository, you can install the
development version directly from GitHub using:

.. code-block:: bash

    pip install -e git+https://github.com/altair-viz/altair.git

Please see `CONTRIBUTING.md <https://github.com/altair-viz/altair/blob/main/CONTRIBUTING.md>`_
for details on how to contribute to the Altair project.

.. _conda: https://docs.conda.io/
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _vega_datasets: https://github.com/altair-viz/vega_datasets
.. _JupyterLab: http://jupyterlab.readthedocs.io/
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/
.. _Altair source repository: http://github.com/altair-viz/altair
