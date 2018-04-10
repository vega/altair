"""
Utilities that use selenium + chrome headless to save figures
"""

import base64
import contextlib
import os
import tempfile

try:
    from selenium import webdriver
except ImportError:
    webdriver = None


@contextlib.contextmanager
def temporary_filename(**kwargs):
    """Create and clean-up a temporary file

    Arguments are the same as those passed to tempfile.mkstemp

    We could use tempfile.NamedTemporaryFile here, but that causes issues on
    windows (see https://bugs.python.org/issue14243).
    """
    filedescriptor, filename = tempfile.mkstemp(**kwargs)
    os.close(filedescriptor)

    try:
        yield filename
    finally:
        if os.path.exists(filename):
            os.remove(filename)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Embedding Vega-Lite</title>
  <script src="https://cdn.jsdelivr.net/npm/vega@{vega_version}"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@{vegalite_version}"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@{vegaembed_version}"></script>
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


def spec_to_image_mimebundle(spec, format, mode,
                             vega_version,
                             vegaembed_version,
                             vegalite_version=None,
                             driver_timeout=10,
                             webdriver_class=None):
    """Conver a vega/vega-lite specification to a PNG/SVG image

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    format : string {'png' | 'svg'}
        the file format to be saved.
    mode : string {'vega' | 'vega-lite'}
        The rendering mode.
    vega_version : string
        For html output, the version of vega.js to use
    vegalite_version : string
        For html output, the version of vegalite.js to use
    vegaembed_version : string
        For html output, the version of vegaembed.js to use
    driver_timeout : int (optional)
        the number of seconds to wait for page load before raising an
        error (default: 10)
    webdriver_class : Type[Union[webdriver.Chrome, webdriver.Firefox]]
        Webdriver to use (default: webdriver.Chrome).

    Returns
    -------
    output : dict
        a mime-bundle representing the image

    Note
    ----
    This requires the pillow, selenium, and chromedriver or geckodriver
    packages to be installed.
    """
    # TODO: allow package versions to be specified
    # TODO: detect & use local Jupyter caches of JS packages?
    if format not in ['png', 'svg']:
        raise NotImplementedError("format must be 'svg' and 'png'")
    if mode not in ['vega', 'vega-lite']:
        raise ValueError("mode must be 'vega' or 'vega-lite'")

    if mode == 'vega-lite' and vegalite_version is None:
        raise ValueError("must specify vega-lite version")

    if webdriver is None:
        raise ImportError("selenium package is required "
                          "for saving chart as {0}".format(format))
    if webdriver_class is None:
        webdriver_class = webdriver.Chrome
    if issubclass(webdriver_class, webdriver.Chrome):
        webdriver_options_class = webdriver.chrome.options.Options
    elif issubclass(webdriver_class, webdriver.Firefox):
        webdriver_options_class = webdriver.firefox.options.Options
    else:
        raise ValueError("Only Chrome and Firefox webdrivers are supported")

    html = HTML_TEMPLATE.format(vega_version=vega_version,
                                vegalite_version=vegalite_version,
                                vegaembed_version=vegaembed_version)
    
    webdriver_options = webdriver_options_class()
    webdriver_options.add_argument("--headless")

    if issubclass(webdriver_class, webdriver.Chrome):
        # for linux/osx root user, need to add --no-sandbox option.
        # since geteuid doesn't exist on windows, we don't check it
        if hasattr(os, 'geteuid') and (os.geteuid() == 0):
            webdriver_options.add_argument('--no-sandbox')

    driver = webdriver_class(options=webdriver_options)

    try:
        driver.set_page_load_timeout(driver_timeout)

        with temporary_filename(suffix='.html') as htmlfile:
            with open(htmlfile, 'w') as f:
                f.write(html)
            driver.get("file://" + htmlfile)
            online = driver.execute_script("return navigator.onLine")
            if not online:
                raise ValueError("Internet connection required for saving "
                                 "chart as {0}".format(format))
            render = driver.execute_async_script(EXTRACT_CODE[format],
                                                 spec, mode)
    finally:
        driver.close()

    if format == 'png':
        return {'image/png': base64.decodebytes(render.split(',', 1)[1].encode())}
    elif format == 'svg':
        return {'image/svg+xml': render}
