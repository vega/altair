from __future__ import unicode_literals
import json
import jinja2


HTML_TEMPLATE = jinja2.Template("""
{%- if fullhtml -%}
<!DOCTYPE html>
<html>
<head>
{%- endif %}
  <style>
    .vega-actions a {
        margin-right: 12px;
        color: #757575;
        font-weight: normal;
        font-size: 13px;
    }
    .error {
        color: red;
    }
  </style>
{%- if not requirejs %}
  <script type="text/javascript" src="{{ base_url }}/vega@{{ vega_version }}"></script>
  {%- if mode == 'vega-lite' %}
  <script type="text/javascript" src="{{ base_url }}/vega-lite@{{ vegalite_version }}"></script>
  {%- endif %}
  <script type="text/javascript" src="{{ base_url }}/vega-embed@{{ vegaembed_version }}"></script>
{%- endif %}
{%- if fullhtml %}
{%- if requirejs %}
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js"></script>
<script>
requirejs.config({
    "paths": {
        "vega": "{{ base_url }}/vega@{{ vega_version }}?noext",
        "vega-lib": "{{ base_url }}/vega-lib?noext",
        "vega-lite": "{{ base_url }}/vega-lite@{{ vegalite_version }}?noext",
        "vega-embed": "{{ base_url }}/vega-embed@{{ vegaembed_version }}?noext",
    }
});
</script>
{%- endif %}
</head>
<body>
{%- endif %}
  <div id="{{ output_div }}"></div>
  <script>
    {%- if requirejs %}
    {%- if not fullhtml %}
    requirejs.config({
        "paths": {
            "vega": "{{ base_url }}/vega@{{ vega_version }}?noext",
            "vega-lib": "{{ base_url }}/vega-lib?noext",
            "vega-lite": "{{ base_url }}/vega-lite@{{ vegalite_version }}?noext",
            "vega-embed": "{{ base_url }}/vega-embed@{{ vegaembed_version }}?noext",
        }
    });
    {%- endif %}
    require(['vega-embed'], function(vegaEmbed){
    {%- endif %}
      var spec = {{ spec }};
      var embedOpt = {{ embed_options }};

      function showError(el, error){
          el.innerHTML = ('<div class="error" style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      }
      const el = document.getElementById('{{ output_div }}');
      vegaEmbed("#{{ output_div }}", spec, embedOpt)
        .catch(error => showError(el, error));
    {%- if requirejs %}
    });
    {%- endif %}

  </script>
{%- if fullhtml %}
</body>
</html>
{%- endif %}
"""
)


def spec_to_html(spec, mode,
                 vega_version, vegaembed_version, vegalite_version=None,
                 base_url="https://cdn.jsdelivr.net/npm/",
                 output_div='vis', embed_options=None, json_kwds=None,
                 fullhtml=True, requirejs=False):
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
        Dictionary of options to pass to the vega-embed script. Default
        entry is {'mode': mode}.
    json_kwds : dict (optional)
        Dictionary of keywords to pass to json.dumps().
    fullhtml : boolean (optional)
        If True (default) then return a full html page. If False, then return
        an HTML snippet that can be embedded into an HTML page.
    requirejs : boolean (optional)
        If False (default) then load libraries from base_url using <script>
        tags. If True, then load libraries using requirejs

    Returns
    -------
    output : string
        an HTML string for rendering the chart.
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
        raise ValueError("must specify vega-lite version for mode='vega-lite'")

    return HTML_TEMPLATE.render(spec=json.dumps(spec, **json_kwds),
                                embed_options=json.dumps(embed_options),
                                mode=mode,
                                vega_version=vega_version,
                                vegalite_version=vegalite_version,
                                vegaembed_version=vegaembed_version,
                                base_url=base_url, output_div=output_div,
                                fullhtml=fullhtml, requirejs=requirejs)
