"""
Utilities that use selenium + chrome headless to save figures
"""

import base64
import io
import json
import os
import tempfile

import six

from .importing import attempt_import


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Embedding Vega-Lite</title>
  <script src="https://cdn.jsdelivr.net/npm/vega@3.0.10"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@2.1.3"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@3.0.0"></script>
</head>
<body>
  <div id="vis"></div>
</body>
</html>
"""

EMBED_CODE = """
vegaEmbed("#vis", {spec}).then(function(result) {{
    window.view = result.view;
}}).catch(console.error);
"""

CONVERT_CODE = """
window.view.toCanvas().then(function(canvas) {
    window.png_render = canvas.toDataURL('image/png');
})
"""

EXTRACT_CODE = """
return window.png_render;
"""

def save_spec(spec, fp, mode='vega-lite', format=None):
    """Save a spec to file

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    fp : string or file-like object
        the filename or file object at which the result will be saved
    mode : string
        Whether the spec is 'vega' or 'vega-lite'.
        Currently only mode='vega-lite' is supported.
    format : string (optional)
        the file format to be saved. If not specified, it will be inferred
        from the extension of filename

    Note
    ----
    This requires the pillow, selenium, and chrome headless packages to be
    installed.
    """
    # TODO: remove PIL dependency?
    # TODO: use SVG renderer when it makes sense
    # TODO: support mode='vega'
    # TODO: allow package versions to be specified
    # TODO: detect & use local Jupyter caches of JS packages?

    if format is None and isinstance(fp, six.string_types):
        format = fp.split('.')[-1]

    if format != 'png':
        raise NotImplementedError("Only 'png' format is supported")

    Image = attempt_import('PIL.Image',
                           'save_spec requires the pillow package')
    webdriver = attempt_import('selenium.webdriver',
                               'save_spec requires the selenium package')
    Options = attempt_import('selenium.webdriver.chrome.options',
                             'save_spec requires the selenium package').Options

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            fd, name = tempfile.mkstemp(suffix='.html', text=True)
            with open(name, 'w') as f:
                f.write(HTML_TEMPLATE)
            driver.get("file://" + name)
            driver.execute_script(EMBED_CODE.format(spec=json.dumps(spec)))
            driver.execute_script(CONVERT_CODE)
            png_base64 = driver.execute_script(EXTRACT_CODE)
        finally:
            os.remove(name)
    finally:
        driver.close()

    png_bytes = base64.decodebytes(png_base64.split(',')[1].encode())

    if isinstance(fp, six.string_types):
        with open(fp, 'wb') as f:
            f.write(png_bytes)
    else:
        fp.write(png_bytes)
