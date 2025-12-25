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

Altair can also be installed with just the dependencies necessary for saving charts to offline HTML files or PNG/SVG/PDF formats, using:

.. code-block:: bash

    pip install "altair[save]"

Installing Altair in WASM / Pyodide environments
-----------------------------------------------

Altair can be installed in browser-based Python environments such as
Pyodide, PyScript, or other WebAssembly (WASM) runtimes using ``micropip``.

For example, in a Pyodide-based environment:

.. code-block:: python

    import micropip
    await micropip.install("altair")

To install a specific version of Altair, specify the version explicitly:

.. code-block:: python

    await micropip.install("altair==5.3.0")

Development Installation
========================

Please see `CONTRIBUTING.md <https://github.com/vega/altair/blob/main/CONTRIBUTING.md>`_
for details on how to contribute to the Altair project.

.. _conda: https://docs.conda.io/
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _JupyterLab: http://jupyterlab.readthedocs.io/
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/
