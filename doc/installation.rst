.. _Installation:

Installation
============
Altair can be installed via the Python Package Index with the following:

.. code-block:: bash

    $ pip install altair
    $ pip install --upgrade notebook
    $ jupyter nbextension install --sys-prefix --py vega

The additional commands serve to set-up the `ipyvega`_ module to automatically
render Altair plots within the Jupyter notebook (see :ref:`displaying-plots-jupyter`)
Alternatively, you can install with conda_, which handles the Jupyter notebook
setup within the single install command:

.. code-block:: bash

    $ conda install altair --channel conda-forge

Dependencies
------------

Altair has the following dependencies, all of which are installed by default
with either of the above installation commands:

- Pandas_
- Traitlets_
- IPython_

Additionally, the following optional dependencies are required to use Altair
within the Jupyter Notebook:

- `Jupyter Notebook`_
- ipyvega_

Both JupyterLab_ and nteract_ have builtin rendering for Vega-Lite, so ipyvega_
doesn't need to be installed. However, to get Altiar to emit the right data
to render in these more modern frontends, you must call the ``enable_mime_rendering``
function before trying to render a visualization:

.. code-block: Python

    from altair import enable_mime_rendering
    enable_mime_rendering()

Eventually this will not be needed, but is being provided to keep Altair working
without change in the classic Jupyter notebook.

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
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
.. _conda: http://conda.pydata.org
.. _Altair source repository: http://github.com/altair-viz/altair
.. _JupyterLab: https://github.com/jupyterlab/jupyterlab
.. _nteract: https://github.com/nteract/nteract
