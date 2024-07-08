from __future__ import annotations

import json
from typing import Any, Literal

import jinja2

from altair.utils._importers import import_vl_convert, vl_version_for_vl_convert

TemplateName = Literal["standard", "universal", "inline"]
RenderMode = Literal["vega", "vega-lite"]

HTML_TEMPLATE = jinja2.Template(
    """
{%- if fullhtml -%}
<!DOCTYPE html>
<html>
<head>
{%- endif %}
  <style>
    #{{ output_div }}.vega-embed {
      width: 100%;
      display: flex;
    }

    #{{ output_div }}.vega-embed details,
    #{{ output_div }}.vega-embed details summary {
      position: relative;
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
    {%- if requirejs and not fullhtml %}
    requirejs.config({
        "paths": {
            "vega": "{{ base_url }}/vega@{{ vega_version }}?noext",
            "vega-lib": "{{ base_url }}/vega-lib?noext",
            "vega-lite": "{{ base_url }}/vega-lite@{{ vegalite_version }}?noext",
            "vega-embed": "{{ base_url }}/vega-embed@{{ vegaembed_version }}?noext",
        }
    });
    {% endif %}
    {% if requirejs -%}
    require(['vega-embed'],
    {%- else -%}
    (
    {%- endif -%}
    function(vegaEmbed) {
      var spec = {{ spec }};
      var embedOpt = {{ embed_options }};

      function showError(el, error){
          el.innerHTML = ('<div style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      }
      const el = document.getElementById('{{ output_div }}');
      vegaEmbed("#{{ output_div }}", spec, embedOpt)
        .catch(error => showError(el, error));
    }){% if not requirejs %}(vegaEmbed){% endif %};

  </script>
{%- if fullhtml %}
</body>
</html>
{%- endif %}
"""
)


HTML_TEMPLATE_UNIVERSAL = jinja2.Template(
    """
<style>
  #{{ output_div }}.vega-embed {
    width: 100%;
    display: flex;
  }

  #{{ output_div }}.vega-embed details,
  #{{ output_div }}.vega-embed details summary {
    position: relative;
  }
</style>
<div id="{{ output_div }}"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "{{ output_div }}") {
      outputDiv = document.getElementById("{{ output_div }}");
    }
    const paths = {
      "vega": "{{ base_url }}/vega@{{ vega_version }}?noext",
      "vega-lib": "{{ base_url }}/vega-lib?noext",
      "vega-lite": "{{ base_url }}/vega-lite@{{ vegalite_version }}?noext",
      "vega-embed": "{{ base_url }}/vega-embed@{{ vegaembed_version }}?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "{{vega_version}}")
        .then(() => maybeLoadScript("vega-lite", "{{vegalite_version}}"))
        .then(() => maybeLoadScript("vega-embed", "{{vegaembed_version}}"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({{ spec }}, {{ embed_options }});
</script>
"""
)


# This is like the HTML_TEMPLATE template, but includes vega javascript inline
# so that the resulting file is not dependent on external resources. This was
# ported over from altair_saver.
#
# implies requirejs=False and full_html=True
INLINE_HTML_TEMPLATE = jinja2.Template(
    """\
<!DOCTYPE html>
<html>
<head>
  <style>
    #{{ output_div }}.vega-embed {
      width: 100%;
      display: flex;
    }

    #{{ output_div }}.vega-embed details,
    #{{ output_div }}.vega-embed details summary {
      position: relative;
    }
  </style>
  <script type="text/javascript">
    // vega-embed.js bundle with Vega-Lite version v{{ vegalite_version }}
    {{ vegaembed_script }}
  </script>
</head>
<body>
<div class="vega-visualization" id="{{ output_div }}"></div>
<script type="text/javascript">
  const spec = {{ spec }};
  const embedOpt = {{ embed_options }};
  vegaEmbed('#{{ output_div }}', spec, embedOpt).catch(console.error);
</script>
</body>
</html>
"""
)


TEMPLATES: dict[TemplateName, jinja2.Template] = {
    "standard": HTML_TEMPLATE,
    "universal": HTML_TEMPLATE_UNIVERSAL,
    "inline": INLINE_HTML_TEMPLATE,
}


def spec_to_html(
    spec: dict[str, Any],
    mode: RenderMode,
    vega_version: str | None,
    vegaembed_version: str | None,
    vegalite_version: str | None = None,
    base_url: str = "https://cdn.jsdelivr.net/npm",
    output_div: str = "vis",
    embed_options: dict[str, Any] | None = None,
    json_kwds: dict[str, Any] | None = None,
    fullhtml: bool = True,
    requirejs: bool = False,
    template: jinja2.Template | TemplateName = "standard",
) -> str:
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
    template : jinja2.Template or string (optional)
        Specify the template to use (default = 'standard'). If template is a
        string, it must be one of {'universal', 'standard', 'inline'}. Otherwise, it
        can be a jinja2.Template object containing a custom template.

    Returns
    -------
    output : string
        an HTML string for rendering the chart.
    """
    embed_options = embed_options or {}
    json_kwds = json_kwds or {}

    mode = embed_options.setdefault("mode", mode)

    if mode not in {"vega", "vega-lite"}:
        msg = "mode must be either 'vega' or 'vega-lite'"
        raise ValueError(msg)

    if vega_version is None:
        msg = "must specify vega_version"
        raise ValueError(msg)

    if vegaembed_version is None:
        msg = "must specify vegaembed_version"
        raise ValueError(msg)

    if mode == "vega-lite" and vegalite_version is None:
        msg = "must specify vega-lite version for mode='vega-lite'"
        raise ValueError(msg)

    render_kwargs = {}
    if template == "inline":
        vlc = import_vl_convert()
        vl_version = vl_version_for_vl_convert()
        render_kwargs["vegaembed_script"] = vlc.javascript_bundle(vl_version=vl_version)

    jinja_template = TEMPLATES.get(template, template)  # type: ignore[arg-type]
    if not hasattr(jinja_template, "render"):
        msg = f"Invalid template: {jinja_template}"
        raise ValueError(msg)

    return jinja_template.render(
        spec=json.dumps(spec, **json_kwds),
        embed_options=json.dumps(embed_options),
        mode=mode,
        vega_version=vega_version,
        vegalite_version=vegalite_version,
        vegaembed_version=vegaembed_version,
        base_url=base_url,
        output_div=output_div,
        fullhtml=fullhtml,
        requirejs=requirejs,
        **render_kwargs,
    )
