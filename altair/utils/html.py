from __future__ import unicode_literals
import json


TOP = """
<!DOCTYPE html>
<html>
<head>
  <style>
    .vega-actions a {{
        margin-right: 12px;
        color: #757575;
        font-weight: normal;
        font-size: 13px;
    }}
    .error {{
        color: red;
    }}
  </style>
"""

VEGA_SCRIPTS = """
<script src="{base_url}/vega@{vega_version}"></script>
<script src="{base_url}/vega-embed@{vegaembed_version}"></script>
"""

VEGALITE_SCRIPTS = """
<script src="{base_url}/vega@{vega_version}"></script>
<script src="{base_url}/vega-lite@{vegalite_version}"></script>
<script src="{base_url}/vega-embed@{vegaembed_version}"></script>
"""

BOTTOM = """
</head>
<body>
  <div id="{output_div}"></div>
  <script type="text/javascript">
    var spec = {spec};
    var embed_opt = {embed_opt};

    function showError(el, error){{
        el.innerHTML = ('<div class="error">'
                        + '<p>JavaScript Error: ' + error.message + '</p>'
                        + "<p>This usually means there's a typo in your chart specification. "
                        + "See the javascript console for the full traceback.</p>"
                        + '</div>');
        throw error;
    }}
    const el = document.getElementById('{output_div}');
    vegaEmbed("#{output_div}", spec, embed_opt)
      .catch(error => showError(el, error));
  </script>
</body>
</html>
"""


HTML_TEMPLATE = {
  'vega-lite': TOP + VEGALITE_SCRIPTS + BOTTOM,
  'vega': TOP + VEGA_SCRIPTS + BOTTOM
}


def spec_to_html(spec, mode,
                 vega_version, vegaembed_version, vegalite_version=None,
                 base_url="https://cdn.jsdelivr.net/npm/",
                 output_div='vis', embed_options=None, json_kwds=None):
    """Embed a Vega/Vega-Lite spec into an HTML page

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec.
    mode : string {'vega' | 'vega-lite'}
        The rendering mode. This value is overridden by embed_options['mode'],
        if it is present.
    vega_version : string
        For html output, the version of vega.js to use.
    vegalite_version : string
        For html output, the version of vegalite.js to use.
    vegaembed_version : string
        For html output, the version of vegaembed.js to use.
    base_url : string (optional)
        The base url from which to load the javascript libraries.
    output_div : string (optional)
        The id of the div element where the plot will be shown.
    embed_options : dict (optional)
        Dictionary of options to pass to the vega-embed script.
    json_kwds : dict (optional)
        Dictionary of keywords to pass to json.dumps().

    Returns
    -------
    output : dict
        a mime-bundle representing the image
    """
    embed_options = embed_options or {}
    json_kwds = json_kwds or {}

    mode = embed_options.setdefault('mode', mode)

    if mode not in ['vega', 'vega-lite']:
        raise ValueError("mode must be either 'vega' or 'vega-lite'")

    if vega_version is None:
        raise ValueError("must specify vega_version")

    if vegaembed_version is None:
        raise ValueError("must specify vegaembed_version")

    if mode == 'vega-lite' and vegalite_version is None:
        raise ValueError("must specify vega-lite version")

    template = HTML_TEMPLATE[mode]

    spec_html = template.format(spec=json.dumps(spec, **json_kwds),
                                embed_opt=json.dumps(embed_options),
                                vega_version=vega_version,
                                vegalite_version=vegalite_version,
                                vegaembed_version=vegaembed_version,
                                base_url=base_url,
                                output_div=output_div)
    return spec_html
