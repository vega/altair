from types import ModuleType
from packaging.version import Version


def import_vegafusion() -> ModuleType:
    min_vf_version = "1.4.0"
    try:
        import vegafusion as vf  # type: ignore

        if Version(vf.__version__) < Version(min_vf_version):
            raise ImportError(
                f"The vegafusion package must be version {min_vf_version} or greater. "
                f"Found version {vf.__version__}"
            )
        return vf
    except ImportError as err:
        raise ImportError(
            'The "vegafusion" data transformer and chart.transformed_data feature requires\n'
            f"version {min_vf_version} or greater of the 'vegafusion-python-embed' and 'vegafusion' packages.\n"
            "These can be installed with pip using:\n"
            f'    pip install "vegafusion[embed]>={min_vf_version}"\n'
            "Or with conda using:\n"
            f'    conda install -c conda-forge "vegafusion-python-embed>={min_vf_version}" '
            f'"vegafusion>={min_vf_version}"\n\n'
            f"ImportError: {err.args[0]}"
        ) from err


def import_vl_convert() -> ModuleType:
    min_vlc_version = "0.12.0"
    try:
        import vl_convert as vlc

        if Version(vlc.__version__) < Version(min_vlc_version):
            raise ImportError(
                f"The vl-convert-python package must be version {min_vlc_version} or greater. "
                f"Found version {vlc.__version__}"
            )
        return vlc
    except ImportError as err:
        raise ImportError(
            f"The vl-convert Vega-Lite compiler and image export feature requires\n"
            f"version {min_vlc_version} or greater of the 'vl-convert-python' package. \n"
            f"This can be installed with pip using:\n"
            f'   pip install "vl-convert-python>={min_vlc_version}"\n'
            "or conda:\n"
            f'   conda install -c conda-forge "vl-convert-python>={min_vlc_version}"\n\n'
            f"ImportError: {err.args[0]}"
        ) from err


def import_pyarrow_interchange() -> ModuleType:
    min_pa_version = "11.0.0"
    try:
        import pyarrow as pa

        if Version(pa.__version__) < Version(min_pa_version):
            raise ImportError(
                f"The pyarrow package must be version {min_pa_version} or greater. "
                f"Found version {pa.__version__}"
            )
        import pyarrow.interchange as pi

        return pi
    except ImportError as err:
        raise ImportError(
            f"Usage of the DataFrame Interchange Protocol requires\n"
            f"version {min_pa_version} or greater of the pyarrow package. \n"
            f"This can be installed with pip using:\n"
            f'   pip install "pyarrow>={min_pa_version}"\n'
            "or conda:\n"
            f'   conda install -c conda-forge "pyarrow>={min_pa_version}"\n\n'
            f"ImportError: {err.args[0]}"
        ) from err


def pyarrow_available() -> bool:
    try:
        import_pyarrow_interchange()
        return True
    except ImportError:
        return False
