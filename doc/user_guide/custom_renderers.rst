
.. _customizing-renderers:

Customizing Renderers
=====================
Renderers in Altair are all based on the mimebundle representation accessed by
the ``_repr_mimebundle_`` method of the top-level Altair objects. When you enable
a renderer, functionally what that does is to define a new kind of mimebundle
output.

The ``alt.renderers`` registry allows the user to define and enable new mimetypes
for the chart.
As a simple example, imagine we would like to add a ``plaintext`` renderer that
renders a chart description in plain text. We could do it this way::

    def plaintext_mimetype(spec):
        return {'text/plain': "description: " + spec.get('description', 'none')}

    alt.renderers.register('plaintext', plaintext_mimetype)

Now you can enable this mimetype, and then when your chart is displayed you
will see this description::

    alt.renderers.enable('plaintext')

    alt.Chart('data.txt').mark_point().encode(
        x='x:Q',
        y='y:Q'
    ).properties(
        description='This is a simple chart'
    )

.. code-block:: none

    description: This is a simple chart

This is a simple example, but it shows you the flexibility of this approach.
If you have a frontend that recognizes ``_repr_mimebundle_`` as a means of
obtaining a MIME type representation of a Python object, then you can define
a function that will process the chart content in any way before returning
any mimetype.

The renderers built-in to Altair are the following:

- ``"default"``: default rendering, using the
  ``'application/vnd.vegalite.v2+json'`` MIME type which is supported
  by JupyterLab and nteract.
- ``"jupyterlab"``: identical to ``"default"``
- ``"nteract"``: identical to ``"default"``
- ``"colab"``: renderer for Google's Colab notebook, using the
  ``"text/html"`` MIME type.
- ``"notebook"``: renderer for the classic notebook, provided by the ipyvega3_
  package
- ``"json"``: renderer that outputs the raw JSON chart specification, using the
  ``'application/json'`` MIME type.
- ``"png"``: renderer that renders and converts the chart to PNG, outputting it
  using the ``'image/png'`` MIME type.
- ``"svg"``: renderer that renders and converts the chart to an SVG image,
  outputting it using the ``'image/svg+xml'`` MIME type.


.. _ipyvega3: https://github.com/vega/ipyvega/tree/vega3
