.. _importing:

Importing Vega & Vega-Lite Versions
===================================

The main Altair API is based on version 2.X of `Vega-Lite`_. The core of the API,
found in the ``altair.vegalite.v2.schema`` module, is programmatically generated
from the Vega-Lite schema.

Altair additionally provides wrappers for several other schemas:

- Vega-Lite 1.X in ``altair.vegalite.v1``
- Vega 2.X in ``altair.vega.v2``
- Vega 3.X in ``altair.vega.v3``

So, for example, if you would like to create Altair plots targeting Vega-Lite
version 1, you can use::

    import altair.vegalite.v1 as alt

and then proceed to use the Altair version 1 API.

.. note::

  We strongly recommend all users transition to Vega-Lite 2.x and Vega 3.x.
  These versions support many new features, are more stable, and Altair 2.0
  works best with them.

Because Altair has focused primarily on the vega-lite API, the vega wrappers are
far less developed than the vega-lite wrappers, though it is possible to
create Vega plots using a very low-level Python interface that mirrors the
schema itself.


.. Vega-Lite: http://vega.github.io/vega-lite/
.. Vega: http://vega.github.io/vega/
