.. _Installation:

Installation
============
Altair can be installed via the Python Package Index with the following::

    pip install altair
    pip install --upgrade notebook
    jupyter nbextension install --sys-prefix --py vega

The additional commands serve to set-up the Jupyter notebook to automatically
render Altair plots.
Alternatively, you can install with conda_, which handles the Jupyter notebook
setup within the single install command::

    conda install altair --channel conda-forge

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

Development Install
-------------------
The `Altair source repository`_ is available on github.
Once you have cloned the repository, run the following command from the root of
the repository to install the master version of Altair::

    pip install -e .

If you do not wish to clone the source repository, you can install using::

    pip install git+https://github.com/ellisonbg/altair


.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Pandas: http://pandas.pydata.org
.. _traitlets: https://github.com/ipython/traitlets
.. _IPython: https://github.com/ipython/ipython
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
.. _conda: http://conda.pydata.org
.. _Altair source repository: http://github.com/ellisonbg/altair
