import json

from .. import urls


def to_html(json_dict,
            template=None, title=None,
            d3_js_url=urls.D3_JS_URL,
            vega_js_url=urls.VEGA_JS_URL,
            vegalite_js_url=urls.VEGALITE_JS_URL,
            vegaembed_js_url=urls.VEGAEMBED_JS_URL,
            **kwargs):
    """Embed a Vega-Lite JSON into an HTML document.

    Parameters
    ----------
    json_dict : dict
        A dictionary describing the Vega-Lite specification.
    template : string
        The HTML template to use. This should have a format method, which
        accepts a "spec" and "title" argument. Note that a standard Python
        format string meets these requirements.
        By default, uses DEFAULT_TEMPLATE.
    title: string
        The title to use in the document. Default is "Vega-Lite Chart"

    Returns
    -------
    html : string
        A string of HTML representing the chart
    """
    if template is None:
        template = DEFAULT_TEMPLATE
    if title is None:
        title = "Vega-Lite Chart"
    spec = json.dumps(json_dict, indent=4)
    return template.format(spec=spec, title=title,
                           d3_js_url=d3_js_url,
                           vega_js_url=vega_js_url,
                           vegalite_js_url=vegalite_js_url,
                           vegaembed_js_url=vegaembed_js_url,
                           **kwargs)


DEFAULT_TEMPLATE = """
<!DOCTYPE html>
<head>
  <title>{title}</title>
  <meta charset="utf-8">

  <script src="{d3_js_url}"></script>
  <script src="{vega_js_url}"></script>
  <script src="{vegalite_js_url}"></script>
  <script src="{vegaembed_js_url}" charset="utf-8"></script>

  <style media="screen">
    /* Add space between vega-embed links  */
    .vega-actions a {{
      margin-right: 5px;
    }}
  </style>
</head>
<body>
  <!-- Container for the visualization -->
  <div id="vis"></div>

  <script>
  var vlSpec = {spec}

  var embedSpec = {{
    mode: "vega-lite",  // Instruct Vega-Embed to use the Vega-Lite compiler
    spec: vlSpec
  }};

  // Embed the visualization in the container with id `vis`
  vg.embed("#vis", embedSpec, function(error, result) {{
    // Callback receiving the View instance and parsed Vega spec
    // result.view is the View, which resides under the '#vis' element
  }});
  </script>
</body>
</html>
"""
