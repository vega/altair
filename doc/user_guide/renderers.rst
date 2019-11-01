.. _user-guide-renderers:

Altair Renderers
----------------
In order to turn your altair chart from the JSON structure output by Altair into
a rendered visualization requires a front-end that knows how to interpret Vega
and Vega-Lite specifications. To enable a particular renderer, you can use::

    import altair as alt
    alt.renderers.enable(renderer_name)

Altair ships with the following renderers:

**JupyterLab**
  JupyterLab_ works with the default renderer, and requires no additional enable
  step. To switch back to it after another renderer has been enabled, use::

      alt.renderers.enable('jupyterlab')  # Note: identical to enable('default')

  for more details on version and system requirements, see :ref:`display-jupyterlab`.

**nteract**
  nteract_ works with the default renderer and requires no additional enable
  step. To switch back to it after another renderer has been enabled, use::

      alt.renderers.enable('nteract')  # Note: identical to enable('default')

  for more details on version and system requirements, see :ref:`display-nteract`.

**Jupyter Notebook**
  for the classic `Jupyter Notebook`_ (not JupyterLab),
  you must switch to the ``notebook`` renderer::

      alt.renderers.enable('notebook')

  Note that this requires the vega_ package; see :ref:`display-notebook`.

**Google Colab**
  Colab_ requires use of the ``colab`` renderer, which will be enabled by
  default when Altair is imported.
  To switch back to it after another renderer has been enabled, use::

      alt.renderers.enable('colab')

  For more information, see :ref:`display-colab`.

.. _JupyterLab: http://jupyterlab.readthedocs.io/en/stable/
.. _nteract: https://nteract.io
.. _Colab: https://colab.research.google.com
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/en/stable/
.. _vega: https://github.com/vega/ipyvega/tree/vega
