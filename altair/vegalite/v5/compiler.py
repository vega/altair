import sys

from ...utils.compiler import VegaLiteCompilerRegistry

from typing import Final


ENTRY_POINT_GROUP: Final = "altair.vegalite.v5.vegalite_compiler"
vegalite_compilers = VegaLiteCompilerRegistry(entry_point_group=ENTRY_POINT_GROUP)


def vl_convert_compiler(vegalite_spec: dict) -> dict:
    """
    Vega-Lite to Vega compiler that uses vl-convert
    """
    from . import SCHEMA_VERSION

    try:
        import vl_convert as vlc
    except ImportError as err:
        raise ImportError(
            "The vl-convert Vega-Lite compiler requires the vl-convert-python package"
        ) from err

    # Compute vl-convert's vl_version string (of the form 'v5_8')
    # from SCHEMA_VERSION (of the form 'v5.8.0')
    vl_version = "_".join(SCHEMA_VERSION.split(".")[:2])
    return vlc.vegalite_to_vega(vegalite_spec, vl_version=vl_version)


vegalite_compilers.register("vl-convert", vl_convert_compiler)
vegalite_compilers.enable("vl-convert")
