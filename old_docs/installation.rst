.. _Installation:

Installation
============

Altair can be installed via `pip` with the following:

.. code-block:: bash

    $ pip install altair
    $ pip install --upgrade notebook

In addition, to render Altair visualizations in the classic Jupyter Notebook,
you will need to enable the `ipyvega`_ nbextension:

.. code-block:: bash

    $ jupyter nbextension enable --sys-prefix --py vega

This single step is **not** needed for usage with JupyterLab and nteract, which have built-in
support for Vega-Lite.

If you use conda to install Altair:

.. code-block:: bash

    $ conda install altair --channel conda-forge

the nbextension is automatically enabled.

Dependencies
------------

Altair has the following dependencies, all of which are installed by default
with either of the above installation commands:

- Pandas_
- Traitlets_
- IPython_
- ipyvega_

Development Install
-------------------

The `Altair source repository`_ is available on GitHub.
Once you have cloned the repository and installed all the above dependencies,
run the following command from the root of the repository to install the
master version of Altair:

.. code-block:: bash

    $ pip install -e .

If you do not wish to clone the source repository, you can install the development
version directly from GitHub using:

.. code-block:: bash

    $ pip install git+https://github.com/altair-viz/altair


.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Pandas: http://pandas.pydata.org
.. _traitlets: https://github.com/ipython/traitlets
.. _IPython: https://github.com/ipython/ipython
.. _ipyvega: http://github.com/vega/ipyvega
.. _conda: http://conda.pydata.org
.. _Altair source repository: http://github.com/altair-viz/altair
.. _JupyterLab: https://github.com/jupyterlab/jupyterlab
.. _nteract: https://github.com/nteract/nteract
