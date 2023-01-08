.. _importing:

Importing Vega-Lite Versions
===================================

The main Altair API is based on version 5.X of `Vega-Lite`_. The core of the API,
found in the ``altair.vegalite.v5.schema`` module, is programmatically generated
from the Vega-Lite schema.

Altair additionally provides wrappers for some of the previous `Vega-Lite`_ schemas.

So, for example, if you would like to create Altair plots targeting Vega-Lite
version 3, you can use::

    import altair.vegalite.v3 as alt

and then proceed to use the Altair version 3 API.

.. note::

  We strongly recommend all users transition to Vega-Lite 5.x.
  These versions support many new features, are more stable, and Altair 5
  works best with them.

.. _Vega-Lite: http://vega.github.io/vega-lite/
