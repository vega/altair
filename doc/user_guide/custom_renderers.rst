
.. _customizing-renderers:

Customizing Renderers
=====================
A renderer, as introduced in :ref:`renderers`, is a function that accepts a Vega-Lite or Vega
visualization specification as a Python ``dict``, and returns a Python ``dict``
in Jupyter's `MIME Bundle format
<https://jupyter-client.readthedocs.io/en/stable/messaging.html#display-data>`_. 
This dictionary will be returned by a charts ``_repr_mimebundle_`` method.

The keys of the MIME bundle should be MIME types (such as ``image/png``) and the
values should be the data for that MIME type (text, base64 encoded binary or
JSON). Altair's default ``html`` renderer returns a cross-platform HTML representation using
the ``"text/html"`` mimetype; schematically it looks like this::

    def default_renderer(spec):
        bundle = {'text/html': generate_html(spec)}
        metadata = {}
        return bundle, metadata


If a renderer needs to do custom display logic that doesn't use the frontend's display
system, it can also return an empty MIME bundle dict::

    def empty_bundle_renderer(spec):
        # Custom display logic that uses the spec
        ...
        # Return empty MIME bundle
        return {}

As a simple example of a custom renderer, imagine we would like to add a ``plaintext`` renderer that
renders a chart description in plain text. We could do it this way::

    def plaintext_mimetype(spec):
        return {'text/plain': "description: " + spec.get('description', 'none')}

    alt.renderers.register('plaintext', plaintext_mimetype)

The ``alt.renderers`` registry allows the user to define and enable new renderers. 
Now you can enable this mimetype and then when your chart is displayed you
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
