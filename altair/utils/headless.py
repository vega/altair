"""
Utilities that use selenium + chrome headless to save figures
"""

import contextlib
import os
import tempfile


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
        var mode = arguments[1];
        var scaleFactor = arguments[2];
        var done = arguments[3];

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
            .toCanvas(scaleFactor)
            .then(function(canvas){return canvas.toDataURL('image/png');})
            .then(done)
            .catch(function(err) { console.error(err); });
        """,
'svg': """
        var spec = arguments[0];
        var mode = arguments[1];
        var scaleFactor = arguments[2];
        var done = arguments[3];

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
            .toSVG(scaleFactor)
            .then(done)
            .catch(function(err) { console.error(err); });
        """,
'vega': """
        var spec = arguments[0];
        var mode = arguments[1];
        var done = arguments[3];

        if(mode === 'vega-lite'){
          // compile vega-lite to vega
          const compiled = vl.compile(spec);
          spec = compiled.spec;
        }

        done(spec);
        """}


def compile_spec(spec, format, mode,
                 vega_version, vegaembed_version, vegalite_version,
                 scale_factor=1, driver_timeout=20, webdriver='chrome'):
    # TODO: detect & use local Jupyter caches of JS packages?

    # selenium is an optional dependency, so import it here
    try:
        import selenium.webdriver
    except ImportError:
        raise ImportError("selenium package is required "
                          "for saving chart as {}".format(format))

    if format not in ['png', 'svg', 'vega']:
        raise NotImplementedError("format must be 'svg', 'png' or 'vega'")

    if mode not in ['vega', 'vega-lite']:
        raise ValueError("mode must be either 'vega' or 'vega-lite'")

    if vega_version is None:
        raise ValueError("must specify vega_version")

    if vegaembed_version is None:
        raise ValueError("must specify vegaembed_version")

    if mode == 'vega-lite' and vegalite_version is None:
        raise ValueError("must specify vega-lite version")

    if webdriver == 'chrome':
        webdriver_class = selenium.webdriver.Chrome
        webdriver_options_class = selenium.webdriver.chrome.options.Options
    elif webdriver == 'firefox':
        webdriver_class = selenium.webdriver.Firefox
        webdriver_options_class = selenium.webdriver.firefox.options.Options
    else:
        raise ValueError("webdriver must be 'chrome' or 'firefox'")

    html = HTML_TEMPLATE.format(vega_version=vega_version,
                                vegalite_version=vegalite_version,
                                vegaembed_version=vegaembed_version)

    webdriver_options = webdriver_options_class()
    webdriver_options.add_argument("--headless")

    if issubclass(webdriver_class, selenium.webdriver.Chrome):
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
                                 "chart as {}".format(format))
            return driver.execute_async_script(EXTRACT_CODE[format],
                                               spec, mode, scale_factor)
    finally:
        driver.close()
