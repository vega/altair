from .html import spec_to_html


def spec_to_mimebundle(
    spec,
    format,
    mode=None,
    vega_version=None,
    vegaembed_version=None,
    vegalite_version=None,
    **kwargs,
):
    """Convert a vega/vega-lite specification to a mimebundle

    The mimebundle type is controlled by the ``format`` argument, which can be
    one of the following ['html', 'json', 'png', 'svg', 'pdf', 'vega', 'vega-lite']

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    format : string {'html', 'json', 'png', 'svg', 'pdf', 'vega', 'vega-lite'}
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
    The png, svg, pdf, and vega outputs require the altair_saver package
    to be installed.
    """
    if mode not in ["vega", "vega-lite"]:
        raise ValueError("mode must be either 'vega' or 'vega-lite'")

    if mode == "vega" and format == "vega":
        if vega_version is None:
            raise ValueError("Must specify vega_version")
        return {"application/vnd.vega.v{}+json".format(vega_version[0]): spec}
    if format in ["png", "svg", "pdf", "vega"]:
        if format in ["png", "svg", "vega"]:
            try:
                import vl_convert as vlc
                from ..vegalite import SCHEMA_VERSION

                # Compute VlConvert's vl_version string (of the form 'v5_2')
                # from SCHEMA_VERSION (of the form 'v5.2.0')
                vl_version = "_".join(SCHEMA_VERSION.split(".")[:2])

                if format == "vega":
                    vg = vlc.vegalite_to_vega(spec, vl_version=vl_version)
                    return {"application/vnd.vega.v5+json": vg}
                elif format == "svg":
                    svg = vlc.vegalite_to_svg(spec, vl_version=vl_version)
                    return {"image/svg+xml": svg}
                elif format == "png":
                    png = vlc.vegalite_to_png(
                        spec,
                        vl_version=vl_version,
                        scale=kwargs.get("scale_factor", 1.0),
                    )
                    return {"image/png": png}
            except ImportError:
                # Continue and try to use altair_saver below
                pass
        try:
            import altair_saver
        except ImportError:
            if format == "pdf":
                raise ValueError(
                    "Saving charts in {fmt!r} format requires the altair_saver package: "
                    "see http://github.com/altair-viz/altair_saver/".format(fmt=format)
                )
            else:
                raise ValueError(
                    "Saving charts in {fmt!r} format requires the vl-convert-python or altair_saver package: "
                    "see http://github.com/altair-viz/altair_saver/".format(fmt=format)
                )
        return altair_saver.render(spec, format, mode=mode, **kwargs)
    if format == "html":
        html = spec_to_html(
            spec,
            mode=mode,
            vega_version=vega_version,
            vegaembed_version=vegaembed_version,
            vegalite_version=vegalite_version,
            **kwargs,
        )
        return {"text/html": html}
    if format == "vega-lite":
        assert mode == "vega-lite"  # sanity check: should never be False
        if mode == "vega":
            raise ValueError("Cannot convert a vega spec to vegalite")
        if vegalite_version is None:
            raise ValueError("Must specify vegalite_version")
        return {"application/vnd.vegalite.v{}+json".format(vegalite_version[0]): spec}
    if format == "json":
        return {"application/json": spec}
    raise ValueError(
        "format must be one of "
        "['html', 'json', 'png', 'svg', 'pdf', 'vega', 'vega-lite']"
    )
