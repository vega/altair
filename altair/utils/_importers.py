from __future__ import annotations

from importlib.metadata import version as importlib_version
from typing import TYPE_CHECKING

from packaging.version import Version

from altair.utils.schemapi import VERSIONS

if TYPE_CHECKING:
    from types import ModuleType


def import_vegafusion() -> ModuleType:
    min_version = VERSIONS["vegafusion"]
    try:
        version = importlib_version("vegafusion")
        if Version(version) < Version(min_version):
            msg = (
                f"The vegafusion package must be version {min_version} or greater. "
                f"Found version {version}"
            )
            raise RuntimeError(msg)
        import vegafusion as vf

        return vf
    except ImportError as err:
        msg = (
            'The "vegafusion" data transformer and chart.transformed_data feature requires\n'
            f"version {min_version} or greater of the 'vegafusion' package.\n"
            "This can be installed with pip using:\n"
            f'    pip install "vegafusion>={min_version}"\n'
            "or conda:\n"
            f'    conda install -c conda-forge "vegafusion>={min_version}"\n\n'
            f"ImportError: {err.args[0]}"
        )
        raise ImportError(msg) from err


def import_vl_convert() -> ModuleType:
    min_version = VERSIONS["vl-convert-python"]
    try:
        version = importlib_version("vl-convert-python")
        if Version(version) < Version(min_version):
            msg = (
                f"The vl-convert-python package must be version {min_version} or greater. "
                f"Found version {version}"
            )
            raise RuntimeError(msg)
        import vl_convert as vlc

        return vlc
    except ImportError as err:
        msg = (
            f"The vl-convert Vega-Lite compiler and file export feature requires\n"
            f"version {min_version} or greater of the 'vl-convert-python' package. \n"
            f"This can be installed with pip using:\n"
            f'   pip install "vl-convert-python>={min_version}"\n'
            "or conda:\n"
            f'   conda install -c conda-forge "vl-convert-python>={min_version}"\n\n'
            f"ImportError: {err.args[0]}"
        )
        raise ImportError(msg) from err


def vl_version_for_vl_convert() -> str:
    from altair.vegalite import SCHEMA_VERSION

    # Compute VlConvert's vl_version string (of the form 'v5_2')
    # from SCHEMA_VERSION (of the form 'v5.2.0')
    return "_".join(SCHEMA_VERSION.split(".")[:2])


def import_pyarrow_interchange() -> ModuleType:
    min_version = "11.0.0"
    try:
        version = importlib_version("pyarrow")

        if Version(version) < Version(min_version):
            msg = (
                f"The pyarrow package must be version {min_version} or greater. "
                f"Found version {version}"
            )
            raise RuntimeError(msg)
        import pyarrow.interchange as pi

        return pi
    except ImportError as err:
        msg = (
            f"Usage of the DataFrame Interchange Protocol requires\n"
            f"version {min_version} or greater of the pyarrow package. \n"
            f"This can be installed with pip using:\n"
            f'   pip install "pyarrow>={min_version}"\n'
            "or conda:\n"
            f'   conda install -c conda-forge "pyarrow>={min_version}"\n\n'
            f"ImportError: {err.args[0]}"
        )
        raise ImportError(msg) from err


def pyarrow_available() -> bool:
    try:
        import_pyarrow_interchange()
        return True
    except (ImportError, RuntimeError):
        return False
