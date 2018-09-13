import base64

from .headless import compile_spec
from .html import spec_to_html


def spec_to_mimebundle(spec, format, mode=None,
                       vega_version=None,
                       vegaembed_version=None,
                       vegalite_version=None,
                       **kwargs):
    """Convert a vega/vega-lite specification to a mimebundle

    The mimebundle type is controlled by the ``format`` argument, which can be
    one of the following ['png', 'svg', 'vega', 'vega-lite', 'html', 'json']

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    format : string {'png', 'svg', 'vega', 'vega-lite', 'html', 'json'}
        the file format to be saved.
    mode : string {'vega', 'vega-lite'}
        The rendering mode.
    vega_version : string
        The version of vega.js to use
    vegaembed_version : string
        The version of vegaembed.js to use
    vegalite_version : string
        The version of vegalite.js to use. Only required if mode=='vega-lite'
    **kwargs :
        Additional arguments will be passed to the generating function

    Returns
    -------
    output : dict
        a mime-bundle representing the image

    Note
    ----
    The png, svg, and vega outputs require the pillow and selenium Python modules
    to be installed. Additionally they requires either chromedriver
    (if webdriver=='chrome') or geckodriver (if webdriver=='firefox')
    """
    if mode not in ['vega', 'vega-lite']:
        raise ValueError("mode must be either 'vega' or 'vega-lite'")

    if mode == 'vega' and format == 'vega':
        if vega_version is None:
            raise ValueError("Must specify vega_version")
        return {'application/vnd.vega.v{}+json'.format(vega_version[0]): spec}
    elif format in ['png', 'svg', 'vega']:
        render = compile_spec(spec, format=format, mode=mode,
                              vega_version=vega_version,
                              vegaembed_version=vegaembed_version,
                              vegalite_version=vegalite_version, **kwargs)
        if format == 'png':
            render = base64.b64decode(render.split(',', 1)[1].encode())
            return {'image/png': render}
        elif format == 'svg':
            return {'image/svg+xml': render}
        elif format == 'vega':
            assert mode == 'vega-lite'  # TODO: handle vega->vega conversion more gracefully
            return {'application/vnd.vega.v{}+json'.format(vega_version[0]): render}
    elif format == 'html':
        html = spec_to_html(spec, mode=mode,
                            vega_version=vega_version,
                            vegaembed_version=vegaembed_version,
                            vegalite_version=vegalite_version, **kwargs)
        return {'text/html': html}
    elif format == 'vega-lite':
        assert mode == 'vega-lite'  # sanity check: should never be False
        if mode == 'vega':
            raise ValueError("Cannot convert a vega spec to vegalite")
        if vegalite_version is None:
            raise ValueError("Must specify vegalite_version")
        return {'application/vnd.vegalite.v{}+json'.format(vegalite_version[0]): spec}
    elif format == 'json':
        return {'application/json': spec}
    else:
        raise ValueError("format must be one of "
                         "['png', 'svg', 'vega', 'vega-lite', 'html', 'json']")
