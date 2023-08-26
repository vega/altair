from .html import spec_to_html
from ._importers import import_vl_convert
import struct


def spec_to_mimebundle(
    spec,
    format,
    mode=None,
    vega_version=None,
    vegaembed_version=None,
    vegalite_version=None,
    engine=None,
    **kwargs,
):
    """Convert a vega-lite specification to a mimebundle

    The mimebundle type is controlled by the ``format`` argument, which can be
    one of the following ['html', 'json', 'png', 'svg', 'pdf', 'vega', 'vega-lite']

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    format : string {'html', 'json', 'png', 'svg', 'pdf', 'vega', 'vega-lite'}
        the file format to be saved.
    mode : string {'vega-lite'}
        The rendering mode.
    vega_version : string
        The version of vega.js to use
    vegaembed_version : string
        The version of vegaembed.js to use
    vegalite_version : string
        The version of vegalite.js to use. Only required if mode=='vega-lite'
    engine: string {'vl-convert', 'altair_saver'}
        the conversion engine to use for 'png', 'svg', 'pdf', and 'vega' formats
    **kwargs :
        Additional arguments will be passed to the generating function

    Returns
    -------
    output : dict
        a mime-bundle representing the image

    Note
    ----
    The png, svg, pdf, and vega outputs require the altair_saver package
    """
    # Local import to avoid circular ImportError
    from altair.utils.display import compile_with_vegafusion, using_vegafusion

    if mode != "vega-lite":
        raise ValueError("mode must be 'vega-lite'")

    if using_vegafusion():
        spec = compile_with_vegafusion(spec)
        mode = "vega"

    if format in ["png", "svg", "pdf", "vega"]:
        return _spec_to_mimebundle_with_engine(
            spec, format, mode, engine=engine, **kwargs
        )
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
        if vegalite_version is None:
            raise ValueError("Must specify vegalite_version")
        return {"application/vnd.vegalite.v{}+json".format(vegalite_version[0]): spec}
    if format == "json":
        return {"application/json": spec}
    raise ValueError(
        "format must be one of "
        "['html', 'json', 'png', 'svg', 'pdf', 'vega', 'vega-lite']"
    )


def _spec_to_mimebundle_with_engine(spec, format, mode, **kwargs):
    """Helper for Vega-Lite to mimebundle conversions that require an engine

    Parameters
    ----------
    spec : dict
        a dictionary representing a vega-lite plot spec
    format : string {'png', 'svg', 'pdf', 'vega'}
        the format of the mimebundle to be returned
    mode : string {'vega-lite', 'vega'}
        The rendering mode.
    engine: string {'vl-convert', 'altair_saver'}
        the conversion engine to use
    **kwargs :
        Additional arguments will be passed to the conversion function
    """
    # Normalize the engine string (if any) by lower casing
    # and removing underscores and hyphens
    engine = kwargs.pop("engine", None)
    normalized_engine = _validate_normalize_engine(engine, format)

    if normalized_engine == "vlconvert":
        vlc = import_vl_convert()
        from ..vegalite import SCHEMA_VERSION

        # Compute VlConvert's vl_version string (of the form 'v5_2')
        # from SCHEMA_VERSION (of the form 'v5.2.0')
        vl_version = "_".join(SCHEMA_VERSION.split(".")[:2])
        if format == "vega":
            if mode == "vega":
                vg = spec
            else:
                vg = vlc.vegalite_to_vega(spec, vl_version=vl_version)
            return {"application/vnd.vega.v5+json": vg}
        elif format == "svg":
            if mode == "vega":
                svg = vlc.vega_to_svg(spec)
            else:
                svg = vlc.vegalite_to_svg(spec, vl_version=vl_version)
            return {"image/svg+xml": svg}
        elif format == "png":
            scale = kwargs.get("scale_factor", 1)
            # The default ppi for a PNG file is 72
            default_ppi = 72
            ppi = kwargs.get("ppi", default_ppi)
            if mode == "vega":
                png = vlc.vega_to_png(
                    spec,
                    scale=scale,
                    ppi=ppi,
                )
            else:
                png = vlc.vegalite_to_png(
                    spec,
                    vl_version=vl_version,
                    scale=scale,
                    ppi=ppi,
                )
            factor = ppi / default_ppi
            w, h = _pngxy(png)
            return {"image/png": png}, {
                "image/png": {"width": w / factor, "height": h / factor}
            }
        else:
            # This should be validated above
            # but raise exception for the sake of future development
            raise ValueError("Unexpected format {fmt!r}".format(fmt=format))
    elif normalized_engine == "altairsaver":
        import altair_saver

        return altair_saver.render(spec, format, mode=mode, **kwargs)
    else:
        # This should be validated above
        # but raise exception for the sake of future development
        raise ValueError(
            "Unexpected normalized_engine {eng!r}".format(eng=normalized_engine)
        )


def _validate_normalize_engine(engine, format):
    """Helper to validate and normalize the user-provided engine

    engine : {None, 'vl-convert', 'altair_saver'}
        the user-provided engine string
    format : string {'png', 'svg', 'pdf', 'vega'}
        the format of the mimebundle to be returned
    """
    # Try to import vl_convert
    try:
        vlc = import_vl_convert()
    except ImportError:
        vlc = None

    # Try to import altair_saver
    try:
        import altair_saver
    except ImportError:
        altair_saver = None

    # Normalize engine string by lower casing and removing underscores and hyphens
    normalized_engine = (
        None if engine is None else engine.lower().replace("-", "").replace("_", "")
    )

    # Validate or infer default value of normalized_engine
    if normalized_engine == "vlconvert":
        if vlc is None:
            raise ValueError(
                "The 'vl-convert' conversion engine requires the vl-convert-python package"
            )
        if format == "pdf":
            raise ValueError(
                "The 'vl-convert' conversion engine does not support the {fmt!r} format.\n"
                "Use the 'altair_saver' engine instead".format(fmt=format)
            )
    elif normalized_engine == "altairsaver":
        if altair_saver is None:
            raise ValueError(
                "The 'altair_saver' conversion engine requires the altair_saver package"
            )
    elif normalized_engine is None:
        if vlc is not None and format != "pdf":
            normalized_engine = "vlconvert"
        elif altair_saver is not None:
            normalized_engine = "altairsaver"
        else:
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
    else:
        raise ValueError(
            "Invalid conversion engine {engine!r}. Expected one of {valid!r}".format(
                engine=engine, valid=("vl-convert", "altair_saver")
            )
        )
    return normalized_engine


def _pngxy(data):
    """read the (width, height) from a PNG header

    Taken from IPython.display
    """
    ihdr = data.index(b"IHDR")
    # next 8 bytes are width/height
    return struct.unpack(">ii", data[ihdr + 4 : ihdr + 12])
