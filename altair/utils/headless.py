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
  <script src="https://cdn.jsdelivr.net/npm/vega@3.2"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@2.3"></script>
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
        var mode = arguments[1]
        var done = arguments[2];

        if(mode === 'vega-lite'){
          // compile vega-lite to vega
          const compiled = vl.compile(spec);
          spec = compiled.spec;
        }

        new vega.View(vega.parse(spec), {
              loader: vega.loader(),
              logLevel: vega.Warn,
              renderer: 'none',
            })
            .initialize()
            .toCanvas()
            .then(function(canvas){return canvas.toDataURL('image/png');})
            .then(done)
            .catch(function(err) { console.error(err); });
        """,
'svg': """
        var spec = arguments[0];
        var mode = arguments[1];
        var done = arguments[2];

        if(mode === 'vega-lite'){
          // compile vega-lite to vega
          const compiled = vl.compile(spec);
          spec = compiled.spec;
        }

        new vega.View(vega.parse(spec), {
              loader: vega.loader(),
              logLevel: vega.Warn,
              renderer: 'none',
            })
            .initialize()
            .toSVG()
            .then(done)
            .catch(function(err) { console.error(err); });
        """}

def save_spec(spec, fp, mode=None, format=None, driver_timeout=10):
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
    driver_timeout : int (optional)
        the number of seconds to wait for page load before raising an
        error (default: 10)

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

    if mode is None:
        if '$schema' in spec:
            mode = spec['$schema'].split('/')[-2]
        else:
            mode = 'vega'
    if mode not in ['vega', 'vega-lite']:
        raise ValueError("mode must be 'vega' or 'vega-lite'")

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.set_page_load_timeout(driver_timeout)

        try:
            fd, htmlfile = tempfile.mkstemp(suffix='.html', text=True)
            with open(htmlfile, 'w') as f:
                f.write(HTML_TEMPLATE)
            driver.get("file://" + htmlfile)
            render = driver.execute_async_script(EXTRACT_CODE[format],
                                                 spec, mode)
        finally:
            os.remove(htmlfile)
    finally:
        driver.close()

    if format == 'png':
        img_bytes = base64.decodebytes(render.split(',')[1].encode())
        write_file_or_filename(fp, img_bytes, mode='wb')
    else:
        img_bytes = render.encode()
        write_file_or_filename(fp, img_bytes, mode='wb')
