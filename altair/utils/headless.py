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
from .core import write_file_or_filename


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

EXTRACT_CODE = {
'png': """
        var spec = arguments[0];
        var opt = arguments[1];
        var done = arguments[2];
        vegaEmbed('#vis', spec, opt).then(function(result){
            return result.view;
        }).then(function(view){
            return view.toCanvas();
        }).then(function(canvas){
            return canvas.toDataURL('image/png');
        }).then(done);
       """,
'svg': """
        var spec = arguments[0];
        var opt = arguments[1];
        var done = arguments[2];
        vegaEmbed('#vis', spec, opt).then(function(result){
            return result.view.toSVG();
        }).then(done);
       """}

def save_spec(spec, fp, mode=None, format=None):
    """Save a spec to file

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    fp : string or file-like object
        the filename or file object at which the result will be saved
    mode : string or None
        The rendering mode ('vega' or 'vega-lite'). If None, the mode will be
        inferred from the $schema attribute of the spec, or will default to
        'vega' if $schema is not in the spec.
    format : string (optional)
        the file format to be saved. If not specified, it will be inferred
        from the extension of filename.

    Note
    ----
    This requires the pillow, selenium, and chrome headless packages to be
    installed.
    """
    # TODO: allow package versions to be specified
    # TODO: detect & use local Jupyter caches of JS packages?

    if format is None and isinstance(fp, six.string_types):
        format = fp.split('.')[-1]

    if format not in ['png', 'svg']:
        raise NotImplementedError("save_spec only supports 'svg' and 'png'")

    webdriver = attempt_import('selenium.webdriver',
                               'save_spec requires the selenium package')
    Options = attempt_import('selenium.webdriver.chrome.options',
                             'save_spec requires the selenium package').Options

    opt = {'renderer': 'canvas' if format == 'png' else 'svg'}
    if mode is not None:
        if mode not in ['vega', 'vega-lite']:
            raise ValueError("mode must be 'vega' or 'vega-lite'")
        opt['mode'] = mode

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # TODO: figure out how to do with without time.sleep
        import time
        try:
            fd, name = tempfile.mkstemp(suffix='.html', text=True)
            with open(name, 'w') as f:
                f.write(HTML_TEMPLATE)
            driver.get("file://" + name)
            render = driver.execute_async_script(EXTRACT_CODE[format],
                                                 spec, opt)
        finally:
            os.remove(name)
    finally:
        driver.close()

    if format == 'png':
        img_bytes = base64.decodebytes(render.split(',')[1].encode())
        write_file_or_filename(fp, img_bytes, mode='wb')
    else:
        img_bytes = render.encode()
        write_file_or_filename(fp, img_bytes, mode='wb')
