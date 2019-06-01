.. currentmodule:: altair

.. _user-guide-internals:

Altair Internals: Understanding the Library
===========================================
This section will provide some details about how the Altair API relates to the
Vega-Lite visualization specification, and how you can use that knowledge to
use the package more effectively.

First of all, it is important to realize that when stripped down to its core,
Altair itself cannot render visualizations. Altair is an API that does one
very well-defined thing:

- **Altair provides a Python API for generating validated Vega-Lite specifications**

That's it. In order to take those specifications and turn them into actual
visualizations requires a frontend that is correctly set up, but strictly
speaking that rendering is generally not controlled by the Altair package.

Altair chart to Vega-Lite Spec
------------------------------
Since Altair is fundamentally about constructing chart specifications, the central
functionality of any chart object are the :meth:`~Chart.to_dict` and
:meth:`~Chart.to_json` methods, which output the chart specification as a Python
dict or JSON string, respectively. For example, here is a simple scatter chart,
from which we can output the JSON representation:

.. altair-plot::
    :output: stdout

    import altair as alt
    from vega_datasets import data

    chart = alt.Chart(data.cars.url).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
    ).configure_view(
        height=300,
        width=400,
    )

    print(chart.to_json(indent=2))

Before returning the dict or JSON output, Altair validates it against the
`Vega-Lite schema <https://github.com/vega/schema>`_ using the
`jsonschema <https://python-jsonschema.readthedocs.io/en/latest/>`_ package.
The Vega-Lite schema defines valid attributes and values that can appear
within the specification of a Vega-Lite chart.

With the JSON schema in hand, it can then be passed to a library such as
`Vega-Embed <https://github.com/vega/vega-embed>`_ that knows how to read the
specification and render the chart that it describes, and the result is the
following visualization:

.. altair-plot::
   :hide-code:

   chart

Whenever you use Altair within JupyterLab, Jupyter notebook, or other frontends,
it is frontend extensions that extract the JSON output from the Altair chart
object and pass that specification along to the appropriate rendering code.

Altair's Low-Level Object Structure
-----------------------------------
The standard API methods used in Altair (e.g. :meth:`~Chart.mark_point`,
:meth:`~Chart.encode`, ``configure_*()``, ``transform_*()``, etc.)
are higher-level convenience functions that wrap the low-level API.
That low-level API is essentially a Python object hierarchy that mirrors
that of the JSON schema definition.

For example, we can choose to avoid the convenience methods and rather construct
the above chart using these low-level object types directly:

.. altair-plot::

    alt.Chart(
        data=alt.UrlData(
            url='https://vega.github.io/vega-datasets/data/cars.json'
        ),
        mark='point',
        encoding=alt.FacetedEncoding(
            x=alt.PositionFieldDef(
                field='Horsepower',
                type='quantitative'
            ),
            y=alt.PositionFieldDef(
                field='Miles_per_Gallon',
                type='quantitative'
            ),
            color=alt.StringFieldDefWithCondition(
                field='Origin',
                type='nominal'
            )
        ),
        config=alt.Config(
            view=alt.ViewConfig(
                height=300,
                width=400
            )
        )
    )

This low-level approach is much more verbose than the typical idiomatic approach
to creating Altair charts, but it makes much more clear the mapping between
Altair's python object structure and Vega-Lite's schema definition structure.

One of the nice features of Altair is that this low-level object hierarchy is not
constructed by hand, but rather *programmatically generated* from the Vega-Lite
schema, using the ``generate_schema_wrapper.py`` script that you can find in
`Altair's repository <https://github.com/altair-viz/altair/blob/master/tools/generate_schema_wrapper.py>`_.
This auto-generation of code propagates descriptions from the vega-lite schema
into the Python class docstrings, from which the
`API Reference <http://altair-viz.github.io/user_guide/API.html>`_
within Altair's documentation are in turn automatically generated.
This means that as the Vega-Lite schema evolves, Altair can very quickly be brought
up-to-date, and only the higher-level chart methods need to be updated by hand.

Converting Vega-Lite to Altair
------------------------------
With this knowledge in mind, and with a bit of practice, it is fairly
straightforward to construct an Altair chart from a Vega-Lite spec.
For example, consider the
`Simple Bar Chart <https://vega.github.io/vega-lite/examples/bar.html>`_ example
from the Vega-Lite documentation, which has the following JSON specification::

    {
      "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
      "description": "A simple bar chart with embedded data.",
      "data": {
        "values": [
          {"a": "A","b": 28}, {"a": "B","b": 55}, {"a": "C","b": 43},
          {"a": "D","b": 91}, {"a": "E","b": 81}, {"a": "F","b": 53},
          {"a": "G","b": 19}, {"a": "H","b": 87}, {"a": "I","b": 52}
        ]
      },
      "mark": "bar",
      "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"}
      }
    }

At the lowest level, we can use the :meth:`~Chart.from_json` class method to
construct an Altair chart object from this string of Vega-Lite JSON:

.. altair-plot::

    import altair as alt

    alt.Chart.from_json("""
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
      "description": "A simple bar chart with embedded data.",
      "data": {
        "values": [
          {"a": "A","b": 28}, {"a": "B","b": 55}, {"a": "C","b": 43},
          {"a": "D","b": 91}, {"a": "E","b": 81}, {"a": "F","b": 53},
          {"a": "G","b": 19}, {"a": "H","b": 87}, {"a": "I","b": 52}
        ]
      },
      "mark": "bar",
      "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"}
      }
    }
    """)

Likewise, if you have the Python dictionary equivalent of the JSON string,
you can use the :meth:`~Chart.from_dict` method to construct the chart object:

.. altair-plot::

    import altair as alt

    alt.Chart.from_dict({
      "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
      "description": "A simple bar chart with embedded data.",
      "data": {
        "values": [
          {"a": "A","b": 28}, {"a": "B","b": 55}, {"a": "C","b": 43},
          {"a": "D","b": 91}, {"a": "E","b": 81}, {"a": "F","b": 53},
          {"a": "G","b": 19}, {"a": "H","b": 87}, {"a": "I","b": 52}
        ]
      },
      "mark": "bar",
      "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"}
      }
    })

With a bit more effort and some judicious copying and pasting, we can
manually convert this into more idiomatic Altair code for the same chart,
including constructing a Pandas dataframe from the data values:

.. altair-plot::

    import altair as alt
    import pandas as pd

    data = pd.DataFrame.from_records([
          {"a": "A","b": 28}, {"a": "B","b": 55}, {"a": "C","b": 43},
          {"a": "D","b": 91}, {"a": "E","b": 81}, {"a": "F","b": 53},
          {"a": "G","b": 19}, {"a": "H","b": 87}, {"a": "I","b": 52}
        ])

    alt.Chart(data).mark_bar().encode(
        x='a:O',
        y='b:Q'
    )

The key is to realize that ``"encoding"`` properties are usually set using the
:meth:`~Chart.encode` method, encoding types are usually computed from
short-hand type codes, ``"transform"`` and ``"config"`` properties come from
the ``transform_*()`` and ``configure_*()`` methods, and so on.

This approach is the process by which Altair contributors constructed many
of the initial examples in the
`Altair Example Gallery <https://altair-viz.github.io/gallery/index.html>`_,
drawing inspiration from the
`Vega-Lite Example Gallery <https://vega.github.io/vega-lite/examples/>`_.
Becoming familiar with the mapping between Altair and Vega-Lite at this level
is useful in making use of the Vega-Lite documentation in places where Altair's
documentation is weak or incomplete.
