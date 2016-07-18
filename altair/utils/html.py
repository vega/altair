import json


def to_html(json_dict, template=None, title=None, local_file=True, **kwargs):
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
    local_file: bool
        A boolean indicating if a local HTML document is being viewed (and
        no web server being run). If True (default), the required CDNs are
        loaded over HTTP.

    Returns
    -------
    html : string
        A string of HTML representing the chart
    """
    if template is None:
        template = DEFAULT_TEMPLATE
    if title is None:
        title = "Vega-Lite Chart"
    cdn_load = "http://" if local_file else "//"
    spec = json.dumps(json_dict, indent=4)
    return template.format(spec=spec, title=title, cdn_load=cdn_load, **kwargs)


DEFAULT_TEMPLATE = """
<!DOCTYPE html>
<head>
  <title>{title}</title>
  <meta charset="utf-8">

  <script src="{cdn_load}d3js.org/d3.v3.min.js"></script>
  <script src="{cdn_load}vega.github.io/vega/vega.js"></script>
  <script src="{cdn_load}vega.github.io/vega-lite/vega-lite.js"></script>
  <script src="{cdn_load}vega.github.io/vega-editor/vendor/vega-embed.js" charset="utf-8"></script>

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
