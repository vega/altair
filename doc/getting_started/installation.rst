.. _installation:

Installation
============

.. note::

   Altair version 2.0 requires Python 3.5 or later.
   It does not work with Python 2.

Altair can be installed via `pip` with the following:

.. code-block:: bash

    $ pip install altair

Or you use conda to install Altair:

.. code-block:: bash

    $ conda install altair --channel conda-forge

To display plots, Altair relies on the `Vega-Lite`_ and `Vega`_
javascript libraries.
Different user interfaces, such as the classic `Jupyter Notebook`_,
`JupyterLab`_, and `nteract`_, offer built-in or separate third-party packages
for rendering Vega-Lite and Vega.

For information about these renderers,
see the :ref:`displaying-charts` section of the documentation.

Dependencies
------------

Altair has the following dependencies, all of which are installed by default
with either of the above installation commands:

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
