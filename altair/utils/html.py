import json


HTML_TEMPLATE = {
'vega-lite': """
<!DOCTYPE html>
<html>
<head>
  <script src="{base_url}/vega@{vega_version}"></script>
  <script src="{base_url}/vega-lite@{vegalite_version}"></script>
  <script src="{base_url}/vega-embed@{vegaembed_version}"></script>
</head>
<body>
  <div id="vis"></div>
  <script type="text/javascript">
    var spec = {spec};
    var opt = {embed_opt};
    vegaEmbed("#vis", spec, opt);
  </script>
</body>
</html>
""",

'vega': """
<!DOCTYPE html>
<html>
<head>
  <script src="{base_url}/vega@{vega_version}"></script>
  <script src="{base_url}/vega-embed@{vegaembed_version}"></script>
</head>
<body>
  <div id="vis"></div>
  <script type="text/javascript">
    var spec = {spec};
    var opt = {embed_opt};
    vegaEmbed("#vis", spec, opt);
  </script>
</body>
</html>
"""}


def spec_to_html_mimebundle(spec, mode,
                            vega_version,
                            vegaembed_version,
                            vegalite_version=None,
                            base_url="https://cdn.jsdelivr.net/npm/",
                            opt=None, json_kwds=None):
    """Conver a vega/vega-lite specification to a PNG/SVG image

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    mode : string {'vega' | 'vega-lite'}
        The rendering mode.
    vega_version : string
        For html output, the version of vega.js to use
    vegalite_version : string
        For html output, the version of vegalite.js to use
    vegaembed_version : string
        For html output, the version of vegaembed.js to use
    base_url : string (optional)
        The base url from which to load the javascript libraries
    opt : dict (optional)
        Dictionary of options to pass to the renderer
    json_kwds : dict (optional)

    Returns
    -------
    output : dict
        a mime-bundle representing the image
    """
    opt = opt or {}
    json_kwds = json_kwds or {}
    template = HTML_TEMPLATE[mode]
    opt['mode'] = mode
    spec_html = template.format(spec=json.dumps(spec, **json_kwds),
                                embed_opt=json.dumps(opt),
                                vega_version=vega_version,
                                vegalite_version=vegalite_version,
                                vegaembed_version=vegaembed_version,
                                base_url=base_url)
    return {'text/html': spec_html}
