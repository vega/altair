"""
Utilities that use selenium + chrome headless to save figures
"""

import base64
import io
import json
import os
import tempfile

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

def save_spec(spec, filename, format=None, mode='vega-lite'):
    """Save a spec to file

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    filename : string
        the filename at which the result will be saved
    format : string (optional)
        the file format to be saved. If not specified, it will be inferred
        from the extension of filename
    mode : string
        Whether the spec is 'vega' or 'vega-lite'.
        Currently only mode='vega-lite' is supported.

    Note
    ----
    This requires the pillow, selenium, and chrome headless packages to be
    installed.
    """
    # TODO: remove PIL dependency?
    # TODO: use SVG renderer when it makes sense
    # TODO: support mode='vega'
    # TODO: allow package versions to be specified
    # TODO: detect local Jupyter caches of JS packages?

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

    out = io.BytesIO()
    metadata, image = png_base64.split(',')
    base64.decode(io.BytesIO(image.encode()), out)
    out.seek(0)
    image = Image.open(out)
    image.save(filename)
